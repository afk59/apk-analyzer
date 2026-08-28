# Placing AR Objects

#### Overview

AR Engine supports this capability since version 5.0.0(12).

This section describes how AR Engine identifies planes surrounding a device and allows users to place virtual objects on them, bridging the virtual and real worlds. It is ideal for virtual home decoration and digital exhibition hall layouts.

**Figure 1** AR object placement  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ZdiowNPxStu_nUAPXoTzOg/en-us_image_0000002500426106.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8924DAC084D960D72542F3A66F5B8954C2C12CD21474778539B7B1857C55B4C "Click to enlarge")

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)
-   Hit testing

#### API Description

The following lists APIs used for AR object placement. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3)

 | 

Creates an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARSession\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1d1cacf372a8011a439f0e4e76994259)

 | 

Updates the computation result of AR Engine.

 |
| 

[HMS\_AREngine\_ARSession\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga6394ae995148abbe3d00082817bf320a)

 | 

Configures an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARFrame\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gadfcb9589137a39c5afcb217e18853a9d)

 | 

Creates an [AREngine\_ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in **\*outFrame**.

 |
| 

[HMS\_AREngine\_ARSession\_SetDisplayGeometry](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3f23bf747def8303c3fb261a9e9a2286)

 | 

Sets the display height and width (in pixels). Ensure that the height and width you set here are consistent with those of the display view. A mismatch will result in a camera preview failure.

 |
| 

[HMS\_AREngine\_ARSession\_SetCameraGLTexture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac697e4be36db63ed6098f154aa9ac01c)

 | 

Sets the OpenGL texture for storing the camera preview stream data.

 |
| 

[HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[HMS\_AREngine\_ARTrackableList\_AcquireItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab1782eeeeddc01b77a140af915cb351c)

 | 

Obtains the object at a specified index from the trackable object list.

 |
| 

[HMS\_AREngine\_ARPlane\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gabbb03027afb984be8542d00d2eebd063)

 | 

Obtains the pose information for the conversion from the plane's local coordinate system to the world coordinate system.

 |
| 

[HMS\_AREngine\_ARFrame\_HitTest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9377f19261d5bbc2044497729b4e0df)

 | 

Obtains the hit testing result based on the POI position on the screen.

 |
| 

[HMS\_AREngine\_ARHitResultList\_GetSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga131d081663d457c594664c977bd9033c)

 | 

Obtains the number of objects in the list of hit testing result objects.

 |
| 

[HMS\_AREngine\_ARHitResultList\_GetItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf165c7a1c9ae003cac2a1c2ac2e5e5c4)

 | 

Obtains the hit testing result object at a specific index from the list of hit testing result objects.

 |
| 

[HMS\_AREngine\_ARHitResult\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga4b06bcca0f6fc0b081ef8210765d9c91)

 | 

Creates an empty hit testing result object.

 |
| 

[HMS\_AREngine\_ARHitResult\_AcquireNewAnchor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga30abe7b3457c991815dd79fcfaf26018)

 | 

Creates an anchor at the intersection.

 |
| 

[HMS\_AREngine\_ARHitResult\_AcquireTrackable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac3a02e30bb7706d87c4c29d38b363840)

 | 

Obtains the trackable object that is hit.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga5295c975a0ff3d633a1dde5a8eb70863)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[HMS\_AREngine\_ARPose\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gafb471f39563ca1a4947d4f87c77e24e2)

 | 

Allocates and initializes a new pose object.

 |
| 

[HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a)

 | 

Obtains the pose of the current camera object in the AR world space.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp) to access the complete demo code.

## Declaring Native APIs

Declare ArkTS APIs.

import { resourceManager } from '@kit.LocalizationKit';

export const start: (id: string, params: Int32Array) => void;
export const show: (id: string) => void;
export const hide: (id: string) => void;
export const update: (id: string) => number;
export const stop: (id: string) => void;
export const init: (resmgr: resourceManager.ResourceManager) => void;
export const getDistance: (id: string) => string;
export const initImage: (id: string, width: number, height: number, buffer: ArrayBuffer) => number;
export const setPath: (id: string, path: string) => void;
export const saveImageDataBaseToLocal: (id: string, path: string) => void;
export const getImageCount: (id: string) => number;
export const getVolume: (id: string) => string;

Create the mapping between ArkTS APIs and C++ APIs.

