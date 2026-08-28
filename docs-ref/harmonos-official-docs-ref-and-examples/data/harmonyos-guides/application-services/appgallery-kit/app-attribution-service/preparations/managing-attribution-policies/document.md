# Managing Attribution Policies

Through attribution policy management, you can use the cloud platform of the app attribution service to maintain distribution platforms for attribution, set attribution priorities, configure attribution windows, and define attribution nodes. This enhances the flexibility and scalability of attribution capabilities, catering to diverse attribution needs.

**The developer role can perform the following operations on the attribution policy management page:**

Add, edit, view, and delete an attribution policy. An attribution policy takes effect immediately after being created and is valid for 24 hours.

Choose **Attribution policy management** on the left. On the displayed page, you can maintain attribution policies based on dimensions like promoted apps and conversion events. Each policy is specifically configured for a specific promoted app under your account.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/wJ2YlykHRvuoAnkUXizThA/en-us_image_0000002337894584.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=055BB5DB3AF274118E6F2E719F85C3321F37DA005FD5EA961AE2157CFC3DE7BB "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/RxMVGaq3QGy-96cAhYt4cw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6445C6E177E8FE920DB21B96EA87B4E0AFF3BB83E6A4844DC555D1458382D0B2)

Use the slider to enable or disable a record.

#### Adding an Attribution Policy

On the **Attribution policy management** page, click **New**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/N-DV6JvtTZCPe6rJkKjGnw/en-us_image_0000002337894580.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D11DF69E684C3D80D077882A49E6EFEDBE95C2C369D4D30939A256DD5D8F031 "Click to enlarge")

The related parameters are described as follows.

| 
Parameter

 | 

Description

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

Attribution policy name

 | 

Mandatory. Enter an attribution policy name in the text box. A maximum of 30 characters can be entered.

 | 

\_

 |
| 

Promoted app

 | 

Mandatory. Select one or more options.

Value range: names of all promoted apps registered under the attribution role.

The options include only HarmonyOS apps.

 | 

If there are multiple promoted apps, you can enter a keyword to search for the apps.

 |
| 

Conversion Events

 | 

Optional. You can select zero or multiple options.

Value range: all effective standard conversions, and effect custom conversion events under this promoted app.

 | 

You can use the search box to find conversion events by name and filter events by type.

 |
| 

Attribution window

 | 

Mandatory. Enter a number, based on the dimensions of promoted apps and conversion events.

Value range: (0,180\], in days. Default value: **7**.

 | 

\_

 |
| 

Post-activation attribution

 | 

Optional. Enable or disable this function.

 | 

\_

 |
| 

Post-activation attribution window

 | 

Mandatory. Enter a number. This parameter is visible only after **Post-activation attribution** is enabled.

Value range: (0,180\], in days. Default value: **7**.

 | 

\_

 |
| 

Attribution model

 | 

Mandatory. Select an option from the drop-down list box.

NOTE:

Currently, only **Last attribution** is supported.

 | 

\_

 |
| 

Attribution Priority

 | 

Attribution priority. The priorities of all distribution platforms are listed on the editing page. Edit the priority as needed.

Click **+** to add rows for configuring attribution priorities for different distribution platforms. Adjust the priority of selected platforms using the up and down arrows, or remove the current priority using the **x** button. Each priority level can be configured for multiple distribution platforms (no limit), but each distribution platform can only have one priority.

The priority values range from 1 to 10, matching the maximum number of distribution platforms, with smaller values indicating higher priority.

 | 

\_

 |
| 

Distribution Platform

 | 

Optional. Select zero or multiple options. By default, this parameter is left empty.

Value range: valid distribution platforms registered with the app attribution service.

 | 

Use the search box to filter results based on distribution platform names.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/QhuCp5IXS7CHY3PNo50vhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F78BC22F441789679DEB32AD49861A463E472D3D0A87C561E720A4C9BA54DAA1)

A maximum of 20 attribution policies can be created. That is, a maximum of 20 attribution policies can take effect at the same time.

#### Editing an Attribution Policy

On the attribution policy management page, click **Edit**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/AycGe3pjSpK2SWoat0BqiQ/en-us_image_0000002371732769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AAE9A97F535894C7E01CC7D8827B467D1D800D46E7FAA150C74EE0CC25CEBF7 "Click to enlarge")

After the editing is complete, click **OK** to make the modification take effect. If you click **Cancel**, the original record will remain unchanged.

#### Viewing an Attribution Policy

On the attribution policy management page, click **View**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/NhqSEznSQ_eR-TfEwWSGMQ/en-us_image_0000002371652913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA2F89F40359B415CCD8016ACAC674171A2F4178CC25510634AB5262266E2FB1 "Click to enlarge")

You can click **Edit** to go to the editing page, or click **Cancel** to close the current page and return to the list page.

#### Deleting an Attribution Policy

On the attribution policy management page, click **Delete**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/xmPDGpYuQVWHQpnIbvT9Ng/en-us_image_0000002371732773.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AAC65DE27D04829424CBE483DA2467E2FD6E0312C386FFEDE39E426543B94D8 "Click to enlarge")

If you click **OK**, the record will be marked as deleted. A deleted record can only be viewed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/3EBCEsY3Tb2QOLnssAes2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8244E2316C9692339812DE06F481CBB4DEFAD75B14F256CC90B8DD561AF0D64F)

Operations such as adding, editing, viewing, and deleting a record do not need to be approved. Successfully creating or editing a record will automatically enable it. Use the slider to enable or disable a record. Once a record is deleted, it will be marked as deleted.
