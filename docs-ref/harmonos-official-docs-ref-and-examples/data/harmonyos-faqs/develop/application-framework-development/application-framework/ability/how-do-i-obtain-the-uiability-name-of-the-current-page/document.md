# How do I obtain the UIAbility name of the current page?

You can use **getBundleInfoForSelf()**, with **bundleFlags** set to at least **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_ABILITY**, of [bundleManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager) to obtain [AbilityInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo) of the application. **AbilityInfo** contains information such as the ability name and bundle name of the application.
