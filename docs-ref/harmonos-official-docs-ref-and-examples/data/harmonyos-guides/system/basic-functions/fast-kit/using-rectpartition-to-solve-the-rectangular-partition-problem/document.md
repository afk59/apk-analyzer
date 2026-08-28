# Using RectPartition to Solve the Rectangular Partition Problem

The Rectangular Partition Solver is used to solve the rectangular partition problem. It takes a set of non-overlapping rectangle as input (focusing on the union of these areas) and computes a rectangular partitioning scheme to generate a minimum number of rectangles that cover the same total area (but not guaranteed to be optimal). The following is an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/IL5GwKwRRXaVIy-MzIHWyQ/en-us_image_0000002525433057.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE99058EA572F0B49A382AA3C3A5921FFE8285ABD338F2D40C0589F5019254A2 "Click to enlarge")

A rectangle (![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/jZPOLlRdQrenTszEmsEKhQ/en-us_formulaimage_0000002485707398.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66DB1B0F5B58896D1A5D81259DF10CB6F863A6CFEB842E694C001DE6291BBBE3 "Click to enlarge")) is a set of all unit rectangles within a 2D grid that satisfy the requirements of ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/I1FIH4M5R664ipvFA5aImw/en-us_formulaimage_0000002517707611.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CF4A31E78BFFEEA01DDE6F0EA2682223EBDFB4A697F295EF78C615582CCCC79 "Click to enlarge"). (Coordinate system: X-axis increases from left to right; Y-axis increases from top to bottom.) Two rectangles intersect if and only if they share at least one common unit rectangle.

In the rectangular partition problem, given _N_ non-overlapping rectangles, the task is to output _M_ rectangles that satisfy the following conditions:

-   All _M_ output rectangles must be mutually non-overlapping.
-   The union of the _M_ output rectangles must be identical to the union of the _N_ input rectangles.
-   The number of output rectangles, _M_, should be minimized as much as possible.

The Rectangular Partition Solver operates with a time complexity of ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/VX2F-ZdVQN-ZXVlwd1nWiw/en-us_formulaimage_0000002480520950.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C1BBCFBB488E38CFD91A4E156DA8ACA726AC0376A720E6F5D7F41ACB04C5384 "Click to enlarge"), enabling the efficient processing of large-scale input data. In optimization scenarios such as grid data processing and spatial geometry computation, the Rectangular Partition Solver can be used to enhance area processing efficiency and reduce spatial redundancy.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_CreateConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga051634633006a8f12665a412dc96687e) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gabd3bea5600684d0638b6221f3d0eb23e) \*\*config)

 | 

Creates the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gae515ef39072676065cef8b9af446f2ac) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gabd3bea5600684d0638b6221f3d0eb23e) \*config)

 | 

Destroys the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_SetAlgo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gaec5519d0974e98f6fe99ab2fa50411cc) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gabd3bea5600684d0638b6221f3d0eb23e) \*config, const char \*name)

 | 

