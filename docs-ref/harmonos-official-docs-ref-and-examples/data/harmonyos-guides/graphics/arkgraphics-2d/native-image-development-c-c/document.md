# Native Image Development (C/C++)

#### Overview

NativeImage is a module that **binds surfaces to OpenGL external textures**. It indicates the consumer of a graphics queue. You can use the NativeImage API to receive and use Buffer and associate Buffer with the bound OpenGL external texture.

NativeImage is commonly used in the following scenarios:

-   Use the native image APIs to create an **OH\_NativeImage** instance as the consumer and obtain the corresponding **OHNativeWindow** instance (functioning as the producer). Use the native window APIs to fill in and flush the buffer, and then use the native image APIs to update the buffer content to an OpenGL ES texture.
    
    The native image module must be used together with the native window, native buffer, EGL, and GLES3 modules.
    

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_NativeImage\_Create (uint32\_t textureId, uint32\_t textureTarget) | Creates an **OH\_NativeImage** instance to be associated with the specified OpenGL ES texture ID and target. This function must be used in pair with **OH\_NativeImage\_Destroy**. Otherwise, memory leak occurs. |
| OH\_NativeImage\_AcquireNativeWindow (OH\_NativeImage \*image) | Obtains an **OHNativeWindow** instance associated with an **OH\_NativeImage** instance. It is unnecessary to manually release this **OHNativeWindow** with **OH\_NativeWindow\_DestroyNativeWindow** as it will be automatically freed upon calling **OH\_NativeImage\_Destroy**. Failing to do so could result in memory access violations after the memory has been freed, which might cause the application to crash. |
| OH\_NativeImage\_AttachContext (OH\_NativeImage \*image, uint32\_t textureId) | Attaches an **OH\_NativeImage** instance to the current OpenGL ES context. The OpenGL ES texture will be bound to an **GL\_TEXTURE\_EXTERNAL\_OES** instance and updated through the **OH\_NativeImage** instance. |
| OH\_NativeImage\_DetachContext (OH\_NativeImage \*image) | Detaches an **OH\_NativeImage** instance from the current OpenGL ES context. |
| OH\_NativeImage\_UpdateSurfaceImage (OH\_NativeImage \*image) | Updates the OpenGL ES texture associated with the latest frame through an **OH\_NativeImage** instance. |
| OH\_NativeImage\_GetTimestamp (OH\_NativeImage \*image) | Obtains the timestamp of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function. |
| OH\_NativeImage\_GetTransformMatrixV2 (OH\_NativeImage \*image, float matrix\[16\]) | Obtains the transformation matrix of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function. |
| OH\_NativeImage\_Destroy (OH\_NativeImage \*\*image) | Destroys an **OH\_NativeImage** instance created by calling **OH\_NativeImage\_Create**. After the instance is destroyed, the pointer to it is assigned **NULL**. |

For details about the APIs, see [native\_image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativeimage).

#### How to Develop

The following steps describe how to use the native Image APIs to create an **OH\_NativeImage** instance as the consumer and update the data to a OpenGL external texture.

**Adding Dynamic Link Libraries**

Add the following library file to the **CMakeLists.txt** file.

libEGL.so
libGLESv3.so
libnative\_image.so
libnative\_window.so
libnative\_buffer.so

**Including Header Files**

#include <iostream>
#include <string>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES3/gl3.h>
#include <GLES2/gl2ext.h>
#include <sys/mman.h>
#include <native\_image/native\_image.h>
#include <native\_window/external\_window.h>
#include <native\_buffer/native\_buffer.h>

