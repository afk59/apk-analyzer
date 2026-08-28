# LazyVGridLayout

The **LazyVGridLayout** component implements a lazy-loading grid layout, with its parent component restricted to [WaterFlow](../waterflow/document.md) or [FlowItem](../flowitem/document.md). It can also be used within the **WaterFlow** or **FlowItem** component after being wrapped by custom components or [NodeContainer](../../custom-placeholder-components/nodecontainer/document.md).

Lazy loading is supported only when the **WaterFlow** component uses single-column mode or single-column segments in segmented layout and [FlexDirection](../../common-definitions/enums/document.md#flexdirection) is set to **FlexDirection.Column**. Lazy loading is not supported if the **WaterFlow** component is in multi-column mode or the layout direction is **FlexDirection.Row** or **FlexDirection.RowReverse**. Using this component with **FlexDirection.ColumnReverse** in the **WaterFlow** component causes display anomalies. When lazy loading is enabled, the component only loads child components within the **WaterFlow** visible area, with pre-loading of half-screen content above and below the viewport during frame idle periods.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/STZGkjrcQFKrecMYZBlETw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CB7AEABCB545E6071B3BDFC19B3B50F21EC3E9D9C5C09577595D39D297993FB)

-   This component is supported since API version 19. Updates will be marked with a superscript to indicate their earliest API version.
-   This component's height adapts to content by default. Setting the height, height constraints, or aspect ratio causes display anomalies.

#### APIs

LazyVGridLayout()

Creates a vertical lazy-loading grid layout container.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]columnsTemplate

columnsTemplate(value: string)

Sets the number of columns, fixed column width, or minimum column width of the grid. If this attribute is not set, one column will be used.

For example, **'1fr 1fr 2fr'** indicates three columns, with the first column taking up 1/4 of the parent component's full width, the second column 1/4, and the third column 2/4.

**columnsTemplate('repeat(auto-fit, track-size)')**: The layout automatically calculates the number of columns and their actual widths while respecting the minimum column width specified by **track-size**.

**columnsTemplate('repeat(auto-fill, track-size)')**: The layout automatically calculates the number of columns based on the fixed column width specified by **track-size**.

**columnsTemplate('repeat(auto-stretch, track-size)')**: The layout uses **columnsGap** to define the minimum gap between columns and automatically calculates the number of columns and the actual gap size based on the fixed column width specified by **track-size**.

**repeat**, **auto-fit**, **auto-fill**, and **auto-stretch** are keywords. **track-size** indicates the column width, in units of px, vp (default), %, or any valid numeric value. The value must be greater than or equal to a valid column width.

In auto-fit and auto-stretch modes, only a valid column width value is supported for **track-size**. Additionally, in auto-stretch mode, **track-size** only supports units such as px, vp, and valid numbers, but does not support percentage (%). The auto-fill mode supports one or more valid column widths, for example: columnsTemplate('repeat(auto-fill, 20)') or columnsTemplate('repeat(auto-fill, 20 80px)').

If this attribute is set to **'0fr'**, the column width is 0, and child components are not displayed. If this attribute is set to an invalid value, the child components are displayed in a fixed column.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Number of columns or minimum column width of the grid. |

#### \[h2\]columnsGap

columnsGap(value: LengthMetrics): T

Sets the gap between columns. Values less than 0 are treated as the default value.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Gap between columns.

Default value: **0vp**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current **LazyVGridLayout** component. |

#### \[h2\]rowsGap

rowsGap(value: LengthMetrics): T

Sets the gap between rows. Values less than 0 are treated as the default value.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Gap between rows.

Default value: **0vp**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current **LazyVGridLayout** component. |

#### Events

Only the [universal events](../../universal-events/document.md) are supported.

#### Example

This example demonstrates how to implement a lazy-loading grid layout using the **WaterFlow** and **LazyVGridLayout** components.

**MyDataSource** implements the [IDataSource](../../state-management-and-rendering-control/lazyforeach/document.md#idatasource) API for [LazyForEach](../../state-management-and-rendering-control/lazyforeach/document.md), which provides child components for **LazyVGridLayout** through **LazyForEach**.

import { LengthMetrics } from '@kit.ArkUI'
import { MyDataSource } from './MyDataSource'

@Entry
@Component
struct LazyVGridLayoutSample1 {
  private arr1:MyDataSource<number> = new MyDataSource<number>();
  private arr2:MyDataSource<number> = new MyDataSource<number>();
  build() {
    Column() {
      WaterFlow() {
        LazyVGridLayout() {
          LazyForEach(this.arr1, (item:number)=>{
            Text('item' + item.toString())
              .height(64)
              .width('100%')
              .borderRadius(5)
              .backgroundColor(Color.White)
              .textAlign(TextAlign.Center)
          })
        }
        .columnsTemplate('1fr')
        .rowsGap(LengthMetrics.vp(10))

        LazyVGridLayout() {
          LazyForEach(this.arr2, (item:number)=>{
            Text('item' + item.toString())
              .height(128)
              .width('100%')
              .borderRadius(5)
              .backgroundColor(Color.White)
              .textAlign(TextAlign.Center)
          })
        }
        .columnsTemplate('1fr 1fr')
        .rowsGap(LengthMetrics.vp(10))
        .columnsGap(LengthMetrics.vp(10))
      }.padding(10)
      .rowsGap(10)
    }
    .width('100%').height('100%')
    .backgroundColor('#DCDCDC')
  }

  aboutToAppear(): void {
    for (let i = 0; i < 6; i++) {
      this.arr1.pushData(i);
    }
    for (let i = 0; i < 100; i++) {
      this.arr2.pushData(i);
    }
  }
}

// MyDataSource.ets
export class BasicDataSource<T> implements IDataSource {
  private listeners: DataChangeListener\[\] = \[\];
  protected dataArray: T\[\] = \[\];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): T {
    return this.dataArray\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  notifyDatasetChange(operations: DataOperation\[\]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    })
  }
}

export class MyDataSource<T> extends BasicDataSource<T> {
  public shiftData(): void {
    this.dataArray.shift();
    this.notifyDataDelete(0);
  }
  public unshiftData(data: T): void {
    this.dataArray.unshift(data);
    this.notifyDataAdd(0);
  }
  public pushData(data: T): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
  public popData(): void {
    this.dataArray.pop();
    this.notifyDataDelete(this.dataArray.length);
  }
  public clearData(): void {
    this.dataArray = \[\];
    this.notifyDataReload();
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4xP5rqL0QYGFd18kF_LZRw/en-us_image_0000002537765556.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AB04BA0FBED9B9F05150BD8EE0B4D02596B2D866A3ABECD212689841EB34D38)
