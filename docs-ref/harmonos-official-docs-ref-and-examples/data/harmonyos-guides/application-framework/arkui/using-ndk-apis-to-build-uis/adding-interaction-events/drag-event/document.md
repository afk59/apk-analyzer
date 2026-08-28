# Drag Event

The ArkUI framework provides a set of drag event APIs to help you implement drag-and-drop functionality.These events include [NODE\_ON\_PRE\_DRAG](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), [NODE\_ON\_DRAG\_START](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), [NODE\_ON\_DROP](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), [NODE\_ON\_DRAG\_ENTER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), [NODE\_ON\_DRAG\_MOVE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), [NODE\_ON\_DRAG\_LEAVE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype), and [NODE\_ON\_DRAG\_END](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype). These events are triggered at different stages of the drag operation, allowing you to perform specific actions and manage the drag interaction as needed.

#### Basic Drag Implementation

In ArkUI, you can implement the drag-and-drop functionality using C and C++ by calling C APIs. The following provides step-by-step instructions using the **Image** component as an example, along with key points to keep in mind during development.

1.  Set a component draggable.
    
    Initialize **nodeAPI** using the [OH\_ArkUI\_GetModuleInterface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface) API. Node operations, such as creating a node, must be performed through **nodeAPI**.
    
    ArkUI\_NativeNodeAPI\_1 \*nativeNodeAPI = nullptr;
    OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, nativeNodeAPI);
    nodeAPI = nativeNodeAPI;
    
    Create an **Image** node, use [OH\_ArkUI\_SetNodeDraggable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_setnodedraggable) to set the node to be draggable, and set other related attributes.
    
    dragImage2 = nodeAPI->createNode(ARKUI\_NODE\_IMAGE);
    SetId(dragImage2, "dragImage");
    SetCommonAttribute(dragImage2, 140.0f, 140.0f, 0xFFFFFFFF, 5.0f);
    // Replace src/main/resources/base/media/seagull.png with the image resource file you use.
    SetImageSrc(dragImage2, "/resources/base/media/seagull.png");
    OH\_ArkUI\_SetNodeDraggable(dragImage2, true);
    nodeAPI->registerNodeEvent(dragImage2, NODE\_ON\_DRAG\_START, 1, nullptr);
    
    #define DEFAULT\_WIDTH 200.0
    // Set the node brightness.
    void SetWidth(ArkUI\_NodeHandle &node, float width = DEFAULT\_WIDTH)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue widthValue\[\] = {width};
        ArkUI\_AttributeItem widthItem = {widthValue, 1};
        nodeAPI->setAttribute(node, NODE\_WIDTH, &widthItem);
    }
    
    #define DEFAULT\_HEIGHT 200.0
    // Set the node height.
    void SetHeight(ArkUI\_NodeHandle &node, float height = DEFAULT\_HEIGHT)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue heightValue\[\] = {height};
        ArkUI\_AttributeItem heightItem = {heightValue, 1};
        nodeAPI->setAttribute(node, NODE\_HEIGHT, &heightItem);
    }
    
    #define DEFAULT\_BG\_COLOR 0xFFFFFFFF
    // Set the background color of the node.
    void SetBackgroundColor(ArkUI\_NodeHandle &node, uint32\_t color = DEFAULT\_BG\_COLOR)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue colorValue\[\] = {{.u32 = color}};
        ArkUI\_AttributeItem colorItem = {colorValue, 1};
        nodeAPI->setAttribute(node, NODE\_BACKGROUND\_COLOR, &colorItem);
    }
    
    #define DEFAULT\_MARGIN 5.0
    // Set the margin of the node.
    void SetMargin(ArkUI\_NodeHandle &node, float margin = DEFAULT\_MARGIN)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue marginValue\[\] = {margin};
        ArkUI\_AttributeItem marginItem = {marginValue, 1};
        nodeAPI->setAttribute(node, NODE\_MARGIN, &marginItem);
    }
    
    // Set tags for a Button node.
    void SetButtonLabel(ArkUI\_NodeHandle &node, const char \*label)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_AttributeItem NODE\_Button\_SRC\_Item = {.string = label};
        nodeAPI->setAttribute(node, NODE\_BUTTON\_LABEL, &NODE\_Button\_SRC\_Item);
    }
    
    // Set the node identifier.
    void SetId(ArkUI\_NodeHandle &node, const char \*id)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_AttributeItem idItem = {.string = id};
        nodeAPI->setAttribute(node, NODE\_ID, &idItem);
    }
    
    #define DEFAULT\_BORDER\_WIDTH 0.0
    // Set the border width for the node.
    void SetBorderWidth(ArkUI\_NodeHandle &node, float width = DEFAULT\_BORDER\_WIDTH)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue borderWidthValue\[\] = {width};
        ArkUI\_AttributeItem borderWidthItem = {borderWidthValue, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_WIDTH, &borderWidthItem);
    }
    
    #define DEFAULT\_BORDER\_COLOR 0xFF000000
    // Set the border color of the node.
    void SetBorderColor(ArkUI\_NodeHandle &node, uint32\_t color = DEFAULT\_BORDER\_COLOR)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue borderColorValue\[\] = {{.u32 = color}};
        ArkUI\_AttributeItem borderColorItem = {borderColorValue, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_COLOR, &borderColorItem);
    }
    
    // Set common node attributes, such as the width, height, background color, margin, and border style.
    void SetCommonAttribute(ArkUI\_NodeHandle &node, float width = DEFAULT\_WIDTH, float height = DEFAULT\_HEIGHT,
                            unsigned int color = DEFAULT\_BG\_COLOR, float margin = DEFAULT\_MARGIN)
    {
        SetWidth(node, width);
        SetHeight(node, height);
        SetBackgroundColor(node, color);
        SetMargin(node, margin);
        SetBorderWidth(node, DEFAULT\_BORDER\_WIDTH);
        SetBorderColor(node);
    }
    
    void SetImageSrc(ArkUI\_NodeHandle &node, const char \*src)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_AttributeItem imageSrcItem = {.string = src};
        nodeAPI->setAttribute(node, NODE\_IMAGE\_SRC, &imageSrcItem);
    }
    
