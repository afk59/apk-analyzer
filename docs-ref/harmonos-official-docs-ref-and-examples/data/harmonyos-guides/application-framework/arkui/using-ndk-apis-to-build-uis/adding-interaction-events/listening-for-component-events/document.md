# Listening for Component Events

The NDK API provides a way to listen for UI component events through listener functions. First, you can use the [addNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodeeventreceiver) function to add an event listener for the component, which will listen for all events that occur on that component, such as click events and focus events. Then, you can use the [registerNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent) function to declare which events of the component need to be listened for. The range of events supported by the NDK API is defined through the [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype) enum.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/_35qV4s1Qi6eejNkOY9i9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=574B0272D18B161C6E8BD00DF66EA12DE0494D8C0545084418BD9D7F87B91007)

-   Event registration requires the declaration of [addNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodeeventreceiver) listener registration and [registerNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent) event types. The listener can only listen for declared events.
    
-   Pay attention to the logic of event deregistration. For example, before the component is destroyed, call [removeNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodeeventreceiver) to remove the event listener and [unregisterNodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodeevent) to notify the ArkUI framework that the listened events no longer need to be listened for.
    
-   [addNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodeeventreceiver) can add multiple function pointers, each of which is triggered when the corresponding event occurs. To remove a listener, the corresponding [removeNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#removenodeeventreceiver) function must be called with the exact function pointer used for adding the listener.
    
-   [registerNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeeventreceiver) is a global event listener function. Unlike [addNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addnodeeventreceiver), [registerNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeeventreceiver) can listen for the event triggers of all native components, but it can only accept a single function pointer. If it is called multiple times, only the last function pointer provided will be used for callbacks. To release the listener, use the [unregisterNodeEventReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#unregisternodeeventreceiver) function.
    

The following example is based on the [Integrating with ArkTS Pages](../../integrating-with-arkts-pages/document.md) section, supplementing related event listening. For the complete sample code, see [Sample Code](#sample-code).

-   Event registration and deregistration
    
    Bind event handlers to nodes using **addNodeEventReceiver**, and then register specific events with **registerNodeEvent**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/SJeabZhJS7ajU8qMEYCVdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22A4CC5A1998911B0F10330C31166950F5B71752919C50B67FC565790E392E1F)
    
    The [ArkUI\_NodeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent)\* event parameter in event callbacks is only valid during the callback execution. Do not cache this pointer or process it asynchronously.
    
    Define a pointer of type [ArkUI\_NativeNodeAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1):
    
    ArkUI\_NativeNodeAPI\_1 \*nodeAPI = nullptr;
    
    Call the [OH\_ArkUI\_GetModuleInterface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface) API to assign a value to the defined pointer:
    
    OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, nodeAPI);
    
    Define an event trigger callback function:
    
    void NodeEventReceiver(ArkUI\_NodeEvent \*event) {
      // Handle specific event types, such as NODE\_ON\_CLICK\_EVENT.
    };
    
    Create a node, bind the event trigger callback function to the node, and register the event for the node:
    
    auto button = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
    nodeAPI->addNodeEventReceiver(button, NodeEventReceiver);
    nodeAPI->registerNodeEvent(button, NODE\_ON\_CLICK\_EVENT, 0, nullptr);
    
    For details about event types, see [ArkUI\_NodeEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype).
    
    Deregister events using **unregisterNodeEvent** and remove handlers with **removeNodeEventReceiver**.
    
    Unregister the specified event type for the node:
    
    nodeAPI->unregisterNodeEvent(button, NODE\_ON\_CLICK\_EVENT);
    
    Remove the event handler function bound to the node:
    
    nodeAPI->removeNodeEventReceiver(button, NodeEventReceiver);
    
-   Global event listening
    
    Register a global event handler with **registerNodeEventReceiver** for centralized event processing. Release it with **unregisterNodeEventReceiver** when it is no longer needed.
    
    Register a global event handler function:
    
    nodeAPI->registerNodeEventReceiver(\[\](ArkUI\_NodeEvent \*event) {
        // Obtain the basic event object from the component event.
        auto \*inputEvent = OH\_ArkUI\_NodeEvent\_GetInputEvent(event);
        // Obtain the event type from the component event.
        auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
        // ···
        switch (eventType) {
            case NODE\_ON\_CLICK\_EVENT: {
                // Perform operations when the click event is triggered. Obtain event information from the base input event.
                // ···
            }
            default: {
                break;
            }
        }
    });
    
    Unregister the registered global event handler function:
    
    nodeAPI->unregisterNodeEventReceiver();
    
-   Event information retrieval
    
    Use [OH\_ArkUI\_NodeEvent\_GetInputEvent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeevent_getinputevent) to obtain input event objects for interaction-related component events (such as NODE\_ON\_CLICK\_EVENT and NODE\_TOUCH\_EVENT). Then, you can call APIs such as [OH\_ArkUI\_PointerEvent\_GetDisplayX()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_pointerevent_getdisplayx), [OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_pointerevent_getdisplayxbyindex), [OH\_ArkUI\_UIInputEvent\_GetAction()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_uiinputevent_getaction), and [OH\_ArkUI\_UIInputEvent\_GetEventTime()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_uiinputevent_geteventtime) to obtain more information from the basic event. Applications can implement differentiated interaction logic during gesture event execution based on the obtained information.
    
    Register a callback function for the event listener:
    
    // Register the click event.
    nodeAPI->registerNodeEvent(button, NODE\_ON\_CLICK\_EVENT, 0, nullptr);
    // Set a global component event listener.
    nodeAPI->registerNodeEventReceiver(\[\](ArkUI\_NodeEvent \*event) {
        // Obtain the basic event object from the component event.
        auto \*inputEvent = OH\_ArkUI\_NodeEvent\_GetInputEvent(event);
        // Obtain the event type from the component event.
        auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_eventInfo inputEvent = %{public}p", inputEvent);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_eventInfo eventType = %{public}d", eventType);
        auto componentEvent = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event);
        // Obtain the numerical data from the component event.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_eventInfo componentEvent = %{public}p", componentEvent);
        // Obtain the component object that triggers the event.
        auto nodeHandle = OH\_ArkUI\_NodeEvent\_GetNodeHandle(event);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                     "NdkAddInteractionEvent\_eventInfo nodeHandle = %{public}p", nodeHandle);
        // Differentiate event types and handle them accordingly. Other event information APIs follow similar usage patterns.
        switch (eventType) {
            case NODE\_ON\_CLICK\_EVENT: {
                // Perform operations when the click event is triggered. Obtain event information from the base input event.
                auto x = OH\_ArkUI\_PointerEvent\_GetX(inputEvent);
                auto y = OH\_ArkUI\_PointerEvent\_GetY(inputEvent);
                auto displayX = OH\_ArkUI\_PointerEvent\_GetDisplayX(inputEvent);
                auto displayY = OH\_ArkUI\_PointerEvent\_GetDisplayY(inputEvent);
                auto windowX = OH\_ArkUI\_PointerEvent\_GetWindowX(inputEvent);
                auto windowY = OH\_ArkUI\_PointerEvent\_GetWindowY(inputEvent);
                auto pointerCount = OH\_ArkUI\_PointerEvent\_GetPointerCount(inputEvent);
                auto xByIndex = OH\_ArkUI\_PointerEvent\_GetXByIndex(inputEvent, 0);
                auto yByIndex = OH\_ArkUI\_PointerEvent\_GetYByIndex(inputEvent, 0);
                auto displayXByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(inputEvent, 0);
                auto displayYByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(inputEvent, 0);
                auto windowXByIndex = OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(inputEvent, 0);
                auto windowYByIndex = OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(inputEvent, 0);
                auto pointerId = OH\_ArkUI\_PointerEvent\_GetPointerId(inputEvent, 0);
                auto pressure = OH\_ArkUI\_PointerEvent\_GetPressure(inputEvent, 0);
                auto action = OH\_ArkUI\_UIInputEvent\_GetAction(inputEvent);
                auto eventTime = OH\_ArkUI\_UIInputEvent\_GetEventTime(inputEvent);
                auto sourceType = OH\_ArkUI\_UIInputEvent\_GetSourceType(inputEvent);
                auto type = OH\_ArkUI\_UIInputEvent\_GetType(inputEvent);
                std::string eventInfo =
                    "x: " + std::to\_string(x) + ", y: " + std::to\_string(y) +
                    ", displayX: " + std::to\_string(displayX) + ", displayY: " + std::to\_string(displayY) +
                    ", windowX: " + std::to\_string(windowX) + ", windowY: " + std::to\_string(windowY) +
                    ", pointerCount: " + std::to\_string(pointerCount) + ", xByIndex: " + std::to\_string(xByIndex) +
                    ", yByIndex: " + std::to\_string(yByIndex) +
                    ", displayXByIndex: " + std::to\_string(displayXByIndex) +
                    ", displayYByIndex: " + std::to\_string(displayYByIndex) +
                    ", windowXByIndex: " + std::to\_string(windowXByIndex) +
                    ", windowYByIndex: " + std::to\_string(windowYByIndex) +
                    ", pointerId: " + std::to\_string(pointerId) + ", pressure: " + std::to\_string(pressure) +
                    ", action: " + std::to\_string(action) + ", eventTime: " + std::to\_string(eventTime) +
                    ", sourceType: " + std::to\_string(sourceType) + ", type: " + std::to\_string(type);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                             "NdkAddInteractionEvent\_eventInfoOfCommonEvent eventInfo = %{public}s",
                             eventInfo.c\_str());
                break;
            }
            default: {
                break;
            }
        }
    });
    
    Unregister the registered event handler function:
    
    nodeAPI->unregisterNodeEventReceiver();
    
    Unregister the specified event type for the node:
    
    nodeAPI->unregisterNodeEvent(button, NODE\_ON\_CLICK\_EVENT);
    
