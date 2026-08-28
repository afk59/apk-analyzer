# Integrating Accessibility Through XComponent

For third-party framework platforms that are accessed through XComponent, the NDK provides functions for interoperability with accessibility services, enabling third-party framework components to support basic accessibility features in ArkUI. These include focus acquisition, accessibility node retrieval, and operation response.

If a single instance is required, use [OH\_NativeXComponent\_GetNativeAccessibilityProvider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-xcomponent-h#oh_nativexcomponent_getnativeaccessibilityprovider) of XComponent to obtain the [ArkUI\_AccessibilityProvider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pi-arkui-accessibility-arkui-accessibilityprovider) instance. and then register the required callback functions [ArkUI\_AccessibilityProviderCallbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/accessibility-arkui-accessibilityprovidercallbacks) via [OH\_ArkUI\_AccessibilityProviderRegisterCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallback).

For multi-instance scenarios, register callback functions [ArkUI\_AccessibilityProviderCallbacksWithInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/y-arkui-accessibilityprovidercallbackswithinstance) using [OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallbackwithinstance).

In these callbacks, third-party frameworks must handle accessibility [actions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#arkui_accessibility_actiontype) from the accessibility system and send appropriate accessibility [events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#arkui_accessibilityeventtype) based on component interactions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/c9aCSCT8TJ2AloDQIeTTig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=285005F57E8BD8867269D593ADFFC913EF583667CA46BDF61166755B0D1B4CFF)

-   Accessibility capability enables you to create accessible application UIs for users with visual, auditory, motor, and cognitive disabilities.
-   When implementing query APIs ([OH\_ArkUI\_AccessibilityProviderRegisterCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallback) or [OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallbackwithinstance)), use [OH\_ArkUI\_AddAndGetAccessibilityElementInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_addandgetaccessibilityelementinfo) to create and manage accessibility node information.
-   When sending events with [OH\_ArkUI\_SendAccessibilityAsyncEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_sendaccessibilityasyncevent), create event and element info objects using the appropriate creation functions and destroy them after use. Specifically, create an [ArkUI\_AccessibilityEventInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/i-arkui-accessibility-arkui-accessibilityeventinfo) object using [OH\_ArkUI\_CreateAccessibilityEventInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_createaccessibilityeventinfo) and an [ArkUI\_AccessibilityElementInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkui-accessibility-arkui-accessibilityelementinfo) object using [OH\_ArkUI\_CreateAccessibilityElementInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_createaccessibilityelementinfo), and then destroy the objects after use with [OH\_ArkUI\_DestoryAccessibilityEventInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_destoryaccessibilityeventinfo) and [OH\_ArkUI\_DestoryAccessibilityElementInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_destoryaccessibilityelementinfo).
-   When logging within callback functions, include the provided **requestId** parameter to link logs to a specific interaction process. This practice facilitates indexing and querying and aids in troubleshooting and pinpointing issues.

This example demonstrates accessibility integration. For the complete implementation, see [AccessibilityCapiSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AccessibilityCapi). Once integrated, third-party framework components in **XComponent** will support accessibility interactions when accessibility features are enabled.

1.  Create a project based on [OH\_ArkUI\_SurfaceHolder for surface lifecycle management](../../ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md#managing-the-lifecycle-of-the-surface-held-by-xcomponent) in custom rendering (XComponent).
    
2.  Obtain the accessibility provider and register callbacks (the following uses the multi-instance scenario as an example).
    
    #include <arkui/native\_interface\_accessibility.h>
    #include <string>
    #include "common/common.h"
    // For details about the complete implementation, see AccessibilityCapiSample.
    #include "fakenode/fake\_node.h"
    // For details about the complete implementation, see AccessibilityCapiSample.
    #include "AccessibilityManager.h"
    
    // ...
    AccessibilityManager::AccessibilityManager()
    {
    // Multi-instance scenario
        accessibilityProviderCallbacksWithInstance\_.findAccessibilityNodeInfosById = FindAccessibilityNodeInfosById;
        accessibilityProviderCallbacksWithInstance\_.findAccessibilityNodeInfosByText = FindAccessibilityNodeInfosByText;
        accessibilityProviderCallbacksWithInstance\_.findFocusedAccessibilityNode = FindFocusedAccessibilityNode;
        accessibilityProviderCallbacksWithInstance\_.findNextFocusAccessibilityNode = FindNextFocusAccessibilityNode;
        accessibilityProviderCallbacksWithInstance\_.executeAccessibilityAction = ExecuteAccessibilityAction;
        accessibilityProviderCallbacksWithInstance\_.clearFocusedFocusAccessibilityNode = ClearFocusedFocusAccessibilityNode;
        accessibilityProviderCallbacksWithInstance\_.getAccessibilityNodeCursorPosition = GetAccessibilityNodeCursorPosition;
    // Single-instance scenario
        accessibilityProviderCallbacks\_.findAccessibilityNodeInfosById = FindAccessibilityNodeInfosById;
        accessibilityProviderCallbacks\_.findAccessibilityNodeInfosByText = FindAccessibilityNodeInfosByText;
        accessibilityProviderCallbacks\_.findFocusedAccessibilityNode = FindFocusedAccessibilityNode;
        accessibilityProviderCallbacks\_.findNextFocusAccessibilityNode = FindNextFocusAccessibilityNode;
        accessibilityProviderCallbacks\_.executeAccessibilityAction = ExecuteAccessibilityAction;
        accessibilityProviderCallbacks\_.clearFocusedFocusAccessibilityNode = ClearFocusedFocusAccessibilityNode;
        accessibilityProviderCallbacks\_.getAccessibilityNodeCursorPosition = GetAccessibilityNodeCursorPosition;
    }
    
    void AccessibilityManager::Initialize(const std::string &id, OH\_NativeXComponent \*nativeXComponent)
    {
        int32\_t ret = OH\_NativeXComponent\_GetNativeAccessibilityProvider(nativeXComponent, &provider);
        if (provider == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "get provider is null");
            return;
        }
        // 2. Register callbacks.
        ret = OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance(id.c\_str(), provider,
            &accessibilityProviderCallbacksWithInstance\_);
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                         "InterfaceDesignTest OH\_ArkUI\_AccessibilityProviderRegisterCallback failed");
            return;
        }
        g\_provider = provider;
    }
    
    // ...
    
