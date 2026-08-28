# Overview

The digital shield service provides end-to-end security protection for large-amount bank transfers in finance apps through the trusted user interface (TUI). It mainly leverages the following TUI-based core functions:

1.  Data isolation: The input, transmission, and verification of password information are all completed in the trusted execution environment (TEE) security sandbox, which is completely isolated from the rich execution environment (REE) to prevent malicious programs in the REE from stealing the password information.
2.  UI anti-tampering: Key information (such as the password input screen or identity verification prompt) displayed on the TUI is rendered using the TEE graphics channel, preventing attackers from overwriting or modifying the information displayed on the UI through the REE.
3.  Input confidence: Passwords entered by users are captured and encrypted by the TEE process for storage, preventing plaintext passwords from being exposed to the REE memory or peripheral interfaces.

The digital shield service provides the following key functions:

-   Digital shield password management: Creates, changes, and disables digital shield passwords. The TEE-isolated digital keyboard control is used for password input to prevent the password information from being stolen.
-   Password-based authentication of transaction information: In fund transfer scenarios, transaction information undergoes strong authentication based on the digital shield password. The authentication result is then verified using the encrypted signature function provided by Universal Keystore Kit, ensuring transaction integrity and non-repudiation.
-   Biometric feature binding and authentication: Supports binding and authentication of biometric features such as face or fingerprints to enhance transaction security.
-   Backup and restoration of the digital shield signature key: Backs up the digital shield signature key to ensure that the password authentication function can still run properly after an app is uninstalled and then reinstalled, providing persistent storage of keys.

Password data management and storage provided by the digital shield service are described as follows:

-   Storage: Digital shield passwords are persistently stored in the TEE of devices.
-   Data deletion trigger condition: When a user disables the digital shield service, all associated password data and keys are deleted from the device to ensure privacy security.
-   Note: When integrating the digital shield service, you must explicitly inform users about the lifecycle of password data, ensure that users understand the password data management method, and provide the privacy statement to users in your app.
