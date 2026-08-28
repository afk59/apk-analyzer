# 401 Parameter Check Failure

**Symptom**

Error code 401 is reported upon an API call, indicating that a parameter check failure.

**Possible causes**

1.  A mandatory parameter is not passed.
2.  Incorrect parameter type. (Type Error)
3.  The number of parameters is incorrect. (Argument Count Error)
4.  Null is passed to a parameter that requires a value. (Null Argument Error)
5.  Invalid parameter format. (Format Error)
6.  The parameter value is out of the valid range. (Value Range Error)
7.  The **client\_id** parameter is incorrectly set.
8.  Manual signing is not used.

**Solution**

1.  Ensure that the mandatory parameters are passed, the parameter types are correct, and the parameter values meet the requirements.
2.  Ensure that the **client\_id** parameter in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](../../getting-started/configuring-the-client-id/document.md).
3.  Manually configure signing information. For details, please refer to [Configuring Signing Information and Fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md).
