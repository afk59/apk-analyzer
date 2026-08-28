# Implementing a List Layout

The ArkUI development framework provides list components through NDK APIs, enabling efficient display of structured, scrollable content. List components allow you to control the scroll position, group display content, and use [NodeAdapter](#nodeadapter-overview) for lazy loading to improve list creation performance.

#### Creating a List

For details about how to create a list, see [Integrating with ArkTS Pages](../../integrating-with-arkts-pages/document.md).

#### Listening for Scroll Events

For details, see [Listening for Component Events](../../adding-interaction-events/listening-for-component-events/document.md).

#### Implementing Lazy Loading

## NodeAdapter Overview

The NDK provides the **NodeAdapter** object as an alternative to [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-rendering-control-lazyforeach) in ArkTS for on-demand generation of child components. NodeAdapter works with [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list)/[ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup), [Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow), and [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper) components.

-   Child components cannot be added to a node where **NodeAdapter** is set by using APIs such as [addChild](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#addchild). Child components are managed entirely by **NodeAdapter**. If a parent component already has child nodes, setting **NodeAdapter** will fail and return an error code.
    
-   **NodeAdapter** notifies you of on-demand generation of components through relevant events. Similar to the component event mechanism, you need to register an [event listener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeadapter_registereventreceiver) when using **NodeAdapter** and handle logic in the listener events. Relevant events are defined by [ArkUI\_NodeAdapterEventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeadaptereventtype). **NodeAdapter** does not actively release off-screen component objects; you must release or cache and reuse component objects in the [NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeadaptereventtype) event. The following image illustrates the event triggering mechanism in a typical list scrolling scenario.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/79k0bkd3QMuYQCxXi3ZlMg/en-us_image_0000002568684603.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CB80FABC2E84CA3B22049B2086972FEF1867730E7B0A5FB86C19879D8D16CD3)
    

This example demonstrates how to implement an adapter for lazy loading.

## Implementing a Lazy Loading Adapter

Use the **ArkUIListItemAdapter** class to manage the lazy loading adapter. Create a **NodeAdapter** object in the class constructor and set an event listener for the **NodeAdapter** object. In the class destructor, destroy the **NodeAdapter** object.

// ArkUIListItemAdapter.h
// Code for lazy loading functionality in a text list.

#ifndef MYAPPLICATION\_ARKUILISTITEMADAPTER\_H
#define MYAPPLICATION\_ARKUILISTITEMADAPTER\_H

#include <arkui/native\_node.h>
#include <stack>
#include <string>
#include <unordered\_set>

#include "ArkUIListItemNode.h"
#include "ArkUITextNode.h"
#include "NativeModule.h"
#include <hilog/log.h>

namespace NativeModule {
const int32\_t NUMBER\_1000 = 1000;
const int32\_t NUMBER\_100 = 100;
const int32\_t NUMBER\_16 = 16;
class ArkUIListItemAdapter {
public:
    ArkUIListItemAdapter()
        : module\_(NativeModuleInstance::GetInstance()->GetNativeNodeAPI()),
          handle\_(OH\_ArkUI\_NodeAdapter\_Create())
    { // Use the NodeAdapter creation function.
        // Initialize lazy loading data.
        for (int32\_t i = 0; i < NUMBER\_1000; i++) {
            data\_.emplace\_back(std::to\_string(i));
        }
        // Set lazy loading data.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(handle\_, data\_.size());
        // Register the event receiver for lazy loading.
        OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver(handle\_, this, OnStaticAdapterEvent);
    }

    ~ArkUIListItemAdapter()
    {
        // Release created components.
        while (!cachedItems\_.empty()) {
            cachedItems\_.pop();
        }
        items\_.clear();
        // Release adapter resources.
        OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver(handle\_);
        OH\_ArkUI\_NodeAdapter\_Dispose(handle\_);
    }

    ArkUI\_NodeAdapterHandle GetHandle() const { return handle\_; }
    void RemoveItem(size\_t  index)
    {
        // Remove the item at the specified index.
        data\_.erase(data\_.begin() + index);
        // If the index change affects the visibility of items in the visible area, the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event will be triggered to remove the element.
        // Depending on whether there are new elements, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID or NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER event will be triggered.
        OH\_ArkUI\_NodeAdapter\_RemoveItem(handle\_, index, 1);
        // Update the total count.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(handle\_, data\_.size());
    }
    void InsertItem(int32\_t index, const std::string &value)
    {
        data\_.insert(data\_.begin() + index, value);
        // If the index change affects the visibility of elements in the visible area, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID and NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER events will be triggered.
        // If items are removed, the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event will be triggered accordingly.
        OH\_ArkUI\_NodeAdapter\_InsertItem(handle\_, index, 1);
        // Update the total count.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(handle\_, data\_.size());
    }

    void MoveItem(int32\_t oldIndex, int32\_t newIndex)
    {
        auto temp = data\_\[oldIndex\];
        data\_.insert(data\_.begin() + newIndex, temp);
        data\_.erase(data\_.begin() + oldIndex);
        // If the move changes the visibility of items within the visible area, the corresponding events will be triggered. Otherwise, no event is triggered.
        OH\_ArkUI\_NodeAdapter\_MoveItem(handle\_, oldIndex, newIndex);
    }

    void ReloadItem(int32\_t index, const std::string &value)
    {
        data\_\[index\] = value;
        // If the index is within the visible area, first trigger the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event to remove the old item,
        // then trigger the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID and NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER events.
        OH\_ArkUI\_NodeAdapter\_ReloadItem(handle\_, index, 1);
    }

    void ReloadAllItem()
    {
        std::reverse(data\_.begin(), data\_.end());
        // In the scenario where all items are reloaded, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID event will be triggered to obtain new component IDs,
        // compare the new component IDs, and reuse those whose IDs have not changed,
        // for items with new IDs, trigger the NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER event to create new components,
        // then identify any unused IDs from the old data and call NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER to remove the old items.
        OH\_ArkUI\_NodeAdapter\_ReloadAllItems(handle\_);
    }

private:
    static void OnStaticAdapterEvent(ArkUI\_NodeAdapterEvent \*event)
    {
        // Obtain the instance object and invoke the instance event callback.
        auto itemAdapter = reinterpret\_cast<ArkUIListItemAdapter \*>(OH\_ArkUI\_NodeAdapterEvent\_GetUserData(event));
        itemAdapter->OnAdapterEvent(event);
    }

    void OnAdapterEvent(ArkUI\_NodeAdapterEvent \*event)
    {
        // Obtain the event type.
        auto type = OH\_ArkUI\_NodeAdapterEvent\_GetType(event);
        switch (type) {
            // Obtain the unique ID of the new element to add.
            case NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID:
                OnNewItemIdCreated(event);
                break;
            // Obtain the content of the new element to add.
            case NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER:
                OnNewItemAttached(event);
                break;
            // Remove elements from the adapter.
            case NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER:
                OnItemDetached(event);
                break;
            default:
                break;
            }
    }

    // Assign IDs to items that need to be displayed, used for element diffing in ReloadAllItems scenarios.
    void OnNewItemIdCreated(ArkUI\_NodeAdapterEvent \*event)
    {
        auto index = OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(event);
        static std::hash<std::string> hashId = std::hash<std::string>();
        auto id = hashId(data\_\[index\]);
        OH\_ArkUI\_NodeAdapterEvent\_SetNodeId(event, id);
    }
    // Handle the display of new items in the visible area.
    void OnNewItemAttached(ArkUI\_NodeAdapterEvent \*event)
    {
        auto index = OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(event);
        ArkUI\_NodeHandle handle = nullptr;
        if (!cachedItems\_.empty()) {
            // Use and update the recycled item from the cache.
            auto recycledItem = cachedItems\_.top();
            auto textItem = std::dynamic\_pointer\_cast<ArkUITextNode>(recycledItem->GetChildren().back());
            textItem->SetTextContent(data\_\[index\]);
            handle = recycledItem->GetHandle();
            // ...
            // Release the reference in the cache pool.
            cachedItems\_.pop();
        } else {
            // Create an element.
            auto listItem = std::make\_shared<ArkUIListItemNode>();
            auto textNode = std::make\_shared<ArkUITextNode>();
            textNode->SetTextContent(data\_\[index\]);
            textNode->SetFontSize(NUMBER\_16);
            textNode->SetPercentWidth(1);
            textNode->SetHeight(NUMBER\_100);
            textNode->SetBackgroundColor(0xFFfffacd);
            textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            listItem->AddChild(textNode);
            // Create the swipe action item for the ListItem.
            auto swipeNode = std::make\_shared<ArkUITextNode>();
            // ...
            swipeNode->RegisterOnClick(\[this, data = data\_\[index\]\](ArkUI\_NodeEvent \*event) {
                auto it = std::find(data\_.begin(), data\_.end(), data);
                if (it != data\_.end()) {
                    auto index = std::distance(data\_.begin(), it);
                    RemoveItem(index);
                }
            });
            listItem->SetSwiperAction(swipeNode);
            handle = listItem->GetHandle();
            // Maintain a reference to the text list item.
            items\_.emplace(handle, listItem);
        }
        // Set the element to be displayed.
        OH\_ArkUI\_NodeAdapterEvent\_SetItem(event, handle);
    }
    // Remove an item from the visible area.
    void OnItemDetached(ArkUI\_NodeAdapterEvent \*event)
    {
        auto item = OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode(event);
        // Place the item in the cache pool for recycling and reuse.
        cachedItems\_.emplace(items\_\[item\]);
    }
    
    std::vector<std::string> data\_;
    ArkUI\_NativeNodeAPI\_1 \*module\_ = nullptr;
    ArkUI\_NodeAdapterHandle handle\_ = nullptr;

    // Manage items generated by the NodeAdapter.
    std::unordered\_map<ArkUI\_NodeHandle, std::shared\_ptr<ArkUIListItemNode>> items\_;

    // Manage the component reuse pool.
    std::stack<std::shared\_ptr<ArkUIListItemNode>> cachedItems\_;
};
} // namespace NativeModule

#endif // MYAPPLICATION\_ARKUILISTITEMADAPTER\_H

## Applying the Lazy Loading Adapter in a List

1.  Add the **SetLazyAdapter** function to **ArkUIListNode**, set the [NODE\_LIST\_NODE\_ADAPTER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) property for the list node, and pass **NodeAdapter** as the input parameter.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    #ifndef MYAPPLICATION\_ARKUILISTNODE\_H
    #define MYAPPLICATION\_ARKUILISTNODE\_H
    
    #include "ArkUINode.h"
    #include "ArkUIListItemAdapter.h"
    namespace NativeModule {
    class ArkUIListNode : public ArkUINode {
    public:
        ArkUIListNode() // Create an ArkUI list component instance.
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST)) {}
    
        ~ArkUIListNode() override
        {
            if (nativeModule\_) {
                nativeModule\_->unregisterNodeEvent(handle\_, NODE\_LIST\_ON\_SCROLL\_INDEX);
            }
            if (adapter\_) {
                // Unload the UI components under the adapter during destruction.
                nativeModule\_->resetAttribute(handle\_, NODE\_LIST\_NODE\_ADAPTER);
                adapter\_.reset();
            }
        }
        // List component's API encapsulation for attributes.
        void SetScrollBarState(bool isShow)
        {
            ArkUI\_ScrollBarDisplayMode displayMode =
                isShow ? ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON : ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF;
            ArkUI\_NumberValue value\[\] = {{.i32 = displayMode}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_BAR\_DISPLAY\_MODE, &item);
        }
    
        void RegisterOnScrollIndex(const std::function<void(int32\_t index)> &onScrollIndex)
        {
            onScrollIndex\_ = onScrollIndex;
            nativeModule\_->registerNodeEvent(handle\_, NODE\_LIST\_ON\_SCROLL\_INDEX, 0, nullptr);
        }
        // Import the lazy loading module.
        void SetLazyAdapter(const std::shared\_ptr<ArkUIListItemAdapter> &adapter)
        {
            ArkUI\_AttributeItem item{nullptr, 0, nullptr, adapter->GetHandle()};
            nativeModule\_->setAttribute(handle\_, NODE\_LIST\_NODE\_ADAPTER, &item);
            adapter\_ = adapter;
        }
        // ...
    protected:
        void OnNodeEvent(ArkUI\_NodeEvent \*event) override
        {
            auto eventType = OH\_ArkUI\_NodeEvent\_GetEventType(event);
            switch (eventType) {
                case NODE\_LIST\_ON\_SCROLL\_INDEX: {
                    auto index = OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(event)->data\[0\];
                    if (onScrollIndex\_) {
                        onScrollIndex\_(index.i32);
                    }
                    break;
                }
                default: {
                    break;
                }
            }
        }
    
    private:
        std::function<void(int32\_t index)> onScrollIndex\_;
    
        std::shared\_ptr<ArkUIListItemAdapter> adapter\_;
    };
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_ARKUILISTNODE\_H
    
