# Getting Started with Network Navigator

#### Overview

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/YSZeSMSYREmQDbvX2fECag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F339C0C545DFF6C95FCBF08E5E502E4BF773657E63A18340DF00C1C89D7398B8)

The Network Navigator functionality is supported since API version 20.

Before app launch, developers usually need to optimize and verification app performance across diverse network conditions. For instance, after optimizing an app for smooth short video streaming during subway commutes, developers must verify whether stuttering issues have actually been resolved—but this requires testing in real-world scenarios.

Network Navigator, also known as netcopilot, provides comprehensive network simulation capabilities that enable developers to rapidly validate app user experience across typical network scenarios. This significantly improves testing efficiency and reduces verification costs. For example, developers can verify high-speed rail optimization effects without actually boarding a train.

Additionally, Network Navigator provides data transmission optimization recommendations for various network scenarios. By integrating Huawei's Network Boost Kit, apps can achieve cross-layer collaboration with the OS, significantly improving network connectivity and user experience.

For example, when transitioning between WLAN and mobile data networks while entering or exiting elevators, the app rapidly senses network interface changes and promptly redirects high-priority data requests to the new connection, ensuring seamless network switching without interruptions. When the network performance deteriorates, Network Boost Kit reports quality of service (QoS) data to assist the app in optimizing transmission scheduling.

#### Using Preset Network Simulation Scenarios

Network Navigator provides two access methods: the **Settings** interface and hdc command-line interface (CLI).

The following section describes how to access Network Navigator through the **Settings** interface. For usage via hdc CLI, see [Getting to Know Network Navigator](../../../debugging-tools/debugging-commands/command-line-utilities/getting-to-know-network-navigator/document.md).

When using this functionality for the first time, you need to enable the developer mode on your device by following instructions in [Developer Options](../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432). Then navigate to **Settings** > **System** > **Developer options** > **Network navigator** to access the Network Navigator interface.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/yqySUGklTQqGeOKcvAuhyw/en-us_image_0000002358741097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=400F7306F708F351197F61242E8C0A912B29147F788BF314CDF5D2C0EEE66027 "Click to enlarge")

Network Navigator has preset the following common network simulation scenarios. You can use them to quickly test app user experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/2kO9rNT7Rv-Anq81vgl20w/en-us_image_0000002358722249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3629E747F81A37A7EB74BC4739E9D553AFB62A16CA931620A568D59FB1056F4 "Click to enlarge")

**How to Start a Network Simulation Scenario**

To start network simulation, click any network simulation scenario you need from **Available simulations**. For example, after clicking **In & out of elevator**, the simulation scenario will be activated and you can view it in **Active simulations**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/O0giG13CTeiI2WdixxCquQ/en-us_image_0000002358721269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AB11990318CAE110EAEFED3FD28D4C5EBAB8F1A1052612029A29AE1B597450F "Click to enlarge")

You can also view the network simulation details in the device's live window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/HB_TJg8sSvahIIL9QUGpqw/en-us_image_0000002324801828.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBA26307C49A174F424871E22B1E2FA7469A1ABA9323763B6DF8439B6B01DC4A "Click to enlarge")

**How to Exit a Network Simulation Scenario**

To exit a network simulation scenario, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/XCUKzIyOT3ypmwEanOC8ww/en-us_image_0000002306341766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9A64BB1DED19C480F675A4F89803A04ED9CB03E9E613B541ACEBE25B39942E9) on the right and then click **Exit this network simulation scenario**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/OjrjRgh4R7azaT8-gOA7WQ/en-us_image_0000002324604290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B2F0997AC9A0670C18DB9C6963FED7D636E4A928646BCC814AC8A8A08BD8458 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/HhLEIQxXSka6DwL-ZSIlkQ/en-us_image_0000002358720285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0379E8A280CB9D3BBAA9EC2B3852AF44AF2C3594F2B2FD77BD68484FF0E3F362 "Click to enlarge")

The following table lists the prerequisites and phases for the preset network simulation scenarios.

