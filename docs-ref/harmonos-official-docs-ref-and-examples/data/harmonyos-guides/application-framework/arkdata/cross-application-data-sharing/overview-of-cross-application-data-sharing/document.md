# Overview of Cross-Application Data Sharing

#### Introduction

HarmonyOS provides APIs for an application to manage its own data and share data with other applications.

Data needs to be shared in a wealth of scenarios. For example, the Contacts, short message service (SMS), and Gallery data always needs to be shared with other applications. However, certain data, such as accounts and passwords, cannot be shared. Some data, such as SMS messages, can be queried but not modified by other applications. Therefore, a secure and efficient cross-application data sharing mechanism for different data sharing scenarios and data privacy protection is very important.

Currently, HarmonyOS supports one-to-many and many-to-many cross-application data sharing, based on the number of the data provider applications involved.

#### Basic Concepts

Before you start, understand the following concepts:

-   **Data provider**: an application that provides data and implements related services. It is also called the producer or server.
    
-   **Data consumer**: an application that accesses the data or services provided by the data provider. It is also called the client.
    
-   **ValuesBucket**: a set of data to be inserted. It can be one or more data records in key-value (KV) pairs. In each KV pair, the key must be of the string type, and the value can be a number, a string, a Boolean value, or an unsigned integer array.
    
-   **ResultSet**: a set of query results. It provides flexible modes for users to obtain various data.
    
-   **Predicates**: an object that specifies the conditions for updating, deleting, or querying data in a database.
    

#### One-to-Many Cross-Application Data Sharing

You can use **DataShare** to implement one-to-many data sharing across applications. **DataShare** implements data sharing between data providers and data consumers. The following describes the implementation modes.

## Implementation

The data provider can directly use **DataShare** to share data with other applications without complex encapsulation. The data consumer only needs to use a set of APIs because the **DataShare** access mode does not vary with the data provision mode. This greatly reduces the learning time and development difficulty.

**DataShare** implements cross-application data sharing in either of the following ways:

-   Using DataShareExtensionAbility：It is available only to system applications. Related content and guidance are not provided.
    
-   Using Silent Access via the DatamgrService: It is available only to system applications. Related content and guidance are not provided.
    
-   [Sharing Configurations Between Applications](../one-to-many-data-sharing/sharing-configurations-between-applications-arkts/document.md)
    
    You need to manage common configuration information in a centralized manner and share the configurations between different applications to improve collaboration efficiency.
    

## Constraints

-   Currently, **dataShare** supports development based on the stage model only.

#### Many-to-Many Cross-Application Data Sharing

In one-to-many cross-application data sharing, there is only one data provider. In many-to-many cross-application data sharing, you need to consider data definition, data exchange, and permission management. The UDMF provides a new data sharing and interaction mode to implement many-to-many cross-application data sharing.

## Implementation

[Sharing Data via Unified Data Channels](../many-to-many-data-sharing/sharing-data-via-unified-data-channels-arkts/document.md)

Applications can call the APIs provided by the UDMF to write data that complies with the unified data definition to different data sharing channels of the UDMF. The data in these channels can be read by other applications. The data written into the UDMF is managed based on the permissions of the application, permissions of the data channels, and the permission management logic of the UDMF. Lifecycle management is also performed on the data written into the channels in the same way. In this way, the data scattered in each application is aggregated via different channels of the UDMF, improving the development efficiency and data experience of users.
