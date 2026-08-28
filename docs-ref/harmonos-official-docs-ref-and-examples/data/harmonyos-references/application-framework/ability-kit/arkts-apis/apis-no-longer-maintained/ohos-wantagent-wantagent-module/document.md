# @ohos.wantAgent (WantAgent Module)

The WantAgent module provides APIs for creating and comparing WantAgent objects, and obtaining the user ID and bundle name of a WantAgent object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/9_Sq-vUiR3i6W0O3iQ3V1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2A73EE2E91A985C753DEDBF6D507537821824045AAD7A7F3113D501856BC2A0)

The APIs of this module are supported since API version 7 and deprecated since API version 9. You are advised to use [@ohos.app.ability.wantAgent](../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) instead. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import wantAgent from '@ohos.wantAgent';

#### wantAgent.getWantAgent

getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void

Creates a WantAgent object. If the creation fails, a null WantAgent object is returned. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [WantAgentInfo](../../dependent-elements-and-definitions/wantagent/wantagentinfo/document.md) | Yes | WantAgent object. |
| callback | AsyncCallback<WantAgent> | Yes | Callback used to return the WantAgent object. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    if (err.code) {
        console.info('getWantAgent Callback err:' + JSON.stringify(err));
    } else {
        console.info('getWantAgent Callback success');
    }
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.getWantAgent

getWantAgent(info: WantAgentInfo): Promise<WantAgent>

Creates a WantAgent object. If the creation fails, a null WantAgent object is returned. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [WantAgentInfo](../../dependent-elements-and-definitions/wantagent/wantagentinfo/document.md) | Yes | WantAgent object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<WantAgent> | Promise used to return the WantAgent object. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}).then((data: \_WantAgent) => {
    console.info('==========================>getWantAgentCallback=======================>');
});

#### wantAgent.getBundleName

getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void

Obtains the bundle name of a WantAgent object. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |
| callback | AsyncCallback<string> | Yes | Callback used to return the bundle name. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj: \_WantAgent;

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    console.info('==========================>getWantAgentCallback=======================>');
    if (err.code == 0) {
        wantAgentObj = data;
    } else {
        console.error('getWantAgent failed, error: ' + JSON.stringify(err));
        return;
    }

    // getBundleName callback
    let getBundleNameCallback = (err: BusinessError, data: string) => {
        console.info('==========================>getBundleNameCallback=======================>');
    }
    wantAgent.getBundleName(wantAgentObj, getBundleNameCallback);
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.getBundleName

getBundleName(agent: WantAgent): Promise<string>

Obtains the bundle name of a WantAgent object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';

// WantAgent object
let wantAgentObj: \_WantAgent;

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}).then((data: \_WantAgent) => {
    console.info('==========================>getWantAgentCallback=======================>');
    wantAgentObj = data;
    if (wantAgentObj) {
        wantAgent.getBundleName(wantAgentObj).then((data) => {
            console.info('==========================>getBundleNameCallback=======================>');
        });
    }
});

#### wantAgent.getUid

getUid(agent: WantAgent, callback: AsyncCallback<number>): void

Obtains the user ID of a WantAgent object. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |
| callback | AsyncCallback<number> | Yes | Callback used to return the user ID. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj: \_WantAgent;

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    console.info('==========================>getWantAgentCallback=======================>');
    if (err.code == 0) {
        wantAgentObj = data;
    } else {
        console.error('getWantAgent failed, error: ' + JSON.stringify(err));
        return;
    }

    // getUid callback
    let getUidCallback = (err: BusinessError, data: number) => {
        console.info('==========================>getUidCallback=======================>');
    }
    wantAgent.getUid(wantAgentObj, getUidCallback);
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.getUid

getUid(agent: WantAgent): Promise<number>

Obtains the user ID of a WantAgent object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the user ID. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';

// WantAgent object
let wantAgentObj: \_WantAgent;

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}).then((data) => {
    console.info('==========================>getWantAgentCallback=======================>');
    wantAgentObj = data;
    if (wantAgentObj) {
        wantAgent.getUid(wantAgentObj).then((data) => {
        console.info('==========================>getUidCallback=======================>');
    });
    }
});

#### wantAgent.cancel

cancel(agent: WantAgent, callback: AsyncCallback<void>): void

Cancels a WantAgent object. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj: \_WantAgent;

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    console.info('==========================>getWantAgentCallback=======================>');
    if (err.code == 0) {
        wantAgentObj = data;
    } else {
        console.error('getWantAgent failed, error: ' + JSON.stringify(err));
        return;
    }

    // cancel callback
    let cancelCallback = (err: BusinessError) => {
        console.info('==========================>cancelCallback=======================>');
    }
    wantAgent.cancel(wantAgentObj, cancelCallback);
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.cancel

cancel(agent: WantAgent): Promise<void>

Cancels a WantAgent object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj: \_WantAgent;

wantAgent.getWantAgent({
    wants: \[
    {
        deviceId: 'deviceId',
        bundleName: 'com.neu.setResultOnAbilityResultTest1',
        abilityName: 'com.example.test.EntryAbility',
        action: 'action1',
        entities: \['entity1'\],
        type: 'MIMETYPE',
        uri: 'key={true,true,false}',
        parameters:
        {
            mykey0: 2222,
            mykey1: \[1, 2, 3\],
            mykey2: '\[1, 2, 3\]',
            mykey3: 'ssssssssssssssssssssssssss',
            mykey4: \[false, true, false\],
            mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
            mykey6: true,
        }
    }
\],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}).then((data) => {
    console.info('==========================>getWantAgentCallback=======================>');
    wantAgentObj = data;
    if (wantAgentObj) {
        wantAgent.cancel(wantAgentObj).then((data) => {
            console.info('==========================>cancelCallback=======================>');
        });
    }
});