napi\_property\_descriptor desc\[\] = {
    {"init", nullptr, Global::Init, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"start", nullptr, NapiManager::NapiOnPageAppear, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"show", nullptr, NapiManager::NapiOnPageShow, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"hide", nullptr, NapiManager::NapiOnPageHide, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"update", nullptr, NapiManager::NapiOnPageUpdate, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"stop", nullptr, NapiManager::NapiOnPageDisappear, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"getDistance", nullptr, NapiManager::NapiGetDistance, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"initImage", nullptr, NapiManager::NapiInitImage, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"setPath", nullptr, NapiManager::NapiSetPath, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"saveImageDataBaseToLocal", nullptr, NapiManager::NapiSaveImageDataBaseToLocal, nullptr, nullptr, nullptr,
     napi\_default, nullptr},
    {"getImageCount", nullptr, NapiManager::NapiGetImageCount, nullptr, nullptr, nullptr, napi\_default, nullptr},
    {"getVolume", nullptr, NapiManager::NapiGetVolume, nullptr, nullptr, nullptr, napi\_default, nullptr}
};

## Creating a UI

Create a UI, use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to display the camera preview image, and periodically trigger the drawing of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARWorld.ets.
import { PromptAction } from '@kit.ArkUI';
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARWorldBuilder() {
  ARWorld();
}

@Component
struct ARWorld {
  pageInfo: NavPathStack = new NavPathStack();
  private currentMillisecond: number = 0;
  private interval: number = -1;
  private isUpdate: boolean = true;
  private xComponentId: string = 'ARWorld';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State numberOfPlans: number = 0;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // Update the calculation result of each frame by calling the native API **update** of AR Engine.
                this.numberOfPlans = arEngineDemo.update(this.xComponentId);
                this.planeNum();
              }
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[1, this.rotation\]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private messageNotification(): void {
    let promptAction: PromptAction = this.getUIContext().getPromptAction();
    promptAction.showToast({
      message: 'Unable to identify the plane due to limited number of feature points. Please move the camera.',
      bottom: 300
    })
  }

  private planeNum(): void {
    if (this.numberOfPlans < 1) {
      // The number of planes is less than 1.
      let tempMillisecond: number = new Date().getTime();
      // Assign a value as the first launch time.
      if (this.currentMillisecond === 0) {
        this.currentMillisecond = tempMillisecond;
        return;
      }
      // If the plane recognition duration exceeds 10 seconds, display a pop-up.
      if (tempMillisecond - this.currentMillisecond > 10000) {
        this.messageNotification();
        this.currentMillisecond = 0;
      }
    } else {
      this.currentMillisecond = 0;
    }
  }
}

## Importing AR Engine

For details, please refer to [Importing AR Engine](../managing-ar-sessions/document.md#section1410827131110) in **Managing AR Sessions**.

## Creating an AR Scene

1.  Call [HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3) to create an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session, by referring to [Managing AR Sessions](../managing-ar-sessions/document.md).
2.  Configure the AR session and preview size.
    
    // (Optional) Create a configuration object with a proper default configuration.
    AREngine\_ARConfig \*arConfig = nullptr;
    HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
    // (Optional) Configure an **AREngine\_ARSession** session.
    HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);
    // (Optional) Release the memory used by the specified configuration object.
    HMS\_AREngine\_ARConfig\_Destroy(arConfig);
    
    // Create an AREngine\_ARFrame object.
    AREngine\_ARFrame \*arFrame = nullptr;
    HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
    // Set the actual width and height of the preview area. If you display the image with xComponent, make sure that the width and height are consistent with those in xComponent. Otherwise, an error will occur with the camera preview.
    int32\_t width = 1440;
    int32\_t height = 1080;
    // Display rotation constant. The value is an enum defined in AREngine\_ARPoseType.
    AREngine\_ARPoseType displayRotation = ARENGINE\_POSE\_TYPE\_IDENTITY;
    // Set the display height and width (in pixels).
    HMS\_AREngine\_ARSession\_SetDisplayGeometry(arSession, displayRotation, width, height);
    
3.  Obtain the texture ID through an OpenGL API.
    
    // Obtain the texture ID through an OpenGL API.
    GLuint textureId = 0;
    glGenTextures(1, &textureId);
    
4.  Set the OpenGL texture for storing the camera preview stream data.
    
    // Set the OpenGL texture for storing the camera preview stream data.
    HMS\_AREngine\_ARSession\_SetCameraGLTexture(arSession, textureId );
    

## Obtaining the Plane