1.  Initialize the EGL environment.
    
    The following is an example of the code for initializing the EGL environment. For details about how to use the XComponent module, see [XComponent Development Guidelines](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md).
    
    bool ImageRender::InitEGL(EGLNativeWindowType window, uint64\_t width, uint64\_t height)
    {
        window\_ = window;
        width\_ = width;
        height\_ = height;
    
        if (!InitializeEGLDisplay() || !ChooseEGLConfig() || !CreateEGLContext() || !CreateEGLSurface()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to initialize EGL");
            return false;
        }
    
        if (!MakeCurrentContext()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to make EGL context current");
            return false;
        }
    
        if (!CompileAndLinkShaders()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to compile and link shaders");
            return false;
        }
    
        UpdateViewport();
    
        return true;
    }
    
    // ···
    bool ImageRender::InitializeEGLDisplay()
    {
        display\_ = eglGetDisplay(EGL\_DEFAULT\_DISPLAY);
        if (display\_ == EGL\_NO\_DISPLAY) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to get EGL display");
            return false;
        }
    
        if (!eglInitialize(display\_, nullptr, nullptr)) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to initialize EGL");
            return false;
        }
    
        return true;
    }
    
    bool ImageRender::ChooseEGLConfig()
    {
        const EGLint attribs\[\] = {
            EGL\_RENDERABLE\_TYPE, EGL\_OPENGL\_ES2\_BIT,
            EGL\_SURFACE\_TYPE, EGL\_WINDOW\_BIT,
            EGL\_RED\_SIZE, 8,
            EGL\_GREEN\_SIZE, 8,
            EGL\_BLUE\_SIZE, 8,
            EGL\_ALPHA\_SIZE, 8,
            EGL\_NONE
        };
    
        EGLint numConfigs;
        if (!eglChooseConfig(display\_, attribs, &config\_, 1, &numConfigs) || numConfigs == 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to choose EGL config");
            return false;
        }
        return true;
    }
    
    bool ImageRender::CreateEGLContext()
    {
        const EGLint contextAttribs\[\] = { EGL\_CONTEXT\_CLIENT\_VERSION, 2, EGL\_NONE };
        context\_ = eglCreateContext(display\_, config\_, EGL\_NO\_CONTEXT, contextAttribs);
        if (context\_ == EGL\_NO\_CONTEXT) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to create EGL context");
            return false;
        }
        return true;
    }
    
    bool ImageRender::CreateEGLSurface()
    {
        surface\_ = eglCreateWindowSurface(display\_, config\_, window\_, nullptr);
        if (surface\_ == EGL\_NO\_SURFACE) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to create EGL surface");
            return false;
        }
        return true;
    }
    
    bool ImageRender::MakeCurrentContext()
    {
        if (!eglMakeCurrent(display\_, surface\_, surface\_, context\_)) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "ImageRender", "Failed to make EGL context current");
            return false;
        }
        return true;
    }
    
    void ImageRender::UpdateViewport()
    {
        glViewport(0, 0, static\_cast<GLsizei>(width\_), static\_cast<GLsizei>(height\_));
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "ImageRender",
                    "Viewport updated to %{public}llu x %{public}llu", width\_, height\_);
    }
    
    bool ImageRender::CompileAndLinkShaders()
    {
        GLuint vertexShader = CompileShader(GL\_VERTEX\_SHADER, g\_vertexShaderSource);
        if (vertexShader == 0) {
            return false;
        }
    
        GLuint fragmentShader = CompileShader(GL\_FRAGMENT\_SHADER, g\_fragmentShaderSource);
        if (fragmentShader == 0) {
            glDeleteShader(vertexShader);
            return false;
        }
    
        shaderProgram\_ = glCreateProgram();
        glAttachShader(shaderProgram\_, vertexShader);
        glAttachShader(shaderProgram\_, fragmentShader);
        glLinkProgram(shaderProgram\_);
    
        GLint linked;
        glGetProgramiv(shaderProgram\_, GL\_LINK\_STATUS, &linked);
        if (!linked) {
            PrintProgramLinkError(shaderProgram\_);
            glDeleteProgram(shaderProgram\_);
            glDeleteShader(vertexShader);
            glDeleteShader(fragmentShader);
            return false;
        }
    
        glUseProgram(shaderProgram\_);
    
        positionAttrib\_ = glGetAttribLocation(shaderProgram\_, "aPosition");
        texCoordAttrib\_ = glGetAttribLocation(shaderProgram\_, "aTexCoord");
        textureUniform\_ = glGetUniformLocation(shaderProgram\_, "uTexture");
    
        glDeleteShader(vertexShader);
        glDeleteShader(fragmentShader);
    
        return true;
    }
    
    void ImageRender::PrintProgramLinkError(GLuint program)
    {
        GLint infoLen = 0;
        glGetProgramiv(program, GL\_INFO\_LOG\_LENGTH, &infoLen);
        if (infoLen > 1) {
            std::unique\_ptr<char\[\]> infoLog = std::make\_unique<char\[\]>(infoLen);
            glGetProgramInfoLog(program, infoLen, nullptr, infoLog.get());
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                        "ImageRender", "Error linking program: %{public}s", infoLog.get());
        }
    }
    