2.  Customize the drag preview and background image.
    
    Create a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_createpixelmap) object and set its width, height, and other properties. Set [ArkUI\_DragPreviewOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption) for the **Image** node to customize the rounded corners and badges of the drag preview.
    
    // Create a PixelMap object.
    uint8\_t data\[960000\];
    size\_t dataSize = 960000;
    for (int i = 0; i < dataSize; i++) {
        data\[i\] = i + 1;
    }
    // Create a parameter structure instance and set parameters.
    OH\_Pixelmap\_InitializationOptions \*createOpts;
    OH\_PixelmapInitializationOptions\_Create(&createOpts);
    OH\_PixelmapInitializationOptions\_SetWidth(createOpts, 200U);
    OH\_PixelmapInitializationOptions\_SetHeight(createOpts, 200U);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOpts, PIXEL\_FORMAT\_BGRA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);
    // Define the custom drag preview.
    OH\_PixelmapNative \*pixelmap = nullptr;
    OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &pixelmap);
    OH\_PixelmapNative\_Opacity(pixelmap, 0.1f);
    OH\_ArkUI\_SetNodeDragPreview(node, pixelmap);
    // Set the drag preview configuration options.
    auto \*previewOptionsText = OH\_ArkUI\_CreateDragPreviewOption();
    OH\_ArkUI\_DragPreviewOption\_SetScaleMode(previewOptionsText, ARKUI\_DRAG\_PREVIEW\_SCALE\_DISABLED);
    OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled(previewOptionsText, true);
    OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber(previewOptionsText, 10U);
    OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled(previewOptionsText, true);
    OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled(previewOptionsText, true);
    int returnValue = OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled(previewOptionsText, true);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "Manager",
        "dragTest DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled returnValue = %{public}d",
        returnValue);
    OH\_ArkUI\_SetNodeDragPreviewOption(node, previewOptionsText);
    
