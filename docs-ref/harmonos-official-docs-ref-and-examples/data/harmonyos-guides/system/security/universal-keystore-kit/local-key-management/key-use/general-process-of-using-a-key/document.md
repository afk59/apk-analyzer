# General Process of Using a Key

The key generated or imported can be used to perform the following operations to ensure data confidentiality and integrity:

-   [Encryption and decryption](../encryption-and-decryption/encryption-and-decryption-overview-and-algorithm-specifications/document.md)
    
-   [Signing and signature verification](../signing-and-signature-verification/signing-and-signature-verification-overview-and-algorithm-specifications/document.md)
    
-   [Key agreement](../key-agreement/key-agreement-overview-and-algorithm-specifications/document.md)
    
-   [Key derivation](../key-derivation/key-derivation-overview-and-algorithm-specifications/document.md)
    

This section provides examples of the preceding common key operations. Secondary access control is not configured in the following examples. For details about how to configure key access control, see [HUKS Access Control Overview](../access-control/huks-access-control-overview/document.md).

#### General Development Process

HUKS operates data based on a key session. The general process is as follows:

1.  (Mandatory) Initialize a key session using [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9).
    
    You need to pass in the key alias and key operation parameters. A session handle will be returned after the initialization. The key operation parameters must contain the parameters required by the cipher algorithm, including the cipher algorithm, key size, key purpose, working mode, padding mode, hash mode, IV, NONCE, and AAD.
    
2.  (Optional) Process data by segment using [updateSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksupdatesession9).
    
    Process data by segment as required by the cryptographic algorithm in use or if the data to be processed exceeds 100 KB in size. Otherwise, skip this step.
    
3.  (Mandatory) Finish the key session using [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9).
    
    If the data is processes by segment, \[huks.finishSession()\] processes the last data segment and finishes the key session.
    

You can use [abortSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksabortsession9) to abort the session if an error occurs in any of the preceding steps or the current key operation data is not required.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/fkyS4WSoQ4Ors_ykpoVdlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3AE65C54B233D007FB294EE3B16E6E9CA4005136BC0DAAE68C9C13BA53400C9)

-   For devices with small memory, you are advised to split data based on the storage capability of the device and cyclically call [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) and [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9).
-   The session duration refers to the interval between the [initSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksinitsession9) and [finishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksfinishsession9) calls. When the system memory is low, the system clears the timeout sessions. Therefore, the session duration should not be too long (not more than 1 minute).
