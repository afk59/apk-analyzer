# Activating a Transportation Card

The transportation card activation process consists of four steps: obtaining the card activation entry, checking whether a card can be added, generating and paying an order, and adding the card. For details about the relevant APIs, please refer to [ArkTS API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-arkts).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-Mg3BKGCTW2Ue0yP48L4mw/en-us_image_0000002182921498.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40EBD603D5DCB3C54AB499200A382014DD6CE26D8C745A34D3F63579EFC309BB "Click to enlarge")

-   After your app is started, it calls the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API to obtain the information about transportation cards that can be accessed by the app on a specified device. The result is returned in an array. If the returned array is empty, your app does not have any accessible transportation cards on this device and does not need to display the card activation entry. If the returned array is not empty, your app displays a proper page based on the actual transportation card information. If the transportation card information includes the card number and balance, the card has been activated, and your app can directly display the transportation card information. Otherwise, your app can display the card activation entry.
-   When a user requests to activate a transportation card, your app calls the [canAddTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section842743618139) API to pass the issuer ID and device ID. HUAWEI Wallet checks whether the card activation conditions are met on this device. If the conditions are not met, HUAWEI Wallet returns an error code (see [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code) for details) and displays the error message to the user. If the conditions are met, HUAWEI Wallet returns the card activation credential data (**addCardOpaqueData**).
-   After obtaining **addCardOpaqueData**, your app submits it together with the card activation and first top-up information to your server to generate an order for card activation and first top-up. Please note that **addCardOpaqueData** needs to be associated with the order for storage. Your server submits the order to the payment service provider. After the user completes the payment, your server receives a payment completion notification from the payment service provider. Then your server delivers the order data of card activation and first top-up, including **addCardOpaqueData**, to the SP TSM server of the card issuing company.
-   After confirming that the order is paid, your app calls the [addTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section1973893821320) API to pass **addCardOpaqueData** and **serverOrderId** to activate the card. The user will be redirected to the HUAWEI Wallet page to complete card activation. After the card is activated successfully, your app page will be displayed containing the basic card data, including the card number and balance information. If a failure occurs during card activation, HUAWEI Wallet automatically retries. If the retry fails, HUAWEI Wallet automatically initiates a rollback to apply for a refund.

#### Development Procedure

1.  Obtain the list of transportation cards that can be activated on a device.
    
    During **TransitCardClient** initialization, the second input parameter **callerId** of the construction method is the ID of the API caller. You can contact the Wallet Kit operations personnel to obtain the caller ID when applying for the transportation card service.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async getCardMetadataInDevice() {
      this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE\_PHONE).then((result) => {
        console.info(\`Succeeded in getting cardMetadataInDevice\`);
        // Display the transportation card list.
      }).catch((err: BusinessError) => {
        console.error(\`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}\`);
      })
    }
    
2.  Obtain **addCardOpaqueData** for card activation.
    
    Select a transportation card and call the [canAddTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section842743618139) API to obtain **addCardOpaqueData** for card activation.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async canAddTransitCard() {
      // The value of **issuerId** must be the data returned by [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115).
      const issuerId = 'issuerId';
      // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115).
      const specifiedDeviceId = 'specifiedDeviceId';
      this.transitCardClient.canAddTransitCard(issuerId, specifiedDeviceId).then((result) => {
        console.info(\`Succeeded in canning AddTransitCard\`);
        // Save the result as the input parameter **addCardOpaqueData** of [addTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section1973893821320).
      }).catch((err: BusinessError) => {
        console.error(\`Failed to can AddTransitCard, code:${err.code}, message:${err.message}\`);
      })
    }
    
3.  Activate the transportation card.
    
    Use **addCardOpaqueData** obtained in step 2 to call the [addTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section1973893821320) API to activate the transportation card.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async addTransitCard() {
      // Order ID generated in your app after payment, which is implemented by you.
      let serverOrderId = 'serverOrderId';
      // **addCardOpaqueData** obtained in step 2.
      let addCardOpaqueData = 'addCardOpaqueData';
      this.transitCardClient.addTransitCard(addCardOpaqueData, serverOrderId).then((result) => {
        console.info(\`Succeeded in adding TransitCard\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to add TransitCard, code:${err.code}, message:${err.message}\`);
      })
    }
