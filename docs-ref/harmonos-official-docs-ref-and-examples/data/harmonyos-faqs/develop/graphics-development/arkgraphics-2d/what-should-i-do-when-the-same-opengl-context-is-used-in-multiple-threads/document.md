# What should I do when the same OpenGL context is used in multiple threads?

**Symptom**

The EGL environment is initialized and the context is created in the main thread, and the rendering process is processed in an independent child thread. In this case, a black screen is displayed.

**Solution**

The OpenGL context is bound to a specific thread. Therefore, you cannot perform operations from multiple threads in the same OpenGL context at the same time.

Method 1: Place the EGL environment initialization and rendering process in the same thread.

Method 2: After the main thread initializes the EGL environment and creates the context, call **eglMakeCurrent** to unbind the context from the main thread, and then bind the context to a child thread.