-   Color mode change event
    
    The ArkUI development framework provides system color mode (dark/light) change events through NDK APIs at the component level. When the system color mode changes, the framework notifies registered component callbacks, enabling color mode adaptation capabilities on the NDK side.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/QNBiwJqcQi6Pz9odM8xN8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=485A82DCC09F260F28AF9E01C39B4DDF2014DFA0AA514D73932172C996F66D71)
    
    -   Multiple components can share the same callback for color mode changes.
    -   A single component can only register one callback for system color mode changes.
    -   It is recommended that you register persistent nodes (those that will not be destroyed during the page lifecycle) to prevent callback failures due to node destruction.
    
    struct ColorModeInfo {
        const char\* lightMsg;
        const char\* darkMsg;
    };
    
    // Register a callback.
    void onColorModeChange(ArkUI\_SystemColorMode colorMode, void \*userData)
    {
        ColorModeInfo\* info = static\_cast<ColorModeInfo\*>(userData);
        if (colorMode == ARKUI\_SYSTEM\_COLOR\_MODE\_LIGHT) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                         "NdkAddInteractionEvent\_Light mode: ", info->lightMsg);
        } else if (colorMode == ARKUI\_SYSTEM\_COLOR\_MODE\_DARK) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                         "NdkAddInteractionEvent\_Dark mode: ", info->darkMsg);
        }
    }
    
    ArkUI\_NodeHandle testColorModeChange(ArkUI\_NativeNodeAPI\_1 \*nodeAPI) {
        ArkUI\_NodeHandle text = nodeAPI->createNode(ARKUI\_NODE\_TEXT);
        static ColorModeInfo info = {"Light mode", "Dark mode"};
        OH\_ArkUI\_RegisterSystemColorModeChangeEvent(text, &info, onColorModeChange);
    
        ArkUI\_AttributeItem itemstring = {nullptr, 0, ("test\_light\_dark")};
        nodeAPI->setAttribute(text, NODE\_TEXT\_CONTENT, &itemstring);
    
        return text;
    }
    

