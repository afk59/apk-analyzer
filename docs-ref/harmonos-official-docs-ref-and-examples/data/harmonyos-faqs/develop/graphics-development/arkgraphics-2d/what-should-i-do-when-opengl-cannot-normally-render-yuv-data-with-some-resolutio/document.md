# What should I do when OpenGL cannot normally render YUV data with some resolutions?

**Symptom**

YUV data with specific resolutions (for example, 668 x 352) is distorted when rendered by OpenGL.

**Solution**

OpenGL rendering requires that the width be 16-pixel aligned and the height be 2-pixel aligned. If this requirement is not met, add the following code during rendering:

cpp glPixelStorei(GL\_UNPACK\_ALIGNMENT, 1); // Disable the texture byte alignment restriction.
