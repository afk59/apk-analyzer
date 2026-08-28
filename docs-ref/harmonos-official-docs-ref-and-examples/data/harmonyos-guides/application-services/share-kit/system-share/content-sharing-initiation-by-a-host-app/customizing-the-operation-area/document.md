# Customizing the Operation Area

#### Use Case

The operation area provides system-level shortcut operations, such as Copy, Save, Save as, Print, and Copy to SuperHub. The host app determines the operations displayed to users based on the service requirements.

For example, if the shared images do not need to be printed, the print button can be removed from the operation area.

#### Development Procedure

1.  Import required modules.
    
    import { common } from '@kit.AbilityKit';
    import { fileUri } from '@kit.CoreFileKit';
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    
2.  Construct the data to be shared. You can add multiple sharing records.
    
    // Construct **ShareData**. You need to configure a valid data record.
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN\_TEXT,
      content: 'Hello HarmonyOS'
    });
    // You can call **addRecord** to add multiple records one by one. You can share one or more records at a time by setting **selectionMode**.
    let uiContext: UIContext = this.getUIContext();
    let contextFaker: Context = uiContext.getHostContext() as Context;
    let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // This is only an example. Replace it with the correct file path.
    data.addRecord({
      utd: utd.UniformDataType.PNG,
      uri: fileUri.getUriFromPath(filePath)
    });
    
3.  Start the sharing panel and configure not to display the print shortcut operation. For details about how to shield other system-level shortcut operations, please refer to [ShareAbilityType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-system-share#section205631342153016).
    
    // Build **ShareController**.
    let controller: systemShare.ShareController = new systemShare.ShareController(data);
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    // Register a listener for sharing panel closing events.
    controller.on('dismiss', () => {
      console.info('Share panel closed');
      // The sharing ends and other services can be processed.
    });
    // Display the sharing panel.
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.SINGLE,
      excludedAbilities: \[systemShare.ShareAbilityType.PRINT\]
    })
