# Integration Process

1.  **Enabling the digital product service**
    
    Complete basic preparations and fingerprint configuration by referring to [Application Development Preparations](../../../../getting-prepared/application-development-preparations/document.md) before proceeding with subsequent development activities. To call APIs of the digital product service, you need to [enable the digital product service](../enabling-the-digital-product-service/document.md), toggle on relevant API switches, and set service parameters.
    
2.  **Configuring digital products**
    
    You need to enter product information (including the product ID, product type, product price in different countries or regions, and product name) in advance. When your app calls the purchase API, only the configured product ID and product type need to be passed. Currently, you can configure the settings through [AppGallery Connect](../configuring-digital-products/configuring-digital-products-in-appgallery-connect/document.md) and [the Server API](../configuring-digital-products/configuring-digital-products-through-the-server-api/document.md).
    
3.  **Distributing digital products in your app**
    
    Currently, you can display and [distribute digital products](../distributing-digital-products-in-your-app/document.md) in your app. After you have configured digital products and integrated the digital product purchase capability, when a user initiates a purchase in your app, relevant APIs will be called. This will display the order page to show the product name and price. The user can then confirm and complete the transaction.
    
4.  **Testing the digital product service**
    
    You can use the sandbox testing service to test processes like digital product purchase without real payment. Before the test, you need to add test accounts in **Users and permissions** in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/). These test accounts must be real HUAWEI IDs. To access the IAP sandbox for testing, sign in on the test device using the test account first. For details, please refer to [Testing the Digital Product Service](../testing-the-digital-product-service/document.md).
