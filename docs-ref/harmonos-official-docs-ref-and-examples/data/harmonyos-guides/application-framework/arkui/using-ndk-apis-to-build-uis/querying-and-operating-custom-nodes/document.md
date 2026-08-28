# Querying and Operating Custom Nodes

The NDK provides comprehensive capabilities for node query, traversal, and operations. You can use the following APIs to efficiently access and manipulate nodes.

The following scenarios are based on the project configuration described in [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).

#### Querying Node uniqueId and Obtaining Node Information by uniqueId

**uniqueId** is a system-allocated unique identifier for each node.

Since API version 20, you can use the [OH\_ArkUI\_NodeUtils\_GetNodeUniqueId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getnodeuniqueid) API to obtain the **uniqueId** value of a target node, and the [OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getnodehandlebyuniqueid) API to obtain the node pointer using the obtained **uniqueId** value.

ArkUI\_NativeNodeAPI\_1\* nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
ArkUI\_NodeHandle testNode = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
ArkUI\_NumberValue value\[\] = {VALUE\_1};
ArkUI\_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
value\[0\].f32 = VALUE\_2;
nodeAPI->setAttribute(testNode, NODE\_WIDTH, &item);
nodeAPI->setAttribute(testNode, NODE\_HEIGHT, &item);
struct IdList {
    int32\_t id = -1;
};
IdList \*idl = new IdList;
int32\_t uid = -1;
OH\_ArkUI\_NodeUtils\_GetNodeUniqueId(testNode, &uid);
idl->id = uid;
auto button = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
value\[0\].f32 = VALUE\_3;
nodeAPI->setAttribute(button, NODE\_WIDTH, &item);
nodeAPI->setAttribute(button, NODE\_HEIGHT, &item);
nodeAPI->addChild(testNode, button);
nodeAPI->registerNodeEvent(button, NODE\_ON\_CLICK, 1, idl);
OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_PRINT, "GetNodeUniqueId", "GetNodeHandleByUniqueId success1");
nodeAPI->registerNodeEventReceiver(\[\](ArkUI\_NodeEvent \*event) {
    auto targetId = OH\_ArkUI\_NodeEvent\_GetTargetId(event);
    if (targetId == 1) {
        auto idl = (IdList \*)OH\_ArkUI\_NodeEvent\_GetUserData(event);
        ArkUI\_NodeHandle Test\_Column;
        auto ec = OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId(idl->id, &Test\_Column);
        if (ec == 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_PRINT, "GetNodeUniqueId", "GetNodeHandleByUniqueId success");
        }
    }
});

#### Obtaining Node Information Using Custom IDs

Use the [OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid) API to obtain the target node pointer based on a custom ID.

1.  Access native components in ArkTS:
    
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct GetNodeById {
      private rootSlot = new NodeContent();
    
      aboutToAppear(): void {
        nativeNode.createUserIdNode(this.rootSlot);
      }
    
      build() {
        Scroll() {
          Column({ space: 15 }) {
            Column() {
              ContentSlot(this.rootSlot)
            }
          }
          .width('100%')
        }.scrollBarColor(Color.Transparent)
      }
    }
    
