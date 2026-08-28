# Vulkan External Memory Development

#### When to Use

The VK\_OHOS\_external\_memory extension is designed for zero-copy memory sharing between the GPU Vulkan environment and HarmonyOS OHNativeBuffer.

This extension allows you to import OHNativeBuffers created by HarmonyOS or other components (such as Camera, RenderService, video decoders, and OHNativeWindow) as Vulkan memory (and bind it to VkImage or VkBuffer).

This enables efficient sharing of video frames, camera outputs, and image decoder outputs between the producer and Vulkan rendering/computation ends, avoiding additional copying or pixel conversion.

This guide introduces how to achieve zero-copy between video decoders and renderers by directly importing OHNativeBuffers output by the decoder into Vulkan.

#### Available APIs

## Structs

| Name | Description |
| :-- | :-- |
| [VkNativeBufferPropertiesOHOS](../../vulkan-extensions/vknativebufferpropertiesohos/document.md) | Describes the properties of the NativeBuffer. |
| [VkNativeBufferFormatPropertiesOHOS](../../vulkan-extensions/vknativebufferformatpropertiesohos/document.md) | Describes the format properties of the NativeBuffer. |
| [VkImportNativeBufferInfoOHOS](../../vulkan-extensions/vkimportnativebufferinfoohos/document.md) | Describes the pointer to an OH\_NativeBuffer struct. |
| [VkMemoryGetNativeBufferInfoOHOS](../../vulkan-extensions/vkmemorygetnativebufferinfoohos/document.md) | Used to obtain an OH\_NativeBuffer from the Vulkan memory. |
| [VkExternalFormatOHOS](../../vulkan-extensions/vkexternalformatohos/document.md) | Describes an externally defined format. |

## Functions

