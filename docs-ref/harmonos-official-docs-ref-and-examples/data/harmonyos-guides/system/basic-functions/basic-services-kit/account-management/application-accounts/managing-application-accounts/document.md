# Managing Application Accounts

You can use the [application account SDK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount) to manage application accounts.

When an application is uninstalled, the account data of the application will be automatically deleted. When a local account is deleted, the account data of all applications of the local account will be automatically deleted.

#### Before You Start

1.  Import the **appAccount** module.
    

import { appAccount, BusinessError } from '@kit.BasicServicesKit';

1.  Obtain an **AppAccountManager** instance.
    

const appAccountManager = appAccount.createAppAccountManager();

#### Creating an Application Account

Create an application account for an application user.

**Procedure**

1.  Specify the account name and optional parameters.
    

    let name: string = 'ZhangSan';
    let options: appAccount.CreateAccountOptions = {
      customData: {
        age: '10'
      }
    };

1.  Use [createAccount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#createaccount9) to create an application account based on the specified parameters.
    

    appAccountManager.createAccount(name, options).then(()=>{
      console.info('createAccount successfully');
    // ···
    }).catch((err: BusinessError)=>{
       console.error(\`createAccount failed, error: code is ${err.code}, message is ${err.message}\`);
    // ···
    });

#### Obtaining Application Account List

**Procedure**

Use [getAllAccounts](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#getallaccounts9) to obtain the application account list.

    appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo\[\]) => {
      console.info('getAllAccounts successfully, data: ' + JSON.stringify(data));
    // ···
    }).catch((err: BusinessError) => {
      console.error(\`getAllAccounts failed, code is ${err.code}, message is ${err.message}\`);
    // ···
    });

#### Accessing Account Credentials

**Procedure**

1.  Specify the account name, credential type, and credential.
    

    let name: string = 'ZhangSan';
    let credentialType: string = 'PIN\_SIX';
    let credential: string = 'xxxxxx';

1.  Use [getCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#getcredential9) to obtain the account credential.
    

    appAccountManager.getCredential(name, credentialType).then((data: string) => {
      console.info('getCredential successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(\`getCredential failed, code is ${err.code}, message is ${err.message}\`);
    // ···
    });

1.  Use [setCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#setcredential9) to set the account credential.
    

    await appAccountManager.setCredential(name, credentialType, credential).then(() => {
      console.info('setCredential successfully');
    }).catch((err: BusinessError) => {
      console.error(\`setCredential failed: code is ${err.code}, message is ${err.message}\`);
    // ···
    });

#### Accessing Custom Account Data

**Procedure**

1.  Specify the account name and custom data.
    

    let name: string = 'ZhangSan';
    let key: string = 'age';
    let value: string = '12';

1.  Use [setCustomData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#setcustomdata9) to customize account data.
    

    await appAccountManager.setCustomData(name, key, value).then(() => {
      console.info('setCustomData successfully');
    }).catch((err: BusinessError) => {
      console.error(\`setCustomData failed: code is ${err.code}, message is ${err.message}\`);
    // ···
    });

1.  Use [getCustomData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#getcustomdata9) to obtain the custom account data.
    

    appAccountManager.getCustomData(name, key).then((data: string) => {
      console.info('getCustomData successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(\`getCustomData failed, code is ${err.code}, message is ${err.message}\`);
    // ···
    });

#### Accessing the Account Authentication Token

**Procedure**

1.  Specify the account name, account owner, authorization type, and authentication token.
    

    let name: string = 'ZhangSan';
    let owner: string = 'com.samples.managerapplicationaccount';
    let authType: string = 'getSocialData';
    let token: string = 'xxxxxx';

1.  Use [setAuthToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#setauthtoken9) to set an authorization token for the specified authentication type.
    

    await appAccountManager.setAuthToken(name, authType, token).then(() => {
      console.info('setAuthToken successfully');
    }).catch((err: BusinessError) => {
      console.error(\`setAuthToken failed: code is ${err.code}, message is ${err.message}\`);
    // ···
    });

1.  Use [getAuthToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#getauthtoken9) to obtain the authentication token of the specified authentication type.
    

    await appAccountManager.getAuthToken(name, owner, authType).then((data: string) => {
      console.info('getAuthToken successfully, data: ' + data);
    // ···
    }).catch((err: BusinessError) => {
      console.error(\`getAuthToken failed, code is ${err.code}, message is ${err.message}\`);
    // ···
    });

#### Removing an Application Account

Remove the application account after the user logs out of the system.

**Procedure**

Use [removeAccount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount#removeaccount9) to remove the application account.

    let name: string = 'ZhangSan';
    appAccountManager.removeAccount(name).then(() => {
      console.info('removeAccount successfully');
    // ···
    }).catch((err: BusinessError) => {
      console.error(\`removeAccount failed, code is ${err.code}, message is ${err.message}\`);
    // ···
    });
