# Sharing an Application File

An application can share a file with another application based on the uniform resource identifier (URI) of the file.

#### Using startAbility to Start a File Application

[startAbility](../../../ability-kit/stage-model-development/inter-application-redirection/starting-an-application-of-the-specified-type/using-startability-to-start-a-file-application/document.md)\-based file sharing: You can use [wantConstant.Flags](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantconstant#flags) to specify the read or read/write permission on the file for the target application (application with which the file is shared). The target application can call [fs.open](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopen) to open the file based on the URI and perform read and write operations.

#### Shareable Application Directories

| Application Sandbox Path | Description |
| :-- | :-- |
| /data/storage/el1/base | Encrypted database directory under **/el1**. |
| /data/storage/el2/base | Encrypted database directory under **/el2**. |
| /data/storage/el2/distributedfiles | Distributed data directory with an account under **el2/**. |

#### File URI Specifications

The file URIs are in the following format:

file://<bundleName>/<path>

-   **file**: indicates a file URI.
    
-   bundleName: specifies the owner of the file, that is, the application that shares the file.
    
-   path: specifies the application sandbox path of the file.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Fyh4oerrS-SDo35ZQLW1IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FEC79D3571FC3F8E8DC20B56426F3A367FF4E5F663E8A95B1FFFF1C60B36634)

-   URI processing involves encoding and decoding. The system cannot guarantee the availability of the URI address that an application combines by itself.
-   You are advised to use the APIs provided by the system to obtain URIs, for example, [getUriFromPath](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath).
