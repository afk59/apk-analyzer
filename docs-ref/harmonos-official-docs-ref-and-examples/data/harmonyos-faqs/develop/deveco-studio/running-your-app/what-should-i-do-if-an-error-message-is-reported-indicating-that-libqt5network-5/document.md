# What should I do if an error message is reported, indicating that libQt5Network.5.dylib cannot be opened because Apple cannot check whether the VM contains malware when the VM is started?

**Symptom**

After a VM is created according to the guide, the VM cannot be started. In addition, when the VM is started, an error message is reported, indicating that libQt5Network.5.dylib cannot be opened because Apple cannot check whether the VM contains malware. After you repeatedly agree to enable the file in **Settings** > **Privacy**, this issue persists.

**Solution**

You can use **Unzip** to resolve this issue. After the installation of the DevEco Studio, download the mapping emulator mirror and platform. Choose **Tools** > **Unzip** to open the decompression entry provided by the DevEco Studio, select the download path and decompression path of the compressed packages of both emulator mirror and platform, and decompress the packages. After the decompression and installation are complete, start the Emulator.

Workaround: Keep the preceding dialog box open. Go to **System Preferences** > **Security & privacy** \> **General** and select **Open Anyway**. Restart the Emulator and select **Open** in the dialog box.
