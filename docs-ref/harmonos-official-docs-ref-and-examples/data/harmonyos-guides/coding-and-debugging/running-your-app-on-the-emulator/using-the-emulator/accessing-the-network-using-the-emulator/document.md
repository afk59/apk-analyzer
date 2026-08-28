# Accessing the Network Using the Emulator

#### Accessing the Internet

Emulators can access the Internet through the network of the local computer.

If the connection fails, refer to [What should I do if the Emulator cannot connect to the Internet?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-app-running-26) for troubleshooting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/IRX8o0nxQkGwzVcx3fD4ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D1F085AA954E52F1161241DC72ED484CF4910A92F3F6B9D39F8C977017FA6B2)

Since the emulator's virtual Ethernet remains in a connected state, disconnecting the local computer's network or the Wi-Fi within the emulator will not put the emulator into a fully disconnected network state.

#### Accessing the Local Network

Create a network server on the local computer. The emulator can access the server on the local computer through 10.0.2.2:<_localPort_\>. 10.0.2.2 is the default gateway of the emulator.

#### Enabling Mutual Access Between Two Emulators

If two emulators need to communicate with each other, perform the following steps:

1.  Run emulators A and B on the local computer. The device IP address of the emulator is 10.0.2.15.
2.  On emulator B, set the server to listen for 10.0.2.15:<_serverPort_\>.
3.  On the local computer, set redirection from the local computer (localhost:<_localPort_\>) to emulator B (10.0.2.15:<_serverPort_\>). For example:
    
    hdc -t 127.0.0.1:5555 fport tcp:<localPort> tcp:<serverPort>
    
    **127.0.0.1:5555** is the HDC service port number of emulator B, which can be queried using the **hdc list targets** command.
    
4.  On emulator A, set the client to connect to 10.0.2.2:<_localPort_\>. 10.0.2.2 indicates the default gateway of the emulator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/KlghbBFjQKWOAbfqUIxZcA/en-us_image_0000002532748607.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F446F9B33751DE643A39E7E62F0DF953A305BF9C4142E06384120FD060D87D8)
