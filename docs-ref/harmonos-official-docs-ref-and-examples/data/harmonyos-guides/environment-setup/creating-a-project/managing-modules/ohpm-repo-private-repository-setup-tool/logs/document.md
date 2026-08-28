# Logs

Like any web application, ohpm-repo has a built-in logger that defines four log types.

#### Access Log – access.log

An access log contains the operation time, server IP address, operation source, operation result, and requested API or static resource. A maximum of 180 access logs can be stored.

#### Operation Log – operate.log

An operation log contains the operation time, log level, operator (**userId**), terminal IP address (**ip**), operation resource (**resource**), operation method (**event**), and operation result (**result**). A maximum of 180 operation logs can be stored.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/c0cDaEmoSCqI0FAdNoxCJg/en-us_image_0000002532748667.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CB8231330815D13462805C5A6B52E4C33D2BF940EE0D1061260B66009DC7F9F "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/zs55Ew2MQhyP4cnf3byjEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D5930364D5610237342A4D7AA6B32960675CD6B228547365D9A2369045C05A6)

**Operation method (event)**: When an operation is performed on the ohpm-repo management page, a piece of operation data is generated in the **operate.log** file. The operation method indicates the name of the method involved in the current operation. For example, **login** indicates the login operation, and **analyzePackage** indicates the package parsing operation performed during upload.

**Table 1** Common operation methods
| 
No.

 | 

Event

 | 

Description

 |
| :-- | :-- | :-- |
| 

1

 | 

generateAccessToken/deleteAccessToken

 | 

Generates or deletes an AccessToken item.

 |
| 

2

 | 

login/logout

 | 

Logs in or logs out.

 |
| 

3

 | 

publish / unPublish/batchUnPublish

 | 

Publishes, unpublishes, or batch unpublishes resource packages.

 |
| 

4

 | 

addGroup/deleteGroup

 | 

Adds or deletes an organization.

 |
| 

5

 | 

updateGroup

 | 

Updates an organization.

 |
| 

6

 | 

addMember/deleteMember

 | 

Adds or deletes an organization member.

 |
| 

7

 | 

addAdminMember/deleteAdminMember

 | 

Adds or deletes an organization administrator.

 |
| 

8

 | 

addPublicKey / delPublicKeyById

 | 

Adds or deletes a public key.

 |
| 

9

 | 

addRepo/updateRepo/deleteRepo

 | 

Adds, updates, or deletes a repository.

 |
| 

10

 | 

analyzePackage

 | 

Parses an uploaded package file.

 |
| 

11

 | 

uploadPackage

 | 

Uploads a file.

 |
| 

12

 | 

getPackageSizeLimit

 | 

Gets the maximum size of a package.

 |
| 

13

 | 

addUplink/deleteUplink

 | 

Adds or deletes an uplink item.

 |
| 

14

 | 

updateUplink

 | 

Updates an uplink item.

 |
| 

15

 | 

updateUplinkProxy

 | 

Updates the uplink proxy.

 |
| 

16

 | 

addUser / delUserByUserId

 | 

Adds or deletes a user.

 |
| 

17

 | 

changePassWord

 | 

Changes the password of a user account

 |
| 

18

 | 

resetPassWord

 | 

Resets the password of a user account

 |
| 

19

 | 

changeRole

 | 

Changes a user role (administrator or non-administrator).

 |
| 

20

 | 

register

 | 

Registers an account.

 |
| 

21

 | 

resetKey

 | 

Resets the system key.

 |
| 

22

 | 

addPackagePermissionOwner/deletePackagePermissionOwner/transferPackagePermissionOwner

 | 

Adds, deletes, or changes a package owner.

 |
| 

23

 | 

addPackagePermissionMaintainer/deletePackagePermissionMaintainer

 | 

Adds or deletes a package maintainer.

 |
| 

24

 | 

addPackagePermissionVisitor/deletePackagePermissionVisitor

 | 

Adds or deletes a package trustlist user.

 |
| 

25

 | 

editPackageReadPolicy

 | 

Sets the package visibility.

 |

#### Run Log – run.log

A run log contains the operation time, log level, and log information. A maximum of 30 run logs can be stored. Run logs define log levels: all, trace, debug, info, warn, error, fatal, mark, and off.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/8fHZFF7IQpS4In9_batoLA/en-us_image_0000002500908808.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AA4A8F8C0B92C905A013E65E68FC1DF4D253921EACF53EE3D3CFC005E45AF09 "Click to enlarge")

#### Run Error Log – RepoError.log

When ohpm-repo is running, all error logs generated in the **run.log** file are recorded in the **repoError.log** file. The **repoError.log** file is a collection of error logs. The log printing levels are the same as those of the **run.log** file.

#### Download Error Log

When a package fails to be downloaded from the repository, the repository generates an error log and records it in the **downloadfailure** table in the database. When the SFTP storage service is configured for ohpm-repo, an error log is generated and saved when the package fails to be downloaded from any SFTP service. Each log has a **handled** flag. If the value of **handled** is **0**, the log has been processed. If the value of **handled** is **1**, the log has not been processed.

#### Log Storage Path

The default log storage path is **./logs**. If a relative path is used, it is resolved based on the ohpm-repo deployment root directory ([deploy\_root](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root)).

#### Log Printing Levels

You can set the printing levels of access, operation, and run logs in the configuration file. Only logs whose levels are not lower than the set level are printed. The log levels are all, trace, debug, info, warn, error, fatal, mark, and off in ascending order.

loglevel\_run: info
loglevel\_operate: info
loglevel\_access: info
