# quickBarManager (Quick Bar Management Service)

This module provides apps with the capability of adding their icons to the quick bar. Apps can customize their quick bar context menus by calling the corresponding APIs.

**Start version**: 6.0.2(22)

#### Module Import

import { quickBarManager } from '@kit.DeskTopExtensionKit';

#### quickBarManager.QuickTaskInfo

Detailed parameters of the quick bar menu task.

**System capability**: SystemCapability.PCService.QuickBarManager

**Start version**: 6.0.2(22)

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

taskName

 | 

string

 | 

No

 | 

No

 | 

Name of the quick bar icon menu task.

The value contains 1 to 512 characters and cannot be empty.

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

Name of the app ability started when users click a menu task.

The value contains 1 to 512 characters and cannot be empty.

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

Name of the module to which the app ability to be started when a menu task is clicked belongs.

The value contains 1 to 512 characters and cannot be empty.

Default value: ''

 |
| 

taskIcon

 | 

[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Yes

 | 

Image information of the quick bar icon menu task. The JPEG, PNG, GIF, WebP, BMP, SVG, ICO, and DNG image formats are supported.

The default value is **undefined**.

NOTE:

An image of 512 vp x 512 vp is recommended. If no image information is passed, the app icon is used as the task icon.

 |
| 

taskDetail

 | 

string

 | 

No

 | 

Yes

 | 

Description of the quick bar icon menu task.

Default value: ''

 |
| 

parameters

 | 

[ParameterItem](#section1217412444191)\[\]

 | 

No

 | 

Yes

 | 

Custom parameters of the quick bar icon menu task.

The number of elements in the array cannot exceed 64.

The default value is **undefined**.

 |

#### quickBarManager.QuickTask

Information about the quick bar menu task of an app.

**System capability**: SystemCapability.PCService.QuickBarManager

**Start version**: 6.0.2(22)

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

taskId

 | 

number

 | 

Yes

 | 

No

 | 

ID of the quick bar icon menu task.

 |
| 

categoryId

 | 

number

 | 

Yes

 | 

No

 | 

ID of the quick bar icon menu category.

 |
| 

taskInfo

 | 

[QuickTaskInfo](#section105181855219)

 | 

No

 | 

No

 | 

Information about the quick bar task.

 |

#### quickBarManager.ParameterItem

Custom parameter of the quick bar menu task, which is **WantParams**. You can customize the key-value pair.

**System capability**: SystemCapability.PCService.QuickBarManager

**Start version**: 6.0.2(22)

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

key

 | 

string

 | 

No

 | 

No

 | 

Key of the custom parameter.

The value contains 1 to 512 characters and cannot be empty.

 |
| 

value

 | 

string

 | 

No

 | 

No

 | 

Value of the custom parameter.

The value contains 1 to 512 characters and cannot be empty.

 |

#### quickBarManager.CustomCategory

Information about the quick bar menu category of an app.

**System capability**: SystemCapability.PCService.QuickBarManager

**Start version**: 6.0.2(22)

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

categoryId

 | 

number

 | 

Yes

 | 

No

 | 

ID of the quick bar icon menu category.

 |
| 

categoryName

 | 

string

 | 

No

 | 

No

 | 

Name of the quick bar icon menu category.

The value contains 1 to 512 characters and cannot be empty.

 |

#### quickBarManager.addCustomCategory

addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>

Method for an app to access the quick bar. The app can call the **addCustomCategory** API to add a quick bar category. Then the app can add tasks to the category. A maximum of three categories can be added.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

categoryName

 | 

string

 | 

Yes

 | 

Name of the quick bar icon menu category.

The value contains 1 to 512 characters and cannot be empty.

 |

**Returns:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CustomCategory](#section19779819185015)\>

 | 

Promise object, which returns menu category information.

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

1020210001

 | 

Maximum number of categories reached

 |
| 

1020210002

 | 

Duplicate category name.

 |
| 

1020210008

 | 

The string length exceeds the threshold

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function addCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.addCustomCategory(context, 'Recent tasks');
    console.info(\`customCategory info: ${JSON.stringify(res)}\`);
  } catch (error) {
    console.error(\`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.addQuickTask

addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>

Method for an app to access the quick bar. The app can call the **addQuickTask** API to add a quick bar task. The added menu item will be displayed after you right-click the app icon on the quick bar.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

categoryId

 | 

number

 | 

Yes

 | 

ID of the quick bar icon menu category.

 |
| 

taskInfo

 | 

[QuickTaskInfo](#section105181855219)

 | 

Yes

 | 

Detailed information of the quick bar icon menu task.

 |

**Returns:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QuickTask](#section16180063819)\>

 | 

Promise object, which returns menu task information.

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

1020210003

 | 

Category not found.

 |
| 

1020210008

 | 

The string length exceeds the threshold

 |
| 

1020210009

 | 

Invalid parameter.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function addQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // Create **pixelMap** for the task. You need to preset the **testImage.png** image in the **rawfile** folder.
  const whiteFileData = resourceMgr.getRawFileContentSync('testImage.png');
  const whiteImageSource = image.createImageSource(whiteFileData.buffer);
  const imagePixelMap = await whiteImageSource.createPixelMap();
  // Build parameters.
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  // Build QuickTaskInfo.
  let task: quickBarManager.QuickTaskInfo = {
    taskName: 'Test task name',
    abilityName: 'TestAbility1',
    moduleName: 'entry',
    // This parameter is optional.
    taskIcon: imagePixelMap,
    // This parameter is optional.
    taskDetail: 'Task description',
    parameters: \[parameters\]
  }
  try {
    // Obtain all category information and add the task to the desired category.
    const categoryList = await quickBarManager.getCustomCategories(context);
    // Add the task to the first category.
    let res = await quickBarManager.addQuickTask(context, categoryList\[0\].categoryId, task);
    console.info(\`quickTask info: ${JSON.stringify(res)}\`);
  } catch (error) {
    console.error(\`addQuickTask failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.getCustomCategories

getCustomCategories(context: common.Context): Promise<CustomCategory\[\]>

Method for an app to access the quick bar. The app can call the **getCustomCategories** API to obtain all categories defined in the quick bar.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |

**Returns:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CustomCategory](#section19779819185015)\[\]>

 | 

Promise object, which returns all menu category information.

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

1020210003

 | 

Category not found.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function getCustomCategories(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.getCustomCategories(context);
    console.info(\`customCategoryList info: ${JSON.stringify(res)}\`);
  } catch (error) {
    console.error(\`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.getTasksFromCategory

getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask\[\]>

Method for an app to access the quick bar. An app can obtain information about all tasks in the quick bar category by calling the **getTasksFromCategory** API.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

categoryId

 | 

number

 | 

Yes

 | 

ID of the quick bar icon menu category.

 |

**Returns:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

Promise<[QuickTask](#section16180063819)\[\]>

 | 

Promise object, which returns the information about all tasks in a category.

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

1020210003

 | 

Category not found.

 |
| 

1020210004

 | 

Quick task not found.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function getTasksFromCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // Obtain all category information and the tasks in the category.
    const category = await quickBarManager.getCustomCategories(context);
    // Obtain all tasks in the first category.
    const res = await quickBarManager.getTasksFromCategory(context, category\[0\].categoryId)
    console.info(\`quickTaskList info: ${JSON.stringify(res)}\`);
  } catch (error) {
    console.error(\`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.updateCustomCategory

updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>

Method for an app to access the quick bar. The app can call the **updateCustomCategory** API to update a quick bar category.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

category

 | 

[CustomCategory](#section19779819185015)

 | 

Yes

 | 

Information of the quick bar icon menu category.

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

1020210002

 | 

Duplicate category name.

 |
| 

1020210003

 | 

Category not found.

 |
| 

1020210008

 | 

The string length exceeds the threshold

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function updateCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  const category: quickBarManager.CustomCategory = {
    categoryId: 1,
    categoryName: 'demo'
  }
  try {
    await quickBarManager.updateCustomCategory(context, category);
  } catch (error) {
    console.error(\`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.updateQuickTask

updateQuickTask(context: common.Context, task: QuickTask): Promise<void>

Method for an app to access the quick bar. The app can call the **updateQuickTask** API to update a quick bar task.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

task

 | 

[QuickTask](#section16180063819)

 | 

Yes

 | 

Information of the quick bar icon menu task.

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

1020210004

 | 

Quick task not found.

 |
| 

1020210008

 | 

The string length exceeds the threshold

 |
| 

1020210009

 | 

Invalid parameter.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function updateQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // Create **pixelMap** for the task. You need to preset the **testUpdateImage.png** image in the **rawfile** folder.
  const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();
  // Build parameters.
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let taskInfo: quickBarManager.QuickTaskInfo = {
    taskName: 'newTaskName',
    abilityName: 'newEntryAbility',
    moduleName: 'newModuleName',
    // This parameter is optional.
    taskIcon: imagePixelMap,
    // This parameter is optional.
    taskDetail: 'Task description',
    // This parameter is optional.
    parameters: \[parameters\]
  }

  const task: quickBarManager.QuickTask = {
    taskId: 1,
    categoryId: 1,
    taskInfo: taskInfo
  }

  try {
    await quickBarManager.updateQuickTask(context,task);
  } catch (error) {
    console.error(\`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.deleteQuickTask

deleteQuickTask(context: common.Context, taskId: number): Promise<void>

Method for an app to access the quick bar. The app can call the **deleteQuickTask** API to delete a quick bar task.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

taskId

 | 

number

 | 

Yes

 | 

ID of the quick bar icon menu task.

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

1020210004

 | 

Quick task not found.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function deleteQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // Delete the task whose ID is 1.
    await quickBarManager.deleteQuickTask(context, 1);
  } catch (error) {
    console.error(\`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}

#### quickBarManager.deleteCustomCategory

deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>

Method for an app to access the quick bar. The app can call the **deleteCustomCategory** API to delete a quick bar category, and all tasks in the category will be deleted accordingly.

**System capability**: SystemCapability.PCService.QuickBarManager

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

 |
| 

taskId

 | 

number

 | 

Yes

 | 

ID of the quick bar icon menu task.

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

1020210003

 | 

Category not found.

 |

**Example:**

import { quickBarManager } from '@kit.DeskTopExtensionKit';

/\*\*
 \* Context information can be obtained using the built-in method of the custom component.
 \* Specific method: **this.getUIContext().getHostContext()**;
 \*/
async function deleteCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // Delete the category whose ID is 1.
    await quickBarManager.deleteCustomCategory(context, 1);
  } catch (error) {
    console.error(\`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}\`);
  }
}