#### Sample Code

1.  Implement common event registration logic in the **ArkUINode** base class object.
    
    // ArkUINode.h
    // Provide encapsulation of common properties and events.
    
    #ifndef MYAPPLICATION\_ARKUINODE\_H
    #define MYAPPLICATION\_ARKUINODE\_H
    
    #include "ArkUIBaseNode.h"
    #include "NativeModule.h"
    
    #include <arkui/native\_node.h>
    #include <arkui/native\_type.h>
    
    namespace NativeModule {
    
    class ArkUINode : public ArkUIBaseNode {
    public:
        explicit ArkUINode(ArkUI\_NodeHandle handle) : ArkUIBaseNode(handle)
        {
            nativeModule\_ = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
            // When an event is triggered, you need to get the corresponding event object through a function. Here, by setting the node's custom data, the encapsulated class pointer is kept on the component for subsequent event distribution.
            nativeModule\_->setUserData(handle\_, this);
            // Register the node event receiver.
            nativeModule\_->addNodeEventReceiver(handle\_, ArkUINode::NodeEventReceiver);
        }
    
        ~ArkUINode() override
        {
            if (onClick\_) {
                nativeModule\_->unregisterNodeEvent(handle\_, NODE\_ON\_CLICK\_EVENT);
            }
            if (onTouch\_) {
                nativeModule\_->unregisterNodeEvent(handle\_, NODE\_TOUCH\_EVENT);
            }
            if (onDisappear\_) {
                nativeModule\_->unregisterNodeEvent(handle\_, NODE\_EVENT\_ON\_DISAPPEAR);
            }
            if (onAppear\_) {
                nativeModule\_->unregisterNodeEvent(handle\_, NODE\_EVENT\_ON\_APPEAR);
            }
            nativeModule\_->removeNodeEventReceiver(handle\_, ArkUINode::NodeEventReceiver);
        }
        // Set the node brightness.
        void SetWidth(float width)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_NumberValue value\[\] = {{.f32 = width}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH, &item);
        }
        // Set the node width (in percentage).
        void SetPercentWidth(float percent)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_WIDTH\_PERCENT, &item);
        }
        // Set the node height.
        void SetHeight(float height)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_NumberValue value\[\] = {{.f32 = height}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT, &item);
        }
        // Set the node height (in percentage).
        void SetPercentHeight(float percent)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_NumberValue value\[\] = {{.f32 = percent}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_HEIGHT\_PERCENT, &item);
        }
        // Set the background color of the node.
        void SetBackgroundColor(uint32\_t color)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_NumberValue value\[\] = {{.u32 = color}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_BACKGROUND\_COLOR, &item);
        }
        // Process common events.
        void RegisterOnClick(const std::function<void(ArkUI\_NodeEvent \*event)> &onClick)
        {
            if (!handle\_) {
                return;
            }
            onClick\_ = onClick;
            // Register the click event.
            nativeModule\_->registerNodeEvent(handle\_, NODE\_ON\_CLICK\_EVENT, 0, nullptr);
        }
    
        void RegisterOnTouch(const std::function<void(int32\_t type, float x, float y)> &onTouch)
        {
            if (!handle\_) {
                return;
            }
            onTouch\_ = onTouch;
            // Register the touch event.
            nativeModule\_->registerNodeEvent(handle\_, NODE\_TOUCH\_EVENT, 0, nullptr);
        }
    
        void RegisterOnDisappear(const std::function<void()> &onDisappear)
        {
            if (!handle\_) {
                return;
            }
            onDisappear\_ = onDisappear;
            // Register the disappear event.
            nativeModule\_->registerNodeEvent(handle\_, NODE\_EVENT\_ON\_DISAPPEAR, 0, nullptr);
        }
    
        void RegisterOnAppear(const std::function<void()> &onAppear)
        {
            if (!handle\_) {
                return;
            }
            onAppear\_ = onAppear;
            // Register the appear event.
            nativeModule\_->registerNodeEvent(handle\_, NODE\_EVENT\_ON\_APPEAR, 0, nullptr);
        }
    
    protected:
        // Event listener function pointer.
        static void NodeEventReceiver(ArkUI\_NodeEvent \*event)
        {
            // Obtain the UI component object where the event occurs.
            auto nodeHandle = OH\_ArkUI\_NodeEvent\_GetNodeHandle(event);
            // Obtain the custom data kept in the UI component object, and return the encapsulated class pointer.
            auto \*node = reinterpret\_cast<ArkUINode \*>(
                NativeModuleInstance::GetInstance()->GetNativeNodeAPI()->getUserData(nodeHandle));
            // Process the event based on the encapsulated class instance object.
            node->ProcessNodeEvent(event);
        }
        void ProcessNodeEvent(ArkUI\_NodeEvent \*event)
        {
            auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
            switch (eventType) {
                case NODE\_ON\_CLICK\_EVENT: {
                    if (onClick\_) {
                        onClick\_(event);
                    }
                    break;
                }
                case NODE\_TOUCH\_EVENT: {
                    if (onTouch\_) {
                        auto \*uiInputEvent = OH\_ArkUI\_NodeEvent\_GetInputEvent(event);
                        float x = OH\_ArkUI\_PointerEvent\_GetX(uiInputEvent);
                        float y = OH\_ArkUI\_PointerEvent\_GetY(uiInputEvent);
                        auto type = OH\_ArkUI\_UIInputEvent\_GetAction(uiInputEvent);
                        onTouch\_(type, x, y);
                    }
                }
                case NODE\_EVENT\_ON\_DISAPPEAR: {
                    if (onDisappear\_) {
                        onDisappear\_();
                    }
                    break;
                }
                case NODE\_EVENT\_ON\_APPEAR: {
                    if (onAppear\_) {
                        onAppear\_();
                    }
                    break;
                }
                default: {
                    // Component-specific events are processed by child classes.
                    OnNodeEvent(event);
                }
            }
        }
    
        virtual void OnNodeEvent(ArkUI\_NodeEvent \*event) {}
    
        void OnAddChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->addChild(handle\_, child->GetHandle());
        }
    
        void OnRemoveChild(const std::shared\_ptr<ArkUIBaseNode> &child) override
        {
            nativeModule\_->removeChild(handle\_, child->GetHandle());
        }
    
        void OnInsertChild(const std::shared\_ptr<ArkUIBaseNode> &child, int32\_t index) override
        {
            nativeModule\_->insertChildAt(handle\_, child->GetHandle(), index);
        }
    
    private:
        std::function<void(ArkUI\_NodeEvent \*event)> onClick\_;
        std::function<void()> onDisappear\_;
        std::function<void()> onAppear\_;
        std::function<void(int32\_t type, float x, float y)> onTouch\_;
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUINODE\_H
    
