# Authentication Using Passkeys (C/C++)

#### API Description

The following table lists the main APIs provided by the passkey service.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

FIDO2\_ErrorCode [HMS\_FIDO2\_getClientCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/passkey#ga3745265749b2776403960fbeece3de77)([FIDO2\_CapabilityArray](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___capability_array) \*\* capability)

 | 

Queries the client capabilities supported by the current device or version.

 |
| 

FIDO2\_ErrorCode [HMS\_FIDO2\_getPlatformAuthenticator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/passkey#ga18b569cb28a659f4282acbb64e198195)([FIDO2\_AuthenticatorMetadataArray](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array) \*\*authenticators)

 | 

Queries the platform authenticator capabilities (face, fingerprint, and PIN) supported by the current device or version.

 |
| 

FIDO2\_ErrorCode [HMS\_FIDO2\_register](https://developer.huawei.com/consumer/en/doc/harmonyos-references/passkey#gaaaed812197e7dc4d5f9a3354d5349665)(const [FIDO2\_CredentialCreationOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___credential_creation_options) options, const [FIDO2\_TokenBinding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___token_binding) tokenBinding, const char \* origin, [FIDO2\_PublicKeyAttestationCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___public_key_attestation_credential) \*\* publicKeyAttestationCredential )

 | 

Registers a passkey.

 |
| 

FIDO2\_ErrorCode [HMS\_FIDO2\_authenticate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/passkey#gaac4365229064efc78dc25dceb7c932a3)(const [FIDO2\_CredentialRequestOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___credential_request_options) options, const [FIDO2\_TokenBinding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___token_binding) tokenBinding, const char \*origin, [FIDO2\_PublicKeyAssertionCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/_f_i_d_o2___public_key_assertion_credential) \*\*publicKeyAssertionCredential)

 | 

Performs authentication using a passkey.

 |

#### Development Procedure

The passkey service provides a FIDO client implementation based on FIDO2 standards. The following only demonstrates the usage of FIDO client APIs. You are responsible for implementing the logic related to the FIDO server, which is not described here. For details, please refer to [FIDO2 standards](https://fidoalliance.org/passkeys/) (here is the [website link disclaimer](../../website-link-disclaimer/document.md)).

Use the CMake script to link related dynamic libraries.

target\_link\_libraries(projectName libfido2\_ndk.z.so)

1.  Deploy the FIDO server in accordance with FIDO2 standards.
2.  Register a passkey.
    1.  Obtain capability information. Call the **HMS\_FIDO2\_getClientCapability** API to obtain the client capability list, and call the **HMS\_FIDO2\_getPlatformAuthenticator** API to obtain the platform authenticator capability list.
        
        #include "OnlineAuthenticationKit/fido2\_api.h"
        
        FIDO2\_ErrorCode TestGetClientCapability()
        {
            // Obtain the client capability list.
            FIDO2\_CapabilityArray \*capability = NULL;
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_getClientCapability(&capability);
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_CapabilityArray\_Destroy(capability);
                return ret;
            }
            return FIDO2\_SUCCESS; 
        }
        
        FIDO2\_ErrorCode GetPlatformAuthenticator()
        {
            // Obtain the platform authenticator capability list.
            FIDO2\_AuthenticatorMetadataArray \*authenticators = NULL;
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_getPlatformAuthenticator(&authenticators); 
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy(authenticators);
                return ret;
            }
            return FIDO2\_SUCCESS;
        }
        
    2.  Access the FIDO server, obtain the registration message, and call the **HMS\_FIDO2\_register** API for registration.
        
        FIDO2\_ErrorCode TestReg()
        {
            // Initialize the registration parameters. The **init** method must be called.
            FIDO2\_CredentialCreationOptions options;
            HMS\_FIDO2\_initCreationOptions(&options);
        
            // Registration message returned by the FIDO server. The specific message content is determined by you.
            FIDO2\_PublicKeyCredentialCreationOptions publicKey;  
        
            // Assemble registration information, including whether user mediation is required and the registration message.
            options.mediation = FIDO2\_CONDITIONAL;
            options.publicKey = publicKey; 
        
            // Initialize the **tokenBinding** parameter. You can leave the parameter empty, but the **init** method must be called.
            FIDO2\_TokenBinding tokenBinding;
            HMS\_FIDO2\_initTokenBinding(&tokenBinding);
        
            // Origin used for testing only. Change it based on your service needs.
            char \*origin = "http://www.fidotest.com"; 
        
            // Call **HMS\_FIDO2\_register** to register a passkey.
            FIDO2\_PublicKeyAttestationCredential\* publicKeyAttestationCredential = NULL; 
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_register(options, tokenBinding, origin, &publicKeyAttestationCredential);
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_PublicKeyAttestationCredential\_Destroy(publicKeyAttestationCredential);
                return ret;
            }
            return FIDO2\_SUCCESS;
        }
        
    3.  Assemble a registration response message based on the registration result (**publicKeyAttestationCredential**), send the message to the FIDO server for verification, and obtain the registration result message.
3.  Use the password for authentication.
    1.  Obtain capability information. Call the **HMS\_FIDO2\_getClientCapability** API to obtain the client capability list, and call the **HMS\_FIDO2\_getPlatformAuthenticator** API to obtain the platform authenticator capability list.
        
        #include "OnlineAuthenticationKit/fido2\_api.h"
        
        FIDO2\_ErrorCode TestGetClientCapability()
        {
            // Obtain the client capability list.
            FIDO2\_CapabilityArray \*capability = NULL;
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_getClientCapability(&capability);
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_CapabilityArray\_Destroy(capability);
                return ret;
            }
            return FIDO2\_SUCCESS; 
        }
        
        FIDO2\_ErrorCode GetPlatformAuthenticator()
        {
            // Obtain the platform authenticator capability list.
            FIDO2\_AuthenticatorMetadataArray \*authenticators = NULL;
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_getPlatformAuthenticator(&authenticators); 
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_AuthenticatorMetadataArray\_Destroy(authenticators);
                return ret;
            }
            return FIDO2\_SUCCESS;
        }
        
    2.  Access the FIDO server, obtain the authentication message, and call the **HMS\_FIDO2\_authenticate** API for authentication.
        
        FIDO2\_ErrorCode TestAuth()
        {
            // Initialize the authentication parameters. The **init** method must be called.
            FIDO2\_CredentialRequestOptions options;
            HMS\_FIDO2\_initRequestOptions(&options);
        
            // Authentication message returned by the FIDO server. The specific message content is determined by you.
            FIDO2\_PublicKeyCredentialRequestOptions publicKey;  
        
            // Assemble authentication information, including whether user mediation is required and the authentication message.
            options.mediation = FIDO2\_CONDITIONAL;
            options.publicKey = publicKey; 
        
            // Initialize the **tokenBinding** parameter. You can leave the parameter empty, but the **init** method must be called.
            FIDO2\_TokenBinding tokenBinding;
            HMS\_FIDO2\_initTokenBinding(&tokenBinding);
        
            // Origin used for testing only. Change it based on your service needs.
            char \*origin = "http://www.fidotest.com"; 
        
            // Call **HMS\_FIDO2\_authenticate** to perform authentication using the passkey.
            FIDO2\_PublicKeyAssertionCredential \*assertionCredential = NULL;
            FIDO2\_ErrorCode ret = HMS\_FIDO2\_authenticate(options, tokenBinding, origin, &assertionCredential);
        
            // Determine the error type based on the error code and rectify the fault accordingly. For details, please refer to the error code reference.
            if (ret != FIDO2\_SUCCESS) {
                HMS\_FIDO2\_PublicKeyAssertionCredential\_Destroy(assertionCredential);
                return ret;
            }
            return FIDO2\_SUCCESS;
        }
        
    3.  Assemble an authentication response message based on the authentication result (**assertionCredential**), send the message to the FIDO server for verification, and obtain the authentication result message.
