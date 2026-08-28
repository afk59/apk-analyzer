# Implementing a Waterfall Flow Layout

The ArkUI framework provides a waterfall flow container component through NDK APIs. This component arranges items of different sizes in a waterfall-like manner from top to bottom.

#### Integrating with ArkTS Pages

To use the NDK APIs for building UIs, follow the instructions in [Integrating with ArkTS Pages](../../integrating-with-arkts-pages/document.md). This involves creating a placeholder component on the ArkTS page for mounting the native page and implementing the **NativeNode** module APIs on the ArkTS side.

#### Implementing Lazy Loading

## NodeAdapter Overview

The NDK provides the **NodeAdapter** object as an alternative to the **LazyForEach** functionality in ArkTS for on-demand generation of child components. For details, see [NodeAdapter Overview](../implementing-a-list-layout/document.md#nodeadapter-overview).

## Lazy Loading Adapter Implementation

Use the **FlowItemAdapter** class to manage the lazy loading adapter. Create a **NodeAdapter** object in the class constructor with event listeners, and destroy it in the class destructor.

// FlowItemAdapter.h
// Lazy loading implementation

#ifndef MYAPPLICATION\_FLOWITEMADAPTER\_H
#define MYAPPLICATION\_FLOWITEMADAPTER\_H

#include <arkui/native\_node.h>
#include <stack>
#include <string>
#include <unordered\_set>
#include <arkui/native\_interface.h>

namespace NativeModule {
const int NUM = 100;
class FlowItemAdapter {
public:
    FlowItemAdapter()
    {
        // Initialize the function pointer structure.
        OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, nodeApi\_);
        // Create a NodeAdapter object.
        adapter\_ = OH\_ArkUI\_NodeAdapter\_Create();
        
        // Initialize lazy loading data.
        for (int32\_t i = 0; i < NUM; i++) {
            data\_.emplace\_back(std::to\_string(i));
        }
        // Set the total number of items for lazy loading.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(adapter\_, data\_.size());
        // Set the event listener.
        OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver(adapter\_, this, OnStaticAdapterEvent);
    }

    ~FlowItemAdapter()
    {
        // Release created components.
        while (!cachedItems\_.empty()) {
            cachedItems\_.pop();
        }
        // Release adapter resources.
        OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver(adapter\_);
        OH\_ArkUI\_NodeAdapter\_Dispose(adapter\_);
    }

    ArkUI\_NodeAdapterHandle GetAdapter() const { return adapter\_; }

    void RemoveItem(int32\_t index)
    {
        // Remove the item at the specified index.
        data\_.erase(data\_.begin() + index);
        // If the index change affects the visibility of items in the visible area, the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event will be triggered to remove the element.
        // If items are added, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID and NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER events will be triggered accordingly.
        OH\_ArkUI\_NodeAdapter\_RemoveItem(adapter\_, index, 1);
        // Update the total count.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(adapter\_, data\_.size());
    }

    void InsertItem(int32\_t index, const std::string &value)
    {
        data\_.insert(data\_.begin() + index, value);
        // If the index change affects the visibility of elements in the visible area, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID and NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER events will be triggered.
        // If items are removed, the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event will be triggered accordingly.
        OH\_ArkUI\_NodeAdapter\_InsertItem(adapter\_, index, 1);
        // Update the total count.
        OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(adapter\_, data\_.size());
    }

    void MoveItem(int32\_t oldIndex, int32\_t newIndex)
    {
        auto temp = data\_\[oldIndex\];
        data\_.insert(data\_.begin() + newIndex, temp);
        data\_.erase(data\_.begin() + oldIndex);
        // If the move changes the visibility of items within the visible area, the corresponding events will be triggered.
        OH\_ArkUI\_NodeAdapter\_MoveItem(adapter\_, oldIndex, newIndex);
    }

    void ReloadItem(int32\_t index, const std::string &value)
    {
        data\_\[index\] = value;
        // If the index is within the visible area, first trigger the NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER event to remove the old item,
        // then trigger the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID and NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER events.
        OH\_ArkUI\_NodeAdapter\_ReloadItem(adapter\_, index, 1);
    }

    void ReloadAllItem()
    {
        std::reverse(data\_.begin(), data\_.end());
        // In the scenario where all items are reloaded, the NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID event will be triggered to obtain new component IDs,
        // compare the new component IDs, and reuse those whose IDs have not changed;
        // for items with new IDs, trigger the NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER event to create new components,
        // then identify any unused IDs from the old data and call NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER to remove the old items.
        OH\_ArkUI\_NodeAdapter\_ReloadAllItems(adapter\_);
    }

private:
    static void OnStaticAdapterEvent(ArkUI\_NodeAdapterEvent \*event)
    {
        // Obtain the instance object and invoke the instance event callback.
        auto itemAdapter = reinterpret\_cast<FlowItemAdapter \*>(OH\_ArkUI\_NodeAdapterEvent\_GetUserData(event));
        itemAdapter->OnAdapterEvent(event);
    }

    void OnAdapterEvent(ArkUI\_NodeAdapterEvent \*event)
    {
        auto type = OH\_ArkUI\_NodeAdapterEvent\_GetType(event);
        switch (type) {
            case NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID:
                OnGetChildId(event);
                break;
            case NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER:
                OnCreateNewChild(event);
                break;
            case NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER:
                OnDisposeChild(event);
                break;
            default:
                break;
        }
    }
    
    void OnGetChildId(ArkUI\_NodeAdapterEvent \*event)
    {
        auto index = OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(event);
        // Set the unique identifier for the generated component.
        auto hash = std::hash<std::string>();
        OH\_ArkUI\_NodeAdapterEvent\_SetNodeId(event, hash(data\_\[index\]));
    }
    
    void OnCreateNewChild(ArkUI\_NodeAdapterEvent \*event)
    {
        auto index = OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(event);
        ArkUI\_NodeHandle flowItem = nullptr;
        if (!cachedItems\_.empty()) {
            // Reuse cached items.
            flowItem = cachedItems\_.top();
            cachedItems\_.pop();
            // Update data.
            auto \*text = nodeApi\_->getFirstChild(flowItem);
            ArkUI\_AttributeItem item{nullptr, 0, data\_\[index\].c\_str()};
            nodeApi\_->setAttribute(text, NODE\_TEXT\_CONTENT, &item);
        } else {
            // Create an item.
            auto \*text = nodeApi\_->createNode(ARKUI\_NODE\_TEXT);
            ArkUI\_AttributeItem item{nullptr, 0, data\_\[index\].c\_str()};
            nodeApi\_->setAttribute(text, NODE\_TEXT\_CONTENT, &item);
            flowItem = nodeApi\_->createNode(ARKUI\_NODE\_FLOW\_ITEM);
            ArkUI\_NumberValue value\[\] = {100};
            ArkUI\_AttributeItem height{value, 1};
            nodeApi\_->setAttribute(flowItem, NODE\_HEIGHT, &height);
            value\[0\] = {1};
            ArkUI\_AttributeItem width{value, 1};
            nodeApi\_->setAttribute(flowItem, NODE\_WIDTH\_PERCENT, &width);
            value\[0\] = {.u32 = 0xFFD3D3D3};
            ArkUI\_AttributeItem backgroundColor{value, 1};

            nodeApi\_->setAttribute(flowItem, NODE\_BACKGROUND\_COLOR, &backgroundColor);
            nodeApi\_->addChild(flowItem, text);
        }
        OH\_ArkUI\_NodeAdapterEvent\_SetItem(event, flowItem);
    }
    
    void OnDisposeChild(ArkUI\_NodeAdapterEvent \*event)
    {
        auto \*node = OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode(event);
        // Cache the node.
        cachedItems\_.emplace(node);
    }

    std::vector<std::string> data\_;
    ArkUI\_NativeNodeAPI\_1 \*nodeApi\_ = nullptr;
    ArkUI\_NodeAdapterHandle adapter\_ = nullptr;

    // Manage the component reuse pool.
    std::stack<ArkUI\_NodeHandle> cachedItems\_;
};

} // namespace NativeModule

