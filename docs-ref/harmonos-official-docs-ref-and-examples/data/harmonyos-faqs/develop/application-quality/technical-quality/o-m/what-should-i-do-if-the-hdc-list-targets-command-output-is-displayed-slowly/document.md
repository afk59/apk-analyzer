# What should I do if the hdc list targets command output is displayed slowly?

**Symptom**

The **hdc list targets** command output is displayed slowly.

**Possible Causes**

The USB is faulty.

**Solution**

Troubleshooting methods and solutions for USB faults.

| 
No.

 | 

Troubleshooting Method

 | 

Solution

 |
| :-- | :-- | :-- |
| 

1

 | 

Run the **hdc -l5 list targets** command to query the log details of the slow command output.

 | 

View the log details of the slow command output and provide them to the hdc developers.

 |
| 

2

 | 

On Windows, go to Device Manager and check whether there is a USB device with an exclamation mark (!).

 | 

Uninstall the USB device with an exclamation mark (!) in Device Manager.

 |
| 

3

 | 

On Windows, open the Task Manager and check whether the hdc.exe startup user is the same as the actual user.

 | 

End the process and restart the hdc.

 |
| 

4

 | 

On Unix, run the **ps -u |grep hdc** command to query the startup user of hdc.exe.

 | 

If the startup user is different from the current user, end the process and restart the hdc.

 |

On Linux, you can run the **time lsusb** command to troubleshoot whether USB blocking is causing slow display of list targets output. If the execution time of the **time lsusb** command is longer than 0.5s, the USB may be faulty. In this case, run the **dmesg |grep -i USB** command to query the USB fault type. The known fault types and solutions are as follows:

| 
No.

 | 

Fault Type

 | 

Solution

 |
| :-- | :-- | :-- |
| 

1

 | 

maybe the cable is bad

 | 

Replace the USB data cable. If the USB 2.0 data cable is used, replace it with the USB 3.0 data cable.

 |