2.  Create example code for a **List** using lazy loading and call the **SetLazyAdapter** API of the **List** node to set the lazy loading adapter.
    
    // LazyTextListExample
    // Example code for a lazy loading text list.
    
    #ifndef MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
    #define MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
    
    #include "ArkUIBaseNode.h"
    #include "ArkUIListNode.h"
    
    namespace NativeModule {
    
    std::shared\_ptr<ArkUIBaseNode> CreateLazyTextListExample()
    {
        // Create and mount the component to the parent node.
        // 1: Create a List component.
        auto list = std::make\_shared<ArkUIListNode>();
        list->SetPercentWidth(1);
        list->SetPercentHeight(1);
        // 2: Create a ListItem child component for lazy loading and mount it to the List component.
        auto adapter = std::make\_shared<ArkUIListItemAdapter>();
        list->SetLazyAdapter(adapter);
        return list;
    }
    } // namespace NativeModule
    
    #endif // MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
    
3.  Call the **List** lazy loading example code in **NativeEntry.cpp**.
    
    // NDK API entry mounting file.
    
    #include "NativeEntry.h"
    
    #include "LazyTextListExample.h"
    
    #include <arkui/native\_node\_napi.h>
    #include <arkui/native\_type.h>
    #include <js\_native\_api.h>
    #include <uv.h>
    
    namespace NativeModule {
    
    // ···
    
    napi\_value CreateNativeRoot(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        // Obtain the NodeContent object.
        ArkUI\_NodeContentHandle contentHandle;
        OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
        NativeEntry::GetInstance()->SetContentHandle(contentHandle);
    
        // Create a lazy loading text list.
        auto node = CreateLazyTextListExample();
    
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
    
    } // namespace NativeModule
    

#### Controlling the List Scroll Position

1.  Control the list to scroll to a specified offset position.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    // ...
    class ArkUIListNode : public ArkUINode {
    public:
        // ...
        void ScrollTo(float offset)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = 0}, {.f32 = offset}, {.f32 = 0}};
            ArkUI\_AttributeItem Item = {.value = value, .size = 3};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_OFFSET, &Item);
        }
        // ...
    };
    
