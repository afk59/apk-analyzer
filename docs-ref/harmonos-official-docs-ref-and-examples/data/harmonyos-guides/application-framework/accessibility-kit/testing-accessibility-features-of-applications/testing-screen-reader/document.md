# Testing Screen Reader

Screen Reader enables users to interact with their devices without viewing the screen. Visually impaired users may rely on Screen Reader for a more convenient operation experience.

After the development of the Screen Reader feature is complete, you can verify the feature as follows.

#### Enabling Operation Verification

This operation is a prerequisite for using the Screen Reader feature, which allows you to check whether the feature is enabled or not.

## Enabling Screen Reader in General Mode

1.  Open **Settings** on your device.
2.  Touch **Accessibility**.
3.  Touch **Screen Reader**.
4.  Enable **Screen Reader**.
5.  In the security alert dialog box, check the box indicating that you understand the risks, and enable Screen Reader.

## Enabling Screen Reader in Shortcut Mode

In addition to common methods, shortcut keys are provided to help users quickly enable or disable Screen Reader.

1.  Open **Settings** on your device.
2.  Touch **Accessibility**.
3.  Touch **Accessibility shortcut**.
4.  Enable **Accessibility shortcut**, select **Screen Reader**, and enable the shortcut key to work when the screen is locked.
5.  Long press the volume up and volume down buttons for 3 seconds to check whether Screen Reader can be enabled or disabled in shortcut mode.

#### Verifying Screen Reading Effect

After Screen Reader is enabled, you can navigate in the following ways:

-   Navigation by touch: The Screen Reader announces the content where the user touches.
-   Linear navigation: The Screen Reader announces the focused content in a linear manner, from top to bottom, when the user swipes on the screen to move the focus.

## Common Gestures

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/pwrqstCbS1G4FaV_brsf9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061919Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAC5AF2A72D4D69614FD56D21406DA02E2040C7C876A19D6D8ECB09EED1E8969)

The following lists the common gestures and corresponding operations of Screen Reader. You can view and set more gestures by going to **Settings** > **Accessibility** > **Screen Reader** > **More settings** > **Custom gestures**.

**Table 1** Basic gestures
| 
Action

 | 

Gesture

 |
| :-- | :-- |
| 

Move to the next item on the screen

 | 

Swipe right or down

 |
| 

Move to the previous item on the screen

 | 

Swipe left or up

 |
| 

Tap/Select the current item

 | 

Tap twice

 |
| 

Long press

 | 

Tap twice, then long press

 |
| 

Swipe horizontally

 | 

Swipe with two fingers

 |

**Table 2** Reciprocating gestures
| 
Action

 | 

Gesture

 |
| :-- | :-- |
| 

Navigate to the previous setting

 | 

Swipe up, then down

 |
| 

Navigate to the next setting

 | 

Swipe down, then up

 |
| 

Scroll down (backward) a page

 | 

Swipe right, then left

 |
| 

Scroll up (forward) a page

 | 

Swipe left, then right

 |

**Table 3** Angle gestures
| 
Action

 | 

Gesture

 |
| :-- | :-- |
| 

Open the home screen

 | 

Swipe up, then left

 |
| 

Back

 | 

Swipe down, then left

 |
| 

Open the notification panel

 | 

Swipe up, then right

 |
| 

Open a recently used application

 | 

Swipe down, then right

 |
| 

Open the shortcut menu

 | 

Swipe right, then down

 |
| 

Open the Control Panel

 | 

Swipe left, then down

 |
| 

Perform operations in the edit box

 | 

Swipe left, then up

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/4L2K_eUHSHifKe3LN9Lk0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061919Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5941DA2AFDFAE50D0E634DE17839260AEB7B69C1C3D755CB87C9787B3D8C30C5)

To use Screen Reader more conveniently, go to **Settings** > **Accessibility features** > **ScreenReader** > **More settings** to set more options (such as speed and pitch).

## Using Screen Reader to Browse an Application

After adapting the application to Screen Reader, you can perform the following steps to verify whether the reading function is correctly implemented.

1.  Launch an application.
2.  Swipe through the elements in sequence.
    
    During the browsing, pay attention to the following:
    
    -   Whether the voice feedback of each element properly conveys the content or usage
    -   Whether you can complete the main workflows easily
    -   Whether you can swipe through each element
    -   Whether Screen Reader can read the alerts or other temporary messages
    
3.  Rectify the adaptation issues by referring to the development guide.