3.  Third-party frameworks must implement the following callbacks:
    
    int32\_t AccessibilityManager::FindAccessibilityNodeInfosById(const char\* instanceId, int64\_t elementId,
        ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList \*elementList)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "FindAccessibilityNodeInfosById start,instanceId %{public}s elementId: %{public}ld, "
                     "requestId: %{public}d, mode: %{public}d", instanceId,
                     elementId, requestId, static\_cast<int32\_t>(mode));
        if (elementList == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                         "FindAccessibilityNodeInfosById elementList is null");
            return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
        }
        int ret = 0;
        const int parentOfRoot = -2100000;
        if (elementId == -1) {
            elementId = 0;
        }
        
        if (mode == ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_RECURSIVE\_CHILDREN) {
            // Third-party frameworks must implement custom search logic in this method and return accessibility node information to the accessibility service. The following implementation serves as a reference example only.
            // Special constant defined for ArkUI framework compatibility. Root node parent ID must be set to this specific value.
            auto rootNode = OH\_ArkUI\_AddAndGetAccessibilityElementInfo(elementList);
            if (!rootNode) {
                return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
            }
            // Set the root node information.
            OH\_ArkUI\_AccessibilityElementInfoSetElementId(rootNode, 0);
            OH\_ArkUI\_AccessibilityElementInfoSetParentId(rootNode, parentOfRoot);
            FakeWidget::Instance().fillAccessibilityElement(rootNode);
    
            ArkUI\_AccessibleRect rect;
            rect.leftTopX = NUMBER\_ZERO;
            rect.leftTopY = NUMBER\_ZERO;
            rect.rightBottomX = NUMBER\_THIRD;
            rect.rightBottomY = NUMBER\_THIRD;
            ret = OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(rootNode, &rect);
            // Set the root node to be ignored by accessibility services.
            OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(rootNode, "no");
            auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
            int64\_t childNodes\[1024\];
            for (int i = 0; i < objects.size(); i++) {
                int elementId = i + 1;
    
                childNodes\[i\] = elementId;
            }
            for (int i = 0; i < objects.size(); i++) {
                int elementId = i + 1;
                childNodes\[i\] = elementId;
                auto child = OH\_ArkUI\_AddAndGetAccessibilityElementInfo(elementList);
                // Set the child node information.
                OH\_ArkUI\_AccessibilityElementInfoSetElementId(child, elementId);
                OH\_ArkUI\_AccessibilityElementInfoSetParentId(child, 0);
                // Set the current component to be accessible to accessibility services.
                OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(child, "yes");
                objects\[i\]->fillAccessibilityElement(child);
    
                ArkUI\_AccessibleRect rect;
                rect.leftTopX = i \* NUMBER\_FIRST;
                rect.leftTopY = NUMBER\_FIRST;
                rect.rightBottomX = i \* NUMBER\_FIRST + NUMBER\_FIRST;
                rect.rightBottomY = NUMBER\_SECOND;
                OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(child, &rect);
                if (objects\[i\]->ObjectType() == "FakeSlider") {
                    auto rangeInfo = objects\[i\]->GetRangeInfo();
                    OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo(child, &rangeInfo);
                }
                if (objects\[i\]->ObjectType() == "FakeList") {
                    auto gridInfo = objects\[i\]->GetGridInfo();
                    OH\_ArkUI\_AccessibilityElementInfoSetGridInfo(child, &gridInfo);
                }
                if (objects\[i\]->ObjectType() == "FakeSwiper") {
                    auto gridItemInfo = objects\[i\]->GetGridItemInfo();
                    OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo(child, &gridItemInfo);
                }
            }
    
            ret = OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds(rootNode, objects.size(), childNodes);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                         "FindAccessibilityNodeInfosById child count: %{public}ld %{public}d",
                         objects.size(), ret);
        } else if (mode == ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_CURRENT) {
            auto &widget = FakeWidget::Instance();
            AccessibleObject \*obj = nullptr;
            if (elementId == 0) {
                obj = &widget;
            } else {
                obj = widget.GetChild(elementId);
            }
            if (!obj) {
                return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
            }
            auto node = OH\_ArkUI\_AddAndGetAccessibilityElementInfo(elementList);
            OH\_ArkUI\_AccessibilityElementInfoSetElementId(node, elementId);
            OH\_ArkUI\_AccessibilityElementInfoSetParentId(node, elementId == 0 ? parentOfRoot : 0);
            OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(node, elementId == 0 ?  "no" : "yes");
            obj->fillAccessibilityElement(node);
            ArkUI\_AccessibleRect rect;
            if (elementId == 0) {
                rect.leftTopX = NUMBER\_ZERO;
                rect.leftTopY = NUMBER\_ZERO;
                rect.rightBottomX = NUMBER\_THIRD;
                rect.rightBottomY = NUMBER\_THIRD;
            } else {
                int i = elementId - 1;
                rect.leftTopX = i \* NUMBER\_FIRST;
                rect.leftTopY = NUMBER\_FIRST;
                rect.rightBottomX = i \* NUMBER\_FIRST + NUMBER\_FIRST;
                rect.rightBottomY = NUMBER\_SECOND;
            }
    
            OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(node, &rect);
            if (elementId == 0) {
                auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
                int64\_t childNodes\[1024\];
    
                for (int i = 0; i < objects.size(); i++) {
                    int elementId = i + 1;
    
                    childNodes\[i\] = elementId;
                    auto child = OH\_ArkUI\_AddAndGetAccessibilityElementInfo(elementList);
                    OH\_ArkUI\_AccessibilityElementInfoSetElementId(child, elementId);
                    OH\_ArkUI\_AccessibilityElementInfoSetParentId(child, 0);
    
                    objects\[i\]->fillAccessibilityElement(child);
    
                    ArkUI\_AccessibleRect rect;
                    rect.leftTopX = i \* NUMBER\_FIRST;
                    rect.leftTopY = NUMBER\_ZERO;
                    rect.rightBottomX = i \* NUMBER\_FIRST + NUMBER\_FIRST;
                    rect.rightBottomY = NUMBER\_SECOND;
                    OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(child, &rect);
                }
                ret = OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds(node, objects.size(), childNodes);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                             "FindAccessibilityNodeInfosById child2 count: %{public}ld", objects.size());
            }
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "FindAccessibilityNodeInfosById end");
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    int32\_t AccessibilityManager::FindNextFocusAccessibilityNode(const char\* instanceId, int64\_t elementId,
        ArkUI\_AccessibilityFocusMoveDirection direction, int32\_t requestId,
        ArkUI\_AccessibilityElementInfo \*elementInfo)
    {
        // Search for the next focusable accessibility node. The third-party framework needs to implement its own search policy in this method. The following logic is only an example.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "FindNextFocusAccessibilityNode instanceId %{public}s "
                     "elementId: %{public}ld, requestId: %{public}d, direction: %{public}d",
                     instanceId, elementId, requestId, static\_cast<int32\_t>(direction));
        auto objects = FakeWidget::Instance().GetAllObjects(instanceId);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "objects.size() %{public}d", objects.size());
        // object.size does not contain the root node.
        if ((elementId < 0) || (elementId > objects.size())) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "elementId invalid");
            return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
        }
        int64\_t nextElementId = -1;
        if (direction == ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_FORWARD) {
            nextElementId = elementId + 1;
        } else {
            nextElementId = elementId - 1;
        }
        
        // Screen reader constraint: If it is the root node and navigating backward, return to the last node.
        if ((nextElementId == -1) && (direction == ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_BACKWARD)) {
            nextElementId = objects.size();
        }
        
        if (nextElementId >  objects.size()) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "nextElementId invalid");
            return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
        }
        
        if (nextElementId <=  0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "nextElementId less than zero");
            return OH\_NATIVEXCOMPONENT\_RESULT\_FAILED;
        }
        OH\_ArkUI\_AccessibilityElementInfoSetElementId(elementInfo, nextElementId);
        OH\_ArkUI\_AccessibilityElementInfoSetParentId(elementInfo, 0);
        // The ID is 1 greater than the object index.
        objects\[nextElementId - 1\]->fillAccessibilityElement(elementInfo);
        ArkUI\_AccessibleRect rect;
        rect.leftTopX = nextElementId \* NUMBER\_FIRST;
        rect.leftTopY = NUMBER\_ZERO;
        rect.rightBottomX = nextElementId \* NUMBER\_FIRST + NUMBER\_FIRST;
        rect.rightBottomY = NUMBER\_SECOND;
        OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(elementInfo, &rect);
        auto eventInfo = OH\_ArkUI\_CreateAccessibilityEventInfo();
        OH\_ArkUI\_AccessibilityEventSetRequestFocusId(eventInfo, requestId);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "%{public}ld", nextElementId);
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    int32\_t AccessibilityManager::FindAccessibilityNodeInfosByText(const char\* instanceId, int64\_t elementId,
        const char \*text, int32\_t requestId, ArkUI\_AccessibilityElementInfoList \*elementList)
    {
        // Third-party frameworks need to implement the logic for querying accessibility nodes based on text content.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "FindAccessibilityNodeInfosByText start,instanceId %{public}s elementId: %{public}ld, "
                     "requestId: %{public}d, text: %{public}s.", instanceId,
                     elementId, requestId, text);
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    int32\_t AccessibilityManager::FindFocusedAccessibilityNode(const char\* instanceId, int64\_t elementId,
        ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo \*elementInfo)
    {
        // Third-party frameworks need to implement the logic for obtaining the focus element information based on a specified node.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "FindFocusedAccessibilityNode start instanceId %{public}s, "
                     "elementId: %{public}ld, requestId: %{public}d, focusType: %{public}d",
                     instanceId, elementId, requestId, static\_cast<int32\_t>(focusType));
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    void FillEvent(ArkUI\_AccessibilityEventInfo \*eventInfo, ArkUI\_AccessibilityElementInfo \*elementInfo,
                   ArkUI\_AccessibilityEventType eventType, std::string announcedText)
    {
        if (eventInfo == nullptr) {
            return;
        }
        if (elementInfo == nullptr) {
            return;
        }
        // Set the event type.
        OH\_ArkUI\_AccessibilityEventSetEventType(eventInfo, eventType);
        // Set the element information corresponding to the event.
        OH\_ArkUI\_AccessibilityEventSetElementInfo(eventInfo, elementInfo);
        
        if (eventType == ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ANNOUNCE\_FOR\_ACCESSIBILITY && announcedText.size() > 0) {
            // Set the accessibility text that takes precedence during announcement for the accessibility node.
            OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility(eventInfo, announcedText.data());
        }
    }
    
    // ...
    
    void AccessibilityManager::SendAccessibilityAsyncEvent(ArkUI\_AccessibilityElementInfo \*elementInfo,
                                                           ArkUI\_AccessibilityEventType eventType,
                                                           std::string announcedText)
    {
        auto eventInfo = OH\_ArkUI\_CreateAccessibilityEventInfo();
        // 1. Enter the event content.
        FillEvent(eventInfo, elementInfo, eventType, announcedText);
        // 2. Callback
        auto callback = \[\](int32\_t errorCode) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT, "result: %{public}d", errorCode);
        };
        // 3. Call the API to send the event to the HarmonyOS side.
        OH\_ArkUI\_SendAccessibilityAsyncEvent(g\_provider, eventInfo, callback);
    }
    // ...
    
    int32\_t AccessibilityManager::ExecuteAccessibilityAction(const char\* instanceId, int64\_t elementId,
        ArkUI\_Accessibility\_ActionType action, ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)
    {
        // The third-party framework needs to implement the logic for executing the accessibility node behavior.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "ExecuteAccessibilityAction instanceId %{public}s elementId: %{public}ld, "
                     "action: %{public}d, requestId: %{public}d",
                     instanceId, elementId, action, requestId);
        auto object = FakeWidget::Instance().GetChild(elementId);
        // The passed accessibility node object may be null. A null check is required.
        if (!object) {
            return 0;
        }
        // Obtain the accessibility node element.
        auto announcedText = object->GetAnnouncedForAccessibility();
        auto element = OH\_ArkUI\_CreateAccessibilityElementInfo();
        OH\_ArkUI\_AccessibilityElementInfoSetElementId(element, elementId);
        const char \*actionKey = "some\_key";
        char \*actionValue = nullptr;
        OH\_ArkUI\_FindAccessibilityActionArgumentByKey(actionArguments, actionKey, &actionValue);
        // Execute the corresponding behavior based on the action type.
        switch (action) {
            case ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLICK:
                if (object) {
                    object->OnClick();
                    object->fillAccessibilityElement(element);
                }
                // Send the specified event to the accessibility service.
                AccessibilityManager::SendAccessibilityAsyncEvent(element,
                    ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_CLICKED, announcedText);
                break;
            case ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_GAIN\_ACCESSIBILITY\_FOCUS:
                if (object) {
                    object->SetFocus(true);
    
                    object->fillAccessibilityElement(element);
                }
                // Send the specified event to the accessibility service.
                AccessibilityManager::SendAccessibilityAsyncEvent(element,
                    ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUSED,
                    announcedText);
                break;
            case ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLEAR\_ACCESSIBILITY\_FOCUS:
                if (object) {
                    object->SetFocus(false);
                    object->fillAccessibilityElement(element);
                }
                AccessibilityManager::SendAccessibilityAsyncEvent(
                    element, ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUS\_CLEARED,
                    announcedText);
                break;
            default:
                // Handle unsupported action types.
                break;
        }
        OH\_ArkUI\_DestoryAccessibilityElementInfo(element);
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    int32\_t AccessibilityManager::ClearFocusedFocusAccessibilityNode(const char\* instanceId)
    {
        // Third-party frameworks need to implement the logic for clearing the currently focused node.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "ClearFocusedFocusAccessibilityNode, instanceId %{public}s", instanceId);
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
    int32\_t AccessibilityManager::GetAccessibilityNodeCursorPosition(const char\* instanceId, int64\_t elementId,
        int32\_t requestId, int32\_t \*index)
    {
        // Third-party frameworks need to implement the logic for obtaining the cursor position within the current text component.
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, LOG\_PRINT\_TEXT,
                     "GetAccessibilityNodeCursorPosition, instanceId %{public}s "
                     "elementId: %{public}ld, requestId: %{public}d, index: %{public}d",
                     instanceId, elementId, requestId, index);
        return OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS;
    }
    
4.  After the provider is successfully connected using the [OH\_ArkUI\_AccessibilityProviderRegisterCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallback) or [OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-accessibility-h#oh_arkui_accessibilityproviderregistercallbackwithinstance) callback, the accessibility function can be enabled.
