# Recognizing the Target Shape

#### Overview

AR Engine supports this capability since version 5.0.0(12).

This section describes how to recognize the shape of a target object. Currently, rectangle and circle can be recognized.

#### Importing AR Engine

For details, please refer to [Importing AR Engine](../managing-ar-sessions/document.md#section1410827131110) in **Managing AR Sessions**.

#### Creating an AR Session

Create an AR session and set the target shape recognition mode.

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Set the semantic recognition mode to target shape recognition.
HMS\_AREngine\_ARConfig\_SetSemanticMode(arSession, arConfig, ARENGINE\_SEMANTIC\_MODE\_TARGET);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

#### Creating a Trackable Object List

Create a list of trackable objects (**targetList**) for storing all trackable objects detected when AR Engine is running.

AREngine\_ARTrackableList \*targetList = nullptr;
HMS\_AREngine\_ARTrackableList\_Create(arSession, &targetList);

#### Obtaining Trackable Objects in the Environment

Call [HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c) to detect all trackable objects in the current environment. The result is stored in **targetList**.

HMS\_AREngine\_ARSession\_GetAllTrackables(arSession, ARENGINE\_TRACKABLE\_TARGET, targetList);

#### Obtaining the Number of Trackable Objects

Call [HMS\_AREngine\_ARTrackableList\_GetSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9729d4436f3d969286f31b33d07513e) to obtain the number of trackable objects. The result is stored in **targetSize**.

int32\_t targetSize = 0;
HMS\_AREngine\_ARTrackableList\_GetSize(arSession, targetList, &targetSize);

**targetSize** = **0**: no trackable object in the current environment

**targetSize** = **1**: one trackable object in the current environment

**targetSize** > **1**: more than one trackable object in the current environment

#### Traversing and Recognizing Object Shapes

1.  When there is one or more trackable object in the environment, traverse **targetList** to recognize the shapes of these objects.
    
    for (int i = 0; i < targetSize; ++i) {
       // Traverse trackable objects to recognize their shapes.
    }
    
2.  Create and obtain the instance for the _i_th object.
    
    AREngine\_ARTrackable \*target = nullptr;
    HMS\_AREngine\_ARTrackableList\_AcquireItem(arSession, targetList, i, &target);
    
3.  Obtain the tracking status of the instance. Shape recognition is supported only when the tracking status is **ARENGINE\_TRACKING\_STATE\_TRACKING**.
    
    AREngine\_ARTrackingState outTrackingState;
    HMS\_AREngine\_ARTrackable\_GetTrackingState(arSession, target, &outTrackingState);
    
    if (AREngine\_ARTrackingState::ARENGINE\_TRACKING\_STATE\_TRACKING != outTrackingState) {
        continue;
    }
    
4.  Obtain the target shape of the instance, which is stored in the label.
    
    AREngine\_ARTargetShapeLabel label = ARENGINE\_TARGET\_SHAPE\_UNKNOWN;
    HMS\_AREngine\_ARTarget\_GetShapeType(arSession, reinterpret\_cast<AREngine\_ARTarget \*>(target), &label);
    
    [AREngine\_ARTargetShapeLabel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaed68dc13cc314da98d79c88b12d3ae49) is an enumeration type that describes the target object's shape.
    

#### Destroying the Trackable Object List

HMS\_AREngine\_ARTrackableList\_Destroy(targetList);
