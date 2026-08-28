# How do I access the local macOS HTTP service on the Emulator?

You can run the **hdc shell ip -r** command to check the IP address mapped to the PC, which is **10.0.2.2**.

In the HTTP request URL, replace the IP address with **10.0.2.2**. For example, if the HTTP URL on the Mac is **http://127.0.0.1:8088/api/userinfo**, the URL after replacement is **http://10.0.2.2:8088/api/userinfo**.
