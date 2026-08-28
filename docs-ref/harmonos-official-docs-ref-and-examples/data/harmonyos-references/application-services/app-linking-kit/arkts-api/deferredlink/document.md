# deferredLink

This module provides the deferred link capability of App Linking Kit. This capability enables the system to save an app link tapped by a user for 10 minutes. After the user downloads, installs, and opens the app, they can still access the link information.

**Start version**: 5.0.3(15)

#### Module Import

import { deferredLink } from '@kit.AppLinkingKit';

#### popDeferredLink

popDeferredLink(): Promise<string>

Obtains the information of an app link tapped by users previously from the system cache when the app is opened for the first time. The link can be obtained only once. After it is obtained, the system deletes the link from the cache. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.BundleManager.AppLinking.DeferredLink

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise used to return a deferred link.

 |

**Example**:

import { deferredLink } from '@kit.AppLinkingKit';  
import { hilog } from '@kit.PerformanceAnalysisKit';

// When the app is opened for the first time, obtain the app link tapped previously by the user.
deferredLink.popDeferredLink().then((link: string) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in getting deferred link, result: ${link}\`);
  // If the link is successfully obtained, it can redirect to the details screen based on the service logic that you define.
  if (link) {
    // Configure the service logic for redirecting the link to the details screen.
  }
}).catch(() => {
  // An unknown error has occurred.
  hilog.error(0x0000, 'testTag', \`Failed to get deferred link.\`);
})
