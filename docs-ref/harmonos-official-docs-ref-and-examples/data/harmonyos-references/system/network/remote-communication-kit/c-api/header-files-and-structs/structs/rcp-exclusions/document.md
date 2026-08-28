# Rcp\_Exclusions

#### Overview

URLs excluded from proxy processing.

If [Rcp\_Request.url](../rcp-request/document.md#a39a1cc0a1ad666d8d9ad40eec4b52de7) matches a pattern defined in [Rcp\_Exclusions](#), [Rcp\_Request](../rcp-request/document.md) will not go through proxy processing.

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Rcp\_ExclusionsValueType](../../../modules/remotecommunication/document.md#ga1f5ed8748d80bca8e803ea26d63d1ecf) [type](#adea8e4bddc87a6c451c94abbec909fbe)

 | 

Data type used in the union structure.

 |
| 

union {

 | 

Union structure.

 |
| 

[Rcp\_Urls](../rcp-urls/document.md) \* [urls](#abd535558039767647290d03621389486)

 | 

URLs stored in the data chain.

 |
| 

[Rcp\_ExclusionFunction](../../../modules/remotecommunication/document.md#gac6517b72e4a8c0feaf864f3669d2c127) [exclusionFunction](#ad99a237a7685adc45de3d3a728112922)

 | 

Callback function used to filter out URLs.

 |
| 

} **data**

 | 

The **type** variable defines the data type used in **data**.

 |

#### Member Variable Description

#### \[h2\]exclusionFunction

[Rcp\_ExclusionFunction](../../../modules/remotecommunication/document.md#gac6517b72e4a8c0feaf864f3669d2c127) Rcp\_Exclusions::exclusionFunction

**Description**

Callback function used to filter out URLs.

#### \[h2\]type

[Rcp\_ExclusionsValueType](../../../modules/remotecommunication/document.md#ga1f5ed8748d80bca8e803ea26d63d1ecf) Rcp\_Exclusions::type

**Description**

Data type used in the union structure.

#### \[h2\]urls

[Rcp\_Urls](../rcp-urls/document.md)\* Rcp\_Exclusions::urls

**Description**

URLs.
