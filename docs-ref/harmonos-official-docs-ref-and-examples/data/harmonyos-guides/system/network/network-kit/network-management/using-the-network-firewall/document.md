# Using the Network Firewall

#### Introduction

The network firewall module provides the following functions:

-   Basic firewall management functions, such as enabling and disabling of firewalls and firewall rules, and audit.
-   Firewall rule configuration, including the rule name, description, operation, applicable application, protocol type, address, port, and outbound/inbound direction.
-   DNS policy configuration, including the domain names allowed or not allowed for resolution and the DNS server (active or standby) used for resolution (application level).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/1kpCp2BxSJuu1zkZXAH0wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC0F72A6D2AA58C96EBE7490E87D2B7AF6FF68530D2E034E36A9D651A9D91CE8)

To maximize the application running efficiency, all APIs are called asynchronously in callback or promise mode. The following code examples use the promise mode. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-netfirewall).

#### When to Use

Typical firewall scenarios include:

-   IP address-based access control

1.  Restricting network access for specific applications
2.  Restricting network communication to specific IP addresses, protocols, and ports
3.  Restricting network communication of specific applications to specific IP addresses, protocols, and ports
4.  Putting interception rules into effect immediately after delivery (This function is applicable only to the TCP protocol. An intercepted TCP connection must be disconnected.)

-   Domain name-based access control

1.  Restricting DNS resolution of an application for specific domain names (This function is applicable to standard unencrypted DNS protocols, but not encrypted and private DNS protocols.)
2.  Restricting DNS resolution of an application for specific domain names (This function is applicable to standard unencrypted DNS protocols, but not encrypted and private DNS protocols.)
3.  Putting interception rules into effect immediately after delivery (This function is applicable only to the TCP protocol. An intercepted TCP connection must be disconnected.)

The following describes the development procedure specific to each application scenario.

#### IP address-based access control

1.  Use a network cable to connect the device to a network port.
    
2.  Import the **netFirewall** namespace from **@kit.NetworkKit**.
    
    // Import the netFirewall namespace from @kit.NetworkKit.
    import { netFirewall } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
3.  Call **setNetFirewallPolicy** to enable the firewall.
    
    // IP address type
    interface IpType{
      family:number;
      type:number;
      address?:string;
      mask?:number;
      startIp?:string;
      endIp?:string;
    }
    // Port number
    interface IpPort{
      startPort:number;
      endPort:number;
    }
    // ...
        // Define the firewall policy to enable the firewall and deny inbound traffic while allowing outbound traffic.
        let policy: netFirewall.NetFirewallPolicy = {
          isOpen: true,
          inAction: netFirewall.FirewallRuleAction.RULE\_DENY,
          outAction: netFirewall.FirewallRuleAction.RULE\_ALLOW
        };
    
        // Set the firewall policy for user 100.
        netFirewall.setNetFirewallPolicy(100, policy).then(() => {
          hilog.info(0x0000, 'testTag', \`set firewall policy success.\`);
        }).catch((error : BusinessError) => {
          hilog.error(0x0000, 'testTag', \`error: set firewall policy failed: ${JSON.stringify(error)}\`);
        });
    
4.  Call **addNetFirewallRule** to add firewall rules.
    
    // Initialize firewall rules for specific types of IP addresses.
    let ipRule: netFirewall.NetFirewallRule = {
      name: 'rule1',
      description: 'rule1 description',
      direction: netFirewall.NetFirewallRuleDirection.RULE\_IN,
      action: netFirewall.FirewallRuleAction.RULE\_DENY,
      type: netFirewall.NetFirewallRuleType.RULE\_IP,
      isEnabled: true,
      appUid: 20001,
      localIps: \[
        {
          family: 1,
          type: 1,
          address: '10.10.1.1',
          mask: 32
        },{
        family: 1,
        type: 2,
        startIp: '10.20.1.1',
        endIp: '10.20.1.10'
      }\] as IpType\[\],
      remoteIps:\[
        {
          family: 1,
          type: 1,
          address: '20.10.1.1',
          mask: 32
        },{
        family: 1,
        type: 2,
        startIp: '20.20.1.1',
        endIp: '20.20.1.10'
      }\] as IpType\[\],
      protocol: 6,
      localPorts: \[
        {
          startPort: 1000,
          endPort: 1000
        },{
        startPort: 2000,
        endPort: 2001
      }\] as IpPort\[\],
      remotePorts: \[
        {
          startPort: 443,
          endPort: 443
        }\] as IpPort\[\],
      userId: 100
    };
    // Add firewall rules.
    netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
      // ...
      hilog.info(0x0000, 'testTag', \`rule Id: ${result}\`);
    }, (reason: BusinessError) => {
      // ...
      hilog.error(0x0000, 'testTag', \`error: add firewall rule failed:  ${JSON.stringify(reason)}\`);
    });
    

#### Domain Name-based Access Control

1.  Use a network cable to connect the device to a network port.
    
2.  Import the **netFirewall** namespace from **@kit.NetworkKit**.
    
    // Import the netFirewall namespace from @kit.NetworkKit.
    import { netFirewall } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
3.  Call **setNetFirewallPolicy** to enable the firewall.
    
    interface domain{
      isWildcard: boolean;
      domain: string;
    }
    // ...
        // Define the firewall policy to enable the firewall and deny inbound traffic while allowing outbound traffic.
        let policy: netFirewall.NetFirewallPolicy = {
          isOpen: true,
          inAction: netFirewall.FirewallRuleAction.RULE\_DENY,
          outAction: netFirewall.FirewallRuleAction.RULE\_ALLOW
        };
    
        // Set the firewall policy for user 100.
        netFirewall.setNetFirewallPolicy(100, policy).then(() => {
          hilog.info(0x0000, 'testTag', \`set firewall policy success.\`);
        }).catch((error : BusinessError) => {
          hilog.error(0x0000, 'testTag', \`error: set firewall policy failed: ${JSON.stringify(error)}\`);
        });
    
4.  Call **addNetFirewallRule** to add firewall rules.
    
    // Initialize firewall rules for specific types of domain names.
    let domainRule: netFirewall.NetFirewallRule = {
      name: 'rule2',
      description: 'rule2 description',
      direction: netFirewall.NetFirewallRuleDirection.RULE\_IN,
      action: netFirewall.FirewallRuleAction.RULE\_DENY,
      type: netFirewall.NetFirewallRuleType.RULE\_DOMAIN,
      isEnabled: true,
      appUid: 20002,
      domains: \[
        {
          isWildcard: false,
          domain: 'www.HarmonyOS.cn'
        },{
        isWildcard: true,
        domain: '\*.HarmonyOS.cn'
      }\] as domain\[\],
      userId: 100
    };
    
    // Add firewall rules.
    netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
      // ...
      hilog.info(0x0000, 'testTag', \`rule Id: ${result}\`);
    }, (reason: BusinessError) => {
      // ...
      hilog.error(0x0000, 'testTag', \`error: add firewall rule failed:  ${JSON.stringify(reason)}\`);
    });
