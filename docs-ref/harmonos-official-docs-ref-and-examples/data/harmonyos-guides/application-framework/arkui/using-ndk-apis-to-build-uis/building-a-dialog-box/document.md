# Building a Dialog Box

You can display a custom dialog box by creating a dialog controller or by creating a custom dialog content object, and then setting its styles and content.

[Displaying a custom dialog box through a dialog controller](#displaying-a-custom-dialog-box-through-a-dialog-controller): In this approach, you use the APIs defined in a struct named **ArkUI\_NativeDialogAPI\_x** (where x denotes the version) for dialog box control.

[Displaying a custom dialog box through a custom dialog content object](#displaying-a-custom-dialog-box-through-a-custom-dialog-content-object): In this approach, you use the APIs defined in the functions of [native\_dialog.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-dialog-h#functions).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/yIXZCoVcR1ugI-TLubHDRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E52FCDDF395596D8CBA613C0648C5637DDCB5E9F5571D9D361F4C1CFAABDBA0D)

-   For details about how to display a custom dialog box through a dialog controller, see [openCustomDialogWithController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18).
    
-   For details about how to display a custom dialog box through a custom dialog content object, see [openCustomDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12).
    
-   [OH\_ArkUI\_QueryModuleInterfaceByName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_querymoduleinterfacebyname) is used to obtain a collection of native module APIs of a specified type. You can call APIs in the native module using the returned data of the **ArkUI\_NativeDialogHandle** type.
    

#### Creating and Destroying a Custom Dialog Box

## Displaying a Custom Dialog Box Through a Dialog Controller

-   Creating a Dialog Controller
    
    [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) represents a pointer to the dialog controller, which you can create by calling the [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#create) API of [ArkUI\_NativeDialogAPI\_x](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1).
    
    This API returns data of the **ArkUI\_NativeDialogHandle** type.
    
    ArkUI\_NativeDialogHandle g\_dialogController = nullptr;
    // ···
        ArkUI\_NativeDialogAPI\_1 \*dialogAPI = reinterpret\_cast<ArkUI\_NativeDialogAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_DIALOG, "ArkUI\_NativeDialogAPI\_1"));
        if (!g\_dialogController) {
            g\_dialogController = dialogAPI->create();
        }
    
-   Destroying the Dialog Controller
    
    When dialog box operations are no longer needed, actively call the [dispose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#dispose) API to destroy the dialog controller object.
    
    ArkUI\_NativeDialogAPI\_1 \*dialogAPI = reinterpret\_cast<ArkUI\_NativeDialogAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_DIALOG, "ArkUI\_NativeDialogAPI\_1"));
    dialogAPI->dispose(g\_dialogController);
    g\_dialogController = nullptr;
    

## Displaying a Custom Dialog Box Through a Custom Dialog Content Object

