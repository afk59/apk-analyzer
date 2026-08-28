# What should I do if the Emulator cannot connect to the Internet?

**Symptom**

The WLAN option is enabled and the Emulator is successfully connected to VirtWifi, but websites still cannot be accessed.

**Solution**

Whether VirtWifi is connected is irrelevant to whether the Emulator can access the Internet. VirtWifi is used only to determine the WLAN connection status in the Emulator. The Emulator uses the Ethernet or WLAN of the local PC to access the Internet and shares the same network resources with the local PC. If the network cannot be connected, check whether the local network access is restricted (for example, when using a company's intranet). If the network access is restricted, the Emulator cannot access the Internet.
