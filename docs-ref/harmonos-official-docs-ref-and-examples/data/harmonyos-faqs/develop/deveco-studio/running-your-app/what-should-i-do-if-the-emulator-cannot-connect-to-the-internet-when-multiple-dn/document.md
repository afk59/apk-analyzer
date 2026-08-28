# What should I do if the Emulator cannot connect to the Internet when multiple DNS servers exist?

**Symptom**

If multiple DNS server addresses are configured in the computer network environment, the HarmonyOS Emulator selects only one address for DNS resolution during startup. When this selected address fails to resolve a certain domain name, while the backup DNS of the host machine can resolve that domain name, it may result in a situation where the host machine can resolve the domain name, but the Emulator fails.

**Solution**

-   Windows: Open **Control Panel**, click **Network and Internet** > **View network status and tasks**, and click **Properties** of the network in use. In the dialog box that is displayed, double-click **Internet Protocol Version 4 (TCP/IPv4)**. On the properties page that is displayed, click **Use the following DNS server addresses**, enter a public high-quality DNS that is commonly used in the world.
-   Mac: Open **System Setting**, go to **Wi-Fi Network**, click the **Details** of the current network, and change the DNS to a public high-quality DNS that is commonly used in the world.
