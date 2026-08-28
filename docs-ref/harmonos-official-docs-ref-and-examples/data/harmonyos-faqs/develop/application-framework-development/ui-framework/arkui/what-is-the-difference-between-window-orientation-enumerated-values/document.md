# What is the difference between window orientation enumerated values?

1.  When the window is set to values 8–10 or 12, it follows the sensor's automatic rotation and is controlled by the rotation switch in the Control Panel.
2.  When the window is set to values 13–16, it temporarily rotates to the specified direction (for example, 13 temporarily rotates to portrait), after which it follows the sensor's automatic rotation. It is still controlled by the rotation switch in the Control Panel, but the allowable rotation direction is determined by the system.

Differences: At values 13–16, the window will temporarily rotate to the specified direction and will retain that orientation during switching between the foreground and background. At values 8–10 or 12, the window will not retain the orientation during switching between the foreground and background.

**Scenarios**

1.  Hold the device vertically (portrait) with rotation lock turned off. -> Set the application orientation to **AUTO\_ROTATION\_RESTRICTED**. -> Rotate the device to landscape (application orientation: landscape). -> Move the application to the background by going to the home screen, while holding the device vertically (application orientation: portrait). -> Bring the application back to the foreground (application orientation: portrait).
2.  Hold the device vertically (portrait) with rotation lock turned off. -> Set the application orientation to **USER\_ROTATION\_PORTRAIT** (application orientation: portrait). -> Rotate the device to landscape (application orientation: landscape). -> Move the application to the background by going to the home screen, while holding the device vertically (application orientation: portrait). -> Bring the application back to the foreground (application orientation: landscape).

| 
Name

 | 

Value

 | 

Rotatable Direction

 | 

Follows Sensor Rotation

 | 

Controlled by Rotation Switch

 |
| :-- | :-- | :-- | :-- | :-- |
| 

AUTO\_ROTATION\_RESTRICTED

 | 

8

 | 

Landscape, portrait, reverse portrait, reverse landscape

 | 

Yes

 | 

Yes

 |
| 

AUTO\_ROTATION\_PORTRAIT\_RESTRICTED

 | 

9

 | 

Portrait, reverse portrait

 | 

Yes

 | 

Yes

 |
| 

AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED

 | 

10

 | 

Landscape, reverse landscape

 | 

Yes

 | 

Yes

 |
| 

AUTO\_ROTATION\_UNSPECIFIED

 | 

12

 | 

Determined by the system

 | 

Yes

 | 

Yes

 |
| 

USER\_ROTATION\_PORTRAIT

 | 

13

 | 

Determined by the system

 | 

Yes

 | 

Yes

 |
| 

USER\_ROTATION\_LANDSCAPE

 | 

14

 | 

Determined by the system

 | 

Yes

 | 

Yes

 |
| 

USER\_ROTATION\_PORTRAIT\_INVERTED

 | 

15

 | 

Determined by the system

 | 

Yes

 | 

Yes

 |
| 

USER\_ROTATION\_LANDSCAPE\_INVERTED

 | 

16

 | 

Determined by the system

 | 

Yes

 | 

Yes

 |
