# Analyzing the ArkTS Memory Leak

This section explains how to identify potential ArkTS memory leaks in an app and determine their root causes by comparing memory snapshots.

#### Identifying Memory Issues

1.  Use the real-time monitoring feature to observe the app's memory usage. (For details, see [Real-Time Monitoring for Problem Demarcating](../../using-deveco-profiler/real-time-monitoring-for-problem-demarcating/document.md).) Interact with the app and observe the memory usage changes. If memory usage remains stable or returns to a normal level after a temporary increase, the app likely does not have a memory leak. If memory usage continues to increase and does not return to a baseline level, or grows significantly beyond expectations, a memory leak is probable.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/FwTL4hYTRBm0t-FXxVhWXA/en-us_image_0000002532670231.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0808B0773201468CF8A66E45B984B28F0EA6EDEAE5947DE53A99B5DB850A220 "Click to enlarge")
    
2.  Once a memory anomaly is suspected, use the Memory lane in either the Allocation or Snapshot template to capture detailed data and analyze memory trends in the affected scenario.
3.  Create an analysis task, and then deselect all lanes except the Memory lane to reduce overhead.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/TGZ_wbOyTdevmB7ogeES9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA40D4BAAD545D2517A3F82FD1B461D327FB76298102C230CFEBA5E1052039AE)
    
    Additional lanes (for example, memory allocation or object tracking) can introduce noise that interferes with accurate preliminary diagnosis.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/RBI_QLK7QaCD1X52Y9ntCw/en-us_image_0000002500910326.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=112EA44B43D0A1D2E8B487B171358283B4B5C3A3D6B06E23AF2FF7282647B045)
    
4.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/FS-BKod1T5aAGGnWF5_QdA/en-us_image_0000002501070168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A233A8A63AB1596AF2BBE3DF813D697A332991D8A1825D31096395EF1234795 "Click to enlarge") to start recording.
5.  During recording, continuously perform operations in the suspected scenario to help reproduce the issue.
6.  To stop recording, click the stop or pause button, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/J9N1CQzOR6CmKSLwyBy5AQ/en-us_image_0000002532750199.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E176AAEADC120F9452F5E2C31304DE9C5C5E9D2D2C8EFEC6C133296C1F98F436 "Click to enlarge")
    
7.  After the recording is complete, expand the Memory lane. **ArkTS Heap** indicates the memory managed by the ARK VM. A significant increase here may indicate a leak in ARK VM heap memory. **Native Heap** indicates the memory allocated through native APIs or C/C++ code. This memory must be manually managed by developers. A significant increase suggests a native memory leak.
    
    Use the Snapshot template for deeper analysis of ArkTS heap issues, and the Allocation template for native heap issues.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/0vTzRpN1TfeOIYAqxyR4Sg/en-us_image_0000002532750187.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA93FD7445977D21B86DDFA13FDC61C13C0BA85A6500D457831DD2C269570CC2 "Click to enlarge")
    

#### Using the Snapshot Template to Analyze ArkTS Memory Issues

## Analysis Steps

To analyze memory leak issues:

1.  Use the Snapshot template to record data.
2.  Take a snapshot before the issue occurs.
3.  Reproduce the suspected issue, and take a second snapshot after the issue occurs.
4.  Compare the two snapshots to identify the objects that may be causing the leak.
5.  If multiple objects appear suspicious, repeat steps 2–5 with additional snapshots to detect trends and narrow down the root cause.

## Recording Snapshot Data

1.  Connect the device and launch the app. Click the app selection box to select the target app. Select the **Snapshot** template, and click **Create Session** or double-click the **Snapshot** icon to create a snapshot session.
    
2.  Click the triangle button to start recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/LdStAjjiQ0itCiVS2iX8BA/en-us_image_0000002501070166.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21991F0BF7779AB9567860041067E0AA504599F7FA6EC9BDD2601C1A965F25EB "Click to enlarge")
    
3.  When recording is in progress, all lanes on the right display "recording."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/w6J4aITATNyHl9_QYD849A/en-us_image_0000002532670235.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=104A6D1108803608739A49992AEF4F8B6DE9A9F0E1E937584B0D2A8862BD82E0 "Click to enlarge")
    