3.  Set related events.
    
    Use a unified callback to handle events. Distinguish between different events using [eventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype).
    
    nodeAPI->addNodeEventReceiver(dragNode, \[\](ArkUI\_NodeEvent \*event) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "RegisterNodeEventFirstReceiver called");
        auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
        auto preDragStatus = OH\_ArkUI\_NodeEvent\_GetPreDragStatus(event);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "eventType = %{public}d, preDragStatus = %{public}d", eventType, preDragStatus);
        auto \*dragEvent = OH\_ArkUI\_NodeEvent\_GetDragEvent(event);
        switch (eventType) {
            case NODE\_ON\_PRE\_DRAG:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_PRE\_DRAG Event Receive");
                break;
            case NODE\_ON\_CLICK:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_CLICK Event Receive");
                break;
            case NODE\_ON\_DROP:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DROP Event Receive");
                break;
            case NODE\_ON\_DRAG\_ENTER:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_ENTER Event Receive");
                break;
            case NODE\_ON\_DRAG\_MOVE:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_MOVE Event Receive");
                break;
            case NODE\_ON\_DRAG\_LEAVE:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_LEAVE Event Receive");
                break;
            case NODE\_ON\_DRAG\_START: {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_START Event Receive");
                // ···
                break;
            }
            case NODE\_ON\_DRAG\_END: {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_END Event Receive");
                // ···
                break;
            }
            default:
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "UNKNOWN Event Receive");
                break;
        }
    });
    
4.  Handle the **NODE\_ON\_DRAG\_START** event.
    
    In the **NODE\_ON\_DRAG\_START** event, perform operations required to initiate the drag operation, typically involving data processing. For example, create an [OH\_UdmfRecord](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udmfrecord), add the data **imageValue** required for dragging an image to **OH\_UdmfRecord** as the [OH\_UdsFileUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udsfileuri) type, then set **OH\_UdmfRecord** into [OH\_UdmfData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udmfdata), and finally set **OH\_UdmfData** into [DragEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragevent).
    
    void SetImageData(ArkUI\_DragEvent\* dragEvent)
    {
        int returnValue;
        OH\_UdmfRecord \*record = OH\_UdmfRecord\_Create();
        OH\_UdsFileUri \*imageValue = OH\_UdsFileUri\_Create();
        // Replace src/main/resources/base/media/seagull.png with the image resource file you use.
        returnValue = OH\_UdsFileUri\_SetFileUri(imageValue, "/resources/base/media/seagull.png");
        returnValue = OH\_UdmfRecord\_AddFileUri(record, imageValue);
        OH\_UdmfData \*data = OH\_UdmfData\_Create();
        returnValue = OH\_UdmfData\_AddRecord(data, record);
        returnValue = OH\_ArkUI\_DragEvent\_SetData(dragEvent, data);
    }
    // ···
                case NODE\_ON\_DRAG\_START: {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DRAG\_START EventReceiver");
                    SetImageData(dragEvent);
                    break;
                }
    
