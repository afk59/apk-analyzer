# Does an EGL surface support simultaneous display and output to the encoder?

No.

**Possible Causes**

If the same EGL surface is used for display and output to the encoder, the buffer cannot be rotated properly. In the EGL surface, the producer and consumer are in one-to-one mapping.

**Solution**

After OpenGL processing, simultaneous display and output to the encoder are supported. To achieve this, create two EGL surfaces and call **eglMakeCurrent** to select the EGL surface to be consumed each time.
