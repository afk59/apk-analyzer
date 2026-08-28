# Module Description

The collections module provides ArkTS containers for efficient data transfer in concurrency scenarios. The ArkTS containers provide similar functionalities as their JavaScript counterparts, except that their properties cannot be added or updated through . or \[\].

By default, ArkTS containers are passed by reference between concurrent instances. This means that multiple concurrent instances can simultaneously operate the same container instance. Pass-by-copy is also supported. In this mode, each concurrent instance holds an ArkTS container instance.

ArkTS containers are not thread-safe. They adopt the fail-fast approach. An exception is thrown if multiple concurrent instances make structural changes to a container instance at the same time. Therefore, in multi-thread read/write scenarios, you must use the ArkTS asynchronous lock to ensure secure access to the ArkTS containers.

Currently, the following ArkTS containers are provided: [Array](../class-array/document.md), [Map](../class-map/document.md), [Set](../class-set/document.md), TypedArray ([Int8Array](../class-int8array/document.md), [Uint8Array](../class-uint8array/document.md), [Int16Array](../class-int16array/document.md), [Uint16Array](../class-uint16array/document.md), [Int32Array](../class-int32array/document.md), [Uint32Array](../class-uint32array/document.md), [Uint8ClampedArray](../class-uint8clampedarray/document.md) and [Float32Array](../class-float32array/document.md)), [ArrayBuffer](../class-arraybuffer/document.md), [BitVector](../class-bitvector/document.md), and [ConcatArray](../interface-concatarray/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/dzz2o9tzRJCkrIzXjqLsjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062221Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF0585D329C85EB000B84D61CC8246CA430F69B1DFF158D510E8B167C214DE1F)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module can be imported only to ArkTS files (with the file name extension .ets).
    

#### Modules to Import

import { collections } from '@kit.ArkTS';
