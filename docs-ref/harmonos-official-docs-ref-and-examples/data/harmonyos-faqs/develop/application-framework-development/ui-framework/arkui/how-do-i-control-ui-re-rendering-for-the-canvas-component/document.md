# How do I control UI re-rendering for the Canvas component?

The content displayed in the **Canvas** component can be divided into two categories:

1\. Universal component attributes, such as background color and border. These attributes can be automatically updated through state variables.

2\. Content drawn by the application through the **CanvasRenderingContext2D** API. This API does not respond to state variables and will automatically re-render the content in the next frame without requiring you to manually control the re-rendering.

**Reference**

[CanvasRenderingContext2D](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-canvasrenderingcontext2d)
