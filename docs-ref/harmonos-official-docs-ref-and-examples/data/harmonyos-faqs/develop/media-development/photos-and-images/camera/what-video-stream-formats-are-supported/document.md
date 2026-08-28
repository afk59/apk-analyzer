# What video stream formats are supported?

**Question**

In addition to ArrayBuffer and Uint8Array, Blob is supported. Can these byte data be converted into images in different formats?

**Answer**

There are no other formats at the TS layer. The byte data can be converted into a PixelMap, encoded, and then converted into the JPEG, WebP, or PNG format.
