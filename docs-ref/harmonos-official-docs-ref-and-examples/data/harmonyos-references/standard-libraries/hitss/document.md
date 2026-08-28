# HiTSS

#### Overview

HiTSS is a component developed based on the Trusted Platform Module (TPM) 2.0 specification. It provides APIs for accessing the TPM 2.0 chip, including command transmission APIs, system-level APIs, and marshalling and unmarshalling APIs. Through these APIs, you can access the TPM 2.0 chip's capabilities for various TPM operations, such as key creation, signing, and signature verification, simplifying the communication with the TPM 2.0 chip. HiTSS is currently only available to enterprise developers using HarmonyOS PCs.

#### HiTSS Versions

From API version 20, HiTSS complies with the following Trusted Computing Group (TCG) TPM2 Software Stack (TSS) specifications:

-   TCG TSS 2.0 Overview and Common Structures Specification Version 1.0 Revision 10, September 23 2021
-   TCG TSS 2.0 Marshaling/Unmarshaling API Specification Version 1.0 Revision 07, 10 March 2020
-   TCG TSS 2.0 System Level API (SAPI) Specification Version 1.1 Revision 36, October 1 2021
-   TCG TSS 2.0 TPM Command Transmission Interface (TCTI) API Specification Version 1.0 Revision 18, 24 January 2020

#### Supported Capabilities

