# What should I do if "Failed to request the remote SDK" is reported during pipeline build?

**Symptom**

An error occurs during SDK installation.

./sdkmgr install xxx --sdk-directory="/opt/HarmonyOS/SDK" Failed to request url https://devecostudio-dre.op.hicloud.com/sdkmanager/v7/hos/getSdkList \[ \]0% Failed to request the remote SDK. This may be caused by a network error. If your environment needs a proxy to access the Internet, check whether the --proxy and --no-proxy parameters are correctly set. If they are not set, check whether the http\_proxy/HTTP\_PROXY and no\_proxy/NO\_PROXY environment variables are correctly set. root@luckyclientbuild01-test3-ucscompute16-cloudvsp:~/command-line-tools/sdkmanager/bin#

**Solution**

During compilation, you are advised to perform the clean operation first, preventing the previous build product from affecting the new compilation.