5.  Handle the **NODE\_ON\_DROP** event.
    
    In the **NODE\_ON\_DROP** event, perform operations related to the drop phase, typically involving retrieving the data passed during the drag process. For example, import the [udmf\_meta.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-meta-h) file, obtain [OH\_UdmfData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udmfdata), check whether the required data type exists, extract the corresponding data from [OH\_UdmfRecord](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udmfrecord), and destroy the pointer.
    
    void GetDragData(ArkUI\_DragEvent\* dragEvent)
    {
        // Obtain the UDMF data.
        int returnValue;
        // Create an OH\_UdmfData object.
        OH\_UdmfData \*data = OH\_UdmfData\_Create();
        returnValue = OH\_ArkUI\_DragEvent\_GetUdmfData(dragEvent, data);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragEvent\_GetUdmfData returnValue = %{public}d", returnValue);
        // Check whether OH\_UdmfData has the required data type.
        bool resultUdmf = OH\_UdmfData\_HasType(data, UDMF\_META\_GENERAL\_FILE);
        if (resultUdmf) {
            // Obtain records from OH\_UdmfData.
            unsigned int recordsCount = 0;
            OH\_UdmfRecord \*\*records = OH\_UdmfData\_GetRecords(data, &recordsCount);
            // Extract elements from records.
            int returnStatus;
            for (int i = 0; i < recordsCount; i++) {
                // Obtain the file type data from OH\_UdmfRecord.
                OH\_UdsFileUri \*imageValue = OH\_UdsFileUri\_Create();
                returnStatus = OH\_UdmfRecord\_GetFileUri(records\[i\], imageValue);
                const char \*fileUri = OH\_UdsFileUri\_GetFileUri(imageValue);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                    "dragTest OH\_UdmfRecord\_GetPlainText "
                    "returnStatus= %{public}d "
                    "fileUri= %{public}s",
                    returnStatus, fileUri);
                // Destroy the pointer after use.
                OH\_UdsFileUri\_Destroy(imageValue);
            }
            if (recordsCount != 0) {
                OH\_ArkUI\_DragEvent\_SetDragResult(dragEvent, ARKUI\_DRAG\_RESULT\_SUCCESSFUL);
                ArkUI\_DropOperation option;
                OH\_ArkUI\_DragEvent\_GetDropOperation(dragEvent, &option);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                    "OH\_ArkUI\_DragEvent\_GetDropOperation returnValue = %{public}d", option);
            }
        } else {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                "OH\_UdmfData\_HasType not contain UDMF\_META\_GENERAL\_FILE");
        }
        int32\_t count;
        OH\_ArkUI\_DragEvent\_GetDataTypeCount(dragEvent, &count);
        if (count <= 0 || count >= 128U) {
            return;
        }
        char \*\*eventTypeArray = new char \*\[count\];
        for (int i = 0; i < count; i++) {
            eventTypeArray\[i\] = new char\[128U\];
        }
        OH\_ArkUI\_DragEvent\_GetDataTypes(dragEvent, eventTypeArray, count, 128U);
        for (int i = 0; i < count; i++) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                "OH\_ArkUI\_DragEvent\_GetDataTypes returnValue = %{public}s", eventTypeArray\[i\]);
        }
    }
    // ···
                case NODE\_ON\_DROP: {
                    OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation(dragEvent, ARKUI\_DROP\_OPERATION\_COPY);
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DROP EventReceiver");
                    GetDragData(dragEvent);
                    break;
                }
    

#### Initiating a Drag Operation

In addition to the basic drag-and-drop functionality, ArkUI allows you to initiate a drag operation using C APIs. The following example demonstrates how to use C APIs to start a drag operation with text data and highlights key points to keep in mind during development.

