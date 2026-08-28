# What should I do if application performance deteriorates after stability stress testing?

**Symptom**

After stability stress tests are conducted with DevEco Testing, performance testing reveals a degradation in performance.

**Possible Causes**

By default, DevEco Testing turns on the multi-threading switch for stability stress tests and turns it off once the tests are completed. However, the switch may fail to be turned off sometimes. While the switch is intended to help identify multi-threading safety issues, it can negatively affect performance.

**Solution**

Run the following command to disable multi-threading:

hdc shell param set persist.ark.properties 0x105c
hdc shell reboot
