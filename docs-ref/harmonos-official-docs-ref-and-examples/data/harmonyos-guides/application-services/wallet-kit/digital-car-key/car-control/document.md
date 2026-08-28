# Car Control

After a digital car key is enabled, the car owner app can remotely unlock the car and perform other operations through car control commands.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/9SYn_NQhSVmBo-x_Oaqavg/en-us_image_0000002218521713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A9D988803B27339FE41C9B755AC8764A3B243A58823ECE76C92C753BADA5C50)

The typical service process is as follows:

-   The car owner app calls the [queryICCEConnectionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section82336268523) API to check the Bluetooth connection status of the car control system. If the Bluetooth connection is not set up, the car owner app calls [startICCEConnection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section137818297525) to set up the connection.
-   The car owner app calls [registerICCEListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section287123205213) to register a listener for messages sent from HUAWEI Wallet.
-   The car owner app calls the [sendICCERKEMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section73091546144716) API to send a car control command.
-   When the user exits the digital key car control page, the car owner app calls the [unregisterICCEListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section692193414523) API to unregister the listener.

#### Development Procedure

1.  Make the car owner app call the [queryICCEConnectionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section82336268523) API to check the Bluetooth connection status of the car key based on the service ID registered in [applying for Wallet Kit](../../applying-for-wallet-kit/document.md) and the unique pass ID defined in [applying for the key card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    private serialNumber: string = ''; 
    
    async queryICCEConnectionState() {
      let passStr = JSON.stringify({
        passType: this.passType,
        serialNumber: this.serialNumber
      });
      this.walletPassClient.queryICCEConnectionState(passStr).then((result: string) => {
        console.info(\`Succeeded in querying ICCEConnectionState, result: ${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to query ICCEConnectionState, code:${err.code}, message:${err.message}\`);
      })
    }
    
2.  If the value of **connectionState** returned by the [queryICCEConnectionState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section82336268523) API is **0** (not paired), call [startICCEConnection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section137818297525) to set up a Bluetooth connection.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    private serialNumber: string = ''; 
    
    async startICCEConnection() {
      let passStr = JSON.stringify({
        passType: this.passType,
        serialNumber: this.serialNumber
      });
      this.walletPassClient.startICCEConnection(passStr).then((result: string) => {
        console.info(\`Succeeded in starting ICCEConnection, result: ${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to start ICCEConnection, code:${err.code}, message:${err.message}\`);
      })
    }
    
3.  Make the car owner app call [registerICCEListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section287123205213) to register a listener for messages sent from HUAWEI Wallet.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { rpc } from '@kit.IPCKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    private callback: rpc.RemoteObject | null = null;
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Name of the app for which the listener needs to be registered, which is usually the app package name.
    private registerName: string = '';  
    
    async registerICCEListener() {
      let passStr = JSON.stringify({
         passType: this.passType,
         registerName: this.registerName
      });
      this.callback = new ICCECallBack();
      this.walletPassClient.registerICCEListener(passStr, this.callback).then((result: string) => {
        console.info(\`Succeeded in registering ICCEListener, result: ${result}\`);
       }).catch((err: BusinessError) => {
        console.error(\`Failed to register ICCEListener, code:${err.code}, message:${err.message}\`);
      })
    }
    
    class ICCECallBack extends rpc.RemoteObject {
      constructor() {
        super('ICCECallBack');
      }
    
      async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
    // Match data information based on the code.
        let codeInt = data.readInt();
        return true;
      }
    }
    
4.  Make the car owner app call the [sendICCERKEMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section73091546144716) API to send a car control command.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = '';  
    // Unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    private serialNumber: string = ''; 
    // Car control command.
    private rkeCommand: string = '';  
    
    async sendICCERKEMessage() {
      let passStr = JSON.stringify({
        passType: this.passType,
        serialNumber: this.serialNumber,
        rkeCommand: this.rkeCommand,
        encryptFlag: '0',
        directionFlag: '1'
      });
      this.walletPassClient.sendICCERKEMessage(passStr).then((result: string) => {
        console.info(\`Succeeded in sending ICCERKEMessage, result: ${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to send ICCERKEMessage, code:${err.code}, message:${err.message}\`);
      })
    }
    
5.  Exit the digital key car control page, and make the car owner app call the [unregisterICCEListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section692193414523) API to unregister the listener.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    private callback: rpc.RemoteObject | null = null;
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Name of the app for which the listener is registered, which is usually the app package name.
    private registerName: string = ''; 
    
    async unregisterICCEListener() {
      let passStr = JSON.stringify({
        passType: this.passType,
        registerName: this.registerName
      });
    
      this.walletPassClient.unregisterICCEListener(passStr).then((result: string) => {
        console.info(\`Succeeded in unregistering ICCEListener, result: ${result}\`);
        this.callback = null;
      }).catch((err: BusinessError) => {
        console.error(\`Failed to unregister ICCEListener, code:${err.code}, message:${err.message}\`);
      })
    }