<table class="simpletableborder"><tbody><tr><td valign="top"><p><strong>Network Simulation Scenario</strong></p></td><td valign="top"><p><strong>Prerequisites</strong></p></td><td valign="top"><p><strong>Scenario and Phase Description</strong></p></td></tr><tr><td valign="top"><p>In &amp; out of elevator</p></td><td valign="top"><p>Connect to WLAN and enable mobile data switch.</p></td><td valign="top"><p>Simulates the scenario in which a user enters and exits elevator with network switching between WLAN and mobile network. This scenario consists of six phases, runs for 5 minutes total, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Leave home WLAN range</p></td><td valign="top"><p>Connect to WLAN and enable mobile data switch.</p></td><td valign="top"><p>Simulates the scenario in which a user leaves home, disconnecting from WLAN and switching to mobile network. This scenario consists of four phases, lasts for 3 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Enter home WLAN range</p></td><td valign="top"><p>Connect to WLAN and enable mobile data switch.</p></td><td valign="top"><p>Simulates the scenario in which a user moves from outdoor to indoor area, connecting to WLAN and disconnecting from mobile network. This scenario consists of three phases, lasts for 3 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Busy cafeteria</p></td><td valign="top"><p>Connect to WLAN or mobile network.</p></td><td valign="top"><p>Simulates a network with many connected devices, featuring high contention, low bandwidth, and high latency. This scenario consists of three phases, lasts for 5 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Parking garage</p></td><td valign="top"><p>Connect to WLAN or mobile network.</p></td><td valign="top"><p>Simulates poor network coverage with weak signal, low bandwidth, and high latency. This scenario consists of three phases, lasts for 5 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Riding the subway</p></td><td valign="top"><p>Connect to WLAN or mobile network.</p></td><td valign="top"><p>Simulates highly variable network conditions, with strong signal at stations and weak signal between stations. This scenario consists of five phases, lasts for 5 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Riding high-speed train</p></td><td valign="top"><p>Insert dual SIM cards and enable mobile data switch.</p></td><td valign="top"><p>Simulates highly variable network conditions with frequent base station switching and intermittent service unavailability. This scenario consists of five phases, lasts for 10 minutes, and executes cyclically.</p></td></tr><tr><td valign="top"><p>Highway driving</p></td><td valign="top"><p>Connect to WLAN or mobile network.</p></td><td valign="top"><p>Simulates highly variable network conditions, with strong signal in urban areas and weak signal in tunnels. This scenario consists of five phases, lasts for 5 minutes, and executes cyclically.</p></td></tr></tbody></table>

