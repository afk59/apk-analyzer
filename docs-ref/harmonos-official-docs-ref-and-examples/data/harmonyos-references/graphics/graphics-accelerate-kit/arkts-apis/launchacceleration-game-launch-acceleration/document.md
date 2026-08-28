# launchAcceleration (Game Launch Acceleration)

This module provides the game launch acceleration capability.

**System capability**: SystemCapability.GraphicsGame.LaunchAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 6.0.0(20)

#### Module Import

import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

#### isLaunchMirrorEnabled

isLaunchMirrorEnabled(): boolean

Checks whether the memory snapshot function is enabled for the game.

**System capability**: SystemCapability.GraphicsGame.LaunchAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

The system determines whether to enable the memory snapshot function by considering the game's activity level, the number of existing memory snapshots, and the amount of memory swapped out to disk for the current day on the current device.

-   **true**: The memory snapshot function is enabled. The game switches to a specific scene (the game sign-in screen is recommended) and the system automatically creates a memory snapshot before the game exits. It takes about 4 seconds to create a memory snapshot.
-   **false**: The memory snapshot function is disabled. When a user exits the game, the system will directly terminate the game process.

The default value is **false**.

 |

**Example**:

import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

onWindowStageWillDestroy(): void {
    let enable = launchAcceleration.isLaunchMirrorEnabled()
    if (enable) {
        // Code logic for scene switching.
    }
}
