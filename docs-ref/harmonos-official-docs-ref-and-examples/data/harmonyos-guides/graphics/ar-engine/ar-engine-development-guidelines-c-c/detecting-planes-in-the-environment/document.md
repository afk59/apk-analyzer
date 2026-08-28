# Detecting Planes in the Environment

#### Overview

AR Engine supports this capability since version 5.0.0(12).

This section describes how to use AR Engine to detect planes in an environment and process the detected planes in apps.

#### Importing AR Engine

For details, please refer to [Importing AR Engine](../managing-ar-sessions/document.md#section1410827131110) in **Managing AR Sessions**.

#### Creating an AR Session

Create an AR session by referring to [Managing AR Sessions](../managing-ar-sessions/document.md).

#### Creating a Plane Object List

1.  Create a plane object list (**planeList**) to store all planes detected when AR Engine is running.
    
    AREngine\_ARTrackableList \*planeList = nullptr;
    HMS\_AREngine\_ARTrackableList\_Create(arSession, &planeList);
    
2.  Set the type of trackable objects to **ARENGINE\_TRACKABLE\_PLANE**.
    
    AREngine\_ARTrackableType planeTrackedType = ARENGINE\_TRACKABLE\_PLANE;
    

#### Recognizing Planes in the Current Environment

Call [HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c) to detect all planes in the current environment. The result is stored in **planeList**.

HMS\_AREngine\_ARSession\_GetAllTrackables(arSession, planeTrackedType, planeList);

#### Obtaining the Number of Planes

Call [HMS\_AREngine\_ARTrackableList\_GetSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9729d4436f3d969286f31b33d07513e) to obtain the number of planes. The result is stored in **planeListSize**.

int32\_t planeListSize = 0;
HMS\_AREngine\_ARTrackableList\_GetSize(arSession, planeList, &planeListSize);

In the app environment, there may be zero, one, or more planes.

**planeListSize** = **0**: no plane in the current environment

**planeListSize** = **1**: one plane in the current environment

**planeListSize** > **1**: more than one plane in the current environment

#### Obtaining a Plane Instance

When one or more planes are detected, traversing **planeList** can obtain all plane objects.

for (int i = 0; i < planeListSize; ++i) {
    // Traverse all plane objects and process them as required.
}

Create and obtain a trackable object for the _i_th plane, and convert it into a plane object [AREngine\_ARPlane](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga76f9bdb23634312b8488fcbaff4aa9b5).

AREngine\_ARTrackable \*arTrackable = nullptr;
HMS\_AREngine\_ARTrackableList\_AcquireItem(arSession, planeList, i, &arTrackable);
AREngine\_ARPlane \*arPlane = reinterpret\_cast<AREngine\_ARPlane\*>(arTrackable);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fj84VVybQtm4tK_QF4qRkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3EAD43E86C72278610E73779DD95B665EB81A03A5C72A3313FB06C315CFC8BE)

In AR Engine, any object is defined as a trackable object [AREngine\_ARTrackable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga54808ebd1a6ed026494acdd945c4f970). A plane is also a trackable object. **reinterpret\_cast** can be used to convert a trackable object [AREngine\_ARTrackable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga54808ebd1a6ed026494acdd945c4f970) to a plane object [AREngine\_ARPlane](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga76f9bdb23634312b8488fcbaff4aa9b5).

#### Destroying the Plane Object List

HMS\_AREngine\_ARTrackableList\_Destroy(planeList);