1.  Call [HMS\_AREngine\_ARSession\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1d1cacf372a8011a439f0e4e76994259) to update the current [AREngine\_ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf35f728a1179ef54a3eba9f1cf021719) object.
    
    // Obtain the frame data AREngine\_ARFrame.
    HMS\_AREngine\_ARSession\_Update(arSession, arFrame);
    
2.  Obtain the view matrix and the projection matrix of the camera for subsequent rendering.
    
    // Obtain the camera object AREngine\_ARCamera based on AREngine\_ARFrame.
    AREngine\_ARCamera \*arCamera = nullptr;
    HMS\_AREngine\_ARFrame\_AcquireCamera(arSession, arFrame, &arCamera);
    // Obtain the view matrix of the camera in the latest frame.
    HMS\_AREngine\_ARCamera\_GetViewMatrix(arSession, arCamera, glm::value\_ptr(\*viewMat), 16);
    // Obtain the projection matrix used for rendering virtual content on top of the camera image. This matrix can be used for converting from the camera coordinate system to the clip coordinate system. Near (0.1) Far (100)
    HMS\_AREngine\_ARCamera\_GetProjectionMatrix(arSession, arCamera, {0.1f, 100.f}, glm::value\_ptr(\*projectionMat), 16);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/NUdkPJ0xQRSLaqkHUyB7vg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D26958C8B6A2AF9FE09BC635C371A087BB3B172990B7848E9B8799962227511)
    
    The view matrix and the projection matrix of the camera are obtained to facilitate rendering. You can also call [HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a) and [HMS\_AREngine\_ARPose\_GetPoseRaw](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1ee66c006ffe8255cc04f2a24c277709) to obtain changes to the camera pose as the camera moves. For details, please refer to [Obtaining the Current Device Pose](../obtaining-the-device-pose/document.md#section1894312892612).
    
3.  Call [HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c) to obtain the plane list. For details, please refer to [Detecting Planes in the Environment](../detecting-planes-in-the-environment/document.md).
    
    // Obtain the list of detected planes.
    AREngine\_ARTrackableList \*planeList = nullptr;
    // Create a list of trackable objects.
    HMS\_AREngine\_ARTrackableList\_Create(arSession, &planeList);
    // Obtain the list of all trackable objects of the ARENGINE\_TRACKABLE\_PLANE type.
    AREngine\_ARTrackableType planeTrackedType = ARENGINE\_TRACKABLE\_PLANE;
    HMS\_AREngine\_ARSession\_GetAllTrackables(arSession, planeTrackedType, planeList);
    int32\_t planeListSize = 0;
    // Obtain the number of trackable objects in the list.
    HMS\_AREngine\_ARTrackableList\_GetSize(arSession, planeList, &planeListSize);
    for (int i = 0; i < planeListSize; ++i) {
        AREngine\_ARTrackable \*arTrackable = nullptr;
        // Obtain the object at a specified index from the trackable object list.
        HMS\_AREngine\_ARTrackableList\_AcquireItem(arSession, planeList, i, &arTrackable);
        AREngine\_ARPlane \*arPlane = reinterpret\_cast<AREngine\_ARPlane\*>(arTrackable);
        // Obtain the tracking status of the current trackable object. Plane drawing is performed only when the tracking status is ARENGINE\_TRACKING\_STATE\_TRACKING (trackable).
        AREngine\_ARTrackingState outTrackingState;
        HMS\_AREngine\_ARTrackable\_GetTrackingState(arSession, arTrackable, &outTrackingState);
        AREngine\_ARPlane \*subsumePlane = nullptr;
        // Obtain a plane's parent plane (generated when the plane is merged with another one). If there is no parent plane, NULL is returned.
         HMS\_AREngine\_ARPlane\_AcquireSubsumedBy(arSession, arPlane, &subsumePlane);
        if (subsumePlane != nullptr) {
            HMS\_AREngine\_ARTrackable\_Release(reinterpret\_cast<AREngine\_ARTrackable\*>(subsumePlane));
            // If the current plane has a parent plane, the current plane is not displayed. Otherwise, it will result in overlapping planes.
            continue;
        }
        // Perform plane drawing only when the tracking status is ARENGINE\_TRACKING\_STATE\_TRACKING.
        if (AREngine\_ARTrackingState::ARENGINE\_TRACKING\_STATE\_TRACKING != outTrackingState) {
            continue;
        }
        // Perform plane drawing.
    }
    HMS\_AREngine\_ARTrackableList\_Destroy(planeList);
    planeList = nullptr;
    
4.  Call [HMS\_AREngine\_ARPlane\_GetPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3537ce62e6a92dcdbddff0f39de0fae3) to obtain the plane's 2D vertex coordinate array for drawing the plane boundary.
    
    // Obtain the size of the 2D vertex coordinate array of the detected plane.
    int32\_t polygonLength = 0;
    HMS\_AREngine\_ARPlane\_GetPolygonSize(arSession, arPlane, &polygonLength);
    
    // Obtain the 2D vertex coordinate array of the detected plane, in the format of \[x1, z1, x2, z2, ...\].
    const int32\_t verticesSize = polygonLength / 2;
    std::vector<glm::vec2> raw\_vertices(verticesSize);
    HMS\_AREngine\_ARPlane\_GetPolygon(arSession, arPlane, glm::value\_ptr(raw\_vertices.front()), polygonLength);
    
    // Vertex coordinates in the local coordinate system.
    for (int32\_t i = 0; i < verticesSize; ++i) {
        vertices.emplace\_back(raw\_vertices\[i\].x, raw\_vertices\[i\].y, 0.75f);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Gm7IRvZ9SfuVkUMw8Fa8kA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=692E9FA7DBA364C80A02E535D32006CF5694D8EC12D239BC7F8BF88AD5855335)
    
    Call [HMS\_AREngine\_ARPlane\_GetPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3537ce62e6a92dcdbddff0f39de0fae3) to obtain the plane's 2D vertex coordinate array, in the format of \[x1, z1, x2, z2, ...\]. These values are defined in the x-z plane of the plane's local coordinate system and must be converted to the world coordinate system. To do this, call [HMS\_AREngine\_ARPlane\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gabbb03027afb984be8542d00d2eebd063) to obtain the pose data used for the conversion from the plane's local coordinate system to the world coordinate system, call [HMS\_AREngine\_ARPose\_GetMatrix](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga787f4daf9efd13c79737ef18cef6d7c7) to convert the pose data into a 4 x 4 matrix, and then multiply this matrix with the coordinates in the local coordinate system.
    
5.  Convert the plane's 2D vertex coordinates to the world coordinate system and draw the plane.
    
    // Obtain the pose information for the conversion from the plane's local coordinate system to the world coordinate system.
    AREngine\_ARPose \*scopedArPose = nullptr;
    HMS\_AREngine\_ARPose\_Create(arSession, nullptr, 0, &scopedArPose);
    HMS\_AREngine\_ARPlane\_GetCenterPose(arSession, arPlane, scopedArPose);
    
    // Convert the pose data into a 4 x 4 matrix. outMatrixColMajor4x4 is the array for storing the matrix, where data is stored in column-major order.
    // Multiply the matrix with the coordinates in the local coordinate system, to convert these coordinates to the world coordinate system.
    HMS\_AREngine\_ARPose\_GetMatrix(arSession, scopedArPose, glm::value\_ptr(modelMat), 16);
    HMS\_AREngine\_ARPose\_Destroy(scopedArPose);
    
    // Construct the data required for drawing the rendered plane.
    // Generate a triangle.
    for (int i = 1; i < verticesSize - 1; ++i) {
        triangles.push\_back(0);
        triangles.push\_back(i);
        triangles.push\_back(i + 1);
    }
    // Generate a plane bounding line.
    for (int i = 0; i < verticesSize; ++i) {
        lines.push\_back(i);
    }
    

## Tapping the Screen

1.  Obtain the screen coordinates based on the tap event after the user taps the screen. For details, please refer to [Native XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent).
    
    Add the header file: **native\_interface\_xcomponent.h**
    
    #include <ace/xcomponent/native\_interface\_xcomponent.h>
    
    Obtain the screen coordinates based on the tap event.
    
    float pixelX= 0.0f;
    float pixelY= 0.0f;
    int32\_t ret = OH\_NativeXComponent\_GetTouchEvent(component, window, &mTouchEvent);
    
    if (ret == OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
        if (mTouchEvent.type == OH\_NATIVEXCOMPONENT\_DOWN) {
            pixelX= mTouchEvent.touchPoints\[0\].x;
    	pixelY= mTouchEvent.touchPoints\[0\].y;
        } else {
    	return;
        }
    }
    
2.  Call [HMS\_AREngine\_ARFrame\_HitTest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9377f19261d5bbc2044497729b4e0df) to perform collision detection. The result is stored in the collision detection result list.
    
    // Create a list of hit testing result objects. arSession refers to the session object created in the step of creating an AR scene.
    AREngine\_ARHitResultList \*hitResultList = nullptr;
    HMS\_AREngine\_ARHitResultList\_Create(arSession, &hitResultList);
    
    // Obtain the list of hit testing result objects. arFrame refers to the frame object created in the step of creating an AR scene, and pixelX/pixelY refer to the coordinates of the point tapped on the screen.
    HMS\_AREngine\_ARFrame\_HitTest(arSession, arFrame, pixelX, pixelY, hitResultList);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/OsgyRh48QCq2J2xF_iNwsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C292E2170C2034955D734865CE827E78ECAAEA27ABBF62377BA9EAB0504A7836)
    
    Collision results are sorted by the distance from the intersection to the device, from nearest to farthest, and stored in a list of collision results.
    

