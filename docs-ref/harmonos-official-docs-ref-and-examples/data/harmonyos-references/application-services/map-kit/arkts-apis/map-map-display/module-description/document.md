# Module Description

The **map** module provides easy-to-use APIs that enable developers to seamlessly integrate map features to HarmonyOS apps or atomic services, including map display, overlay rendering, animation effects, interactive controls, map status updates, and a suite of utility functions.

This module provides the following functionalities:

-   [MapComponentController](../mapcomponentcontroller/document.md): displays maps and provides all map-related methods.

Map overlays:

-   [Marker](../marker/document.md): marker.
-   [MapPolyline](../mappolyline/document.md): polyline.
-   [MapArc](../maparc/document.md): arc.
-   [MapPolygon](../mappolygon/document.md): polygon.
-   [MapCircle](../mapcircle/document.md): circle.
-   [PointAnnotation](../pointannotation/document.md): point annotation.
-   [Bubble](../bubble/document.md): bubble.
-   [ClusterOverlay](../clusteroverlay/document.md): point cluster.
-   [ImageOverlay](../imageoverlay/document.md): image overlay.
-   [BuildingOverlay](../buildingoverlay/document.md): 3D building.
-   [TraceOverlay](../traceoverlay/document.md): trajectory tracking.
-   [TileOverlay](../tileoverlay/document.md): tile overlay.
-   [Heatmap](../heatmap/document.md): heatmap.
-   [MvtOverlay](../mvtoverlay/document.md): vector overlay.
-   [FlowFieldOverlay](../flowfieldoverlay/document.md): flow field overlay.
-   [MassPointOverlay](../masspointoverlay/document.md): massive point overlay.

Adding animations:

-   [Animation](../animation/document.md): animation abstract class.
-   [AlphaAnimation](../alphaanimation/document.md): animation class for controlling opacity.
-   [RotateAnimation](../rotateanimation/document.md): animation class for controlling rotation.
-   [ScaleAnimation](../scaleanimation/document.md): animation class for controlling scaling.
-   [TranslateAnimation](../translateanimation/document.md): animation class for controlling movement.
-   [FontSizeAnimation](../fontsizeanimation/document.md): animation class for controlling the font size.
-   [PlayImageAnimation](../playimageanimation/document.md): frame animation for controlling multiple images.
-   [AnimationSet](../animationset/document.md): animation class set.

Map interaction:

-   [MapEventManager](../mapeventmanager/document.md): map listening event manager.

Map status updates:

-   [newLatLng](../newlatlng/document.md): sets the map center and zoom level.
-   [newLatLngBounds](../newlatlngbounds/document.md): sets the map's longitude and latitude extent as well as the padding between the map region and map edges.
-   [scrollBy](../scrollby/document.md): moves the map center point by pixel.
-   [zoomBy](../zoomby/document.md): zooms in or out on the map by a specified value with the specified pixel point as the center.
-   [zoomIn](../zoomin/document.md): zooms in on the map by 1 level.
-   [zoomOut](../zoomout/document.md): zooms out on the map by 1 level.
-   [zoomTo](../zoomto/document.md): sets the zoom level of the map.

Common utility functions:

-   [calculateDistance](../calculatedistance/document.md): calculates the distance between coordinate points.
-   [convertCoordinate](../convertcoordinate/document.md): converts coordinate systems. This API uses a promise to return the result asynchronously.
-   [convertCoordinateSync](../convertcoordinatesync/document.md): converts coordinate systems
-   [rectifyCoordinate](../rectifycoordinate/document.md): checks whether the input coordinates need to be rectified based on the input coordinates, input coordinate system, and obtained current route location.

#### Module Import

import { map } from '@kit.MapKit';
