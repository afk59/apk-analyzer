# What should I do if the error message "command not found: hdc" is displayed after running the hdc list targets command in the toolchains directory of the SDK?

**Symptom**

After DevEco Studio is installed on the Linux or macOS, the message **command not found:hdc** is displayed when the hdc command is run in the **toolchains** subdirectory in the installation directory.

**Possible Causes**

1.  The **hdc** executable file in the **toolchains** directory is manually replaced. The replaced file does not have the execute permission.
2.  When executing a shell (such as bash or zsh) command, it does not by default search for executable files in the current directory (./).

**Solution**

1.  The hdc file must have the execute permission to be executed by the system.
    
    -   Check method: Run the **ls -l** command to check the file details.
    
    $ cd {SDK PATH}/sdk/default/openharmony/toolchains
    $ ls -l hdc
    
    Check the first column (permission bits) in the command output. If there is no "x" at the beginning (which stands for "execute"), it means that the file does not have the execute permission. An example with the execute permission is **\-rwxr-xr-x**, and an example without the execute permission is **\-rw-r--r--**.
    
    -   Solution: Run the **chmod** command to grant the execute permission for the hdc file.
    
    $ chmod +x hdc
    
2.  By default, the PATH environment variable does not add the current directory (./) to the list. You need to manually add the current directory.
    -   Explicitly specify the current directory and add **./** before running the hdc command.
    -   Add the absolute path of the directory where the hdc file is located to the PATH environment variable. For details, see hdc [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup).
