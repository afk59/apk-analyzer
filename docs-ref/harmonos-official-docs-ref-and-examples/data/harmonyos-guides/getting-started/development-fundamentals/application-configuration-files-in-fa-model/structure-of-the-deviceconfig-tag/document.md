# Structure of the deviceConfig Tag

The **deviceConfig** tag contains device-specific configuration of the application, including properties such as **default**, **tv**, **car**, and **wearable**.

#### Internal Structure of the deviceConfig Tag

**Table 1** Internal structure of the deviceConfig tag

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| default | Default application configuration. Applications with the default configuration can be compiled and built but cannot be released. Change the device type to phone. | Object | Yes (initial value: left empty) |
| tablet | Application configuration specific to tablets. | Object | Yes (initial value: left empty) |
| tv | Application configuration specific to smart TVs. | Object | Yes (initial value: left empty) |
| car | Application configuration specific to telematics devices. | Object | Yes (initial value: left empty) |
| wearable | Application configuration specific to wearables. | Object | Yes (initial value: left empty) |
| 2in1 | Application configuration specific to PCs, mainly used for multi-window and multi-task interactions, and keyboard and mouse operations. It fully showcases the device productivity. | Object | Yes (initial value: left empty) |
| phone | Application configuration specific to smartphones. | Object | Yes (initial value: left empty) |
| liteWearable | Application configuration specific to lite wearables. | Object | Yes (initial value: left empty) |

For details about the properties of the **deviceConfig** tag, see [Internal Structure of deviceConfig's Properties](#internal-structure-of-deviceconfigs-properties).

#### Internal Structure of deviceConfig's Properties

**Table 2** Internal structure of deviceConfig's properties

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| process | Name of the process running the application or ability. If the **process** property is configured in the **deviceConfig** tag, all abilities of the application run in this process. You can set the **process** property for a specific ability in the **abilities** tag, so that the ability can run in the particular process. The value can contain a maximum of 31 characters. | String | Yes (initial value: left empty) |
| keepAlive | 
Whether the application keeps running. This property applies only to system applications and does not take effect for third-party applications.

\- **true**: The application keeps running. The system starts the application upon its startup and restarts the application when the application exits.

\- **false**: The application does not keep running. The system neither starts the application upon its startup nor restarts the application when the application exits.

 | Boolean | Yes (initial value: **false**) |
| supportBackup | 

Whether the application supports backup and restore.

\- **true**: Yes

\- **false**: No

 | Boolean | Yes (initial value: **false**) |
| compressNativeLibs | 

Whether libraries are stored in the HAP after being compressed during HAP packaging.

\- **true**: Libraries are stored in the HAP file after being compressed.

\- **false**: Libraries are stored without being compressed.

Whether libraries need to be decompressed during application installation. (Since API version 16, this field is supported. In earlier versions, libraries are decompressed by default.)

\- **true**: Libraries need to be decompressed.

\- **false**: Libraries do not need to be decompressed.

 | Boolean | Yes (During HAP packaging, initial value: **false**; during application installation, initial value: **true**) |
| network | Network security configuration. You can customize the network security settings of the application in the security statement of the configuration file without modifying the application code. | Object | Yes (initial value: left empty) |

#### Internal Structure of the network Property

**Table 3** Internal structure of the network property

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| cleartextTraffic | 
Whether to allow the application to use plaintext traffic, for example, plaintext HTTP traffic.

\- **true**: The application is allowed to use plaintext traffic.

\- **false**: The application is not allowed to use plaintext traffic.

 | Boolean | Yes (initial value: **false**) |
| securityConfig | Network security configuration of the application. | Object | Yes (initial value: left empty) |

#### Internal Structure of the securityConfig Property

**Table 4** Internal structure of the securityConfig property

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| domainSettings | Security configuration for custom domain name ranges. This property allows nested domains. A **domainSettings** object can nest **domainSettings** objects of smaller domain name ranges. | Object | Yes (initial value: left empty) |

#### Internal Structure of the domainSettings Property

**Table 5** Internal structure of the domainSettings property

| Name | Description | Data Type | Initial Value Allowed |
| :-- | :-- | :-- | :-- |
| cleartextPermitted | 
Whether cleartext traffic transmission is allowed within the custom domain name range. If both **cleartextTraffic** and **securityConfig** exist, the value of **cleartextPermitted** is used.

\- **true**: Cleartext is allowed.

\- **false**: Cleartext is not allowed.

 | Boolean | Yes (initial value: **false**) |
| domains | 

Domain name. This property consists of two sub-properties: **subdomains** and **name**.

\- **subdomains** (boolean): whether the domain name contains subdomains. When set to **true**, the rule matches the corresponding domain and all its subdomains (including subdomains of subdomains). When set to **false**, the rule applies only to exact matches.

\- **name** (string): domain name.

 | Object array | Yes (initial value: left empty) |

Example of the **deviceConfig** tag:

"deviceConfig": {
  "default": {
    "process": "com.example.test.example",
    "supportBackup": false,
    "network": {
      "cleartextTraffic": true,
      "securityConfig": {
        "domainSettings": {
          "cleartextPermitted": true,
          "domains": \[
            {
              "subdomains": true,
              "name": "example.ohos.com"
            }
          \]
        }
      }
    }
  }
}
