# Updating a Security Control Policy

#### Use Case

Enterprise Data Guard Kit allows apps to deliver control policies to HarmonyOS for security control.

#### API Description

For details about these APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[updatePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section068912217520)(policy: string, callback: AsyncCallback<void>): void

 | 

Updates a security control policy using a callback.

 |
| 

[updatePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section16264735355)(policy: string): Promise<void>

 | 

Updates a security control policy using a promise.

 |

#### Development Procedure

1.  Import the required module.
    
    import { fileGuard } from '@kit.EnterpriseDataGuardKit';
    
2.  Initialize the **guard** object of [FileGuard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-fileguard#section18457214114215) and call the **updatePolicy** API to update a security control policy in either of the following ways:
    
    -   Update a security control policy using a callback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function updatePolicyCallback() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let policy: string = '{' +
        '"net\_intercept\_toggle":0,' +
        '"boundary":\["10.10.0.0-10.255.255.255","172.16.0.0-172.31.255.255"\],' +
        '"netsegment\_trustlist":\["10.10.0.0-10.255.255.255"\],' +
        '"netsegment\_blocklist":\["172.16.0.0-172.31.255.255"\],' +
        '"default\_policy":0' +
        '}';
      guard.updatePolicy(policy, (err: BusinessError) => {
        if (err) {
          console.error(\`Failed to update policy. Code: ${err.code}, message: ${err.message}.\`);
        } else {
          console.info(\`Succeeded in updating policy.\`);
        }
      });
    }
    
    -   Update a security control policy using a promise.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function updatePolicyPromise() {
      let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
      let policy: string = '{' +
        '"net\_intercept\_toggle":0,' +
        '"boundary":\["10.10.0.0-10.255.255.255","172.16.0.0-172.31.255.255"\],' +
        '"netsegment\_trustlist":\["10.10.0.0-10.255.255.255"\],' +
        '"netsegment\_blocklist":\["172.16.0.0-172.31.255.255"\],' +
        '"default\_policy":0' +
        '}';
      guard.updatePolicy(policy).then(() => {
        console.info(\`Succeeded in updating policy.\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to update policy. Code: ${err.code}, message: ${err.message}.\`);
      });
    }