2.  Create **GetNodeByIdExample.h** to create a **Text** node with an **id** attribute and obtain it using **OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById**:
    
    // GetNodeByIdExample.h
    #ifndef MYAPPLICATION\_GETNODEBYID\_H
    #define MYAPPLICATION\_GETNODEBYID\_H
    
    #include "ArkUINode.h"
    #include <hilog/log.h>
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateGetNodeByIdExample()
    {
        auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
        
        // Create a structure for passing event nodes.
        struct A {
            ArkUI\_NodeHandle node;
        };
        A\* a = new A;
        
        // Create the root Scroll node.
        ArkUI\_NodeHandle scroll = nodeAPI->createNode(ARKUI\_NODE\_SCROLL);
        ArkUI\_NumberValue length\_value\[\] = {{.f32 = 480}};
        ArkUI\_AttributeItem length\_item = {length\_value, sizeof(length\_value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_WIDTH, &length\_item);
        ArkUI\_NumberValue length\_value1\[\] = {{.f32 = 650}};
        ArkUI\_AttributeItem length\_item1 = {length\_value1, sizeof(length\_value1) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_HEIGHT, &length\_item1);
        ArkUI\_AttributeItem scroll\_id = {.string = "Scroll\_CAPI"};
        nodeAPI->setAttribute(scroll, NODE\_ID, &scroll\_id);
        
        // Create a Column node.
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue value\[\] = {480};
        ArkUI\_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_WIDTH, &item);
        ArkUI\_NumberValue column\_bc\[\] = {{.u32 = 0xFFF00BB}};
        ArkUI\_AttributeItem column\_item = {column\_bc, 1};
        nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &column\_item);
        ArkUI\_AttributeItem column\_id = {.string = "Column\_CAPI"};
        nodeAPI->setAttribute(column, NODE\_ID, &column\_id);
        
        // Create a Text node.
        ArkUI\_NodeHandle text0 = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_NumberValue text\_width\[\] = {300};
        ArkUI\_AttributeItem text\_item0 = {text\_width, sizeof(text\_width) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(text0, NODE\_WIDTH, &text\_item0);
        ArkUI\_NumberValue text\_height\[\] = {50};
        ArkUI\_AttributeItem text\_item1 = {text\_height, sizeof(text\_height) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(text0, NODE\_HEIGHT, &text\_item1);
        ArkUI\_AttributeItem text\_item = {.string = "Example Text node"};
        nodeAPI->setAttribute(text0, NODE\_TEXT\_CONTENT, &text\_item);
        ArkUI\_NumberValue margin\[\] = {10};
        ArkUI\_AttributeItem item\_margin = {margin, sizeof(margin) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(text0, NODE\_MARGIN, &item\_margin);
        ArkUI\_AttributeItem text0\_id = {.string = "Text0\_CAPI"};
        nodeAPI->setAttribute(text0, NODE\_ID, &text0\_id);
        a->node = text0;
        
        // Create a Row node.
        ArkUI\_NodeHandle row0 = nodeAPI->createNode(ARKUI\_NODE\_ROW);
        ArkUI\_NumberValue width\_value\[\] = {{.f32=330}};
        ArkUI\_AttributeItem width\_item = {width\_value, sizeof(width\_value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(row0, NODE\_WIDTH, &width\_item);
        nodeAPI->setAttribute(row0, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(row0, NODE\_MARGIN, &item\_margin);
        
        // Create a Button node.
        ArkUI\_NodeHandle bt0 = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
        ArkUI\_NumberValue btn\_width\[\] = {150};
        ArkUI\_AttributeItem btn\_item0 = {btn\_width, sizeof(btn\_width) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(bt0, NODE\_WIDTH, &btn\_item0);
        nodeAPI->setAttribute(bt0, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(bt0, NODE\_MARGIN, &item\_margin);
        ArkUI\_AttributeItem bt0\_item = {.string = "GetAttachedNodeHandleById"};
        nodeAPI->setAttribute(bt0, NODE\_BUTTON\_LABEL, &bt0\_item);
        nodeAPI->registerNodeEvent(bt0, NODE\_ON\_CLICK, 0, a);
        
        // Register events.
        auto onClick = \[\](ArkUI\_NodeEvent \*event) {
            ArkUI\_NodeHandle node = OH\_ArkUI\_NodeEvent\_GetNodeHandle(event);
            auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
            
            if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == 0) {  // GetAttachedNodeHandleById
                A\* a = (A\*)OH\_ArkUI\_NodeEvent\_GetUserData(event);
                ArkUI\_NodeHandle node = nullptr;
                auto res = OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById("Text0\_CAPI", &node);
                if (node == a->node) {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "GetNodeByIdExample", "get Text0\_CAPI success");
                } else {
                    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "GetNodeByIdExample", "get Text0\_CAPI failed");
                }
            }
        };
        nodeAPI->registerNodeEventReceiver(onClick);
        
        // Add nodes.
        nodeAPI->addChild(scroll, column);
        nodeAPI->addChild(column, text0);
        nodeAPI->addChild(column, row0);
        nodeAPI->addChild(row0, bt0);
        
        return std::make\_shared<ArkUINode>(scroll);
    }
    } // namespace NativeModule
    
    #endif //MYAPPLICATION\_GETNODEBYID\_H
    
3.  Mount the native node in **NativeEntry.cpp**.
    
    // NativeEntry.cpp
    #include <arkui/native\_node\_napi.h>
    #include <hilog/log.h>
    #include <js\_native\_api.h>
    #include "NativeEntry.h"
    #include "MoveToExample.h"
    #include "GetNodeByIdExample.h"
    
    
    namespace NativeModule {
    // ...
    static napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info, const char \*who, MakeNodeFn makeNodeFn)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain NodeContent.
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        if (contentHandle == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, K\_LOG\_DOMAIN,
                         "%{public}s nodeContentHandle is null", who);
            return nullptr;
        }
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // Create a node.
        auto node = makeNodeFn();
    
        // Keep the native-side object in the management class to maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(node);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native-side object from the management class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    // ...
    } // namespace NativeModule
    
4.  Run the program and click the button to verify successful node retrieval.
    

#### Moving a Node

Use the [OH\_ArkUI\_NodeUtils\_MoveTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_moveto) API to move a native node to a new parent node, modifying the node tree structure as needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/-u6cILP8REaVqpngpf4N3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B395C47EBF4F878781C4C4F9A312AF6EEDA1512A521C87E4C1730FA4B5E55D5)