#endif //MYAPPLICATION\_FLOWITEMADAPTER\_H

#### Creating a Section

Implement the **WaterflowSection** class to manage grouping within WaterFlow components, where **SectionOption** describes the configuration parameters for each section. In the class constructor, create an **ArkUI\_WaterFlowSectionOption** object, which is destroyed in the destructor.

//WaterflowSection.h

#ifndef MYAPPLICATION\_WATERFLOWSECTION\_H
#define MYAPPLICATION\_WATERFLOWSECTION\_H

#include <arkui/native\_node.h>
#include <hilog/log.h>

namespace NativeModule {

struct SectionOption {
    int32\_t itemsCount = 0;
    int32\_t crossCount;
    float columnsGap;
    float rowsGap;
    // {Top margin, right margin, bottom margin, left margin}
    ArkUI\_Margin margin{0, 0, 0, 0};
    float (\*onGetItemMainSizeByIndex)(int32\_t itemIndex);
    void \*userData;
};

class WaterflowSection {
public:
    WaterflowSection() : sectionOptions\_(OH\_ArkUI\_WaterFlowSectionOption\_Create()){};
    
    ~WaterflowSection()
    {
        OH\_ArkUI\_WaterFlowSectionOption\_Dispose(sectionOptions\_);
    }

    void SetSection(ArkUI\_WaterFlowSectionOption \*sectionOptions, int32\_t index, SectionOption section)
    {
        OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount(sectionOptions, index, section.itemsCount);
        OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount(sectionOptions, index, section.crossCount);
        OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap(sectionOptions, index, section.columnsGap);
        OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap(sectionOptions, index, section.rowsGap);
        OH\_ArkUI\_WaterFlowSectionOption\_SetMargin(sectionOptions, index, section.margin.top, section.margin.right,
                                                  section.margin.bottom, section.margin.left);
        OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex(sectionOptions, index,
                                                                               section.onGetItemMainSizeByIndex);
    }
    
