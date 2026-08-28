# Access Token Manager

Access Token Manager (atm) is a tool used to query the information such as permission and usage type of an application process. It provides the capability of access control based on the token ID, bundle name, and process name.

#### Environment Setup

Before using this tool, you must obtain [hdc](../../performance-analysis-kit/command-line-tools/hdc/document.md) and run the **hdc shell** command.

#### Commands

| Command | Description |
| :-- | :-- |
| help | Displays the commands supported by the atm tool. |
| dump | Obtains access control data. |

#### help

\# Display the help information.
atm help

#### dump

atm dump \[-h\] \[-t \[-i <token-id>\] \[-b <bundle-name>\] \[-n <process-name>\]\] \[-r \[-i <token-id>\] \[-p <permission-name>\]\] \[-v \[-i <token-id>\] \[-p <permission-name>\]\]

In the following table, **\-t** is mandatory, and **\-i**, **\-b**, **\-n**, and **\-p** are optional. For the **atm dump -t** command, the **\-i**, **\-b**, and **\-n** parameters can be used only separately.

| Parameter | Description |
| :-- | :-- |
| \-d | Queries all permission definitions in the system. This parameter is mandatory. |
| \-d -p <permission-name> | Queries the permission definition based on the permission name. This parameter is optional. |
| \-h | Displays help information. |
| \-t | Queries information about all application processes in the system. This parameter is mandatory. |
| \-t -i <token-id> | Queries the basic information about an application and the corresponding [permission information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#grantstatus) based on the token ID of the application process. |
| \-t -b <bundle-name> | Queries the basic information about an application and the corresponding [permission information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#grantstatus) based on the bundle name of the application process. This parameter is optional. |
| \-t -n <process-name> | Queries the basic information about an application and the corresponding [permission information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#grantstatus) based on the process name of the application process. This parameter is optional. |

Example:

#Query all permission definitions in the system.
atm dump -d

#Query the permission definition by permission name.
atm dump -d -p \*\*\*\*\*\*\*\*\*
# Command output:
# {
#     "permissionName": "ohos.permission.KERNEL\_ATM\_SELF\_USE",
#     "grantMode": "SYSTEM\_GRANT",
#     "availableLevel": "SYSTEM\_CORE",
#     "availableType": "SYSTEM",
#     "distributedSceneEnable": true,
#     "isKernelEffect": true,
#     "hasValue": true,
# }

#Display the help information about the atm dump command.
atm dump -h

#Query the token IDs and bundle names of all application processes in the system.
atm dump -t

#Query the permission information based on the token ID.
atm dump -t -i \*\*\*\*\*\*\*\*\*
# Command output:
# {
#   "tokenID": 672078897,
#   "processName": "samgr",
#   "apl": 2,
#   "permStateList": \[
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED\_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   \]
# }

#Query the permission information based on the bundle name.
atm dump -t -b ohos.telephony.resources
# Command output:
# {
#   "tokenID": 537280686,
#   "tokenAttr": 1,
#   "ver": 1,
#   "userId": 100,
#   "bundleName": "ohos.telephony.resources",
#   "instIndex": 0,
#   "dlpType": 0,
#   "isRemote": false,
#   "isPermDialogForbidden": false,
#   "permStateList": \[
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED\_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   \]
# }

#Query the permission information based on the process name.
atm dump -t -n \*\*\*\*\*\*\*\*\*
