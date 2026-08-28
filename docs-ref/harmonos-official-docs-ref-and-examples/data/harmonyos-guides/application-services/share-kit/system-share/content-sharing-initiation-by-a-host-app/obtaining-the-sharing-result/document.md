# Obtaining the Sharing Result

#### Use Case

Starting from version 5.1.0(18), host apps can obtain sharing results.

You can collect statistics on the channels to which users share content based on your service requirements. The sharing channel information falls into either of the following types:

-   A system operation name, which has a fixed value. For details, please refer to [ShareAbilityName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-system-share#section16531512163920).
-   A non-system operation name, which is in _\[bundleName\]_#_\[moduleName\]_#_\[abilityName\]_ format.

#### Development Procedure

1.  Import required modules.
    
    import { common } from '@kit.AbilityKit';
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    
2.  Construct the data to be shared.
    
    // Construct **ShareData**. You need to configure a valid data record.
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN\_TEXT,
      content: 'Hello HarmonyOS'
    });
    
3.  Register a sharing result event listener and start the sharing panel.
    
    // Build **ShareController**.
    let controller: systemShare.ShareController = new systemShare.ShareController(data);
    // Obtain the **UIAbility** context object.
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    // Register a sharing result event listener.
    controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
      console.info('shareCompleted name:', result.targetAbilityInfo.name);
      // Collect statistics based on the sharing channel.
    });
    
    // Display the sharing panel.
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DEFAULT,
      selectionMode: systemShare.SelectionMode.SINGLE
    });
