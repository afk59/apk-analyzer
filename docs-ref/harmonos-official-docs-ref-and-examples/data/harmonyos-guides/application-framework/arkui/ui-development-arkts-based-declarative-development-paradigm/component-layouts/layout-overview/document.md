# Layout Overview

Components are systematically arranged according to layout specifications to construct application pages. In declarative UI, all pages consist of custom components. You can select appropriate layout approaches for page development based on specific requirements.

Layout involves managing the size and position of UI components on user pages using dedicated components or attributes. In practical development, follow this process to ensure overall layout effectiveness:

-   Define the layout structure of the page.
    
-   Analyze the composition of elements on the page.
    
-   Select appropriate container components and attributes to control the position and size of each element on the page.
    

#### Layout Structure

A layout is generally in a hierarchical structure. Below is a common page structure.

**Figure 1** Common page structure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qpLU3D8TT7OWFDUm9qHx9g/en-us_image_0000002568684247.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061932Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AF726DD1A056571617FD8C453286AF9BFBA05A5A9E0A585E5120E94EBC52414)

To achieve the preceding effect, you need to declare the corresponding elements on the page. **Page** indicates the root node of the page, and other elements such as **Column** and **Row** are built-in components. ArkUI provides a wide variety of layout components, which you can draw on to implement different layouts. For example, you can use **Row** to implement a linear layout.

#### Layout Elements

You can use layout-related container components to create a specific layout.

**Figure 2** Layout elements

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/SYabqYVvRuy65Eg25ImI2w/en-us_image_0000002568764257.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061932Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A47D414B83D14D0180CDE714DBEC804EB36117E7A8AAFA2E86191FCECA615167)

-   Component area (blue block): size of the component, subject to the [width](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#width) and [height](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#height) attributes.
    
-   Component content area (yellow block): size of the component area minus the [border](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-border#border) of the component. It serves as the layout constraint for calculating the size of the component content (or child component).
    
-   Component content (green block): size of the component content, for example, size of the text content in the component. The component content may not match the component content area. For example, if fixed **width** and **height** values are set, the actual size of the component content area is determined by subtracting [padding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#padding) and **border** values from the set size. However, the size of component content is calculated by the layout engine, which may be less than the component content area. In such cases, the component content may not fully occupy the space provided by the component content area. When the component content and component content area do not match, the [align](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#align) attribute takes effect, defining the alignment mode of the component content in the component content area, for example, center aligned.
    
-   Component layout bounds (dotted lines): component area plus the [margins](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#margin) (if supplied).
    

#### Layout Selection

The declarative UI provides the following common layouts. Choose a layout that best suits the use case.

| Layout | Description |
| :-- | :-- |
| [Linear layout](../building-a-layout/linear-layout-row-column/document.md) (Row and Column) | Use this layout when there are multiple child components and they can be arranged linearly. |
| [Stack layout](../building-a-layout/stack-layout-stack/document.md) (Stack) | Use this layout when you want to stack components. The stacking does not occupy or affect the layout space of other components in the same container. For example, when the [Panel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-panel) component is displayed as a child, superimposing it over other components makes more sense. In this case, the stack layout is preferred at the outer layer. |
| [Flex layout](../building-a-layout/flex-layout-flex/document.md) (Flex) | The flex layout is similar to the linear layout. However, it empowers the container to adjust the size of its child components to best fill the available space. Use this layout when you need elements to stretch or shrink to fit into the container. |
| [Relative layout](../building-a-layout/relative-layout-relativecontainer/document.md) (RelativeContainer) | The relative layout is a two-dimensional layout system. It does not need to comply with linear layout rules, and therefore exhibits more flexibility. By setting anchor rules (**AlignRules**) on a child component, you enable the component to position itself on the horizontal axis and vertical axis as relative to other child component in the container. Anchor rules support compression, stretching, stacking, and wrapping of child components. Use this layout when the distribution of elements is complex or when a linear layout may result in deeply nested components in the container. |
| [Responsive grid layout](../building-a-layout/responsive-grid-layout-gridrow-gridcol/document.md) (GridRow and GridCol) | The responsive grid is an auxiliary positioning tool for a multi-device application, with capability of dividing space into rows and columns. Unlike the regular grid, the responsive grid is not allocating fixed-size space. Instead, it allows a layout to dynamically change based on the screen size. In this way, the design and development costs for adapting to different screen sizes are significantly reduced, and the overall design and development process is more orderly and rhythmic. In addition, the responsive grid offers a consistent display experience across devices. Use this layout when you are presenting the same content on different screen sizes. |
| [Tabs](../building-a-layout/using-tabs-tabs/document.md) | The **Tabs** component can quickly switch between views on a page, improving information search efficiency and reducing the amount of information that users receive at a time. |

#### Layout Position

Attributes such as **position** and **offset** affect the position of the layout container relative to itself or other components.

| Positioning Capability | Description | Implementation |
| :-- | :-- | :-- |
| Absolute positioning | Absolute positioning is poor in adaptability to devices of different sizes, and is prone to screen adaptation errors. | Use [position](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#position) to implement absolute positioning and set the offset position of the upper left corner of an element relative to the upper left corner of the parent container. When laying out components, this attribute does not affect the layout of the parent component. It only adjusts the component position during drawing. |
| Relative positioning | Relative positioning keeps an element in the normal document flow, while allowing you to move it around relative to its original location. | You can use [offset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-location#offset) to implement relative positioning and set the offset of an element relative to itself. This attribute does not affect the layout of the parent component. It only adjusts the component position during drawing. |

#### Constraints on Child Components

-   Stretching: When the size of a container component changes, the increased or decreased amount of space is allocated to the specified area in the container component.
    
    [flexGrow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexgrow) and [flexShrink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink) attributes:
    
    1.  **flexGrow** defines the grow factor of a flex item.
    2.  **flexShrink** defines the shrink factor of a flex item.
-   Scaling: The width and height of a child component change with the container component, with its aspect ratio fixed at the preset value.
    
    The [aspectRatio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-layout-constraints#aspectratio) attribute specifies the aspect ratio of the current component. The formula is as follows: aspectRatio = width/height.
    
-   Proportion: The width and height of child components to adjust dynamically in response to changes in the size of the container component, according to the preset proportion value.
    
    Two implementation modes are available with the universal attributes:
    
    1.  Set the width and height of child components using percentage values.
        
        | Parent and Ancestor Component Configuration | Child Component Reference Basis |
        | :-- | :-- |
        | The parent component sets the width or height, and the ancestor component does not specify the parent's width or height. | Parent component's actual width and height |
        | The parent component sets the width or height, and the ancestor component specifies the parent's width or height. | Parent component's width and height specified by the ancestor component |
        | The parent component does not set the width or height, and the ancestor component specifies the parent's width or height | Parent component's width and height specified by the ancestor component |
        | The parent component does not set the width or height, and the ancestor component does not specify the parent's width or height | Percentage reference inherited from the parent component. Since the parent component does not specify the width or height, this reference is passed down from the ancestor component. |
        
    2.  Use the [layoutWeight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-size#layoutweight) attribute to enable the child components to adaptively occupy the remaining space.
        
-   Hiding: The child components in a container component are shown or hidden according to their preset display priority as the container component's size changes. Child components with the same display priority are shown or hidden at the same time.
    
    This feature is governed by the [displayPriority](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-layout-constraints#displaypriority) attribute, which dictates the visibility of components.
