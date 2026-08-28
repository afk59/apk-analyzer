# systemShare (System Share)

This module provides the functions of creating shared data and starting the sharing panel, and offers multiple standard sharing services, such as sharing data to other apps, copying data, and printing files.

-   If your app functions as a host app that shares content to other apps, you need to integrate Share Kit into your app so that it can configure, start, and close the sharing panel.
-   The sharing panel configuration includes the data object, view presentation mode, and preview mode.

**Model restriction**: APIs of this module can be used only in the stage model.

**Start version**: 4.1.0(11)

#### Module Import

import { systemShare } from '@kit.ShareKit';

#### SharedRecord

Constructs a shared data record, including the data type, data content, description, and some other information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

utd

 | 

string

 | 

No

 | 

No

 | 

Uniform data type. For details, please refer to [@ohos.data.uniformTypeDescriptor (Uniform Data Definition and Description)](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md).

You are advised to pass the precise data type to match the most suitable target app. For details, please refer to [Share Kit Experience Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/share-access-precautions).

 |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

Title of the shared content. You are advised to set this parameter if the content is a text or link. When this parameter is left empty, if the shared content is a piece of text, the text content is used as the value of **title**; if the shared content is a file, the file name is used as the value of **title**.

 |
| 

label

 | 

string

 | 

No

 | 

Yes

 | 

