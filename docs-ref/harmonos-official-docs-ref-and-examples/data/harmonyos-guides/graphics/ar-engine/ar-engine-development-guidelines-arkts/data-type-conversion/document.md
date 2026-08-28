# Data Type Conversion

When developing AR apps, certain data types need to be converted before they can be used. Below is a summary along with examples.

#### ArrayBuffer

For methods that do not support receiving the **ArrayBuffer** data type, the data must be deserialized into the int32 or float32 type. The list of APIs requiring the conversion is as follows:

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ImageComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section175993235012)

 | 

The parameter **buffer** is of type ArrayBuffer, which can be converted to int32.

 |
| 

[ARPlane.getPolygonXZ](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section12949442354)

 | 

The return value is of type ArrayBuffer, which can be converted to float32.

 |
| 

[ARSceneMesh.getVertices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section15211205153115)

 | 

The return value is of type ArrayBuffer, which can be converted to float32.

 |
| 

[ARSceneMesh.getVertexNormals](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section4793111183211)

 | 

The return value is of type ArrayBuffer, which can be converted to float32.

 |
| 

[ARSceneMesh.getTriangleIndices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section19221187183218)

 | 

The return value is of type ArrayBuffer, which can be converted to int32.

 |
| 

[ARSemanticDensePointData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1031071863714)

 | 

The parameter **id** is of type ArrayBuffer, which can be converted to int32.

 |
| 

[ARSemanticDensePointData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1031071863714)

 | 

The parameter **position** is of type ArrayBuffer, which can be converted to float32.

 |
| 

[ARSemanticDensePointData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1031071863714)

 | 

The parameter **color** is of type ArrayBuffer, which can be converted to int32.

 |

The following are conversion examples:

// ArrayBuffer to float32
function arrayBufferFloat32ToNumber(buffer: ArrayBuffer): number\[\] {
  let view: Float32Array = new Float32Array(buffer);
  let numberArray: number\[\] = Array.from(view);
  return numberArray;
}

// ArrayBuffer to int32
function arrayBufferInt32ToNumber(buffer: ArrayBuffer): number\[\] {
  let view: Int32Array = new Int32Array(buffer);
  let numberArray: number\[\] = Array.from(view);
  return numberArray;
}
