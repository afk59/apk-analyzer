# External Key Management Extension Overview

HUKS provides unified Ability extension APIs for the driver HAP to implement external key management extension as well as register and unregister the custom hardware key management module, meeting identity authentication requirements in scenarios such as browser-based two-way SSL authentication of Ukey certificates in the financial field.

A USB key (Ukey) is a hardware device based on the USB API, which can be used to store user private keys, certificates, and identity authentication information.

This guide describes how to implement identity authentication in scenarios such as browser-based two-way SSL authentication of Ukey certificates.

#### Working Principles

The following figure shows the process of calling APIs to implement identity authentication. For details about the process, see the marks in the figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/g_BAQarfShu5UauptmmePw/en-us_image_0000002568764813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69C1C765D141D0AE4B1BD1133CD99A2EC23FE57A4D962BFDEDE664F9D8CCA46C)

-   Mark 1: A Ukey device is inserted.
    
-   Mark 2: The driver HAP registers the external key management extension capability (Ukey Extension) through the Provider management API.
    
    The driver HAP can register and unregister the external key management extension capability through the Provider management capability. For details, see [Provider Management Overview and Specifications](../provider-management/provider-management-overview-and-specifications/document.md).
    
-   Mark 3: The application displays a selection dialog box for certificate authorization for the user to select a certificate.
    
    3.1: The IPC is used to read certificate information from the Ukey hardware.
    
-   Mark 4: The application layer queries HUKS for certificate details.
    
    4.1: The IPC is used to read certificate information from the Ukey hardware.
    
-   Mark 5: After the user selects a certificate, the application obtains the certificate index **KeyUri** (that is, **resourceId**) to open the resource and query the PIN authentication status.
    
    HUKS provides the PIN authentication and authentication status query capabilities. Before the PIN authentication, you can query its authentication status. For details, see [Ukey PIN Authentication](../ukey-pin-authentication-management/ukey-pin-authentication-overview-and-specifications/document.md).
    
    5.1: If the resource has not been authenticated, that is, the PIN has not been authenticated, the application needs to call the certificate management capability to display the PIN authentication dialog box. The user enters the PIN to complete the authentication. After the authentication is complete, the process goes to mark 5. The application calls the unified HUKS APIs to perform the corresponding operations.
    
-   Mark 6: The application calls the unified APIs provided by HUKS to perform operations such as resource management, signing, and signature verification. Example:
    
    -   [Open and close resources](../resource-management/resource-management-overview-and-specifications/document.md).
    -   [Verify the authenticity of the message content and the message sender](../signing-and-signature-verification/signing-and-signature-verification-overview-and-algorithm-specifications/document.md)
    
    In addition, HUKS allows the application to query the Ukey key properties. For details, see [General Query](../general-operations/general-query-overview-and-specifications/document.md).
    
-   Mark 7: Core operations, such as certificate query, resource management, PIN authentication, and signing, are performed at the HUKS SA layer.
    

Before the application initiates identity authentication based on the Ukey, the third-party driver HAP must complete the following operations:

-   Design and develop the external key management extension capabilities of the application based on service scenarios.
    
    The driver HAP must inherit **CryptoExtensionAbility** provided by HUKS and implement the capability APIs. For details, see [CryptoExtensionAbility Extension Capability Overview](../driver-hap-extensionability-adaptation-guide/cryptoextensionability-extension-capability-overview/document.md).
    
    **CryptoExtensionAbility** is a derived class of [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) in the stage model. You can customize external hardware key management by inheriting **CryptoExtensionAbility** and implementing custom APIs, including calling APIs for opening and closing resources of external hardware key management, implementing PIN authentication for external hardware key management, and calling general APIs of external hardware key management. For details, see [CryptoExtensionAbility Adaptation Development Guide](../driver-hap-extensionability-adaptation-guide/cryptoextensionability-adaptation-development-guide/document.md).
    
-   Register the key management extension capabilities with the system HUKS service.
    
    **CryptoExtensionAbility** can isolate the implementation differences of Ukey driver vendors. The capabilities implemented by the driver HAP are opened for applications through the SDKs of HUKS and [certificate management](../../../device-certificate-kit/certificate-management/certificate-management-overview/document.md).
    

In this way, the applications such as the browser can call the APIs provided by HUKS and [certificate management](../../../device-certificate-kit/certificate-management/certificate-management-overview/document.md) to use the external key management capabilities provided by the driver HAP, including certificate query, PIN authentication, and signing and signature verification.
