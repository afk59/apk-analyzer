# Introduction to Variable Frame Rates

Nowadays, low-temperature polycrystalline oxide (LTPO) screens are widely used. This type of screen supports switching between frame rates at multiple levels.

For fast-changing content, such as shooting games and interactive animations, a high frame rate is required. It ensures smooth images while causing high power consumption.

For slow-changing content, such as game halls and clock update animations, a low frame rate is used. It consumes less power and does not cause frame freezing.

The variable frame rate capability enables you to achieve a balance between performance experience and power consumption on devices with the LTPO screens.

HarmonyOS supports this capability. You can use the variable frame rate APIs to develop related services.

#### Use Scenarios

The variable frame rate capability allows you to specify the frame rate in different scenarios. Typical use scenarios are as follows:

-   Configure the frame rate parameter for property animations or explicit animations. For details, see [Requesting Frame Rates for Animations](../requesting-frame-rates-for-animations/document.md).
-   Request an independent frame rate for UI components. For details, see [Requesting Frame Rates for UI Components](../requesting-frame-rates-for-ui-components/document.md).
-   Request an independent frame rate for custom content (such as gaming) through the **XComponent** on the native side. For details, see [Requesting Frame Rates for Custom Content](../requesting-frame-rates-for-custom-content/document.md).
-   Request an independent frame rate for drawing of non-UI threads through NativeVsync on the native side. For details, see [NativeDisplaySoloist Development (C/C++)](../native-displaysoloist-development-c-c/document.md).

#### Working Principles

The variable frame rate provides the basic frame rate configuration for animation components, **XComponent**, and UI components.

After a valid expected frame rate is set, the system collects the configured frame rate and divides the frequency on the rendering pipeline.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/BpgfTRabTcya3hn7q_hIKA/en-us_image_0000002568764921.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80804BE9DF100CD60AB2B98BA2CABCF767B14285C11A322B65570910DCCB9D64)

As illustrated above, different UI elements at the application layer (including animation components, UI drawing, XComponent for self-drawing, and non-UI thread drawing) can connect to the frame rate control system via specific variable frame rate APIs (such as **expectedFrameRateRange**, **displaySync**, **OH\_NativeXComponent\_SetExpectedFrameRateRange**, and **DisplaySoloist**). The frame control system collects the expected drawing frame rate set by the UI and participates in the decision-making of the entire system refresh rate at the framework layer. The server distributes the drawing frame rate based on the determined refresh rate result and transfers the drawing frame rate to various UIs at the application layer level by level. In addition, the hardware layer adjusts its refresh rate based on the overall decision to ensure synchronization.

#### Constraints

The actual frame rate may be different from the expected one configured. It is limited by the system power consumption and hardware capability of the screen refresh rate.
