# How do I proactively disable CPU access to window buffers to reduce power consumption?

By default, window buffers use CPU access for compatibility reasons. However, GPU access to window buffers is more energy-efficient, and relying on CPU access can lead to higher power consumption. If your application does not need CPU access, you can manually disable it to enhance the application's energy efficiency.

**Symptom**

A self-drawing application uses CPU access by default when producing buffer content. This approach results in lower efficiency and higher performance overhead due to the inefficiency of CPU access.

**Solution**

If you ensure that the application does not need to use the CPU to access window buffer data, you can disable CPU access when the application first obtains the window handle (OnSurfaceCreatedCB). This allows the hardware platform to select the most efficient image format, thereby improving energy efficiency and reducing power consumption.

When the application obtains the window handle (OnSurfaceCreatedCB) for the first time, call the **OH\_NativeWindow\_NativeWindowHandleOpt(…, SET\_USAGE, …)** method to set the value of **USAGE** in the buffer. This disables CPU access, and the system will use a more efficient method (such as GPU access) to access the buffer. Refer to the code snippet below.

void OnSurfaceCreatedCB(OH\_NativeXComponent \*component, void \*window) {    
    uint64\_t usage = 0;
    int32\_t ret = OH\_NativeWindow\_NativeWindowHandleOpt((OHNativeWindow\*)window, GET\_USAGE, &usage);
    usage &= ~NATIVEBUFFER\_USAGE\_CPU\_READ;
    int32\_t ret2 = OH\_NativeWindow\_NativeWindowHandleOpt((OHNativeWindow\*)window, SET\_USAGE, usage);
}

For high-load scenarios, such as large games, disabling CPU access can improve energy efficiency by about 30%.
