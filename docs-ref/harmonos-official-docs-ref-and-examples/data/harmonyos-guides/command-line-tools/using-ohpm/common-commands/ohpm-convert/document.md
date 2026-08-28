# ohpm convert

Converts a third-party library from npm to ohpm. Due to syntax differences, the conversion only transforms file formats and does not modify the code logic of the original npm package. If code incompatibility errors occur in the converted HAR package, you must adapt the original npm package's code accordingly.

Since ohpm 6.0.2.636, the **log\_level** and **debug** parameters can be appended to the command to obtain the log level and specify the log level for the current command execution.

#### Command Format

ohpm convert \[\[<@group>/\]<pkg>\[@<version> | @tag:<tag>\]\] --registry <string> \[--publish\]
ohpm convert <node\_modules\_path> \[--publish\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/trrxonOaQQuhWAUeU7h3bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18E863A43F09034D7EF931E7B3E1178B288A224D5B1F57DD229A0C7CEAE71519)

-   **@group**: namespace of the third-party library. This parameter is optional.
-   **pkg**: name of the third-party library. This parameter is mandatory.
-   **version**: version number of the third-party library. This parameter is optional.
-   **tag**: tag of the third-party library, marking a specific version number. This parameter is optional.

#### Description

This command is used to convert a package in the specified npm repository or a package in the local **node\_modules** directory to a HAR package that meets the ohpm format requirements and save the HAR package to the current working directory, the converted package can be uploaded to the ohpm-repo private repository or OpenHarmony third-party library central repository.

-   ohpm convert @group/pkg@version --registry <npm repository address>
    
    Downloads a package and all its dependencies from a specified repository, and converts the package and its dependencies into a HAR package that meets the ohpm format requirements.
    
-   ohpm convert <node\_modules\_path>
    
    Converts all packages in the specified **node\_modules** directory to a HAR package that meets the ohpm format requirements. Note that **<node\_modules\_path>** must be the path to the **node\_modules** directory generated after executing the **npm install** command.
    
    Example:
    
    ohpm convert ./xxxx/node\_modules
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nBf3BFH1QaiMnFXK8jUEBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A27D1D5D6003D621F2E6B5BD84064A91C66B13582F71E3E6EDB4C56A1F0DA264)

The **ohpm convert** command only retains the following fields in **package.json** of the npm package: **name**, **version**, **main**, **types**, **license**, **description**, **author**, **keywords**, **homepage**, **repository**, **artifactType**, **dependencies**, **devDependencies**, **dynamicDependencies**, **overrides**, **scripts**, **hooks**, **module**, **packageType**, **typesVersions**, **exports**, and **jsnext:main**. For specific field descriptions, see [oh-package.json5](../../oh-package-json5/document.md#en-us_topic_0000001792256137_oh-packagejson5-%E5%AD%97%E6%AE%B5%E8%AF%B4%E6%98%8E).

#### Options

## registry

-   Default value: none
-   Type: URL

You can configure the **\--registry <registry>** parameter at the end of the **ohpm convert** command to specify a repository address for conversion. If the **\--registry** parameter is specified, the **ohpm convert** command will download the specified package and its dependencies from the remote repository address and then perform the conversion process. If it is not specified, the command will perform the conversion process using the local **node\_modules** directory.

## publish

-   Default value: **false**
-   Value type: boolean

You can configure the **\--publish** parameter at the end of the **ohpm convert** command. If this parameter is specified, confirm that the push package related configurations in .ohpmrc are correct before executing the **ohpm convert** command. After all packages have been converted, the packages will be pushed sequentially according to the configurations in .ohpmrc.

## log\_level

-   Default value: none
-   Value type: string

You can append the **\--log\_level <string>** parameter to the **ohpm convert** command to specify the log level (**info**, **debug**, **warn**, or **error**) for the execution of the current command. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

## debug

-   Default value: false
-   Value type: boolean

You can append the **\--debug** parameter to the command to set the log level to **debug** for the execution of the current command. This configuration takes effect only on the current command line and does not alter the log level configured in the .ohpmrc file. If this parameter is not specified, the **log\_level** setting in the .ohpmrc file is applied.

#### Example

**Converting a Package from the npm Third-Party Library**

To convert the axios package from an npm third-party library, run the following command:

ohpm convert axios --registry https://registry.npmjs.org/

Below is an output example:

PS C:\\Users\\xxxxx\\Desktop> ohpm convert axios --registry https://registry.npmjs.org
...
ohpm INFO: > start convert package: asynckit@0.4.0
ohpm INFO: > start convert package: axios@1.6.8
ohpm INFO: > start convert package: combined-stream@1.0.8
...
ohpm INFO: A total of 9 packets are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\\Users\\xxxxx\\Desktop\\convert\_1712127991590" directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/2PWFyd9JTFGRjQP4UpPMAQ/en-us_image_0000002500910492.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=183ABB1D170750E091BB7B264608733E74D74F18C59C5FDF5ABDAD75476AA36E "Click to enlarge")

**Converting a Package in the Local node\_modules Directory**

After running the **npm install uuid** command, run the following command to convert the packages in the local **node\_modules** directory:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/BLAy1pAZQ228UgSvbUUAHw/en-us_image_0000002501070340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52A4E9C48BE5B6BAC683964F07F3BF66D2BB790312AB99941F7D91C37FFD622C)

ohpm convert C:\\Users\\xxxxx\\Desktop\\uuidInstallDir\\node\_modules

Below is an output example:

PS C:\\Users\\xxxxx\\Desktop> ohpm convert C:\\Users\\xxxxx\\Desktop\\uuidInstallDir\\node\_modules
ohpm INFO: > start convert package: uuid
...
ohpm INFO: A total of 1 package(s) are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\\Users\\xxxxx\\Desktop\\convert\_1712128912583" directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/c_yiJiFoQ1mMWnDj3m7muQ/en-us_image_0000002501070338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062200Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E3450E06FA1D8FCE75C63D06D8B406A14425E9DFD32E7DA47DE1222878C4FDD)