| Name | Description |
| :-- | :-- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [vkGetNativeBufferPropertiesOHOS](../../vulkan-extensions/vulkan-ohos-h/document.md#vkgetnativebufferpropertiesohos) (VkDevice device, const struct OH\_NativeBuffer \*buffer, [VkNativeBufferPropertiesOHOS](../../vulkan-extensions/vknativebufferpropertiesohos/document.md) \*pProperties) | Obtains the properties of an OH\_NativeBuffer instance. |

#### How to Develop

The following steps illustrate how to import the OHNativeBuffer output by the video decoder as Vulkan memory and bind it to VkImage or VkBuffer.

1.  Launch the rendering child thread, initialize the Vulkan environment, dynamically load libvulkan.so, and load the pointers of the Vulkan base functions.
    
    void VulkanRenderThread::ThreadMainLoop() {
        threadId\_ = std::this\_thread::get\_id();
        if (!InitRenderContext()) {
            return;
        }
        if (!InitNativeVsync()) {
            return;
        }
        if (!CreateNativeImage()) {
            return;
        }
        while (running\_) {
            {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderThread", "Waiting for Vsync.");
                std::unique\_lock<std::mutex> Lock(wakeUpMutex\_);
                wakeUpCond\_.wait(Lock, \[this\]() { return wakeup\_ || vSyncCnt\_ > 0 || availableFrameCnt\_ > 0; });
                wakeup\_ = false;
                vSyncCnt\_--;
                (void)OH\_NativeVSync\_RequestFrame(nativeVsync\_, &VulkanRenderThread::OnVsync, this);
            }
    
            std::vector<VulkanRenderTask> tasks;
            {
                std::lock\_guard<std::mutex> lock(taskMutex\_);
                tasks.swap(tasks\_);
            }
            for (const auto &task : tasks) {
                task(\*vulkanRenderContext\_);
            }
            if (availableFrameCnt\_ <= 0) {
                continue;
            }
            DrawImage();
            availableFrameCnt\_--;
        }
    }
    
    Dynamically load libvulkan.so, and load the pointers of the Vulkan base functions.
    
    // Dynamically load Vulkan library and base function pointers.
    bool LoadVulkanLibrary() {
        // Load the Vulkan library.
        constexpr char \*path = "libvulkan.so";
        dlerror();
        g\_libVulkan = dlopen(path, RTLD\_NOW | RTLD\_LOCAL);
        if (!g\_libVulkan) {
            OH\_LOG\_ERROR(LOG\_APP, "Failed to load vulkan Library, %{public}s", dlerror());
            return false;
        }
    
        // Load the base function pointers.
        vkEnumerateInstanceExtensionProperties = reinterpret\_cast<PFN\_vkEnumerateInstanceExtensionProperties>(
            dlsym(g\_libVulkan, "vkEnumerateInstanceExtensionProperties"));
        vkEnumerateInstanceLayerProperties = reinterpret\_cast<PFN\_vkEnumerateInstanceLayerProperties>(
            dlsym(g\_libVulkan, "vkEnumerateInstanceLayerProperties"));
        vkCreateInstance = reinterpret\_cast<PFN\_vkCreateInstance>(dlsym(g\_libVulkan, "vkCreateInstance"));
        vkGetInstanceProcAddr = reinterpret\_cast<PFN\_vkGetInstanceProcAddr>(dlsym(g\_libVulkan, "vkGetInstanceProcAddr"));
        vkGetDeviceProcAddr = reinterpret\_cast<PFN\_vkGetDeviceProcAddr>(dlsym(g\_libVulkan, "vkGetDeviceProcAddr"));
    
        return true;
    }
    
2.  Create a NativeImage object as the consumer of OHNativeBuffer, and obtain the corresponding NativeWindow object from the NativeImage object. Pass the NativeWindow handle to the video codec as the producer of OHNativeBuffer to generate video frame content.
    
    bool VulkanRenderThread::CreateNativeImage() {
        nativeImage\_ = OH\_ConsumerSurface\_Create();
        if (nativeImage\_ == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderThread", "OH\_NativeImage\_Create failed.");
            return false;
        }
        int ret = 0;
        {
            std::lock\_guard<std::mutex> Lock(nativeImageSurfaceIdMutex\_);
            nativeImageWindow\_ = OH\_NativeImage\_AcquireNativeWindow(nativeImage\_);
            ret = OH\_NativeImage\_GetSurfaceId(nativeImage\_, &nativeImageSurfaceId\_);
        }
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderThread",
                        "OH\_NativeImage\_GetSurfaceId failed, ret is %{public}d.", ret);
            return false;
        }
    
        nativeImageFrameAvailableListener\_.context = this;
        nativeImageFrameAvailableListener\_.onFrameAvailable = &VulkanRenderThread::OnNativeImageFrameAvailable;
        ret = OH\_NativeImage\_SetOnFrameAvailableListener(nativeImage\_, nativeImageFrameAvailableListener\_);
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderThread",
                        "OH\_NativeImage\_SetonFrameAvailableListener failed, ret is %{public}d.", ret);
            return false;
        }
        return true;
    }
    
3.  Obtain the NativeWindow object of the XComponent, and create a VkSurface in the Vulkan environment based on the NativeWindow object for drawing and displaying content.
    
    void VulkanRenderThread::UpdateNativeWindow(void \*window, uint64\_t width, uint64\_t height) {
        OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_PRINT\_DOMAIN, "RenderThread", "UpdateNativeWindow.");
        auto nativeWindow = reinterpret\_cast<OHNativeWindow \*>(window);
        PostTask(\[this, nativeWindow, width, height\](VulkanRender &renderContext) {
            if (nativeWindow\_ != nativeWindow) {
                if (nativeWindow\_ != nullptr) {
                    (void)OH\_NativeWindow\_NativeObjectUnreference(nativeWindow\_);
                }
                nativeWindow\_ = nativeWindow;
                if (nativeWindow\_ != nullptr) {
                    (void)OH\_NativeWindow\_NativeObjectReference(nativeWindow\_);
                }
            }
            if (nativeWindow\_ != nullptr) {
                vulkanRenderContext\_->SetupWindow(nativeWindow\_);
            }
        });
    }
    
    Update the Vulkan initialization context, including the Vulkan instance, selecting the physical device, and creating the rendering pipeline.
    
    void VulkanRender::SetupWindow(NativeWindow \*nativeWindow) {
        nativeWindow\_ = nativeWindow;
        CreateInstance();
        vkExample::utils::LoadVulkanFunctions(instance);
        CreateSurface();
        PickPhysicalDevice();
        CreateLogicalDevice();
        vkExample::utils::LoadVulkanFunctions(device);
    
        createSwapChain();
        createRenderPass();
        createFrameBuffersAndImages();
        createVertexBuffer();
        createUniformBuffer();
        deviceInfoInitialized = true;
    }
    
    Call vkCreateSurfaceOHOS() to create a VkSurface object.
    
    bool VulkanRender::CreateSurface() {
        VkSurfaceCreateInfoOHOS surfaceCreateInfo{};
        surfaceCreateInfo.sType = VK\_STRUCTURE\_TYPE\_SURFACE\_CREATE\_INFO\_OHOS;
        if (nativeWindow\_ == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "nativeWindow\_ is nulptr.Failed to create surface !");
            return false;
        }
        surfaceCreateInfo.window = nativeWindow\_;
        surfaceCreateInfo.flags = 0;
        surfaceCreateInfo.pNext = nullptr;
        bool res = CheckResult(vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, nullptr, &surface));
        return res;
    }
    
