# Using an EL5 Database (ArkTS)

#### When to Use

To meet the security requirements of sensitive data, the EL5 database is provided to improve the data security when the screen is locked. An application that contains sensitive information creates a database in the [EL5](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode) directory after requesting the **ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA** permission. If the screen is locked (and the **Access** API is not called to obtain the key of the reserved file), the file key will be destroyed, and the database cannot be read or written. After the screen is unlocked, the key is restored and the read and write operations on the database are restored. This mechanism can effectively protect user data.

An application can continue to write data even if the screen is locked, which may lead to data loss. A solution is provided to solve this problem. When the screen is locked, incremental data is stored in an [EL2](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode) database. The data temporarily stored in the EL2 database will be moved to the EL5 database when the EL5 database is unlocked. This ensures data security and integrity when the screen is locked.

Both the KV store and RDB store can be used as an EL5 database.

#### Working Principles

The following classes are encapsulated to implement the data operations and transfer between EL2 and EL5 databases:

**Mover** class: provides APIs for moving data from an EL2 database to an EL5 database after the screen is unlocked.

**Store** class: provides APIs for obtaining a database instance, adding, deleting, and updating data, and obtaining the data count in the database.

**SecretKeyObserver** class: provides APIs for obtaining the key status. After the key is destroyed, the EL5 database will be closed.

**ECStoreManager** class: provides APIs for managing the EL2 and EL5 databases.

#### Requesting Permissions

