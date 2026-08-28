# @ohos.security.certManagerDialog (Certificate Management Dialog Box)

The **certificateManagerDialog** module provides APIs for opening the certificate management pages, on which the certificates are installed, stored, used, and destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/iWLOMoJVQi-gByZ39Bvm-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062337Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A87E200A59DE897AE27C7F71322917E64AEFBBF81B1FF44468B7B398829D86F)

The initial APIs of this module are supported since API version 13. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';

#### CertificateDialogPageType

Enumerates the page types of the certificate management dialog box.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| PAGE\_MAIN | 1 | Main page of the Certificate Manager application. |
| PAGE\_CA\_CERTIFICATE | 2 | CA certificate list page. |
| PAGE\_CREDENTIAL | 3 | Credential list page. |
| PAGE\_INSTALL\_CERTIFICATE | 4 | Certificate installation page. |

#### CertificateType14+

Enumerates the types of the certificate to be installed.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| CA\_CERT | 1 | CA certificate. |
| CREDENTIAL\_USER22+ | 2 | User public credential. |
| CREDENTIAL\_APP22+ | 3 | Private credential of an application. |
| CREDENTIAL\_UKEY22+ | 4 | USB credential. |

#### CertificateScope14+

Defines the usage scope of the certificate to be installed.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| NOT\_SPECIFIED18+ | 0 | No user is specified. |
| CURRENT\_USER | 1 | The installed certificate is accessible only to the current user. |
| GLOBAL\_USER18+ | 2 | The installed certificate is accessible to all users. |

#### CertificateDialogErrorCode

Enumerates the error codes reported when the certificate management dialog box APIs are called.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Value | Description |
| :-- | :-- | :-- |
| ERROR\_GENERIC | 29700001 | Internal error. |
| ERROR\_OPERATION\_CANCELED14+ | 29700002 | The user canceled the operation when the API is called. |
| ERROR\_OPERATION\_FAILED14+ | 29700003 | The certificate installation fails. |
| ERROR\_DEVICE\_NOT\_SUPPORTED14+ | 29700004 | The device does not support the API called. |
| ERROR\_NOT\_COMPLY\_SECURITY\_POLICY18+ | 29700005 | The device security policy is not met when the API is called. |
| ERROR\_PARAMETER\_VALIDATION\_FAILED22+ | 29700006 | 
The parameter verification fails when the API is called.

For example, the parameter format is incorrect or the parameter range is invalid.

 |
| ERROR\_NO\_AVAILABLE\_CERTIFICATE22+ | 29700007 | No certificate is available. |

#### CertificateDialogProperty18+

Defines the property of the certificate management dialog box.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| showInstallButton | boolean | No | No | Whether to display the button for installing the certificate. The value **true** means to display the button; the value **false** means the opposite. |

#### CertReference22+

