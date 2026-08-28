# Database Encryption (C/C++)

#### When to Use

The database encryption capability is provided to effectively protect the data stored in a database.

Database encryption allows data to be stored and used in ciphertext, ensuring data confidentiality and integrity.

The encrypted database can be accessed only using an API, and the database file cannot be opened in other ways. Whether a database is encrypted is set when the database is created, and the setting cannot be changed.

Currently, only RDB stores (C/C++) support database encryption.

#### How to Develop

Call **OH\_Rdb\_SetEncrypted** to set whether to encrypt an RDB store. If **isEncrypted** is set to **true**, the database is encrypted; otherwise, the database is not encrypted. This parameter is set to **false** by default.

When **isEncrypted** is set to **true**, call **OH\_Rdb\_SetCryptoParam** to set custom keys and algorithms for encryption or decryption.

1.  Add the following library to **CMakeLists.txt**.
    
    libnative\_rdb\_ndk.z.so
    
2.  Include header files.
    
    #include <cstring>
    #include "database/rdb/relational\_store.h"
    #include "hilog/log.h"
    
3.  You can set encryption/decryption parameters as follows:
    
    -   Scenario 1: If no custom encryption/decryption parameter is configured, the default configuration is used.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el2/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL2);
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        // Set the database to be created or opened in encryption mode.
        OH\_Rdb\_SetEncrypted(config, true);
        int errCode = 0;
        // Create an OH\_Rdb\_Store instance.
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        OH\_Rdb\_CloseStore(store);
        store = nullptr;
        OH\_Rdb\_DestroyConfig(config);
        config = nullptr;
        
    -   Scenario 2: Call **OH\_Rdb\_SetCryptoParam** to configure encryption parameters. The database is encrypted and decrypted using the custom key and algorithm parameters.
        
        If custom configuration is not required, you can use the default encryption configuration.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el2/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL2);
        OH\_Rdb\_SetStoreName(config, "RdbTestConfigEncryptParam.db");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        // Set the database to be created or opened in encryption mode.
        OH\_Rdb\_SetEncrypted(config, true);
        // Create a custom encryption parameter object.
        OH\_Rdb\_CryptoParam \*cryptoParam = OH\_Rdb\_CreateCryptoParam();
        
        // Hard-coded keys are used as an example. You should use a secure key management service in actual development.
        uint8\_t key\[6\] = {0x31, 0x32, 0x33, 0x34, 0x35, 0x36};
        // Use the specified key to open the encrypted database. If no key is specified, the database generates and saves the key and uses the generated key.
        const int32\_t length = 6;
        OH\_Crypto\_SetEncryptionKey(cryptoParam, key, length);
        // Clear the key information after it is used.
        for (size\_t i = 0; i < sizeof(key); i++) {
            key\[i\] = 0;
        }
        // Set the number of iterations of the KDF algorithm, which must be greater than 0. If the value is not specified or the number of iterations is 0, the default value 10000 and the default encryption algorithm are used.
        const int64\_t iteration = 64000;
        OH\_Crypto\_SetIteration(cryptoParam, iteration);
        // Set the encryption algorithm. If it is not specified, AES\_256\_GCM is used by default.
        OH\_Crypto\_SetEncryptionAlgo(cryptoParam, Rdb\_EncryptionAlgo::RDB\_AES\_256\_CBC);
        // Set the HMAC algorithm. If it is not specified, SHA-256 is used by default.
        OH\_Crypto\_SetHmacAlgo(cryptoParam, RDB\_HMAC\_SHA512);
        // Set the KDF algorithm. If it is not specified, SHA-256 is used by default.
        OH\_Crypto\_SetKdfAlgo(cryptoParam, RDB\_KDF\_SHA512);
        // Set the page size used when the database is encrypted. The value must be an integer ranging from 1024 to 65536 and be a power of 2. If it is not specified, the default value 1024 is used.
        const int64\_t pageSize = 4096;
        OH\_Crypto\_SetCryptoPageSize(cryptoParam, pageSize);
        // Set the custom encryption parameters.
        OH\_Rdb\_SetCryptoParam(config, cryptoParam);
        
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        // Destroy the custom encryption parameter object.
        OH\_Rdb\_DestroyCryptoParam(cryptoParam);
        cryptoParam = nullptr;
        OH\_Rdb\_CloseStore(store);
        store = nullptr;
        OH\_Rdb\_DestroyConfig(config);
        config = nullptr;
        
