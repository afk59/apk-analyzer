# How do I check whether the current network is accessible?

You can use the APIs provided by **@ohos.net.connection** to check whether a network is accessible. Each time the network connection status changes, the system checks whether the current network is accessible and stores the check result in AppStorage. You can then directly obtain the result from AppStorage. The code snippet is as follows:

import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct NetJudge {
  public static netConnection: connection.NetConnection | undefined = undefined;
  private static JUDGE\_NET\_TAG: string = 'NetJudge.currNet.isUseful';

  init() {
    NetJudge.netConnection = connection.createNetConnection();
    NetJudge.netConnection.register(() => {
      console.info('connection register success');
    });

    NetJudge.netConnection.on('netAvailable', (data) => {
      console.info('NetJudge  netAvailable ');
      AppStorage.setOrCreate(NetJudge.JUDGE\_NET\_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netUnavailable', () => {
      console.info('NetJudge  netUnavailable ');
      AppStorage.setOrCreate(NetJudge.JUDGE\_NET\_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
      AppStorage.setOrCreate(NetJudge.JUDGE\_NET\_TAG, this.judgeHasNet());
    });

    // Subscribe to network connection information change events. You can only receive this event notification after calling register
    NetJudge.netConnection.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
      AppStorage.setOrCreate(NetJudge.JUDGE\_NET\_TAG, this.judgeHasNet());
    });

    NetJudge.netConnection.on('netLost', () => {
      AppStorage.setOrCreate(NetJudge.JUDGE\_NET\_TAG, this.judgeHasNet());
    });
  }

  regist() {
    if (NetJudge.netConnection === undefined) {
      this.init();
    }
  }

  judgeHasNet(): boolean {
    try { // Get current network connection
      let netHandle = connection.getDefaultNetSync();

      // 0-100 Reserved connections for the system
      if (!netHandle || netHandle.netId < 100) {
        return false;
      }

      // Get the properties of the connection
      let netCapability = connection.getNetCapabilitiesSync(netHandle);
      let cap = netCapability.networkCap;
      if (!cap) {
        return false;
      }

      for (let em of cap) {
        if (connection.NetCap.NET\_CAPABILITY\_VALIDATED === em) {
          return true;
        }
      }
    } catch (e) {
      let err = e as BusinessError;
      console.info('get netInfo error : ' + JSON.stringify(err));
    }
    return false;
  }

  build() {
    Column({ space: 10 }) {
      Button('Check Network Accessibility')
        .onClick(() => {
          this.regist();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
