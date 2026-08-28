# Are EGL operations supported in multithreaded scenarios? How do I operate a buffer to draw a graphic in multithreaded scenarios?

-   EGL operations are supported in multithreaded scenarios. You can generate a texture through each thread, and then combine the textures into a buffer.
-   The shared context can be used. In addition, the drawing operation can be implemented through OpenGL.
-   The code for creating a shared context is as follows:
    
    void CreateShareEglContext() 
    {
      if (renderContext == nullptr) { // RenderContext is the main thread context 
        RS\_LOGE("renderContext\_ is nullptr");
        return;
      }
      eglShareContext = renderContext->CreateShareContext(); // Create share context 
      if (eglShareContext == EGL\_NO\_CONTEXT) {
        RS\_LOGE("eglShareContext is EGL\_NO\_CONTEXT");
        return;
      }
      if (!eglMakeCurrent(renderContext->GetEGLDisplay(), EGL\_NO\_SURFACE, EGL\_NO\_SURFACE, eglShareContext)) {
        RS\_LOGE("eglMakeCurrent failed");
        return;
      }
    }
