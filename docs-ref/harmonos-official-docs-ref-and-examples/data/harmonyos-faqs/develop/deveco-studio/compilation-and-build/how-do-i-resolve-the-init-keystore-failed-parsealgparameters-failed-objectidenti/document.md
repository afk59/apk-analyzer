# How do I resolve the "Init keystore failed: parseAlgParameters failed: ObjectIdentifier()" error?

**Symptom**

The error "Init keystore failed: parseAlgParameters failed: ObjectIdentifier()" is reported during compilation and build.

hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools

**Possible Causes**

The error may occur due to incompatibility resulting from a version mismatch between the JDK used to generate the key pair (.p12) and the JDK used to execute the signing command. This incompatibility can prevent the .p12 file from parsing correctly, leading to signing failures.

**Scenarios**

1.  When DevEco Studio generates a key pair, it uses the pre-installed JDK 17 by default. If a lower version JDK is used for signing locally, an error will occur.
2.  If a key pair is generated locally using a higher version of JDK, and signing is done through DevEco Studio, which uses the pre-installed JDK 17, an error will occur because the pre-installed JDK version is lower than the one used locally.

**Solution**

Check whether DevEco Studio in the local environment uses JDK 17.

Command: **java -version**

Alternatively, use the built-in JDK 17 of DevEco Studio. The path is **${DevEco Studio}/jbr**.
