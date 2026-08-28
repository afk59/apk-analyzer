# DLP Service Development

The Data Loss Prevention (DLP) service is a system solution provided to prevent leakage of sensitive data. It provides a file format called DLP. A DLP file consists of the original file in ciphertext and the authorization credential, and ".dlp" is added to the end of the original file name (including the file name extension), for example, **test.docx.dlp**.

A DLP file can be accessed only after successful device-cloud authentication (network connection required). The permissions for a DLP file include the following:

-   Read-only: The user can only view the file.
-   Edit: The user can read and write the file, but cannot change the permission on the file.
-   Full control: The user can read and write the file, change the permission on the file, and restore the plaintext of the file.

When an application accesses a DLP file, the system automatically installs a dual application, a copy based on the current application. Both can run at the same time without affecting each other. The dual application is running in a sandbox, which restricts external access to prevent data leakage. For simplicity, the dual application running in a sandbox is referred to as sandbox application. Each time a DLP file is opened, a sandbox application is generated. The sandbox applications are also isolated from each other. When an application is closed, its sandbox application will be automatically uninstalled and the temporary data generated in the sandbox directory will be cleared.

Normally, the application is unaware of the sandbox and accesses the file in plaintext, like accessing a common file. However, the DLP sandbox restricts the application from accessing external resources (such as the network, clipboard, screenshot capturing, screen recording, and Bluetooth). For better user experience, you need to adapt your application to service requirements. For example, for a read-only file, you'd better hide the **Save** button and disable automatic Internet access.

#### Sandbox Restrictions

The sandbox also restricts the permissions granted to the application based on the permission on the DLP file.

| 
Application Permission

 | 

Description

 | 

Read-Only

 | 

Edit/Full Control

 |
| :-- | :-- | :-- | :-- |
| 

ohos.permission.USE\_BLUETOOTH

 | 

Allows an application to use Bluetooth.

 | 

Forbidden

 | 

Forbidden

 |
| 

ohos.permission.INTERNET

 | 

Allows an application to access the Internet.

 | 

Forbidden

 | 

Forbidden

 |
| 

ohos.permission.DISTRIBUTED\_DATASYNC

 | 

Allows an application to exchange user data (such as images, music, videos, and application data) with another device.

 | 

Forbidden

 | 

Forbidden

 |
| 

ohos.permission.WRITE\_MEDIA

 | 

Allows an application to read and write media files, such as videos, audio clips, and images.

 | 

Forbidden

 | 

Allowed

 |
| 

ohos.permission.NFC\_TAG

 | 

Allows an application to use NFC.

 | 

Forbidden

 | 

Allowed

 |

#### Available APIs

| 
API

 | 

Description

 |
| :-- | :-- |
| 

isDLPFile(fd: number): Promise<boolean>

isDLPFile(fd: number, callback: AsyncCallback<boolean>): void

 | 

Checks whether a file is a DLP file.

 |
| 

getDLPPermissionInfo(): Promise<DLPPermissionInfo>

getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void

 | 

Obtains the DLP permission information of this sandbox application.

 |
| 

getOriginalFileName(fileName: string): string

 | 

Obtains the original name of a DLP file.

 |
| 

getDLPSuffix(): string

 | 

Obtains the file name extension of this DLP file.

 |
| 

on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void

 | 

Subscribes to the DLP file open event.

 |
| 

off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void

 | 

Unsubscribes from the DLP file open event.

 |
| 

isInSandbox(): Promise<boolean>

isInSandbox(callback: AsyncCallback<boolean>): void

 | 

Checks whether this application is a sandbox application.

 |
| 

getDLPSupportedFileTypes(): Promise<Array<string>>

getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void

 | 

Obtains the file name extension types that can be appended with .dlp.

 |
| 

setRetentionState(docUris: Array<string>): Promise<void>

setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

 | 

Sets the sandbox application retention state. If the retention state is set, the sandbox application will not be automatically uninstalled after being closed.

 |
