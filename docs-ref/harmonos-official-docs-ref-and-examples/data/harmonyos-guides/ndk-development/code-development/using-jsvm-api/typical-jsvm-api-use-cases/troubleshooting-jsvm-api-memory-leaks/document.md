# Troubleshooting JSVM-API Memory Leaks

JSVM memory usage includes native memory usage (C/C++ memory usage) and heap memory usage of the underlying JavaScript engine. Heap memory is used for maintaining a heap and its lifecycle to manage generated JavaScript objects by the JavaScript engine. Other memory is called native memory. When using the JSVM, you may encounter the two types of memory exceptions.

This topic describes how to determine the memory leak type and how to locate the native memory leak and JavaScript engine heap memory leak.

#### Determining the Memory Leak Type

You can use hdc to connect to the device, run the following command to sample the memory of the target application, and compare the memory changes within a period of time to determine whether the native memory leaks or JavaScript memory leaks. In the **Pss Total** column in the following figure, **native heap** indicates the native memory usage, and **AnonPage other** indicates the JavaScript heap memory usage.

hidumper --mem $(pidof dest\_app)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Bkfb5fN6QqihINDWSAutAw/en-us_image_0000002568765025.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B5BAFE8AF51BB66741070345B337162172B4FFFC1E4B1F6AF8E849E426EEB0E)

#### Locating Native Memory Leaks

## When to Use

1.  **OH\_JSVM\_CreateReference** and **OH\_JSVM\_DeleteReference** are not called in pairs. As a result, references are not released.

JSVM\_Value obj = nullptr;
OH\_JSVM\_CreateObject(env, &obj);
// Create a reference.
JSVM\_Ref reference;
OH\_JSVM\_CreateReference(env, obj, 1, &reference);

// Use the reference.
JSVM\_Value result;
OH\_JSVM\_GetReferenceValue(env, reference, &result);

// The reference is not released.
// OH\_JSVM\_DeleteReference(env, reference);

## How to Locate

To analyze native memory leaks, you can use the memory analysis module of DevEco Studio. For details, see [Memory Analysis and Optimization](../../../../../performance-optimization/memory-analysis-allocation/overview/document.md).

1.  Use the **Allocation** module of Profiler to record the native memory information within a period of time.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/qa-DPfTPT6SlBtUIpZD7ZA/en-us_image_0000002537765300.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFF0996B20FB08C22FB2D4252E67CA23B9867232634C6831C3C5462BDDDEA91D)
2.  Compare the memory changes in **Created & Existing** during this period. If the unreleased memory accounts for a large proportion and the value of **Count** is large, a memory leak may occur. In this case, check the call stack.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/l0oHHbl7S6GIK44jWp_o-A/en-us_image_0000002537925240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC876FE838C995D3157A167DD25AA36AAB3833DE1DFA759E85AB49265C0F6228)

#### Locating JavaScript Engine Heap Memory Leaks

## When to Use

1.  Global variables are misused. As a result, DOM elements are not released.

const elements = \[\];
function createElements() {
  for (let i = 0; i < 1000; i++) {
    const el = document.createElement('div');
    document.body.appendChild(el);
    elements.push(el); // Even if the element is removed from the DOM, the array still holds the reference.
  }
}

## How to Locate

Currently, JSVM provides OH\_JSVM\_OpenInspector to enable the inspector. For details, see [Using OH\_JSVM\_OpenInspector](../jsvm-api-debugging/document.md#using-oh_jsvm_openinspector) and [Using Chrome Inspect](../jsvm-api-debugging/document.md#using-chrome-inspect).

Use DevTools to take a snapshot of the heap memory in the target scenario (click the garbage collection button above before taking a snapshot). Compare the snapshots to find the unreleased JavaScript objects and their locations in the source code to further locate the cause of the unreleased heap memory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ickbM8e3RimMGrQjFM-x9Q/en-us_image_0000002568685017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0D83AB2EB1E7986E72CDF79EDEC29C5F57A95B7E486205FE3C0EE2FED0DFB8F)
