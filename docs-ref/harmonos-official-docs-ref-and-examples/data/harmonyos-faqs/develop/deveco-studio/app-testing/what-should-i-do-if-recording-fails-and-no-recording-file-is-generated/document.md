# What should I do if recording fails and no recording file is generated?

**Possible Causes**

The **uitest** capability on which the recording capability depends is occupied by another program.

**Solution**

Restart the mobile phone or run the following command to kill the service:

hdc shell killall -9 uitest
