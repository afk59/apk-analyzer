# How Do I Implement Zoom Ratio Change Through Gestures?

**Problem**

How do I implement the function of changing the zoom ratio of the camera stream through gestures for the custom barcode scanning UI?

**Solution**

Call **setZoom(zoomValue : number): void** by referring to [Combined Gestures](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/implementing-interaction-responses/implementing-gesture-responses/combined-gestures/document.md) to set the zoom ratio.

In the sample code, the zoom ratio can be changed in both the gesture-based zooming follow-up and gesture-based zooming ending APIs.

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

const TAG: string = '\[Scan Sample\]';
const MIN\_ZOOM\_RATIO: number = 1; // For example, the minimum zoom ratio is 1.
const MAX\_ZOOM\_RATIO: number = 4; // For example, the maximum zoom ratio is 4.

@Entry
@Component
struct Index {
  private baseZoom: number = 1; // Zoom ratio in use.
  private zoomRatio: number = 1; // Zoom ratio after the operation.

  build() {
    Column() {
      // Bind a gesture.
    }.gesture(PinchGesture({ fingers: 2 })
      .onActionStart(() => {
        // The pinch gesture starts.
        hilog.info(0x0001, TAG, 'Pinch start');
        this.pinchGestureStart();
      })
      .onActionUpdate((event: GestureEvent) => {
        if (event && event.scale) {
          // The pinch gesture is updated.
          this.pinchGestureUpdate(event.scale);
        }
      })
      .onActionEnd(() => {
        // The pinch gesture ends.
        hilog.info(0x0001, TAG, 'Pinch end');
      })
    )
  }

  /\*\*
   \* Obtain the zoom ratio in use.
   \* @returns {number} Zoom ratio in use.
   \*/
  getZoom(): number {
    let zoom = 1;
    try {
      zoom = customScan.getZoom();
      hilog.info(0x0001, TAG, \`getZoom end, zoom: ${zoom}\`);
    } catch (error) {
      hilog.error(0x0001, TAG, \`Failed to getZoom. Code: ${error.code}, message: ${error?.message}\`);
    }
    return zoom;
  }

  /\*\*
   \* Set the zoom ratio.
   \* @param {number} zoomRatio - Zoom ratio to be set.
   \*/
  setZoom(zoomRatio: number): void {
    try {
      customScan.setZoom(zoomRatio);
      hilog.info(0x0001, TAG, \`setZoom end, zoomRatio: ${zoomRatio}\`);
    } catch (error) {
      hilog.error(0x0001, TAG, \`Failed to setZoom. Code: ${error.code}, message: ${error?.message}\`);
    }
  }

  /\*\*
   \* Process the pinch gesture start event and record the initial zoom ratio.
   \*/
  pinchGestureStart(): void {
    this.baseZoom = this.getZoom();
    this.zoomRatio = this.baseZoom;
    hilog.info(0x0001, TAG, \`pinchGestureStart. baseZoom: ${this.baseZoom}\`);
  }

  /\*\*
   \* Process the pinch gesture update event and update the zoom ratio based on the scale factor of the gesture.
   \* @param {number} scale - Scale factor of the pinch gesture.
   \*/
  public pinchGestureUpdate(scale: number): void {
    hilog.info(0x0001, TAG, \`pinchGestureUpdate. scale: ${scale}\`);
    let tmpZoom: number = scale \* this.baseZoom;
    if (scale > 1) {
      if (tmpZoom <= MAX\_ZOOM\_RATIO) {
        this.updateZoom(tmpZoom);
      }
    } else {
      if (tmpZoom < MIN\_ZOOM\_RATIO) {
        tmpZoom = MIN\_ZOOM\_RATIO;
      }
      this.updateZoom(tmpZoom);
    }
  }

  /\*\*
   \* Update the zoom ratio if its change is greater than 0.01 (threshold).
   \* @param {number} tmpZoom - Zoom ratio calculated temporarily.
   \*/
  public updateZoom(tmpZoom: number): void {
    if (Math.abs(tmpZoom - this.zoomRatio) > 0.01) {
      hilog.info(0x0001, TAG, \`updateZoom. tmpZoom: ${tmpZoom}\`);
      this.zoomRatio = tmpZoom;
      this.setZoom(this.zoomRatio);
    }
  }
}