-   Creating a Dialog Content Object
    
    You can create a custom dialog content object [ArkUI\_CustomDialogOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions) by calling the OH\_ArkUI\_CustomDialog\_CreateOptions\](../reference/apis-arkui/capi-native-dialog-h.md#oh\_arkui\_customdialog\_createoptions) API,
    
    which returns a pointer of the **ArkUI\_CustomDialogOptions** type.
    
    ArkUI\_CustomDialogOptions\* g\_dialogOptions = nullptr;
    // ···
        auto textNode = std::make\_shared<NativeModule::ArkUITextNode>();
        if (!g\_dialogOptions) {
            g\_dialogOptions = OH\_ArkUI\_CustomDialog\_CreateOptions(textNode->GetHandle());
        }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/RWynmg6vSTOnxDWkj6s6Dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FE885E746BC587D6BA54DB722CB5B94053189A3156BEFF273AC2A01D733F7B4)
    
    For details about how to declare **ArkUITextNode**, refer to the implementation of the text component in the [ArkUINode.h](../integrating-with-arkts-pages/document.md#example) file.
    
-   Destroying the Dialog Controller
    
    When dialog box operations are no longer needed, actively call the [OH\_ArkUI\_CustomDialog\_DisposeOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-dialog-h#oh_arkui_customdialog_disposeoptions) API to destroy the dialog controller object.
    
    OH\_ArkUI\_CustomDialog\_DisposeOptions(g\_dialogOptions);
    

#### Setting Dialog Box Styles

You can set the alignment, offset, corner radius of the background, background color, mask color, and region of the dialog box.

1.  Create a dialog box content node.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/jGTw0WTvQTedOTWoaJzMGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E656F08210302D50120EB6116EA19FBEFD9BD18203D30D6E4A813FC0A69B9CFA)
    
    The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not packaged by default when a project or module is created. To package these resources, go to **buildOptions** in the module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. For details, see the description of [resOptions](../../../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md#table1476161719356).
    
    ArkUI\_NodeHandle CreateDialogContent()
    {
        ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        ArkUI\_NodeHandle text = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_NumberValue textWidthValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textWidthItem = {.value = textWidthValue,
                                             .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(text, NODE\_WIDTH, &textWidthItem);
        ArkUI\_NumberValue textHeightValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textHeightItem = {.value = textHeightValue,
                                              .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(text, NODE\_HEIGHT, &textHeightItem);
        ArkUI\_NodeHandle span = nodeAPI->createNode(ARKUI\_NODE\_SPAN);
        ArkUI\_AttributeItem spanItem = {.string = "This is a dialog box"};
        nodeAPI->setAttribute(span, NODE\_SPAN\_CONTENT, &spanItem);
        ArkUI\_NodeHandle imageSpan = nodeAPI->createNode(ARKUI\_NODE\_IMAGE\_SPAN);
        // Replace src/main/ets/pages/common/sky.jpg with the image resource file you use.
        ArkUI\_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
        nodeAPI->setAttribute(imageSpan, NODE\_IMAGE\_SPAN\_SRC, &imageSpanItem);
        ArkUI\_NumberValue imageSpanWidthValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
                                                  .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(imageSpan, NODE\_WIDTH, &imageSpanWidthItem);
        ArkUI\_NumberValue imageSpanHeightValue\[\] = {{.f32 = 200}};
        ArkUI\_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
                                                   .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(imageSpan, NODE\_HEIGHT, &imageSpanHeightItem);
        nodeAPI->addChild(text, span);
        nodeAPI->addChild(text, imageSpan);
        return text;
    }
    
2.  Control dialog box styles using either of the following methods. For details about the dialog box APIs, see [native\_dialog.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-dialog-h).
    
    -   Using the controller
        
        void ShowDialog()
        {
            ArkUI\_NativeDialogAPI\_1 \*dialogAPI = reinterpret\_cast<ArkUI\_NativeDialogAPI\_1 \*>(
                OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_DIALOG, "ArkUI\_NativeDialogAPI\_1"));
            if (!g\_dialogController) {
                g\_dialogController = dialogAPI->create();
            }
            auto contentNode = CreateDialogContent();
            dialogAPI->setContent(g\_dialogController, contentNode);
            dialogAPI->setContentAlignment(g\_dialogController, static\_cast<int32\_t>(ARKUI\_ALIGNMENT\_BOTTOM), 0, 0);
            dialogAPI->setBackgroundColor(g\_dialogController, 0xffffffff);
            dialogAPI->setCornerRadius(g\_dialogController, 6.0f, 6.0f, 6.0f, 6.0f);
            dialogAPI->setModalMode(g\_dialogController, false);
            dialogAPI->setAutoCancel(g\_dialogController, true);
            dialogAPI->show(g\_dialogController, false);
        }
        
    -   Using **dialogOptions**
        
        int32\_t g\_id = 0;
        void OpenDialogCallBack(int32\_t dialogId)
        {
            g\_id = dialogId;
        }
        
        void OpenCustomDialog()
        {
            auto contentNode = CreateDialogContent();
            if (!g\_dialogOptions) {
                g\_dialogOptions = OH\_ArkUI\_CustomDialog\_CreateOptions(contentNode);
            }
            OH\_ArkUI\_CustomDialog\_SetAlignment(g\_dialogOptions, static\_cast<int32\_t>(ARKUI\_ALIGNMENT\_BOTTOM), 0, 0);
            OH\_ArkUI\_CustomDialog\_SetBackgroundColor(g\_dialogOptions, 0xffffffff);
            OH\_ArkUI\_CustomDialog\_SetCornerRadius(g\_dialogOptions, 6.0f, 6.0f, 6.0f, 6.0f);
            OH\_ArkUI\_CustomDialog\_SetModalMode(g\_dialogOptions, false);
            OH\_ArkUI\_CustomDialog\_SetAutoCancel(g\_dialogOptions, true);
            OH\_ArkUI\_CustomDialog\_SetBorderStyle(g\_dialogOptions, ARKUI\_BORDER\_STYLE\_SOLID,
                                                 ARKUI\_BORDER\_STYLE\_SOLID, ARKUI\_BORDER\_STYLE\_SOLID, ARKUI\_BORDER\_STYLE\_SOLID);
            OH\_ArkUI\_CustomDialog\_OpenDialog(g\_dialogOptions, OpenDialogCallBack);
        }
        
3.  Close the dialog box using either of the following methods:
    
    -   Using the controller
        
        void CloseDialog()
        {
            ArkUI\_NativeDialogAPI\_1 \*dialogAPI = reinterpret\_cast<ArkUI\_NativeDialogAPI\_1 \*>(
                OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_DIALOG, "ArkUI\_NativeDialogAPI\_1"));
            dialogAPI->close(g\_dialogController);
        }
        
    -   Using **dialogOptions**
        
        void CloseCustomDialog()
        {
            OH\_ArkUI\_CustomDialog\_CloseDialog(g\_id);
        }
        

#### Interacting with the Dialog Box

You can create an interactive page to open or close a dialog box.

1.  Create a button that, when clicked, will trigger the display of a dialog box. For details about how to obtain and use nodes of the ArkUI\_NodeContentHandle type, see [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).
    
    constexpr int32\_t BUTTON\_CLICK\_ID = 1;
    ArkUI\_NodeHandle g\_buttonNode = nullptr;
    
    void MainViewMethod(ArkUI\_NodeContentHandle handle)
    {
        ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue widthValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem widthItem = {.value = widthValue, .size = sizeof(widthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_WIDTH, &widthItem);
        ArkUI\_NumberValue heightValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem heightItem = {.value = heightValue, .size = sizeof(heightValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_HEIGHT, &heightItem);
        
        g\_buttonNode = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
        ArkUI\_NumberValue buttonWidthValue\[\] = {{.f32 = 200}};
        ArkUI\_AttributeItem buttonWidthItem = {.value = buttonWidthValue,
                                               .size = sizeof(buttonWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(g\_buttonNode, NODE\_WIDTH, &buttonWidthItem);
        ArkUI\_NumberValue buttonHeightValue\[\] = {{.f32 = 50}};
        ArkUI\_AttributeItem buttonHeightItem = {.value = buttonHeightValue,
                                                .size = sizeof(buttonHeightValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(g\_buttonNode, NODE\_HEIGHT, &buttonHeightItem);
        ArkUI\_AttributeItem labelItem = {.string = "Click Dialog Box"};
        nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
        ArkUI\_NumberValue buttonTypeValue\[\] = {{.i32 = static\_cast<int32\_t>(ARKUI\_BUTTON\_TYPE\_NORMAL)}};
        ArkUI\_AttributeItem buttonTypeItem = {.value = buttonTypeValue,
                                              .size = sizeof(buttonTypeValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_TYPE, &buttonTypeItem);
        nodeAPI->registerNodeEvent(g\_buttonNode, NODE\_ON\_CLICK, BUTTON\_CLICK\_ID, nullptr);
        nodeAPI->addNodeEventReceiver(g\_buttonNode, OnButtonClicked);
        nodeAPI->addChild(column, g\_buttonNode);
        OH\_ArkUI\_NodeContent\_AddNode(handle, column);
    }
    
2.  Create a button event callback function to trigger the display or closure of the dialog box when the button is clicked.
    
    -   Using the controller
        
        bool g\_isShown = false;
        
        void OnButtonClicked(ArkUI\_NodeEvent \*event)
        {
            if (!event || !g\_buttonNode) {
                return;
            }
            auto eventId = OH\_ArkUI\_NodeEvent\_GetTargetId(event);
            if (eventId == BUTTON\_CLICK\_ID) {
                ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
                    OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
                if (g\_isShown) {
                    g\_isShown = false;
                    ArkUI\_AttributeItem labelItem = {.string = "Show Dialog Box"};
                    nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
                    CloseDialog();
                } else {
                    g\_isShown = true;
                    ArkUI\_AttributeItem labelItem = {.string = "Close Dialog Box"};
                    nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
                    ShowDialog();
                }
            }
        }
        
    -   Using **dialogOptions**
        
        void OnButtonClicked(ArkUI\_NodeEvent \*event)
        {
            if (!event || !g\_buttonNode) {
                return;
            }
            auto eventId = OH\_ArkUI\_NodeEvent\_GetTargetId(event);
            if (eventId == BUTTON\_CLICK\_ID) {
                ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
                    OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
                if (g\_isShown) {
                    g\_isShown = false;
                    ArkUI\_AttributeItem labelItem = {.string = "Show Dialog Box"};
                    nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
                    CloseCustomDialog();
                } else {
                    g\_isShown = true;
                    ArkUI\_AttributeItem labelItem = {.string = "Close Dialog Box"};
                    nodeAPI->setAttribute(g\_buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
                    OpenCustomDialog();
                }
            }
        }
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tAsQM4QlTnKWM_VIqeke1w/en-us_image_0000002568764615.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47859D11972D5D33D047B21EBE5C17F36CED535BC17B15B7BAE858C6C9E49B55)

#### Managing the Dialog Box Lifecycle

From API version 19, four lifecycle callbacks are available before and after a dialog box is displayed and closed: [registerOnWillAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3#registeronwillappear), [registerOnDidAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3#registerondidappear), [registerOnWillDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3#registeronwilldisappear), and [registerOnDidDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3#registerondiddisappear).

These lifecycle APIs must be called before the **show** API is invoked. The sequence of lifecycle events is as follows:

registerOnWillAppear -> Dialog box display animation starts -> Dialog box display animation ends -> registerOnDidAppear -> Dialog box display completes -> registerOnWillDisappear -> Dialog box close animation starts -> Dialog box close animation ends -> registerOnDidDisappear -> Dialog box close animation completes.

The following is an example of creating a dialog box that triggers lifecycle callback functions when the dialog box is displayed and closed. For details about how to obtain and use nodes of the ArkUI\_NodeContentHandle type, see [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/sHswFi_HR0OoknElkD1O9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58C0E403BC46FBF5BF337B7E53D9066F79B70B96A1498A2A64AF784B508C93B8)

The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not packaged by default when a project or module is created. To package these resources, go to **buildOptions** in the module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. For details, see the description of [resOptions](../../../../building-an-app/configuration-files/module-level-build-profile-json5-file/document.md#table1476161719356).

ArkUI\_NodeHandle CreateDialogContent()
{
    ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
    ArkUI\_NodeHandle text = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
    ArkUI\_NumberValue textWidthValue\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem textWidthItem = {.value = textWidthValue,
                                         .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(text, NODE\_WIDTH, &textWidthItem);
    ArkUI\_NumberValue textHeightValue\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem textHeightItem = {.value = textHeightValue,
                                          .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(text, NODE\_HEIGHT, &textHeightItem);
    ArkUI\_NodeHandle span = nodeAPI->createNode(ARKUI\_NODE\_SPAN);
    ArkUI\_AttributeItem spanItem = {.string = "This is a dialog box"};
    nodeAPI->setAttribute(span, NODE\_SPAN\_CONTENT, &spanItem);
    ArkUI\_NodeHandle imageSpan = nodeAPI->createNode(ARKUI\_NODE\_IMAGE\_SPAN);
    // Replace src/main/ets/pages/common/sky.jpg with the image resource file you use.
    ArkUI\_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
    nodeAPI->setAttribute(imageSpan, NODE\_IMAGE\_SPAN\_SRC, &imageSpanItem);
    ArkUI\_NumberValue imageSpanWidthValue\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
                                              .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(imageSpan, NODE\_WIDTH, &imageSpanWidthItem);
    ArkUI\_NumberValue imageSpanHeightValue\[\] = {{.f32 = 200}};
    ArkUI\_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
                                               .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(imageSpan, NODE\_HEIGHT, &imageSpanHeightItem);
    nodeAPI->addChild(text, span);
    nodeAPI->addChild(text, imageSpan);
    return text;
}

void OnWillAppearCallBack(void\* userdata)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "CustomDialogContentTest", "OnWillAppearCallBack");
}

void OnDidAppearCallBack(void\* userdata)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "CustomDialogContentTest", "OnDidAppearCallBack");
}

void OnWillDisappearCallBack(void\* userdata)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "CustomDialogContentTest", "OnWillDisappearCallBack");
}

void OnDidDisappearCallBack(void\* userdata)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "CustomDialogContentTest", "OnDidDisappearCallBack");
}

void ShowDialog()
{
    ArkUI\_NativeDialogAPI\_3 \*dialogAPI = reinterpret\_cast<ArkUI\_NativeDialogAPI\_3 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_DIALOG, "ArkUI\_NativeDialogAPI\_3"));
    if (!g\_dialogController) {
        g\_dialogController = dialogAPI->nativeDialogAPI1.create();
    }
    auto contentNode = CreateDialogContent();
    dialogAPI->nativeDialogAPI1.setContent(g\_dialogController, contentNode);
    dialogAPI->nativeDialogAPI1.setAutoCancel(g\_dialogController, true);
    dialogAPI->registerOnWillAppear(g\_dialogController, nullptr, OnWillAppearCallBack);
    dialogAPI->registerOnDidAppear(g\_dialogController, nullptr, OnDidAppearCallBack);
    dialogAPI->registerOnWillDisappear(g\_dialogController, nullptr, OnWillDisappearCallBack);
    dialogAPI->registerOnDidDisappear(g\_dialogController, nullptr, OnDidDisappearCallBack);
    dialogAPI->nativeDialogAPI1.show(g\_dialogController, false);
}