4.  Click the snapshot button (marked as 1 in the figure below) to take the first heap snapshot as the baseline. When a purple bar appears (marked as 2), the snapshot has been successfully taken.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/PHOPshqBSR-gDlYMO4ckLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AE1BE70203DE86119AFBC257FC0BA8342769DE7BA87252909D47D0D439127A2)
    
    The ARK VM automatically performs garbage collection (GC) before the snapshot, so manual GC triggering is not necessary.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/_BuQhHP4S_me9iv2XehpAw/en-us_image_0000002532750191.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770D92530DC18CF6922AD261B639871041199F5291257BD9E369B467438B168B "Click to enlarge")
    
5.  Reproduce the suspected memory leak by performing the target operation repeatedly. To confirm whether a memory leak exists, perform the operation multiple times (for example, 5, 7, or 11 times). If each repetition leads to the creation of new instances that are not released (for example, five repetitions result in five retained instances), this suggests a potential memory leak. Repeating the operation more times, such as seven, can make the leak pattern more apparent and easier to analyze.
6.  Take the second snapshot after the suspected leak occurs.
7.  To stop recording, click the stop or pause button, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/x8gxJnOtTQ--ik3M3_TTjQ/en-us_image_0000002532670237.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73B4DD1A3F8A0B294C8C7B22B06611324120DAAA9576FD3C32AEEC85529083E5 "Click to enlarge")
    

## Analyzing ArkTS Heap

1.  Before each heap snapshot is taken, the ARK VM automatically triggers GC. As a result, the objects that remain in the snapshot are those that could not be reclaimed by the GC. By comparing two snapshots, you can identify which objects were added and retained after reproducing the suspected memory leak scenario. To begin the comparison, switch to the **Comparison** tab in the details area at the bottom of the window. The comparison shows the differences between snapshots (for example, Snapshot2 vs. Snapshot1, as shown below).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/hCVFDnNVTMmrXiS2bBJkBg/en-us_image_0000002501070162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=641D4A977D1CD585A5B495FF67C8277789FD8C98F66EBCF5D07D246389E0392B "Click to enlarge")
    
2.  Focus on constructors that correlate strongly with the number of memory-leak-inducing operations and the service code. Assess whether these objects should logically remain in memory. Next, explore the reference chains by sorting them in descending order of **Distance**. This helps locate how and why the certain objects (typically those associated with the service logic) remain referenced.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/O59KTC7vRZGxCLT4_AFybA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4445649DBD37925C965BCFB6AAEB033358A64E1132D4C1A9230A66B16BCF6F7)
    
    For further analysis, select an instance node. When the **Path to GC Root** button in the bottom search bar becomes clickable, click it to enable the system to calculate the shortest reference path from the GC Roots to the selected instance and display it in the right pane. This path traces references backward from the selected instance to the GC Roots, with the **Distance** value decreasing by 1 at each step until reaching the node with **Distance = 1**.
    

#### Analyzing Snapshot Data

## Introduction to Common Objects

**JSArray**

Currently, all JSArray objects, when expanded, show the individual elements within the array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/F9EPDTJBTweoajHxoY5QzA/en-us_image_0000002532750177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=810A9B49ACD8BE80AED98F481E37383FC238ABEEE2AD63BE5376C55A134F8F57)

**\_\_proto\_\_** represents a prototype object; the **\_\_proto\_\_** objects of all arrays should be consistent. **length** represents a built-in property accessor that allows access to the length of the array.

**TaggedDict**

Located within the (array) tag, **TaggedDict** is generally a dictionary created internally by the virtual machine and is not visible at the ArkTS code level.

**TaggedArray**

Located within the (array) tag, **TaggedArray** is generally an array created internally by the virtual machine and is not visible at the ArkTS code level.

**COWArray**

Located within the (array) tag, **COWArray** is generally an array created internally by the virtual machine and is not visible at the ArkTS code level.

**JSObject**

When a JSObject is expanded, it shows the following internal properties:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/_1DCGW9dT3Cn2H9naIKkuA/en-us_image_0000002500910310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=377209FF59D09C11092D2EEDEFCC0C929710BA01ABB5A5CD49D8D27030F664C0)

The following introduces the relationships between instantiated objects, declared objects, and constructors with a specific code example:

// HelloWorldPage.ets
class People {
  old: number
  name: string
  constructor(old: number, name: string) {
    this.old = old;
    this.name = name;
  }
  printOld() {
    console.log("old = ", this.old);
  }
  printName() {
    console.log("name = ", this.name);
  }
}

