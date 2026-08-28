# Listening for Text Box Events

Text boxes support various interactive behaviors, allowing you to register event listeners and obtain status information.

Real-time search: Register the [NODE\_TEXT\_AREA\_ON\_CHANGE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) event to receive notifications and obtain the current text content when the text box input changes.

Text filtering: Register the [NODE\_TEXT\_AREA\_ON\_WILL\_INSERT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) event to receive notifications before text is inserted and control whether to insert text through the return value.

Layout changes during editing: Register the [NODE\_TEXT\_AREA\_ON\_EDIT\_CHANGE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) event to receive notifications when the text box editing state changes.

The following example demonstrates how to listen for text box events and parse data based on the [Integrating with ArkTS Pages](../../integrating-with-arkts-pages/document.md) section.

-   Registering events
    
    Events are registered through a unified API. For details, see [registerNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent). For details about the event types supported by the text box, see the [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) section, searching for **NODE\_TEXT\_AREA\_**.
    
    ArkUI\_NodeHandle text = nodeApi->createNode(ARKUI\_NODE\_TEXT);
    ArkUI\_NumberValue textWidth\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
    nodeApi->setAttribute(text, NODE\_WIDTH, &textWidthItem);
    // ···
    ArkUI\_NodeHandle selectionText = nodeApi->createNode(ARKUI\_NODE\_TEXT);
    ArkUI\_NumberValue selectionTextWidth\[\] = {{.f32 = 300}};
    ArkUI\_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
    nodeApi->setAttribute(selectionText, NODE\_WIDTH, &selectionTextWidthItem);
    // ···
    const ArkUI\_AttributeItem \*attributeItem = nodeApi->getAttribute(textArea, NODE\_UNIQUE\_ID);
    auto id = attributeItem->value\[0\].i32;
    nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_CHANGE, id, text);
    nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_PASTE, id, text);
    nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE, id, selectionText);
    
-   Registering event callbacks
    
    Event callbacks are registered through a unified API. For details, see [registerNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeeventreceiver).
    
    nodeApi->registerNodeEventReceiver(\[\](ArkUI\_NodeEvent \*event) {
        ArkUI\_NodeEventType eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
        ArkUI\_AttributeItem content;
        if (eventType == NODE\_TEXT\_AREA\_ON\_CHANGE || eventType == NODE\_TEXT\_AREA\_ON\_PASTE) {
            ArkUI\_StringAsyncEvent \*stringEvent = OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent(event);
            content = {.string = stringEvent->pStr };
        } else if (eventType == NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE) {
            ArkUI\_NodeComponentEvent \*componentEvent = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event);
            std::stringstream selectContent;
            selectContent << "start: " << componentEvent->data\[0\].i32 << " , end: " << componentEvent->data\[1\].i32;
            content = {.string = selectContent.str().c\_str() };
        } else {
            return;
        }
        ArkUI\_NodeHandle textNode = reinterpret\_cast<ArkUI\_NodeHandle>(OH\_ArkUI\_NodeEvent\_GetUserData(event));
        if (textNode) {
            ArkUI\_NativeNodeAPI\_1 \*nodeApi = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
                OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
            nodeApi->setAttribute(textNode, NODE\_TEXT\_CONTENT, &content);
        }
    });
    
