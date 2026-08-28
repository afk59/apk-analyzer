# Using SegmentMap to Query and Maintain Range Information

FAST Kit provides the Segment Map to query and maintain range information, implementing efficient range queries and updates for data sequences. As a data structure designed for efficient management of range information, the Segment Map is well suited for scenarios requiring frequent statistical analysis or modifications over specific data segments. Its typical operations include point updates, range updates, and range queries.

While there are multiple ways to implement Segment Maps, the most common method uses a binary tree, frequently referred to as a Segment Tree. Compared with direct range traversal, the Segment Map optimizes the time complexity of many range operations from ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ZXa1HqPdTjKuXapW6Kt9Sw/en-us_formulaimage_0000002497557050.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B03AE34B9536217691BCF62027E94DD0EDEADAF96F0475542FFEE4A80E6B5C27 "Click to enlarge") to ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/FGi0Re15SRORhzjrppv4Bg/en-us_formulaimage_0000002529117051.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=188D64524C5B8CE311681BD6784598CD1FDCDB096EBB5A16884EFE86E25AE103 "Click to enlarge"). This provides a significant advantage when handling large-scale data, serving as the data structure foundation for building high-performance and responsive applications.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_CreateConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga3c5e1b0e64894e3a8910c06800afe560) ([FAST\_SegmentMapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*\*config)

 | 

Creates the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga54dc92174e74665cd52b96dd0dc99e45) ([FAST\_SegmentMapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Destroys the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetQueryType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga14043280774888f1d2a34951f27415ae) ([FAST\_SegmentMapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapQueryType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga8ef2e816f027493a63bd4e82876f233f) type)

 | 

Sets the query type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetUpdateType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga1f37b6071a0af42c8e217cc0bf2bda2a) ([FAST\_SegmentMapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapUpdateType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga2747e3df771507eaeff23cc28f17fc76) type)

 | 

Sets the update type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga1e6c63ee4731e04eeac80a64246db037) ([FAST\_SegmentMapHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga3c42403e7c9306245dd1340f166993d9) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Creates a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gaf24e3e9e42dbf8e6fd7092762ffdf894) ([FAST\_SegmentMapHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga3c42403e7c9306245dd1340f166993d9) handle)

 | 

Destroys a Segment Map instance and deallocates memory. Calling this API again after destruction is considered undefined behavior.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gae85d6f1561a1c4bab0c9161401db07fe) ([FAST\_SegmentMapHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t value)

 | 

Performs a range update (value assignment, addition, or subtraction) on a Segment Map based on the configuration.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga13129191dae4340dccb99132f54d4055) ([FAST\_SegmentMapHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t \*result)

 | 

Performs a range query on a Segment Map to return statistics like the maximum, minimum, or sum based on the configuration.

 |

#### Development Procedure

1.  Link the related dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libfast\_ads.so)
    
2.  Call **HMS\_FAST\_SegmentMap\_CreateConfig** to generate a Segment Map configuration instance (**FAST\_SegmentMapConfig**).
3.  Call **HMS\_FAST\_SegmentMap\_SetQueryType** to set the query type.
4.  Call **HMS\_FAST\_SegmentMap\_SetUpdateType** to set the update type.
5.  Call **HMS\_FAST\_SegmentMap\_Create** to generate a Segment Map instance (**FAST\_SegmentMapHandle**). After the instance is generated, the query and update types cannot be changed.
6.  Call **HMS\_FAST\_SegmentMap\_Query** to perform efficient range queries.
7.  Call **HMS\_FAST\_SegmentMap\_Update** to perform efficient range updates.
8.  Call **HMS\_FAST\_SegmentMap\_Destroy** to destroy the Segment Map instance.
9.  Call **HMS\_FAST\_SegmentMap\_DestroyConfig** to destroy the Segment Map configuration instance.

#include <cassert>
#include <iostream>
#include "FASTKit/fast\_ads\_segment\_map.h"

FAST\_ErrorCode demoSegmentMapSumSet()
{
    FAST\_SegmentMapConfig \*config = nullptr;
    FAST\_SegmentMapHandle handle = nullptr;
    int32\_t \*array = nullptr;
    FAST\_ErrorCode ret;

    ret = HMS\_FAST\_SegmentMap\_CreateConfig(&config);
    if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
        return ret;
    }

    do {
        // Initialize configuration.
        ret = HMS\_FAST\_SegmentMap\_SetQueryType(config, FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }

        ret = HMS\_FAST\_SegmentMap\_SetUpdateType(config, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }

        // Initialize the array.
        size\_t size = 10;
        array = new int32\_t\[size\];
        for (size\_t i = 0; i < size; ++i) {
            array\[i\] = i + 1;
        }
        // array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        // Create a Segment Map instance.
        ret = HMS\_FAST\_SegmentMap\_Create(&handle, size, array, config);
        // The initial Segment Map is {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }

        int32\_t result;

        // First query: Query the sum of the range \[0, 5).
        ret = HMS\_FAST\_SegmentMap\_Query(handle, 0, 5, &result);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        assert(result == 15);  // 1 + 2 + 3 + 4 + 5 = 15

        // First update: Set each element in the range \[3, 7) to -1.
        ret = HMS\_FAST\_SegmentMap\_Update(handle, 3, 7, -1);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        // The Segment Map is updated to {1, 2, 3, -1, -1, -1, -1, 8, 9, 10}.

        // Second query: Query the sum of the range \[0, 5).
        ret = HMS\_FAST\_SegmentMap\_Query(handle, 0, 5, &result);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        assert(result == 4);  // 1 + 2 + 3 - 1 - 1 = 4

        // Second update: Set each element in the range \[5, 9) to 2.
        ret = HMS\_FAST\_SegmentMap\_Update(handle, 5, 9, 2);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        // The Segment Map is updated to {1, 2, 3, -1, -1, 2, 2, 2, 2, 10}.

        // Third query: Query the sum of the range \[0, 10).
        ret = HMS\_FAST\_SegmentMap\_Query(handle, 0, 10, &result);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        assert(result == 22);  // 1 + 2 + 3 -1 -1 + 2 + 2 + 2 + 2 + 10 = 22

        // Third update: Set each element in the range \[0, 3) to 0.
        ret = HMS\_FAST\_SegmentMap\_Update(handle, 0, 3, 0);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        // The Segment Map is updated to {0, 0, 0, -1, -1, 2, 2, 2, 2, 10}.

        // Fourth query: Query the sum of the range \[3, 7).
        ret = HMS\_FAST\_SegmentMap\_Query(handle, 3, 7, &result);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        assert(result == 2);  // -1 -1 + 2 + 2 = 2

        // Fourth update: Set each element in the range \[7, 10) to 5.
        ret = HMS\_FAST\_SegmentMap\_Update(handle, 7, 10, 5);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        // The Segment Map is updated to {0, 0, 0, -1, -1, 2, 2, 5, 5, 5}.

        // Fifth query: Query the sum of the range \[0, 10).
        ret = HMS\_FAST\_SegmentMap\_Query(handle, 0, 10, &result);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            break;
        }
        assert(result == 17);  // 0 + 0 + 0 -1 -1 + 2 + 2 + 5 + 5 + 5 = 17
    } while (0);

    // Destroy the Segment Map instance.
    HMS\_FAST\_SegmentMap\_Destroy(handle);

    // Destroy the configuration.
    HMS\_FAST\_SegmentMap\_DestroyConfig(config);

    // Release the array.
    if (array) {
        delete\[\] array;
    }

    return ret;
}