Label indicating the current data record type. This parameter is valid in the single selection mode. The default value is a data type defined by [UniformDataType](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md#uniformdatatype), which has the following options: **HYPERLINK**: link; **HTML**: web page; **TEXT**: text; **VIDEO**: video; **AUDIO**: music; **IMAGE**: image; **FILE**: file.

 |
| 

description

 | 

string

 | 

No

 | 

Yes

 | 

Data record description. The default value is an empty string.

 |
| 

thumbnail

 | 

Uint8Array

 | 

No

 | 

Yes

 | 

Data record thumbnail. When this parameter is left empty, the default icon matching the shared content type is used as the thumbnail.

You are advised to pass a thumbnail matching the data record. If no matching thumbnail is available, you can pass the app icon.

NOTE:

The image size cannot exceed 32 KB. Oversized images may cause the **want** data to exceed the threshold and the failure in starting Share Kit. You can use [ImagePacker.packToData](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagepacker/document.md#packtodata13) to compress images.

 |
| 

thumbnailUri

 | 

string

 | 

No

 | 

Yes

 | 

Data record thumbnail URI. When this parameter is left empty, the default icon matching the shared content type is used as the thumbnail. The following URI types are supported:

-   App file URI. For details, please refer to [Sharing an Application File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/share-app-file).
-   User file URI. For details, please refer to [User File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro).

**Start version**: 5.0.0(12).

NOTE:

If both this parameter and the **thumbnail** parameter exist, the **thumbnail** parameter is used preferentially.

 |
| 

uri

 | 

string

 | 

No

 | 

Yes

 | 

Data record URI. The following URI types are supported:

-   App file URI. For details, please refer to [Sharing an Application File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/share-app-file).
-   User file URI. For details, please refer to [User File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro).

NOTE:

You can use the [fileUri.getUriFromPath](../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#fileurigeturifrompath) method to obtain the file URI from the sandbox path.

Either **content** or **uri** must be set.

 |
| 

content

 | 

string

 | 

No

 | 

Yes

 | 

Data record content. Content of the link (including links of App Linking) and text types is passed through this parameter.

NOTE:

Either **content** or **uri** must be set.

 |
| 

extraData

 | 

Record<string, string | number | boolean | Array<string | number | boolean>>

 | 

No

 | 

Yes

 | 

Extension data, used to share custom extension content with the target app or device.

 |

#### ShareControllerOptions

Sharing controller configuration items, such as the preview mode of the shared content, selection mode, and other information, which determine the display style of the sharing panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Required permissions**: To use the **appLaunchTrustInfo** field, you need to apply for the **ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST** permission. This restricted permission is available only to enterprise apps, enabling them to restrict target apps to a set of trusted apps for secure internal data sharing. For details about how to apply for the permission, please refer to [Requesting Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions-in-acl).

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

anchor

 | 

[ShareControllerAnchor](#section19505934714) | string

 | 

No

 | 

Yes

 | 

When the value type is **string**, this parameter indicates the ID of the control associated with the sharing panel. For details about the ID, please refer to the [value of id in common attributes of ArkUI components](../../../../application-framework/arkui/javascript-components/javascript-compatible-web-like-development-paradigm-arkui-full/universal-components/universal-attributes/document.md#common-attributes).

When the value type is **ShareControllerAnchor**, this parameter indicates the anchor position.

If this parameter is not passed, the sharing panel will be displayed in the default position (center).

 |
| 

previewMode

 | 

[SharePreviewMode](#section71597311103)

 | 

No

 | 

Yes

 | 

Preview mode. The default mode is card.

 |
| 

selectionMode

 | 

[SelectionMode](#section188631791714)

 | 

No

 | 

Yes

 | 

Selection mode. The default mode is single selection.

 |
| 

excludedAbilities

 | 

Array<[ShareAbilityType](#section205631342153016)\>

 | 

No

 | 

Yes

 | 

List of capabilities that do not need to be displayed in the operation area.

**Start version**: 5.0.0(12).

 |
| 

appLaunchTrustInfo

 | 

Array<string>

 | 

No

 | 

Yes

 | 

List of supported target apps (identified by the **appIdentifier** field in [SignatureInfo](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#signatureinfo)). Only the first 50 values are effective. The **ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST** permission is required.

This restricted permission is available only to enterprise apps, enabling them to restrict target apps to a set of trusted apps for secure internal data sharing.

**Start version**: 6.0.1(21).

 |

#### ShareControllerAnchor

Anchor of the sharing pop-up window. The sharing panel will adapt to the screen size and may appear as a pop-up window depending on the screen size.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/XBGCwC9zS6y6H7AKSmx_lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16530AB89832EE1F6ED1766578D1D97802AAC69EC4F2CF63B121A59F7A00E3E9)

If the device screen width is small, the sharing panel will not be displayed in pop-up mode, but displayed in modal mode instead.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

windowOffset

 | 

[Offset](#section747515217482)

 | 

No

 | 

No

 | 

Window offset to the anchor.

 |
| 

size

 | 

[Size](#section16811150124912)

 | 

No

 | 

Yes

 | 

Dimensions of the anchor rectangle. The anchor is a point by default, that is, the width and height are both **0**.

 |

#### Offset

Window offset to the anchor.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate, in pixels.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate, in pixels.

 |

#### Size

Dimensions of the anchor rectangle. The anchor is a point by default, that is, the width and height are both **0**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Component width, in pixels. Negative values are treated as **0**.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Component height, in pixels. Negative values are treated as **0**.

 |

#### ShareOperationResult

Return value of the **shareCompleted** event, which provides information about the sharing channel used by a user.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.1.0(18)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

targetAbilityInfo

 | 

[ShareAbilityInfo](#section8809223154210)

 | 

Yes

 | 

No

 | 

Information about the sharing channel used by a user.

 |

#### ShareAbilityInfo

Information about the sharing channel used by a user.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.1.0(18)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Sharing channel name, which can be either of the following types:

-   A system operation name, which has a fixed value. For details, please refer to [ShareAbilityName](#section16531512163920).
-   A non-system operation name, which is in _\[bundleName\]_#_\[moduleName\]_#_\[abilityName\]_ format.

 |

#### ContactInfo

Contact information recommended by Intents Kit. When content is shared to a recommended contact, this parameter is passed.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

contactType

 | 

string

 | 

No

 | 

No

 | 

Contact type. The value comes from the value of **entityName** in the data provided by an app to Intents Kit, for example, **Contact** or **ChatGroup**.

 |
| 

contactId

 | 

string

 | 

No

 | 

No

 | 

Contact ID. The value comes from the value of **entityId** in the data provided by an app to Intents Kit.

 |

#### SharePreviewMode

Preview mode of the shared content. The detailed preview image mode is recommended for images and videos.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

0

 | 

Default mode (thumbnail card). This mode is recommended for text and links.

 |
| 

DETAIL

 | 

1

 | 

Detailed preview image. This mode is recommended for images and videos.

 |

#### SelectionMode

Selection mode.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SINGLE

 | 

0

 | 

Single selection mode. When multiple shared data records (**SharedRecord**) are passed, the user needs to select one from them for sharing.

 |
| 

BATCH

 | 

1

 | 

Batch mode, in which all data records are shared.

 |

#### ShareAbilityType

Defines system capabilities that are excluded from the operation area.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COPY\_TO\_PASTEBOARD

 | 

0

 | 

Copy.

 |
| 

SAVE\_TO\_MEDIA\_ASSET

 | 

1

 | 

Save to Gallery.

 |
| 

SAVE\_AS\_FILE

 | 

2

 | 

Save as.

 |
| 

PRINT

 | 

3

 | 

Print.

 |
| 

SAVE\_TO\_SUPERHUB

 | 

4

 | 

Add to SuperHub.

 |

#### ShareAbilityResultCode

Result code returned from UIExtensionAbility, which controls the behavior of the sharing panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ERROR

 | 

\-1

 | 

An error occurred. If the **message** parameter is also passed, a toast message will be displayed.

 |
| 

BACK

 | 

0

 | 

Returns to the sharing panel after a user taps the back button.

 |
| 

CLOSE

 | 

1

 | 

Closes the sharing panel after a user taps the close button.

 |

#### ShareAbilityName

System operation name, which is used to return the sharing result data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COPY\_TO\_PASTEBOARD

 | 

SystemShare\_CopyToPasteboard

 | 

Copy.

 |
| 

SAVE\_TO\_MEDIA\_ASSET

 | 

SystemShare\_SaveToMediaAsset

 | 

Save to Gallery.

 |
| 

SAVE\_AS\_FILE

 | 

SystemShare\_SaveAsFile

 | 

Save as.

 |
| 

PRINT

 | 

SystemShare\_Print

 | 

Print.

 |
| 

SAVE\_TO\_SUPERHUB

 | 

SystemShare\_Superhub

 | 

Add to SuperHub.

 |
| 

COLLECTION

 | 

SystemShare\_Collection

 | 

Celia Knowledge Base.

 |
| 

HARMONYSHARE

 | 

SystemShare\_HarmonyShare

 | 

Huawei Share.

 |
| 

ENCRYPT

 | 

SystemShare\_Encrypt

 | 

Encrypted sharing.

 |

#### SharedData

Shared data object, which provides the method of encapsulating a group of data records.

A shared data object must have at least one record. The first record must be passed using the first parameter of the constructor during **SharedData** instantiation. If the shared data contains multiple records, you need to use the **addRecord(record: SharedRecord)** method to add subsequent records.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/5umgY7dRQwaIG6igICp87A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D69C6BB57C438B8BAF5C6023A2F7C89F223C51B5B447A37FB47DEF775DCA797)

A **SharedData** object supports a maximum of 500 data records, with a total size limit of 200 KB due to IPC transmission constraints.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(record: SharedRecord)

Constructs a **SharedData** object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

record

 | 

[SharedRecord](#section20696483813)

 | 

Yes

 | 

Shared data record.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData'; 

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

#### \[h2\]addRecord

addRecord(record: SharedRecord): void

Adds a data record to the current shared data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

record

 | 

[SharedRecord](#section20696483813)

 | 

Yes

 | 

**SharedRecord** object, which is to be added to **SharedData**.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1003700001](../arkts-api-error-codes/document.md#section16205152494111)

 | 

The number of records exceeds the maximum.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData'; 

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});

#### \[h2\]getRecords

getRecords(): Array<SharedRecord>

Obtains all data records of the current shared data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Array<[SharedRecord](#section20696483813)\>

 | 

All records contained in the current **SharedData** object.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData'; 

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

let records: systemShare.SharedRecord\[\] = data.getRecords();
records.forEach((record: systemShare.SharedRecord) => {
  // To do things.
});

#### ShareController

The display mode of the sharing panel varies according to devices. Different preview modes and sharing methods are provided for apps based on screen specifications and parameters.

-   On phones, the sharing panel is displayed in modal mode by default. When phones are in landscape or unfolded mode, the sharing panel is displayed as a dialog box.
-   On 2-in-1 devices and tablets, the sharing panel is displayed in pop-up mode, which requires the anchor information to be passed.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

#### \[h2\]constructor

constructor(data: SharedData)

A constructor used to create the sharing panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

data

 | 

[SharedData](#section816451553012)

 | 

Yes

 | 

Shared data.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);

#### \[h2\]show

show(context: common.UIAbilityContext, options: ShareControllerOptions): Promise<void>

Displays the sharing panel. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context object for starting the sharing panel.

 |
| 

options

 | 

[ShareControllerOptions](#section107934816010)

 | 

Yes

 | 

Sharing controller configuration items.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1003702001](../arkts-api-error-codes/document.md#section1559215645516)

 | 

Record types are not support.(The batch and multiple selection modes support { @link UDMF.File } type records only.)

 |
| 

[1003702002](../arkts-api-error-codes/document.md#section1761113519576)

 | 

IPC data is oversized.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
export struct ShareUtdText {
  build() {
  }

  private share() {
    // Construct **ShareData**. You need to configure a valid data record.
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.TEXT,
      content: 'This is a piece of text.'
    });
    // Display the sharing panel.
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DETAIL,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(\`ShareController show error. code: ${error.code}, message: ${error.message}\`);
    });
  }
}

#### \[h2\]on('dismiss')

on(event: 'dismiss', callback: () => void): void

Registers a listener for sharing panel closing events.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

string

 | 

Yes

 | 

Event callback type. The supported event is **dismiss**. This event is triggered when the sharing panel is closed.

 |
| 

callback

 | 

() => void

 | 

Yes

 | 

Event callback.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});
data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
controller.on('dismiss', () => {
  console.info('Share panel closed');
});

#### \[h2\]off('dismiss')

off(event: 'dismiss', callback: () => void): void

Unregisters a listener for sharing panel closing events.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

string

 | 

Yes

 | 

Event callback type. The supported event is **dismiss**. It's used to unregister a listener for sharing panel closing events.

 |
| 

callback

 | 

() => void

 | 

Yes

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});
data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
let callback = () => {
  console.info('Share panel closed');
};
controller.on('dismiss', callback);
controller.off('dismiss', callback);

#### \[h2\]on('shareCompleted')

on(type: 'shareCompleted', callback: Callback<ShareOperationResult>): void

Registers a sharing completion event listener. This API returns the sharing channel used by a user, which can be used for data statistics.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 5.1.0(18)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event callback type. The supported event is **shareCompleted**. This event is triggered when a user completes sharing.

 |
| 

callback

 | 

Callback<[ShareOperationResult](#section17135118312)\>

 | 

Yes

 | 

Event callback.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
  console.info('shareCompleted name:', result.targetAbilityInfo.name);
});

#### \[h2\]off('shareCompleted')

off(type: 'shareCompleted', callback?: Callback<ShareOperationResult>): void

Unregisters a sharing completion event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Device behavior**: This API has no effect on TVs and works on other devices.

**Start version**: 5.1.0(18)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event callback type. The supported event is **shareCompleted**. It's used to unregister a sharing completion event listener.

 |
| 

callback

 | 

Callback<[ShareOperationResult](#section17135118312)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN\_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
let callback = (result: systemShare.ShareOperationResult) => {
  console.info('shareCompleted name:', result.targetAbilityInfo.name);
};
controller.on('shareCompleted', callback);
controller.off('shareCompleted', callback);

#### getSharedData

getSharedData(want: Want): Promise<SharedData>

Parses shared data from **want** obtained by the target app. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ability/want/document.md)

 | 

Yes

 | 

Want information obtained by the target app.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SharedData](#section816451553012)\>

 | 

Promise that returns the shared data.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1003703001](../arkts-api-error-codes/document.md#section13612105175717)

 | 

Parse data failed.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    systemShare.getSharedData(want)
      .then((data: systemShare.SharedData) => {
        data.getRecords().forEach((record: systemShare.SharedRecord) => {        
          // Process the shared data.
        });
        session.loadContent('pages/Index');
      })
      .catch((error: BusinessError) => {
        console.error(\`Failed to getSharedData. Code: ${error.code}, message: ${error.message}\`);
        session.terminateSelf();
      });
  }
}

#### getContactInfo

getContactInfo(want: Want): Promise<ContactInfo>

Parses contact information from **want** obtained by the target app. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ability/want/document.md)

 | 

Yes

 | 

Want information obtained by the target app.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ContactInfo](#section102532316184)\>

 | 

Promise that returns contact information.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1003703001](../arkts-api-error-codes/document.md#section13612105175717)

 | 

Parse data failed.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    systemShare.getContactInfo(want)
      .then(async (contact: systemShare.ContactInfo) => {
        // Process contact information. The target user can be specified based on contact type (such as individual or group) and contact ID.
        // Obtain the shared data.
        let data = await systemShare.getSharedData(want);
      })
      .catch((error: BusinessError) => {
        console.error(\`Failed to getContactInfo. Code: ${error.code}, message: ${error.message}\`);
        // The contact does not exist or an exception occurs when obtaining data.
        session.terminateSelf();
      });
  }
}

#### getWant

getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>

Constructs the **want** data based on **SharedData** and the preview mode. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Jh5akkEqR-uXDrDoqObR2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5943248DD8E5360A0A1C75A5DA0DF11A30883A04AA6163B6C74E191B9CF0F22)

Do not arbitrarily modify parameters in the returned **want** data, as this may lead to unknown errors.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.SystemShare

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

data

 | 

[SharedData](#section816451553012)

 | 

Yes

 | 

Data to be shared to the target app.

 |
| 

options

 | 

[ShareControllerOptions](#section107934816010)

 | 

No

 | 

Sharing controller configuration items.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Want](../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ability/want/document.md)\>

 | 

Promise that returns the **want** information to be shared to the target app.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1003703001](../arkts-api-error-codes/document.md#section13612105175717)

 | 

Parse data failed.

 |

**Example:**

Preview mode not configured

import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // Process the shared data.
    // To do things.
    // Prepare the data to be returned.
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN\_TEXT,
      content: 'Hello HarmonyOS'
    });
    data.addRecord({
      utd: utd.UniformDataType.PNG,
      uri: 'file://.../test.png'
    });
    systemShare.getWant(data)
      .then((want) => {
        console.info('want = ', JSON.stringify(want));
        session!.terminateSelfWithResult({
          resultCode: 2,
          want: want
        })
      })
      .catch((error: BusinessError) => {
        console.error(\`Failed to getWant. Code: ${error.code}, message: ${error.message}\`);
      });
  }
}

Preview mode configured

import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // Process the shared data.
    // To do things.
    // Prepare the data to be returned.
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN\_TEXT,
      content: 'Hello HarmonyOS'
    });
    data.addRecord({
      utd: utd.UniformDataType.PNG,
      uri: 'file://.../test.png'
    });
    let options : systemShare.ShareControllerOptions = {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.SINGLE
    };
    systemShare.getWant(data,options)
      .then((want) => {
        console.info('want = ', JSON.stringify(want));
        session!.terminateSelfWithResult({
          resultCode: 2,
          want: want
        })
      })
      .catch((error: BusinessError) => {
        console.error(\`Failed to getWant. Code: ${error.code}, message: ${error.message}\`);
      });
  }
}