2.  Control the list to scroll to a specified element.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    // ...
    class ArkUIListNode : public ArkUINode {
    public:
        // ...
        void ScrollToIndex(int32\_t index)
        {
            ArkUI\_NumberValue value\[\] = {{.i32 = index}};
            ArkUI\_AttributeItem Item = {.value = value, .size = 1};
            nativeModule\_->setAttribute(handle\_, NODE\_LIST\_SCROLL\_TO\_INDEX, &Item);
        }
        // ...
    };
    
3.  Control the list to scroll by a specified offset.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    // ...
    class ArkUIListNode : public ArkUINode {
    public:
        // ...
        void ScrollBy(float offset)
        {
            ArkUI\_NumberValue value\[\] = {{.f32 = 0}, {.f32 = offset}};
            ArkUI\_AttributeItem Item = {.value = value, .size = 2};
            nativeModule\_->setAttribute(handle\_, NODE\_SCROLL\_BY, &Item);
        }
        // ...
    };
    

#### Implementing Swipe-to-Delete for List Items

1.  Set the [NODE\_LIST\_ITEM\_SWIPE\_ACTION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) attribute of [ListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem) and pass the [ArkUI\_ListItemSwipeActionOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype) object as the attribute parameter.
    
    // ArkUIListItemNode.h
    // Provide an encapsulation class for list items
    #ifndef MYAPPLICATION\_ARKUILISTITEMNODE\_H
    #define MYAPPLICATION\_ARKUILISTITEMNODE\_H
    #include "ArkUINode.h"
    namespace NativeModule {
    class ArkUIListItemNode : public ArkUINode {
    public:
        ArkUIListItemNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI\_NODE\_LIST\_ITEM)) {}
        ~ArkUIListItemNode() override
        {
            // Dispose of a ListItemSwipeActionOption instance.
            if (swipeAction\_) {
                OH\_ArkUI\_ListItemSwipeActionOption\_Dispose(swipeAction\_);
            }
            // Dispose of a ListItemSwipeActionItem instance.
            if (swipeItem\_) {
                OH\_ArkUI\_ListItemSwipeActionItem\_Dispose(swipeItem\_);
            }
        }
        void SetSwiperAction(std::shared\_ptr<ArkUINode> node)
        {
            swipeContent\_ = node;
            // Create a ListItemSwipeActionItem instance.
            swipeItem\_ = OH\_ArkUI\_ListItemSwipeActionItem\_Create();
            // Set the layout content for the ListItemSwipeActionItem instance.
            OH\_ArkUI\_ListItemSwipeActionItem\_SetContent(swipeItem\_, node->GetHandle());
            // Create a ListItemSwipeActionOption instance.
            swipeAction\_ = OH\_ArkUI\_ListItemSwipeActionOption\_Create();
            // Set the layout content for the right edge (for a vertical layout) or bottom edge (for a horizontal layout) of the ListItemSwipeActionItem instance.
            OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd(swipeAction\_, swipeItem\_);
            ArkUI\_AttributeItem Item = {.object = swipeAction\_};
            nativeModule\_->setAttribute(handle\_, NODE\_LIST\_ITEM\_SWIPE\_ACTION, &Item);
        }
        std::shared\_ptr<ArkUINode> GetSwipeContent() const { return swipeContent\_; }
    
    private:
        ArkUI\_ListItemSwipeActionOption \*swipeAction\_ = nullptr;
        ArkUI\_ListItemSwipeActionItem \*swipeItem\_ = nullptr;
        std::shared\_ptr<ArkUINode> swipeContent\_ = nullptr;
    };
    } // namespace NativeModule
    #endif // MYAPPLICATION\_ARKUILISTITEMNODE\_H
    
