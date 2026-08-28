# Access Control by Device and Data Level (C/C++)

#### When to Use

The access control mechanism ensures secure data storage and sync across devices. When creating a database, you need to correctly set the security label based on the specifications to ensure the consistency between the database content and data labels.

Currently, only RDB stores (C/C++) support hierarchical access control.

#### Basic Concepts

Distributed data management implements access control based on data security labels and device security levels.

A higher data security label and device security level indicate stricter encryption and access control measures and higher data security.

## Data Security Labels

The data can be rated into four security levels as below. For details, see [OH\_Rdb\_SecurityLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-relational-store-h#oh_rdb_securitylevel).

| Risk Level | Security Level | Definition | Example |
| :-- | :-- | :-- | :-- |
| Critical | S4 | Special data types defined by industry laws and regulations, involving the most private individual information or data that may cause severe adverse impact on an individual or group once disclosed, tampered with, corrupted, or destroyed. | Political opinions, religious and philosophical belief, trade union membership, genetic data, biological information, health and sexual life status, sexual orientation, device authentication, and personal credit card information |
| High | S3 | Data that may cause critical adverse impact on an individual or group once disclosed, tampered with, corrupted, or destroyed. | Individual real-time precise positioning information and movement trajectory |
| Moderate | S2 | Data that may cause major adverse impact on an individual or group once disclosed, tampered with, corrupted, or destroyed. | Detailed addresses and nicknames of individuals |
| Low | S1 | Data that may cause minor adverse impact on an individual or group once disclosed, tampered with, corrupted, or destroyed. | Gender, nationality, and user application records |

## Device Security Levels

Device security levels are classified into SL1 to SL5 based on devices' security capabilities, for example, whether a Trusted Execution Environment (TEE) or a secure storage chip is available. Watches are SL1 (lower security) devices, and phones and tablets are SL4 (higher security) devices.

During device networking, you can run the hidumper -s 3511 command to query the device security level.

#### Access Control Mechanism in Cross-Device Sync

In cross-device data sync, data access is controlled based on the device security level and data security labels. In principle, data can be synced only to the devices whose data security labels are not higher than the device's security level. The access control matrix is as follows.

| Device Security Level | Data Security Labels of the Synchronization Device |
| :-- | :-- |
| SL1 | S1 |
| SL2 | S1 to S2 |
| SL3 | S1 to S3 |
| SL4 | S1 to S4 |
| SL5 | S1 to S4 |

For example, watches are SL1 (lower security) devices. The database with data security label S1 can be synced between these devices, but the databases with database labels S2-S4 cannot.

#### How to Develop

When creating an RDB store, call the **OH\_Rdb\_SetSecurityLevel** API to specify the security level of the RDB store. The following example shows how to create an RDB store with security level of SL3.

1.  Add the following library to **CMakeLists.txt**.
    
    libnative\_rdb\_ndk.z.so
    
2.  Include header files.
    
    #include <cstring>
    #include "database/rdb/relational\_store.h"
    #include "hilog/log.h"
    
3.  Call **OH\_Rdb\_SetSecurityLevel** to set the database security level.
    
    OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
    OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el2/database");
    OH\_Rdb\_SetStoreName(config, "RdbTest.db");
    OH\_Rdb\_SetBundleName(config, "com.example.nativedemo");
    OH\_Rdb\_SetModuleName(config, "entry");
    // Set the security level of the database.
    OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
    OH\_Rdb\_SetEncrypted(config, false);
    OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL2);
        
    int errCode = 0;
    OH\_Rdb\_Store \*store\_ = OH\_Rdb\_CreateOrOpen(config, &errCode);
    OH\_Rdb\_CloseStore(store\_);
    store\_ = nullptr;
    OH\_Rdb\_DestroyConfig(config);
    config = nullptr;