| 

cancelRetentionState(docUris: Array<string>): Promise<void>

cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

 | 

Cancels the sandbox application retention state.

 |
| 

getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>

getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

 | 

Obtains the sandbox applications in the retention state.

 |
| 

getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>

getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void

 | 

Obtains the recently accessed DLP files.

 |
| 

setSandboxAppConfig(configInfo: string): Promise<void>

 | 

Sets sandbox application configuration.

 |
| 

getSandboxAppConfig(): Promise<string>

 | 

Obtains the sandbox application configuration.

 |
| 

cleanSandboxAppConfig(): Promise<void>

 | 

Clears the sandbox application configuration.

 |
| 

startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>

 | 

Starts the DLP manager application on the current UIAbility page in borderless mode (available only for the stage model).

 |

#### How to Develop

DLP is a system-level data protection solution that can be integrated into your application with minor adaptation or without adaptation.

When a DLP file is opened using the default application or a specified application, the DLP framework:

1.  Installs a sandbox application for your application.
2.  Binds a Filesystem in Userspace (FUSE) file to the DLP file.
3.  Shares the FUSE file with the DLP sandbox application.

This allows the sandbox application to seamlessly access the decrypted content of the DLP file, without aware of the encryption and decryption process.

To incorporate the DLP feature (support opening of DLP files) to a third-party application, perform the following adaptation.

## Prerequisites

Before you start, ensure that the following conditions are met:

-   Your application supports one or more of the following file types:
    
      ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".odp", ".odt", ".pdf", ".pot", ".potm", ".potx", ".ppa",
      ".ppam", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".rtf", ".txt", ".wps", ".xla", ".xlam", ".xls",
      ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltm", ".xltx", ".xlw", ".xml", ".xps"
    

-   The application must have **ohos.want.action.viewData** or **ohos.want.action.editData** configured under **skills** in the **module.json5** file.
    
      "skills":\[
        {
          "entities":\[
            ...
          \],
          "actions":\[
            ...
            "ohos.want.action.viewData"
          \]
        }
      \]
    

-   The device supports domain accounts.
    

## Importing Modules

Import the [dlpPermission](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission) module.

import { dlpPermission } from '@kit.DataProtectionKit';

## Opening the FUSE File