1.  Register node events.
    
    Create a **Button** node, set its attributes, and register the [NODE\_ON\_TOUCH\_INTERCEPT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) event.
    
    // Use buttonTouch as targetId to distinguish events from different targets.
    enum {
        BUTTON\_TOUCH = 1
    };
    
    dragButton = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
    SetId(dragButton, "dragBt3");
    SetCommonAttribute(dragButton, 80.0f, 50.0f, 0xFFFF0000, 20.0f);
    SetButtonLabel(dragButton, "Drag");
    nodeAPI->registerNodeEvent(dragButton, NODE\_ON\_TOUCH\_INTERCEPT, BUTTON\_TOUCH, nullptr);
    
    #define DEFAULT\_WIDTH 200.0
    // Set the node brightness.
    void SetWidth(ArkUI\_NodeHandle &node, float width = DEFAULT\_WIDTH)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue widthValue\[\] = {width};
        ArkUI\_AttributeItem widthItem = {widthValue, 1};
        nodeAPI->setAttribute(node, NODE\_WIDTH, &widthItem);
    }
    
    #define DEFAULT\_HEIGHT 200.0
    // Set the node height.
    void SetHeight(ArkUI\_NodeHandle &node, float height = DEFAULT\_HEIGHT)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue heightValue\[\] = {height};
        ArkUI\_AttributeItem heightItem = {heightValue, 1};
        nodeAPI->setAttribute(node, NODE\_HEIGHT, &heightItem);
    }
    
    #define DEFAULT\_BG\_COLOR 0xFFFFFFFF
    // Set the background color of the node.
    void SetBackgroundColor(ArkUI\_NodeHandle &node, uint32\_t color = DEFAULT\_BG\_COLOR)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue colorValue\[\] = {{.u32 = color}};
        ArkUI\_AttributeItem colorItem = {colorValue, 1};
        nodeAPI->setAttribute(node, NODE\_BACKGROUND\_COLOR, &colorItem);
    }
    
    #define DEFAULT\_MARGIN 5.0
    // Set the margin of the node.
    void SetMargin(ArkUI\_NodeHandle &node, float margin = DEFAULT\_MARGIN)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue marginValue\[\] = {margin};
        ArkUI\_AttributeItem marginItem = {marginValue, 1};
        nodeAPI->setAttribute(node, NODE\_MARGIN, &marginItem);
    }
    
    // Set tags for a Button node.
    void SetButtonLabel(ArkUI\_NodeHandle &node, const char \*label)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_AttributeItem NODE\_Button\_SRC\_Item = {.string = label};
        nodeAPI->setAttribute(node, NODE\_BUTTON\_LABEL, &NODE\_Button\_SRC\_Item);
    }
    
    // Set the node identifier.
    void SetId(ArkUI\_NodeHandle &node, const char \*id)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_AttributeItem idItem = {.string = id};
        nodeAPI->setAttribute(node, NODE\_ID, &idItem);
    }
    
    #define DEFAULT\_BORDER\_WIDTH 0.0
    // Set the border width for the node.
    void SetBorderWidth(ArkUI\_NodeHandle &node, float width = DEFAULT\_BORDER\_WIDTH)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue borderWidthValue\[\] = {width};
        ArkUI\_AttributeItem borderWidthItem = {borderWidthValue, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_WIDTH, &borderWidthItem);
    }
    
    #define DEFAULT\_BORDER\_COLOR 0xFF000000
    // Set the border color of the node.
    void SetBorderColor(ArkUI\_NodeHandle &node, uint32\_t color = DEFAULT\_BORDER\_COLOR)
    {
        if (!nodeAPI) {
            return;
        }
        ArkUI\_NumberValue borderColorValue\[\] = {{.u32 = color}};
        ArkUI\_AttributeItem borderColorItem = {borderColorValue, 1};
        nodeAPI->setAttribute(node, NODE\_BORDER\_COLOR, &borderColorItem);
    }
    
    // Set common node attributes, such as the width, height, background color, margin, and border style.
    void SetCommonAttribute(ArkUI\_NodeHandle &node, float width = DEFAULT\_WIDTH, float height = DEFAULT\_HEIGHT,
                            unsigned int color = DEFAULT\_BG\_COLOR, float margin = DEFAULT\_MARGIN)
    {
        SetWidth(node, width);
        SetHeight(node, height);
        SetBackgroundColor(node, color);
        SetMargin(node, margin);
        SetBorderWidth(node, DEFAULT\_BORDER\_WIDTH);
        SetBorderColor(node);
    }
    
2.  Receive the **NODE\_ON\_TOUCH\_INTERCEPT** event.
    
    In the **NODE\_ON\_TOUCH\_INTERCEPT** event, you need to set up **DragAction** to initiate the drag operation. Use [targetId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeevent_gettargetid) to distinguish events triggered by different buttons.
    
    nodeAPI->addNodeEventReceiver(dragButton, \[\](ArkUI\_NodeEvent \*event) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "RegisterNodeEventForthReceiver called");
        auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
        auto preDragStatus = OH\_ArkUI\_NodeEvent\_GetPreDragStatus(event);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "eventType = %{public}d, preDragStatus = %{public}d", eventType, preDragStatus);
    
        auto \*dragEvent = OH\_ArkUI\_NodeEvent\_GetDragEvent(event);
        switch (eventType) {
            case NODE\_ON\_TOUCH\_INTERCEPT: {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_TOUCH\_INTERCEPT EventReceiver");
                // ···
                break;
            }
            default: {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "UNKNOWN EventReceiver");
                break;
            }
        }
    });
    
