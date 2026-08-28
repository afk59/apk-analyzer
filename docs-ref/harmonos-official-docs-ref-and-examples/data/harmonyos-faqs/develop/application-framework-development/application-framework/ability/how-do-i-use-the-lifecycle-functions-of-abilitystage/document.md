# How do I use the lifecycle functions of AbilityStage?

The default project of DevEco Studio does not contain AbilityStage. To use AbilityStage, you can manually create an AbilityStage file. The procedure is as follows:

1.  In the **ets** directory of the **Module** project, right-click and choose **New > Directory** to create a directory named **myabilitystage**.
2.  In the **myabilitystage** directory, right-click and choose **New > ArkTS File** to create a file named **MyAbilityStage.ets**.
3.  Open the **MyAbilityStage.ets** file, import the dependency package of AbilityStage, customize a class to inherit from AbilityStage, and add the required lifecycle callbacks. The following code snippet adds the **onCreate()** lifecycle callback.
    
    import { AbilityStage, Want } from '@kit.AbilityKit';
    
    export default class MyAbilityStage extends AbilityStage {
      onCreate(): void {
        // When the HAP of the application is first loaded, initialize the operation for the module
      }
    
      onAcceptWant(want: Want): string {
        // Triggered only when UIAbility is configured in specified startup mode
        return 'MyAbilityStage';
      }
    }
    
4.  In the [module.json5 file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file), set **srcEntry** to specify the code path of the module as the entry for loading the HAP.
    
    {
      "module": {
        "name": "entry",
        "type": "entry",
        "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
        // ...
      }
    }
    

An [AbilityStage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage) has the [onCreate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#oncreate) and [onDestroy()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#ondestroy12) lifecycle callbacks, and the [onAcceptWant()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#onacceptwant), [onConfigurationUpdate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#onconfigurationupdate), and [onMemoryLevel()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#onmemorylevel) event callbacks.
