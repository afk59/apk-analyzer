# FAQs About Imperative Nodes

This topic addresses common issues related to imperative nodes.

#### JS Crash Occurs When FrameNode Is Running

**Symptom**

A [JS crash](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/js-crash-process-crash-detection/document.md) occurs after [FrameNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-framenode) is used in an improper way.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/wgM32DlFTvmxEg-QEcfU1g/en-us_image_0000002568684703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17D9F8CD3108162618C0C228C0ED674BD1FD7CF4930C73A4505C7BD00CF30EBB)

**Solution**

Go to the error log as prompted, view the error cause, and rectify the fault. For details, see the code example below.

**Code Example**

This example shows how to throw a [dispose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-framenode#dispose12) exception in FrameNode. After the sample code is executed, a JS crash error is reported. Go to the error scenario as prompted. The error cause is that [getMeasuredSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-framenode#getmeasuredsize12) cannot be called after **dispose** is called. In this example, deleting the code related to **dispose** will allow the application to run normally.

import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  makeNode(uiContext: UIContext): FrameNode | null {
    let node = new FrameNode(uiContext);
    node.dispose(); // Deleting this line will allow the application to run normally.
    node.getMeasuredSize();
    return node;
  }
}

@Entry
@Component
struct FrameNodeTypeTest {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      Text('Hello')
      NodeContainer(this.myNodeController);
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/M4xucnbhTzOIywxKnwkAOw/en-us_image_0000002537764988.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD46D947DDCE3F298D1479BB25310BB38EFEF08D2073004FB9C905CE74C836C8)
