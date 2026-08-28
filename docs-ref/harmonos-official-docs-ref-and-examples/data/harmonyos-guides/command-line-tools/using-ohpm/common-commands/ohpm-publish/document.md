# ohpm publish

Publishes a third-party library.

Since ohpm 6.0.2.636, the **log\_level**, **debug**, **use\_stream\_threshold\_size**, **compability\_log\_level**, **disallow\_nested\_package**, **ensure\_dependency\_include**, and **cache** parameters can be appended to the command.

#### Command Format

ohpm publish \[options\] <har\_or\_tgz\_file>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/6j7hScQEQICPWMg_NdLVHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9777CBE97D8B74846FD9566D648D28203797415C9A490A07DA80747D60E6A1BD)

-   **har\_or\_tgz\_file**: path of the compressed package. The package can be a .har package or a .tgz package packed by the hsp module. This parameter is mandatory.
-   ohpm versions earlier than 1.3.0 only support the .har package. ohpm 1.3.0 and later support the .tgz package.
-   ohpm supports the publishing and downloading of .har and .tgz packages with a maximum size of 300 MB since 5.0.1.

#### Description

-   This command is used to publish a third-party library to the central repository for OpenHarmony third-party libraries. Before publishment, you need to generate public and private keys, upload the public key to the server, and configure the publish code of the public repository and private key path in the .ohpmrc file.
-   By default, **ohpm publish** publishes third-party libraries to the [OpenHarmony Third-Party Library Repository](https://ohpm.openharmony.cn/#/en/home). However, you can still configure **publish\_registry** to specify the target repository. For details about **publish\_registry** values, see its description in section [ohpmrc](../../ohpmrc/document.md).
-   If the combination of the third-party library name and version already exists in the specified repository, the publishment fails.
-   Once the third-party library with a specified name and version is published and approved, the name and version number will be occupied and cannot be used again, even if it has been removed by [ohpm unpublish](../ohpm-unpublish/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/IZ90SPF_SNmIFsXsWJ_Ysg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C07A2D1E36B7A162B0CAD9D0EF4496C2C6B9499B4795D005E8A6704F82DD523D)

-   To ensure that the .har or .tgz package can be built and run properly, the **oh-package.json5** file in the package must contain all direct dependencies of the package. If any dependency is imported through the project-level **oh-package.json5** file, it has to be written into the corresponding **oh-package.json5** file in the package.
-   The HAR built in debug mode contains source code for local debugging. Pay attention to code security. For details, see [Building a HAR](../../../../building-an-app/configuring-your-build/building-a-har/document.md).
-   Before publishing a package, make sure the configurations of its **oh-package.json5** file meet requirements. For details, see [oh-package.json5](../../oh-package-json5/document.md#en-us_topic_0000001792256137_oh-packagejson5-%E5%AD%97%E6%AE%B5%E8%AF%B4%E6%98%8E).

#### Publishment Verification Rules

## Third-Party Library Verification Rules

1.  The package of the third-party library published by **ohpm publish** must be suffixed with .har or .tgz.
2.  All third-party libraries must be stored in the **package** directory, which must contain the **oh-package.json5** file, **README.md** file, **LICENSE** file, and **CHANGELOG.md** file. The **oh-package.json5** file must contain mandatory fields. For details, see the field description of the [oh-package.json5](../../oh-package-json5/document.md) file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/6NhivVAUT_2SOGBDQsZiig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F74A808F55A1189616CB6A8890190F9310F1A37B2508093D43C47BD34F642988)
    
    The **README.md**, **LICENSE**, and **CHANGELOG.md** files must be contained when the HAR is published to the OpenHarmony Third-Party Library Repository and cannot be empty. For details, see [Preparing Essential Files for Publishing a Third-Party Library](https://ohpm.openharmony.cn/#/en/help/publishrequirefile).
    
3.  To obtain the .har package of a third-party library, compress the package directory into a .tgz file and change the file name extension to .har

## Rules for Open/Closed-Source Projects

1.  Open-source
    
    ArkTS code is not compiled. Instead, only C++ code is compiled and OpenHarmony resources are processed. Some original configuration files of the module are packaged. The value of **artifactType** in the **oh-package.json5** file is **original**.
    
2.  Closed-source
    
    ArkTS code is compiled as .js, .d.ets, and .d.ts declaration files. C++ code is compiled and OpenHarmony resources are processed. Some original configuration files of the module are packaged. The value of **artifactType** in the **oh-package.json5** file is **obfuscation**. In this case, the check focuses on whether the declaration files defined in **types** in the **oh-package.json5** file are suffixed with .d.ts or .d.ets and whether these files exist in the corresponding directories. If not, an error is reported indicating a publishment failure.
    

#### Options

## publish\_id

-   Default value: ""
-   Value type: string

You can configure the -**\-publish\_id <id>** parameter at the end of the **ohpm publish** command to specify the publish code.

## key\_path

-   Default value: ""
-   Value type: string

You can configure the **\--key\_path <p>** parameter at the end of the **ohpm publish** command to specify the SSH private key path.

## tag

-   Default value: none
-   Value type: string
-   Alias: t

You can configure the **\-t <tag\_name>** or **\--tag <tag\_name>** parameter at the end of the **ohpm publish** command to label the third-party library to be published.

## publish\_registry

-   Default value: ""
-   Type: URL

You can configure the **\--publish\_registry <r>** parameter at the end of the **ohpm publish** command to specify a repository address for publishment. If this parameter is not specified, the repository address is obtained from the configuration by default.

## fetch\_timeout

-   Default value: 60000
-   Type: number
-   Alias: ft

You can configure the **\--ft <number>** or **\--fetch\_timeout <number>** parameter at the end of the **ohpm publish** command to set the operation timeout period. If the parameter is not specified, the default timeout period is 60000 ms.

## strict\_ssl

-   Default value: true
-   Value type: boolean

You can configure **\--strict\_ssl true** at the end of the **ohpm publish** command to enable HTTPS certificate verification or configure **\--strict\_ssl false** to disable it.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm publish** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## use\_stream\_threshold\_size

-   Default value: none
-   Type: number

You can append the **\--use\_stream\_threshold\_size <number>** parameter to the **ohpm publish** command to specify the streaming upload threshold. The value range is \[0, 300\], in MB. When a third-party library is published, if the file size exceeds this threshold, streaming upload will be used. If the repository does not support a streaming upload API, the upload method will switch to Base64 encoding.

## compability\_log\_level

-   Default value: none
-   Value type: string

You can append the **\--compability\_log\_level <string>** parameter to the **ohpm publish** command. This enables ohpm to verify that all fields required for compatibility checks (**'compatibleSdkVersion'**, **'compatibleSdkType'**, **'obfuscated'**, and **'nativeComponents'**) are configured in the **oh-package.json5** file. If this parameter is not configured, ohpm will log messages or throw errors according to the log level (**info**, **debug**, **warn**, or **error**) specified by **compability\_log\_level**. For details, see [compability\_log\_level](../../ohpmrc/document.md#section96369529419).

## disallow\_nested\_package

-   Default value: false
-   Value type: boolean

You can append the **\--disallow\_nested\_package** parameter to the **ohpm publish** command. This enables ohpm to scan the package for dependencies in .har or .tgz format that are referenced via relative paths in the form of **./**. If such dependencies exist, the command fails and an error message is displayed. For details, see [disallow\_nested\_package](../../ohpmrc/document.md#section1237023983514).

## ensure\_dependency\_include

-   Default value: false
-   Value type: boolean

You can append the **\--ensure\_dependency\_include** parameter to the **ohpm publish** command to enable dependency scanning. For details, see [ensure\_dependency\_include](../../ohpmrc/document.md#section1291814578276).

## cache

-   Default value: none
-   Value type: string

You can append the **\--cache <string>** parameter to the **ohpm publish** command to specify the cache path.

#### Example

Run the following command to publish a third-party library in the working directory:

ohpm publish publish\_test.har

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/WaWCpt2_QkGBLXfiKDz7hQ/en-us_image_0000002501069752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62C16BA10383BC58A924D43CFCAD275EE4042606E43675867A542BDC3534E429)