4.  Initialize the video decoding environment, including initializing the demuxer and decoder.
    
    napi\_value PluginRender::StartPlayer(napi\_env env, napi\_callback\_info info)
    {
        SampleInfo sampleInfo;
        size\_t argc = 4;
        napi\_value args\[4\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_get\_value\_int32(env, args\[0\], &sampleInfo.inputFd);
        napi\_get\_value\_int64(env, args\[1\], &sampleInfo.inputFileOffset);
        napi\_get\_value\_int64(env, args\[2\], &sampleInfo.inputFileSize);
        size\_t length = 0;
        napi\_status status = napi\_get\_value\_string\_utf8(env, args\[3\], nullptr, 0, &length);
        char\* buf = new char\[length + 1\];
        std::memset(buf, 0, length + 1);
        status = napi\_get\_value\_string\_utf8(env, args\[3\], buf, length + 1, &length);
        std::string type = buf;
        PluginRender \*render = PluginRender::GetInstance(type);
        if (render != nullptr) {
            if (type == "Vulkan") {
                sampleInfo.window = render->vulkanRenderThread\_->GetNativeImageWindow();
            } else {
                sampleInfo.window = render->nativeWindow;
            }
        }
        int32\_t ret = Player::GetInstance().Init(sampleInfo);
        if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
            return nullptr;
        }
        Player::GetInstance().Start();
        return nullptr;
    }
    
5.  Start the decoder, decoder input thread, and decoder output thread.
    
    int32\_t Player::Start() {
        std::unique\_lock<std::mutex> lock(mutex\_);
        int32\_t ret;
        if (isStarted\_ || demuxer\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Already started.");
            return AVCODEC\_SAMPLE\_ERR\_ERROR;
        }
        
        if (videoDecContext\_) {
            ret = videoDecoder\_->Start();
            if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Video Decoder start failed");
                lock.unlock();
                StartRelease();
                return AVCODEC\_SAMPLE\_ERR\_ERROR;
            }
            isStarted\_ = true;
            videoDecInputThread\_ = std::make\_unique<std::thread>(&Player::VideoDecInputThread, this);
            videoDecOutputThread\_ = std::make\_unique<std::thread>(&Player::VideoDecOutputThread, this);
    
            if (videoDecInputThread\_ == nullptr || videoDecOutputThread\_ == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "Create thread failed");
                lock.unlock();
                StartRelease();
                return AVCODEC\_SAMPLE\_ERR\_ERROR;
            }
        }
    
        OH\_LOG\_INFO(LOG\_APP, "Succeed");
        doneCond\_.notify\_all();
        return AVCODEC\_SAMPLE\_ERR\_OK;
    }
    
6.  In the decoder input thread, read video data using the demuxer and pass it to the decoder.
    
    void Player::VideoDecInputThread() {
        while (true) {
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Decoder input thread out");
                break;;
            }
            
            std::unique\_lock<std::mutex> lock(videoDecContext\_->inputMutex);
            bool condRet = videoDecContext\_->inputCond.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !videoDecContext\_->inputBufferInfoQueue.empty(); });
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Work done, thread out");
                break;
            }
            if (videoDecContext\_->inputBufferInfoQueue.empty()) {
                OH\_LOG\_ERROR(LOG\_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
                continue;
            }
    
            CodecBufferInfo bufferInfo = videoDecContext\_->inputBufferInfoQueue.front();
            videoDecContext\_->inputBufferInfoQueue.pop();
            videoDecContext\_->inputFrameCount++;
            lock.unlock();
    
            demuxer\_->ReadSample(demuxer\_->GetVideoTrackId(), reinterpret\_cast<OH\_AVBuffer \*>(bufferInfo.buffer),
                                bufferInfo.attr);
    
            int32\_t ret = videoDecoder\_->PushInputBuffer(bufferInfo);
            if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Push data failed, thread out");
                break;
            }
    
            if (bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                OH\_LOG\_ERROR(LOG\_APP, "Catch EOS, thread out");
                break;
            }
        }
    }
    
