# network-cfg

network-cfg (cfg is short for config) is a tool provided for setting network parameters, for example, setting a proxy for Wi-Fi.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/xm5VzAdCRUuQMtmTcKJ0JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CA91F80B3C8F107B02D4666FCC13F017C7689F6759146105AC542D0A8C2DD26)

network-cfg is supported since API version 20.

#### Environment Requirements

Before using this tool, you must obtain [hdc](../../performance-analysis-kit/command-line-tools/hdc/document.md) and run the **hdc shell** command.

#### Commands

| Command | Description |
| :-- | :-- |
| help | Displays the commands supported by the tool. |
| set | Sets network parameters. |

#### help

\# Display the help information.
network-cfg help
network-cfg -h

#### Setting Network Parameters

-   Display the commands supported by **set**.

network-cfg set -h

-   Set or cancel the current Wi-Fi proxy.

network-cfg set http\_proxy \[ip:port\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Q8cjVc_3SZquGFJ8EJkK_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=882B8A60F1B738EDA8BD2597B2C2A5CC4E8BB66D4E2B5DF168B58639A017B4C3)

-   The proxy can be set only when the Wi-Fi is connected.
-   The value range of the port number is \[1, 65535\]. If the port number is not specified or exceeds the value range, the default value **8080** is used.
-   The proxy takes effect only for the current Wi-Fi. You need to set the proxy again after switching the Wi-Fi.

Example:

\# Set a proxy for the current Wi-Fi. The host name is localhost, and the port number is 8080.
network-cfg set http\_proxy 127.0.0.1:8080
# Set a proxy for the current Wi-Fi. The host name is ip6-localhost, and the port number is 8080.
network-cfg set http\_proxy \[::1\]
# Cancel the current Wi-Fi proxy.
network-cfg set http\_proxy 0
