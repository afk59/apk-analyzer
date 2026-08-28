# statusBarManager (Status Bar Management Service)

This module provides apps with the capability of adding their icons to the status bar. By integrating the corresponding APIs, apps can quickly display their icons and menus in the status bar, and allow users to perform certain operations directly through the status bar icon.

**Start version**: 5.0.0(12)

#### Module Import

import { statusBarManager } from '@kit.DeskTopExtensionKit';

#### statusBarManager.StatusBarItem

Status bar icon parameters.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icons

 | 

[StatusBarIcon](#section1844717231113)

 | 

No

 | 

No

 | 

Image information of an app icon in the status bar.

 |
| 

quickOperation

 | 

[QuickOperation](#section1139214183436)

 | 

No

 | 

No

 | 

Information about the pop-up window displayed when users click an app icon in the status bar.

 |
| 

statusBarGroupMenu

 | 

[StatusBarGroupMenu](#section8291353172219)\[\]

 | 

No

 | 

Yes

 | 

Information about a menu group in a status bar icon's context menu.

The default value is **undefined**.

NOTE:

The total number of level-1 menu items across all groups cannot exceed 20.

 |
| 

hoverTips

 | 

string

 | 

No

 | 

Yes

 | 

Information displayed when the cursor hovers over an app icon in the status bar.

The value length ranges from 1 to 128 characters.

NOTE:

**Start version**: 6.0.2(22)

If this parameter is not set, the [label](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#hapmoduleinfo-1) of the module configured in [statusBarManager.QuickOperation](#section1139214183436) is displayed by default when the cursor hovers over the app icon.

 |

#### statusBarManager.StatusBarIcon

Image information of an app icon in the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

white

 | 

[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Icons displayed against dark wallpapers. Pure white is recommended for these icons. Supported image formats include JPEG, PNG, GIF, WebP, BMP, SVG, ICO, and DNG.

NOTE:

The recommended image size is 24 [vp](../../../../../application-framework/arkui/arkts-components/common-definitions/pixel-units/document.md) × 24 vp.

 |
| 

black

 | 

[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

Icons displayed against light wallpapers. Pure black is recommended for these icons. Supported image formats include JPEG, PNG, GIF, WebP, BMP, SVG, ICO, and DNG.

NOTE:

The recommended image size is 24 vp × 24 vp.

 |

#### statusBarManager.QuickOperation

Information about the pop-up window displayed when users click an app icon in the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Title of the service pop-up window after you click the status bar icon.

Value range: no limit. Overflowing text is replaced with an ellipsis (...).

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

Height of the custom area in the pop-up window displayed when users click an app icon in the status bar, in vp.

The value must be greater than **0**.

 |
| 

abilityName

 | 

string

 | 

No

 | 

No

 | 

[StatusBarViewExtensionAbility](../statusbarviewextensionability-status-bar-extension-ability/document.md) name. The ability corresponds to the custom area in the pop-up window displayed when users click an app icon in the status bar.

NOTE:

If an empty string is passed, clicks can be processed by listening to the [statusBarIconClick](#section18493519506) events.

 |
| 

moduleName

 | 

string

 | 

No

 | 

Yes

 | 

Name of the module to which [StatusBarViewExtensionAbility](../statusbarviewextensionability-status-bar-extension-ability/document.md) belongs. The ability corresponds to the custom area in the pop-up window displayed when users click an app icon in the status bar.

Default value: ''

 |
| 

loadingStatus

 | 

boolean

 | 

No

 | 

Yes

 | 

Whether to load the animation when the level-2 menu is displayed by clicking a status bar icon.

The default value is **false**.

NOTE:

**Start version**: 6.0.0(20)

 |

#### statusBarManager.StatusBarGroupMenu

type StatusBarGroupMenu = StatusBarMenuItem\[\]

Information about a menu group in a status bar icon's context menu.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[StatusBarMenuItem](#section3627115133810)\[\]

 | 

Information about a menu group. A menu group can contain multiple level-1 menu items.

 |

#### statusBarManager.StatusBarMenuItem

Information about a level-1 menu item in a status bar icon's context menu.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Title of a menu item.

Value range: no limit. Overflowing text is replaced with an ellipsis (...).

 |
| 

menuAction

 | 

[StatusBarMenuAction](#section1196811528487)

 | 

No

 | 

Yes

 | 

Menu item action information.

The default value is **undefined**.

NOTE:

Currently, only starting the in-app UIAbility you have defined is supported. At least one of the **menuAction** and **subMenu** parameters must be set.

 |
| 

subMenu

 | 

[StatusBarSubMenuItem](#section18651641195110)\[\]

 | 

No

 | 

Yes

 | 

Submenu items of a level-1 menu item.

The default value is **undefined**.

NOTE:

A level-1 menu can contain up to 20 submenu items.

 |

#### statusBarManager.StatusBarMenuAction

Information about the click action on a status bar icon context menu item.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

abilityName

 | 

string

 | 

No

 | 

No

 | 

Name of the app ability triggered by menu item clicks.

NOTE:

Currently, only UIAbility can be started.

 |
| 

moduleName

 | 

string

 | 

No

 | 

Yes

 | 

Module name of the app ability triggered by menu item clicks.

Default value: ''

 |
| 

notifyOnly

 | 

boolean

 | 

No

 | 

Yes

 | 

Whether to enable notifications for icon context menu item click events.

The options are as follows:

**false**: no. No event notification will be triggered on icon context menu item clicks.

**true**: yes. Event notifications will be triggered on icon context menu item clicks.

The default value is **false**.

NOTE:

When this parameter is set to **true** and **menuCode** is provided, you can process icon context menu item clicks by listening to the [rightMenuClick](#section10893144462716) events.

**Start version**: 5.0.2 (14)

 |
| 

menuCode

 | 

string

 | 

No

 | 

Yes

 | 

Unique ID of the icon context menu item.

Default value: ''

NOTE:

Ensure that the ID is unique to distinguish different menu items.

**Start version**: 5.0.2 (14)

 |

#### statusBarManager.StatusBarSubMenuItem

Information about a level-2 menu item in a status bar icon's context menu.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

subTitle

 | 

string

 | 

No

 | 

No

 | 

Title of a level-2 menu item.

Value range: no limit. Overflowing text is replaced with an ellipsis (...).

 |
| 

menuAction

 | 

[StatusBarMenuAction](#section1196811528487)

 | 

No

 | 

No

 | 

Menu item action information.

NOTE:

Currently, only starting the in-app UIAbility you have defined is supported.

 |

#### statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void

Adds an app icon to the status bar. Currently, only one icon can be added for an app. Repeated adding is invalid.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarItem

 | 

[StatusBarItem](#section105181855219)

 | 

Yes

 | 

Details about the app icon added to the status bar.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710001

 | 

The size of the pixelmap exceeds the limit.

 |
| 

1010710002

 | 

The number of menu items or submenu items exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010710005

 | 

The string length exceeds the threshold.

 |
| 

1010720001

 | 

A menu item contains neither submenu nor menuAction.

 |

**Example:**

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/\*\*
\* Context information can be obtained using the built-in method of the custom component.
\* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // Build icon information.
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // Build information about icon context menu items.
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "Submenu item",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "Level-1 menu item",
    // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
  statusBarGroupMenus.push(statusBarMenuItems);

  // Build information about the pop-up window displayed when users click an app icon in the status bar.
  let operation: statusBarManager.QuickOperation = {
    abilityName: "MyStatusBarViewAbility",
    title: "Test Demo",
    height: 300,
    // Can be left empty.
    moduleName: 'entry'
  };

  // Build information about the icon added to the status bar.
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item);
  } catch (error) {
    console.error(\`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void

Adds an app icon to the status bar. This API returns the result asynchronously through a callback. Currently, only one icon can be added for an app. Repeated adding is invalid.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarItem

 | 

[StatusBarItem](#section105181855219)

 | 

Yes

 | 

Details about the app icon added to the status bar.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function for adding an app icon to the status bar.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710001

 | 

The size of the pixelmap exceeds the limit.

 |
| 

1010710002

 | 

The number of menu items or submenu items exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010710005

 | 

The string length exceeds the threshold.

 |
| 

1010720001

 | 

A menu item contains neither submenu nor menuAction.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // Build icon information.
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // Build information about icon context menu items.
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "Submenu item",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "Level-1 menu item",
    // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
  statusBarGroupMenus.push(statusBarMenuItems);

  // Build information about the pop-up window displayed when users click an app icon in the status bar.
  let operation: statusBarManager.QuickOperation = {
    abilityName: "MyStatusBarViewAbility",
    title: "Test Demo",
    height: 300,
    // Can be left empty.
    moduleName: 'entry'
  };

  // Build information about the icon added to the status bar.
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('addToStatusBar success');
    });
  } catch (error) {
    console.error(\`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context): void

Removes an icon from the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010710004

 | 

The icon cannot be deleted when no window is in the foreground.

 |

**Example:**

import { statusBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context);
  } catch (error) {
    console.error(\`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void

Removes an icon from the status bar. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function for removing an app icon from the status bar.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010710004

 | 

The icon cannot be deleted when no window is in the foreground.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('removeFromStatusBar success');
    });
  } catch (error) {
    console.error(\`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number): void

Updates the height of the custom area in the pop-up window displayed when users click an app icon in the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

height

 | 

number

 | 

Yes

 | 

Height of the custom area in the pop-up window displayed when users click an app icon in the status bar, in vp.

The value must be greater than **0**.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |

**Example:**

import { statusBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height);
  } catch (error) {
    console.error(\`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void

Updates the height of the custom area in the pop-up window displayed when users click an app icon in the status bar. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

height

 | 

number

 | 

Yes

 | 

Height of the custom area in the pop-up window displayed when users click an app icon in the status bar, in vp.

The value must be greater than **0**.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function for updating the height of the custom area in the pop-up window displayed when users click an app icon in the status bar.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height, (error) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateQuickOperationHeight success');
    });
  } catch (error) {
    console.error(\`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu\[\]): void

Updates the content of a status bar icon's context menu.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarGroupMenus

 | 

[StatusBarGroupMenu](#section8291353172219)\[\]

 | 

Yes

 | 

New information about the status bar icon's context menu.

NOTE:

The total number of level-1 menu items across all groups cannot exceed 20.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710002

 | 

The number of menu items or submenu items exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010720001

 | 

A menu item contains neither submenu nor menuAction.

 |

**Example:**

import { statusBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function updateStatusBarMenu(context: Context) {
  // Build information about icon context menu items.
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "Level-2 menu item",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "Level-1 menu item",
    // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
  } catch (error) {
    console.error(\`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu\[\], callback: AsyncCallback<void>): void

Updates the content of a status bar icon's context menu. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarGroupMenus

 | 

[StatusBarGroupMenu](#section8291353172219)\[\]

 | 

Yes

 | 

New information about the status bar icon's context menu.

NOTE:

The total number of level-1 menu items across all groups cannot exceed 20.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function for updating the content of a status bar icon's context menu.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710002

 | 

The number of menu items or submenu items exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010720001

 | 

A menu item contains neither submenu nor menuAction.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
function updateStatusBarMenu(context: Context) {
  // Build information about icon context menu items.
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "Level-2 menu item",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "Level-1 menu item",
    // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus, (err: BusinessError) => {
      if (err) {
        // ...
        return;
      }
      console.info('updateStatusBarMenu success');
    });
  } catch (error) {
    console.error(\`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void

Updates the app icon added to the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarIcon

 | 

[StatusBarIcon](#section1844717231113)

 | 

Yes

 | 

Updated icon.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710001

 | 

The size of the pixelmap exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |

**Example:**

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // Build icon information.
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons);
  } catch (error) {
    console.error(\`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void

Updates the app icon added to the status bar. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

statusBarIcon

 | 

[StatusBarIcon](#section1844717231113)

 | 

Yes

 | 

Updated icon.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function for updating an app icon added to the status bar.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

The parameter check failed.

 |
| 

1010710001

 | 

The size of the pixelmap exceeds the limit.

 |
| 

1010710003

 | 

The API is being called too frequently.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // Build icon information.
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateStatusBarIcon success');
    });
  } catch (error) {
    console.error(\`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### statusBarManager.on('statusBarIconClick')

on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void

Listens for status bar icon click events.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

Event callback type. The event **'statusBarIconClick'** is supported. When an app icon is clicked, the event is triggered.

NOTE:

When [addToStatusBar](#section665018220561) is called and **abilityName** is not specified in [quickOperation](#section1139214183436), clicks can be processed by listening to the **statusBarIconClick** events.

 |
| 

callback

 | 

Callback<[emitter.EventData](../../../basic-services-kit/arkts-apis/process-and-thread-communication/ohos-events-emitter-emitter/document.md#eventdata)\>

 | 

Yes

 | 

Callback function to be registered. The callback returns icon click information.

NOTE:

Returned information:

\- **iconClickType**: click event type. Currently, only left-click events are supported.

 |

**Example**:

private onStatusBarIconClick = (eventData: emitter.EventData) => {
  // Customize the pop-up window displayed when users click an app icon.
  let data = eventData.data;
  if (data) {
    switch (data\['iconClickType'\]) {
      case 'leftClickType':
        // Customize the pop-up window displayed when users click an app icon.
        break;
      default:
        break;
    }
  }
}

// Listen for status bar icon click events.
statusBarManager.on('statusBarIconClick', this.onStatusBarIconClick);

#### statusBarManager.off('statusBarIconClick')

off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void

Unregisters listeners for status bar icon click events.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

Event callback type. The event **'statusBarIconClick'** is supported.

 |
| 

callback

 | 

Callback<[emitter.EventData](../../../basic-services-kit/arkts-apis/process-and-thread-communication/ohos-events-emitter-emitter/document.md#eventdata)\>

 | 

No

 | 

Callback function to be unregistered.

The default value is **undefined**.

NOTE:

If no callback is passed, this API unregisters all callbacks for the event.

If a callback is passed, it must be the same object used in the **on** method. Otherwise, the callback function will not be unregistered, leading to potential memory leaks.

 |

**Example**:

private onStatusBarIconClick = (eventData: emitter.EventData) => {
  // Customize the pop-up window displayed when users click an app icon.
  let data = eventData.data;
  if (data) {
    switch (data\['iconClickType'\]) {
      case 'leftClickType':
        // Customize the pop-up window displayed when users click an app icon.
        break;
      default:
        break;
    }
  }
}
// Unregister the event callback function.
statusBarManager.off('statusBarIconClick', this.onStatusBarIconClick);

// Unregister the event listener.
statusBarManager.off('statusBarIconClick');

#### statusBarManager.on('rightMenuClick')

on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void

Listens for click events on status bar icon context menu items.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

Event callback type. The event **'rightMenuClick'** is supported. When an item in the app icon context menu is clicked, this event is triggered.

NOTE:

This parameter takes effect when **notifyOnly** is set to **true** and **menuCode** is specified in [menuAction](#section1196811528487) of a menu item updated via [updateStatusBarMenu](#section188071452172811).

 |
| 

callback

 | 

Callback<[emitter.EventData](../../../basic-services-kit/arkts-apis/process-and-thread-communication/ohos-events-emitter-emitter/document.md#eventdata)\>

 | 

Yes

 | 

Callback function to be registered. The callback returns information about icon context menu clicks.

NOTE:

Returned information:

\- **menuCode**: unique ID of a clicked menu item.

 |

**Example**:

private onRightMenuClick = (eventData: emitter.EventData) => {
  // Customize the icon context menu item click logic.
  let data = eventData.data;
  if (data) {
    let menuCode = data\['menuCode'\] as string;
    // Process the click on a menu item.
  }
}

// Listen for context menu item click events.
statusBarManager.on('rightMenuClick', this.onRightMenuClick);

#### statusBarManager.off('rightMenuClick')

off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void

Unregisters listeners for click events on status bar icon context menu items.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.2 (14)

**Parameters**:

| 
Name

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

Event callback type. The event **'rightMenuClick'** is supported.

 |
| 

callback

 | 

Callback<[emitter.EventData](../../../basic-services-kit/arkts-apis/process-and-thread-communication/ohos-events-emitter-emitter/document.md#eventdata)\>

 | 

No

 | 

Callback function to be unregistered.

The default value is **undefined**.

NOTE:

If no callback is passed, this API unregisters all callbacks for the event.

If a callback is passed, it must be the same object used in the **on** method. Otherwise, the callback function will not be unregistered, leading to potential memory leaks.

 |

**Example**:

private onRightMenuClick = (eventData: emitter.EventData) => {
  // Customize the icon context menu item click logic.
  let data = eventData.data;
  if (data) {
    let menuCode = data\['menuCode'\] as string;
    // Process the click on a menu item.
  }
}

// Unregister the event callback function.
statusBarManager.off('rightMenuClick', this.onRightMenuClick);

// Unregister the event listener.
statusBarManager.off('rightMenuClick');

#### statusBarManager.updateStatusBarHoverTips

updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>

Updates the content displayed when the cursor hovers over an app icon in the status bar.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 6.0.2(22)

**Parameters:**

| 
Name

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context.

NOTE:

Currently, the context supports only its child classes **UIAbilityContext**, **ServiceExtensionContext**, and **FormExtensionContext**.

 |
| 

hoverTips

 | 

string

 | 

Yes

 | 

Information displayed when the cursor hovers over an app icon in the status bar.

The value contains 1 to 128 characters.

 |

**Returns:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010710003

 | 

The API is being called too frequently.

 |
| 

1010710005

 | 

The string length exceeds the threshold.

 |

**Example**:

import { statusBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function updateStatusBarHoverTips(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let hoverTips: string = 'hoverTips';
  try {
    await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
  } catch (error) {
    console.error(\`updateStatusBarHoverTips failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}