@Entry
@Component
struct HelloWorldPage {
  @State message: string = 'Hello World';
  private people: People = new People(20, "Tom");

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

The collected snapshot data is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/oxH-KjEWR6aNQa5_M98SOw/en-us_image_0000002532670233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89BBD28C054E5570A74504FF5C203C4A1BAF67B2A1C509DF9EAB9A368B52171A)

The object with ID 202169 corresponds to **People**, which mainly declares the object's properties and methods.

The **\_\_proto\_\_** property of the instance points to the object declared at the time of definition. The declared object has the constructor function. When multiple objects are instantiated, there will be multiple instantiated objects, but there will be only one declared object and one constructor function.

**JSFunction**

Currently, all JSFunction objects are located within the (closure) tag. Expanding this tag will reveal all the JSFunction objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ONZkWRrgQYuswUeVUCzcWA/en-us_image_0000002532670241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DF5FAA31D3E82AD06BDD50564BB0AB1B63FA9155AF39C3F44CE83560A418DF6 "Click to enlarge")

Upon expanding a function, you can see various properties within the function.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/850njs9EShG54e9M8QG8Dw/en-us_image_0000002532670249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E24F8C255C024FABD100F9A3ED98A333583FC4A10290049E9A46A27C9E1CA63)

**HomeObject** represents the parent object, indicating to which object the method belongs. **\_proto\_** indicates the prototype object. **LexicalEnv** represents the closure context of the function. **name** represents a built-in property accessor that allows retrieval of the function name. **FunctionExtraInfo** provides additional information, such as function addresses recorded by some Node-APIs. **ProtoOrHClass** represents the prototype or hidden class.

If a function appears as **anonymous()**, it signifies an anonymous function. If it appears as **JSFunction()**, it suggests that the function may be a framework-level function without a set name upon creation. For these functions whose name is not directly visible, you can confirm their name by examining their references.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/uxAb7AjCT3OCeduCwu_qRQ/en-us_image_0000002501070156.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=723434EE3FAB5AEF50DC2312E9C51F3B0BDD2505B4E00FBDD4AB5E81A6B719FF)

**ArkInternalConstantPool**

Virtual machine's created constant pool, which is not visible at the ArkTS code level. String constants involved are displayed within the (array) tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/6r_1vStKSAiupK6ZpORzrw/en-us_image_0000002501070158.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=869F7AC991E131DF9073D6C3B7EF57C70E71D1206C77D5FB993F4CD653648F75 "Click to enlarge")

**LexicalEnv**

Closure variable context; a closure is structured as a chain, as shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/QzTir4HhROWbz-MupenYjA/en-us_image_0000002532670229.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE2398720EDDEE0DE9DDC16B5003363813C7AC14D899C7B58CF9F8B81A99D214)

Node 733 is a closure array, where the element at index 0 is the closure of the caller (or further up the chain of callers), the element at index 1 stores debug information, and elements from index 2 onwards store the variables passed by the closure, with one variable passed in the example provided.

**InternalAccessor**

Built-in property accessor that includes getter and setter methods. Through the getter and setter, you can obtain and set the property value.

## Analysis Methods

**Viewing Object Names**

For declared objects, you can determine the object name through the **constructor** property.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/knPOSbWATDSPCfWJk7bgJg/en-us_image_0000002500910332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78A406AC377D96174EADA0054DC58A36C97D028B6A7E89677C9E5C70A2CA0651)

For instantiated objects, which generally do not have a constructor, you need to expand the **\_\_proto\_\_** property and then look for **constructor**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/HDOAd8TkS0GRIxgdIdnBTQ/en-us_image_0000002532750205.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=071C93AB677F3A5AD3116583D9E0CAF9CAF08768B44F9A238A460C5613F993FF)

If an object has some characteristic properties, you can search for the property names in the code to identify which specific object it is.

If there is an inheritance relationship between objects, you can continue expanding **\_\_proto\_\_** to trace the inheritance chain.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Ac9omaS3Qsiqs47kumM0ZQ/en-us_image_0000002501070176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062158Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=360F355DDFF316554E06F0EB68C733A1E4B8D3C99E02CACEA7ACEA6D976CA180)

In the preceding figure, the **Man** object inherits from the **People** object.
