# What should I do when the error code "EGL\_BAD\_ALLOC" is reported during the call of the eglSwapBuffers API?

The encoder obtains the NativeWindow through **OH\_VideoEncoder\_GetSurface(encoder\_, &NativeWindow)** and uses the NativeWindow to create an EGL surface of the encoder to receive texture data from OpenGL. If **OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_BUFFER\_GEOMETRY, height, width)** is not called to set the buffer size, the error code is reported during the call of the **eglSwapBuffers** API.
