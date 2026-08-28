# How do I listen for screen rotation?

To listen for screen rotation events, use the media query API. The sample code is as follows:

import { mediaquery, UIContext } from '@kit.ArkUI';
const context = AppStorage.get("context") as UIContext;
let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen for landscape screen events
function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register callback
listener.off('change', onPortrait) // Unregister callback

**Reference**

[@ohos.mediaquery (Media Query)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-mediaquery)
