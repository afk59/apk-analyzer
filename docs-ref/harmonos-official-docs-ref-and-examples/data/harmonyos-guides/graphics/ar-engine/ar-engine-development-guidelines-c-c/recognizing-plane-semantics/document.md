# Recognizing Plane Semantics

#### Overview

AR Engine supports this capability since version 5.0.0(12).

AR Engine allows you to recognize the semantics of a detected plane, which can be wall, floor, seat, table, ceiling, door, window, bed, plane space, cube volume, cube space volume, and unknown types. Specifically, the plane space, cube volume, and cube space volume types are supported only in high-precision geometric reconstruction mode.

#### Importing AR Engine

For details, please refer to [Importing AR Engine](../managing-ar-sessions/document.md#section1410827131110) in **Managing AR Sessions**.

#### Creating an AR Session

Create an AR session and set the plane semantic recognition mode.

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Set the semantic recognition mode to plane semantic recognition.
HMS\_AREngine\_ARConfig\_SetSemanticMode(arSession, arConfig, ARENGINE\_SEMANTIC\_MODE\_PLANE);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

#### Detecting Planes in the Environment

Detect planes in the environment by referring to [Detecting Planes in the Environment](../detecting-planes-in-the-environment/document.md), obtain the number of planes in the environment, and then recognize plane semantics. If at least one plane is detected, proceed with the following steps.

#### Initializing Plane Semantic Labels

Create and initialize labels to describe the plane semantics.

AREngine\_ARSemanticPlaneLabel label = ARENGINE\_PLANE\_UNKNOWN;

The plane semantic labels are defined as an enumeration type, including 12 enumerated values (1 unknown type + 11 plane types).

typedef enum {
    /\*\* Unknown type. \*/
    ARENGINE\_PLANE\_UNKNOWN = 0,
    /\*\* Wall. \*/
    ARENGINE\_PLANE\_WALL = 1,
    /\*\* Floor. \*/
    ARENGINE\_PLANE\_FLOOR = 2,
    /\*\* Seat. \*/
    ARENGINE\_PLANE\_SEAT = 3,
    /\*\* Table. \*/
    ARENGINE\_PLANE\_TABLE = 4,
    /\*\* Ceiling. \*/
    ARENGINE\_PLANE\_CEILING = 5,
    /\*\* Door. \*/
    ARENGINE\_PLANE\_DOOR = 6,
    /\*\* Window. \*/
    ARENGINE\_PLANE\_WINDOW = 7,
    /\*\* Bed. \*/
    ARENGINE\_PLANE\_BED = 8,
    /\*\* Plane Space. \*/
    ARENGINE\_PLANE\_SPACE = 9,
    /\*\* Cube Volume. \*/
    ARENGINE\_CUBE\_VOLUME = 10,
    /\*\* Cube Space. \*/
    ARENGINE\_CUBE\_SPACE = 11,
} AREngine\_ARSemanticPlaneLabel;

#### Recognizing the Plane Type

Call [HMS\_AREngine\_ARPlane\_GetLabel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga913456f9586c82adcdbcae291ec8e17c) to obtain the plane type. The result is stored in the label. You can refer to [Obtaining a Plane Instance](../detecting-planes-in-the-environment/document.md#section4891238142419) for details.

HMS\_AREngine\_ARPlane\_GetLabel(arSession, arPlane, &label);
