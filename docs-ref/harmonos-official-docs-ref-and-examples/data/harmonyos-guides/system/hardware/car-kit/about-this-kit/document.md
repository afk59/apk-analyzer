# About This Kit

Car Kit offers a set of capabilities that can be easily integrated into mobility services. By integrating Car Kit, you can enable users to seamlessly transfer navigation information between their phones and the head unit of Harmony Intelligent Mobility Alliance (HIMA) vehicles, access their phone apps on the head unit of these vehicles through Super Home Screen, or run phone apps on the head unit of HiCar-certified vehicles. All these features are designed to deliver a smoother and smarter mobility experience for users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/nWfmHB3XTYmwVcrLbVuT8w/en-us_image_0000002513566297.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAE01EF498B1DD93986F76735F134DE2CFA8838089A50C78B38FDC41B67EDD0B)

#### Use Cases

Car Kit provides Huawei phone users with two types of solutions in mobility scenarios, one for HIMA vehicles and the other for HiCar-certified vehicles.

## HIMA Vehicles

The navigation hop and Super Home Screen solutions are provided for users driving a HIMA vehicle (equipped with a dashboard or head-up display).

Navigation hop:

-   This solution is used for seamless navigation information transfer between phones and head units in various scenarios. For example, users can transfer navigation and address data from their phones to the head unit, and once they exit the vehicle, navigation automatically switches back to their phones to guide them as they walk.
-   By integrating navigation APIs of Car Kit, your app can provide navigation information and respond to hop events to implement the navigation hop service between phones and head units.

Super Home Screen:

-   This solution enables users to access their phone apps on the head unit of HIMA vehicles, thereby expanding the reach and richness of the HIMA ecosystem.
-   By integrating connectivity APIs of Car Kit for mobility services, your app can obtain the head unit screen information for UI display or use the head unit's camera for enhanced service interaction based on the Super Home Screen connection status.

## HiCar-Certified Vehicles

The HiCar interconnection solution is provided for users driving a HUAWEI HiCar-certified vehicle.

-   HiCar connects mobile devices and HiCar-certified vehicles, leveraging the software and hardware of both vehicles and devices, along with the multi-device interconnection capability, to deliver a smart mobility experience for users.
-   By integrating connectivity APIs of Car Kit for mobility services, your app can obtain the screen information of HiCar-certified vehicles for UI display or use the vehicle's camera for enhanced service interaction based on the HiCar connection status.

#### Implementation Principle

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/BSzeAsVGR1iD5biLhxZrSQ/en-us_image_0000002513566623.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35C851A0DD482C64BCB29887E05DB13045511164E85A1DD063029212D67E42C8 "Click to enlarge")

Located at the framework layer of HarmonyOS, Car Kit serves as a bridge between ecosystem apps and system apps.

1.  System apps subscribe to navigation data changes from Car Kit. When the navigation data of an ecosystem app changes, it notifies Car Kit of the change. Then, Car Kit forwards the change to system apps.
2.  Ecosystem apps subscribe to system events from Car Kit. When a system app wants an ecosystem app to execute a task, it notifies Car Kit. Then, Car Kit forwards the system event to the ecosystem app.
3.  Ecosystem apps subscribe to smart mobility connection status changes from Car Kit. When the smart mobility connection status changes, Car Kit forwards the current smart mobility connection status to ecosystem apps.

#### Restrictions

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Supported Devices

This kit is applicable only to phones.

## Supported Emulators

Currently, this kit does not support emulators.