-   Sample
    
    This section demonstrates core API usage only. For the complete sample project, see [TextAreaEventNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/TextAreaEventNDK).
    
    #include "manager.h"
    #include <sstream>
    #include <arkui/native\_interface.h>
    #include <arkui/styled\_string.h>
    
    namespace NativeNode::Manager {
    constexpr int32\_t NUM\_10 = 10;
    constexpr int32\_t NUM\_28 = 28;
    constexpr int32\_t NUM\_400 = 400;
    NodeManager &NodeManager::GetInstance()
    {
        static NodeManager instance;
        return instance;
    }
    
    void NodeManager::SetXComponent(OH\_NativeXComponent \*xComponent) { xComponent\_ = xComponent; }
    
    void NodeManager::CreateTextAreaNode()
    {
        if (!xComponent\_) {
            return;
        }
        ArkUI\_NativeNodeAPI\_1 \*nodeApi = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        if (nodeApi == nullptr) {
            return;
        }
        ArkUI\_NodeHandle column = nodeApi->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue colWidth\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem widthItem = {.value = colWidth, .size = 1};
        nodeApi->setAttribute(column, NODE\_WIDTH, &widthItem);
    
        ArkUI\_NodeHandle text = nodeApi->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_NumberValue textWidth\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
        nodeApi->setAttribute(text, NODE\_WIDTH, &textWidthItem);
        ArkUI\_NumberValue textHeight\[\] = {{.f32 = 100}};
        ArkUI\_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
        nodeApi->setAttribute(text, NODE\_HEIGHT, &textHeightItem);
        
        nodeApi->addChild(column, text);
        
        ArkUI\_NodeHandle selectionText = nodeApi->createNode(ARKUI\_NODE\_TEXT);
        ArkUI\_NumberValue selectionTextWidth\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
        nodeApi->setAttribute(selectionText, NODE\_WIDTH, &selectionTextWidthItem);
        nodeApi->addChild(column, selectionText);
        ArkUI\_NodeHandle textArea = nodeApi->createNode(ARKUI\_NODE\_TEXT\_AREA);
        ArkUI\_NumberValue textAreaWidth\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textAreaWidthItem = {.value = textAreaWidth, .size = 1};
        nodeApi->setAttribute(textArea, NODE\_WIDTH, &textAreaWidthItem);
    
        ArkUI\_NumberValue borderWidth\[\] = {{.f32 = 1}};
        ArkUI\_AttributeItem borderWidthItem = {.value = borderWidth, .size = 1};
        nodeApi->setAttribute(textArea, NODE\_BORDER\_WIDTH, &borderWidthItem);
    
        const ArkUI\_AttributeItem \*attributeItem = nodeApi->getAttribute(textArea, NODE\_UNIQUE\_ID);
        auto id = attributeItem->value\[0\].i32;
        nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_CHANGE, id, text);
        nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_PASTE, id, text);
        nodeApi->registerNodeEvent(textArea, NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE, id, selectionText);
        TextAreaNodeEventReceiver(nodeApi);
        nodeApi->addChild(column, textArea);
        OH\_NativeXComponent\_AttachNativeRootNode(xComponent\_, column);
    }
    
    void NodeManager::TextAreaNodeEventReceiver(ArkUI\_NativeNodeAPI\_1\* nodeApi)
    {
        nodeApi->registerNodeEventReceiver(\[\](ArkUI\_NodeEvent \*event) {
            ArkUI\_NodeEventType eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
            ArkUI\_AttributeItem content;
            if (eventType == NODE\_TEXT\_AREA\_ON\_CHANGE || eventType == NODE\_TEXT\_AREA\_ON\_PASTE) {
                ArkUI\_StringAsyncEvent \*stringEvent = OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent(event);
                content = {.string = stringEvent->pStr };
            } else if (eventType == NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE) {
                ArkUI\_NodeComponentEvent \*componentEvent = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event);
                std::stringstream selectContent;
                selectContent << "start: " << componentEvent->data\[0\].i32 << " , end: " << componentEvent->data\[1\].i32;
                content = {.string = selectContent.str().c\_str() };
            } else {
                return;
            }
            ArkUI\_NodeHandle textNode = reinterpret\_cast<ArkUI\_NodeHandle>(OH\_ArkUI\_NodeEvent\_GetUserData(event));
            if (textNode) {
                ArkUI\_NativeNodeAPI\_1 \*nodeApi = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
                    OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
                nodeApi->setAttribute(textNode, NODE\_TEXT\_CONTENT, &content);
            }
        });
    }
    } // namespace NativeNode::Manager
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mLKGlsmsQgW8IvdkVuMw8w/en-us_image_0000002568684605.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BBECB2C97490B11894E288985227EF8BBD33416D41CC82F15FD9D1CB3965424)