    ArkUI\_WaterFlowSectionOption \*GetSectionOptions() const
    {
        return sectionOptions\_;
    }
    
    void PrintSectionOptions()
    {
        int32\_t sectionCnt = OH\_ArkUI\_WaterFlowSectionOption\_GetSize(sectionOptions\_);
        for (int32\_t i = 0; i < sectionCnt; i++) {
            ArkUI\_Margin margin = OH\_ArkUI\_WaterFlowSectionOption\_GetMargin(sectionOptions\_, i);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "CreateWaterflowExample",
                         "Section\[%{public}d\].margin:{%{public}f, %{public}f, %{public}f, %{public}f}", i, margin.top,
                         margin.right, margin.bottom, margin.left);
        }
    }

private:
    ArkUI\_WaterFlowSectionOption \*sectionOptions\_ = nullptr;
};
} // namespace NativeModule

#endif // MYAPPLICATION\_WATERFLOWSECTION\_H

#### Creating a WaterFlow Component

Implement the **ArkUIWaterflowNode** class to manage **WaterFlow** components. This class supports configuration through **SetLazyAdapter** for assigning a **FlowItemAdapter** and **SetSection** for defining sections.

// waterflow.h
#ifndef MYAPPLICATION\_WATERFLOW\_H
#define MYAPPLICATION\_WATERFLOW\_H
  
#include "FlowItemAdapter.h"
#include "WaterflowSection.h"
#include "ArkUINode.h"
  
namespace NativeModule {
  
class ArkUIWaterflowNode : public ArkUINode {
public:
    ArkUIWaterflowNode()
        : ArkUINode(CreateWaterflowNode()) {}
  
