# What should I do if the Run button is always disabled on macOS after a file is modified on DevEco Studio?

**Symptom**

In the macOS environment, after a file is modified in DevEco Studio, the **Run** button is always disabled and the file fails to be executed.

**Possible Causes**

The hdc uses IPv6 on the macOS address by default. However, Java uses IPv4 by default and does not support IPv6. As a result, although the network port receives data, the protocol layer fails to receive it.

**Solution**

1.  Choose **Help** > **Edit Custom VM Options** to configure the IPv4 for DevEco Studio.
2.  Set **\-Djava.net.preferIPv4Stack=true**.
