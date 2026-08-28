# Introduction to Mechanic Kit

Mechanic Kit is a set of APIs provided by mechanicManager. Starting from API version 20, applications can use Mechanic Kit to control mechanic devices. Mechanic Kit offers a complete integration solution for third-party mechanic devices, supporting interaction between mobile phones and devices such as gimbals.

Functions provided by Mechanic Kit include device connection management and object tracking, as well as status monitoring and precise control, helping developers to build high-quality device interaction applications.

Through Mechanic Kit, your applications can control and interact with mechanic devices, providing functions such as connection management, control, and monitoring.

#### When to Use

Mechanic Kit primarily targets interaction control scenarios involving mechanic devices such as gimbals.

-   **Object tracking**: Enable face tracking and object tracking through mechanic devices to enhance photography quality.
-   **Photographying control**: With mobile phones serving as control terminals, manipulate mechanic devices like gimbals for precise angle adjustment and motion trajectory control.

Mechanic Kit provides device connection, target tracking, and precise control functions, making it more convenient to build mechanic accessory control applications.

#### Capabilities

Mechanic Kit provides developers with comprehensive mechanic device control capabilities.

## Managing Device Connections

-   **Device discovery**: Obtain the list of currently connected mechanic devices, such as tripods.
-   **Connection status listening**: Listen for the connection status changes of mechanic devices in real time.
-   **Device information query**: Obtain basic information such as the ID, name, and type of mechanic devices.

## Object Tracking Control

-   **Camera tracking switch**: Enable or disable object tracking of the camera.
-   **Tracking layout setting**: Provide four tracking layout modes: default, left, center, and right.
-   **Tracking status listening**: Listen for events such as user operations and layout changes.

## Status Monitoring

-   **Current angle query**: Obtain the current angle of the mechanic device on three axes in real time.
-   **Rotation limit query**: Obtain the maximum rotation range of the mechanic device on each axis.
-   **Rotation axis status listening**: Listen for the enabling status change events and restriction of each rotation axis.
-   **Movement parameter query**: Obtain the maximum rotation speed and continuous rotation time.

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/vWY73blUTGS2SVrLFvzKuw/en-us_image_0000002568764839.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E90CCF635FADE8DD55A6C9C9E671C7F863AF6D827AE626E0C7D130D6CAB5DBA)

Note: Gray indicates that the feature is not supported.

**Object tracking mechanism**: After detecting a face, the camera driver reports the face to the camera service. The camera service reports the face location and camera parameters to the Mechanic Manager service. The Mechanic Manager service converts the information into a rotation instruction and delivers the instruction to the mechanic device via Bluetooth. The application can manage object tracking through open APIs.

#### Constraints

Before using Mechanic Kit, ensure that the following conditions are met:

-   **Mechanical device**: The mechanic device must comply with the Mechanic Kit specifications.
-   **Development device**: To support object tracking, the camera driver on the development device must have the face detection capability and support the reporting of face metadata, which complies with the HDI specifications.
-   **Device connection requirements**: The development device must be connected to the mechanic device to ensure that the communication link is normal.
-   **Camera permission**: An application in the foreground must obtain the camera permission to support visual functions such as object tracking.
-   **System permission**: Some advanced functions (such as rotation control) require system application permissions.
-   **Hardware restriction**: The operation range is limited by the movement limit of the mechanic device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/SQu8PLMERACvZ7MkhuCC5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84BF6863E89106CDF3D93C65741EDB931F87A415FF08B75FB37364F5CFC86A91)

Before calling the APIs of Mechanic Kit, make sure the preceding conditions are met. Otherwise, service exceptions may occur.
