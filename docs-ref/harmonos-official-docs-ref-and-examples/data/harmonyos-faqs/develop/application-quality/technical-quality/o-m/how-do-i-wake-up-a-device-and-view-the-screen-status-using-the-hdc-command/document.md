# How do I wake up a device and view the screen status using the hdc command?

Use **hdc shell power-shell wakeup** to wake up the device.

Use **hdc shell hidumper -s 3301 -a** to view the screen status.

To obtain the IMEI of a mobile phone, run **hdc target boot bootloader** to enter fastboot and run **fastboot oem get-psid**.
