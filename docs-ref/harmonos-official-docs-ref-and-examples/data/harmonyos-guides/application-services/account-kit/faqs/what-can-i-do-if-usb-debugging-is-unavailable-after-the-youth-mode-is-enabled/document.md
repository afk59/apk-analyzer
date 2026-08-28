# What can I do if USB debugging is unavailable after the youth mode is enabled?

When the youth mode is enabled, USB debugging on the device will be disabled. You can re-enable this function as follows: (1) Go to **Settings** > **System & updates** > **Developer options**; (2) Tap **USB debugging**; (3) Enter the parental control password as prompted. USB debugging will be enabled once the password verification is successful.

After USB debugging is enabled, if you find that the hilog in DevEco Studio is not restored to the state before the unavailability of USB debugging, run the **hdc shell hilog -G 16M** command to expand the hilog buffer. If the hilog still cannot be completely displayed, you can view the hilog locally. To learn more, please refer to [hilog](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hilog/document.md).
