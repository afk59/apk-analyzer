# What should I do if "ohpm ERROR: EINSTALL install failed, Error: Dependency node build failed Install failed" is displayed in DevEco Studio during compilation?

**Symptom**

The following error is reported during compilation:

ohpm ERROR: EFETCH Fetch local file package error, D:\\dev\\harmonyos\\mgty-ohos-phone\\oh\_modules.ohpm@ohos+mgkv@pediph1+Vjwini4jdg9r1s9hqaq=\\oh\_modules@ohos\\mgkv\\libs\\MMKV.har does not exist.

ohpm ERROR: missing: D:\\dev\\harmonyos\\mgty-ohos-phone\\oh\_modules.ohpm@ohos+mgkv@pediph1+Vjwini4jdg9r1s9hqaq=\\oh\_modules@ohos\\mgkv\\libs\\MMKV.har, required by @ohos/mgkVOD:/dev/harmony/mgtv-ohos-phone/baseLib/kv/Lib/ngkv.nde.

ohpm ERROR: ERUNNING execute tasks failed, Error: Dependency node build failed.

ohpm ERROR: EINSTALL install failed, Error: Dependency node build failed.

Install failed.

**Possible Causes**

Since ohpm 1.4.0, there are relative path dependencies in the HAR files. This issue occurs if the corresponding dependencies are not added when **oh\_modules** is generated.

**Solution**

1.  Upload the dependency package to the private repository and configure the private repository dependencies. For details, see [ohpm-repo: Private Repository Setup Tool](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo).
2.  Alternatively, add the [overrides](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-oh-package-json5#en-us_topic_0000001792256137_overrides) configuration to the project-level **oh-package.json5** file to override the dependency information and replace the dependency with another version.
