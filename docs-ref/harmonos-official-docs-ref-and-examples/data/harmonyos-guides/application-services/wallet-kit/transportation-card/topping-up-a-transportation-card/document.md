# Topping Up a Transportation Card

The transportation card top-up process consists of three steps: card display, top-up order generation and payment, and top-up initiation. For details about the relevant APIs, please refer to [walletTransitCard (Transportation Card Capability)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/m6ZjCfGnRQO9NpFQ0_qT2g/en-us_image_0000002218367305.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=793E5E4801DEDFF3B4B9E484FC172595E4517ACF1DAF925B2778BC5E683BCCD9 "Click to enlarge")

-   After your app is started, it calls the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API to obtain the information about transportation cards that can be accessed by the app on a specified device. The result is returned in an array. If the returned array is empty, your app does not have any accessible transportation cards on this device and does not need to display the card activation entry. If the returned array is not empty, your app displays a proper page based on the actual transportation card information. If the transportation card information includes the card number and balance, the card has been activated, and your app can directly display the transportation card information. Otherwise, your app can display the card activation entry.
-   When a user requests to top up a transportation card, your app sends a top-up order generation request to your server and asks the user to complete the payment.
-   After confirming that the order has been paid, your app calls the [rechargeTransitCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section17143122485417) API to top up the order amount to the card. If the top-up is successful, your app receives a return value indicating top-up success and containing the new balance. If the top-up fails at first and still fails after HUAWEI Wallet initiates a retry, HUAWEI Wallet initiates a refund request. After the SP TSM system or your server confirms that the order is refundable, the SP TSM system or your server calls the order cancellation API of the corresponding payment channel to return the order amount to the original account. In this case, your app receives an error code indicating top-up failure. For details, please refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code).

#### Development Procedure

1.  Obtain the list of activated transportation cards on a device.
    
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
    
2.  Top up the transportation card.
    
    import { common } from '@kit.AbilityKit';
    import { walletTransitCard } from '@kit.WalletKit'
    import { BusinessError } from '@kit.BasicServicesKit';
    
    transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');
    
    async rechargeTransitCard() {
      // Number of the activated transportation card, returned by the [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115) API in step 1.
      const logicalCardNumber = 'logicalCardNumber';
      // The value of **specifiedDeviceId** is returned by [getCardMetadataInDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-wallettransitcard#section3931434195115).
      const specifiedDeviceId = 'specifiedDeviceId';
      // Order ID generated in your app after payment, which is implemented by you.
      const serverOrderId = 'serverOrderId';
      this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then((result) => {
        console.info(\`Succeeded in recharging TransitCard\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to recharge TransitCard, code:${err.code}, message:${err.message}\`);
      })
    }
