# How do I resolve the "java.io.IOException: DerValue.getOID, not an OID 49" error?

**Symptom**

The error "java.io.IOException: DerValue.getOID, not an OID 49" is reported during compilation and build.

hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools

**Possible Causes**

The certificate file fails to be parsed, because the OID is not found.

**Scenarios**

1.  The certificate has been altered.
2.  The **appCertPath** parameter is pointing to a non-certificate file.

**Solution**

Check whether the certificate file is correct.