Currently, only the following [ArkUI\_NodeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodetype) nodes can be moved: ARKUI\_NODE\_STACK, ARKUI\_NODE\_XCOMPONENT, and ARKUI\_NODE\_EMBEDDED\_COMPONENT. This API does not work for other node types.

1.  Access native components in ArkTS:
    
    // MoveTo.ets
    import nativeNode from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct MoveTo {
      private rootSlot = new NodeContent();
    
      aboutToAppear(): void {
        nativeNode.createMoveToNode(this.rootSlot);
      }
    
      build() {
        Scroll() {
          Column({ space: 15 }) {
            Column() {
              ContentSlot(this.rootSlot)
            }
          }
          .width('100%')
        }.scrollBarColor(Color.Transparent)
      }
    }
    
2.  Create **MoveTo.h** to create **Stack** nodes and move them using **OH\_ArkUI\_NodeUtils\_MoveTo**:
    
    // MoveToExample.h
    #ifndef MYAPPLICATION\_MOVETO\_H
    #define MYAPPLICATION\_MOVETO\_H
    
    #include "ArkUINode.h"
    #include <hilog/log.h>
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateMoveToExample()
    {
        auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
    
        // Create a structure for passing event nodes.
        struct A {
            ArkUI\_NodeHandle node;
            ArkUI\_NodeHandle targetParent;
        };
        A\* a = new A;
    
        // Create the root Scroll node.
        ArkUI\_NodeHandle scroll = nodeAPI->createNode(ARKUI\_NODE\_SCROLL);
        ArkUI\_NumberValue length\_value\[\] = {{.f32 = 480}};
        ArkUI\_AttributeItem length\_item = {length\_value, sizeof(length\_value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_WIDTH, &length\_item);
        ArkUI\_NumberValue length\_value1\[\] = {{.f32 = 650}};
        ArkUI\_AttributeItem length\_item1 = {length\_value1, sizeof(length\_value1) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(scroll, NODE\_HEIGHT, &length\_item1);
        ArkUI\_AttributeItem scroll\_id = {.string = "Scroll\_CAPI"};
        nodeAPI->setAttribute(scroll, NODE\_ID, &scroll\_id);
    
        // Create a Column node.
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue value\[\] = {480};
        ArkUI\_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_WIDTH, &item);
        ArkUI\_AttributeItem column\_id = {.string = "Column\_CAPI"};
        nodeAPI->setAttribute(column, NODE\_ID, &column\_id);
    
        // Create a Row node.
        ArkUI\_NumberValue text\_height\[\] = {50};
        ArkUI\_AttributeItem text\_item1 = {text\_height, sizeof(text\_height) / sizeof(ArkUI\_NumberValue)};
        ArkUI\_NumberValue margin\[\] = {10};
        ArkUI\_AttributeItem item\_margin = {margin, sizeof(margin) / sizeof(ArkUI\_NumberValue)};
        ArkUI\_NodeHandle row0 = nodeAPI->createNode(ARKUI\_NODE\_ROW);
        ArkUI\_NumberValue width\_value\[\] = {{.f32=330}};
        ArkUI\_AttributeItem width\_item = {width\_value, sizeof(width\_value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(row0, NODE\_WIDTH, &width\_item);
        nodeAPI->setAttribute(row0, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(row0, NODE\_MARGIN, &item\_margin);
    
        ArkUI\_NodeHandle row1 = nodeAPI->createNode(ARKUI\_NODE\_ROW);
        nodeAPI->setAttribute(row1, NODE\_WIDTH, &width\_item);
        nodeAPI->setAttribute(row1, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(row1, NODE\_MARGIN, &item\_margin);
        a->targetParent = row1;
    
        ArkUI\_NodeHandle row2 = nodeAPI->createNode(ARKUI\_NODE\_ROW);
        nodeAPI->setAttribute(row2, NODE\_WIDTH, &width\_item);
        nodeAPI->setAttribute(row2, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(row2, NODE\_MARGIN, &item\_margin);
    
        //Create a Stack node.
        ArkUI\_NodeHandle stack0 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        ArkUI\_NumberValue stack\_value\[\] = {{.f32=50}};
        ArkUI\_AttributeItem stack\_item1 = {stack\_value, sizeof(width\_value) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(stack0, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack0, NODE\_HEIGHT, &stack\_item1);
        ArkUI\_NumberValue stack\_bc\[\] = {{.u32 = 0xFFFFB6C1}};
        ArkUI\_AttributeItem stack\_item2 = {stack\_bc, 1};
        nodeAPI->setAttribute(stack0, NODE\_BACKGROUND\_COLOR, &stack\_item2);
        a->node = stack0;
    
        ArkUI\_NodeHandle stack1 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        nodeAPI->setAttribute(stack1, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack1, NODE\_HEIGHT, &stack\_item1);
        ArkUI\_NumberValue stack\_bc1\[\] = {{.u32 = 0xFF6495ED}};
        ArkUI\_AttributeItem stack\_item3 = {stack\_bc1, 1};
        nodeAPI->setAttribute(stack1, NODE\_BACKGROUND\_COLOR, &stack\_item3);
    
        ArkUI\_NodeHandle stack2 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        nodeAPI->setAttribute(stack2, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack2, NODE\_HEIGHT, &stack\_item1);
        ArkUI\_NumberValue stack\_bc2\[\] = {{.u32 = 0xFF90EE90}};
        ArkUI\_AttributeItem stack\_item4 = {stack\_bc2, 1};
        nodeAPI->setAttribute(stack2, NODE\_BACKGROUND\_COLOR, &stack\_item4);
    
        ArkUI\_NodeHandle stack3 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        nodeAPI->setAttribute(stack3, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack3, NODE\_HEIGHT, &stack\_item1);
        nodeAPI->setAttribute(stack3, NODE\_BACKGROUND\_COLOR, &stack\_item2);
    
        ArkUI\_NodeHandle stack4 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        nodeAPI->setAttribute(stack4, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack4, NODE\_HEIGHT, &stack\_item1);
        nodeAPI->setAttribute(stack4, NODE\_BACKGROUND\_COLOR, &stack\_item3);
        
        ArkUI\_NodeHandle stack5 = nodeAPI->createNode(ARKUI\_NODE\_STACK);
        nodeAPI->setAttribute(stack5, NODE\_WIDTH, &stack\_item1);
        nodeAPI->setAttribute(stack5, NODE\_HEIGHT, &stack\_item1);
        nodeAPI->setAttribute(stack5, NODE\_BACKGROUND\_COLOR, &stack\_item4);
    
        // Create a Button node.
        ArkUI\_NodeHandle bt0 = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
        ArkUI\_NumberValue btn\_width\[\] = {150};
        ArkUI\_AttributeItem btn\_item0 = {btn\_width, sizeof(btn\_width) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(bt0, NODE\_WIDTH, &btn\_item0);
        nodeAPI->setAttribute(bt0, NODE\_HEIGHT, &text\_item1);
        nodeAPI->setAttribute(bt0, NODE\_MARGIN, &item\_margin);
        ArkUI\_AttributeItem bt0\_item = {.string = "MoveTo"};
        nodeAPI->setAttribute(bt0, NODE\_BUTTON\_LABEL, &bt0\_item);
        nodeAPI->registerNodeEvent(bt0, NODE\_ON\_CLICK, 0, a);
    
        // Register events.
        auto onClick = \[\](ArkUI\_NodeEvent \*event) {
            ArkUI\_NodeHandle node = OH\_ArkUI\_NodeEvent\_GetNodeHandle(event);
            auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
            
            if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == 0) {  // MoveTo
                A\* a = (A\*)OH\_ArkUI\_NodeEvent\_GetUserData(event);
                auto res = OH\_ArkUI\_NodeUtils\_MoveTo(a->node, a->targetParent, 2);
            }
        };
        nodeAPI->registerNodeEventReceiver(onClick);
    
        // Add nodes.
        nodeAPI->addChild(scroll, column);
        nodeAPI->addChild(column, row0);
        nodeAPI->addChild(column, row1);
        nodeAPI->addChild(column, row2);
        nodeAPI->addChild(row0, stack0);
        nodeAPI->addChild(row0, stack1);
        nodeAPI->addChild(row0, stack2);
        nodeAPI->addChild(row1, stack3);
        nodeAPI->addChild(row1, stack4);
        nodeAPI->addChild(row1, stack5);
        nodeAPI->addChild(row2, bt0);
    
        return std::make\_shared<ArkUINode>(scroll);
    }
    } // namespace NativeModule
    
    #endif //MYAPPLICATION\_MOVETO\_H
    
3.  Mount the native node in **NativeEntry.cpp**.
    
    // NativeEntry.cpp
    #include <arkui/native\_node\_napi.h>
    #include <hilog/log.h>
    #include <js\_native\_api.h>
    #include "NativeEntry.h"
    #include "MoveToExample.h"
    #include "GetNodeByIdExample.h"
    
    
    namespace NativeModule {
    // ...
    static napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info, const char \*who, MakeNodeFn makeNodeFn)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain NodeContent.
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        if (contentHandle == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, K\_LOG\_DOMAIN,
                         "%{public}s nodeContentHandle is null", who);
            return nullptr;
        }
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // Create a node.
        auto node = makeNodeFn();
    
        // Keep the native-side object in the management class to maintain its lifecycle.
        NativeEntry::GetInstance()->SetRootNode(node);
        return nullptr;
    }
    
    napi\_value DestroyNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        // Release the native-side object from the management class.
        NativeEntry::GetInstance()->DisposeRootNode();
        return nullptr;
    }
    // ...
    } // namespace NativeModule
    
4.  Run the program and click the button to observe the **Stack** node moving to the target position.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/40ZNfe-sS3anladffZ4TuQ/en-us_image_0000002568684609.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9DDA2E61195C482D68F9AB1F30A939188ED71EC15F61BA91E2831685542DFB0)
    

#### Updating Node Attributes in the Current Frame

Since API version 21, use the [OH\_ArkUI\_NativeModule\_InvalidateAttributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nativemodule_invalidateattributes) API to update node attributes within the current frame, preventing flickering during component switching.

1.  Access native components in ArkTS:
    
    import testNapi from 'libentry.so';
    import { NodeContent } from '@kit.ArkUI';
    
    @Component
    struct ImageContent {
      private nodeContent: NodeContent = new NodeContent();
    
      aboutToAppear() {
        // Create a node through the C API and add it to the nodeContent manager.
        testNapi.createNativeNode(this.nodeContent);
      }
      build() {
        Column() {
          // Display the native components stored in the nodeContent manager.
          ContentSlot(this.nodeContent)
        }
      }
    }
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
      @State showParent: boolean = true;
      build() {
        Row() {
          Column() {
            // Replace $r('app.string.Switch') with the resource file you use.
            Button($r('app.string.Switch')).onClick(()=>{
              this.showParent = !this.showParent;
            }).margin(20)
            if(this.showParent) {
              ImageContent()
            } else {
              ImageContent()
            }
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
2.  Create **Attribute\_util.h** for setting component attributes:
    
    #ifndef MYAPPLICATION\_ATTRIBUTE\_UTIL\_H
    #define MYAPPLICATION\_ATTRIBUTE\_UTIL\_H
    
    #include <arkui/native\_node.h>
    #include <cstdint>
    #include <string>
    class AttributeUtil {
    public:
        ArkUI\_NativeNodeAPI\_1 \*api\_;
        ArkUI\_NodeHandle node\_;
        AttributeUtil(ArkUI\_NodeHandle node, ArkUI\_NativeNodeAPI\_1 \*api)
        {
            this->node\_ = node;
            api\_ = api;
        }
        int32\_t Width(float width)
        {
            ArkUI\_NumberValue NODE\_WIDTH\_value\[\] = {width};
            ArkUI\_AttributeItem NODE\_WIDTH\_Item = {NODE\_WIDTH\_value, 1};
            return api\_->setAttribute(node\_, NODE\_WIDTH, &NODE\_WIDTH\_Item);
        }
        int32\_t Height(float height)
        {
            ArkUI\_NumberValue NODE\_HEIGHT\_value\[\] = {height};
            ArkUI\_AttributeItem NODE\_HEIGHT\_Item = {NODE\_HEIGHT\_value, 1};
            return api\_->setAttribute(node\_, NODE\_HEIGHT, &NODE\_HEIGHT\_Item);
        }
        int32\_t ImageSrc(std::string src)
        {
            ArkUI\_AttributeItem NODE\_IMAGE\_SRC\_VALUE = {.string = src.c\_str()};
            return api\_->setAttribute(node\_, NODE\_IMAGE\_SRC, &NODE\_IMAGE\_SRC\_VALUE);
        }
        int32\_t ImageSyncLoad()
        {
            ArkUI\_NumberValue NODE\_TRANSLATE\_ITEM\_VALUE\[\] = {{.i32 = 1}};
            ArkUI\_AttributeItem NODE\_BORDER\_WIDTH\_ITEM = {NODE\_TRANSLATE\_ITEM\_VALUE, 1};
            return api\_->setAttribute(node\_, NODE\_IMAGE\_SYNC\_LOAD, &NODE\_BORDER\_WIDTH\_ITEM);
        }
    };
    #endif // MYAPPLICATION\_ATTRIBUTE\_UTIL\_H
    
3.  Mount the native node in **nai\_init.cpp**.
    
    #include "Attribute\_util.h"
    #include "napi/native\_api.h"
    #include <arkui/native\_interface.h>
    #include <arkui/native\_node.h>
    #include <arkui/native\_node\_napi.h>
    #include <hilog/log.h>
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    // ...
    const unsigned int NUMBER\_2 = 2;
    const unsigned int NUMBER\_WIDTH = 100;
    const unsigned int NUMBER\_HEIGHT = 100;
    
    static napi\_value Add(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = NUMBER\_2;
        napi\_value args\[NUMBER\_2\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        napi\_valuetype valuetype0;
        napi\_typeof(env, args\[0\], &valuetype0);
    
        napi\_valuetype valuetype1;
        napi\_typeof(env, args\[1\], &valuetype1);
    
        double value0;
        napi\_get\_value\_double(env, args\[0\], &value0);
    
        double value1;
        napi\_get\_value\_double(env, args\[1\], &value1);
    
        napi\_value sum;
        napi\_create\_double(env, value0 + value1, &sum);
    
        return sum;
    }
    
    static ArkUI\_NativeNodeAPI\_1 \*nodeAPI = nullptr;
    
    static napi\_value NAPI\_Global\_createNativeNode(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, nodeAPI);
        // Create an Image component.
        auto imageNode = nodeAPI->createNode(ARKUI\_NODE\_IMAGE);
        AttributeUtil imageNodeAttr(imageNode, nodeAPI);
        // Set the attributes of the Image component.
        imageNodeAttr.ImageSrc("resources/base/media/startIcon.png");
        imageNodeAttr.ImageSyncLoad();
        imageNodeAttr.Width(NUMBER\_WIDTH);
        imageNodeAttr.Height(NUMBER\_HEIGHT);
        // Update the  attributes in the current frame.
        OH\_ArkUI\_NativeModule\_InvalidateAttributes(imageNode);
        // Mount the Image component to the component tree.
        OH\_ArkUI\_NodeContent\_AddNode(contentHandle, imageNode);
        return nullptr;
    }
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"createNativeNode", nullptr, NAPI\_Global\_createNativeNode, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // ...
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void\*)0),
        .reserved = { 0 },
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
    {
        napi\_module\_register(&demoModule);
    }
    
4.  Run the program and click the button to verify proper image display.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/v1lJVy5tRcexF_ToFgj73A/en-us_image_0000002568764619.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08AC5EC01FCDF790A0F8738BADEB3D4566909100CC349F71B202C31F26A80457)
    

#### Obtaining Child Nodes with Different Expansion Modes

The NDK supports obtaining valid node information under target nodes using different expansion modes, such as in **LazyForEach** scenarios with multiple child nodes.

Since API version 20: Use [OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getfirstchildindexwithoutexpand) to obtain the first child node index. Use [OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getlastchildindexwithoutexpand) to obtain the last child node index. Use [OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getchildwithexpandmode) to obtain child nodes with specific indices in different expansion modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/MYPi0bR4R_2v16_t_lZtlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F050DEEAEABAE9802ED16CC5B35CB4F4EC7EFC3435708E95094C1E6BC272E4A)

