# Refunding

When [a user requests a refund](#section435204014114) from a non-game app, you can process this request in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Rq_rrLoMR6OpfiXuE_wP5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5B839034B06C35FA3699E3C2DA09CF6F3B337BAD70B5CD1FEDDC5A3F7467E36)

-   Refunds can only be initiated by users. For details, please refer to [Requesting a Refund](#section435204014114).
-   For a game app, [the refund request](#section435204014114) will be processed by Huawei game operations personnel. In this case, just skip this topic.

#### Processing a Refund Request

To use the refund management function, make sure that you have at least one of the following roles with the refund permission: account holder, administrator, app administrator, and finance. For details, please refer to [Adding a Member Account](https://developer.huawei.com/consumer/en/doc/app/agc-help-manageaccount-0000001099996700#section151241455193313).

After you have the refund permission, you can process a refund request as follows:

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Apps**. In the app list, click the app for which the refund request comes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/pdwYHoC5SKi3l_jDWyIVBg/en-us_image_0000002477594058.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF797177228323947CDA32E0BE893220511C11D0A2A53D229A9DA36EB3836053 "Click to enlarge")
    
2.  On the **Operate** tab, choose **Products** > **Refund Management**. Then, you can view the refund request.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/alyTFDcERSamEXzQx5A_Sw/en-us_image_0000002446733389.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=294E98FFD8D910D846C20582079D610DA2AEEAFAFDE415821BF4CBF921176F27 "Click to enlarge")
    
3.  Process the refund request.
    
    **Approve**: If you want to approve the refund request, input the amount in the **Refund amount** field and click **Approve**. In the confirmation dialog box, click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/wq5A6JYQTCadouXd9piqFA/en-us_image_0000002446613433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0E48717978390448A7E690A35C8DBAA81E91C859BFC9C810368F046BC0D9697 "Click to enlarge")
    
    **Reject**: If you want to reject the refund request, click **Reject**, input the reason for rejection, and click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/fXcXLOsYReOyYOaVjAepLg/en-us_image_0000002446733349.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EFC66ACCF4E375477F4E942A5DFBB52C8D230BD84A948A970ACC87CF7448639 "Click to enlarge")
    
    **View details**: You can also click **View details** to access the **Refund details** page. On this page, you can check the request details, specify **Refund amount** and **Review result** accordingly, and finally click **Submit**. (If you determine to reject a refund request, ignore **Refund amount**.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/oFFi42POSGCTFX99hs1SWw/en-us_image_0000002446613521.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AEF2449F7D974950DAD9A7A15DC3655CEF97DFD719A6491CC62EFC7AD9690CA "Click to enlarge")
    
    **Completed**: The refund request that has been processed will be moved to the **Completed** tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Ex56nhqNQmaUgP1kc9Qv_Q/en-us_image_0000002446613425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B257D8B83B03D3D31549DB797CAB6E360553AEE73D8AE6AB35532C1E182066C "Click to enlarge")
    
    Below lists the refund request statuses.
    
    <table><tbody><tr><td class="cellrowborder" valign="top" width="12.26%"><p><strong>No.</strong></p></td><td class="cellrowborder" valign="top" width="24.52%"><p><strong>Refund Request Status</strong></p></td><td class="cellrowborder" valign="top" width="63.22%"><p><strong>Description</strong></p></td></tr><tr><td class="cellrowborder" valign="top" width="12.26%"><p>1</p></td><td class="cellrowborder" valign="top" width="24.52%"><p>Rejected</p></td><td class="cellrowborder" valign="top" width="63.22%"><p>The refund request is rejected by you.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.26%"><p>2</p></td><td class="cellrowborder" valign="top" width="24.52%"><p>Approved</p></td><td class="cellrowborder" valign="top" width="63.22%"><p>The refund request is approved by you.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.26%"><p>3</p></td><td class="cellrowborder" valign="top" width="24.52%"><p>Refund successful</p></td><td class="cellrowborder" valign="top" width="63.22%"><p>The refund request is approved by you, and the refund process is already completed by Huawei.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.26%"><p>4</p></td><td class="cellrowborder" valign="top" width="24.52%"><p>Refund failed</p></td><td class="cellrowborder" valign="top" width="63.22%"><p>The refund request is approved by you, but the refund process fails to be completed by Huawei.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.26%"><p>5</p></td><td class="cellrowborder" valign="top" width="24.52%"><p>Overdue and unprocessed</p></td><td class="cellrowborder" valign="top" width="63.22%"><p>The refund request is not processed by you within the specified timeframe, and Huawei's operations team will process this request.</p></td></tr></tbody></table>
    