2.  When creating a [ListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem), create the swipe action item for it and bind the click event. In the click event, delete the data source. When reusing a **ListItem**, update the binding event of the swipe action item.
    
    // ArkUIListItemAdapter.h
    // ...
    class ArkUIListItemAdapter {
        // ...
        // Handle the display of new items in the visible area.
        void OnNewItemAttached(ArkUI\_NodeAdapterEvent \*event)
        {
            auto index = OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(event);
            ArkUI\_NodeHandle handle = nullptr;
            if (!cachedItems\_.empty()) {
                // Use and update the recycled item from the cache.
                auto recycledItem = cachedItems\_.top();
                auto textItem = std::dynamic\_pointer\_cast<ArkUITextNode>(recycledItem->GetChildren().back());
                textItem->SetTextContent(data\_\[index\]);
                handle = recycledItem->GetHandle();
                auto swipeContent = recycledItem->GetSwipeContent();
                swipeContent->RegisterOnClick(\[this, data = data\_\[index\]\](ArkUI\_NodeEvent \*event) {
                    auto it = std::find(data\_.begin(), data\_.end(), data);
                    if (it != data\_.end()) {
                        auto index = std::distance(data\_.begin(), it);
                        RemoveItem(index);
                    }
                });
                // Release the reference in the cache pool.
                cachedItems\_.pop();
            } else {
                // Create an element.
                auto listItem = std::make\_shared<ArkUIListItemNode>();
                auto textNode = std::make\_shared<ArkUITextNode>();
                textNode->SetTextContent(data\_\[index\]);
                textNode->SetFontSize(NUMBER\_16);
                textNode->SetPercentWidth(1);
                textNode->SetHeight(NUMBER\_100);
                textNode->SetBackgroundColor(0xFFfffacd);
                textNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
                listItem->AddChild(textNode);
                // Create the swipe action item for the ListItem.
                auto swipeNode = std::make\_shared<ArkUITextNode>();
                swipeNode->SetTextContent("del");
                swipeNode->SetFontSize(NUMBER\_16);
                swipeNode->SetFontColor(0xFFFFFFFF);
                swipeNode->SetWidth(NUMBER\_100);
                swipeNode->SetHeight(NUMBER\_100);
                swipeNode->SetBackgroundColor(0xFFFF0000);
                swipeNode->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
                swipeNode->RegisterOnClick(\[this, data = data\_\[index\]\](ArkUI\_NodeEvent \*event) {
                    auto it = std::find(data\_.begin(), data\_.end(), data);
                    if (it != data\_.end()) {
                        auto index = std::distance(data\_.begin(), it);
                        RemoveItem(index);
                    }
                });
                listItem->SetSwiperAction(swipeNode);
                handle = listItem->GetHandle();
                // Maintain a reference to the text list item.
                items\_.emplace(handle, listItem);
            }
            // Set the element to be displayed.
            OH\_ArkUI\_NodeAdapterEvent\_SetItem(event, handle);
        }
        // ...
    };
    
