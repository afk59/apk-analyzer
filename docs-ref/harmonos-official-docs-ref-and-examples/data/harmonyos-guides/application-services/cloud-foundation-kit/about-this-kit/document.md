# About This Kit

Cloud Foundation Kit provides cloud services such as Cloud Functions, Cloud DB, and Cloud Storage for apps as needed. The cloud platform provides the servers and environments needed to run your app. This allows you to focus solely on the business logic of your app without worrying about the underlying infrastructure, such as servers, operating systems, and containers.

#### Advantages

-   Low O&M costs
    
    You do not need to build or manage cloud resources, since Cloud Foundation Kit provides you with a series of capabilities, including function computing, databases, and storage.
    
-   Auto scaling and pay per use
    
    In both peak and off-peak scenarios, Cloud Foundation Kit supports auto-scaling and pay-per-use billing based on your actual needs. This means you only pay for the resources you use, effectively improving resource utilization and reducing costs.
    
-   Security and reliability
    
    Cloud Foundation Kit supports full-process encryption of data, triple authentication for apps, users, and services, and provides a role-based permission management mechanism to ensure the security of your and your users' data.
    
-   Integrated device-cloud development
    
    DevEco Studio offers an integrated device-cloud development experience, enabling developers to collaboratively develop device-side and cloud-side code using a unified technology stack. This seamless transition allows frontend developers to become full-stack engineers with ease, significantly enhancing the efficiency of building HarmonyOS apps and atomic services while reducing development costs.
    

#### Typical Scenarios

## Backend Development for Apps and Atomic Services

You can easily use Cloud Functions, Cloud DB, and Cloud Storage to simplify the development and O&M of apps and atomic services, so you can quickly build backend services for them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/yZSpyv5URruMefN4PWVbGw/en-us_image_0000002474174561.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B81DE37FC9C60365D4C75C7D32DA3A32F76B2EF0E81D4B50F1C3C6CAA6B1B82 "Click to enlarge")

## Compute-Intensive Tasks

Cloud Foundation Kit automatically scales computing resources for compute-intensive tasks in your app during task startup and frees the resources up upon task completion, optimizing cost efficiency.

You can configure a cron trigger for a cloud function to execute tasks at a scheduled time, and use other services to call a cloud function to execute tasks.

For example, Cloud Foundation Kit can be used to render and overlay data, including:

-   Encapsulating original data, for example, processing report data.
-   Synchronizing data, for example, extracting, transforming, or loading data.
-   Processing videos or images, for example, generating videos or images with different resolutions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/1cY00r6XQPW4qzLiMx8E8Q/en-us_image_0000002474214389.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F936BCC16C4F60F4E9ED6C6386580071C25A7E9421002DDD0ACAA5EA521ACCB4 "Click to enlarge")

## Protocol Adaptation and Conversion

Cloud Foundation Kit speeds up your service rollout with our lightweight, flexible services that facilitate protocol adaptation and conversion and seamless third-party platform integration.

For example, functions such as data storage, authentication, message queues, push notifications, and scheduled tasks can be linked or converted through cloud services at the glue layer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/tbwsS8VwRDCwg0wRbIL3Ww/en-us_image_0000002440934408.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=421190029FD6F0E598068AEB9AAE8A07509A915594147E2A2187AA593A73BC5A "Click to enlarge")

## Traffic Surge

In some special scenarios, a large number of access requests may occur in services that adopt the traditional architecture. To ensure stable operation during peak hours, it is usually necessary to purchase high-performance, expensive servers and set up clusters for load balancing. However, when the business demand decreases, this leads to significant resource wastage.

Cloud Foundation Kit can quickly and automatically scale based on business traffic, minimizing the risk of system issues during peak hours. This allows apps to smoothly handle high-demand scenarios, such as flash sales and holiday events. When the traffic decreases, the elastic scaling feature supports automatic scale-in, freeing up idle resources and preventing waste.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/jNyjM3xrQ_68BLLwWDXjzA/en-us_image_0000002440934404.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFE43D2EA1F089AF5B3AA0318406F071630D24B3FC4C5A558F4166F271FBF781 "Click to enlarge")

#### Restrictions

## Supported Devices

| 
Capability

 | 

Device Type

 |
| :-- | :-- |
| 

Cloud Functions

 | 

Phone, tablet, wearable, and TV

 |
| 

Cloud DB

 |
| 

Cloud Storage

 |

## Supported Countries/Regions

| 
Capability

 | 

Country/Region

 |
| :-- | :-- |
| 

Cloud Functions

 | 

For details, please refer to [Supported Countries/Regions](../appendix/supported-countries-regions/document.md).

 |
| 

Cloud DB

 |
| 

Cloud Storage

 |

## Supported Signing Modes

Two signing modes are supported: [signing an app associated with a registered app](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section20943184413328) (DevEco Studio 6.0.0 Beta5 or later) and [signing an app manually](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233)

#### Emulator Support

Since 6.0.0(20) Beta5, this kit has supported the Emulator, but there are some differences between real devices and the Emulator. For details, please refer to [Differences Between the Emulator and the Real Device](../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section1227613205203).

#### Billing

Cloud Foundation Kit includes Cloud Functions, Cloud DB, and Cloud Storage. Huawei provides a free quota for each service for trial use. For details about the quota, see the quota description of each service.

-   [Cloud Functions](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloud-function-price-0000001211271102)
-   [Cloud DB](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-clouddb-price-0000001256815629)
-   [Cloud Storage](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloudstorage-price-0000001253665999)
