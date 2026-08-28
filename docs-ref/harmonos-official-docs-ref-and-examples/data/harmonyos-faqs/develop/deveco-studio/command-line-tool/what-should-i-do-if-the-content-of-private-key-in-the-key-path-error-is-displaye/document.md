# What should I do if "the content of private key in the key\_path error" is displayed when the ohpm publish command is executed in Git Bash?

**Symptom**

When the **ohpm publish** command is executed in the local Git Bash environment, the error "the content of private key in the key path error" keeps appearing. This issue does not occur in DevEco Studio, where it prompts for a password. The current version of ohpm is 1.5, and the environment variables are configured.

**Possible Causes**

When the **ohpm publish** command is executed with SSH certificate password authentication, the program needs to read the password entered by the user through a TTY stream. If the installed version of Git is too old, the Git Bash it provides can cause the TTY stream to be lost, resulting in this error.

**Solution**

1\. Download and install the latest version of Git from the official Git website. Use the Git Bash terminal provided with this version.

2\. In the current Git installation directory, go to the **etc** directory, create a **git-bash.config** file, and add the following line: **MSYS=enable\_pcon**. Then, reopen the Git Bash terminal and run the **ohpm publish** command again.
