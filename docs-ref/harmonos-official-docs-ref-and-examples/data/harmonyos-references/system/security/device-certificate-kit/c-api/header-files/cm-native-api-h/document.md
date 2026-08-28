# cm\_native\_api.h

#### Overview

Declares the APIs used to obtain details of specific certificates.

**File to include**: <device\_certificate/certmanager/cm\_native\_api.h>

**Library**: libohcert\_manager.so

**System capability**: SystemCapability.Security.CertificateManager

**Since**: 22

**Related module**: [CertManager](../../modules/certmanager/document.md)

#### Summary

## Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_CertManager\_GetUkeyCertificate(const OH\_CM\_Blob \*keyUri, const OH\_CM\_UkeyInfo \*ukeyInfo, OH\_CM\_CredentialDetailList \*certificateList)](#oh_certmanager_getukeycertificate) | Obtains the detail list of USB certificate credentials. |
| [int32\_t OH\_CertManager\_GetPrivateCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)](#oh_certmanager_getprivatecertificate) | Obtains the details of a private certificate credential of a specific application. |
| [int32\_t OH\_CertManager\_GetPublicCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)](#oh_certmanager_getpubliccertificate) | Obtains the details of a public certificate credential of a specific user. |
| [void OH\_CertManager\_FreeUkeyCertificate(OH\_CM\_CredentialDetailList \*certificateList)](#oh_certmanager_freeukeycertificate) | Destroys the certificate detail list. |
| [void OH\_CertManager\_FreeCredential(OH\_CM\_Credential \*certificate)](#oh_certmanager_freecredential) | Destroys the certificate details. |

#### Function Description

## OH\_CertManager\_GetUkeyCertificate()

int32\_t OH\_CertManager\_GetUkeyCertificate(const OH\_CM\_Blob \*keyUri, const OH\_CM\_UkeyInfo \*ukeyInfo, OH\_CM\_CredentialDetailList \*certificateList)

**Description**

Obtains the detail list of USB certificate credentials.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_CM\_Blob](../../structs/oh-cm-blob/document.md) \*keyUri | Pointer to the URI that stores the USB certificate credentials, in string format. |
| [const OH\_CM\_UkeyInfo](../../structs/oh-cm-ukeyinfo/document.md) \*ukeyInfo | Pointer to the property information of the USB certificate credential. |
| [OH\_CM\_CredentialDetailList](../../structs/oh-cm-credentialdetaillist/document.md) \*certificateList | Pointer to the USB certificate credential detail list obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[OH\_CM\_ErrorCode](../cm-native-type-h/document.md#oh_cm_errorcode):

**OH\_CM\_SUCCESS = 0**: Operation successful.

**OH\_CM\_HAS\_NO\_PERMISSION = 201**: Permission verification failed.

**OH\_CM\_CAPABILITY\_NOT\_SUPPORTED = 801**: The device is not supported.

**OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011**: Input parameter verification failed. Possible causes:

1\. Incorrect parameter format.

2\. Invalid parameter value range.

**OH\_CM\_INNER\_FAILURE = 17500001**: Internal error. Possible causes:

1\. IPC failure.

2\. Memory operation error.

3\. File operation error.

**OH\_CM\_NOT\_FOUND = 17500002**: The certificate does not exist.

**OH\_CM\_ACCESS\_UKEY\_SERVICE\_FAILED = 17500010**: Failed to access the USB certificate credential.

 |

## OH\_CertManager\_GetPrivateCertificate()

int32\_t OH\_CertManager\_GetPrivateCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)

**Description**

Obtains the details of a private certificate credential of a specific application.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_CM\_Blob](../../structs/oh-cm-blob/document.md) \*keyUri | Pointer to the URI that stores the application's private certificate credentials, in string format. |
| [OH\_CM\_Credential](../../structs/oh-cm-credential/document.md) \*certificate | Pointer to the details of the application's private credentials obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[OH\_CM\_ErrorCode](../cm-native-type-h/document.md#oh_cm_errorcode):

**OH\_CM\_SUCCESS = 0**: Operation successful.

**OH\_CM\_HAS\_NO\_PERMISSION = 201**: Permission verification failed.

**OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011**: Input parameter verification failed. Possible causes:

1\. Incorrect parameter format.

2\. Invalid parameter value range.

**OH\_CM\_INNER\_FAILURE = 17500001**: Internal error. Possible causes:

1\. IPC failure.

2\. Memory operation error.

3\. File operation error.

**OH\_CM\_NOT\_FOUND = 17500002**: The certificate does not exist.

 |

## OH\_CertManager\_GetPublicCertificate()

int32\_t OH\_CertManager\_GetPublicCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)

**Description**

Obtains the details of a public certificate credential of a specific user.

**Required permissions**: ohos.permission.ACCESS\_CERT\_MANAGER

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_CM\_Blob](../../structs/oh-cm-blob/document.md) \*keyUri | Pointer to the URI that stores the user's public certificate credentials, in string format. |
| [OH\_CM\_Credential](../../structs/oh-cm-credential/document.md) \*certificate | Pointer to the details of the user's public certificate credential obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[OH\_CM\_ErrorCode](../cm-native-type-h/document.md#oh_cm_errorcode):

**OH\_CM\_SUCCESS = 0**: Operation successful.

**OH\_CM\_HAS\_NO\_PERMISSION = 201**: Permission verification failed.

**OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011**: Input parameter verification failed. Possible causes:

1\. Incorrect parameter format.

2\. Invalid parameter value range.

**OH\_CM\_INNER\_FAILURE = 17500001**: Internal error. Possible causes:

1\. IPC failure.

2\. Memory operation error.

3\. File operation error.

**OH\_CM\_NOT\_FOUND = 17500002**: The certificate does not exist.

**OH\_CM\_NO\_AUTHORIZATION = 17500005**: The application is not authorized.

 |

## OH\_CertManager\_FreeUkeyCertificate()

void OH\_CertManager\_FreeUkeyCertificate(OH\_CM\_CredentialDetailList \*certificateList)

**Description**

Destroys the certificate detail list.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_CM\_CredentialDetailList](../../structs/oh-cm-credentialdetaillist/document.md) \*certificateList | Pointer to the certificate credential detail list to be destroyed. |

## OH\_CertManager\_FreeCredential()

void OH\_CertManager\_FreeCredential(OH\_CM\_Credential \*certificate)

**Description**

Destroys the certificate details.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_CM\_Credential](../../structs/oh-cm-credential/document.md) \*certificate | Pointer to the certificate credential details to be destroyed. |
