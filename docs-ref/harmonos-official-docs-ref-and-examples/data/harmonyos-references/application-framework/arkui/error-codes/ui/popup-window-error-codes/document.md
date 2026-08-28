# Popup Window Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/M4o6CMDOS5CHXROXUsqC6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73E62DB5495E95574A92CF5695187127289515E27569380420832A6EAE796E85)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 103301 Dialog Content Error

**Error Message**

The ComponentContent is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/48mYs0RIQlSA1FVK2_pprQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDDFB46AA4B5FE75E9E5F3EB0474DDB15413B5F3167AB2CF3E76CFDABAE7FFBF)

When the called API is [openCustomDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialog12), [openCustomDialogWithController](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialogwithcontroller18), [closeCustomDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#closecustomdialog12), or [updateCustomDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatecustomdialog12), the returned error is "Dialog content error."The ComponentContent is incorrect.

**Description**

This error code is reported when there is an issue with the content node of the custom dialog box, which prevents the node from being rendered.

**Possible Causes**

The custom content node passed to the dialog box is empty or incorrect.

**Solution**

1.  Check whether the content node of the custom dialog box exists. You can do so using the [getFrameNodeById()](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getframenodebyid12) API.
    
2.  Ensure that the content node can be rendered properly.
    

#### 103302 Custom Dialog Box Already Exists

**Error Message**

The ComponentContent already exists.

**Description**

This error code is reported when an attempt is made to open a custom dialog box that is already open.

**Possible Causes**

The custom dialog box associated with the content node is currently displayed.

**Solution**

Reinitialize and bind a content node that can be rendered properly to the dialog box.

#### 103303 Custom Dialog Box Not Found

**Error Message**

The ComponentContent cannot be found.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Mt1h4wVYRJu-kcuPkQJd2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3FD3A0BD4410042617031197FA6BD9BE28DB6EE0DFA5ED7B043C77C732C3718)

When the called API is [closeCustomDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#closecustomdialog12) or [updateCustomDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#updatecustomdialog12), the returned error is "Dialog content not found."The ComponentContent cannot be found.

**Description**

This error code is reported when an attempt is made to close or update a custom dialog box that is not open.

**Possible Causes**

The custom dialog box associated with the content node is not open.

**Solution**

1.  Ensure that the custom dialog box associated with the content node is open.
    
2.  Ensure that the content node of the custom dialog box is the target content node that needs to be updated or closed.
    

#### 103304 Target ID Not Found

**Error Message**

The targetId does not exist.

**Description**

This error code is reported when no node can be found based on the provided **targetId**.

**Possible Causes**

The provided **targetId** is invalid, or the node corresponding to the **targetId** has been destroyed.

**Solution**

Check whether the node corresponding to the provided **targetId** exists. You can query the node using the [getFrameNodeById()](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getframenodebyid12) API.

#### 103305 Node Not Mounted

**Error Message**

The node of targetId is not in the component tree.

**Description**

This error code is reported when the node corresponding to the provided **targetId** is not mounted in the component tree.

**Possible Causes**

The node with the specified **targetId** is not mounted in the component tree.

**Solution**

1.  Check whether the node corresponding to the provided **targetId** exists. You can query the node using the [getFrameNodeById()](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getframenodebyid12) API.
    
2.  Check whether the node corresponding to the provided **targetId** has been mounted to the main node tree. You can do so using the [isAttached()](../../../arkts-api/ui/arkui/framenode/document.md#isattached12) API of the content node.
    

#### 103401 Toast Not Found

**Error Message**

Cannot find the toast.

**Description**

This error code is reported when an attempt is made to close a toast that is not being displayed.

**Possible Causes**

The toast has not been displayed or has already been closed.

**Solution**

Ensure that the toast is being displayed.