Generally, an application can open the FUSE file without adaptation if it can open the files mentioned in [Prerequisites](#预置操作) and there is no restriction on the **Want** parameter.

When a DLP file is opened, a sandbox application will be installed for the application. The sandbox application receives a Want request and parses the fields in the request.

 import Want from '@ohos.app.ability.Want';

 interface DLPUriObj {
   name: string
 };

 interface DLPWriteable {
   name:boolean
 };

 interface DLPNameObj {
   dateModified: string,
   displayName: string,
   relativePath: string,
 };

 interface DLPLinkNameObj {
   name: string
 };

 function getParams(want: Want) {
   // Receive the parameters passed after the DLP file is opened.
   let dlpFuseUri: string = want.uri? want.uri : '';  // URI of the FUSE file, which stores the decrypted plaintext.
   let dlpFuseWriteable: boolean = (want.parameters?.linkFileWriteable as DLPWriteable).name; // Whether the FUSE file is writeable.
   let dlpUri: string = (want.parameters?.dlpUri as DLPUriObj).name; // URI of the DLP file.
   let dlpName: string = (want.parameters?.fileAsset as DLPNameObj).displayName; // DLP file name.
   let dlpFuseName: string = (want.parameters?.linkFileName as DLPLinkNameObj).name; // FUSE file name.
 }

The sandbox application opens the FUSE file based on **want.uri**, obtains the FD, and then obtains the content of the FUSE file based on the FD.

 import fileIo from '@ohos.fileio';
 import fs from '@ohos.file.fs';
 import util from '@ohos.util';

 function readFileContent(dlpFuseUri:string): string {
   let content: string = '';
   let file: fs.File;
   try {
     file = fs.openSync(dlpFuseUri, fs.OpenMode.READ\_ONLY); // Open the FUSE file and obtain the FD.
     this.commonFd = file.fd;
   } catch (err) {
     console.error('openSync failed. ' + err);
     return content;
   }

   try {
     let buffer = new ArrayBuffer(4096);
     let readOut = fs.readSync(this.commonFd, buffer, { // Read the file content.
       offset: 0
     });
     content = bufferToString(buffer); // Convert the file content to a string.
   } catch (err) {
     console.error('readSync failed. ' + err);
   }
   fileIo.closeSync(this.commonFd); // Close the file.
   return content;
 }

 function bufferToString(buffer: ArrayBuffer): string {
   let textDecoder = new util.TextDecoder('utf-8', {
     ignoreBOM: true
   });
   let resultPut = textDecoder.decodeWithStream(new Uint8Array(buffer), {
     stream: true
   });
   return resultPut;
 }

If the FUSE file is readable and writeable, you can also update the FUSE file content.

import fs from '@ohos.file.fs';

function writeFileContent(dlpFuseUri: string, content: string): void {
  let file: fs.File = fs.openSync(dlpFuseUri, fs.OpenMode.READ\_WRITE); // Open the FUSE file in read/write mode.
  let writeLen: number = fs.writeSync(file.fd, content);  // Write data to the FUSE file.
  fs.closeSync(file); // Close the file.
}

## Setting the UI Based on the DLP File Permission

Use [getDLPPermissionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissiongetdlppermissioninfo) to obtain the user permission and operations allowed for the login domain account on the DLP file. The operations allowed vary with the user permission.

 import { dlpPermission } from '@kit.DataProtectionKit';
 import { BusinessError } from '@kit.BasicServicesKit';

 dlpPermission.getDLPPermissionInfo().then((data: dlpPermission.DLPPermissionInfo)=> {
   let userAccess: dlpPermission.DLPPermissionInfo.DLPFileAccess = data.dlpFileAccess; // User permission on the DLP file, which can be read-only, edit, or full control.
   let isEditable: number = data.flags & dlpPermission.DLPPermissionInfo.ACTION\_EDIT; // Operations allowed on the DLP file.
 }).catch((err: BusinessError) => {
   console.error('getDLPPermissionInfo: ' + JSON.stringify(err));
 });

In [DLPPermissionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissioninfo) returned by **getDLPPermissionInfo**, **dlpFileAccess** indicates the user permission and **flags** is the bitwise combination of the operations allowed. You can determine the allowed operations based on [ActionFlagType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#actionflagtype) and disable the related buttons on the UI.

## Sharing Data Between an Application and Its Sandbox Application

Since the sandbox application is isolated from the application, its data is different from that of the application. To share data between them, you can use the data sharing mechanism provided by the DLP framework. For example, the application and its sandbox application can share the configuration for determining whether the privacy statement window has been displayed.

Generally, the configuration can be written and read in any of the following sequences:

-   The application writes the configuration and then reads the configuration.
-   The application writes the configuration, and the sandbox application reads the configuration.
-   The sandbox application writes the configuration and then reads the configuration.
-   The sandbox application writes the configuration, and the application reads the configuration.

**Constraints**

-   Each time the API for setting the configuration is called, the settings overwrite the previous ones.
-   To prevent data leakage, the configuration written by a sandbox application must be completed before the FUSE file content is read.

**Procedure**

1.  Set the configuration information.
    
    Convert the configuration information to the string type and call [setSandboxAppConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissionsetsandboxappconfig11) to set the configuration information for the sandbox application.
    
    Both an application and its sandbox application can call this API. However, the DLP sandbox application can call this API only before reading the DLP file content.
    
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     async function setSandboxAppConfig() {
       try {
         await dlpPermission.setSandboxAppConfig('configInfo'); // Set configuration information.
       } catch (err) {
         console.error('setSandboxAppConfig error, ', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
       }
     }
    
2.  Clear the configuration information.
    
    Call [cleanSandboxAppConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissioncleansandboxappconfig11) to clear all configuration of the sandbox application.
    
    This API can be called only by a common application.
    
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     async function cleanSandboxAppConfig() {
       try {
         await dlpPermission.cleanSandboxAppConfig(); // Clear configuration information.
       } catch (err) {
         console.error('cleanSandboxAppConfig error, ', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
       }
     }
    
3.  Obtain configuration information.
    
    Call [getSandboxAppConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissiongetsandboxappconfig11) to obtain configuration of the sandbox application.
    
    Both an application and its sandbox application can call this API.
    
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     async function getSandboxAppConfig() {
       try {
         let res:string = await dlpPermission.getSandboxAppConfig(); // Obtain configuration information.
       } catch (err) {
         console.error('getSandboxAppConfig error, ', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
       }
     }
    

## Updating the DLP File Access Record

You can use the APIs provided by the DLP framework to obtain information about the recently accessed DLP files. Scenarios include the following:

-   The application is not started and cannot detect the DLP files accessed by the sandbox application.
    
    If DLP files are accessed only by the sandbox application, the application can call **getDLPFileAccessRecords()** to obtain information about the DLP files accessed by the sandbox application when started.
    
        import { dlpPermission } from '@kit.DataProtectionKit';
        import { BusinessError } from '@kit.BasicServicesKit';
    
        async function getDLPFileAccessRecords() {
          try {
            let res:Array<dlpPermission.AccessedDLPFileInfo> = await dlpPermission.getDLPFileAccessRecords(); // Obtain a list of recently accessed DLP files.
            console.info('res', JSON.stringify(res))
          } catch (err) {
            console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
          }
        }
    
-   The application is started and can detect the DLP files accessed by the sandbox application.
    
    The application can subscribe to the DLP file open event.
    
     import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     export default class TestAbility extends UIAbility {
       onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
         this.subscribe();
       }
    
       onDestroy(): void {
         this.unSubscribe();
       }
    
       event(info: dlpPermission.AccessedDLPFileInfo) {
         console.info('openDlpFile event', info.uri, info.lastOpenTime)
       }
    
       unSubscribe() {
         try {
           dlpPermission.off('openDLPFile', this.event); // Unsubscribe from the DLP file open event.
         } catch (err) {
            console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
         }
       }
    
       subscribe() {
         try {
           dlpPermission.on('openDLPFile', this.event); // Subscribe to the DLP file open event.
         } catch (err) {
            console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
         }
       }
     }
    

## Opening a DLP File in an Application

You can select a DLP file in the list of recently accessed files or using a file Picker and open it as follows:

1.  Set [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-ability-want) as follows:
    
    Set **action** to **ohos.want.action.viewData**.
    
    Set **bundleName** and **abilityName** to the bundle name and ability name of the application that attempts to open the DLP file, respectively.
    
    Set **uri** to the URI of the DLP file to open.
    
    Set **fileName** in **Parameters** to the name of the DLP file.
    
2.  Obtain [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common).
    
3.  Call [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability) of the context to pass in the **Want** parameter and open the DLP file.
    

 import { Want } from '@kit.AbilityKit';
 import { BusinessError } from '@kit.BasicServicesKit';
 import common from '@ohos.app.ability.common';

 function openDlpFile(dlpUri: string, fileName: string) {
   let want: Want = {
     "action": "ohos.want.action.viewData",
     "bundleName": "com.example.example\_bundle\_name",
     "abilityName": "exampleAbility",
     "uri": dlpUri,
     "parameters": {
       "fileName": {
         "name": fileName
       }
     }
   }
   let context = getContext() as common.UIAbilityContext; // Obtain UIAbilityContext.
   try {
     console.log('openDLPFile:' + JSON.stringify(want));
     console.log('openDLPFile: delegator:' + JSON.stringify(context));
     context.startAbility(want);
   } catch (err) {
     console.error('openDLPFile startAbility failed', (err as BusinessError).code, (err as BusinessError).message);
     return;
   }
 }

## Setting the DLP File Permission in an Application

You can integrate the permission settings button into an application. When opening a common file, you can click the button to open the modal permission settings page of the DLPManager application and generate a DLP file. You can also view the allowed operations for the opened DLP file via the sandbox application.

-   **Setting the permission in an application**
    
    Start the DLP manager application in borderless mode.
    
    -   The **dlpPermission.startDLPManagerForResult()** API can be called only in the UIAbility context and supports only the stage model.
        
    -   In the **Want** parameter, **uri** is the URI of a common file, and **parameters.displayName** is the file name. The two parameters are mandatory.
        
    -   Call [dlpPermission.startDLPManagerForResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissionstartdlpmanagerforresult11) to open the permission settings page of the DLP manager application, enter the domain account information, and click **Save**. In the file Picker started, select the directory for saving the DLP file.
        
    
    Sample code:
    
     import { common, Want } from '@kit.AbilityKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { dlpPermission } from '@kit.DataLossPreventionKit';
    
     try {
       let fileUri: string = "file://docs/storage/Users/currentUser/test.txt";
       let fileName: string = "test.txt";
       let context = getContext() as common.UIAbilityContext; // Obtain UIAbilityContext.
       let want: Want = {
         'uri': fileUri,
         'parameters': {
           'displayName': fileName
         }
       }; // Request parameters.
       dlpPermission.startDLPManagerForResult(context, want).then((res: dlpPermission.DLPManagerResult) => {
         console.info('startDLPManagerForResult res.resultCode:' + res.resultCode);
         console.info('startDLPManagerForResult res.want:' + JSON.stringify(res.want));
       }); // Start the DLPManager application to set permissions.
     } catch (err) {
       console.error('startDLPManagerForResult error:' + (err as BusinessError).code + (err as BusinessError).message);
     }
    
-   **Modifying, obtaining, and removing the DLP permission in a sandbox application**
    
    -   If the current account is the user who creates the DLP file, the user can modify the DLP file permission and remove the DLP protection (making the file become a common file). You can call the following code to start the permission settings page of the DLP manager application, and choose **Change Encryption** or **Cancel Encryption**. If the current account has the read-only or edit permission on the DLP file, you can call the following code to view the permission of the current user.
        
         import { common, Want } from '@kit.AbilityKit';
         import { BusinessError } from '@kit.BasicServicesKit';
         import { dlpPermission } from '@kit.DataLossPreventionKit';
        
         try {
           let fileUri: string = "file://docs/storage/Users/currentUser/test.txt.dlp";// URI of the DLP file.
           let fileName: string = "test.txt.dlp";
           let context = getContext() as common.UIAbilityContext; // Obtain UIAbilityContext.
           let want: Want = {
             'uri': fileUri,
             'parameters': {
               'displayName': fileName
             }
           }; // Request parameters.
           dlpPermission.startDLPManagerForResult(context, want).then((res: dlpPermission.DLPManagerResult) => {
             console.info('startDLPManagerForResult res.resultCode:' + res.resultCode);
             console.info('startDLPManagerForResult res.want:' + JSON.stringify(res.want));
           }); // Start the DLPManager application to set permissions.
         } catch (err) {
           console.error('startDLPManagerForResult error:' + (err as BusinessError).code + (err as BusinessError).message);
         }
        
    
    -   Call [getDLPPermissionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissiongetdlppermissioninfo) to obtain the DLP file permission information of the current user. For details about the permission restrictions of the sandbox application, see [Sandbox Restrictions](#沙箱限制).
        
         import { dlpPermission } from '@kit.DataProtectionKit';
         import { BusinessError } from '@kit.BasicServicesKit';
        
         dlpPermission.getDLPPermissionInfo().then((data:dlpPermission.DLPPermissionInfo)=> {
           console.log('getDLPPermissionInfo, result: ' + JSON.stringify(data));
         }).catch((err: BusinessError) => {
           console.error('getDLPPermissionInfo: ' + JSON.stringify(err));
         });
        

## Other DLP Capabilities

-   Checking whether a file is a DLP file
    
    Check whether the file specified by the FD is a DLP file. If yes, you can open the file by following the instructions provided in [Opening a DLP File](#应用内支持打开选定的dlp文件).
    
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { fileIo } from '@kit.CoreFileKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
     let file = fileIo.openSync(uri);
     try {
       let res: boolean = dlpPermission.isDLPFile (file.fd); // Check whether the file is a DLP file.
       console.info('res', res);
     } catch (err) {
            console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
     }
     fileIo.closeSync(file);
    
-   Checking whether this application is a sandbox application
    
    Call [isInSandbox](https://developer.huawei.com/consumer/n/doc/harmonyos-references/js-apis-dlppermission#dlppermissionisinsandbox) to check whether this application is a DLP sandbox application. If yes, you can disable or hide corresponding buttons on the UI. For details, see [Setting the UI Based on the DLP File Permission](#应用根据dlp文件的权限对界面进行适配). If the DLP file permission is **Read-only**, you can disable the edit and save entries. If the DLP file permission is **Edit**, disable the permission settings entry.
    
     import { dlpPermission } from '@kit.DataProtectionKit';
     import { BusinessError } from '@kit.BasicServicesKit';
    
     dlpPermission.isInSandbox().then((data: boolean)=> {
       console.log('isInSandbox, result: ' + JSON.stringify(data));
     }).catch((err: BusinessError) => {
       console.error('isInSandbox: ' + JSON.stringify(err));
     });
    
-   Setting the retention state for a sandbox application
    
    A sandbox application in the retention state will not be automatically uninstalled when the sandbox application is closed. Then, the sandbox application will be uninstalled only after the retention state is canceled and the sandbox application is closed.
    
    -   Call [setRetentionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissionsetretentionstate) to set the retention state of a sandbox application. You need to pass in the URIs of the DLP files opened in this sandbox. This API can be called only by a sandbox application.
        
         import { dlpPermission } from '@kit.DataProtectionKit';
         import { BusinessError } from '@kit.BasicServicesKit';
        
         async function setRetentionSandboxList() {
           let docUris: Array<string>=\["file://docs/storage/Users/currentUser/Desktop/test.txt.dlp"\]
           try {
             await dlpPermission.setRetentionState (docUris); // Set the sandbox retention state.
           } catch (err) {
                console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
           }
         }
        
    -   Call [cancelRetentionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissioncancelretentionstate) to cancel the sandbox retention state. This API can be called only by a sandbox application.
        
         import { dlpPermission } from '@kit.DataProtectionKit';
         import { BusinessError } from '@kit.BasicServicesKit';
        
         async function setRetentionSandboxList() {
           let docUris: Array<string>=\["file://docs/storage/Users/currentUser/Desktop/test.txt.dlp"\]
           try {
             await dlpPermission.cancelRetentionState (docUris); // Cancel the retention state of the sandbox application.
           } catch (err) {
                console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
           }
         }
        
    -   Call [getRetentionSandboxList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-dlppermission#dlppermissiongetretentionsandboxlist) to obtain the sandbox retention information. This API can be called by a common application and its sandbox application.
        
         import { dlpPermission } from '@kit.DataProtectionKit';
         import { BusinessError } from '@kit.BasicServicesKit';
        
         async function getRetentionSandboxList() {
           try {
             let res:Array<dlpPermission.RetentionSandboxInfo> = await dlpPermission.getRetentionSandboxList(); // Obtain retention information of the sandbox application.
             console.info('res', JSON.stringify(res))
           } catch (err) {
                console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
           }
         }
        

#### FAQs

## What should I do if the application can open a common file but cannot open the FUSE file?

-   Check for specific restrictions on **Want**.
-   Check whether the read-only FUSE file is opened with the read/write permission.