To access the database in the **el5/** directory, the application must have the **ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA** permission. Add this permission in the **module.json5** file.

// module.json5
"requestPermissions": \[
      {
        "name": "ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA"
      }
    \]

#### Using an EL5 KV Store

The following describes how to use the [Mover](#mover), [Store](#store), [SecretKeyObserver](#secretkeyobserver), and [ECStoreManager](#ecstoremanager) classes to implement the use of a KV store in the **el5/** directory. In the following example, [EntryAbility](#entryability) and [index key event](#index-key-event) are used to present how to use these classes.

## Mover

Use **Mover** to move data from an EL2 database to an EL5 database after the screen is unlocked.

import { distributedKVStore } from '@kit.ArkData';
// Logger implements the print feature after Hilog is encapsulated.
import Logger from '../common/Logger';

export class Mover {
  async move(eStore: distributedKVStore.SingleKVStore, cStore: distributedKVStore.SingleKVStore): Promise<void> {
    if (eStore != null && cStore != null) {
      let entries: distributedKVStore.Entry\[\] = await cStore.getEntries('key\_test\_string');
      await eStore.putBatch(entries);
      Logger.info(\`ECDB\_Encry move success\`);
    }
  }
}

## Store

Use the APIs provided by the **Store** class to obtain a database instance, add, delete, and update data, and obtain the data count in the database.

import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
// Logger implements the print feature after Hilog is encapsulated.
import Logger from '../common/Logger';

let kvManager: distributedKVStore.KVManager;

export class StoreInfo {
  kvManagerConfig: distributedKVStore.KVManagerConfig;
  storeId: string;
  option: distributedKVStore.Options;
}

export class Store {
  async getECStore(storeInfo: StoreInfo): Promise<distributedKVStore.SingleKVStore> {
    try {
      kvManager = distributedKVStore.createKVManager(storeInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
    if (kvManager !== undefined) {
      let kvStore: distributedKVStore.SingleKVStore | null;
      try {
        kvStore = await kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeInfo.storeId, storeInfo.option);
        if (kvStore != undefined) {
          Logger.info(\`ECDB\_Encry succeeded in getting store : ${storeInfo.storeId}\`);
          return kvStore;
        }
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
      }
    }
  }

  putOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      const KEY\_TEST\_STRING\_ELEMENT = 'key\_test\_string' + String(Date.now());
      const VALUE\_TEST\_STRING\_ELEMENT = 'value\_test\_string' + String(Date.now());
      try {
        kvStore.put(KEY\_TEST\_STRING\_ELEMENT, VALUE\_TEST\_STRING\_ELEMENT, (err) => {
          if (err !== undefined) {
            Logger.error(\`Failed to put data. Code:${err.code},message:${err.message}\`);
            return;
          }
          Logger.info(\`ECDB\_Encry Succeeded in putting data.${KEY\_TEST\_STRING\_ELEMENT}\`);
        });
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  getDataNum(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      let resultSet: distributedKVStore.KVStoreResultSet;
      kvStore.getResultSet('key\_test\_string').then((result: distributedKVStore.KVStoreResultSet) => {
        Logger.info(\`ECDB\_Encry Succeeded in getting result set num ${result.getCount()}\`);
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet).then(() => {
            Logger.info('Succeeded in closing result set');
          }).catch((err: BusinessError) => {
            Logger.error(\`Failed to close resultset.code is ${err.code},message is ${err.message}\`);
          });
        }
      }).catch((err: BusinessError) => {
        Logger.error(\`Failed to get resultset.code is ${err.code},message is ${err.message}\`);
      });
    }
  }

  deleteOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      kvStore.getEntries('key\_test\_string', (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          Logger.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        if (kvStore != null && entries.length != 0) {
          kvStore.delete(entries\[0\].key, (err: BusinessError) => {
            if (err != undefined) {
              Logger.error(\`Failed to delete.code is ${err.code},message is ${err.message}\`);
              return;
            }
            Logger.info('ECDB\_Encry Succeeded in deleting');
          });
        }
      });
    }
  }

  updateOnedata(kvStore: distributedKVStore.SingleKVStore): void {
    if (kvStore != undefined) {
      kvStore.getEntries('key\_test\_string', async (err: BusinessError, entries: distributedKVStore.Entry\[\]) => {
        if (err != undefined) {
          Logger.error(\`Failed to get Entries.code is ${err.code},message is ${err.message}\`);
          return;
        }
        if (kvStore != null && entries.length != 0) {
          Logger.info(\`ECDB\_Encry old data:${entries\[0\].key},value :${entries\[0\].value.value.toString()}\`);
          await kvStore.put(entries\[0\].key, 'new value\_test\_string' + String(Date.now()) + 'new').then(() => {
          }).catch((err: BusinessError) => {
            Logger.error(\`Failed to put.code is ${err.code},message is ${err.message}\`);
          });
          Logger.info(\`ECDB\_Encry update success\`);
        }
      });
    }
  }
}

## SecretKeyObserver

Use the APIs provided by the **SecretKeyObserver** class to obtain the key status. After the key is destroyed, the EL5 database will be closed.

import { ECStoreManager } from './ECStoreManager';

export enum SecretStatus {
  Lock,
  UnLock
}

export class SecretKeyObserver {
  onLock(): void {
    this.lockStatus = SecretStatus.Lock;
    this.storeManager.closeEStore();
  }

  onUnLock(): void {
    this.lockStatus = SecretStatus.UnLock;
  }

  getCurrentStatus(): number {
    return this.lockStatus;
  }

  initialize(storeManager: ECStoreManager): void {
    this.storeManager = storeManager;
  }

  updateLockStatus(code: number) {
    if (code === SecretStatus.Lock) {
      this.onLock();
    } else {
      this.lockStatus = code;
    }
  }

  // Obtain the screen lock status.
  private lockStatus: number = SecretStatus.UnLock;
  private storeManager: ECStoreManager;
}

export let lockObserve = new SecretKeyObserver();

## ECStoreManager

Use the APIs provided by the **ECStoreManager** class to manage the EL2 and EL5 databases. You can configure database information and migration function information, provide database handles for applications based on the key status, close EL5 databases, and destroy EL2 databases after data migration.

import { distributedKVStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';
// Logger implements the print feature after Hilog is encapsulated.
import Logger from '../common/Logger';

let store = new Store();

export class ECStoreManager {
  config(cInfo: StoreInfo, other: StoreInfo): void {
    this.cInfo = cInfo;
    this.eInfo = other;
  }

  configDataMover(mover: Mover): void {
    this.mover = mover;
  }

  async getCurrentStore(screenStatus: number): Promise<distributedKVStore.SingleKVStore> {
    Logger.info(\`ECDB\_Encry GetCurrentStore start screenStatus: ${screenStatus}\`);
    if (screenStatus === SecretStatus.UnLock) {
      try {
        this.eStore = await store.getECStore(this.eInfo);
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      // Obtain an EL5 database when the screen is unlocked.
      if (this.needMove) {
        if (this.eStore != undefined && this.cStore != undefined) {
          await this.mover.move(this.eStore, this.cStore);
        }
        this.deleteCStore();
        Logger.info(\`ECDB\_Encry Data migration is complete. Destroy cstore\`);
        this.needMove = false;
      }
      return this.eStore;
    } else {
      // Obtain an EL2 database when the screen is locked.
      this.needMove = true;
      try {
        this.cStore = await store.getECStore(this.cInfo);
      } catch (e) {
        let error = e as BusinessError;
        Logger.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      return this.cStore;
    }
  }

  closeEStore(): void {
    try {
      let kvManager = distributedKVStore.createKVManager(this.eInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
      if (kvManager != undefined) {
        kvManager.closeKVStore(this.eInfo.kvManagerConfig.bundleName, this.eInfo.storeId);
        this.eStore = null;
        Logger.info(\`ECDB\_Encry close EStore success\`);
      }
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  deleteCStore(): void {
    try {
      let kvManager = distributedKVStore.createKVManager(this.cInfo.kvManagerConfig);
      Logger.info('Succeeded in creating KVManager');
      if (kvManager != undefined) {
        kvManager.deleteKVStore(this.cInfo.kvManagerConfig.bundleName, this.cInfo.storeId);
        this.cStore = null;
        Logger.info('ECDB\_Encry delete cStore success');
      }
    } catch (e) {
      let error = e as BusinessError;
      Logger.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  private eStore: distributedKVStore.SingleKVStore = null;
  private cStore: distributedKVStore.SingleKVStore = null;
  private cInfo: StoreInfo | null = null;
  private eInfo: StoreInfo | null = null;
  private needMove: boolean = false;
  private mover: Mover | null = null;
}

## EntryAbility

Register a listener for the **COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED** event when the simulated application starts, and configure the database information and key status information.

import { AbilityConstant, application, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { distributedKVStore } from '@kit.ArkData';
import { ECStoreManager } from './ECStoreManager';
import { StoreInfo } from './Store';
import { Mover } from './Mover';
import { SecretKeyObserver } from './SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Logger implements the print feature after Hilog is encapsulated.
import Logger from '../common/Logger';

export let storeManager = new ECStoreManager();
export let e\_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;

export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if (!err) {
    Logger.info('ECDB\_Encry createSubscriber');
    subscriber = commonEventSubscriber;
    try {
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          Logger.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
        } else {
          Logger.info(\`ECDB\_Encry SubscribeCB ${data.code}\`);
          e\_secretKeyObserver.updateLockStatus(data.code);
        }
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
    }
  } else {
    Logger.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
  }
}

let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;

export default class EntryAbility extends UIAbility {
  async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let cContext = this.context;
    cInfo = {
      'kvManagerConfig': {
        context: cContext,
        bundleName: 'com.example.ecstoresamples'
      },
      'storeId': 'cstore',
      'option': {
        createIfMissing: true,
        encrypt: false,
        backup: false,
        autoSync: false,
        // If kvStoreType is left empty, a device KV store is created by default.
        kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
        // The value distributedKVStore.KVStoreType.DEVICE\_COLLABORATION indicates a device KV store.
        securityLevel: distributedKVStore.SecurityLevel.S3
      }
    }
    let eContext = await application.createModuleContext(this.context,'entry');
    eContext.area = contextConstant.AreaMode.EL5;
    eInfo = {
      'kvManagerConfig': {
        context: eContext,
        bundleName: 'com.example.ecstoresamples'
      },
      'storeId': 'estore',
      'option': {
        createIfMissing: true,
        encrypt: false,
        backup: false,
        autoSync: false,
        // If kvStoreType is left empty, a device KV store is created by default.
        kvStoreType: distributedKVStore.KVStoreType.SINGLE\_VERSION,
        // The value distributedKVStore.KVStoreType.DEVICE\_COLLABORATION indicates a device KV store.
        securityLevel: distributedKVStore.SecurityLevel.S3
      }
    }
    Logger.info(\`ECDB\_Encry store area : estore:${eContext.area},cstore${cContext.area}\`);
    // Listen for the COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED event. code == 1 indicates the screen is unlocked, and code==0 indicates the screen is locked.
    try {
      commonEventManager.createSubscriber({
        events: \[ 'COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED' \]
      }, createCB);
      Logger.info(\`ECDB\_Encry success subscribe\`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
    }
    storeManager.config(cInfo, eInfo);
    storeManager.configDataMover(mover);
    e\_secretKeyObserver.initialize(storeManager);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

## Index Key Event

Use **Button** to simulate application operations on the database, such as inserting, deleting, updating, and obtaining the data count, by clicking the button.

import { storeManager, e\_secretKeyObserver } from '../entryability/EntryAbility';
import { distributedKVStore } from '@kit.ArkData';
import { Store } from '../entryability/Store';

let storeOption = new Store();
let lockStatus: number = 1;

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Button('Lock/Unlock').onClick((event: ClickEvent) => {
          if (lockStatus) {
            e\_secretKeyObserver.onLock();
            lockStatus = 0;
          } else {
            e\_secretKeyObserver.onUnLock();
            lockStatus = 1;
          }
          lockStatus ? this.message = 'Unlock' : this.message = 'Lock';
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Button('StoreType').onClick(async (event: ClickEvent) => {
          e\_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Button('Put').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.putOnedata(store);
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Button('Get').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.getDataNum(store);
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Button('Delete').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.deleteOnedata(store);
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Button('Update').onClick(async (event: ClickEvent) => {
          let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
          storeOption.updateOnedata(store);
        }).margin(5)
          .width(100) // Width, in vp (visible pixel).
          .height(40) // Height.

        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### Using an EL5 RDB Store

The following describes how to use the [Mover](#mover-1), [Store](#store-1), [SecretKeyObserver](#secretkeyobserver-1), and [ECStoreManager](#ecstoremanager-1) classes to implement the use of an RDB store in the **el5/** directory. In the following example, [EntryAbility](#entryability-1) and [index key event](#index-key-event-1) are used to present how to use these classes.

## Mover

Use **Mover** to move data from an EL2 database to an EL5 database after the screen is unlocked.

import { relationalStore } from '@kit.ArkData';

export class Mover {
  async move(eStore: relationalStore.RdbStore, cStore: relationalStore.RdbStore) {
    if (eStore != null && cStore != null) {
      let predicates = new relationalStore.RdbPredicates('employee');
      let resultSet = await cStore.query(predicates);
      while (resultSet.goToNextRow()) {
        let bucket = resultSet.getRow();
        await eStore.insert('employee', bucket);
      }
    }
  }
}

## Store

Use the APIs provided by the **Store** class to obtain a database instance, add, delete, and update data, and obtain the data count in the database. The **StoreInfo** class is used to store and obtain database information.

import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { Context } from '@kit.AbilityKit';

export class StoreInfo {
  context: Context;
  config: relationalStore.StoreConfig;
  storeId: string;
}

let id = 1;
const SQL\_CREATE\_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)';

export class Store {
  async getECStore(storeInfo: StoreInfo): Promise<relationalStore.RdbStore> {
    let rdbStore: relationalStore.RdbStore | null;
    try {
      rdbStore = await relationalStore.getRdbStore(storeInfo.context, storeInfo.config);
      if (rdbStore.version == 0) {
        await rdbStore.executeSql(SQL\_CREATE\_TABLE);
        console.info(\`ECDB\_Encry succeeded in getting Store : ${storeInfo.storeId}\`);
        rdbStore.version = 1;
      }
    } catch (e) {
      let error = e as BusinessError;
      console.error(\`An unexpected error occurred.code is ${error.code},message is ${error.message}\`);
    }
    return rdbStore;
  }

  async putOnedata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      const valueBucket: relationalStore.ValuesBucket = {
        ID: id++,
        NAME: 'Lisa',
        AGE: 18,
        SALARY: 100.5,
        CODES: new Uint8Array(\[1, 2, 3, 4, 5\]),
      };
      try {
        await rdbStore.insert('EMPLOYEE', valueBucket);
        console.info(\`ECDB\_Encry insert success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async getDataNum(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        let resultSet = await rdbStore.query(predicates);
        let count = resultSet.rowCount;
        console.info(\`ECDB\_Encry getdatanum success count : ${count}\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async deleteAlldata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        predicates.equalTo('AGE', 18);
        await rdbStore.delete(predicates);
        console.info(\`ECDB\_Encry delete Success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }

  async updateOnedata(rdbStore: relationalStore.RdbStore) {
    if (rdbStore != undefined) {
      try {
        let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
        predicates.equalTo('NAME', 'Lisa');
        const valueBucket: relationalStore.ValuesBucket = {
          NAME: 'Anna',
          SALARY: 100.5,
          CODES: new Uint8Array(\[1, 2, 3, 4, 5\]),
        };
        await rdbStore.update(valueBucket, predicates);
        console.info(\`ECDB\_Encry update success\`);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`An unexpected error occurred. Code:${error.code},message:${error.message}\`);
      }
    }
  }
}

## SecretKeyObserver

Use the APIs provided by the **SecretKeyObserver** class to obtain the key status. After the key is destroyed, the EL5 database will be closed.

import { ECStoreManager } from './ECStoreManager';

export enum SecretStatus {
  Lock,
  UnLock
}

export class SecretKeyObserver {
  onLock(): void {
    this.lockStatus = SecretStatus.Lock;
    this.storeManager.closeEStore();
  }

  onUnLock(): void {
    this.lockStatus = SecretStatus.UnLock;
  }

  getCurrentStatus(): number {
    return this.lockStatus;
  }

  initialize(storeManager: ECStoreManager): void {
    this.storeManager = storeManager;
  }

  updateLockStatus(code: number) {
    if (this.lockStatus === SecretStatus.Lock) {
      this.onLock();
    } else {
      this.lockStatus = code;
    }
  }

  private lockStatus: number = SecretStatus.UnLock;
  private storeManager: ECStoreManager;
}

export let lockObserve = new SecretKeyObserver();

## ECStoreManager

Use the APIs provided by the **ECStoreManager** class to manage the EL2 and EL5 databases. You can configure database information and migration function information, provide database handles for applications based on the key status, close EL5 databases, and destroy EL2 databases after data migration.

import { relationalStore } from '@kit.ArkData';
import { Mover } from './Mover';
import { BusinessError } from '@kit.BasicServicesKit';
import { StoreInfo, Store } from './Store';
import { SecretStatus } from './SecretKeyObserver';

let store = new Store();

export class ECStoreManager {
  config(cInfo: StoreInfo, other: StoreInfo): void {
    this.cInfo = cInfo;
    this.eInfo = other;
  }

  configDataMover(mover: Mover): void {
    this.mover = mover;
  }

  async getCurrentStore(screenStatus: number): Promise<relationalStore.RdbStore> {
    if (screenStatus === SecretStatus.UnLock) {
      try {
        this.eStore = await store.getECStore(this.eInfo);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      // Obtain an EL5 database when the screen is unlocked.
      if (this.needMove) {
        if (this.eStore != undefined && this.cStore != undefined) {
          await this.mover.move(this.eStore, this.cStore);
          console.info(\`ECDB\_Encry cstore data move to estore success\`);
        }
        this.deleteCStore();
        this.needMove = false;
      }
      return this.eStore;
    } else {
      // Obtain an EL2 database when the screen is locked.
      this.needMove = true;
      try {
        this.cStore = await store.getECStore(this.cInfo);
      } catch (e) {
        let error = e as BusinessError;
        console.error(\`Failed to GetECStore.code is ${error.code},message is ${error.message}\`);
      }
      return this.cStore;
    }
  }

  closeEStore(): void {
    this.eStore = undefined;
  }

  async deleteCStore() {
    try {
      await relationalStore.deleteRdbStore(this.cInfo.context, this.cInfo.storeId)
    } catch (e) {
      let error = e as BusinessError;
      console.error(\`Failed to create KVManager.code is ${error.code},message is ${error.message}\`);
    }
  }

  private eStore: relationalStore.RdbStore = null;
  private cStore: relationalStore.RdbStore = null;
  private cInfo: StoreInfo | null = null;
  private eInfo: StoreInfo | null = null;
  private needMove: boolean = false;
  private mover: Mover | null = null;
}

## EntryAbility

Register a listener for the **COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED** event when the simulated application starts, and configure the database information and key status information.

import { AbilityConstant, contextConstant, UIAbility, Want, application } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { relationalStore } from '@kit.ArkData';
import { ECStoreManager } from '../encryptedEStoreGuidelines/ECStoreManager';
import { StoreInfo } from '../encryptedEStoreGuidelines/Store';
import { Mover } from '../encryptedEStoreGuidelines/Mover';
import { SecretKeyObserver } from '../encryptedEStoreGuidelines/SecretKeyObserver';
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

export let storeManager = new ECStoreManager();
export let e\_secretKeyObserver = new SecretKeyObserver();
let mover = new Mover();
let subscriber: commonEventManager.CommonEventSubscriber;

export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if (!err) {
    console.info('ECDB\_Encrypt createSubscriber');
    subscriber = commonEventSubscriber;
    try {
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          console.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
        } else {
          console.info(\`ECDB\_Encrypt SubscribeCB ${data.code}\`);
          e\_secretKeyObserver.updateLockStatus(data.code);
        }
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`subscribe failed, code is ${err.code}, message is ${err.message}\`);
    }
  } else {
    console.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
  }
}

let cInfo: StoreInfo | null = null;
let eInfo: StoreInfo | null = null;

export default class EntryAbility extends UIAbility {
  async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let cContext = this.context;
    cInfo = {
      context: cContext,
      config: {
        name: 'cstore.db',
        securityLevel: relationalStore.SecurityLevel.S3,
      },
      storeId: 'cstore.db'
    };
    let eContext = await application.createModuleContext(this.context, 'entry');
    eContext.area = contextConstant.AreaMode.EL5;
    eInfo = {
      context: eContext,
      config: {
        name: 'estore.db',
        securityLevel: relationalStore.SecurityLevel.S3,
      },
      storeId: 'estore.db',
    };
    // Listen for the COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED event. code == 1 indicates the screen is unlocked, and code==0 indicates the screen is locked.
    console.info(\`ECDB\_Encry store area : estore:${eContext.area},cstore${cContext.area}\`)
    try {
      commonEventManager.createSubscriber({
        events: \['COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED'\]
      }, createCB);
      console.info(\`ECDB\_Encry success subscribe\`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`createSubscriber failed, code is ${err.code}, message is ${err.message}\`);
    }
    storeManager.config(cInfo, eInfo);
    storeManager.configDataMover(mover);
    e\_secretKeyObserver.initialize(storeManager);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

## Index Key Event

Use **Button** to simulate application operations on the database, such as inserting, deleting, updating, and obtaining the data count, by clicking the button.

import { storeManager, e\_secretKeyObserver } from '../entryability/EntryAbility';
import { relationalStore } from '@kit.ArkData';
import { Store } from './Store';

let storeOption = new Store();

let lockStatus: number = 1;

@Entry
@Component
struct Index {
  @State message: string = '';

  build() {
    Row() {
      Column() {
        Button('Lock/Unlock')
          .onClick((event: ClickEvent) => {
            if (lockStatus) {
              e\_secretKeyObserver.onLock();
              lockStatus = 0;
            } else {
              e\_secretKeyObserver.onUnLock();
              lockStatus = 1;
            }
            lockStatus ? this.message = 'Unlock' : this.message = 'Lock';
          })
          .margin('5')
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('store type')
          .onClick(async (event: ClickEvent) => {
            e\_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
            console.info(\`ECDB\_Encry current store : ${this.message}\`);
          })
          .margin('5')
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('put')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.putOnedata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('Get')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.getDataNum(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('delete')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.deleteAlldata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Button('update')
          .onClick(async (event: ClickEvent) => {
            let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e\_secretKeyObserver.getCurrentStatus());
            storeOption.updateOnedata(store);
          })
          .margin(5)
          .backgroundColor('#0D9FFB')
          .width('50%')
          .height('5%')
          .type(ButtonType.Capsule)

        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