3.  Add **RemoveItem** to **ArkUIListItemAdapter** to delete data sources and call the [OH\_ArkUI\_NodeAdapter\_RemoveItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeadapter_removeitem) API to instruct the framework to refresh the UI.
    
    // ArkUIListItemAdapter.h
    // ...
    class ArkUIListItemAdapter {
        // ...
        void RemoveItem(size\_t  index)
        {
            // Remove the item at the specified index.
            data\_.erase(data\_.begin() + index);
            // If the index change affects the visibility of items in the visible area, the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event will be triggered to remove the element.
            // Depending on whether there are new elements, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID or NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER event will be triggered.
            OH\_ArkUI\_NodeAdapter\_RemoveItem(handle\_, index, 1);
            // Update the total count.
            OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(handle\_, data\_.size());
        }
        // ...
    };
    

#### Using a Grouped List

1.  The [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) component is used to implement a grouped list. **ListItemGroup** supports the functions to add the [header](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup#listitemgroupoptions) and [footer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup#listitemgroupoptions), and supports lazy loading.
    
    // ArkUIListItemGroupNode.h
    
    #ifndef MYAPPLICATION\_ARKUILISTITEMGROUPNODE\_H
    #define MYAPPLICATION\_ARKUILISTITEMGROUPNODE\_H
    #include "ArkUINode.h"
    #include "ArkUIListItemAdapter.h"
    namespace NativeModule {
    class ArkUIListItemGroupNode : public ArkUINode {
    public:
        ArkUIListItemGroupNode()
            : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())
        ->createNode(ARKUI\_NODE\_LIST\_ITEM\_GROUP)) {}
        void SetHeader(std::shared\_ptr<ArkUINode> node)
        {
            if (node) {
                // Create an attribute item, put the node handle into it, and set the header.
                ArkUI\_AttributeItem Item = { .object = node->GetHandle() };
                nativeModule\_->setAttribute(handle\_, NODE\_LIST\_ITEM\_GROUP\_SET\_HEADER, &Item);
            } else {
                // If a null pointer (nullptr) is passed, the existing header is to be removed.
                nativeModule\_->resetAttribute(handle\_, NODE\_LIST\_ITEM\_GROUP\_SET\_HEADER);
            }
        }
        void SetFooter(std::shared\_ptr<ArkUINode> node)
        {
            if (node) {
                // Create an attribute item, put the node handle into it, and set the footer.
                ArkUI\_AttributeItem Item = { .object= node->GetHandle() };
                nativeModule\_->setAttribute(handle\_, NODE\_LIST\_ITEM\_GROUP\_SET\_FOOTER, &Item);
            } else {
                // If a null pointer (nullptr) is passed, the existing footer is to be removed.
                nativeModule\_->resetAttribute(handle\_, NODE\_LIST\_ITEM\_GROUP\_SET\_FOOTER);
            }
        }
        std::shared\_ptr<ArkUINode> GetHeader() const
        {
            return header\_;
        }
        std::shared\_ptr<ArkUINode> GetFooter() const
        {
            return footer\_;
        }
        // Import the lazy loading module.
        void SetLazyAdapter(const std::shared\_ptr<ArkUIListItemAdapter> &adapter)
        {
            ArkUI\_AttributeItem item{nullptr, 0, nullptr, adapter->GetHandle()};
            nativeModule\_->setAttribute(handle\_, NODE\_LIST\_ITEM\_GROUP\_NODE\_ADAPTER, &item);
            adapter\_ = adapter;
        }
    private:
        std::shared\_ptr<ArkUINode> header\_;
        std::shared\_ptr<ArkUINode> footer\_;
        std::shared\_ptr<ArkUIListItemAdapter> adapter\_;
    };
    }
    #endif //MYAPPLICATION\_ARKUILISTITEMGROUPNODE\_H
    
