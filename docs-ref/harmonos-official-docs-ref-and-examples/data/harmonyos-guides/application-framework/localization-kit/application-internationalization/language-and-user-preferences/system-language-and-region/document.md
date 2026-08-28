# System Language and Region

#### How It Works

You can add multiple languages in the **Language & region** area in **Settings**. The list formed by multiple languages is called a language list, and the first language in the list is called the system language. Locales are divided based on the locale ID.

When you set or switch the system language, the system checks whether the [extended parameter](../../locale-id-and-cultural-habit-division/document.md) matches the system language. If they do not match, the system deletes the extended parameter. For example, if the current system language is **ar** and the local numeral system is **arab**, the local numeral system will be changed to **mymr** once you switch the system language to **my**. If you switch the language to Chinese, the Arabic numeral system is used because local numerals are not supported. Meanwhile, the extended parameter associated with the numeral system is removed.

Since API version 21, you can also use the **param get persist.global.language** command of the [param tool](../../../../../system/debugging-tools/debugging-commands/param/document.md#get) to obtain the system language.

#### How to Develop

For details about how to use related APIs, see [System](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-i18n#system9).

1.  Import the related modules.
    
    import { i18n } from '@kit.LocalizationKit';
    import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
    
2.  Application scenario.
    

-   Obtain the system language, region, and locale.
    
    // Obtain the system language.
    let systemLanguage = i18n.System.getSystemLanguage();  // systemLanguage indicates the current system language.
    
    // Obtain the system region.
    let systemRegion = i18n.System.getSystemRegion();  // systemRegion indicates the current system region.
    
    // Obtain the system locale.
    let systemLocale: Intl.Locale = i18n.System.getSystemLocaleInstance(); // systemLocale indicates the current system locale.
    
    // Subscribe to system language, region, or locale changes through the common event COMMON\_EVENT\_LOCALE\_CHANGED.
    let subscriber: commonEventManager.CommonEventSubscriber; // Used to save the created subscriber object for subsequent subscription and unsubscription.
    let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: \[commonEventManager.Support.COMMON\_EVENT\_LOCALE\_CHANGED\]
    };
    // Create a subscriber.
    commonEventManager.createSubscriber(subscribeInfo)
      .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
        console.info('CreateSubscriber');
        subscriber = commonEventSubscriber;
        commonEventManager.subscribe(subscriber, (err, data) => {
          if (err) {
            console.error(\`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.\`);
            return;
          }
          console.info('The subscribed event has occurred.'); // The system language, region, or locale has changed.
        })
      })
      .catch((err: BusinessError) => {
        console.error(\`CreateSubscriber failed, code is ${err.code}, message is ${err.message}\`);
      });
