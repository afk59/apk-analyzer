# Ensuring Multi-Instance Functionality in the NDK

Since API version 20, the ArkUI development framework provides the [OH\_ArkUI\_RunTaskInScope](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_runtaskinscope) API to address component operation challenges in multi-instance scenarios on the native side. This feature dynamically switches execution contexts to ensure the validity of component attribute settings across instances, preventing API call exceptions caused by instance context mismatches.

In NDK multi-window development scenarios requiring cross-instance attribute configuration, this capability maintains proper context integrity during cross-instance operations, thereby avoiding cross-instance API call failures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/dDvlSiVSTeaoWI8HvTPikA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D5F1963ED50E01260453EE8AAEF1C7DFB9037940A87B4F0674B7323FB7F6E12)

-   This feature is designed for interaction scenarios between different UI instances in NDK multi-window development, such as modifying attributes of components created on page A or handling logic for components not mounted to the UI tree on page B.
    
-   You can pass custom data structures (such as component pointers or service parameters) through the **userData** parameter to precisely locate target components within callback tasks.
    
-   This feature complements APIs like [OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid) to prevent null pointer or permission exceptions resulting from cross-instance access.
    

This example demonstrates the basic usage of the **OH\_ArkUI\_RunTaskInScope** API, using **OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById** to retrieve components from previous pages. For details, see [OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid). The **userData** parameter passes a component pointer for setting corresponding component attributes.

const uint32\_t VALUE\_2 = 250;
const uint32\_t VALUE\_3 = 480;

//page1
ArkUI\_NodeHandle button = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
ArkUI\_AttributeItem LABEL\_Item = {.string = "pageOneButton"};
// Set the ID for component retrieval using APIs on the second page.
ArkUI\_AttributeItem id = {.string = "pageOneButton"};
nodeAPI->setAttribute(button, NODE\_ID, &id);
nodeAPI->setAttribute(button, NODE\_BUTTON\_LABEL, &LABEL\_Item);
nodeAPI->addChild(textContainer, button);

//page2
// Retrieve pageOneButton created on the previous page using OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById.
ArkUI\_NodeHandle pageOneButton = nullptr;
auto errorCode = OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById("pageOneButton", &pageOneButton);
if (errorCode != ARKUI\_ERROR\_CODE\_NO\_ERROR) {
    OH\_LOG\_ERROR(LOG\_APP, "test Failed to get pageOneButton handle, error code: %{public}d", errorCode);
    return nullptr;
}
auto uiContext = OH\_ArkUI\_GetContextByNode(pageOneButton);
if (uiContext == nullptr) {
    OH\_LOG\_ERROR(LOG\_APP, "test Failed to get UI context for pageOneButton");
    return nullptr;
}
OH\_ArkUI\_RunTaskInScope(uiContext, pageOneButton, \[\](void \*userData) {
    auto \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
        OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
    auto pageOneButton = (ArkUI\_NodeHandle)userData;
    ArkUI\_NumberValue value\[\] = {VALUE\_3};
    ArkUI\_AttributeItem LABEL\_Item = {.string = "success"};
    value\[0\].f32 = VALUE\_2;
    ArkUI\_AttributeItem button\_Item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
    nodeAPI->setAttribute(pageOneButton, NODE\_BUTTON\_LABEL, &LABEL\_Item);
    nodeAPI->setAttribute(pageOneButton, NODE\_WIDTH, &button\_Item);
});
