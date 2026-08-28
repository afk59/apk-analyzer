# What should I do if the hdc command cannot be executed when Linux 18.04 is installed for the first time?

**Symptom**

The Command Line Tools for Linux is downloaded and installed for the first time. An error message is displayed when the **hdc -v** command is executed in the **sdk/default/openharmony/toolchains** directory:

Command 'hdc' not found, did you mean:
 command 'gdc' from deb gdc
 command 'hpc' from deb ghc
 command 'htc' from deb httptunnel
 command 'hsc' from deb hsc
 command 'hd' from deb bsdmainutils
 command 'hc' from deb httpcode
 command 'hyc' from deb python-hy
 command 'hyc' from deb python3-hy
 command 'hdp' from deb hdf4-tools
 command 'dc' from deb dc
 command 'sdc' from deb hpsockd
 command 'hcc' from deb lam4-dev
 command 'hcc' from deb uhexen2
 command 'hcd' from deb hfsutils
 command 'tdc' from deb tdc
Try: sudo apt install <deb name>

**Possible Causes**

The message indicates that the hdc command executed on the terminal is not found. By default, the system searches for the path of the executable program from the environment variable PATH. The environment variable is not configured during the first installation. As a result, an error occurs.

**Solution**

-   Run the hdc command using an absolute path.
    
    $ /path/to/hdc -v
    Note: Replace the path with the actual path in the installation directory.
    
-   Modify the environment variable and add the directory where the hdc command is located. For details, see hdc [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup).
-   Save the hdc command to the **/usr/bin** directory in soft link mode.
    
    $ ln -s /path/to/hdc /usr/bin/hdc
    Note: Replace the path with the actual path in the installation directory.
