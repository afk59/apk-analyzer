# How do I resolve the "generate SignerBlock failed" error?

**Symptom**

The error "generate SignerBlock failed" is reported during compilation and build.

hap-sign-tool: error: {errorcode:0,message:generate SignerBlock failed}

**Possible Causes**

The public and private keys used for signing do not match. In this case, if you sign with the private key, verification with the public key will fail. You must ensure that private key (**keyalias**) and public key (**appCertPath**) are used in pairs.

**Scenarios**

1.  When signing materials are generated locally, if the correct CSR corresponding to **keyalias** is not exported, the public key generated from the certificate will not match the private key associated with **keyalias**.
2.  The **keyalias** or **appCertPath** settings might be incorrect.

**Solution**

Select the correct **keyalias** and **appCertPath** settings.
