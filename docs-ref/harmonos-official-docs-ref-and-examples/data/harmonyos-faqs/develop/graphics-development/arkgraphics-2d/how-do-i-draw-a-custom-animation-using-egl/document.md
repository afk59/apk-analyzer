# How do I draw a custom animation using EGL?

You are responsible for implementing custom animations, which can be rendered using OpenGL. which can be rendered using OpenGL. The core of animation implementation lies in service logic. You should identify the events that trigger animations, determine the start and end points, compute the content of each frame according to the timeline and animation curve, and then use the OpenGL interface to render the animations.

**Reference**

[Custom Rendering (XComponent)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines)