2.  Create an **OH\_NativeImage** instance.
    
    glGenTextures(1, &nativeImageTexId\_);
    // ···
    nativeImage\_ = OH\_NativeImage\_Create(nativeImageTexId\_, GL\_TEXTURE\_EXTERNAL\_OES);
    
3.  Obtain the **OHNativeWindow** instance that functions as the producer.
    
    nativeWindow\_ = OH\_NativeImage\_AcquireNativeWindow(image);
    
4.  Set the width and height of the **OHNativeWindow** instance.
    
    int32\_t result = OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow\_, SET\_BUFFER\_GEOMETRY,
        static\_cast<int32\_t>(width\_), static\_cast<int32\_t>(height\_));
    if (result != SUCCESS) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to set buffer geometry.");
        return false;
    }
    
5.  Write the produced content to the **OHNativeWindowBuffer**.
    
    1.  Obtain an **OHNativeWindowBuffer** instance from the **NativeWindow** instance.
        
        OHNativeWindowBuffer \*buffer = nullptr;
        int releaseFenceFd = INVALID\_FD;
        int32\_t result = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow\_, &buffer, &releaseFenceFd);
        if (result != SUCCESS || buffer == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                        "OHNativeRender", "Failed to request buffer, ret : %{public}d.", result);
            return;
        }
        // ···
        BufferHandle \*handle = OH\_NativeWindow\_GetBufferHandleFromNative(buffer);
        
    2.  Write the produced content to the **OHNativeWindowBuffer**.
        
        // Use mmap to obtain the virtual address.
        void \*mappedAddr = mmap(nullptr, handle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, handle->fd, 0);
        if (mappedAddr == MAP\_FAILED) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to mmap buffer.");
            return;
        }
        
        // Obtain the pixel pointer.
        uint32\_t \*pixel = static\_cast<uint32\_t \*>(mappedAddr);
        
        // Call the encapsulated function to draw gradients.
        DrawGradient(pixel, handle->stride / BYTES\_PER\_PIXEL, height\_);
        
        // Unmap the memory.
        result = munmap(mappedAddr, handle->size);
        if (result == FAILURE) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "OHNativeRender", "Failed to munmap buffer.");
        }
        // ···
        void OHNativeRender::DrawGradient(uint32\_t\* pixel, uint64\_t width, uint64\_t height)
        {
            static double time = 0.0;
            time += ANIMATION\_SPEED\_INCREMENT;
            double offset = (sin(time) + MAX\_INTENSITY) / INTENSITY\_MULTIPLIER;
        
            // Arrow parameters
            const int arrowSize = std::min(width, height) / ARROW\_SIZE\_DIVISOR;
            const int arrowX = width / ARROW\_SIZE\_DIVISOR;
            const int arrowY = height / ARROW\_SIZE\_DIVISOR;
            const int stemWidth = arrowSize / STEM\_WIDTH\_DIVISOR;
            const int headWidth = arrowSize / HEAD\_WIDTH\_DIVISOR;
            const int headLength = arrowSize / HEAD\_LENGTH\_DIVISOR;
            const int stemStart = arrowX - arrowSize / ARROW\_SIZE\_DIVISOR;
            const int stemEnd = arrowX + arrowSize / ARROW\_SIZE\_DIVISOR - headLength;
        
            for (uint64\_t y = 0; y < height; y++) {
                for (uint64\_t x = 0; x < width; x++) {
                    double normalizedX = static\_cast<double>(x) / static\_cast<double>(width - 1);
                    bool isArrow = false;
        
                    if ((x >= stemStart && x <= stemEnd && y >= arrowY - stemWidth \* HEAD\_SLOPE\_MULTIPLIER &&
                        y <= arrowY + stemWidth \* HEAD\_SLOPE\_MULTIPLIER) || (x >= stemEnd && x <= stemEnd + headLength &&
                        fabs(static\_cast<int>(y - arrowY)) <= (headWidth \* HEAD\_SLOPE\_MULTIPLIER) \*
                        (1.0 - static\_cast<double>(x - stemEnd) / headLength))) {
                        isArrow = true;
                    }
        
                    uint8\_t red = static\_cast<uint8\_t>((1.0 - normalizedX) \* MAX\_COLOR\_VALUE);
                    uint8\_t blue = static\_cast<uint8\_t>(normalizedX \* MAX\_COLOR\_VALUE);
                    uint8\_t green = 0;
                    uint8\_t alpha = MAX\_COLOR\_VALUE;
                    if (isArrow) {
                        red = green = blue = MAX\_COLOR\_VALUE;
                    }
                    double intensity = fabs(normalizedX - offset);
                    intensity = MAX\_INTENSITY - std::min(INTENSITY\_MULTIPLIER \* intensity, INTENSITY\_LIMIT);
                    intensity = std::max(intensity, MIN\_INTENSITY);
        
                    red = static\_cast<uint8\_t>(red \* intensity);
                    green = static\_cast<uint8\_t>(green \* intensity);
                    blue = static\_cast<uint8\_t>(blue \* intensity);
        
                    \*pixel++ = (static\_cast<uint32\_t>(alpha) << ALPHA\_SHIFT) | (static\_cast<uint32\_t>(red) << RED\_SHIFT) |
                        (static\_cast<uint32\_t>(green) << GREEN\_SHIFT) | (static\_cast<uint32\_t>(blue) << BLUE\_SHIFT);
                }
            }
        }
        
    3.  Flush the **OHNativeWindowBuffer** to the **NativeWindow**.
        
            // Set the refresh area.
            Region region{nullptr, 0};
            // Submit the buffer to the consumer.
            result = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow\_, buffer, NO\_FENCE, region);
            if (result != SUCCESS) {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                            "OHNativeRender", "Failed to flush buffer, result : %{public}d.", result);
            }
        
