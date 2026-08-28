# PrivacyManagerService

PrivacyManagerService is a command line capability developed based on [hidumper](../hidumper/document.md) for access control. It can display basic access control information and obtain the usage records of sensitive permissions.

#### Environment Setup

Set up the environment by referring to [Environment Setup](../hidumper/document.md#environment-setup).

#### Obtaining Help Information

To view the help information, run the following command:

hidumper -s PrivacyManagerService -a '-h'

**Example**

\-------------------------------\[ability\]-------------------------------

----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
Usage:
       -h: command help
       -t <TOKEN\_ID>: according to specific token id dump permission used records

#### Obtaining Sensitive Permission Usage Records

You can run the following command to view the sensitive permission usage records by token ID of an application process:

hidumper -s PrivacyManagerService -a '-t <tokenId>'

You can run the [atm-tool](../../../../debugging-commands/access-token-manager/document.md#dump) command to query the token ID required by the command.

**Example**

hidumper -s PrivacyManagerService -a '-t 536992218'

-------------------------------\[ability\]-------------------------------

----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
{
  "permissionRecord": \[
    {
      "bundleName": "com.ohos.camera",
      "isRemote": false,
      "permissionName": "ohos.permission.READ\_IMAGEVIDEO",
      "lastAccessTime": 1508577149393,
      "lastAccessDuration": 0,
      "accessCount": 2
    }
  \]
}