For details about node expansion modes, see [ArkUI\_ExpandMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#arkui_expandmode). The **ARKUI\_LAZY\_EXPAND** mode is recommended for intelligent scenario detection.

1.  Create the **LazyForEach** scenario in ArkTS.
    
    import { NodeController, FrameNode, UIContext, BuilderNode, ExpandMode, LengthUnit } from '@kit.ArkUI';
    
    const TEST\_TAG: string = "FrameNode ";
    
    // BasicDataSource implements the IDataSource API to manage listeners and notify LazyForEach of data updates.
    class BasicDataSource implements IDataSource {
      private listeners: DataChangeListener\[\] = \[\];
      private originDataArray: string\[\] = \[\];
    
      public totalCount(): number {
        return 0;
      }
    
      public getData(index: number): string {
        return this.originDataArray\[index\];
      }
    
      // This method is called by the framework to register a listener to the LazyForEach data source.
      registerDataChangeListener(listener: DataChangeListener): void {
        if (this.listeners.indexOf(listener) < 0) {
          console.info('add listener');
          this.listeners.push(listener);
        }
      }
    
      // This method is called by the framework to unregister the listener from the LazyForEach data source.
      unregisterDataChangeListener(listener: DataChangeListener): void {
        const pos = this.listeners.indexOf(listener);
        if (pos >= 0) {
          console.info('remove listener');
          this.listeners.splice(pos, 1);
        }
      }
    
      // Notify LazyForEach that all child components need to be reloaded.
      notifyDataReload(): void {
        this.listeners.forEach(listener => {
          listener.onDataReloaded();
        })
      }
    
      // Notify LazyForEach that a child component needs to be added for the data item with the specified index.
      notifyDataAdd(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataAdd(index);
          // Method 2: listener.onDatasetChange(\[{type: DataOperationType.ADD, index: index}\]);
        })
      }
    
      // Notify LazyForEach that the data item with the specified index has changed and the child component needs to be rebuilt.
      notifyDataChange(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataChange(index);
          // Method 2: listener.onDatasetChange(\[{type: DataOperationType.CHANGE, index: index}\]);
        })
      }
    
      // Notify LazyForEach that the child component needs to be deleted from the data item with the specified index.
      notifyDataDelete(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataDelete(index);
          // Method 2: listener.onDatasetChange(\[{type: DataOperationType.DELETE, index: index}\]);
        })
      }
    
      // Notify LazyForEach that data needs to be swapped between the from and to positions.
      notifyDataMove(from: number, to: number): void {
        this.listeners.forEach(listener => {
          listener.onDataMove(from, to);
          // Method 2: listener.onDatasetChange ()
          //         \[{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}\]);
        })
      }
    
      notifyDatasetChange(operations: DataOperation\[\]): void {
        this.listeners.forEach(listener => {
          listener.onDatasetChange(operations);
        })
      }
    }
    
    class MyDataSource extends BasicDataSource {
      private dataArray: string\[\] = \[\]
    
      public totalCount(): number {
        return this.dataArray.length;
      }
    
      public getData(index: number): string {
        return this.dataArray\[index\];
      }
    
      public addData(index: number, data: string): void {
        this.dataArray.splice(index, 0, data);
        this.notifyDataAdd(index);
      }
    
      public pushData(data: string): void {
        this.dataArray.push(data);
        this.notifyDataAdd(this.dataArray.length - 1);
      }
    }
    
    class Params {
      data: MyDataSource | null = null;
      scroller: Scroller | null = null;
      constructor(data: MyDataSource, scroller: Scroller) {
        this.data = data;
        this.scroller = scroller;
      }
    }
    
    @Builder
    function buildData(params: Params) {
      List({ scroller: params.scroller }) {
        LazyForEach(params.data, (item: string) => {
          ListItem() {
            Column() {
              Text(item)
                .fontSize(20)
                .onAppear(() => {
                  console.info(TEST\_TAG + " node appear: " + item)
                })
                .backgroundColor(Color.Pink)
                .margin({
                  top: 30,
                  bottom: 30,
                  left: 10,
                  right: 10
                })
            }
          }
          .id(item)
        }, (item: string) => item)
      }
      .cachedCount(5)
      .listDirection(Axis.Horizontal)
    }
    
    class MyNodeController extends NodeController {
      private rootNode: FrameNode | null = null;
      private uiContext: UIContext | null = null;
      private data: MyDataSource = new MyDataSource();
      private scroller: Scroller = new Scroller();
    
      makeNode(uiContext: UIContext): FrameNode | null {
        this.uiContext = uiContext;
        for (let i = 0; i <= 20; i++) {
          this.data.pushData(\`N${i}\`);
        }
        const params: Params = new Params(this.data, this.scroller);
        const dataNode: BuilderNode<\[Params\]> = new BuilderNode(uiContext);
        dataNode.build(wrapBuilder<\[Params\]>(buildData), params);
        this.rootNode = dataNode.getFrameNode();
        const scrollToIndexOptions: ScrollToIndexOptions = {
          extraOffset: {
            value: 20, unit: LengthUnit.VP
          }
        };
        this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
        return this.rootNode;
      }
    
      //Obtain the index of the first active node in the non-expansion scenario.
      getFirstChildIndexWithoutExpand() {
        console.info(\`${TEST\_TAG} getFirstChildIndexWithoutExpand: ${this.rootNode!.getFirstChildIndexWithoutExpand()}\`);
      }
    
      //Obtain the index of the last active node in the non-expansion scenario.
      getLastChildIndexWithoutExpand() {
        console.info(\`${TEST\_TAG} getLastChildIndexWithoutExpand: ${this.rootNode!.getLastChildIndexWithoutExpand()}\`);
      }
    
      // Obtain the node in non-expansion mode.
      getChildWithNotExpand() {
        const childNode = this.rootNode!.getChild(3, ExpandMode.NOT\_EXPAND);
        console.info(TEST\_TAG + " getChild(3, ExpandMode.NOT\_EXPAND): " + childNode?.getId());
        if (childNode?.getId() === "N9") {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.NOT\_EXPAND)  result: success.");
        } else {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.NOT\_EXPAND)  result: fail.");
        }
      }
      
      // Obtain the node in expansion mode.
      getChildWithExpand() {
        const childNode = this.rootNode!.getChild(3, ExpandMode.EXPAND);
        console.info(TEST\_TAG + " getChild(3, ExpandMode.EXPAND): " + childNode?.getId());
        if (childNode?.getId() === "N3") {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.EXPAND)  result: success.");
        } else {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.EXPAND)  result: fail.");
        }
      }
      
      getChildWithLazyExpand() {
        const childNode = this.rootNode!.getChild(3, ExpandMode.LAZY\_EXPAND);
        console.info(TEST\_TAG + " getChild(3, ExpandMode.LAZY\_EXPAND): " + childNode?.getId());
        if (childNode?.getId() === "N3") {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.LAZY\_EXPAND)  result: success.");
        } else {
          console.info(TEST\_TAG + " getChild(3, ExpandMode.LAZY\_EXPAND)  result: fail.");
        }
      }
    }
    
    @Entry
    @Component
    struct Index {
      private myNodeController: MyNodeController = new MyNodeController();
      private scroller: Scroller = new Scroller();
    
      build() {
        Scroll(this.scroller) {
          Column({ space: 8 }) {
            Column() {
              Text("This is a NodeContainer.")
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
                .width('100%')
                .fontSize(16)
              NodeContainer(this.myNodeController)
                .borderWidth(1)
                .width(300)
                .height(100)
            }
    
            Button("getFirstChildIndexWithoutExpand")
                .width(300)
                .onClick(() => {
                  this.myNodeController.getFirstChildIndexWithoutExpand();
                })
              Button("getLastChildIndexWithoutExpand")
                .width(300)
                .onClick(() => {
                  this.myNodeController.getLastChildIndexWithoutExpand();
                })
              Button("getChildWithNotExpand")
                .width(300)
                .onClick(() => {
                  this.myNodeController.getChildWithNotExpand();
                })
              Button("getChildWithExpand")
                .width(300)
                .onClick(() => {
                  this.myNodeController.getChildWithExpand();
                })
              Button("getChildWithLazyExpand")
                .width(300)
                .onClick(() => {
                  this.myNodeController.getChildWithLazyExpand();
                })
            }
            .width("100%")
          }
          .scrollable(ScrollDirection.Vertical) // The scrollbar scrolls in the vertical direction.
        }
      }
    
2.  On the NDK side, obtain the ArkTS component through the [OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_getattachednodehandlebyid) API, and obtain the corresponding child component information in lazy expansion mode.
    
    ArkUI\_NodeHandle childNode = nullptr;
    OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById("N3", &childNode);
        
    uint32\_t index = 0;
    OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand(childNode, &index);
    uint32\_t index1 = 0;
    OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand(childNode, &index1);
    ArkUI\_NodeHandle child = nullptr;
    auto result = OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode(childNode, 3, &child, 0);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "Manager",
        "firstChildIndex - lastChildIndex == %{d -- %{public}d, -- getResult = %{public}d",
        index, index1, result);
    
3.  Check whether the result code returned in the log matches the expected value to determine whether the corresponding child node is obtained successfully.
