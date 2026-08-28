# Initializing the Global App Context

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Procedure

The app context is needed if you need to upload or download files through Cloud Storage. You can initialize the global app context by referring to the following code.

1.  Add the **GlobalContext.ets** file to the **entry/src/main/ets/common** directory to implement the APIs for initializing and obtaining the app context.
    
    import { common } from '@kit.AbilityKit';
    
    export class GlobalContext {
      private static context: common.UIAbilityContext;
    
      public static initContext(context: common.UIAbilityContext): void {
        GlobalContext.context = context;
      }
    
      public static getContext(): common.UIAbilityContext {
        return GlobalContext.context;
      }
    }
    
2.  Import **GlobalContext** to the **entry/src/main/ets/entryability/EntryAbility.ets** file and use **GlobalContext.initContext(this.context)** in the **onCreate** method to initialize the global app context.
