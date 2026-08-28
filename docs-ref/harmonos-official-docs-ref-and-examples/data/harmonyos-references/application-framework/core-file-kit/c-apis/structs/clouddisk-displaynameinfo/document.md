# CloudDisk\_DisplayNameInfo

typedef struct CloudDisk\_DisplayNameInfo {...} CloudDisk\_DisplayNameInfo

#### Overview

A struct that encapsulates the display name of the sync root path.

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

**Header file**: [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t displayNameResId | Static resource ID corresponding to the display name of the application's sync root path. |
| char \*customAlias | Pointer to the custom alias, which cannot contain the following characters: \\/\*?<>|:". Additionally, the full name cannot be composed solely of spaces, a single dot (.), or two consecutive dots (..). |
| size\_t customAliasLength | Length of the custom alias. Value range: \[0, 255\]. |
