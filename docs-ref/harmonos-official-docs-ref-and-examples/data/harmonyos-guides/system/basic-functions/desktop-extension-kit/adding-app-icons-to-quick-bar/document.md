# Adding App Icons to Quick Bar

Since version 6.0.2(22), app icons can be added to the quick bar.

#### Use Cases

The quick bar refers to the icon area at the bottom of the screen on a PC/2-in-1 device, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/iKvm_Z3uQSiRdojJhSQ3Iw/en-us_image_0000002502219756.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EBE7A7F1550E420D83F1F21ACA33052F1C2659B19F06B75660CBB72A8AD4CEC "Click to enlarge")

After an app icon is added to the quick bar, the icon menu will display the customized menu items. You can add, delete, update, and query menu items. The following is an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/y6cpmkpxTIG38MgCnZv67g/en-us_image_0000002502220322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A749BACC0A1002221E98CD81CDEC5FEFCF1B83F54DACA1C483928498316075F5 "Click to enlarge")

#### API Description

The following lists the APIs related to operating an app icon in the quick bar. For details, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/bG4ljsUMQziyYv035SZFXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B856ACC6545BA2AAA2173E21E931BC06A32FB7E67DA62348940E801FAC46C549)

The APIs provided by DeskTop Extension Kit take effect only on 2-in-1 devices.

**Table 1** APIs related to operating an app icon in the quick bar
| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getCustomCategories](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section161446211272)(context: common.Context): Promise<CustomCategory\[\]>

 | 

Obtains all categories defined in the quick bar menu.

 |
| 

[addCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section665018220561)(context: common.Context, categoryName: string): Promise<CustomCategory>

 | 

Adds a quick bar menu category.

 |
| 

[updateCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1623472312366)(context: common.Context, category: CustomCategory): Promise<void>

 | 

Updates a quick bar menu category.

 |
| 

[deleteCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section11581123516468)(context: common.Context, categoryId: number): Promise<void>

 | 

Deletes a quick bar menu category.

 |
| 

[getTasksFromCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section103873266327)(context: common.Context, categoryId: number): Promise<QuickTask\[\]>

 | 

Obtains all tasks in a quick bar menu category.

 |
| 

[addQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section13991750101114)(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>

 | 

Adds a quick bar menu task.

 |
| 

[updateQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1427319917408)(context: common.Context, task: QuickTask): Promise<void>

 | 

Updates a quick bar menu task.

 |
| 

[deleteQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1259314566431)(context: common.Context, taskId: number): Promise<void>

 | 

Deletes a quick bar menu task.

 |

#### Development Procedure

1.  Import required modules.
    
    import { quickBarManager }  from '@kit.DeskTopExtensionKit';
    import { UIExtensionContentSession, Want, UIAbility } from '@kit.AbilityKit';
    import { image } from '@kit.ImageKit';
    import { resourceManager } from '@kit.LocalizationKit';
    
2.  Create a **TestAbility.ets** file (for example, in the **entry/src/main/ets/entryability** directory) and a **TestIndex** page (for example, in the **entry/src/main/ets/pages** directory), which is the page to display after the icon menu task is clicked.
    
    let TAG = 'TestAbility';
    export default class TestAbility extends UIAbility {
      onCreate() {
        console.info(TAG, \`onCreate\`);
      }
    
      onSessionCreate(want: Want, session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionCreate, want: ${want.abilityName}\`);
        // **pages/TestIndex** is the page that is displayed after the menu task is clicked.
        session.loadContent('pages/TestIndex');
      }
    
      onForeground() {
        console.info(TAG, \`onForeground\`);
      }
    
      onBackground() {
        console.info(TAG, \`onBackground\`);
      }
    
      onSessionDestroy(session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionDestroy\`);
      }
    
      onDestroy() {
        console.info(TAG, \`onDestroy\`);
      }
    }
    
3.  Configure the ability information in the **module.json5** file of the module to which **TestAbility** belongs.
    
    {
      "name": "TestAbility",
      "srcEntry": "./ets/entryability/TestAbility.ets",
      "description": "$string:EntryAbility\_desc",
      "icon": "$media:layered\_image",
      "label": "$string:EntryAbility\_label",
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start\_window\_background",
      "exported": true,
      "skills": \[
        {
          "entities": \[
            "entity.system.home"
          \],
          "actions": \[
            "action.system.home"
          \]
        }
      \],
    }
    
4.  In the page component (for example, **TestIndex.ets**), call the [addCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section665018220561) API to add a quick bar menu category. You can add tasks to the category only after the category is added.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context === undefined) {
      return;
    }
    try {
      const res = await quickBarManager.addCustomCategory(context, 'Recent tasks');
      console.info(\`customCategory info: ${JSON.stringify(res)}\`);
    } catch (error) {
      console.error(\`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
5.  After adding a category, you can call the [addQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section13991750101114) API to add tasks to the category. The added menu item will be displayed after you right-click the app icon in the quick bar.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context === undefined) {
      return;
    }
    // Obtain a resource manager.
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    // Create **pixelMap** for the task. You need to preset the **testImage.png** image in the **rawfile** folder.
    const fileData = resourceMgr.getRawFileContentSync('testImage.png');
    const imageSource = image.createImageSource(fileData.buffer);
    const imagePixelMap = await imageSource.createPixelMap();
    let parameters: quickBarManager.ParameterItem = {
      key: 'testKey',
      value: 'testValue'
    }
    // Build task information.
    const task: quickBarManager.QuickTaskInfo = {
      taskName: 'Test task name',
      abilityName: 'TestAbility',
      // This parameter is optional.
      moduleName: 'entry',
      // This parameter is optional.
      taskIcon: imagePixelMap,
      // This parameter is optional.
      taskDetail: 'Task description',
      // This parameter is optional.
      parameters: \[parameters\]
    }
    
    try {
      // Obtain all category information and add the task to the desired category.
      const categoryList = await quickBarManager.getCustomCategories(context);
      // Add the task to the first category.
      const res = await quickBarManager.addQuickTask(context, categoryList\[0\].categoryId, task);
      console.info(\`quickTask info: ${JSON.stringify(res)}\`);
    } catch (error) {
      console.error(\`addQuickTask failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
6.  Call the [getCustomCategories](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section161446211272) API to obtain the information about all categories.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context === undefined) {
      return;
    }
    try {
      const res = await quickBarManager.getCustomCategories(context);
      console.info(\`customCategoryList info: ${JSON.stringify(res)}\`);
    } catch (error) {
      console.error(\`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
7.  Call the [getTasksFromCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section103873266327) API to obtain information about all tasks in a category. In this example, information about all tasks in the first category is obtained.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context === undefined) {
      return;
    }
    try {
      // Obtain all category information and the tasks in the category.
      const category = await quickBarManager.getCustomCategories(context);
      // Obtain all tasks in the first category.
      const res = await quickBarManager.getTasksFromCategory(context, category\[0\].categoryId);
      console.info(\`quickTaskList info: ${JSON.stringify(res)}\`);
    } catch (error) {
      console.error(\`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
8.  Call the [updateCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1623472312366) API to update the quick bar menu category information, and update the category name.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
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
    
9.  Call the [updateQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1427319917408) API to update the quick bar menu task information, including the task icon.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context === undefined) {
      return;
    }
    // Obtain a resource manager.
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    // Create **pixelMap** for the task. You need to preset the **testUpdateImage.png** image in the **rawfile** folder.
    const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
    const imageSource = image.createImageSource(fileData.buffer);
    const imagePixelMap = await imageSource.createPixelMap();
    let parameters: quickBarManager.ParameterItem = {
      key: 'testKey',
      value: 'testValue'
    }
    // Build task information.
    const taskInfo: quickBarManager.QuickTaskInfo = {
      taskName: 'Test task name',
      abilityName: 'TestAbility',
      // This parameter is optional.
      moduleName: 'entry',
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
    
10.  Call the [deleteQuickTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section1259314566431) API to delete unnecessary quick bar menu tasks. In this example, the task whose **taskId** is **1** is deleted.
     
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (context === undefined) {
       return;
     }
     try {
       // Delete the task whose **taskId** is **1**.
       await quickBarManager.deleteQuickTask(context, 1);
     } catch (error) {
       console.error(\`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}\`);
     }
     
11.  Call the [deleteCustomCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/desktop-quickbar-extension-manager#section11581123516468) API to delete the unnecessary quick bar menu category. In this example, the category whose **categoryId** is **1** is deleted, and all tasks in the category are also deleted.
     
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (context === undefined) {
       return;
     }
     try {
       // Delete the category whose **categoryId** is **1**.
       await quickBarManager.deleteCustomCategory(context, 1);
     } catch (error) {
       console.error(\`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}\`);
     }
