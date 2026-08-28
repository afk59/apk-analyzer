# About This Kit

Map Kit provides powerful and convenient map capabilities for developers, empowering global developers to effortlessly create customized map experiences by offering robust functions such as personalized map display, location search, and route planning. You can easily integrate map-related functions into HarmonyOS apps or atomic services to improve user experience.

Map Kit provides 320 million points of interest (POIs) worldwide. A POI on a map can be a store, an office building, a landmark, and so on.

Map Kit is constantly optimized to improve the level of detail in its maps. For example, in terms of POI and road network information display, users are presented with more relevant such information at different zoom levels based on POI attribute information and regional road network differences. Gestures including zoom, rotation, moving, and tilt are supported to ensure smooth interaction experience.

#### Use Cases

Sites in the Chinese mainland, Hong Kong (China), and Macao (China) use the GCJ02 coordinate system, and sites in Taiwan (China) and outside China use the WGS84 coordinate system. For details, please refer to [Coordinate Rectification](../map-calculation-tools/coordinate-rectification/document.md).

Map Kit provides the following functions, which can meet most map development requirements:

-   [Map Creation](../map-creation/document.md): Creates map components, sets map attributes, and customizes the map.
-   [Map Interaction](../map-interaction/document.md): Controls the interaction gestures and buttons on the map.
-   [Drawing on a Map](../drawing-on-a-map/document.md): Adds map elements such as location markers, overlays, and various shapes.
-   [Place Search](../place-search/document.md): Offers diverse POI query capabilities, forward geocoding, and reverse geocoding.
-   [Route Planning](../route-planning/document.md): Plans walking, cycling, and driving routes.
-   [Static Map](../static-map/document.md): Obtains a map image.
-   [Map Picker](../map-picker/document.md): Provides the place details display control, location selection control, and administrative division selection control.
-   [Navigation and Other Capabilities Provided by the Map App](../navigation-and-other-capabilities-provided-by-the-map-app/document.md): Provides capabilities including viewing location details, viewing route planning, initiating navigation, and initiating place search.
-   [Map Calculation Tools](../map-calculation-tools/document.md): Describes the two coordinate systems used in Map Kit, including their application regions and conversion methods.

#### Constraints

## Supported Countries/Regions

For details, please refer to [Supported Countries/Regions](../appendixes/supported-countries-regions/document.md).

## Supported Devices

This kit is applicable only to phones, tablets, PCs/2-in-1 devices, and wearables.

## Sample Code

Refer to the [sample code](https://gitcode.com/HarmonyOS_Samples/map-kit_-sample-code_-demo-arkts) of Map Kit for details.

#### Emulator Support

-   General differences: For details, please refer to [Differences Between the Emulator and the Real Device](../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section1227613205203).
-   Arm emulator: The functions in the **petalMaps** namespace and the my-location function are not supported.
-   x86 emulator: The functions in the **petalMaps** namespace, the my-location function, and watches are not supported.
