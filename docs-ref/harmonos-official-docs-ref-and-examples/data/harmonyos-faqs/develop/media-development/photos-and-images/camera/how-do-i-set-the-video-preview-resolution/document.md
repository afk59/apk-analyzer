# How do I set the video preview resolution?

**Symptom**

When the phone rotates, the height of objects in the preview screen changes significantly, and the image is distorted. In the code, the preview resolution is **previewProfile {"format":1003,"size":{"width":3200,"height":2400}}**, and the surface resolution of the **XComponent** is **surfaceWidth: 3200, surfaceHeight: 2400**.

XComponent({
  id: 'componentId',
  type: 'surface',
  controller: this.mXComponentController,
}).onLoad(async () => {
  this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
  let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
  await this.initCamera(baseContext, this.surfaceId)
}).width('100%')
  .height('100%')

**Possible Causes**

The aspect ratio of the **XComponent** is not properly set.

**Solution**

In the preceding code, do not set **width('100%').height('100%')**. Ensure that the width-to-height ratio is the same as the height-to-width ratio in **previewProfile**.
