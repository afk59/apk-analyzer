# Managing Attribution Roles

App ecosystem partners need to register an attribution role and configure information, including the role, name, postback URL (URL for receiving the attribution result), and public key on the cloud platform of the app attribution service. The app attribution service platform generates an attribution role ID after the registration succeeds.

Before registering an attribution role, a key pair for signing/signature verification needs to be generated.

#### Enabling the Service Permission

Before registering an attribution role, you need to enable the AppGallery Kit permission. This feature is currently available by invitation only. If you are interested, please apply via the customer service email **developer@huawei.com**.

We will respond within 1–2 working days, so please check your email for updates. Provide necessary information based on the email template.

**Email template:**

**Email subject**: Request the AppGallery Kit app attribution service permission

**Email content**:

Developer ID: \*\*\*\*\*\*

Developer name: \*\*\*\*\*\*

App ID: \*\*\*\*\*\*

App name: \*\*\*\*\*\*

Request reason: \*\*\*\*\*\*\*

#### Generating a Key Pair

Use the relevant [HarmonyOS API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatesign) to generate a key pair for signing or signature verification. Or you can use a method of your choice to generate a key pair.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/k5SLdfcDT72E3DyzG8S6ow/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8619FC9E86C76986EFE920D7ABAED69A9BF4C61FB7F1606902C3D81AF44E112D)

Use the signing algorithm SHA256withRSA/PSS to generate a key pair of more than 3072 bits.

The generated private key is used to generate a signature. Please keep it secure. The generated public key will be provided for the app attribution service during role registration. Please make sure that the private key for signing and the public key for role registration are generated in a pair, thereby ensuring a successful signature verification.

#### Registering an Attribution Role

1.  Sign in to [HUAWEI Developers](https://developer.huawei.com/consumer/en/).
2.  Click **Console** in the upper right corner to go to the ecosystem service center.
3.  Go to **Ecosystem services** > **App services** > **Development** and click the **AG Service** card to access the cloud platform of the app attribution service.
4.  Click **Register** in the upper right corner. On the displayed **Registration information** page, enter the required information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/471v6YPcTWGWeVtvXaS6_g/en-us_image_0000002337734856.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC8FB41297640658D764B604F36615C95A04B3181FE34BC3052721D2502CBBAB "Click to enlarge")
    
    The related parameters are described as follows.
    
    | 
    Parameter
    
     | 
    
    **Description**
    
     |
    | :-- | :-- |
    | 
    
    Role
    
     | 
    
    Role of the app ecosystem partner: distribution platform, monitoring platform, or developer.
    
     |
    | 
    
    Name
    
     | 
    
    Name of the distribution platform, monitoring platform, or developer.
    
     |
    | 
    
    Public key
    
     | 
    
    Public key obtained in [Generating a Key Pair](#section1810151768). When [generating a signature](../../../appendix/standard-events-and-app-attribution-signatures/document.md#section5203225132112), use the private key paired with the public key and follow the [attribution source signature calculation rules](../../../appendix/standard-events-and-app-attribution-signatures/document.md#section4208115642013) stipulated by the app attribution service. Then the cloud platform of the app attribution service will use the public key to verify the signature.
    
     |
    | 
    
    Send to
    
     | 
    
    URL for receiving the attribution result returned by the app attribution service. HTTPS is recommended.
    
     |
    
5.  After completing the previous step, submit the configuration. A registration record with status of **Reviewing (new)** will be displayed. The operations team will review the registration record. Once approved, the registration is successful.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/5sIzwLApTgaGIdBRJ5WjHQ/en-us_image_0000002371652961.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=997179AEC3CD019658768786E87961337588A0F5E75B499C9549029A7DC4C2C3 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/IJhSIMYrSxe2XJISfr9eLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B35477DC23A142CA3B24B6FC1ADC50CD7447FFE6497602DC5F8DE079E5256B6)
    
    The status of **Reviewing (new)** signals that the registration is pending approval. In this state, editing or deleting the registration record is not allowed.
    
    When the status changes to **Effective**, the registration succeeds. In this state, editing or deleting the registration record can be done with no further review.
    
    If the status changes to **Rejected**, the registration fails. In this state, after editing the registration record, submit it to the operations team for review. Or you can delete the record without further review.
    
6.  After the registration is successful, the platform generates an attribution role ID (specified by **adTechId**), and the registration record will be displayed on the **Registration** page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/5iAwpRC0SD6joaT9OFqFEA/en-us_image_0000002371652953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36A9B15C1D79AA5C650D989F165D731B25E18142D8A1D282DC7FB42AB944CED0 "Click to enlarge")
