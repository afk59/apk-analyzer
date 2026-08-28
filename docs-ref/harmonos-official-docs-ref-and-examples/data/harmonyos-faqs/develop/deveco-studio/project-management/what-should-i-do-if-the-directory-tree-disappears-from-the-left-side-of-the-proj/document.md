# What should I do if the directory tree disappears from the left side of the project view?

**Symptom**

The **.idea/modules** folder, which should be present in the project directory as shown below, has been deleted or is missing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/oaoPZH9CQz2SqP7o9S6R3g/en-us_image_0000002229758589.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BD06FA1FEF28959FE412998D8D06AAAA65AAF030BF496B085F0EADAFB724C9D)

After the project is reopened, the directory tree is not displayed on the left side of the project view, as shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/siTxSahTTkarUd4n4_TpLQ/en-us_image_0000002194318328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73B18F20158EC3DD879077E8BA20D540604AF517F352AB5B18D2726017F95439)

**Possible Causes**

The .iml file in the **modules** folder defines the module structure information of the project, and the **modules.xml** file specifies the location of the module structure file. When the **modules** folder is not present, the corresponding .iml file cannot be found.

**Solution**

To restore the project directory tree, close the project, delete the **modules.xml** file using the file manager, and then open the project again in DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0D8AsIqgS4-ireAoGZxwdw/en-us_image_0000002194158720.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADC293EE44343E269B1A287BBDFC6EA51406BB5367A8BD13FBD8448B5C3BCD0E)