#### wantAgent.trigger

trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: Callback<CompleteData>): void

Triggers a WantAgent object. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | WantAgent object. |
| triggerInfo | [TriggerInfo](../../dependent-elements-and-definitions/wantagent/triggerinfo/document.md) | Yes | TriggerInfo object. |
| callback | Callback<CompleteData> | No | Callback used to return the result. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj: \_WantAgent;

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    console.info('==========================>getWantAgentCallback=======================>');
    if (err.code == 0) {
        wantAgentObj = data;
    } else {
        console.error('getWantAgent failed, error: ' + JSON.stringify(err));
        return;
    }

    // trigger callback
    let triggerCallback = (data: wantAgent.CompleteData) => {
        console.info('==========================>triggerCallback=======================>');
    };

    wantAgent.trigger(wantAgentObj, {code:0}, triggerCallback);
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.equal

equal(agent: WantAgent, otherAgent: WantAgent, callback: AsyncCallback<boolean>): void

Checks whether two WantAgent objects are equal to determine whether the same operation is from the same application. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | The first WantAgent object. |
| otherAgent | WantAgent | Yes | WantAgent object. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. **true** if the two WantAgent objects are equal, **false** otherwise. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';
import { BusinessError } from '@ohos.base';

// WantAgent object
let wantAgentObj1: \_WantAgent;
let wantAgentObj2: \_WantAgent;

// getWantAgent callback
function getWantAgentCallback(err: BusinessError, data: \_WantAgent) {
    console.info('==========================>getWantAgentCallback=======================>');
    if (err.code == 0) {
        wantAgentObj1 = data;
        wantAgentObj2 = data;
    } else {
        console.error('getWantAgent failed, error: ' + JSON.stringify(err));
        return;
    }

    // equal callback
    let equalCallback = (err: BusinessError, data: boolean) => {
        console.info('==========================>equalCallback=======================>');
    };
    wantAgent.equal(wantAgentObj1, wantAgentObj2, equalCallback);
}

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}, getWantAgentCallback);

#### wantAgent.equal

equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>

Checks whether two WantAgent objects are equal to determine whether the same operation is from the same application. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| agent | WantAgent | Yes | The first WantAgent object. |
| otherAgent | WantAgent | Yes | WantAgent object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. **true** if the two WantAgent objects are equal, **false** otherwise. |

**Example**

import wantAgent, { WantAgent as \_WantAgent } from '@ohos.wantAgent';

// WantAgent object
let wantAgentObj1: \_WantAgent;
let wantAgentObj2: \_WantAgent;

wantAgent.getWantAgent({
    wants: \[
        {
            deviceId: 'deviceId',
            bundleName: 'com.neu.setResultOnAbilityResultTest1',
            abilityName: 'com.example.test.EntryAbility',
            action: 'action1',
            entities: \['entity1'\],
            type: 'MIMETYPE',
            uri: 'key={true,true,false}',
            parameters:
            {
                mykey0: 2222,
                mykey1: \[1, 2, 3\],
                mykey2: '\[1, 2, 3\]',
                mykey3: 'ssssssssssssssssssssssssss',
                mykey4: \[false, true, false\],
                mykey5: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
                mykey6: true,
            }
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags:\[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
}).then((data) => {
    console.info('==========================>getWantAgentCallback=======================>');
    wantAgentObj1 = data;
    wantAgentObj2 = data;
    if (data) {
        wantAgent.equal(wantAgentObj1, wantAgentObj2).then((data) => {
            console.info('==========================>equalCallback=======================>');
        });
    }
});

#### WantAgentFlags

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ONE\_TIME\_FLAG | 0 | The WantAgent object can be used only once. |
| NO\_BUILD\_FLAG | 1 | The WantAgent object does not exist and hence it is not created. In this case, **null** is returned. |
| CANCEL\_PRESENT\_FLAG | 2 | The existing WantAgent object should be canceled before a new object is generated. |
| UPDATE\_PRESENT\_FLAG | 3 | Extra information of the existing WantAgent object is replaced with that of the new object. |
| CONSTANT\_FLAG | 4 | The WantAgent object is immutable. |
| REPLACE\_ELEMENT | 5 | The **element** property in the current Want can be replaced by the **element** property in the Want passed in **WantAgent.trigger()**. |
| REPLACE\_ACTION | 6 | The **action** property in the current Want can be replaced by the **action** property in the Want passed in **WantAgent.trigger()**. |
| REPLACE\_URI | 7 | The **uri** property in the current Want can be replaced by the **uri** property in the Want passed in **WantAgent.trigger()**. |
| REPLACE\_ENTITIES | 8 | The **entities** property in the current Want can be replaced by the **entities** property in the Want passed in **WantAgent.trigger()**. |
| REPLACE\_BUNDLE | 9 | The **bundleName** property in the current Want can be replaced by the **bundleName** property in the Want passed in **WantAgent.trigger()**. |

#### OperationType

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_TYPE | 0 | Unknown operation type. |
| START\_ABILITY | 1 | Starts an ability with a UI. |
| START\_ABILITIES | 2 | Starts multiple abilities with a UI. |
| START\_SERVICE | 3 | Starts an ability without a UI. |
| SEND\_COMMON\_EVENT | 4 | Sends a common event. |

#### CompleteData

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| info | WantAgent | No | No | A triggered WantAgent object. |
| want | Want | No | No | An existing triggered Want. |
| finalCode | number | No | No | Request code that triggers the WantAgent object. |
| finalData | string | No | No | Final data collected by the common event. |
| extraInfo | { \[key: string\]: any } | No | Yes | Extra information. |

#### WantAgent

type WantAgent = object

Defines the WantAgent object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| object | WantAgent object. |
