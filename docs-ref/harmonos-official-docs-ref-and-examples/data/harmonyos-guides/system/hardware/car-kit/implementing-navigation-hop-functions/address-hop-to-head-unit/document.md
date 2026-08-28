# Address Hop to Head Unit

This capability enables users to transfer address text on their phone to a specified map app on the head unit.

#### Use Cases

Tap for address hop: When a user is on an address text screen on their phone, tapping the phone against a specified area on the vehicle's central display will transfer the address data from the phone to the head unit's map app and initiate address search.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/T1b4ajKpQqmrUKZKuUF2lA/en-us_image_0000002513696327.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB2C58433A0F3614EBC499BA10C6FF2769CA5C053E29888AD6BAD31F2006B42A "Click to enlarge")

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[accessibilityTextHint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitytexthint12)(value: string): T

 | 

Sets the accessibility text hint.

 |

## Value Description

The value is a JSON string consisting of the attributes described in the following table.

| 
Attribute

 | 

Description

 |
| :-- | :-- |
| 

type

 | 

Text type, which must be **location**.

 |
| 

groupId

 | 

Address group ID, which is used to group multiple address texts. Address texts in the same group will be automatically combined after being transferred to the head unit.

 |
| 

index

 | 

Address index, which is used to identify the sequence of address texts in the same group. Address texts in the same group will be combined into a complete address in ascending order of indexes after being transferred to the head unit.

Example: 'XXX Street' + 'XXX Mall' = 'XXX Street XXX Mall'

 |

You can use the address hop capability after setting **accessibilityTextHint** for the address text on the phone.

#### Development Procedure

1.  Configure the capabilities.
    
    In the scenario of tap for address hop, set **name** in the metadata to **carHopCapability** and set **value** to **carHopAddress**. For details, please refer to [Configuring Capabilities](../../getting-started/document.md#section239110365269). The sample code is as follows:
    
    "metadata": \[
      {
        "name": "carHopCapability",
        "value": "carHopAddress"
      }
    \]
    
2.  Define the value of **accessibilityTextHint**.
    
    const hintContentValue = JSON.stringify({
       type: 'location', // Type, which must be **location**.
       groupId: 1, // Group ID.
       index: 2, // Index.
     });
    
3.  Set **accessibilityTextHint** for the address text.
    
    Text('xxx 1st Road')
       .fontSize(20)
       .fontWeight(FontWeight.Bold)
       .accessibilityTextHint(hintContentValue)
    
    // Single-address scenario.
    Text('xxx 2nd Road')
       .accessibilityTextHint(JSON.stringify({ type: 'location' }))
     
    // Multi-address scenario.
    Text('xxx Mall')
       .accessibilityTextHint(JSON.stringify({ type: 'location', groupId: 1, index: 1, }))
     Text('xxx Street')
       .accessibilityTextHint(JSON.stringify({ type: 'location', groupId: 1, index: 0, }))