2.  Set the sticky header for the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component.
    
    // ArkUIListNode.h
    // Provide encapsulation for the list component.
    // ...
    class ArkUIListNode : public ArkUINode {
        // ...
        void SetSticky(ArkUI\_StickyStyle style)
        {
            ArkUI\_NumberValue value\[\] = {{.i32 = style}};
            ArkUI\_AttributeItem item = {value, 1};
            nativeModule\_->setAttribute(handle\_, NODE\_LIST\_STICKY, &item);
        }
        // ...
    };
    
3.  Use [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) under the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component to implement the grouped list.
    
    // LazyTextListExample.h
    // Example code for a lazy loading text list.
    #ifndef MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
    #define MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
    #include "ArkUIBaseNode.h"
    #include "ArkUIListNode.h"
    #include "ArkUIListItemGroupNode.h"
    namespace NativeModule {
    const int32\_t NUMBER\_3 = 3;
    const int32\_t NUMBER\_50 = 50;
    
    std::shared\_ptr<ArkUIBaseNode> CreateLazyTextListExample()
    {
        // Create and mount the component to the parent node.
        // 1: Create a List component instance.
        auto list = std::make\_shared<ArkUIListNode>();
        list->SetPercentWidth(1);
        list->SetPercentHeight(1);
        // Set the sticky header.
        list->SetSticky(ARKUI\_STICKY\_STYLE\_BOTH);
        // 2: Create a ListItemGroup component instance and mount it to the List component.
        for (int32\_t i = 0; i < NUMBER\_3; i++) {
            auto header = std::make\_shared<ArkUITextNode>();
            header->SetTextContent("header");
            header->SetFontSize(NUMBER\_16);
            header->SetPercentWidth(1);
            header->SetHeight(NUMBER\_50);
            header->SetBackgroundColor(0xFFDCDCDC);
            header->SetTextAlign(ARKUI\_TEXT\_ALIGNMENT\_CENTER);
            auto listItemGroup = std::make\_shared<ArkUIListItemGroupNode>();
            listItemGroup->SetHeader(header);
            auto adapter = std::make\_shared<ArkUIListItemAdapter>();
            listItemGroup->SetLazyAdapter(adapter);
            list->AddChild(listItemGroup);
        }
        return list;
    }
    } // namespace NativeModule
    #endif // MYAPPLICATION\_LAZYTEXTLISTEXAMPLE\_H
