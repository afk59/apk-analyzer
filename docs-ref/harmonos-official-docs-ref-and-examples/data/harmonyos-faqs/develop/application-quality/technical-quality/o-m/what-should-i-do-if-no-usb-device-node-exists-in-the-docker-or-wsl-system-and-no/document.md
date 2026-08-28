# What should I do if no USB device node exists in the Docker or WSL system and no information is returned after a command is executed in hdc?

**Symptom**

1\. No output is displayed or "Connect server failed." is displayed after a command is executed in hdc?

2\. Check the **hdc.log** and an error message "USB mod ctxUSB is nullptr, recompile please." is displayed.

**Possible Causes**

1\. The Docker does not map the external USB device to the container. As a result, the **/dev/bus/usb** node is empty.

2\. The hdc version is outdated. Using the hdc tool of version 3.1.0e (API15 SDK) or later will support starting the service process (hdc server) without a USB device node.

**Solution**

1\. Map the external USB device to the Docker so that the corresponding device is displayed in **/dev/bus/usb**. The following two methods are available:

Method 1: Use the **device** parameter (recommended and secure).

-   On the host, run the **lsusb** command to list USB devices and run the **dmesg | grep tty\*** or **ls /dev/tty\*** command to view serial port device information.
-   Run the container: Use the **\--device** parameter to map the device node of the host machine into the container.

\# Map the USB serial port device, for example, **/dev/ttyUSB0**.
docker run -it --device=/dev/ttyUSB0:/dev/ttyUSB0 image\_name
# Map the common USB device, for example, **/dev/bus/usb/001**.
docker run -it --device=/dev/bus/usb/001 image\_name

Method 2: Use the **privileged** parameter (This method is simple. The container can access all USB devices on the host, with high security risks.)

docker run -it --privileged image\_name

2\. Update the hdc tool to API15 (3.1.0e) or later by referring to [hdc Version Mappings](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#hdc-version-mappings).