3.  Set the drag action.
    
    In the **NODE\_ON\_TOUCH\_INTERCEPT** event, set **DragAction** to initiate the drag operation. Create a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_createpixelmap), set [ArkUI\_DragPreviewOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption) and the touch point, and set the text data to **DragAction**.
    
                case NODE\_ON\_TOUCH\_INTERCEPT: {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_TOUCH\_INTERCEPT EventReceiver");
                    // Create a DragAction object.
                    action = OH\_ArkUI\_CreateDragActionWithNode(dragButton);
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                        "OH\_ArkUI\_CreateDragActionWithNode returnValue = %{public}p", action);
                    // Set a PixelMap object.
                    std::vector<OH\_PixelmapNative \*> pixelVector;
                    SetPixelMap(pixelVector);
                    // Set DragPreviewOption.
                    SetDragPreviewOption();
                    // Set pointerId and touchPoint.
                    PrintDragActionInfos();
                    // Set unifiedData.
                    SetDragActionData();
                    // startDrag
                    int returnValue = OH\_ArkUI\_StartDrag(action);
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                        "OH\_ArkUI\_StartDrag returnValue = %{public}d",
                        returnValue);
                    OH\_ArkUI\_DragAction\_Dispose(action);
                    break;
                }
                // ···
    void SetDragActionData()
    {
        // Create an OH\_UdmfRecord object.
        OH\_UdmfRecord \*record = OH\_UdmfRecord\_Create();
        // Add plain text data to OH\_UdmfRecord.
        OH\_UdsPlainText \*plainText = OH\_UdsPlainText\_Create();
        int returnStatus;
        OH\_UdsPlainText\_SetAbstract(plainText, "this is plainText Abstract example");
        OH\_UdsPlainText\_SetContent(plainText, "this is plainText Content example");
        returnStatus = OH\_UdmfRecord\_AddPlainText(record, plainText);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "dragTest OH\_UdmfRecord\_AddPlainText returnStatus = %{public}d", returnStatus);
        // Create an OH\_UdmfData object.
        OH\_UdmfData \*data = OH\_UdmfData\_Create();
        // Add OH\_UdmfRecord to OH\_UdmfData.
        returnStatus = OH\_UdmfData\_AddRecord(data, record);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "dragTest OH\_UdmfData\_AddRecord returnStatus = %{public}d", returnStatus);
        int returnValue = OH\_ArkUI\_DragAction\_SetData(action, data);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetData returnValue = %{public}d", returnValue);
        // Register a drag status listener.
        OH\_ArkUI\_DragAction\_RegisterStatusListener(action, data, &DragStatusListener);
    }
    
    void SetPixelMap(std::vector<OH\_PixelmapNative \*> &pixelVector)
    {
        uint8\_t data\[960000\];
        size\_t dataSize = 960000;
        for (int i = 0; i < dataSize; i++) {
            data\[i\] = i + 1;
        }
        // Create a parameter structure instance and set parameters.
        OH\_Pixelmap\_InitializationOptions \*createOpts;
        OH\_PixelmapInitializationOptions\_Create(&createOpts);
        OH\_PixelmapInitializationOptions\_SetWidth(createOpts, 200U);
        OH\_PixelmapInitializationOptions\_SetHeight(createOpts, 300U);
        OH\_PixelmapInitializationOptions\_SetPixelFormat(createOpts, PIXEL\_FORMAT\_BGRA\_8888);
        OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);
        // Create a Pixelmap instance.
        OH\_PixelmapNative \*pixelmap = nullptr;
        OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &pixelmap);
        OH\_PixelmapNative\_Flip(pixelmap, true, true);
        pixelVector.push\_back(pixelmap);
        int returnValue = OH\_ArkUI\_DragAction\_SetPixelMaps(action, pixelVector.data(), pixelVector.size());
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetPixelMaps returnValue = %{public}d", returnValue);
    }
    
    void SetDragPreviewOption()
    {
        auto \*previewOptions = OH\_ArkUI\_CreateDragPreviewOption();
        OH\_ArkUI\_DragPreviewOption\_SetScaleMode(previewOptions,
            ArkUI\_DragPreviewScaleMode::ARKUI\_DRAG\_PREVIEW\_SCALE\_DISABLED);
        OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled(previewOptions, true);
        OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled(previewOptions, true);
        int returnValue = OH\_ArkUI\_DragAction\_SetDragPreviewOption(action, previewOptions);
        OH\_ArkUI\_DragPreviewOption\_Dispose(previewOptions);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetDragPreviewOption returnValue = %{public}d", returnValue);
    }
    
    void PrintDragActionInfos()
    {
        // Set pointerId.
        int returnValue = OH\_ArkUI\_DragAction\_SetPointerId(action, 0);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetPointerId returnValue = %{public}d", returnValue);
        // Set the touch point.
        returnValue = OH\_ArkUI\_DragAction\_SetTouchPointX(action, 200.0f);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetTouchPointX returnValue = %{public}d", returnValue);
        returnValue = OH\_ArkUI\_DragAction\_SetTouchPointY(action, 200.0f);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragAction\_SetTouchPointY returnValue = %{public}d", returnValue);
    }
    