Represents the reference information of the credential.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certType | [CertificateType](#certificatetype14) | No | No | Certificate type. |
| keyUri | string | No | No | Unique identifier of the credential. The value contains up to 256 bytes. |

#### UkeyAuthRequest22+

Represents the authorization request information of the USB credential.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| keyUri | string | No | No | Unique identifier of the USB credential. The value contains up to 256 bytes. |

#### AuthorizeRequest22+

Represents the authorization request information of the certificate.

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certTypes | Array<[CertificateType](#certificatetype14)\> | No | No | List of certificate types. |
| certPurpose | [certificateManager.CertificatePurpose](../ohos-security-certmanager-certificate-management/document.md#certificatepurpose22) | No | Yes | 
Certificate usage.

If the **certTypes** parameter contains the **CertificateType.CREDENTIAL\_UKEY** type, the **certPurpose** parameter takes effect.

 |

#### certificateManagerDialog.openCertificateManagerDialog

openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>

Opens the certificate management dialog box and displays the page of the specified type. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| pageType | [CertificateDialogPageType](#certificatedialogpagetype) | Yes | Type of the page to display. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
/\* pageType specifies the type of the page to display. In this example, pageType is PAGE\_MAIN, which indicates the main page of the Certificate Management application. \*/
let pageType: certificateManagerDialog.CertificateDialogPageType = certificateManagerDialog.CertificateDialogPageType.PAGE\_MAIN;
try {
  certificateManagerDialog.openCertificateManagerDialog(context, pageType).then(() => {
    console.info('Succeeded in opening certificate manager dialog.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to open certificate manager dialog. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (error) {
  console.error(\`Failed to open certificate manager dialog. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openInstallCertificateDialog14+

openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>

Opens a dialog box for installing a certificate. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Device support**: This API is available on PCs/2-in-1 devices. For other devices, error code 29700004 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| certType | [CertificateType](#certificatetype14) | Yes | Type of the certificate to install. |
| certScope | [CertificateScope](#certificatescope14) | Yes | Defines the usage scope of the certificate to be installed. |
| cert | Uint8Array | Yes | Data of the certificate to install. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the certificate URI. The value contains up to 256 bytes. |

**Error codes**

For details about the error codes, see [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the installation operation. |
| 29700003 | The user install certificate failed in the certificate manager dialog, such as the certificate is in an invalid format. |
| 29700004 | The API is not supported on this device. |
| 29700005 | The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
/\* certificateType specifies the certificate type. The value CA\_CERT here indicates a CA certificate. \*/
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA\_CERT;
/\* certificateScope specifies the usage scope of the certificate. The value CURRENT\_USER here means the certificate can be used by the current user. \*/
let certificateScope: certificateManagerDialog.CertificateScope = certificateManagerDialog.CertificateScope.CURRENT\_USER;
/\* The CA certificate data must be assigned by the service. In this example, the data is not CA certificate data. \*/
let caCert: Uint8Array = new Uint8Array(\[
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
\]);
try {
  certificateManagerDialog.openInstallCertificateDialog(context, certificateType, certificateScope, caCert).then((uri: string) => {
    console.info('Succeeded opening install certificate');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to open install certificate dialog. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (error) {
  console.error(\`Failed to open install certificate dialog. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openUninstallCertificateDialog18+

openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>

Opens a dialog box for deleting a certificate. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Device support**: This API is available on PCs/2-in-1 devices. For other devices, error code 29700004 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| certType | [CertificateType](#certificatetype14) | Yes | Type of the certificate to delete. |
| certUri | string | Yes | Unique identifier of the certificate to delete. The value contains up to 256 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the uninstallation operation. |
| 29700003 | The user uninstall certificate failed in the certificate manager dialog, such as the certificate uri is not exist. |
| 29700004 | The API is not supported on this device. |
| 29700005 | The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
/\* certificateType specifies the certificate type. The value CA\_CERT here indicates a CA certificate. \*/
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA\_CERT;
/\* certUri is the unique identifier of the certificate installed. The value here is only an example. \*/
let certUri: string = "test";
try {
  certificateManagerDialog.openUninstallCertificateDialog(context, certificateType, certUri).then(() => {
    console.info('Succeeded opening uninstall certificate');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to open uninstall certificate dialog. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (error) {
  console.error(\`Failed to open uninstall certificate dialog. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openCertificateDetailDialog18+

openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>

Opens the certificate management dialog box and displays the certificate details. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Device support**: This API is available on PCs/2-in-1 devices. For other devices, error code 29700004 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| cert | Uint8Array | Yes | Data of the certificate to install. |
| property | [CertificateDialogProperty](#certificatedialogproperty18) | Yes | Property of the certificate management dialog box. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700003 | Show the certificate detail dialog failed, such as the certificate is in an invalid format. |
| 29700004 | The API is not supported on this device. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
/\* The CA certificate data must be assigned by the service. In this example, the data is not CA certificate data. \*/
let caCert: Uint8Array = new Uint8Array(\[
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
\]);
let property: certificateManagerDialog.CertificateDialogProperty = {
  showInstallButton: false /\* Do not display the button for installing the certificate.\*/
};
try {
  certificateManagerDialog.openCertificateDetailDialog(context, caCert, property).then(() => {
    console.info('Succeeded opening certificate detail dialog.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to open certificate detail dialog. Code: ${err.code}, message: ${err.message}\`);
  })
} catch (error) {
  console.error(\`Failed to open certificate detail dialog. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openAuthorizeDialog20+

openAuthorizeDialog(context: common.Context): Promise<string>

Opens the authorization page of the certificate management dialog box to grant a certificate to the application. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the URI of the certificate authorized. The value contains up to 256 bytes. |

**Error codes**

For details about the error codes, see [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Invalid parameter. Possible causes: 1. A mandatory parameter is left unspecified. 2. Incorrect parameter type. 3. Parameter verification failed. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the authorization. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
try {
    certificateManagerDialog.openAuthorizeDialog(context).then((uri: string) => {
        console.info(\`Success to authorize certificate, uri: ${uri}\`)
    }).catch((err: BusinessError) => {
        console.error(\`Failed to authorize certificate. Code: ${err.code}, message: ${err.message}\`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(\`Failed to authorize certificate. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openAuthorizeDialog22+

openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>

Opens the PIN authentication dialog box of the USB credential. On the displayed page, the user authorizes the certificate for the application. The certificate types that can be authorized include the application private credential, user public credential, and USB credential. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Device behavior differences**: This API can be properly called on PCs. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| authorizeRequest | [AuthorizeRequest](#authorizerequest22) | Yes | Authorization request information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CertReference](#certreference22)\> | Promise used to return the result of the authorization certificate reference. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error; 4. Call other service failed. Please try again. |
| 29700002 | The user cancels the authorization. |
| 29700006 | Indicates that the input parameters validation failed. for example, the parameter format is incorrect or the value range is invalid. |
| 29700007 | No available certificate for authorization |

**Example**

import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
let certTypes: Array<certificateManagerDialog.CertificateType> = \[
  certificateManagerDialog.CertificateType.CREDENTIAL\_USER,
  certificateManagerDialog.CertificateType.CREDENTIAL\_APP,
  certificateManagerDialog.CertificateType.CREDENTIAL\_UKEY
\];
let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE\_DEFAULT;
let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
try {
    certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
      let reference = certReference;
      console.info(\`Success to open authorize dialog.\`)
    }).catch((err: BusinessError) => {
        console.error(\`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}\`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(\`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}\`);
}

#### certificateManagerDialog.openUkeyAuthDialog22+

openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>

Opens the PIN authentication dialog box of the USB credential. On the displayed page, the user can enter the PIN to authorize the USB credential. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**System capability**: SystemCapability.Security.CertificateManagerDialog

**Device behavior differences**: This API can be properly called on PCs. If it is called on other device types, error code 801 is returned.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.Context](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md) | Yes | Context of the application. |
| ukeyAuthRequest | [UkeyAuthRequest](#ukeyauthrequest22) | Yes | Authorization request information of the USB credential. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Certificate Management Dialog Box Error Codes](../../error-codes/certificate-management-dialog-box-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 29700001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 29700002 | The user cancels the authentication operation. |
| 29700003 | The authentication operation failed, such as the USB key certificate does not exist, the USB key status is abnormal. |
| 29700006 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |

**Example**

import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/\* context is application context information, which is obtained by the caller. The context here is only an example. \*/
let context: common.Context = new UIContext().getHostContext() as common.Context;
/\* keyUri is the unique identifier of the credential. The invoker obtains the value by itself. The value here is only an example. \*/
let keyUri: string = "test"
let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: keyUri }
try {
    certificateManagerDialog.openUkeyAuthDialog(context, ukeyAuthRequest).then(() => {
        console.info(\`Success to open ukey authorization dialog\`)
    }).catch((err: BusinessError) => {
        console.error(\`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}\`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(\`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}\`);
}
