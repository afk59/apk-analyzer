# TreeView

The **TreeView** component represents a tree view used to display a hierarchical list of items. Each item can contain subitems, which may be expanded or collapsed.

This component is applicable in productivity applications, such as side navigation bars in notepad, email, and Gallery applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/IiqkBl2IRLaI6IYjGFIo1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24A80FC4F520E0B56B0640AC8EEBBBED6EC6D0D003E74889F534B79D5869EEB5)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { TreeView } from "@kit.ArkUI";

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### TreeView

TreeView({ treeController: TreeController })

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| treeController | [TreeController](#treecontroller) | Yes | Node information of the tree view. |

#### TreeController

Implements a **TreeController** object, which can be bound to a tree view component to control the node information of the component. One **TreeController** object can be bound to only one tree view component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]addNode

addNode(nodeParam?: NodeParam): TreeController

Adds a child node to the selected node.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| nodeParam | [NodeParam](#nodeparam) | No | Node information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TreeController](#treecontroller) | Controller of the **TreeView** component. |

#### \[h2\]removeNode

removeNode(): void

Removes the selected node.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]modifyNode

modifyNode(): void

Modifies the selected node.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]buildDone

buildDone(): void

Builds a tree view. After a node is added, this API must be called to save the tree information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]refreshNode

refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void

Refreshes the tree view. You can call this API to update the information about the current node.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parentId | number | Yes | 
ID of the parent node.

The value must be greater than or equal to -1.

 |
| parentSubTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Secondary text of the parent node. |
| currentSubtitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | Secondary text of the current node. |

#### NodeParam

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| parentNodeId | number | No | Yes | 
ID of the parent node.

The value must be greater than or equal to -1.

Default value: -1. The root node ID is -1. If the value is less than -1, the setting does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| currentNodeId | number | No | Yes | 

Current child node ID.

The value must be greater than or equal to -1.

The value cannot be the root node ID or null. Otherwise, an exception is thrown. In addition, duplicate **currentNodeId** values are not allowed.

Default value: **\-1**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isFolder | boolean | No | Yes | 

Whether the node is a directory.

Default value: **false**.

**true**: The node is a directory. **false**: The node is not a directory.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolIconStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon, which has higher priority than **icon**.

Default value: **undefined**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| selectedIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the selected node.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolSelectedIconStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon of the selected node., which has higher priority than **selectedIcon**.

Default value: **undefined**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| editIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Edit icon.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolEditIconStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol edit icon, which has a higher priority than **editIcon**.

Default value: **undefined**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Primary title.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Secondary title.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| container | () => void | No | Yes | 

Right-click child component bound to the node. The child component is decorated with @Builder.

Default value: **() => void**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### TreeListenerManager

Implements a **TreeListenerManager** object, which can be bound to a **TreeView** component to listen for changes of tree nodes. One **TreeListenerManager** object can be bound to only one tree view component.

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### \[h2\]getInstance

static getInstance(): TreeListenerManager

