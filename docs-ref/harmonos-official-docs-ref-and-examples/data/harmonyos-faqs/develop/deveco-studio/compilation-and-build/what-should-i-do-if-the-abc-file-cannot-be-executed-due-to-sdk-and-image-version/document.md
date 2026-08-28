# What should I do if the .abc file cannot be executed due to SDK and image version mismatch?

**Symptom**

When the SDK version does not match the image version, the application may exit unexpectedly and report a jscrash error, and related logs are recorded in the hilog.

**Solution**

Use a matching SDK and image version.

To view the SDK version:

Obtain the SDK path from the **local.properties** file in the project directory and run the **{hwsdk.dir}/openharmony/11/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version** command to check whether the SDK version matches the image version.
