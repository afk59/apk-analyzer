# Context (FA Model)

There is only one context in the [FA model](../../../ability-kit-terminology/document.md#fa-model). All capabilities in the context are provided through methods. The context uses these methods to extend the capabilities of the **featureAbility** class.

#### Available APIs

To use the context in the FA model, first import the **featureAbility** module.

import featureAbility from '@ohos.ability.featureAbility';

Then, call **getContext()** to obtain the Context object:

import featureAbility from '@ohos.ability.featureAbility';

let context = featureAbility.getContext();

For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-app-context).

#### How to Develop

1.  Query bundle information.
    
    import featureAbility from '@ohos.ability.featureAbility';
    import hilog from '@ohos.hilog';
    
    const TAG: string = 'MainAbility';
    const domain: number = 0xFF00;
    
    class MainAbility {
      onCreate() {
        // Obtain the context and call related APIs.
        let context = featureAbility.getContext();
        context.getBundleName((data, bundleName) => {
          hilog.info(domain, TAG, 'ability bundleName:' + bundleName);
        });
        hilog.info(domain, TAG, 'Application onCreate');
      }
    }
    
    export default new MainAbility();
    
2.  Set the display orientation of the **featureAbility**.
    
    import featureAbility from '@ohos.ability.featureAbility';
    import bundle from '@ohos.bundle';
    import hilog from '@ohos.hilog';
    
    const TAG: string = 'PageAbilitySingleton';
    const domain: number = 0xFF00;
    
    class PageAbilitySingleton {
      onCreate() {
        // Obtain the context and call related APIs.
        let context = featureAbility.getContext();
        context.setDisplayOrientation(bundle.DisplayOrientation.PORTRAIT).then(() => {
          hilog.info(domain, TAG, 'Set display orientation.');
        })
        hilog.info(domain, TAG, 'Application onCreate');
      }
    
      onDestroy() {
        hilog.info(domain, TAG, 'Application onDestroy');
      }
    }
    
    export default new PageAbilitySingleton();