7.  In the decoder output thread, submit the decoded video to the output surface.
    
    void Player::VideoDecOutputThread() {
        sampleInfo\_.frameInterval = MICROSECOND / sampleInfo\_.frameRate;
        while (true) {
            thread\_local auto lastPushTime = std::chrono::system\_clock::now();
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Decoder output thread out");
                break;
            }
            std::unique\_lock<std::mutex> lock(videoDecContext\_->outputMutex);
            bool condRet = videoDecContext\_->outputCond.wait\_for(
                lock, 5s, \[this\]() { return !isStarted\_ || !videoDecContext\_->outputBufferInfoQueue.empty(); });
            if (!isStarted\_) {
                OH\_LOG\_ERROR(LOG\_APP, "Decoder output thread out");
                break;
            }
            if (videoDecContext\_->outputBufferInfoQueue.empty()) {
                OH\_LOG\_ERROR(LOG\_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
                continue;
            }
    
            CodecBufferInfo bufferInfo = videoDecContext\_->outputBufferInfoQueue.front();
            videoDecContext\_->outputBufferInfoQueue.pop();
            if (bufferInfo.attr.flags & AVCODEC\_BUFFER\_FLAGS\_EOS) {
                OH\_LOG\_ERROR(LOG\_APP, "Catch EOS, thread out");
                break;
            }
            videoDecContext\_->outputFrameCount++;
            OH\_LOG\_INFO(LOG\_APP,"Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}ld",
                                videoDecContext\_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                bufferInfo.attr.pts);
            lock.unlock();
    
            int32\_t ret = videoDecoder\_->FreeOutputBuffer(bufferInfo.bufferIndex, true);
            if (ret != AVCODEC\_SAMPLE\_ERR\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Decoder output thread out");
                break;
            }
    
            std::this\_thread::sleep\_until(lastPushTime + std::chrono::microseconds(sampleInfo\_.frameInterval));
            lastPushTime = std::chrono::system\_clock::now();
        }
        StartRelease();
    }
    
8.  After NativeImage has available data, call OH\_NativeImage\_AcquireNativeWindowBuffer() to obtain video data and call OH\_NativeBuffer\_FromNativeWindowBuffer() to convert the type of NativeBuffer.
    
    void VulkanRenderThread::DrawImage() {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "VulkanRenderThread", "DrawImage.");
        int ret;
        OHNativeWindowBuffer \*inBuffer = nullptr;
        OH\_NativeBuffer \*nativeBuffer = nullptr;
        int32\_t fenceFd1 = -1;
        ret = OH\_NativeImage\_AcquireNativeWindowBuffer(nativeImage\_, &inBuffer, &fenceFd1);
        ret = OH\_NativeWindow\_NativeObjectReference(inBuffer);
        ret = OH\_NativeBuffer\_FromNativeWindowBuffer(inBuffer, &nativeBuffer);
        if (nativeBuffer == nullptr) {
            OH\_NativeWindow\_NativeObjectUnreference(inBuffer);
            OH\_NativeImage\_ReleaseNativeWindowBuffer(nativeImage\_, inBuffer, -1);
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "VulkanRenderThread", "nativeBuffer is null.");
            return;
        }
        ret = OH\_NativeImage\_GetTransformMatrix(nativeImage\_, matrix\_);
        int32\_t transformTmp = 0;
        ComputeTransform(transformTmp, matrix\_);
        vulkanRenderContext\_->hwBufferToTexture(nativeBuffer, matrix\_);
        vulkanRenderContext\_->render();
        if (lastInBuffer\_ != nullptr) {
            OH\_NativeWindow\_NativeObjectUnreference(lastInBuffer\_);
            OH\_NativeImage\_ReleaseNativeWindowBuffer(nativeImage\_, lastInBuffer\_, -1);
        }
        lastInBuffer\_ = inBuffer;
    }
    
