# What should I do if "The reason and usedScene attributes are mandatory for user\_grant permissions" is reported during compilation?

**Symptom**

DevEco Studio compilation fails and "The reason and usedScene attributes are mandatory for user\_grant permissions" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/enm5Sf9zQZOWD192K1l75w/en-us_image_0000002194158568.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDF877DE435B4A0413C0BE821191FA7B3ED908E99564724BEEC840ED6D7825C2 "Click to enlarge")

**Possible Causes**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule is added: In an application package, the permission list **requestPermissions** under the module of all **Entry.hap** and **Feature.hap** must be specified. (**requestPermissions** can be left empty. If it is not empty, the **name** field is mandatory. For the **user\_grant** permissions, the **reason** and **usedScene** fields are mandatory.)

**Solution**

Open the corresponding **module.json5** file and supplement the **reason** and **usedScene** fields under **requestPermissions**. Example:

"requestPermissions": \[
  {
    "name": "ohos.permission.READ\_IMAGEVIDEO",
    "reason": "$string:module\_desc",
    "usedScene": {
      "abilities": \[
        "EntryAbility"
      \],
      "when": "inuse"
    }
  }
\],
