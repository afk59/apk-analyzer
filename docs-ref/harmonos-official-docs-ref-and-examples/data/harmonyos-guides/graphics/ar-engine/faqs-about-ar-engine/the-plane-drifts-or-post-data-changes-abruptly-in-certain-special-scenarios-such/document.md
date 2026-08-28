# The Plane Drifts or Post Data Changes Abruptly in Certain Special Scenarios (Such as When a Strong Magnetic Field Is Nearby, the Phone Is Overheated, or When Duplicate Textures Are Scanned)

#### Problem

In certain special scenarios, such as when a strong magnetic field is nearby, the phone is operating under heavy load (overheating due to multiple apps running in the background or prolonged use), or when duplicate textures (as shown in the figure below) are scanned by the phone, the identified plane may fail to anchor to the real world, or the pose information obtained via the [HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a) API may change abruptly.

**Figure 1** Floor with duplicate textures

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/9na_yhzGT3WoIlXxKBha1w/en-us_image_0000002500306264.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2B48E5EC5B5F756F8404ADBCF16335D0DCC0DDF2F385546FE63507E77638171 "Click to enlarge")

#### Possible Causes

AR Engine identifies planes and calculates the camera pose based on the accelerometer sensor and magnetometer sensor. However, the system sensor data may become abnormal in the special scenarios mentioned above. As a result, the plane may drift or post data may change abruptly.

#### Procedure

Filter the pose data obtained through the [HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a) API based on intended application scenarios. For instance, in walking navigation, you can cache multiple frames of data and calculate the motion speed from these frames. If the calculated speed is significantly higher than typical walking speed, the AR data is unreliable. In such cases, you can discard the data or restart the AR algorithm.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/8PU84Z5KQkG5yzQt6zqUkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0DFD34AE9B036AAB6B541A3C2B120646DE2C951D0DF89A39592E88FE18D2B49)

**Calculate the motion speed**: _x_, _y_, and _z_ refer to the translation of the pose data at time _t_.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/io4fzUFoRvS8nLU6Z26zpw/en-us_formulaimage_0000002532306155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E9514160BF1F1CADAD3841C96F8C86C80C80D5E43A7DC4DD0F6950BC8DAB074 "Click to enlarge")
