# What should I do if "too many open files" is reported during compilation?

**Symptom**

The following error is reported during the compilation of the macOS project:

hvigor ERROR: EMFILE: too many open files, open '/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/kit\_configs/@kit.ArkTS.json'

**Solution**

The maximum number of connections depends on the maximum number of opened files (file descriptors) supported by the system. In Linux, the default range of dynamic port numbers is 32768 to 65535. Therefore, when the client connects to the same IP address and port number, a maximum of 32768 connections can be established. On macOS, a maximum of 16384 connections can be established by default. To adjust these restrictions, run the following commands in the DevEco Studio terminal (replace the numbers as required):

sysctl kern.maxfiles
sudo sysctl -w kern.maxfiles=20480
sudo sysctl -w kern.maxfilesperproc=18000
hvigorw --stop-daemon-all