2.  Implement list event registration logic in the **ArkUIListNode** object.
    
    // ArkUIListNode.h
    // List encapsulation class object
    
    #ifndef MYAPPLICATION\_ARKUILISTNODE\_H
    #define MYAPPLICATION\_ARKUILISTNODE\_H
    
    #include "ArkUINode.h"
    
    namespace NativeModule {
    class ArkUIListNode : public ArkUINode {
    public:
        ArkUIListNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST)) {}
    
        ~ArkUIListNode() override { nativeModule\_->unregisterNodeEvent(handle\_, NODE\_LIST\_ON\_SCROLL\_INDEX); }
    
        void SetScrollBarState(bool isShow)
        {
            if (!handle\_) {
                return;
            }
            ArkUI\_ScrollBarDisplayMode displayMode =
                isShow ? ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON : ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF;
            ArkUI\_NumberValue value\[\] = {{.i32 = displayMode}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_BAR\_DISPLAY\_MODE, &item);
        }
    
        // Register list-related events.
        void RegisterOnScrollIndex(const std::function<void(int32\_t index)> &onScrollIndex)
        {
            if (!handle\_) {
                return;
            }
            onScrollIndex\_ = onScrollIndex;
            nativeModule\_->registerNodeEvent(handle\_, NODE\_LIST\_ON\_SCROLL\_INDEX, 0, nullptr);
        }
    
    protected:
       // Process list-related events.
        void OnNodeEvent(ArkUI\_NodeEvent \*event) override
        {
            auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
            switch (eventType) {
                case NODE\_LIST\_ON\_SCROLL\_INDEX: {
                    auto index = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event)->data\[0\];
                    if (onScrollIndex\_) {
                        onScrollIndex\_(index.i32);
                    }
                }
                default: {
                }
            }
        }
    
    private:
        std::function<void(int32\_t index)> onScrollIndex\_;
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUILISTNODE\_H
    