For more details about the phases and network conditions, see [Appendix](#section143601919151614).

#### Network Optimization Recommendations

With Network Navigator, you can monitor network changes in real time through the live window. You can also click the live window to view network simulation details. In addition, you can view network parameters and network coding best practices by clicking the respective link in the window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/nNsiR9GRSTiYxm9OdjqV-w/en-us_image_0000002359392873.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5BAEB47B58237D3958E573CB078FF6ED1FB9D4B460D59BF7B946D66E1DA5EDC "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/_jYpl2D0SyGiF3rqB5gQ_w/en-us_image_0000002358639269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B2A7D4CA9607D3D2377D6CA34314EABE929E906E0F95AFE8CFD7DE6B3206968 "Click to enlarge")

#### **Code Optimization Recommendations**

Network Navigator intelligently simulates network QoS changes when activating specified scenarios, helping developers quickly build target network environments. Through this feature, developers can proactively discover app compatibility issues in different network environments and perform targeted optimization based on the best practices in this section.

**Code Optimization Scenarios**

Currently, eight network simulation scenarios are supported. For details, see [Appendix](#section143601919151614). The network characteristics can be classified into three types: network switching, network fluctuation, and poor network quality. The following table lists the scenario characteristics and code development suggestions.

**Network Switching**

-   **Characteristics**: When a device switches between network types (for example, WLAN and cellular) or switches SIM cards, it may experience IP address changes, forced TCP connection resets, and delays due to DNS re-resolution and handshake re-establishment.
-   **Typical scenarios**: Entering and leaving an elevator, disconnecting from WLAN when leaving home, and traveling on high-speed rail (switching between SIM cards).
-   **Best practices**: Detect network switches in a timely manner and re-establish connections, perform DNS resolution, and re-send any incomplete requests. Alternatively, use the HTTP module of Network Kit to initiate network requests. Network Kit incorporates the intelligent multi-network switching capability of the Tongtu network protocol stack, which automatically reroutes pending and ongoing requests to the active network during network switching. This effectively prevents request failures and service response delays in network switching scenarios. The sample code for sending HTTP requests using Network Kit is as follows:
    
    // Import related modules.
    import { http } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // Each httpRequest corresponds to an HTTP request task and cannot be reused.
     let httpRequest = http.createHttp();
     httpRequest.request(
      // Customize EXAMPLE\_URL in extraData on your own. It is up to you whether to add parameters to the URL.
      "EXAMPLE\_URL", (err: BusinessError, data: http.HttpResponse) => {
      if (!err) {
        // Parse the HTTP response carried in data.result based on the service requirements.
        console.info('Result:' + JSON.stringify(data.result));
        // Call destroy() to release resources after HttpRequest is complete.
        httpRequest.destroy();
      } else {
        console.error('error:' + JSON.stringify(err));
        // Call destroy() to release resources after HttpRequest is complete.
        httpRequest.destroy();
      }
    }
    );
    
    **Network Fluctuation**
    
    -   **Characteristics**: Due to rapid fluctuations in signal strength (for example, during movement or high-speed travel), network performance can degrade sharply. This includes a significant reduction in bandwidth (from 50 Mbps to 1 Mbps), severe jitter in delay (RTT fluctuations exceeding 300%), and intermittent packet loss (0% to 5%).
    -   **Typical scenarios**: Riding the subway or driving on highways.
    -   **Best practices**:
    
    1.  Subscribe to **netQuality** events in Network Boost Kit to monitor network quality in real time and take appropriate measures.
        
        // Import related modules.
        import { netQuality } from '@kit.NetworkBoostKit';
        import { BusinessError } from '@kit.BasicServicesKit';
        try {
          netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
            if (list.length > 0) {
              list.forEach((qos) => {
                // Callback processing.
                console.info(\`Uplink bandwidth of this data link type: ${JSON.stringify(qos.linkUpBandwidth)}.\` );
                console.info(\`Downlink bandwidth of the data link type: ${JSON.stringify(qos.linkDownBandwidth)}.\` );
                // The app can detect the network quality in real time based on information such as the uplink and downlink bandwidths and adjust the request policy accordingly.
              });
            }
          });
         } catch (err) {
          console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
        }
        
    2.  When network quality is good, prefetch potential subsequent requests, send them in advance, and cache the fetched resources. When these requests are actually triggered, resources can be loaded directly from the cache, enhancing response speed and reducing latency.
        
        // Import related modules.
        import { rcp } from '@kit.RemoteCommunicationKit';
        import { HashMap } from "@kit.ArkTS";
        export class PrefetchingRcp {
          private session = rcp.createSession();
          private responsePrefetched: HashMap<string, rcp.Response> = new HashMap<string, rcp.Response>();
          public async prefetch(url: string) {
            const request = new rcp.Request(url);
            try {
              // Send a prefetch request.
              let response: rcp.Response = await this.session.fetch(request);
              // Cache the fetched resources.
              this.responsePrefetched.set(url, response);
              return Promise.resolve();
             } catch (reason) {
               console.error(\`Rcp prefetch failed: ${reason.code}\`);
               return Promise.reject();
            }
          }
        }
        
    3.  When network quality is poor, reduce request frequency or data volume to avoid worsening network congestion.

**Poor Network Quality**

-   **Characteristics**: In signal shielding areas (such as underground parking lots) or high-density access environments (such as crowded cafeterias), the network consistently exhibits low bandwidth (<1 Mbps), high latency (>100 ms), and a high packet loss rate.
-   **Typical scenarios**: Crowded cafeterias and parking lots.
-   **Best practices**: Reduce request frequency and data volume promptly when the network is congested, and resume requests once the network recovers. Besides using **netQosChange** to assess network quality, you can also subscribe to network scenario detection events to directly identify network congestion or weak signals. Upon detection, reduce request frequency to avoid repeated requests that could worsen network congestion. The example code is as follows:
    
    // Import the related modules.
    import { netQuality } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    try {
      netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
        if (list.length > 0) {
          list.forEach((sceneInfo) => {
            // Process the network scenario identification callback.
            if (sceneInfo.scene == 'congestion') {
              // Service logic implemented upon network congestion
            }
            if (sceneInfo.scene == 'normal') {
              // Service logic implemented upon network recovery
            }
            if (sceneInfo.weakSignalPrediction) {
              // Service logic implemented upon detection of potential network deterioration via weak signal prediction
            }
          });
        }
      });
     } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    

#### Information Collection

When you use Network Navigator, your app usage records will be collected. We may contact you through the contact information linked to your HUAWEI ID for user feedback surveys, to help us further optimize this feature.

The data that will be collected includes:

-   Usage logs. You need to associate your HUAWEI ID to use Network Navigator. By enabling **User Experience Improvement Program**, you are automatically consenting to upload usage logs.
    
-   Bundle name and version number of the app that uses this feature.
    
-   Network simulation scenarios used by the app and the corresponding timestamps during usage.
    

#### Appendix

**QoS in Different Network Scenarios**

**In & out of elevator**

This scenario lasts for 5 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Waiting for the elevator</p></td><td valign="top"><p>0:00–0:30</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.01%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Entering elevator</p></td><td valign="top"><p>0:30–1:30</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>90 Mbps to 50 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>30 Mbps to 8 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>22 ms to 40 ms</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>0.00% to 0.21%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Elevator door closing</p></td><td valign="top"><p>1:30–1:40</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 10 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>10 Mbps to 5 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0 ms to 200 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Elevator door closing</p></td><td valign="top"><p>1:40–1:50</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>10 Mbps to 3 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>5 Mbps to 0 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>200 ms to 1000 ms</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>0.00% to 8.00%</p></td><td valign="top"><p>Linear increase</p></td></tr><tr><td valign="top"><p>Elevator door closing</p></td><td valign="top"><p>1:50–2:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>20 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>5 Mbps to 15 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.20%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Elevator going up</p></td><td valign="top"><p>2:00–3:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>20 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>5 Mbps to 15 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 50 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.01% to 0.20%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Elevator door opening</p></td><td valign="top"><p>3:00–3:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>30 Mbps to 100 Mbps</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>15 Mbps to 50 Mbps</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>50 ms to 20 ms</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>0.01% to 0.10%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Exiting elevator</p></td><td valign="top"><p>3:30–4:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>100 Mbps to 300 Mbps</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>20 ms to 30 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.01%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Exiting elevator</p></td><td valign="top"><p>4:00–5:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.01%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Leave home WLAN range**

This scenario lasts for 3 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>At home</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 35 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>At the door</p></td><td valign="top"><p>1:00–1:30</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>100 Mbps to 50 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>40 Mbps to 10 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>25 ms to 35 ms</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Walking away</p></td><td valign="top"><p>1:30–1:50</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 10 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>10 Mbps to 5 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0 ms to 200 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Walking away</p></td><td valign="top"><p>1:50–2:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>10 Mbps to 3 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>5 Mbps to 0 Mbps</p></td><td valign="top"><p>Linear decrease</p></td><td valign="top"><p>200 ms to 1000 ms</p></td><td valign="top"><p>Linear increase</p></td><td valign="top"><p>0.00% to 8.00%</p></td><td valign="top"><p>Linear increase</p></td></tr><tr><td valign="top"><p>Walking away</p></td><td valign="top"><p>2:00–2:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>200 Mbps to 400 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 70 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>On the way</p></td><td valign="top"><p>2:30–3:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p><p></p></td></tr></tbody></table>

**Enter home WLAN range**

This scenario lasts for 3 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>In the hallway</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>At the door</p></td><td valign="top"><p>1:00–1:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>200 Mbps to 400 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 70 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>At the door</p></td><td valign="top"><p>1:30–2:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>30 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>10 Mbps to 30 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 ms to 60 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Entering home</p></td><td valign="top"><p>2:00–3:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Busy cafeteria**

This scenario lasts for 5 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Entering the cafeteria</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Queuing for food</p></td><td valign="top"><p>1:00–2:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>5 Mbps to 15 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>5 Mbps to 15 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 ms to 100 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 2.4%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Sitting down for meals</p></td><td valign="top"><p>2:00–4:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>15 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>10 Mbps to 20 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 75 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.2%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Leaving the cafeteria</p></td><td valign="top"><p>4:00–5:00</p></td><td valign="top"><p>WLAN</p></td><td valign="top"><p>60 Mbps to 140 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 60 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 40 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Parking garage**

This scenario lasts for 5 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Heading to the parking garage</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Staying in the parking garage</p></td><td valign="top"><p>1:00–4:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>10 Mbps to 20 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>10 Mbps to 20 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 ms to 100 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.50%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Exiting the parking garage</p></td><td valign="top"><p>4:00–5:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Riding the subway**

This scenario lasts for 5 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Waiting for the train at the subway platform</p></td><td valign="top"><p>0:00–0:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling on the train</p></td><td valign="top"><p>0:30–2:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>100 Mbps to 250 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.50%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Entering the station</p></td><td valign="top"><p>2:30–3:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling on the train</p></td><td valign="top"><p>3:00–4:30</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>100 Mbps to 250 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.50%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Entering the station</p></td><td valign="top"><p>4:30–5:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Riding high-speed train**

This scenario lasts for 10 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Waiting at the high-speed railway platform</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>Cellular (SIM 1)</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling in the suburban area of the city</p></td><td valign="top"><p>1:00–2:00</p></td><td valign="top"><p>Cellular (SIM 1)</p></td><td valign="top"><p>100 Mbps to 250 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.50%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling in the mountainous area</p></td><td valign="top"><p>2:00–4:00</p></td><td valign="top"><p>Cellular (SIM 1)</p></td><td valign="top"><p>0 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0 Mbps to 10 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>300 ms to 2000 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 5.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling in the mountainous area</p></td><td valign="top"><p>4:00–6:00</p></td><td valign="top"><p>Cellular (SIM 2)</p></td><td valign="top"><p>0 Mbps to 50 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0 Mbps to 10 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>300 ms to 2000 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 5.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Arriving at the station in the suburban area of the city</p></td><td valign="top"><p>6:00–8:00</p></td><td valign="top"><p>Cellular (SIM 1)</p></td><td valign="top"><p>200 Mbps to 400 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 70 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.50%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Exiting the station</p></td><td valign="top"><p>8:00–10:00</p></td><td valign="top"><p>Cellular (SIM 1)</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>

**Highway driving**

This scenario lasts for 5 minutes and executes cyclically.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Sub-phase</p></td><td valign="top"><p>Duration (min:sec)</p></td><td valign="top"><p>Network Interface</p></td><td valign="top"><p>Downlink Bandwidth</p></td><td valign="top"><p>Downlink Bandwidth Distribution</p></td><td valign="top"><p>Uplink Bandwidth</p></td><td valign="top"><p>Uplink Bandwidth Distribution</p></td><td valign="top"><p>Latency</p></td><td valign="top"><p>Delay Distribution</p></td><td valign="top"><p>Packet Loss</p></td><td valign="top"><p>Packet Loss Distribution</p></td></tr><tr><td valign="top"><p>Traveling in the urban area</p></td><td valign="top"><p>0:00–1:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Entering a tunnel</p></td><td valign="top"><p>1:00–2:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>0 Mbps to 10 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0 Mbps to 2 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>300 ms to 2000 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 5.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling in the urban area</p></td><td valign="top"><p>2:00–3:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Driving on the elevated road</p></td><td valign="top"><p>3:00–4:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>200 Mbps to 400 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>30 Mbps to 70 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>20 ms to 55 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr><tr><td valign="top"><p>Traveling in the urban area</p></td><td valign="top"><p>4:00–5:00</p></td><td valign="top"><p>Cellular</p></td><td valign="top"><p>300 Mbps to 500 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>50 Mbps to 100 Mbps</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>15 ms to 45 ms</p></td><td valign="top"><p>Random</p></td><td valign="top"><p>0.00% to 0.00%</p></td><td valign="top"><p>Random</p></td></tr></tbody></table>