#### Requesting a Refund

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/NozqOnrDSQms9muj63YkcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C460A1CA124D9E691AF0E5E9F26C3C9368A43C1F42737C5DD8A2B18C2693D5D)

-   The refund function is available for both game and non-game apps on HarmonyOS 6.16.10 or later versions. (To check the HarmonyOS version, go to **Settings** > **HUAWEI ID** > **Payment & purchases** > **More settings** > **About**. The path may vary depending on the OS version.)
-   Refund processing is not immediate. In general, it takes about seven working days from the time a refund request is submitted to its completion.

Users who wish to request a refund for a purchased digital product can select the relevant order and follow the on-screen instructions to submit their request.

Here are step-by-step instructions:

1.  Go to **Settings**, access the **HUAWEI ID** screen, and tap **Payment & purchases**. On the **Purchase history** screen, tap the order for which a refund is needed. Then, on the **Details** screen, tap **Report issue**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/dWvnKxrCTjyCJrc5ZgQBhg/en-us_image_0000002446733405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05FB48D92D83A5724C09F9541FDF66368AD9A7F0AA89DD1CF354FF261E21E8FF "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/yU4dTyXyS8CpTFQJFrGDCg/en-us_image_0000002413174276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C64B661E3BDEAD24EB7AD47CC6F37F490B94387CD05D3CAEFFFA48CE872D914 "Click to enlarge")
    
2.  On the **Report issue** screen, tap **Request refund**, select a reason, and tap **Submit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9gLalwpjTXqDaMAT6Bkncg/en-us_image_0000002446733417.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E16528A9E8B5F62CE1E585D1C635396CB018F20F0581AD179345B489DE567698 "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/X1pRqCTSQMWmtdaZmm1Icw/en-us_image_0000002413014404.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E54B14407CA4998DE24D04B3C61B853573DA6E187FB3F75EA95C0C0DB5815832 "Click to enlarge")
    
    On the **Report issue** screen, tap **View refund records** to check the statuses of all refund requests.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/SPZF_za0QPq3shJumQgmmw/en-us_image_0000002446613461.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F48F14023A8836B72CA20D6D85967199FB3AA5C4B8379B1325C28B3DE156EEE "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/4xAe01pEQ9SXrtn1QlI3iQ/en-us_image_0000002413014376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF61553A40EC097E0C88B99D5E391FF336215C11A00284FAFF2AB68021FA74E9 "Click to enlarge")
    

#### Integrating the Refund API Within the App

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8YVmJuxERLuEFJ2Ybh2HGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD183478C18103F4BA2326D76AD003BCA2E614D0BBD59C6CB9A12426E37E15C3)

-   Only non-game apps are allowed to integrate the refund API.
-   The refund API is applicable to only the refund of orders generated by the app itself.

**Showing the Refund Screen**

After a user initiates a refund request, your app sends a [createRefundRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section3308191561314) request to IAP Kit to show the refund screen. The [createRefundRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/iap-iap#section3308191561314) request must contain the **purchaseOrderId** of the order to be refunded.

**Sample Code**

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  /\*\*
 \* Show the refund screen.
   \*/
  createRefundRequest(context: common.UIAbilityContext) {
  // Call **iap.createRefundRequest** to process the refund. Pass **context** and **purchaseOrderId** in the call request.
    let purchaseOrderId = '';
    iap.createRefundRequest(context, purchaseOrderId).then(() => {
    // Refund succeeded.
      console.info('Succeeded in create refund request.');
      // ...
    }).catch((err: BusinessError) => {
    // Refund failed.
      console.error(\`Failed to create refund request. Code is ${err.code}, message is ${err.message}\`);
      // ...
    });
  }

  build() {}
}