6.  Update the content to the OpenGL texture.
    
    int32\_t ret = OH\_NativeImage\_UpdateSurfaceImage(nativeImage\_);
    if (ret != 0) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine",
                    "OH\_NativeImage\_UpdateSurfaceImage failed, ret: %{public}d, texId: %{public}u",
                    ret, nativeImageTexId\_);
        return;
    }
    
    UpdateTextureMatrix();
    if (imageRender\_) {
        imageRender\_->Render();
    } else {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine", "ImageRender is null");
    }
    // ···
    
    void RenderEngine::UpdateTextureMatrix()
    {
        float matrix\[16\];
        int32\_t ret = OH\_NativeImage\_GetTransformMatrixV2(nativeImage\_, matrix);
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "RenderEngine",
                        "OH\_NativeImage\_GetTransformMatrix failed, ret: %{public}d", ret);
            return;
        }
        imageRender\_->SetTransformMatrix(matrix);
    }
    
7.  Detach the **OH\_NativeImage** from the current OpenGL texture and attach it to a new external texture.
    
    // Detach an OH\_NativeImage instance from the current OpenGL ES context.
    OH\_NativeImage\_DetachContext(nativeImage\_);
    // \[Start nativeimage\_create\]
    glGenTextures(1, &nativeImageTexId\_);
    // \[StartExclude nativeimage\_create\]
    glBindTexture(GL\_TEXTURE\_EXTERNAL\_OES, nativeImageTexId\_);
    // ···
    int ret = OH\_NativeImage\_AttachContext(nativeImage\_, nativeImageTexId\_);
    
8.  Destroy the **OH\_NativeImage** instance when it is no longer needed.
    
    OH\_NativeImage\_Destroy(&nativeImage\_);