    ~ArkUIWaterflowNode() override
    {
        // First unregister the adapter.
        if (adapter\_ && nativeModule\_) {
            nativeModule\_->resetAttribute(handle\_, NODE\_WATER\_FLOW\_NODE\_ADAPTER);
            adapter\_.reset();
        }
        // Destroy sections.
        section\_.reset();
        // The base class automatically handles handle\_ disposal.
    }

    void SetLazyAdapter(const std::shared\_ptr<FlowItemAdapter> &adapter)
    {
        ArkUI\_AttributeItem item{nullptr, 0, nullptr, adapter->GetAdapter()};
        nativeModule\_->setAttribute(handle\_, NODE\_WATER\_FLOW\_NODE\_ADAPTER, &item);
        adapter\_ = adapter;
    }
  
    void SetSection(const std::shared\_ptr<WaterflowSection> &section)
    {
        if (!section->GetSectionOptions()) {
            return;
        }
        ArkUI\_NumberValue start\[\] = {{.i32 = 0}};
        ArkUI\_AttributeItem optionsItem = {start, 1, nullptr, section->GetSectionOptions()};
        nativeModule\_->setAttribute(handle\_, NODE\_WATER\_FLOW\_SECTION\_OPTION, &optionsItem);
        section\_ = section;
    }
  
    std::shared\_ptr<WaterflowSection> GetWaterflowSection() { return section\_; }
  
private:
    static ArkUI\_NodeHandle CreateWaterflowNode()
    {
        ArkUI\_NativeNodeAPI\_1\* api = nullptr;
        OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_NODE, ArkUI\_NativeNodeAPI\_1, api);
        if (!api) {
            return nullptr;
        }
        return api->createNode(ARKUI\_NODE\_WATER\_FLOW);
    }
  
    std::shared\_ptr<WaterflowSection> section\_ = nullptr;
    std::shared\_ptr<FlowItemAdapter> adapter\_;
};
  
} // namespace NativeModule
  
#endif // MYAPPLICATION\_WATERFLOW\_H

#### Implementing a WaterFlow Component

Create an instance of the **ArkUIWaterflowNode** class, set its width and height, and bind the **NodeAdapter** and sections.

// CreateWaterflowExample.h

#ifndef MYAPPLICATION\_CREATEWATERFLOWEXAMPLE\_H
#define MYAPPLICATION\_CREATEWATERFLOWEXAMPLE\_H
#include "waterflow.h"

namespace NativeModule {
const int UI\_WIDTH = 400;
const int UI\_HEIGHT = 600;
const int SECTION\_COUNT = 10;
const int SECTION\_2\_ID = 2;

inline void SetupSections(std::shared\_ptr<WaterflowSection> sections)
{
    SectionOption MARGIN\_GAP\_SECTION\_1 = {10, 2, 10, 10, {20, 30, 40, 50}, nullptr, nullptr};
    SectionOption MARGIN\_GAP\_SECTION\_2 = {10, 4, 10, 10, {20, 30, 40, 50}, nullptr, nullptr};
    for (int i = 0; i < SECTION\_COUNT; i++) {
        sections->SetSection(sections->GetSectionOptions(), i,
                             i % SECTION\_2\_ID ? MARGIN\_GAP\_SECTION\_1 : MARGIN\_GAP\_SECTION\_2);
    }
}

inline std::shared\_ptr<ArkUIWaterflowNode> CreateWaterflowExample(napi\_env env)
{
    auto waterflow = std::make\_shared<ArkUIWaterflowNode>();
    waterflow->SetHeight(UI\_HEIGHT);
    waterflow->SetWidth(UI\_WIDTH);
    waterflow->SetLazyAdapter(std::make\_shared<FlowItemAdapter>());
    auto sections = std::make\_shared<WaterflowSection>();
    SetupSections(sections);
    waterflow->SetSection(sections);
    return waterflow;
}
} // namespace NativeModule

#endif // MYAPPLICATION\_CREATEWATERFLOWEXAMPLE\_H

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fmUEzM6eRS6T7yqxtsKX1g/en-us_image_0000002568764613.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FA672618B64A0B515D441D33E404A22A9B07A9508E46906102F49EAA4DC68ED)