9.  Create a corresponding ImageView in Vulkan for rendering and display based on NativeBuffer, and create a sampler of the corresponding format to sample the YUV format image into an RGBA image for correct rendering and display.
    
    void VulkanRender::hwBufferToTexture(OH\_NativeBuffer \*buffer, float transformMatrix\[16\]) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "VulkanRenderThread", "hwBufferToTexture.");
        if (!deviceInfoInitialized) {
            return;
        }
        UniformBufferObject ubo{};
        memcpy(ubo.mvp, transformMatrix, sizeof(float) \* 16);
        memcpy(buffersInfo.uniformBufferMapped, &ubo, sizeof(ubo));
        VkNativeBufferFormatPropertiesOHOS nbFormatProps = {
            .sType = VK\_STRUCTURE\_TYPE\_NATIVE\_BUFFER\_FORMAT\_PROPERTIES\_OHOS,
            .pNext = nullptr
        };
        VkNativeBufferPropertiesOHOS nbProps = {.sType = VK\_STRUCTURE\_TYPE\_NATIVE\_BUFFER\_PROPERTIES\_OHOS,
                                                .pNext = &nbFormatProps};
        CheckResult(vkGetNativeBufferPropertiesOHOS(device, buffer, &nbProps));
    
        VkImportNativeBufferInfoOHOS importBufferInfo = {
            .sType = VK\_STRUCTURE\_TYPE\_IMPORT\_NATIVE\_BUFFER\_INFO\_OHOS,
            .pNext = nullptr,
            .buffer = buffer
        };
    
        VkMemoryDedicatedAllocateInfo dedicatedAllocateInfo = {
            .sType = VK\_STRUCTURE\_TYPE\_MEMORY\_DEDICATED\_ALLOCATE\_INFO,
            .pNext = &importBufferInfo,
            .image = VK\_NULL\_HANDLE, // It will be set later.
            .buffer = VK\_NULL\_HANDLE
        };
    
        VkPhysicalDeviceMemoryProperties physicalDeviceMemProps;
        uint32\_t foundTypeIndex = 0;
        vkGetPhysicalDeviceMemoryProperties(gpuDevice, &physicalDeviceMemProps);
        uint32\_t memTypeCnt = physicalDeviceMemProps.memoryTypeCount;
        for (uint32\_t i = 0; i < memTypeCnt; ++i) {
            if (nbProps.memoryTypeBits & (1 << i)) {
                const VkPhysicalDeviceMemoryProperties &pdmp = physicalDeviceMemProps;
                uint32\_t supportedFLags = pdmp.memoryTypes\[i\].propertyFlags & VK\_MEMORY\_PROPERTY\_DEVICE\_LOCAL\_BIT;
                if (supportedFLags == VK\_MEMORY\_PROPERTY\_DEVICE\_LOCAL\_BIT) {
                    foundTypeIndex = i;
                    break;
                }
            }
        }
    
        VkMemoryAllocateInfo allocInfo{
            .sType = VK\_STRUCTURE\_TYPE\_MEMORY\_ALLOCATE\_INFO,
            .pNext = &dedicatedAllocateInfo,
            .allocationSize = nbProps.allocationSize,
            .memoryTypeIndex = 0 // The memory type is assigned in the next step.
        };
    
        mapMemoryTypeToIndex(nbProps.memoryTypeBits, VK\_MEMORY\_PROPERTY\_DEVICE\_LOCAL\_BIT, &allocInfo.memoryTypeIndex);
        VkExternalFormatOHOS externalFormat;
        externalFormat.sType = VK\_STRUCTURE\_TYPE\_EXTERNAL\_FORMAT\_OHOS;
        externalFormat.pNext = nullptr;
        externalFormat.externalFormat = 0;
        if (nbFormatProps.format == VK\_FORMAT\_UNDEFINED) {
            externalFormat.externalFormat = nbFormatProps.externalFormat;
        }
    
        VkExternalMemoryImageCreateInfo externalMemoryImageInfo = {
            .sType = VK\_STRUCTURE\_TYPE\_EXTERNAL\_MEMORY\_IMAGE\_CREATE\_INFO,
            .pNext = &externalFormat,
            .handleTypes = VK\_EXTERNAL\_MEMORY\_HANDLE\_TYPE\_OHOS\_NATIVE\_BUFFER\_BIT\_OHOS,
        };
    
        VkImageUsageFlags usageFlags = VK\_IMAGE\_USAGE\_SAMPLED\_BIT;
        if (nbFormatProps.format != VK\_FORMAT\_UNDEFINED) {
            usageFlags = usageFlags | VK\_IMAGE\_USAGE\_TRANSFER\_SRC\_BIT | VK\_IMAGE\_USAGE\_TRANSFER\_DST\_BIT |
                        VK\_IMAGE\_USAGE\_COLOR\_ATTACHMENT\_BIT | VK\_IMAGE\_USAGE\_INPUT\_ATTACHMENT\_BIT;
        }
        OH\_NativeBuffer\_Config config;
        OH\_NativeBuffer\_GetConfig(buffer, &config);
        VkImageCreateInfo image\_create\_info = {
            .sType = VK\_STRUCTURE\_TYPE\_IMAGE\_CREATE\_INFO,
            .pNext = &externalMemoryImageInfo,
            .flags = 0,
            .imageType = VK\_IMAGE\_TYPE\_2D,
            .format = nbFormatProps.format,
            .extent = {static\_cast<uint32\_t>(config.width), static\_cast<uint32\_t>(config.height), 1},
            .mipLevels = 1,
            .arrayLayers = 1,
            .samples = VK\_SAMPLE\_COUNT\_1\_BIT,
            .tiling = VK\_IMAGE\_TILING\_OPTIMAL,
            .usage = usageFlags,
            .sharingMode = VK\_SHARING\_MODE\_EXCLUSIVE,
            .queueFamilyIndexCount = 1,
            .pQueueFamilyIndices = &queueFamilyIndex\_,
            // VK\_IMAGE\_LAYOUT\_UNDEFINED is mandatory when external memory is used.
            .initialLayout = VK\_IMAGE\_LAYOUT\_UNDEFINED
        };
    
        CheckResult(vkCreateImage(device, &image\_create\_info, nullptr, &externalTextureImage));
        dedicatedAllocateInfo.image = externalTextureImage;
        CheckResult(vkAllocateMemory(device, &allocInfo, nullptr, &externalTextureMemory));
        CheckResult(vkBindImageMemory(device, externalTextureImage, externalTextureMemory, 0));
    
        VkSamplerYcbcrConversionCreateInfo ycbcrCreateInfo = {
            .sType = VK\_STRUCTURE\_TYPE\_SAMPLER\_YCBCR\_CONVERSION\_CREATE\_INFO,
            .ycbcrRange = nbFormatProps.suggestedYcbcrRange,
            .components = nbFormatProps.samplerYcbcrConversionComponents,
            .xChromaOffset = nbFormatProps.suggestedXChromaOffset,
            .yChromaOffset = nbFormatProps.suggestedYChromaOffset,
            .chromaFilter = VK\_FILTER\_LINEAR,
            .forceExplicitReconstruction = false
        };
    
        if (nbFormatProps.format == VK\_FORMAT\_UNDEFINED) {
            ycbcrCreateInfo.pNext = &externalFormat;
            ycbcrCreateInfo.format = VK\_FORMAT\_UNDEFINED;
            ycbcrCreateInfo.ycbcrModel = nbFormatProps.suggestedYcbcrModel;
        }
    
        CheckResult(
            vkCreateSamplerYcbcrConversion(device, &ycbcrCreateInfo, nullptr, &externalTextureInfo.ycbcrConversion));
    
        VkSamplerYcbcrConversionInfo convInfoWrap = {
            .sType = VK\_STRUCTURE\_TYPE\_SAMPLER\_YCBCR\_CONVERSION\_INFO,
            .conversion = externalTextureInfo.ycbcrConversion,
            .pNext = nullptr,
        };
    
        VkImageViewCreateInfo view = {
            .sType = VK\_STRUCTURE\_TYPE\_IMAGE\_VIEW\_CREATE\_INFO,
            .pNext = &convInfoWrap,
            .flags = 0,
            .image = externalTextureImage,
            .viewType = VK\_IMAGE\_VIEW\_TYPE\_2D,
            .format = nbFormatProps.format,
            .components =
                {
                    VK\_COMPONENT\_SWIZZLE\_IDENTITY,
                    VK\_COMPONENT\_SWIZZLE\_IDENTITY,
                    VK\_COMPONENT\_SWIZZLE\_IDENTITY,
                    VK\_COMPONENT\_SWIZZLE\_IDENTITY
                },
            .subresourceRange = {VK\_IMAGE\_ASPECT\_COLOR\_BIT, 0, 1, 0, 1},
        };
        CheckResult(vkCreateImageView(device, &view, nullptr, &externalTextureInfo.view));
    
        // Create a sampler.
        const VkSamplerCreateInfo sampler = {
            .sType = VK\_STRUCTURE\_TYPE\_SAMPLER\_CREATE\_INFO,
            .pNext = &convInfoWrap,
            .magFilter = VK\_FILTER\_NEAREST,
            .minFilter = VK\_FILTER\_NEAREST,
            .mipmapMode = VK\_SAMPLER\_MIPMAP\_MODE\_NEAREST,
            .addressModeU = VK\_SAMPLER\_ADDRESS\_MODE\_CLAMP\_TO\_EDGE,
            .addressModeV = VK\_SAMPLER\_ADDRESS\_MODE\_CLAMP\_TO\_EDGE,
            .addressModeW = VK\_SAMPLER\_ADDRESS\_MODE\_CLAMP\_TO\_EDGE,
            .mipLodBias = 0.0f,
            .compareEnable = VK\_FALSE,
            .anisotropyEnable = VK\_FALSE,
            .maxAnisotropy = 1,
            .compareOp = VK\_COMPARE\_OP\_NEVER,
            .minLod = 0.0f,
            .maxLod = 0.0f,
            .borderColor = VK\_BORDER\_COLOR\_FLOAT\_OPAQUE\_WHITE,
            .unnormalizedCoordinates = VK\_FALSE
        };
        CheckResult(vkCreateSampler(device, &sampler, nullptr, &externalTextureInfo.sampler));
    
        createDescriptorSetLayout();
        createDescriptorSet();
    
        VkDescriptorImageInfo imageInfo = {
            .sampler = externalTextureInfo.sampler,
            .imageView = externalTextureInfo.view,
            .imageLayout = VK\_IMAGE\_LAYOUT\_SHADER\_READ\_ONLY\_OPTIMAL
        };
    
        VkDescriptorBufferInfo bufferInfo = {
            .buffer = buffersInfo.uniformBuf, .offset = 0, .range = sizeof(UniformBufferObject)};
        VkWriteDescriptorSet bufferWrite = {.sType = VK\_STRUCTURE\_TYPE\_WRITE\_DESCRIPTOR\_SET,
                                            .dstSet = gfxPipelineInfo.descSet,
                                            .dstBinding = 0,
                                            .dstArrayElement = 0,
                                            .descriptorCount = 1,
                                            .descriptorType = VK\_DESCRIPTOR\_TYPE\_UNIFORM\_BUFFER,
                                            .pImageInfo = nullptr,
                                            .pBufferInfo = &bufferInfo,
                                            .pTexelBufferView = nullptr};
        VkWriteDescriptorSet imageWrite = {.sType = VK\_STRUCTURE\_TYPE\_WRITE\_DESCRIPTOR\_SET,
                                        .dstSet = gfxPipelineInfo.descSet,
                                        .dstBinding = 1,
                                        .dstArrayElement = 0,
                                        .descriptorCount = 1,
                                        .descriptorType = VK\_DESCRIPTOR\_TYPE\_COMBINED\_IMAGE\_SAMPLER,
                                        .pImageInfo = &imageInfo,
                                        .pBufferInfo = nullptr,
                                        .pTexelBufferView = nullptr};
        gfxPipelineInfo.descWrites\[0\] = bufferWrite;
        gfxPipelineInfo.descWrites\[1\] = imageWrite;
        vkUpdateDescriptorSets(device, 2, gfxPipelineInfo.descWrites, 0, nullptr);
    
        createGraphicsPipeline();
        createOtherStaff();
    
        recordCommandBuffer();
        OH\_LOG\_INFO(LOG\_APP, "hwBufferToTexture end");
    }