-   Command transmission APIs. For details, please refer to [List of Command Transmission APIs Supported by HiTSS](#section27781593815).
-   Marshalling and unmarshalling APIs. For details, please refer to [List of Marshalling and Unmarshalling APIs Supported by HiTSS](#section9142142823511).
-   System-level APIs (HiTSS supports only a subset of the system-level APIs due to chip capability limitations). For details, please refer to [List of System-level APIs Supported by HiTSS](#section1705271331).

#### Introducing HiTSS Capabilities

1.  When developing an app, you need to apply for the **ohos.permission.CALL\_TPM\_CMD** permission before accessing the command transmission APIs or system-level APIs. For details about how to apply for the permission, please refer to [Requesting Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions-in-acl).
2.  To use HiTSS capabilities, include the following header files.
    
    #include <tss2/tss2\_common.h>
    #include <tss2/tss2\_tpm2\_types.h>
    #include <tss2/tss2\_mu.h>
    #include <tss2/tss2\_sys.h>
    #include <tss2/tss2\_tcti.h>
    #include <tss2/tss2\_tctildr.h>
    
3.  Add the following dynamic-link libraries to **CMakeLists.txt**:
    
    libtss2-mu.so
    libtss2-sys.so
    libtss2-tctildr.so
    

#### Example

#include <stdio.h>
#include <tss2/tss2\_tctildr.h>
#include <tss2/tss2\_sys.h>
#include <tss2/tss2\_mu.h>

#define SAFE\_FREE(p) do { \\
    if ((p) != NULL) { \\
        free(p); \\
        (p) = NULL; \\
    } \\
} while (false)

// Initialize the context.
TSS2\_SYS\_CONTEXT\* InitSysCtx()
{
    TSS2\_TCTI\_CONTEXT \*tctiCtx = NULL;
    const char \*nameConf = "hmsa";
    // You cannot set **conf** in the **nameConf** parameter value. **conf** must be empty.
    // Example of correct **nameConf** setting.
    // Tss2\_TctiLdr\_Initialize("hmsa", &tctiCtx);
    // Tss2\_TctiLdr\_Initialize("hmsa:", &tctiCtx);
    // Example of incorrect **nameConf** setting.
    **// Tss2\_TctiLdr\_Initialize("hmsa:/dev/tpm0", &tctiCtx);**
    TSS2\_RC rc = Tss2\_TctiLdr\_Initialize(nameConf, &tctiCtx);
    if (rc != TSS2\_RC\_SUCCESS) {
        return NULL;
    }
    size\_t size = Tss2\_Sys\_GetContextSize(0);
    TSS2\_SYS\_CONTEXT \*sysCtx = (TSS2\_SYS\_CONTEXT \*)calloc(1, size);
    if (sysCtx == nullptr) {
        return NULL;
    }
    TSS2\_ABI\_VERSION ver = TSS2\_ABI\_VERSION\_CURRENT;
    rc = Tss2\_Sys\_Initialize(sysCtx, size, tctiCtx, &ver);
    if (rc != TSS2\_RC\_SUCCESS) {
        Tss2\_TctiLdr\_Finalize(&tctiCtx);
        SAFE\_FREE(sysCtx);
        return NULL;
    }
    return sysCtx;
}

// Release the context.
void ReleaseSysCtx(TSS2\_SYS\_CONTEXT \*\*sysCtx)
{
    TSS2\_TCTI\_CONTEXT \*tctiCtx = NULL;
    TSS2\_RC rc = Tss2\_Sys\_GetTctiContext(\*sysCtx, &tctiCtx);
    if (rc != TSS2\_RC\_SUCCESS) {
        return;
    }
    if (tctiCtx != NULL) {
        Tss2\_TctiLdr\_Finalize(&tctiCtx);
    }
    Tss2\_Sys\_Finalize(\*sysCtx);
    SAFE\_FREE(\*sysCtx);
}

// Example of obtaining a random number through the **Sys** API.
void GetRandomExample()
{
    TSS2\_SYS\_CONTEXT \*sysCtx = InitSysCtx();
    if (sysCtx == NULL) {
        return;
    }
    TPM2B\_DIGEST random = {};
    TSS2\_RC rc = Tss2\_Sys\_GetRandom(sysCtx, NULL, 32, &random, NULL); // **32** indicates the random number length.
    if (rc != TSS2\_RC\_SUCCESS) {
        printf("Failed to get random, error:%d.\\n", rc);
    }
    ReleaseSysCtx(&sysCtx);
}

// Example of obtaining a random number through the **Sys** API.
void GetRandomExample2()
{
    TSS2\_SYS\_CONTEXT \*sysCtx = InitSysCtx();
    if (sysCtx == NULL) {
        return;
    }
    TPM2B\_DIGEST random = {};
    do {
        if (Tss2\_Sys\_GetRandom\_Prepare(sysCtx, 32) != TSS2\_RC\_SUCCESS) { // **32** indicates the random number length.
            break;
        }
        if (Tss2\_Sys\_Execute(sysCtx) != TSS2\_RC\_SUCCESS) {
            break;
        }
        if (Tss2\_Sys\_GetRandom\_Complete(sysCtx, &random) != TSS2\_RC\_SUCCESS) {
            break;
        }
    } while(false);
    ReleaseSysCtx(&sysCtx);
}

// Example of using the **MU** API.
void Int32MarshalUnmarshalExample()
{
    INT32 data = 20;
    uint8\_t buffer\[sizeof(data)\] = { 0 };
    size\_t bufferSize = sizeof(data);
    // Perform data marshalling.
    TSS2\_RC rc = Tss2\_MU\_INT32\_Marshal(data, buffer, bufferSize, NULL);
    if (rc != TSS2\_RC\_SUCCESS) {
        printf("Failed to marshal data, error:%d.\\n", rc);
    }
    INT32 dest = 0;
    // Perform data unmarshalling and print the data.
    rc = Tss2\_MU\_INT32\_Unmarshal(buffer, bufferSize, NULL, &dest);
    if (rc != TSS2\_RC\_SUCCESS) {
        printf("Failed to unmarshal data, error:%d.\\n", rc);
    }
    printf("The unmarshal result is %d.\\n", dest);
}

#### Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Q5epdj7vT6mZXiYAhT-lNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062529Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B4B3D241EA9E429B2CB3167B71F7D3FBB170276048ADE03CF8815833F102EF1)

This section describes only HiTSS-specific error codes. For details about common error codes, please refer to [TCG TSS 2.0 Overview and Common Structures Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_Overview_Common_v1_r10_pub09232021.pdf).

## TSS2\_BASE\_RC\_INTERNAL\_ERROR

**Description**

Internal error.

**Possible causes**

The internal processing logic of the code is not as expected.

**Solution**

Ensure that the code logic is correct and the chip is in a normal state.

## TSS2\_BASE\_RC\_SAPI\_INIT

**Description**

The SAPI context failed to be initialized.

**Possible causes**

Incorrect input parameters.

**Solution**

Ensure that input parameters of the API are correct.

## TSS2\_BASE\_RC\_CANCEL

**Description**

Command cancellation error.

**Possible causes**

The command queue is full.

**Solution**

Try again.

## TSS2\_TCTI\_RC\_MEMORY

**Description**

A memory error occurred in the TCTI API.

**Possible causes**

The device memory is insufficient or another memory exception occurred.

**Solution**

Ensure that the available device memory is greater than the requested memory, and clear the device memory in a timely manner.

#### Differences from the TCG TSS Specifications

The following types and structures are different from those in the TCG TSS specifications, as HiTSS has expanded the capabilities and rectified errors based on the specifications.

// New macro definition added by HiTSS.
#define TPM2\_ST\_ATTEST\_NV\_DIGEST ((TPM2\_ST) 0x801C)

// HiTSS adds the **nvDigest** field.
typedef union TPMU\_ATTEST TPMU\_ATTEST;
union TPMU\_ATTEST {
    TPMS\_CERTIFY\_INFO certify; /\* TPM2\_ST\_ATTEST\_CERTIFY \*/
    TPMS\_CREATION\_INFO creation; /\* TPM2\_ST\_ATTEST\_CREATION \*/
    TPMS\_QUOTE\_INFO quote; /\* TPM2\_ST\_ATTEST\_QUOTE \*/
    TPMS\_COMMAND\_AUDIT\_INFO commandAudit; /\* TPM2\_ST\_ATTEST\_COMMAND\_AUDIT \*/
    TPMS\_SESSION\_AUDIT\_INFO sessionAudit; /\* TPM2\_ST\_ATTEST\_SESSION\_AUDIT \*/
    TPMS\_TIME\_ATTEST\_INFO time; /\* TPM2\_ST\_ATTEST\_TIME \*/
    TPMS\_NV\_CERTIFY\_INFO nv; /\* TPM2\_ST\_ATTEST\_NV \*/
    TPMS\_NV\_DIGEST\_CERTIFY\_INFO nvDigest; /\* TPM2\_ST\_ATTEST\_NV\_DIGEST \*/
};

// New type added by HiTSS.
typedef TPM2\_KEY\_BITS TPMI\_TDES\_KEY\_BITS;

// HiTSS adds the **tdes** field.
typedef union TPMU\_SYM\_KEY\_BITS TPMU\_SYM\_KEY\_BITS;
union TPMU\_SYM\_KEY\_BITS {
    TPMI\_TDES\_KEY\_BITS tdes; /\* TPM2\_ALG\_TDES \*/
    TPMI\_AES\_KEY\_BITS aes; /\* TPM2\_ALG\_AES \*/
    TPMI\_SM4\_KEY\_BITS sm4; /\* TPM2\_ALG\_SM4 \*/
    TPMI\_CAMELLIA\_KEY\_BITS camellia; /\* TPM2\_ALG\_CAMELLIA \*/
    TPM2\_KEY\_BITS sym;
    TPMI\_ALG\_HASH exclusiveOr; /\* TPM2\_ALG\_XOR \*/
    TPMS\_EMPTY null; /\* TPM2\_ALG\_NULL \*/
};

// HiTSS adds the **tdes** field.
typedef union TPMU\_SYM\_MODE TPMU\_SYM\_MODE;
union TPMU\_SYM\_MODE {
    TPMI\_ALG\_SYM\_MODE tdes; /\* TPM2\_ALG\_TDES \*/
    TPMI\_ALG\_SYM\_MODE aes; /\* TPM2\_ALG\_AES \*/
    TPMI\_ALG\_SYM\_MODE sm4; /\* TPM2\_ALG\_SM4 \*/
    TPMI\_ALG\_SYM\_MODE camellia; /\* TPM2\_ALG\_CAMELLIA \*/
    TPMI\_ALG\_SYM\_MODE sym;
    TPMS\_EMPTY exclusiveOr; /\* TPM2\_ALG\_XOR \*/
    TPMS\_EMPTY null; /\* TPM2\_ALG\_NULL \*/
};

// Definition not provided by the TCG specification.
typedef UINT32 TPM2\_AT;

// Definition not provided by the TCG specification.
#define TPM2\_MAX\_AC\_CAPABILITIES (TPM2\_MAX\_CAP\_BUFFER / sizeof(TPMS\_AC\_OUTPUT))

// TPM2B struct added by HiTSS to facilitate developer convenience.
typedef struct {
    UINT16 size;
    BYTE buffer\[\];
} TPM2B;

// Definition not provided by the TCG specification.
typedef TPM2\_HANDLE TPMI\_RH\_HIERARCHY\_POLICY;

// HiTSS rectifies the **tag** field type that is incorrectly defined in the TCG specification.
typedef struct TPMS\_AC\_OUTPUT TPMS\_AC\_OUTPUT;
struct TPMS\_AC\_OUTPUT {
    TPM2\_AT tag;
    UINT32 data;
};

#### References

-   [TCG TSS 2.0 Marshaling/Unmarshaling API Specification](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TSS_Marshaling_Unmarshaling_API_v1p0_r07_pub.pdf)
-   [TCG TSS 2.0 System Level API (SAPI) Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_SAPI_v1p1_r36_pub10012021.pdf)
-   [TCG TSS 2.0 TPM Command Transmission Interface (TCTI) API Specification](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TSS_TCTI_v1p0_r18_pub.pdf)
-   [TCG TSS 2.0 Overview and Common Structures Specification](https://trustedcomputinggroup.org/wp-content/uploads/TSS_Overview_Common_v1_r10_pub09232021.pdf)

#### List of System-level APIs Supported by HiTSS

## APIs for Command Context Management

-   Tss2\_Sys\_GetContextSize
-   Tss2\_Sys\_Initialize
-   Tss2\_Sys\_Finalize
-   Tss2\_Sys\_GetTctiContext

## APIs for Command Preparation

-   Tss2\_Sys\_SetCmdAuths

## APIs for Command Execution

-   Tss2\_Sys\_ExecuteAsync
-   Tss2\_Sys\_ExecuteFinish
-   Tss2\_Sys\_Execute
-   Tss2\_Sys\_GetRspAuths

## APIs for TPM Command Invocation

| 
Prepare API

 | 

Complete API

 | 

Command API

 |
| :-- | :-- | :-- |
| 

Tss2\_Sys\_Startup\_Prepare

 | 

Tss2\_Sys\_Startup\_Complete

 | 

Tss2\_Sys\_Startup

 |
| 

Tss2\_Sys\_Shutdown\_Prepare

 | 

Tss2\_Sys\_Shutdown\_Complete

 | 

Tss2\_Sys\_Shutdown

 |
| 

Tss2\_Sys\_SelfTest\_Prepare

 | 

Tss2\_Sys\_SelfTest\_Complete

 | 

Tss2\_Sys\_SelfTest

 |
| 

Tss2\_Sys\_IncrementalSelfTest\_Prepare

 | 

Tss2\_Sys\_IncrementalSelfTest\_Complete

 | 

Tss2\_Sys\_IncrementalSelfTest

 |
| 

Tss2\_Sys\_GetTestResult\_Prepare

 | 

Tss2\_Sys\_GetTestResult\_Complete

 | 

Tss2\_Sys\_GetTestResult

 |
| 

Tss2\_Sys\_StartAuthSession\_Prepare

 | 

Tss2\_Sys\_StartAuthSession\_Complete

 | 

Tss2\_Sys\_StartAuthSession

 |
| 

Tss2\_Sys\_PolicyRestart\_Prepare

 | 

Tss2\_Sys\_PolicyRestart\_Complete

 | 

Tss2\_Sys\_PolicyRestart

 |
| 

Tss2\_Sys\_Create\_Prepare

 | 

Tss2\_Sys\_Create\_Complete

 | 

Tss2\_Sys\_Create

 |
| 

Tss2\_Sys\_Load\_Prepare

 | 

Tss2\_Sys\_Load\_Complete

 | 

Tss2\_Sys\_Load

 |
| 

Tss2\_Sys\_LoadExternal\_Prepare

 | 

Tss2\_Sys\_LoadExternal\_Complete

 | 

Tss2\_Sys\_LoadExternal

 |
| 

Tss2\_Sys\_ReadPublic\_Prepare

 | 

Tss2\_Sys\_ReadPublic\_Complete

 | 

Tss2\_Sys\_ReadPublic

 |
| 

Tss2\_Sys\_ActivateCredential\_Prepare

 | 

Tss2\_Sys\_ActivateCredential\_Complete

 | 

Tss2\_Sys\_ActivateCredential

 |
| 

Tss2\_Sys\_MakeCredential\_Prepare

 | 

Tss2\_Sys\_MakeCredential\_Complete

 | 

Tss2\_Sys\_MakeCredential

 |
| 

Tss2\_Sys\_Unseal\_Prepare

 | 

Tss2\_Sys\_Unseal\_Complete

 | 

Tss2\_Sys\_Unseal

 |
| 

Tss2\_Sys\_ObjectChangeAuth\_Prepare

 | 

Tss2\_Sys\_ObjectChangeAuth\_Complete

 | 

Tss2\_Sys\_ObjectChangeAuth

 |
| 

Tss2\_Sys\_CreateLoaded\_Prepare

 | 

Tss2\_Sys\_CreateLoaded\_Complete

 | 

Tss2\_Sys\_CreateLoaded

 |
| 

Tss2\_Sys\_Duplicate\_Prepare

 | 

Tss2\_Sys\_Duplicate\_Complete

 | 

Tss2\_Sys\_Duplicate

 |
| 

Tss2\_Sys\_Rewrap\_Prepare

 | 

Tss2\_Sys\_Rewrap\_Complete

 | 

Tss2\_Sys\_Rewrap

 |
| 

Tss2\_Sys\_Import\_Prepare

 | 

Tss2\_Sys\_Import\_Complete

 | 

Tss2\_Sys\_Import

 |
| 

Tss2\_Sys\_RSA\_Encrypt\_Prepare

 | 

Tss2\_Sys\_RSA\_Encrypt\_Complete

 | 

Tss2\_Sys\_RSA\_Encrypt

 |
| 

Tss2\_Sys\_RSA\_Decrypt\_Prepare

 | 

Tss2\_Sys\_RSA\_Decrypt\_Complete

 | 

Tss2\_Sys\_RSA\_Decrypt

 |
| 

Tss2\_Sys\_ECDH\_KeyGen\_Prepare

 | 

Tss2\_Sys\_ECDH\_KeyGen\_Complete

 | 

Tss2\_Sys\_ECDH\_KeyGen

 |
| 

Tss2\_Sys\_ECDH\_ZGen\_Prepare

 | 

Tss2\_Sys\_ECDH\_ZGen\_Complete

 | 

Tss2\_Sys\_ECDH\_ZGen

 |
| 

Tss2\_Sys\_ECC\_Parameters\_Prepare

 | 

Tss2\_Sys\_ECC\_Parameters\_Complete

 | 

Tss2\_Sys\_ECC\_Parameters

 |
| 

Tss2\_Sys\_ZGen\_2Phase\_Prepare

 | 

Tss2\_Sys\_ZGen\_2Phase\_Complete

 | 

Tss2\_Sys\_ZGen\_2Phase

 |
| 

Tss2\_Sys\_EncryptDecrypt\_Prepare

 | 

Tss2\_Sys\_EncryptDecrypt\_Complete

 | 

Tss2\_Sys\_EncryptDecrypt

 |
| 

Tss2\_Sys\_EncryptDecrypt2\_Prepare

 | 

Tss2\_Sys\_EncryptDecrypt2\_Complete

 | 

Tss2\_Sys\_EncryptDecrypt2

 |
| 

Tss2\_Sys\_Hash\_Prepare

 | 

Tss2\_Sys\_Hash\_Complete

 | 

Tss2\_Sys\_Hash

 |
| 

Tss2\_Sys\_HMAC\_Prepare

 | 

Tss2\_Sys\_HMAC\_Complete

 | 

Tss2\_Sys\_HMAC

 |
| 

Tss2\_Sys\_GetRandom\_Prepare

 | 

Tss2\_Sys\_GetRandom\_Complete

 | 

Tss2\_Sys\_GetRandom

 |
| 

Tss2\_Sys\_StirRandom\_Prepare

 | 

Tss2\_Sys\_StirRandom\_Complete

 | 

Tss2\_Sys\_StirRandom

 |
| 

Tss2\_Sys\_HashSequenceStart\_Prepare

 | 

Tss2\_Sys\_HashSequenceStart\_Complete

 | 

Tss2\_Sys\_HashSequenceStart

 |
| 

Tss2\_Sys\_SequenceUpdate\_Prepare

 | 

Tss2\_Sys\_SequenceUpdate\_Complete

 | 

Tss2\_Sys\_SequenceUpdate

 |
| 

Tss2\_Sys\_SequenceComplete\_Prepare

 | 

Tss2\_Sys\_SequenceComplete\_Complete

 | 

Tss2\_Sys\_SequenceComplete

 |
| 

Tss2\_Sys\_Certify\_Prepare

 | 

Tss2\_Sys\_Certify\_Complete

 | 

Tss2\_Sys\_Certify

 |
| 

Tss2\_Sys\_CertifyCreation\_Prepare

 | 

Tss2\_Sys\_CertifyCreation\_Complete

 | 

Tss2\_Sys\_CertifyCreation

 |
| 

Tss2\_Sys\_Quote\_Prepare

 | 

Tss2\_Sys\_Quote\_Complete

 | 

Tss2\_Sys\_Quote

 |
| 

Tss2\_Sys\_Commit\_Prepare

 | 

Tss2\_Sys\_Commit\_Complete

 | 

Tss2\_Sys\_Commit

 |
| 

Tss2\_Sys\_EC\_Ephemeral\_Prepare

 | 

Tss2\_Sys\_EC\_Ephemeral\_Complete

 | 

Tss2\_Sys\_EC\_Ephemeral

 |
| 

Tss2\_Sys\_VerifySignature\_Prepare

 | 

Tss2\_Sys\_VerifySignature\_Complete

 | 

Tss2\_Sys\_VerifySignature

 |
| 

Tss2\_Sys\_Sign\_Prepare

 | 

Tss2\_Sys\_Sign\_Complete

 | 

Tss2\_Sys\_Sign

 |
| 

Tss2\_Sys\_PCR\_Extend\_Prepare

 | 

Tss2\_Sys\_PCR\_Extend\_Complete

 | 

Tss2\_Sys\_PCR\_Extend

 |
| 

Tss2\_Sys\_PCR\_Event\_Prepare

 | 

Tss2\_Sys\_PCR\_Event\_Complete

 | 

Tss2\_Sys\_PCR\_Event

 |
| 

Tss2\_Sys\_PCR\_Read\_Prepare

 | 

Tss2\_Sys\_PCR\_Read\_Complete

 | 

Tss2\_Sys\_PCR\_Read

 |
| 

Tss2\_Sys\_PCR\_Allocate\_Prepare

 | 

Tss2\_Sys\_PCR\_Allocate\_Complete

 | 

Tss2\_Sys\_PCR\_Allocate

 |
| 

Tss2\_Sys\_PCR\_Reset\_Prepare

 | 

Tss2\_Sys\_PCR\_Reset\_Complete

 | 

Tss2\_Sys\_PCR\_Reset

 |
| 

Tss2\_Sys\_PolicySigned\_Prepare

 | 

Tss2\_Sys\_PolicySigned\_Complete

 | 

Tss2\_Sys\_PolicySigned

 |
| 

Tss2\_Sys\_PolicySecret\_Prepare

 | 

Tss2\_Sys\_PolicySecret\_Complete

 | 

Tss2\_Sys\_PolicySecret

 |
| 

Tss2\_Sys\_PolicyTicket\_Prepare

 | 

Tss2\_Sys\_PolicyTicket\_Complete

 | 

Tss2\_Sys\_PolicyTicket

 |
| 

Tss2\_Sys\_PolicyOR\_Prepare

 | 

Tss2\_Sys\_PolicyOR\_Complete

 | 

Tss2\_Sys\_PolicyOR

 |
| 

Tss2\_Sys\_PolicyPCR\_Prepare

 | 

Tss2\_Sys\_PolicyPCR\_Complete

 | 

Tss2\_Sys\_PolicyPCR

 |
| 

Tss2\_Sys\_PolicyCommandCode\_Prepare

 | 

Tss2\_Sys\_PolicyCommandCode\_Complete

 | 

Tss2\_Sys\_PolicyCommandCode

 |
| 

Tss2\_Sys\_PolicyCpHash\_Prepare

 | 

Tss2\_Sys\_PolicyCpHash\_Complete

 | 

Tss2\_Sys\_PolicyCpHash

 |
| 

Tss2\_Sys\_PolicyAuthValue\_Prepare

 | 

Tss2\_Sys\_PolicyAuthValue\_Complete

 | 

Tss2\_Sys\_PolicyAuthValue

 |
| 

Tss2\_Sys\_PolicyPassword\_Prepare

 | 

Tss2\_Sys\_PolicyPassword\_Complete

 | 

Tss2\_Sys\_PolicyPassword

 |
| 

Tss2\_Sys\_PolicyGetDigest\_Prepare

 | 

Tss2\_Sys\_PolicyGetDigest\_Complete

 | 

Tss2\_Sys\_PolicyGetDigest

 |
| 

Tss2\_Sys\_CreatePrimary\_Prepare

 | 

Tss2\_Sys\_CreatePrimary\_Complete

 | 

Tss2\_Sys\_CreatePrimary

 |
| 

Tss2\_Sys\_HierarchyControl\_Prepare

 | 

Tss2\_Sys\_HierarchyControl\_Complete

 | 

Tss2\_Sys\_HierarchyControl

 |
| 

Tss2\_Sys\_Clear\_Prepare

 | 

Tss2\_Sys\_Clear\_Complete

 | 

Tss2\_Sys\_Clear

 |
| 

Tss2\_Sys\_ClearControl\_Prepare

 | 

Tss2\_Sys\_ClearControl\_Complete

 | 

Tss2\_Sys\_ClearControl

 |
| 

Tss2\_Sys\_HierarchyChangeAuth\_Prepare

 | 

Tss2\_Sys\_HierarchyChangeAuth\_Complete

 | 

Tss2\_Sys\_HierarchyChangeAuth

 |
| 

Tss2\_Sys\_DictionaryAttackLockReset\_Prepare

 | 

Tss2\_Sys\_DictionaryAttackLockReset\_Complete

 | 

Tss2\_Sys\_DictionaryAttackLockReset

 |
| 

Tss2\_Sys\_DictionaryAttackParameters\_Prepare

 | 

Tss2\_Sys\_DictionaryAttackParameters\_Complete

 | 

Tss2\_Sys\_DictionaryAttackParameters

 |
| 

Tss2\_Sys\_ContextSave\_Prepare

 | 

Tss2\_Sys\_ContextSave\_Complete

 | 

Tss2\_Sys\_ContextSave

 |
| 

Tss2\_Sys\_ContextLoad\_Prepare

 | 

Tss2\_Sys\_ContextLoad\_Complete

 | 

Tss2\_Sys\_ContextLoad

 |
| 

Tss2\_Sys\_FlushContext\_Prepare

 | 

Tss2\_Sys\_FlushContext\_Complete

 | 

Tss2\_Sys\_FlushContext

 |
| 

Tss2\_Sys\_EvictControl\_Prepare

 | 

Tss2\_Sys\_EvictControl\_Complete

 | 

Tss2\_Sys\_EvictControl

 |
| 

Tss2\_Sys\_GetCapability\_Prepare

 | 

Tss2\_Sys\_GetCapability\_Complete

 | 

Tss2\_Sys\_GetCapability

 |
| 

Tss2\_Sys\_TestParms\_Prepare

 | 

Tss2\_Sys\_TestParms\_Complete

 | 

Tss2\_Sys\_TestParms

 |
| 

Tss2\_Sys\_NV\_DefineSpace\_Prepare

 | 

Tss2\_Sys\_NV\_DefineSpace\_Complete

 | 

Tss2\_Sys\_NV\_DefineSpace

 |
| 

Tss2\_Sys\_NV\_UndefineSpace\_Prepare

 | 

Tss2\_Sys\_NV\_UndefineSpace\_Complete

 | 

Tss2\_Sys\_NV\_UndefineSpace

 |
| 

Tss2\_Sys\_NV\_ReadPublic\_Prepare

 | 

Tss2\_Sys\_NV\_ReadPublic\_Complete

 | 

Tss2\_Sys\_NV\_ReadPublic

 |
| 

Tss2\_Sys\_NV\_Write\_Prepare

 | 

Tss2\_Sys\_NV\_Write\_Complete

 | 

Tss2\_Sys\_NV\_Write

 |
| 

Tss2\_Sys\_NV\_Increment\_Prepare

 | 

Tss2\_Sys\_NV\_Increment\_Complete

 | 

Tss2\_Sys\_NV\_Increment

 |
| 

Tss2\_Sys\_NV\_Extend\_Prepare

 | 

Tss2\_Sys\_NV\_Extend\_Complete

 | 

Tss2\_Sys\_NV\_Extend

 |
| 

Tss2\_Sys\_NV\_SetBits\_Prepare

 | 

Tss2\_Sys\_NV\_SetBits\_Complete

 | 

Tss2\_Sys\_NV\_SetBits

 |
| 

Tss2\_Sys\_NV\_WriteLock\_Prepare

 | 

Tss2\_Sys\_NV\_WriteLock\_Complete

 | 

Tss2\_Sys\_NV\_WriteLock

 |
| 

Tss2\_Sys\_NV\_GlobalWriteLock\_Prepare

 | 

Tss2\_Sys\_NV\_GlobalWriteLock\_Complete

 | 

Tss2\_Sys\_NV\_GlobalWriteLock

 |
| 

Tss2\_Sys\_NV\_Read\_Prepare

 | 

Tss2\_Sys\_NV\_Read\_Complete

 | 

Tss2\_Sys\_NV\_Read

 |
| 

Tss2\_Sys\_NV\_ReadLock\_Prepare

 | 

Tss2\_Sys\_NV\_ReadLock\_Complete

 | 

Tss2\_Sys\_NV\_ReadLock

 |
| 

Tss2\_Sys\_NV\_ChangeAuth\_Prepare

 | 

Tss2\_Sys\_NV\_ChangeAuth\_Complete

 | 

Tss2\_Sys\_NV\_ChangeAuth

 |

#### List of Marshalling and Unmarshalling APIs Supported by HiTSS

| 
**Marshalling API**

 | 

**Unmarshalling API**

 |
| :-- | :-- |
| 

Tss2\_MU\_INT8\_Marshal

 | 

Tss2\_MU\_INT8\_Unmarshal

 |
| 

Tss2\_MU\_UINT8\_Marshal

 | 

Tss2\_MU\_UINT8\_Unmarshal

 |
| 

Tss2\_MU\_INT16\_Marshal

 | 

Tss2\_MU\_INT16\_Unmarshal

 |
| 

Tss2\_MU\_UINT16\_Marshal

 | 

Tss2\_MU\_UINT16\_Unmarshal

 |
| 

Tss2\_MU\_INT32\_Marshal

 | 

Tss2\_MU\_INT32\_Unmarshal

 |
| 

Tss2\_MU\_UINT32\_Marshal

 | 

Tss2\_MU\_UINT32\_Unmarshal

 |
| 

Tss2\_MU\_INT64\_Marshal

 | 

Tss2\_MU\_INT64\_Unmarshal

 |
| 

Tss2\_MU\_UINT64\_Marshal

 | 

Tss2\_MU\_UINT64\_Unmarshal

 |
| 

Tss2\_MU\_BYTE\_Marshal

 | 

Tss2\_MU\_BYTE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_ALGORITHM\_ID\_Marshal

 | 

Tss2\_MU\_TPM2\_ALGORITHM\_ID\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_MODIFIER\_INDICATOR\_Marshal

 | 

Tss2\_MU\_TPM2\_MODIFIER\_INDICATOR\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_AUTHORIZATION\_SIZE\_Marshal

 | 

Tss2\_MU\_TPM2\_AUTHORIZATION\_SIZE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_PARAMETER\_SIZE\_Marshal

 | 

Tss2\_MU\_TPM2\_PARAMETER\_SIZE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_KEY\_SIZE\_Marshal

 | 

Tss2\_MU\_TPM2\_KEY\_SIZE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPM2\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_SPEC\_Marshal

 | 

Tss2\_MU\_TPM2\_SPEC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_GENERATED\_Marshal

 | 

Tss2\_MU\_TPM2\_GENERATED\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_ALG\_ID\_Marshal

 | 

Tss2\_MU\_TPM2\_ALG\_ID\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_ECC\_CURVE\_Marshal

 | 

Tss2\_MU\_TPM2\_ECC\_CURVE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_CC\_Marshal

 | 

Tss2\_MU\_TPM2\_CC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_RC\_Marshal

 | 

Tss2\_MU\_TPM2\_RC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_CLOCK\_ADJUST\_Marshal

 | 

Tss2\_MU\_TPM2\_CLOCK\_ADJUST\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_EO\_Marshal

 | 

Tss2\_MU\_TPM2\_EO\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_ST\_Marshal

 | 

Tss2\_MU\_TPM2\_ST\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_SU\_Marshal

 | 

Tss2\_MU\_TPM2\_SU\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_SE\_Marshal

 | 

Tss2\_MU\_TPM2\_SE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_CAP\_Marshal

 | 

Tss2\_MU\_TPM2\_CAP\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_PT\_Marshal

 | 

Tss2\_MU\_TPM2\_PT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_PT\_PCR\_Marshal

 | 

Tss2\_MU\_TPM2\_PT\_PCR\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_PS\_Marshal

 | 

Tss2\_MU\_TPM2\_PS\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_HANDLE\_Marshal

 | 

Tss2\_MU\_TPM2\_HANDLE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_HT\_Marshal

 | 

Tss2\_MU\_TPM2\_HT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_RH\_Marshal

 | 

Tss2\_MU\_TPM2\_RH\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_HC\_Marshal

 | 

Tss2\_MU\_TPM2\_HC\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_ALGORITHM\_Marshal

 | 

Tss2\_MU\_TPMA\_ALGORITHM\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPMA\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_SESSION\_Marshal

 | 

Tss2\_MU\_TPMA\_SESSION\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_LOCALITY\_Marshal

 | 

Tss2\_MU\_TPMA\_LOCALITY\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_PERMANENT\_Marshal

 | 

Tss2\_MU\_TPMA\_PERMANENT\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_STARTUP\_CLEAR\_Marshal

 | 

Tss2\_MU\_TPMA\_STARTUP\_CLEAR\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_MEMORY\_Marshal

 | 

Tss2\_MU\_TPMA\_MEMORY\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_CC\_Marshal

 | 

Tss2\_MU\_TPMA\_CC\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_MODES\_Marshal

 | 

Tss2\_MU\_TPMA\_MODES\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_X509\_KEY\_USAGE\_Marshal

 | 

Tss2\_MU\_TPMA\_X509\_KEY\_USAGE\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_YES\_NO\_Marshal

 | 

Tss2\_MU\_TPMI\_YES\_NO\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_PARENT\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_PARENT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_PERSISTENT\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_PERSISTENT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_ENTITY\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_ENTITY\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_PCR\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_PCR\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_SH\_AUTH\_SESSION\_Marshal

 | 

Tss2\_MU\_TPMI\_SH\_AUTH\_SESSION\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_SH\_HMAC\_Marshal

 | 

Tss2\_MU\_TPMI\_SH\_HMAC\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_SH\_POLICY\_Marshal

 | 

Tss2\_MU\_TPMI\_SH\_POLICY\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_CONTEXT\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_CONTEXT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_DH\_SAVED\_Marshal

 | 

Tss2\_MU\_TPMI\_DH\_SAVED\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_ENABLES\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_ENABLES\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_AUTH\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_AUTH\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_POLICY\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_HIERARCHY\_POLICY\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_PLATFORM\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_PLATFORM\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_OWNER\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_OWNER\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_ENDORSEMENT\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_ENDORSEMENT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_PROVISION\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_PROVISION\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_CLEAR\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_CLEAR\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_NV\_AUTH\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_NV\_AUTH\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_LOCKOUT\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_LOCKOUT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_NV\_INDEX\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_NV\_INDEX\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_AC\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_AC\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RH\_ACT\_Marshal

 | 

Tss2\_MU\_TPMI\_RH\_ACT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_HASH\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_HASH\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_ASYM\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_ASYM\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_SYM\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_SYM\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_SYM\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_SYM\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_SYM\_MODE\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_SYM\_MODE\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_KDF\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_KDF\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_SIG\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_SIG\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ECC\_KEY\_EXCHANGE\_Marshal

 | 

Tss2\_MU\_TPMI\_ECC\_KEY\_EXCHANGE\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ST\_COMMAND\_TAG\_Marshal

 | 

Tss2\_MU\_TPMI\_ST\_COMMAND\_TAG\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_MAC\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_MAC\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_CIPHER\_MODE\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_CIPHER\_MODE\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_EMPTY\_Marshal

 | 

Tss2\_MU\_TPMS\_EMPTY\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ALGORITHM\_DESCRIPTION\_Marshal

 | 

Tss2\_MU\_TPMS\_ALGORITHM\_DESCRIPTION\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_HA\_Marshal

 | 

Tss2\_MU\_TPMU\_HA\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_HA\_Marshal

 | 

Tss2\_MU\_TPMT\_HA\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_DIGEST\_Marshal

 | 

Tss2\_MU\_TPM2B\_DIGEST\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_DATA\_Marshal

 | 

Tss2\_MU\_TPM2B\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_NONCE\_Marshal

 | 

Tss2\_MU\_TPM2B\_NONCE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_AUTH\_Marshal

 | 

Tss2\_MU\_TPM2B\_AUTH\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_OPERAND\_Marshal

 | 

Tss2\_MU\_TPM2B\_OPERAND\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_EVENT\_Marshal

 | 

Tss2\_MU\_TPM2B\_EVENT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_MAX\_BUFFER\_Marshal

 | 

Tss2\_MU\_TPM2B\_MAX\_BUFFER\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_MAX\_NV\_BUFFER\_Marshal

 | 

Tss2\_MU\_TPM2B\_MAX\_NV\_BUFFER\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_TIMEOUT\_Marshal

 | 

Tss2\_MU\_TPM2B\_TIMEOUT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_IV\_Marshal

 | 

Tss2\_MU\_TPM2B\_IV\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_NAME\_Marshal

 | 

Tss2\_MU\_TPMU\_NAME\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_NAME\_Marshal

 | 

Tss2\_MU\_TPM2B\_NAME\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_PCR\_SELECT\_Marshal

 | 

Tss2\_MU\_TPMS\_PCR\_SELECT\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_PCR\_SELECTION\_Marshal

 | 

Tss2\_MU\_TPMS\_PCR\_SELECTION\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_TK\_CREATION\_Marshal

 | 

Tss2\_MU\_TPMT\_TK\_CREATION\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_TK\_VERIFIED\_Marshal

 | 

Tss2\_MU\_TPMT\_TK\_VERIFIED\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_TK\_AUTH\_Marshal

 | 

Tss2\_MU\_TPMT\_TK\_AUTH\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_TK\_HASHCHECK\_Marshal

 | 

Tss2\_MU\_TPMT\_TK\_HASHCHECK\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ALG\_PROPERTY\_Marshal

 | 

Tss2\_MU\_TPMS\_ALG\_PROPERTY\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_TAGGED\_PROPERTY\_Marshal

 | 

Tss2\_MU\_TPMS\_TAGGED\_PROPERTY\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_TAGGED\_PCR\_SELECT\_Marshal

 | 

Tss2\_MU\_TPMS\_TAGGED\_PCR\_SELECT\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_TAGGED\_POLICY\_Marshal

 | 

Tss2\_MU\_TPMS\_TAGGED\_POLICY\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_CC\_Marshal

 | 

Tss2\_MU\_TPML\_CC\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_CCA\_Marshal

 | 

Tss2\_MU\_TPML\_CCA\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_ALG\_Marshal

 | 

Tss2\_MU\_TPML\_ALG\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_HANDLE\_Marshal

 | 

Tss2\_MU\_TPML\_HANDLE\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_DIGEST\_Marshal

 | 

Tss2\_MU\_TPML\_DIGEST\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_DIGEST\_VALUES\_Marshal

 | 

Tss2\_MU\_TPML\_DIGEST\_VALUES\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_PCR\_SELECTION\_Marshal

 | 

Tss2\_MU\_TPML\_PCR\_SELECTION\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_ALG\_PROPERTY\_Marshal

 | 

Tss2\_MU\_TPML\_ALG\_PROPERTY\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_TAGGED\_TPM\_PROPERTY\_Marshal

 | 

Tss2\_MU\_TPML\_TAGGED\_TPM\_PROPERTY\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_TAGGED\_PCR\_PROPERTY\_Marshal

 | 

Tss2\_MU\_TPML\_TAGGED\_PCR\_PROPERTY\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_ECC\_CURVE\_Marshal

 | 

Tss2\_MU\_TPML\_ECC\_CURVE\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_TAGGED\_POLICY\_Marshal

 | 

Tss2\_MU\_TPML\_TAGGED\_POLICY\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_CAPABILITIES\_Marshal

 | 

Tss2\_MU\_TPMU\_CAPABILITIES\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CAPABILITY\_DATA\_Marshal

 | 

Tss2\_MU\_TPMS\_CAPABILITY\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CLOCK\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_CLOCK\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_TIME\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_TIME\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_TIME\_ATTEST\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_TIME\_ATTEST\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CERTIFY\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_CERTIFY\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_QUOTE\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_QUOTE\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_COMMAND\_AUDIT\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_COMMAND\_AUDIT\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SESSION\_AUDIT\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_SESSION\_AUDIT\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CREATION\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_CREATION\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_NV\_CERTIFY\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_NV\_CERTIFY\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ST\_ATTEST\_Marshal

 | 

Tss2\_MU\_TPMI\_ST\_ATTEST\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_ATTEST\_Marshal

 | 

Tss2\_MU\_TPMU\_ATTEST\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ATTEST\_Marshal

 | 

Tss2\_MU\_TPMS\_ATTEST\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_ATTEST\_Marshal

 | 

Tss2\_MU\_TPM2B\_ATTEST\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_AUTH\_COMMAND\_Marshal

 | 

Tss2\_MU\_TPMS\_AUTH\_COMMAND\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_AUTH\_RESPONSE\_Marshal

 | 

Tss2\_MU\_TPMS\_AUTH\_RESPONSE\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_AES\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMI\_AES\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_SM4\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMI\_SM4\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_CAMELLIA\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMI\_CAMELLIA\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SYM\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMU\_SYM\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SYM\_MODE\_Marshal

 | 

Tss2\_MU\_TPMU\_SYM\_MODE\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_SYM\_DEF\_Marshal

 | 

Tss2\_MU\_TPMT\_SYM\_DEF\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_SYM\_DEF\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPMT\_SYM\_DEF\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_SYM\_KEY\_Marshal

 | 

Tss2\_MU\_TPM2B\_SYM\_KEY\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SYMCIPHER\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMS\_SYMCIPHER\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_LABEL\_Marshal

 | 

Tss2\_MU\_TPM2B\_LABEL\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_DERIVE\_Marshal

 | 

Tss2\_MU\_TPMS\_DERIVE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_DERIVE\_Marshal

 | 

Tss2\_MU\_TPM2B\_DERIVE\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SENSITIVE\_CREATE\_Marshal

 | 

Tss2\_MU\_TPMU\_SENSITIVE\_CREATE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_SENSITIVE\_DATA\_Marshal

 | 

Tss2\_MU\_TPM2B\_SENSITIVE\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SENSITIVE\_CREATE\_Marshal

 | 

Tss2\_MU\_TPMS\_SENSITIVE\_CREATE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_SENSITIVE\_CREATE\_Marshal

 | 

Tss2\_MU\_TPM2B\_SENSITIVE\_CREATE\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_HASH\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_HASH\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_ECDAA\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_ECDAA\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_KEYEDHASH\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_KEYEDHASH\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_HMAC\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_HMAC\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_XOR\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_XOR\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SCHEME\_KEYEDHASH\_Marshal

 | 

Tss2\_MU\_TPMU\_SCHEME\_KEYEDHASH\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_KEYEDHASH\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_KEYEDHASH\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSASSA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSASSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSAPSS\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_RSAPSS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDSA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_SM2\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_SM2\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECSCHNORR\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECSCHNORR\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDAA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIG\_SCHEME\_ECDAA\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SIG\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMU\_SIG\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_SIG\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_SIG\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ENC\_SCHEME\_OAEP\_Marshal

 | 

Tss2\_MU\_TPMS\_ENC\_SCHEME\_OAEP\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ENC\_SCHEME\_RSAES\_Marshal

 | 

Tss2\_MU\_TPMS\_ENC\_SCHEME\_RSAES\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECDH\_Marshal

 | 

Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECDH\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECMQV\_Marshal

 | 

Tss2\_MU\_TPMS\_KEY\_SCHEME\_ECMQV\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_MGF1\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_MGF1\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_56A\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_56A\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_KDF2\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_KDF2\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_108\_Marshal

 | 

Tss2\_MU\_TPMS\_SCHEME\_KDF1\_SP800\_108\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_KDF\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMU\_KDF\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_KDF\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_KDF\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_ASYM\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_ASYM\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_ASYM\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMU\_ASYM\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_ASYM\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_ASYM\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_RSA\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_RSA\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_RSA\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_RSA\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_RSA\_DECRYPT\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_RSA\_DECRYPT\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_RSA\_DECRYPT\_Marshal

 | 

Tss2\_MU\_TPMT\_RSA\_DECRYPT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_PUBLIC\_KEY\_RSA\_Marshal

 | 

Tss2\_MU\_TPM2B\_PUBLIC\_KEY\_RSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_RSA\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMI\_RSA\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_PRIVATE\_KEY\_RSA\_Marshal

 | 

Tss2\_MU\_TPM2B\_PRIVATE\_KEY\_RSA\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_ECC\_PARAMETER\_Marshal

 | 

Tss2\_MU\_TPM2B\_ECC\_PARAMETER\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ECC\_POINT\_Marshal

 | 

Tss2\_MU\_TPMS\_ECC\_POINT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_ECC\_POINT\_Marshal

 | 

Tss2\_MU\_TPM2B\_ECC\_POINT\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_ECC\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_ECC\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ECC\_CURVE\_Marshal

 | 

Tss2\_MU\_TPMI\_ECC\_CURVE\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_ECC\_SCHEME\_Marshal

 | 

Tss2\_MU\_TPMT\_ECC\_SCHEME\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ALGORITHM\_DETAIL\_ECC\_Marshal

 | 

Tss2\_MU\_TPMS\_ALGORITHM\_DETAIL\_ECC\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_RSA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_RSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_RSASSA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_RSASSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_RSAPSS\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_RSAPSS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_ECC\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_ECC\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_ECDSA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_ECDSA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_ECDAA\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_ECDAA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_SM2\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_SM2\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_SIGNATURE\_ECSCHNORR\_Marshal

 | 

Tss2\_MU\_TPMS\_SIGNATURE\_ECSCHNORR\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SIGNATURE\_Marshal

 | 

Tss2\_MU\_TPMU\_SIGNATURE\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_SIGNATURE\_Marshal

 | 

Tss2\_MU\_TPMT\_SIGNATURE\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_ENCRYPTED\_SECRET\_Marshal

 | 

Tss2\_MU\_TPMU\_ENCRYPTED\_SECRET\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_ENCRYPTED\_SECRET\_Marshal

 | 

Tss2\_MU\_TPM2B\_ENCRYPTED\_SECRET\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_ALG\_PUBLIC\_Marshal

 | 

Tss2\_MU\_TPMI\_ALG\_PUBLIC\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_PUBLIC\_ID\_Marshal

 | 

Tss2\_MU\_TPMU\_PUBLIC\_ID\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_KEYEDHASH\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMS\_KEYEDHASH\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ASYM\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMS\_ASYM\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_RSA\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMS\_RSA\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ECC\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMS\_ECC\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_PUBLIC\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMU\_PUBLIC\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_PUBLIC\_PARMS\_Marshal

 | 

Tss2\_MU\_TPMT\_PUBLIC\_PARMS\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_PUBLIC\_Marshal

 | 

Tss2\_MU\_TPMT\_PUBLIC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_PUBLIC\_Marshal

 | 

Tss2\_MU\_TPM2B\_PUBLIC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_TEMPLATE\_Marshal

 | 

Tss2\_MU\_TPM2B\_TEMPLATE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_PRIVATE\_VENDOR\_SPECIFIC\_Marshal

 | 

Tss2\_MU\_TPM2B\_PRIVATE\_VENDOR\_SPECIFIC\_Unmarshal

 |
| 

Tss2\_MU\_TPMU\_SENSITIVE\_COMPOSITE\_Marshal

 | 

Tss2\_MU\_TPMU\_SENSITIVE\_COMPOSITE\_Unmarshal

 |
| 

Tss2\_MU\_TPMT\_SENSITIVE\_Marshal

 | 

Tss2\_MU\_TPMT\_SENSITIVE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_SENSITIVE\_Marshal

 | 

Tss2\_MU\_TPM2B\_SENSITIVE\_Unmarshal

 |
| 

Tss2\_MU\_\_PRIVATE\_Marshal

 | 

Tss2\_MU\_\_PRIVATE\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_PRIVATE\_Marshal

 | 

Tss2\_MU\_TPM2B\_PRIVATE\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ID\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPMS\_ID\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_ID\_OBJECT\_Marshal

 | 

Tss2\_MU\_TPM2B\_ID\_OBJECT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_NV\_INDEX\_Marshal

 | 

Tss2\_MU\_TPM2\_NV\_INDEX\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_NT\_Marshal

 | 

Tss2\_MU\_TPM2\_NT\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_NV\_PIN\_COUNTER\_PARAMETERS\_Marshal

 | 

Tss2\_MU\_TPMS\_NV\_PIN\_COUNTER\_PARAMETERS\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_NV\_Marshal

 | 

Tss2\_MU\_TPMA\_NV\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_NV\_PUBLIC\_Marshal

 | 

Tss2\_MU\_TPMS\_NV\_PUBLIC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_NV\_PUBLIC\_Marshal

 | 

Tss2\_MU\_TPM2B\_NV\_PUBLIC\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_CONTEXT\_SENSITIVE\_Marshal

 | 

Tss2\_MU\_TPM2B\_CONTEXT\_SENSITIVE\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CONTEXT\_DATA\_Marshal

 | 

Tss2\_MU\_TPMS\_CONTEXT\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_CONTEXT\_DATA\_Marshal

 | 

Tss2\_MU\_TPM2B\_CONTEXT\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CONTEXT\_Marshal

 | 

Tss2\_MU\_TPMS\_CONTEXT\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_CREATION\_DATA\_Marshal

 | 

Tss2\_MU\_TPMS\_CREATION\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPM2B\_CREATION\_DATA\_Marshal

 | 

Tss2\_MU\_TPM2B\_CREATION\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_ACT\_DATA\_Marshal

 | 

Tss2\_MU\_TPMS\_ACT\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPMA\_ACT\_Marshal

 | 

Tss2\_MU\_TPMA\_ACT\_Unmarshal

 |
| 

Tss2\_MU\_TPM2\_AT\_Marshal

 | 

Tss2\_MU\_TPM2\_AT\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_NV\_DIGEST\_CERTIFY\_INFO\_Marshal

 | 

Tss2\_MU\_TPMS\_NV\_DIGEST\_CERTIFY\_INFO\_Unmarshal

 |
| 

Tss2\_MU\_TPMI\_TDES\_KEY\_BITS\_Marshal

 | 

Tss2\_MU\_TPMI\_TDES\_KEY\_BITS\_Unmarshal

 |
| 

Tss2\_MU\_TPMS\_AC\_OUTPUT\_Marshal

 | 

Tss2\_MU\_TPMS\_AC\_OUTPUT\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_ACT\_DATA\_Marshal

 | 

Tss2\_MU\_TPML\_ACT\_DATA\_Unmarshal

 |
| 

Tss2\_MU\_TPML\_AC\_CAPABILITIES\_Marshal

 | 

Tss2\_MU\_TPML\_AC\_CAPABILITIES\_Unmarshal

 |

#### List of Command Transmission APIs Supported by HiTSS

-   Tss2\_TctiLdr\_Initialize
-   Tss2\_TctiLdr\_Initialize\_Ex
-   Tss2\_TctiLdr\_Finalize
-   Tss2\_TctiLdr\_GetInfo
-   Tss2\_TctiLdr\_FreeInfo
