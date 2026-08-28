# How do I choose between the texture types GL\_TEXTURE\_2D and GL\_TEXTURE\_EXTERNAL\_OES?

**Symptom**

During the process of reading videos in Albums, demultiplexing, decoding, and OpenGL processing, the decoded data is received by the corresponding producer NativeWindow in NativeImage, which is bound to the OpenGL texture. However, the test result shows that the decoded content is not updated to the OpenGL texture, which means that the OpenGL texture data is not obtained.

**Possible Causes**

The differences between the use scenarios of the GL\_TEXTURE\_2D and GL\_TEXTURE\_EXTERNAL\_OES texture types are as follows:

-   GL\_TEXTURE\_2D textures are applicable to most scenarios and used to display static maps, render 2D graphics, and perform image processing.
-   GL\_TEXTURE\_EXTERNAL\_OES textures are used to process external images or real-time video streams. Data received from BufferQueue can be used to render texture polygons, improving video processing and rendering efficiency. For example, if you need to read frames from a camera or an external video source, select this texture type.

**Solution**

The OpenGL ES texture associated with NativeImage is bound to **GL\_TEXTURE\_EXTERNAL\_OES**. Therefore, When creating an OH\_NativeImage object and associating it with OpenGL, select the texture type **GL\_TEXTURE\_EXTERNAL\_OES** instead of **GL\_TEXTURE\_2D**.
