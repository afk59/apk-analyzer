# Use Cases

#### Typical Scenarios

The location-based recommendation capability powered by Huawei's Intents Kit primarily supports high-certainty scenarios such as indoor recommendations, outdoor proximity–based recommendations, and cross-regional recommendations. Combined with Huawei's intelligent decision-making capabilities, it delivers more personalized, timely, and user-centric scenario-specific widgets through smart entry points like Celia Suggestions.

| 
Recommendation Type

 | 

Capability

 | 

Scenario

 |
| :-- | :-- | :-- |
| 

Indoor recommendations

 | 

Implemented based on:

-   WLAN fingerprinting
-   Cell-based positioning
-   Beacon-based positioning

Geofence sensing is triggered when users enter locations such as stores or stadiums, enabling precise indoor positioning.

 | 

Applicable to high-precision indoor positioning scenarios across multiple floors and in confined areas, such as food outlets, museums, stadiums, hospital departments, banks, government service centers, and subway stations.

 |
| 

Outdoor proximity–based recommendations

 | 

Implemented based on:

-   POI-based polygon geofence
-   POI + radius
-   Beacon-based positioning

Geofence sensing is triggered when users approach or enter specific zones.

 | 

Applicable to outdoor scenarios, such as business districts, scenic spots, hospitals, airports, train stations, gas stations, and parking lots.

 |
| 

Cross-regional recommendations

 | 

Geofence sensing is triggered when users cross cities or countries/regions, based on city- or country/region-level geofences, enabling cross-regional location awareness.

 | 

Applicable to cross-city and cross-country/region scenarios, for example, providing travel tips when a user arrives in another city.

 |

#### Widget Display Effect

For location-based recommendations triggered by points of interest (POIs) and Bluetooth beacons, the proximity-based service provides a configuration entry to template-based widgets. After obtaining the proximity-based service permission, you can configure these widgets independently.

For location-based recommendations triggered by WLAN fingerprinting and cell-based positioning, Intents Kit offers standard widget templates, and these widgets will be configured by Huawei.
