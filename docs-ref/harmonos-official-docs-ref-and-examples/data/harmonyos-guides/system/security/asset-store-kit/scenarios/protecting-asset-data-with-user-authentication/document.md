# Protecting Asset Data with User Authentication

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/vIHZs5byRmy0PnMbZxvKwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98BE033AD87129CF7C7F5B71B88237B7ADF9DCFF1E38383D8A09E86516064C35)

The asset data mentioned in this topic refers to sensitive data, including passwords, app tokens, and other critical data (such as bank card numbers).

#### When to Use

Asset store service (ASSET) can be used in the scenario, in which users need to view their bank card numbers using a financial/banking application. To ensure security, you can store bank card numbers in an asset store and enforce a user identity authentication before the back card number is accessed.

When a user wants to view the bank card number, the application requests an identity authentication (for example, the user needs to enter a lock screen password or pass certain biometric authentication). When the identity authentication is successful, the application obtains the bank card number from ASSET and presents it to the user.

#### Development Process

The following figure illustrates the development process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/uySIKzzZTVG1ukJXnj9qLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C36BB6673A1D9ED2EDD25247E01E976840C52AD44E3DCB9516E22667BAF9BA4)

UserIAM provides only ArkTS APIs. Therefore, only ArkTS APIs can be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/tHYj8lnZTjuE9B3G_22LmA/en-us_image_0000002568684797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA34F346726E8ACE0C472B642E831C41B35664778533DCEB006884B648F408A6)

1.  The service queries an asset and determines whether the asset exists in the asset store based on the query result.
    
    -   For details about the development procedure, see [Querying Assets](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md). For details about the sample code, see [Querying Attributes of an Asset](../../asset-store-kit-development-arkts/querying-assets-arkts/document.md#querying-attributes-of-an-asset).
2.  If the asset does not exist:
    
    -   Add an asset. For details, see [Adding an Asset](../../asset-store-kit-development-arkts/adding-an-asset-arkts/document.md).
3.  If the asset exists, the service can perform any of the following operations based on service requirements:
    
    -   Remove the asset. For details, see [Removing Assets](../../asset-store-kit-development-arkts/removing-assets-arkts/document.md).
    -   Update the asset. For details, see [Updating an Asset](../../asset-store-kit-development-arkts/updating-an-asset-arkts/document.md).
    -   Query the plaintext of the asset. The query process involves preprocessing, user authentication, plaintext query, and postprocessing. For details, see [Querying an Asset with User Authentication](../../asset-store-kit-development-arkts/querying-an-asset-with-user-authentication-arkts/document.md).
