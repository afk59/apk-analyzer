# How does AspectRatio affect the layout?

**aspectRatio** affects the layout in two ways:

-   It is used in conjunction with other attributes to calculate the size constraints for measuring the component's size.
-   It ensures that the specified aspect ratio is maintained after the component's size has been measured.

During the layout process, the constraints provided by the parent component are based on the parent's specifications. The child component then uses these constraints according to its own specifications. After the parent component provides size constraints, **aspectRatio** and other attributes (such as **size**, **margin**, and **constraintSize**) you have set work together to determine the child component's size constraints. Then, the child component measures its own size based on the resultant constraints.

**Sample Code**

@Entry
@Component
struct VideoAdaptPage {
  build() {
    Column() {
      Column() {
        Video({})
          .layoutWeight(1)
          .borderRadius(12)
          .clip(true)
          .aspectRatio(1)
          .loop(true)
          .autoPlay(true)
          .muted(true)
          .margin({
            left: 20,
            top: 20,
            right: 20,
          })
      }
    }.height(2000)
  }
}

In the preceding code, the **Column** components contain vertically arranged child components, and have height constraints but no width constraints. For ease of calculation, the height of the outer **Column** component is fixed at **2000**. In the following examples, the **Column** components are all child components nested within the top-level **Column**.

-   The **Column** component has a height constraint of 2000 and no width constraint.
-   The **Column** component passes a height constraint (2000) and width constraint (none) to the **Video** child component.
-   Due to the **aspectRatio** settings, the **Video** component has a height constraint of 2000 and a width constraint of 2000.
-   Due to the **margin** settings, the **Video** component has a height constraint of 1980 and a width constraint of 1960.
-   Due to the **aspectRatio** settings, the **Video** component is measured at a height of 1960 and a width of 1960.
-   After being stretched by its child component, the **Column** component is measured at a height of 1980 and a width of 2000.

Since the **Column** has component no effective width constraint, it allows its child components to be drawn outside the container in the cross axis. In this case, the actual width of the **Video** component is 1960, but only 1080 is visible on the screen.