## Placing a Virtual Object

1.  Call [HMS\_AREngine\_ARHitResultList\_GetItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf165c7a1c9ae003cac2a1c2ac2e5e5c4) to traverse the collision detection result list and obtain the hit trackable object.
    
    // Create a hit testing result object.
    AREngine\_ARHitResult \*arHit = nullptr;
    HMS\_AREngine\_ARHitResult\_Create(arSession, &arHit);
    
    // Obtain the first hit testing result object.
    HMS\_AREngine\_ARHitResultList\_GetItem(arSession, hitResultList, 0, arHit);
    
    // Obtain the trackable object that is hit.
    AREngine\_ARTrackable \*arHitTrackable = nullptr;
    HMS\_AREngine\_ARHitResult\_AcquireTrackable(arSession, arHit, &arHitTrackable);
    
2.  Determine whether the collision occurs within the plane.
    
    AREngine\_ARTrackableType ar\_trackable\_type = ARENGINE\_TRACKABLE\_INVALID;
    HMS\_AREngine\_ARTrackable\_GetType(arSession, arTrackable, &ar\_trackable\_type);
    if (ARENGINE\_TRACKABLE\_PLANE == ar\_trackable\_type) {
        AREngine\_ARPose \*arPose = nullptr;
        HMS\_AREngine\_ARPose\_Create(arSession, nullptr, 0, &arPose);
        HMS\_AREngine\_ARHitResult\_GetHitPose(arSession, arHit, arPose);
        // Check whether the pose is within the plane's bounding polygon. Value 0 indicates that it is out of the range, and other values indicate that it is within the range.
        HMS\_AREngine\_ARPlane\_IsPoseInPolygon(arSession, arPlane, arPose, &inPolygon);
        HMS\_AREngine\_ARPose\_Destroy(arPose);
        if (!inPolygon) {
    	// Skip the plane if the pose is out of the range.
    	continue;
        }
    }
    
