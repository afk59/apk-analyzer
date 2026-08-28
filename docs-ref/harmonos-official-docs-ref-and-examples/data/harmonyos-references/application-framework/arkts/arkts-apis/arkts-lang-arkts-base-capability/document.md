# @arkts.lang (ArkTS Base Capability)

The module provides the basic type definition of ArkTS. Currently, the **ISendable** interface is provided.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-KnjMHAoRH6T05S3f_6_aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E8FA31E5DD63A60A5B37CEBFDC533AA7BE7CFE5E297A6C68387C06C130CE519)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

This module can be imported only to ArkTS files (with the file name extension .ets).

#### Modules to Import

import { lang } from '@kit.ArkTS';

#### lang.ISendable

Parent type of all sendable types except null and undefined. It does not have any necessary methods or properties.

An **ISendable** object is an instance of the Object type in ArkTS.

**ISendable** is mainly used when you want to customize the sendable data structure. Container types in the ArkTS common library implicitly inherit and implement **ISendable**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Example**

// Construct a custom sendable data structure.
@Sendable
class CustomData implements lang.ISendable {
    data1: number;
    data2: string;
    constructor(data1: number, data2: string) {
        this.data1 = data1;
        this.data2 = data2;
    }
}
