# Dependency Error Codes

#### 00301001 Signature Tool Not Found in the SDK

**Error Message**

No HAP signing tool found in the SDK.

**Symptom**

The signing tool cannot be found in the SDK.

**Possible Causes**

The signing tool is not included in the SDK.

**Solution**

Check whether the signing tool exists in the corresponding directory. If not, re-download [DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) from the official website.

#### 00301002 Outdated SDK Version

**Error Message**

The SDK version configured for the current project is too low.

**Symptom**

The SDK version is outdated.

**Possible Causes**

The SDK version is outdated.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00301003 Incorrect SDK Version

**Error Message**

Unsupported SDK version for using AOT compiling. Current SDK version is XXX, but the lowest SDK version which support AOT compiling is XXX.

**Symptom**

The current SDK version does not support the AOT compilation mode.

**Possible Causes**

The SDK version is outdated.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00301004 Incorrect SDK Version

**Error Message**

Current version of SDK has a bug when using AOT compiling. The compiling will continue with AOT compiling function disabled. Current SDK version is XXX, but the lowest fixed SDK version is XXX.

**Symptom**

The current SDK version does not support the AOT compilation mode.

**Possible Causes**

The SDK version is outdated.

**Solution**

Download the latest [DevEco Studio](https://developer.huawei.com/consumer/en/download/deveco-studio) from the official website.

#### 00301005 Bytecode HARs Not Supported by the API Version Earlier Than 12

**Error Message**

byteCodeHar not supported when below API version 12.

**Symptom**

Bytecode HARs are not supported if the API version is earlier than 12.

**Possible Causes**

Bytecode HARs are not supported if the API version is earlier than 12.

**Solution**

Ensure that **compileSdkVersion** and **compatibleSdkVersion** in the **build-profile.json5** file are not earlier than API version 12.

#### 00301006 oh-package.json5 Not Found in the HSP

**Error Message**

The oh-package.json5 file cannot be found in the remote HSP XXX. Check whether the oh-package.json5 file exists in YYY.

**Symptom**

The **oh-package.json5** file cannot be found in HSP _XXX_.

**Possible Causes**

The HSP is damaged.

**Solution**

Check whether the **oh-package.json5** file exists in the HSP in a specific directory. If the file does not exist, the package is damaged. In this case, download the package again or contact the author.

#### 00301007.hsp File Not Found in the HSP

**Error Message**

Cannot find the .hsp file in the remote HSP. Check whether the .hsp file exists in the XXX directory.

**Symptom**

The .hsp file cannot be found in the HSP.

**Possible Causes**

The HSP is damaged.

**Solution**

Check whether the .hsp file exists in the HSP in the _XXX_ directory. If the file does not exist, the package is damaged. In this case, download the package again or contact the author.

#### 00301009 Invalid Local Dependency

**Error Message**

The local dependency below in module XXX invalid. It may cause an ohpm install error when being integrated.

**Symptom**

The local dependency of module _XXX_ is invalid. ohpm may fail to be installed during integration.

**Possible Causes**

The local dependency configured for the module is not in the current module directory.

**Solution**

Ensure that all local dependencies configured in **dependencies** and **dynamicDependencies** in the module-level **oh-package.json5** file are in the current module directory.

#### 00301010 useNormalizedOHMUrl Inconsistency

**Error Message**

The useNormalizedOHMUrl settings of packages XXX and the project useNormalizedOHMUrl:XXX do not match.

**Symptom**

The value of **useNormalizedOHMUrl** in package _XXX_ is different from that in the project.

**Possible Causes**

The value of **useNormalizedOHMUrl** in the project-level **build-profile.json5** file is different from that in package _XXX_.

**Solution**

1.  Modify the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file of the problematic dependency package to be consistent with the current project. Then, regenerate the dependency package and replace the original one (the default value for **useNormalizedOHMUrl** is **false**).
2.  If there are many dependency packages with inconsistent **useNormalizedOHMUrl** values, you are advised to change the value of **useNormalizedOHMUrl** in the project-level **build-profile.json5** and replace other inconsistent dependency packages.
