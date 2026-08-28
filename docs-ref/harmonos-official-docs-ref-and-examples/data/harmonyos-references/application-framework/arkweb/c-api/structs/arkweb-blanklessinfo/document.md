# ArkWeb\_BlanklessInfo

typedef struct {...} ArkWeb\_BlanklessInfo

#### Overview

Describes prediction information about blankless loading, including the first screen similarity, first screen loading duration, and error codes. The application determines whether to enable the blankless loading solution based on the prediction information.

**Since**: 20

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [native\_interface\_arkweb.h](../../header-files/native-interface-arkweb-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| ArkWeb\_BlanklessErrorCode errCode | Error codes of blankless loading. For details, see [ArkWeb\_BlanklessErrorCode](../../header-files/arkweb-error-code-h/document.md#arkweb_blanklesserrorcode). |
| double similarity | First screen similarity, which is calculated based on the historical first screen content. The value ranges from 0 to 1.0. 1.0 indicates that the content is the same. A value closer to 1 indicates a higher similarity. This value is lagging, and the similarity of the local loading is displayed in the next loading. You are advised not to enable the blankless loading frame insertion solution when the similarity is low. |
| int32\_t loadingTime | Loading duration estimated based on the historical first screen loading durations, in milliseconds. The value must be greater than 0. |
