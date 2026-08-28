# Clipboard Paste Box Blocked SmartFill Selection Box

**Problem**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/WU_huwa-S6uEbmT8rQ60Hg/en-us_image_0000002470492194.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8100FD36CC79CEF7F7BC87769E220EF2BC4CA8D2B83DB7FE13E4373D32846E27 "Click to enlarge")

**Solution**

Set **selectionMenuHidden** to **true** in the code to hide the clipboard.

      Row() { 
        Text('Recipient:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PERSON\_FULL\_NAME).selectionMenuHidden(true) 
      }