Sets the algorithm used by the Rectangular Partition Solver. Currently, only the **SweepLineAlgo** algorithm is supported, which outputs a set of non-overlapping rectangles with a minimized count (not guaranteed to be optimal), operating at ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/OQBeMMvMTQCeu3TyTEAx9Q/en-us_formulaimage_0000002539334201.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF5D1C180A62151641E2F9E299810B663A9A0671D1585842B9F729F38925F4D7 "Click to enlarge") complexity.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_Solve](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#ga9329484302723a20438eadc9e4b71609) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit-fast#gabd3bea5600684d0638b6221f3d0eb23e) \*config, size\_t size, const [FAST\_Rect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit--fast-rect) \*origin, [FAST\_Rect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/fast-kit--fast-rect) \*result, size\_t \*resultSize)

 | 

Solves the rectangular partition problem under the specified opaque configuration. The function takes a set of non-overlapping rectangles as input and computes a rectangular partitioning scheme to generate a minimum number of rectangles that cover the same total area.

**Note**:

1\. The input must ensure that any two rectangles do not overlap (that is, any two rectangles must satisfy: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/7jP7x46rSaG9GOxgUKP0rA/en-us_formulaimage_0000002496939068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E29C4CED270A9411E144C1435930B3DE3E118C37F69853BD4F1A99D8513C9ED2 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/m3tST0jkRGmyy5UsHfwGDA/en-us_formulaimage_0000002528699027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE9EFDDDF2189A83D09FB2CED8A2BCFA729F12A0A5F640F823BDD734075C9829 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/cw15pvlnSZ2xWQVXIQUsug/en-us_formulaimage_0000002496939070.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64706494A11821543DA2F283C5A3EE7E86E3DCF209F744AFC4B29CFCFC12FF53 "Click to enlarge"), or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/P7I1ey-8QbqBiBbG5POm7Q/en-us_formulaimage_0000002528699029.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12DAF54CBB1E4C0DEEEE3D2EFB416124FCFCBF444AEB87B4F2B7CC90519869EB "Click to enlarge")). Otherwise, the function returns **FAST\_ERROR\_CODE\_ILLEGAL\_INPUT**.

2\. The function ensures that the number of output rectangles is less than or equal to the number of input rectangles.

 |

#### Development Procedure

1.  Link the related dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libfast\_ads.so)
    
2.  Call **HMS\_FAST\_RectPartition\_CreateConfig** to generate the Rectangular Partition Solver configuration instance (**FAST\_RectPartitionConfig**).
3.  Call **HMS\_FAST\_RectPartition\_SetAlgo** to set the solving algorithm to **SweepLineAlgo**.
4.  Call **HMS\_FAST\_RectPartition\_Solve** to compute the rectangular partitioning scheme.
5.  Call **HMS\_FAST\_RectPartition\_DestroyConfig** to destroy the Rectangular Partition Solver configuration instance.

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast\_solver\_rect\_partition.h"

// Define a function to print rectangles.
void print\_rect(const FAST\_Rect\* rect) {
    printf("Rect: left=%d, top=%d, right=%d, bottom=%d\\n",
           rect->left, rect->top, rect->right, rect->bottom);
}

FAST\_ErrorCode rect\_partition\_demo() {
    // Define the input rectangles.
    FAST\_Rect origin\[\] = {
        {1, 4, 1, 6},
        {2, 1, 2, 6},
        {3, 1, 3, 3}
    };
    size\_t size = sizeof(origin) / sizeof(FAST\_Rect);

    // Define the output rectangles.
    FAST\_Rect\* result = (FAST\_Rect\*)malloc(size \* sizeof(FAST\_Rect));
    size\_t result\_size = 0;

    FAST\_RectPartitionConfig\* config = nullptr;
    FAST\_ErrorCode ret;

    do {
        // Create a configuration instance.
        ret = HMS\_FAST\_RectPartition\_CreateConfig(&config);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            printf("Failed to create config: %d\\n", ret);
            break;
        }

        // Set the algorithm.
        ret = HMS\_FAST\_RectPartition\_SetAlgo(config, "SweepLineAlgo");
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            printf("Failed to set algorithm: %d\\n", ret);
            break;
        }

        // Compute the rectangular partitioning scheme.
        ret = HMS\_FAST\_RectPartition\_Solve(config, size, origin, result, &result\_size);
        if (ret != FAST\_ERROR\_CODE\_SUCCESS) {
            printf("Failed to solve: %d\\n", ret);
            break;
        }

        // Print the result.
        printf("Resulting rectangles(result\_size=%ld):\\n", result\_size);
        for (size\_t i = 0; i < result\_size; ++i) {
            print\_rect(&result\[i\]);
        }
        /\*
            Resulting rectangles(result\_size=2):
            Rect: left=1, top=4, right=2, bottom=6
            Rect: left=2, top=1, right=3, bottom=3
        \*/

    } while (0);

    // Destroy the configuration.
    HMS\_FAST\_RectPartition\_DestroyConfig(config);

    // Release the array.
    free(result);

    return ret;
}