3.  Create an anchor where the collision occurs and place the virtual model based on this anchor.
    
    // Create an anchor at the intersection.
    AREngine\_ARAnchor \*anchor = nullptr;
    HMS\_AREngine\_ARHitResult\_AcquireNewAnchor(arSession, arHitResult, &anchor);
    
    // Determine the tracking status of the anchor.
    AREngine\_ARTrackingState trackingState = ARENGINE\_TRACKING\_STATE\_STOPPED;
    HMS\_AREngine\_ARAnchor\_GetTrackingState(arSession, anchor, &trackingState);
    if (trackingState != ARENGINE\_TRACKING\_STATE\_TRACKING) {
        HMS\_AREngine\_ARAnchor\_Release(anchor);
        return;
    }
    
4.  Draw the model.
    
    Call [HMS\_AREngine\_ARAnchor\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad937acfc5d49f0909bdd84677bb0731a) to obtain the anchor pose and draw the virtual model based on this pose.
    
    // Obtain the anchor pose.
    AREngine\_ARPose \*pose = nullptr;
    HMS\_AREngine\_ARPose\_Create(arSession, nullptr, 0, &pose);
    HMS\_AREngine\_ARAnchor\_GetPose(arSession, anchor, pose);
    // Convert the pose data into a 4 x 4 matrix (modelMat).
    HMS\_AREngine\_ARPose\_GetMatrix(arSession, pose, glm::value\_ptr(modelMat), 16);
    HMS\_AREngine\_ARPose\_Destroy(pose);
    // Draw the virtual model.
    // Models can be drawn using OpenGL. For details, see the sample code world\_render\_manager.cpp and world\_object\_renderer.cpp.
