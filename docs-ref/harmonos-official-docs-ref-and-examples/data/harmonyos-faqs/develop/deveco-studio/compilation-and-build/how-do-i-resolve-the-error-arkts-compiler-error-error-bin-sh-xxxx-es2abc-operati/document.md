# How do I resolve the "ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted" error?

**Symptom**

The error message "ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted" is displayed during compilation.

**Possible Causes**

After the SDK is obtained, macOS uses security measures that append a quarantine flag, **com.apple.quarantine**, to executable files downloaded from the Internet. This attribute prevents the execution of these files.

**Solution**

Execute the following command to remove the **com.apple.quarantine** flag from the executable files.

xattr -d com.apple.quarantine /path/to/es2abc
