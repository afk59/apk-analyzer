# What should I do when the error code "EGL\_BAD\_SURFACE (300d)" is reported during the call of the eglSwapBuffers API? The log information "QEGLPlatformContext: eglSwapBuffers failed: 300d" is displayed.

The error code EGL\_BAD\_SURFACE is reported when the surface is not an EGL surface. Check the settings of **eglCreateWindowSurface**, **eglCreatePixmapSurface**, and **eglCreatePbufferSurface**.
