# @ohos.prompt (Prompt)

The **Prompt** module provides APIs for creating and showing toasts, dialog boxes, and action menus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/P2GQDC7CSJGEgw9b0-b6bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D2AA9B5EE8A5A56CFC60CFD453669D7386696C904474A7B13342FDA227A6448)

The APIs of this module are deprecated since API Version 9. You are advised to use [@ohos.promptAction](../../ui/ohos-promptaction-prompt/document.md) instead.

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import prompt from '@ohos.prompt'

#### prompt.showToast

showToast(options: ShowToastOptions): void

Shows a toast.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowToastOptions](#showtoastoptions) | Yes | Toast options. |

**Example**

import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/hGxxeuLzQcixihmEmIPbXA/en-us_image_0000002568765099.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4718E0B829CF860065CDEAD4E400A724142AB2FC2B547F53D85203D38EC63247)

#### ShowToastOptions

Describes the options for showing the toast.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | string | Yes | Text to display. |
| duration | number | No | Duration that the toast will remain on the screen. The default value is 1500 ms. The value range is 1500 ms to 10000 ms. If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set, the upper limit 10000 ms is used. |
| bottom | string| number | No | Distance between the toast border and the bottom of the screen. It does not have an upper limit. The default unit is vp. |

#### prompt.showDialog

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

Shows a dialog box. This API uses a promise to return the result synchronously.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | Yes | Dialog box options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | Promise used to return the dialog box response result. |

**Example**

import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: \[
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  \],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showDialog error: ' + err);
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ac4fWLdVT3ePC-uGQFqXHA/en-us_image_0000002537765338.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B61770DF6452545D8E041DF2DBCF32447C0CD8334E026E283F305D2B6196B463)

#### prompt.showDialog

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

Shows a dialog box. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | Yes | Dialog box options. |
| callback | AsyncCallback<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | Yes | Callback used to return the dialog box response result. |

**Example**

import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'showDialog Title Info',
  message: 'Message Info',
  buttons: \[
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  \]
}, (err, data) => {
  if (err) {
    console.info('showDialog err: ' + err);
    return;
  }
  console.info('showDialog success callback, click button: ' + data.index);
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5j0D-8bYQq6Jcovm-vpo4g/en-us_image_0000002537925278.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BBD49A12F9BDAA598D344B335584D61BF5FE9DDBBECDC0382B9AC9FB5796B39)

#### ShowDialogOptions

Describes the options for showing the dialog box.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| title | string | No | Title of the dialog box. |
| message | string | No | Text body. |
| buttons | \[[Button](#button),[Button](#button)?,[Button](#button)?\] | No | Array of buttons in the dialog box. The array structure is **{text:'button', color: '#666666'}**. Up to three buttons are supported. The first button is of the **positiveButton** type, the second is of the **negativeButton** type, and the third is of the **neutralButton** type. |

#### ShowDialogSuccessResponse

Describes the dialog box response result.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected button in the **buttons** array. |

#### prompt.showActionMenu

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

Shows an action menu. This API uses a callback to return the result asynchronously.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | Yes | Action menu options. |
| callback | AsyncCallback<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | Yes | Callback used to return the action menu response result. |

**Example**

import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'Title Info',
  buttons: \[
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  \]
}, (err, data) => {
  if (err) {
    console.info('showActionMenu err: ' + err);
    return;
  }
  console.info('showActionMenu success callback, click button: ' + data.index);
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SHWXmZvAQHKN_AhP-TtsTQ/en-us_image_0000002537765340.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CF5A504F60EBEFEA219DC16994BA04E7B7B4D1D06A9BDF551D85D6F01806304)

#### prompt.showActionMenu

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

Shows an action menu. This API uses a promise to return the result synchronously.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | Yes | Action menu options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | Promise used to return the action menu response result. |

**Example**

import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: \[
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  \]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showActionMenu error: ' + err);
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/SDxhrNHqTNSB07Tl0Kn0jw/en-us_image_0000002568685057.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A47B4FF575C0CF5176FE09FBB6DCB74A7D55B4C022E2CB037177E6401BF93926)

#### ActionMenuOptions

Describes the options for showing the action menu.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| title | string | No | Title of the menu. |
| buttons | \[[Button](#button),[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?\] | Yes | Array of menu item buttons. The array structure is **{text:'button', color: '#666666'}**. Up to six buttons are supported. If there are more than six buttons, extra buttons will not be displayed. |

#### ActionMenuSuccessResponse

Describes the action menu response result.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the selected button in the **buttons** array, starting from **0**. |

#### Button

Describes the menu item button in the action menu.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Button text. |
| color | string | Yes | Text color of the button. |
