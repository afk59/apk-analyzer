# Formats of OpenID and UnionID

#### Length

To reduce integration and migration costs, Account Kit adjusted the length limits for OpenID and UnionID on September 21, 2023.

-   OpenID
    -   For apps created at or after 23:00:00 on September 21, 2023, the OpenID will be fixed at 28 characters.
    -   For those created before 23:00:00 on September 21, 2023, the OpenID can contain 1 to 256 characters.
-   UnionID
    -   For developers who registered at or after 23:00:00 on September 21, 2023, the UnionID will be fixed at 29 characters.
    -   For those who registered before 23:00:00 on September 21, 2023, the UnionID can contain 1 to 92 characters.

#### Unique Identifier

1.  When a developer account manages multiple apps, the OpenID returned for the same HUAWEI ID will be different for each app, but the UnionID returned will be the same.
2.  When a developer account manages multiple apps and these apps need to share user information from the same HUAWEI ID, UnionID can be used as the user identifier.

#### Data Type

Both OpenID and UnionID are character strings.

#### Case Sensitivity

OpenID and UnionID are case sensitive.

#### Precautions During Actual Use

When storing, querying, or comparing OpenIDs or UnionIDs, keep their original case.