4.  Since API version 22, you can use **OH\_Rdb\_RekeyEx** to change the key or encryption parameters of an encrypted database as required.
    
    The database key and encryption parameters can be changed in the following scenarios:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/TBE_yBh2QCKWUheW8TaLVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061921Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEF465DEC7DFE30107CEAE2148973BCF1ACD6053E2F27BC936857DA42283685F)
    
    Exercise caution when changing encryption parameters. After **OH\_Rdb\_RekeyEx** is used, you must use the new parameters to open the database. Otherwise, the database may fail to be opened. If the rekey process is interrupted due to device power-off or other reasons, the operation may succeed or fail. Therefore, it is recommended that the service party perform a redundancy retry based on the parameters modified before and after **OH\_Rdb\_RekeyEx** is used to ensure the database status is correctly determined and the database can be opened.
    
    -   Scenario 1: The original database is encrypted using default parameters. Change the key and encryption parameters.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, true);
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_DestroyConfig(config);
            OH\_Rdb\_CloseStore(store);
            config = NULL;
            store = NULL;
            return;
        }
        OH\_Crypto\_SetEncryptionAlgo(crypto, RDB\_AES\_256\_CBC);
        OH\_Crypto\_SetHmacAlgo(crypto, RDB\_HMAC\_SHA512);
        OH\_Crypto\_SetKdfAlgo(crypto, RDB\_KDF\_SHA512);
        OH\_Crypto\_SetCryptoPageSize(crypto, 2048);
        errCode = OH\_Rdb\_RekeyEx(store, crypto);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        config = NULL;
        store = NULL;
        crypto = NULL;
        
    -   Scenario 2: The original database is encrypted using custom parameters. Change the custom key and encryption parameters.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, true);
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        uint8\_t encryptionKey\[\] = "12345678";
        OH\_Crypto\_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
        memset(encryptionKey, 0, sizeof(encryptionKey));
        OH\_Rdb\_SetCryptoParam(config, crypto);
        
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*newCryptoParam = OH\_Rdb\_CreateCryptoParam();
        if (newCryptoParam == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create newCryptoParam failed.");
            OH\_Rdb\_DestroyConfig(config);
            OH\_Rdb\_CloseStore(store);
            OH\_Rdb\_DestroyCryptoParam(crypto);
            config = NULL;
            store = NULL;
            crypto = NULL;
            return;
        }
        // Note: Hard-coded keys are used as an example. You should use a secure key management service in actual development. After using the keys, clear them in a timely manner.
        uint8\_t key\[\] = "87654321";
        OH\_Crypto\_SetEncryptionKey(newCryptoParam, key, sizeof(key));
        memset(key, 0, sizeof(key));
        OH\_Crypto\_SetEncryptionAlgo(newCryptoParam, RDB\_AES\_256\_CBC);
        OH\_Crypto\_SetHmacAlgo(newCryptoParam, RDB\_HMAC\_SHA512);
        OH\_Crypto\_SetKdfAlgo(newCryptoParam, RDB\_KDF\_SHA512);
        OH\_Crypto\_SetCryptoPageSize(newCryptoParam, 4096);
        errCode = OH\_Rdb\_RekeyEx(store, newCryptoParam);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        OH\_Rdb\_DestroyCryptoParam(newCryptoParam);
        config = NULL;
        store = NULL;
        crypto = NULL;
        newCryptoParam = NULL;
        
    -   Scenario 3: The original database is encrypted using default parameters. Change the default key and parameters to the custom key and encryption parameters.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, true);
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_CloseStore(store);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            store = NULL;
            return;
        }
        // Note: Hard-coded keys are used as an example. You should use a secure key management service in actual development. After using the keys, clear them in a timely manner.
        uint8\_t key\[\] = "12345678";
        errCode = OH\_Crypto\_SetEncryptionKey(crypto, key, sizeof(key));
        memset(key, 0, sizeof(key));
        OH\_Crypto\_SetEncryptionAlgo(crypto, RDB\_AES\_256\_CBC);
        OH\_Crypto\_SetHmacAlgo(crypto, RDB\_HMAC\_SHA512);
        OH\_Crypto\_SetKdfAlgo(crypto, RDB\_KDF\_SHA512);
        OH\_Crypto\_SetCryptoPageSize(crypto, 2048);
        errCode = OH\_Rdb\_RekeyEx(store, crypto);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        config = NULL;
        store = NULL;
        crypto = NULL;
        
    -   Scenario 4: The original database is encrypted using custom parameters. Change the key generated by database and custom encryption parameters.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, true);
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        // Note: Hard-coded keys are used as an example. You should use a secure key management service in actual development. After using the keys, clear them in a timely manner.
        uint8\_t encryptionKey\[\] = "12345678";
        OH\_Crypto\_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
        memset(encryptionKey, 0, sizeof(encryptionKey));
        OH\_Rdb\_SetCryptoParam(config, crypto);
        
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*newCryptoParam = OH\_Rdb\_CreateCryptoParam();
        if (newCryptoParam == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create newCryptoParam failed.");
            OH\_Rdb\_DestroyConfig(config);
            OH\_Rdb\_CloseStore(store);
            OH\_Rdb\_DestroyCryptoParam(crypto);
            config = NULL;
            store = NULL;
            crypto = NULL;
            return;
        }
        OH\_Crypto\_SetEncryptionAlgo(newCryptoParam, RDB\_AES\_256\_CBC);
        OH\_Crypto\_SetHmacAlgo(newCryptoParam, RDB\_HMAC\_SHA512);
        OH\_Crypto\_SetKdfAlgo(newCryptoParam, RDB\_KDF\_SHA512);
        OH\_Crypto\_SetCryptoPageSize(newCryptoParam, 4096);
        errCode = OH\_Rdb\_RekeyEx(store, newCryptoParam);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        OH\_Rdb\_DestroyCryptoParam(newCryptoParam);
        config = NULL;
        store = NULL;
        crypto = NULL;
        newCryptoParam = NULL;
        
    -   Scenario 5: The original database is an encrypted database. Change it to a non-encrypted database.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, true);
        
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_DestroyConfig(config);
            OH\_Rdb\_CloseStore(store);
            config = NULL;
            store = NULL;
            return;
        }
        OH\_Crypto\_SetEncryptionAlgo(crypto, RDB\_PLAIN\_TEXT);
        errCode = OH\_Rdb\_RekeyEx(store, crypto);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        config = NULL;
        store = NULL;
        crypto = NULL;
        
    -   Scenario 6: The original database is a non-encrypted database. Change it to an encrypted database.
        
        OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
        OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
        OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
        OH\_Rdb\_SetStoreName(config, "RdbTest.db");
        OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
        OH\_Rdb\_SetModuleName(config, "entry");
        OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
        OH\_Rdb\_SetEncrypted(config, false);
        
        int errCode = 0;
        OH\_Rdb\_Store \*store = OH\_Rdb\_CreateOrOpen(config, &errCode);
        if (store == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
            OH\_Rdb\_DestroyConfig(config);
            config = NULL;
            return;
        }
        OH\_Rdb\_CryptoParam \*crypto = OH\_Rdb\_CreateCryptoParam();
        if (crypto == NULL) {
            OH\_LOG\_ERROR(LOG\_APP, "Create crypto failed.");
            OH\_Rdb\_DestroyConfig(config);
            OH\_Rdb\_CloseStore(store);
            config = NULL;
            store = NULL;
            return;
        }
        OH\_Crypto\_SetEncryptionAlgo(crypto, RDB\_AES\_256\_CBC);
        OH\_Crypto\_SetHmacAlgo(crypto, RDB\_HMAC\_SHA512);
        OH\_Crypto\_SetKdfAlgo(crypto, RDB\_KDF\_SHA512);
        OH\_Crypto\_SetCryptoPageSize(crypto, 2048);
        errCode = OH\_Rdb\_RekeyEx(store, crypto);
        
        if (errCode != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "RekeyEx failed, errCode: %{public}d", errCode);
        }
        // After OH\_Rdb\_RekeyEx is used, use new parameters to reopen the database.
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store);
        OH\_Rdb\_DestroyCryptoParam(crypto);
        config = NULL;
        store = NULL;
        crypto = NULL;
