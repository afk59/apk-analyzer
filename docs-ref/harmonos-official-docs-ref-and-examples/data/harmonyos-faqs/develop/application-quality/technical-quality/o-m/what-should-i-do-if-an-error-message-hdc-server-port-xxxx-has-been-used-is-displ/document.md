# What should I do if an error message "hdc server port XXXX has been used" is displayed during hdc debugging and switching ports has no effect?

**Symptom**

An error message "hdc server port XXXX has been used" is displayed during hdc device debugging, and the error persists after the port is manually switched.

**Possible Causes**

1.  The port is occupied.
2.  The port is blocked.

**Solution**

1.  If the port is occupied, perform the following methods:
    -   Change the port. Set the environment variable **OHOS\_HDC\_SERVER\_PORT** to configure an available port, for example, 18710. After that, restart the command line or the software (such as the emulator, DevEco Studio, DevEco series, and xdevice) that uses the hdc.
    -   Locate the software that occupies the port and release the port.
        
        Windows:
        
        Query the port.
        $ netstat -ano | findstr :{Port number}
        End the service.
        $ taskkill /PID {PID} /F
        Note: Replace the port number and PID with the actual ones.
        
        Linux/macOS:
        
        Query the port.
        $ lsof -i :{Port number}
        $ netstat -tuln | grep :{Port number}
        End the service.
        $ kill -9 {PID}
        Note: Replace the port number and PID with the actual ones.
        
    -   If the occupied port cannot be queried on Windows, perform the following operations:
        
        View the dynamic port range.
        $ netsh int ipv4 show dynamicport tcp
        View the exception port range.
        $ taskkill /PID {PID} /F
        Note: Replace the port number and PID with the actual ones.
        
        If the query result shows that the occupied port is an exception port, perform the following steps or manually restart the Hyper-V service in the task manager:
        
        Disable Hyper-V \[Required to restart the computer\]
        $ dism.exe /Online /Disable-Feature:Microsoft-Hyper-V
        Enable Hyper-V \[Required to restart the computer\]
        $ dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
        
2.  If the port is blocked, check if any firewall or interception-related software is enabled locally. If so, adjust the relevant security group settings or close the software and try again.
