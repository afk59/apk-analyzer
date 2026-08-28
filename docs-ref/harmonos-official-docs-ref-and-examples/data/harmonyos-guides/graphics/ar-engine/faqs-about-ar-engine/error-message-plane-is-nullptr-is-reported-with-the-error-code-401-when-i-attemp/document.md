# Error Message "plane is nullptr!" Is Reported with the Error Code 401 When I Attempt to Obtain the 2D Vertex Coordinate Array of the Detected Plane

#### Problem

Error message "plane is nullptr!" is reported with the error code 401, when the developer attempts to obtain the 2D vertex coordinate array of the detected plane by calling [HMS\_AREngine\_ARPlane\_GetPolygonSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga98760556eee2a4a69c33699b7ce3edc6).

#### Possible Causes

When the app is started for the first time, no plane is identified, and calling [HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c) to obtain the list of trackable objects returns **NULL**. As a result, calling [HMS\_AREngine\_ARTrackableList\_AcquireItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab1782eeeeddc01b77a140af915cb351c) to obtain the object at a specified index also returns **NULL**. An invalid parameter error will occur if the developer uses the returned result without checking its validity.

#### Procedure

Check the validity of the plane obtained from AR Engine, for example, by performing a NOT NULL value check.