Obtains a **TreeListenerManager** singleton object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| [TreeListenerManager](#treelistenermanager) | **TreeListenerManager** singleton object. |

#### \[h2\]getTreeListener

getTreeListener(): TreeListener

Obtains a listener.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| [TreeListener](#treelistener) | Obtained listener. |

#### TreeListener

Listener of the tree view component. You can bind it to the **TreeView** component and use it to listen for changes of tree nodes. One listener can be bound to only one **TreeView** component.

#### \[h2\]on

on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;

Register a listener.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [TreeListenType](#treelistentype) | Yes | Listening type. |
| callback | (callbackParam: [CallbackParam](#callbackparam)) => void | Yes | Node information. |

#### \[h2\]once

once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;

Registers a one-off listener.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [TreeListenType](#treelistentype) | Yes | Listening type. |
| callback | (callbackParam: [CallbackParam](#callbackparam)) => void | Yes | Node information. |

#### \[h2\]off

off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void;

Unregisters a listener.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [TreeListenType](#treelistentype) | Yes | Listening type. |
| callback | (callbackParam: [CallbackParam](#callbackparam)) => void | No | Node information. |

#### TreeListenType

Enumerates the listening types of tree view nodes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| NODE\_CLICK | "NodeClick" | Listens for click events of nodes. |
| NODE\_ADD | "NodeAdd" | Listens for add events of nodes. |
| NODE\_DELETE | "NodeDelete" | Listens for delete events of nodes. |
| NODE\_MODIFY | "NodeModify" | Listens for modify events of nodes. |
| NODE\_MOVE | "NodeMove" | Listens for move events of nodes. |

#### CallbackParam

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentNodeId | number | No | No | 
ID of the current child node.

The value must be greater than or equal to 0.

 |
| parentNodeId | number | No | Yes | 

ID of the current parent node.

The value must be greater than or equal to -1.

Default value: **\-1**

 |
| childIndex | number | No | Yes | 

Child index.

The value must be greater than or equal to -1.

Default value: **\-1**

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Configuring a Simple Tree View

This example showcases how to use **TreeController** to perform operations on tree nodes, such as adding, deleting, and renaming. It also demonstrates the effects of adding nodes with different parameters.

import { TreeController, TreeListener, TreeListenerManager, TreeListenType, NodeParam, TreeView, CallbackParam } from '@kit.ArkUI';

@Entry
@Component
struct TreeViewDemo {
  private treeController: TreeController = new TreeController();
  private treeListener: TreeListener = TreeListenerManager.getInstance().getTreeListener();
  @State clickId: number = 0;

  aboutToDisappear(): void {
    this.treeListener.off(TreeListenType.NODE\_CLICK, undefined);
    this.treeListener.off(TreeListenType.NODE\_ADD, undefined);
    this.treeListener.off(TreeListenType.NODE\_DELETE, undefined);
    this.treeListener.off(TreeListenType.NODE\_MOVE, undefined);
  }

  @Builder menuBuilder1() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Add').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.addNode();
        })
      Divider()
      Text('Delete').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.removeNode();
        })
      Divider()
      Text('Rename').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.modifyNode();
        })
    }.width(100).border({width: 1, color: 0x80808a, radius: '16dp'})
  }

  aboutToAppear(): void {
    this.treeListener.on(TreeListenType.NODE\_CLICK, (callbackParam: CallbackParam) => {
      this.clickId = callbackParam.currentNodeId;
    })
    this.treeListener.on(TreeListenType.NODE\_ADD, (callbackParam: CallbackParam) => {
      this.clickId = callbackParam.currentNodeId;
    })
    this.treeListener.on(TreeListenType.NODE\_DELETE, (callbackParam: CallbackParam) => {
      this.clickId = callbackParam.currentNodeId;
    })
    this.treeListener.once(TreeListenType.NODE\_MOVE, (callbackParam: CallbackParam) => {
      this.clickId = callbackParam.currentNodeId;
    })

    let normalResource: Resource = $r('sys.media.ohos\_ic\_normal\_white\_grid\_folder');
    let selectedResource: Resource = $r('sys.media.ohos\_ic\_public\_select\_all');
    let editResource: Resource = $r('sys.media.ohos\_ic\_public\_edit');
    let nodeParam: NodeParam = { parentNodeId:-1, currentNodeId: 1, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
      editIcon: editResource, primaryTitle: "Directory 1 to verify the adaptive effect",
      secondaryTitle: "6" };
    this.treeController
      .addNode(nodeParam)
      .addNode({parentNodeId:1, currentNodeId: 2, isFolder: false, primaryTitle: "Project 1\_1" })
      .addNode({ parentNodeId:-1, currentNodeId: 7, isFolder: true, primaryTitle: "Directory 2" })
      .addNode({ parentNodeId:-1, currentNodeId: 23, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
        editIcon: editResource, primaryTitle: "Directory 3" })
      .addNode({ parentNodeId:-1, currentNodeId: 24, isFolder: false, primaryTitle: "Project 4" })
      .addNode({ parentNodeId:-1, currentNodeId: 31, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
        editIcon: editResource, primaryTitle: "Directory 5", secondaryTitle: "0" })
      .addNode({ parentNodeId:-1, currentNodeId: 32, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
        editIcon: editResource, primaryTitle: "Directory 6", secondaryTitle: "0" })
      .addNode({ parentNodeId:32, currentNodeId: 35, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
        editIcon: editResource, primaryTitle: "Directory 6-1", secondaryTitle: "0" })
      .addNode({ parentNodeId:-1, currentNodeId: 33, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
        editIcon: editResource, primaryTitle: "Directory 7", secondaryTitle: "0" })
      .addNode({ parentNodeId:33, currentNodeId: 34, isFolder: false, primaryTitle: "Project 8" })
      .addNode({ parentNodeId:-1, currentNodeId: 36, isFolder: false, primaryTitle: "Project 9" })
      .buildDone();
    this.treeController.refreshNode (-1, "Parent", "Child");
  }

  build() {
    Column(){
      SideBarContainer(SideBarContainerType.Embed)
      {
        TreeView({ treeController: this.treeController })
        Row() {
          Divider().vertical(true).strokeWidth(2).color(0x000000).lineCap(LineCapStyle.Round)
          Column({ space: 30 }) {
            Text('ClickId=' + this.clickId).fontSize('16fp')
            Button('Add', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(90)
              .onClick((event: ClickEvent) => {
                this.treeController.addNode();
              })
            Button('Modify', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(90)
              .onClick((event: ClickEvent) => {
                this.treeController.modifyNode();
              })
            Button('Remove', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(120)
              .onClick((event: ClickEvent) => {
                this.treeController.removeNode();
              })
          }.height('100%').width('70%').alignItems(HorizontalAlign.Start).margin(10)
        }
      }
      .focusable(true)
      .showControlButton(false)
      .showSideBar(true)
    }
  }}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/xaBqlIhNRLeRjE6aJnjtLA/en-us_image_0000002568765727.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBE52DF9E40661EC007FCBA956BF5F52154784DCF7AA1AFBA2C8589719A7C43B)

## Example 2: Setting the Symbol Icon

This example demonstrates how to use **symbolIconStyle**, **symbolEditIconStyle**, and **symbolSelectedIconStyle** in **NodeParam** to set custom symbol icons. This functionality is supported since API version 18.

import { TreeController, TreeListener, TreeListenerManager, TreeListenType, NodeParam, TreeView, CallbackParam,
  SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct TreeViewDemo {
  private treeController: TreeController = new TreeController();
  private treeListener: TreeListener = TreeListenerManager.getInstance().getTreeListener();
  @State clickNodeId: number = 0;

  aboutToDisappear(): void {
    this.treeListener.off(TreeListenType.NODE\_CLICK, undefined);
    this.treeListener.off(TreeListenType.NODE\_ADD, undefined);
    this.treeListener.off(TreeListenType.NODE\_DELETE, undefined);
    this.treeListener.off(TreeListenType.NODE\_MOVE, undefined);
  }

  @Builder menuBuilder1() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Add').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.addNode();
        })
      Divider()
      Text('Delete').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.removeNode();
        })
      Divider()
      Text('Rename').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
        .onClick((event: ClickEvent) => {
          this.treeController.modifyNode();
        })
    }.width(100).border({width: 1, color: 0x80808a, radius: '16dp'})
  }

  aboutToAppear(): void {
    this.treeListener.on(TreeListenType.NODE\_CLICK, (callbackParam: CallbackParam) => {
      this.clickNodeId = callbackParam.currentNodeId;
    })
    this.treeListener.on(TreeListenType.NODE\_ADD, (callbackParam: CallbackParam) => {
      this.clickNodeId = callbackParam.currentNodeId;
    })
    this.treeListener.on(TreeListenType.NODE\_DELETE, (callbackParam: CallbackParam) => {
      this.clickNodeId = callbackParam.currentNodeId;
    })
    this.treeListener.once(TreeListenType.NODE\_MOVE, (callbackParam: CallbackParam) => {
      this.clickNodeId = callbackParam.currentNodeId;
    })

    let normalResource: Resource = $r('sys.symbol.house');
    let selectedResource: Resource = $r('sys.symbol.car');
    let editResource: Resource = $r('sys.symbol.calendar');
    let normalSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor(\[Color.Red\]);
    let selectedSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor(\[Color.Blue\]);
    let editSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.cake')).fontColor(\[Color.Pink\]);
    let nodeParam: NodeParam = { parentNodeId:-1, currentNodeId: 1, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
      editIcon: editResource, primaryTitle: "Directory 1",
      secondaryTitle: "6" };
    this.treeController
      .addNode(nodeParam)
      .addNode({parentNodeId:1, currentNodeId: 2, isFolder: false, primaryTitle: "Project 1\_1" })
      .addNode({ parentNodeId:-1, currentNodeId: 7, isFolder: true, primaryTitle: "Directory 2" })
      .addNode({ parentNodeId:-1, currentNodeId: 23, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
        selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
        symbolEditIconStyle: editSymbolResource, primaryTitle: "Directory 3" })
      .addNode({ parentNodeId:-1, currentNodeId: 24, isFolder: false, primaryTitle: "Project 4" })
      .addNode({ parentNodeId:-1, currentNodeId: 31, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
        selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
        symbolEditIconStyle: editSymbolResource, primaryTitle: "Directory 5", secondaryTitle: "0" })
      .addNode({ parentNodeId:-1, currentNodeId: 32, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
        selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
        symbolEditIconStyle: editSymbolResource, primaryTitle: "Directory 6", secondaryTitle: "0" })
      .addNode({ parentNodeId:32, currentNodeId: 35, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
        selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
        symbolEditIconStyle: editSymbolResource, primaryTitle: "Directory 6-1", secondaryTitle: "0" })
      .addNode({ parentNodeId:-1, currentNodeId: 33, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
        selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
        symbolEditIconStyle: editSymbolResource, primaryTitle: "Directory 7", secondaryTitle: "0" })
      .addNode({ parentNodeId:33, currentNodeId: 34, isFolder: false, primaryTitle: "Project 8" })
      .addNode({ parentNodeId:-1, currentNodeId: 36, isFolder: false, primaryTitle: "Project 9" })
      .buildDone();
    this.treeController.refreshNode (-1, "Parent", "Child");
  }

  build() {
    Column(){
      SideBarContainer(SideBarContainerType.Embed)
      {
        TreeView({ treeController: this.treeController })
        Row() {
          Divider().vertical(true).strokeWidth(2).color(0x000000).lineCap(LineCapStyle.Round)
          Column({ space: 30 }) {
            Text('ClickNodeId=' + this.clickNodeId).fontSize('16fp')
            Button('Add', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(90)
              .onClick((event: ClickEvent) => {
                this.treeController.addNode();
              })
            Button('Modify', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(90)
              .onClick((event: ClickEvent) => {
                this.treeController.modifyNode();
              })
            Button('Remove', { type: ButtonType.Normal, stateEffect: true })
              .borderRadius(8).backgroundColor(0x317aff).width(120)
              .onClick((event: ClickEvent) => {
                this.treeController.removeNode();
              })
          }.height('100%').width('80%').alignItems(HorizontalAlign.Start).margin(10)
        }
      }
      .focusable(true)
      .showControlButton(false)
      .showSideBar(true)
    }
  }}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/QFUqkVCAQV6uo5sV38x14g/en-us_image_0000002537766002.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=612B9EFD9250F54044FD44D559A29444B113E1036A9178DA38199D96B0DD0A01)