3.  Add related events.
    
    // NormalTextListExample.h
    // Text list example.
    
    #ifndef MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    #define MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIListItemNode.h"
    #include "ArkUIListNode.h"
    #include "ArkUITextNode.h"
    #include <hilog/log.h>
    
    const unsigned int LOG\_PRINT\_DOMAIN = 0xF811;
    const unsigned int LOOP\_SIZE = 30;
    const unsigned int FONT\_SIZE = 16;
    const unsigned int HEIGHT\_SIZE = 200;
    const float PERCENT\_WIDTH\_1 = 1;
    const float PERCENT\_HEIGHT\_1 = 1;
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateTextListExample()
    {
        // Create components and mount them.
        // 1: Create a List component.
        auto list = std::make\_shared<ArkUIListNode>();
        list->SetPercentWidth(PERCENT\_WIDTH\_1);
        list->SetPercentHeight(PERCENT\_HEIGHT\_1);
        // 2: Create a ListItem child component and mount it to the List component.
        for (int32\_t i = 0; i < LOOP\_SIZE; ++i) {
            auto listItem = std::make\_shared<ArkUIListItemNode>();
            auto textNode = std::make\_shared<ArkUITextNode>();
            textNode->SetTextContent(std::to\_string(i));
            textNode->SetFontSize(FONT\_SIZE);
            textNode->SetPercentWidth(PERCENT\_WIDTH\_1);
            textNode->SetHeight(HEIGHT\_SIZE);
            textNode->SetBackgroundColor(0xFFfffacd);
            textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            listItem->AddChild(textNode);
            // Register the click event for the list item.
            auto onClick = \[\](ArkUI\_NodeEvent \*event) {
                // Obtain the basic event object from the component event.
                auto \*inputEvent = OH\_ArkUI\_NodeEvent\_GetInputEvent(event);
                if (inputEvent == nullptr) {
                    return;
                }
                // Obtain the event type from the component event.
                auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                             "NdkAddInteractionEvent\_eventInfo inputEvent = %{public}p", inputEvent);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                             "NdkAddInteractionEvent\_eventInfo eventType = %{public}d", eventType);
                auto componentEvent = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event);
                // Obtain the numerical data from the component event.
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                             "NdkAddInteractionEvent\_eventInfo componentEvent = %{public}p", componentEvent);
                // Obtain the component object that triggers the event.
                auto nodeHandle = OH\_ArkUI\_NodeEvent\_GetNodeHandle(event);
                if (nodeHandle == nullptr) {
                    return;
                }
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                             "NdkAddInteractionEvent\_eventInfo nodeHandle = %{public}p", nodeHandle);
                // Differentiate event types and handle them accordingly. Other event information APIs follow similar usage patterns.
                switch (eventType) {
                    case NODE\_ON\_CLICK\_EVENT: {
                        // Perform operations when the click event is triggered. Obtain event information from the base input event.
                        auto x = OH\_ArkUI\_PointerEvent\_GetX(inputEvent);
                        auto y = OH\_ArkUI\_PointerEvent\_GetY(inputEvent);
                        auto displayX = OH\_ArkUI\_PointerEvent\_GetDisplayX(inputEvent);
                        auto displayY = OH\_ArkUI\_PointerEvent\_GetDisplayY(inputEvent);
                        auto windowX = OH\_ArkUI\_PointerEvent\_GetWindowX(inputEvent);
                        auto windowY = OH\_ArkUI\_PointerEvent\_GetWindowY(inputEvent);
                        auto pointerCount = OH\_ArkUI\_PointerEvent\_GetPointerCount(inputEvent);
                        auto xByIndex = OH\_ArkUI\_PointerEvent\_GetXByIndex(inputEvent, 0);
                        auto yByIndex = OH\_ArkUI\_PointerEvent\_GetYByIndex(inputEvent, 0);
                        auto displayXByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayXByIndex(inputEvent, 0);
                        auto displayYByIndex = OH\_ArkUI\_PointerEvent\_GetDisplayYByIndex(inputEvent, 0);
                        auto windowXByIndex = OH\_ArkUI\_PointerEvent\_GetWindowXByIndex(inputEvent, 0);
                        auto windowYByIndex = OH\_ArkUI\_PointerEvent\_GetWindowYByIndex(inputEvent, 0);
                        auto pointerId = OH\_ArkUI\_PointerEvent\_GetPointerId(inputEvent, 0);
                        auto pressure = OH\_ArkUI\_PointerEvent\_GetPressure(inputEvent, 0);
                        auto action = OH\_ArkUI\_UIInputEvent\_GetAction(inputEvent);
                        auto eventTime = OH\_ArkUI\_UIInputEvent\_GetEventTime(inputEvent);
                        auto sourceType = OH\_ArkUI\_UIInputEvent\_GetSourceType(inputEvent);
                        auto type = OH\_ArkUI\_UIInputEvent\_GetType(inputEvent);
                        std::string eventInfo =
                            "x: " + std::to\_string(x) + ", y: " + std::to\_string(y) +
                            ", displayX: " + std::to\_string(displayX) + ", displayY: " + std::to\_string(displayY) +
                            ", windowX: " + std::to\_string(windowX) + ", windowY: " + std::to\_string(windowY) +
                            ", pointerCount: " + std::to\_string(pointerCount) + ", xByIndex: " + std::to\_string(xByIndex) +
                            ", yByIndex: " + std::to\_string(yByIndex) +
                            ", displayXByIndex: " + std::to\_string(displayXByIndex) +
                            ", displayYByIndex: " + std::to\_string(displayYByIndex) +
                            ", windowXByIndex: " + std::to\_string(windowXByIndex) +
                            ", windowYByIndex: " + std::to\_string(windowYByIndex) +
                            ", pointerId: " + std::to\_string(pointerId) + ", pressure: " + std::to\_string(pressure) +
                            ", action: " + std::to\_string(action) + ", eventTime: " + std::to\_string(eventTime) +
                            ", sourceType: " + std::to\_string(sourceType) + ", type: " + std::to\_string(type);
                        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "\[Sample\_NdkAddInteractionEvent\]",
                                     "NdkAddInteractionEvent\_eventInfoOfCommonEvent eventInfo = %{public}s",
                                     eventInfo.c\_str());
                    }
                    default: {
                        break;
                    }
                }
            };
            listItem->RegisterOnClick(onClick);
            list->AddChild(listItem);
        }
        // 3: Register list-related listening events.
        list->RegisterOnScrollIndex(\[\](int32\_t index) { OH\_LOG\_INFO(LOG\_APP, "on list scroll index: %{public}d", index); });
        // 4: Register the appear event.
        list->RegisterOnAppear(\[\]() { OH\_LOG\_INFO(LOG\_APP, "on list mount to tree"); });
        // 5: Register the disappear event.
        list->RegisterOnDisappear(\[\]() { OH\_LOG\_INFO(LOG\_APP, "on list unmount from tree"); });
        return list;
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_NORMALTEXTLISTEXAMPLE\_H
    
    Since log-related APIs are used, add a reference to **libhilog\_ndk.z.so** in the **CMakeLists.txt** file as follows:
    
    add\_library(entry SHARED napi\_init.cpp NativeEntry.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libace\_ndk.z.so libhilog\_ndk.z.so)
