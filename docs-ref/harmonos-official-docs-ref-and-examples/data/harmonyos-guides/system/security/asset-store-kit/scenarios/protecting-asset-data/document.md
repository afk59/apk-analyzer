# Protecting Asset Data

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xxmFlmBPQ7qlF_U28O_HGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA5087BC4834D47B5164F4B9D2D1E0EC987538F3834F714494FC7C947B8102B1)

The asset data mentioned in this topic refers to sensitive data less than 1024 bytes in size, including passwords, app tokens, and other critical data (such as bank card numbers).

#### When to Use

Asset store service (ASSET) is used in the logins of the users who select **Remember password** on the login page. The application/browser stores the user passwords in an asset store, which ensures the password security.

When a user opens the login page again, the application/browser obtains the user password from the asset store and automatically fills the password in the **Password** text box. The user only needs to tap the **Log In** button to complete the login.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/LAlDz9uPQhyV2JD_RpoKcw/en-us_image_0000002537765080.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1D3BCF9024DD37F8603CE34579D3F94ACE97B74B7BE1247370E2A85E40E07E9)

#### Development Process

The following figure illustrates the development process for the passwords (assets) protected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Cq45bJyAQJ-aN2a3PEbu1w/en-us_image_0000002537925020.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E349CC3379BAF121E007DEDFB6477A914C689BBD39C725B9AD17A05F5ADE4EFE)

1.  The service queries an asset and determines whether the asset exists in the asset store based on the query result.
    
    -   For details about the development procedure, see [Querying Assets (ArkTS)](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md)/[Querying Assets (C/C++)](../../asset-store-kit-development-c-c/querying-assets-c-c/document.md). For details about the sample code, see [Querying Attributes of an Asset (ArkTS)](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md#querying-attributes-of-an-asset)/[Querying Attributes of an Asset (C/C++)](../../asset-store-kit-development-c-c/querying-assets-c-c/document.md#querying-attributes-of-an-asset).
2.  If the asset does not exist:
    
    -   Add an asset. For details, see [Adding an Asset (ArkTS)](../../asset-store-kit-development-arkts/adding-an-asset-arkts/document.md)/[Adding an Asset (C/C++)](../../asset-store-kit-development-c-c/adding-an-asset-c-c/document.md).
3.  If the asset exists, the service can perform any of the following operations based on service requirements:
    
    -   Remove the asset. For details, see [Removing Assets (ArkTS)](../../asset-store-kit-development-arkts/removing-assets-arkts/document.md)/[Removing Assets (C/C++)](../../asset-store-kit-development-c-c/removing-assets-c-c/document.md).
    -   Update the asset. For details, see [Updating an Asset (ArkTS)](../../asset-store-kit-development-arkts/updating-an-asset-arkts/document.md)/[Updating an Asset (C/C++)](../../asset-store-kit-development-c-c/update-an-asset-c-c/document.md).
    -   Query the plaintext of the asset. For details, see [Querying Assets (ArkTS)](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md)/[Querying Assets (C/C++)](../../asset-store-kit-development-c-c/querying-assets-c-c/document.md). For details about the sample code, see [Querying the Plaintext of an Asset (ArkTS)](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md#querying-the-plaintext-of-an-asset)/[Querying the Plaintext of an Asset (C/C++)](../../asset-store-kit-development-c-c/querying-assets-c-c/document.md#querying-the-plaintext-of-an-asset).