4.  Handle the **NODE\_ON\_DROP** event.
    
    In the **NODE\_ON\_DROP** event, perform actions related to the drop phase. Typically, this involves obtaining the data passed during the drag operation. The drag data from **DragAction** is also obtained through **DragEvent**
    
                case NODE\_ON\_DROP: {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest", "NODE\_ON\_DROP EventReceiver");
                    GetUdmfDataText(dragEvent);
                    OH\_ArkUI\_DragAction\_UnregisterStatusListener(action);
                    break;
                }
                // ···
    void GetUdmfDataText(ArkUI\_DragEvent\* dragEvent)
    {
        // Obtain the UDMF data.
        int returnValue;
        // Create an OH\_UdmfData object.
        OH\_UdmfData \*data = OH\_UdmfData\_Create();
        returnValue = OH\_ArkUI\_DragEvent\_GetUdmfData(dragEvent, data);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
            "OH\_ArkUI\_DragEvent\_GetUdmfData returnValue = %{public}d", returnValue);
        // Check whether OH\_UdmfData has the required data type.
        bool resultUdmf = OH\_UdmfData\_HasType(data, UDMF\_META\_PLAIN\_TEXT);
        if (resultUdmf) {
            // Obtain records from OH\_UdmfData.
            unsigned int recordsCount = 0;
            OH\_UdmfRecord \*\*records = OH\_UdmfData\_GetRecords(data, &recordsCount);
            // Extract elements from records.
            int returnStatus;
            for (int i = 0; i < recordsCount; i++) {
                // Obtain plain text data from OH\_UdmfRecord.
                OH\_UdsPlainText \*plainTextValue = OH\_UdsPlainText\_Create();
                returnStatus = OH\_UdmfRecord\_GetPlainText(records\[i\], plainTextValue);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                    "dragTest OH\_UdmfRecord\_GetPlainText "
                    "returnStatus= %{public}d",
                    returnStatus);
                auto getAbstract = OH\_UdsPlainText\_GetAbstract(plainTextValue);
                auto getContent = OH\_UdsPlainText\_GetContent(plainTextValue);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                    "OH\_UdsPlainText\_GetAbstract = "
                    "%{public}s, OH\_UdsPlainText\_GetContent = "
                    "%{public}s",
                    getAbstract, getContent);
                // Destroy the pointer after use.
                OH\_UdsPlainText\_Destroy(plainTextValue);
            }
        } else {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00U, "dragTest",
                "OH\_UdmfData\_HasType not contain UDMF\_META\_PLAIN\_TEXT");
        }
        OH\_UdmfData\_Destroy(data);
    }
