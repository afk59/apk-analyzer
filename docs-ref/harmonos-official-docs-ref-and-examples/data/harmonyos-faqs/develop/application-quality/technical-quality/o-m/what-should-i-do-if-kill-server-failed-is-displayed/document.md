# What should I do if "Kill server failed" is displayed?

**Symptom**

After the **hdc kill** command is executed, the message "Kill server failed: operation not permitted" is displayed.

**Possible Causes**

The hdc server is started by another program in the background with a higher permission than that of the **hdc kill** command.

**Solution**

1.  Windows: Choose **Task Manager** > **Details** , and terminate **hdc.exe**.
2.  Run the **ps -ef |grep hdc** command to find the process ID of the background program that executes hdc, and then run the **sudo kill -9** _process ID_ command to kill the process.
