# deviceinfo.h

#### Overview

Declares the APIs for querying device information.

**File to include**: <deviceinfo.h>

**Library**: libdeviceinfo\_ndk.z.so

**System capability**: SystemCapability.Startup.SystemInfo

**Since**: 10

**Related modules**: [DeviceInfo](../../modules/deviceinfo/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [const char \*OH\_GetDeviceType(void)](#oh_getdevicetype) | Obtains the device type. |
| [const char \*OH\_GetManufacture(void)](#oh_getmanufacture) | Obtains the device manufacturer. |
| [const char \*OH\_GetBrand(void)](#oh_getbrand) | Obtains the device brand. |
| [const char \*OH\_GetMarketName(void)](#oh_getmarketname) | Obtains the market name. |
| [const char \*OH\_GetProductSeries(void)](#oh_getproductseries) | Obtains the product series. |
| [const char \*OH\_GetProductModel(void)](#oh_getproductmodel) | Obtains the product model. |
| [const char \*OH\_GetSoftwareModel(void)](#oh_getsoftwaremodel) | Obtains the software model. |
| [const char \*OH\_GetHardwareModel(void)](#oh_gethardwaremodel) | Obtains the hardware model. |
| [const char \*OH\_GetBootloaderVersion(void)](#oh_getbootloaderversion) | Obtains the Bootloader version. |
| [const char \*OH\_GetAbiList(void)](#oh_getabilist) | Obtains the application binary interface (ABI) list. |
| [const char \*OH\_GetSecurityPatchTag(void)](#oh_getsecuritypatchtag) | Obtains the security patch tag. |
| [const char \*OH\_GetDisplayVersion(void)](#oh_getdisplayversion) | Obtains the display version. |
| [const char \*OH\_GetIncrementalVersion(void)](#oh_getincrementalversion) | Obtains the incremental version. |
| [const char \*OH\_GetOsReleaseType(void)](#oh_getosreleasetype) | Obtains the OS release type. |
| [const char \*OH\_GetOSFullName(void)](#oh_getosfullname) | Obtains the OS full name. |
| [int OH\_GetSdkApiVersion(void)](#oh_getsdkapiversion) | Obtains the SDK API version. |
| [int OH\_GetFirstApiVersion(void)](#oh_getfirstapiversion) | Obtains the first API version. |
| [const char \*OH\_GetVersionId(void)](#oh_getversionid) | Obtains the version ID. |
| [const char \*OH\_GetBuildType(void)](#oh_getbuildtype) | Obtains the build type. |
| [const char \*OH\_GetBuildUser(void)](#oh_getbuilduser) | Obtains the build user. |
| [const char \*OH\_GetBuildHost(void)](#oh_getbuildhost) | Obtains the build host. |
| [const char \*OH\_GetBuildTime(void)](#oh_getbuildtime) | Obtains the build time. |
| [const char \*OH\_GetBuildRootHash(void)](#oh_getbuildroothash) | Obtains the build root hash. |
| [const char \*OH\_GetDistributionOSName(void)](#oh_getdistributionosname) | Obtains the ISV distribution OS name. Independent software vendors (ISVs) can use their own OS names. |
| [const char \*OH\_GetDistributionOSVersion(void)](#oh_getdistributionosversion) | Obtains the ISV distribution OS version. |
| [int OH\_GetDistributionOSApiVersion(void)](#oh_getdistributionosapiversion) | Obtains the ISV distribution OS API version. |
| [const char \*OH\_GetDistributionOSReleaseType(void)](#oh_getdistributionosreleasetype) | Obtains the ISV distribution OS release type. |

#### Function Description

#### \[h2\]OH\_GetDeviceType()

const char \*OH\_GetDeviceType(void)

**Description**

Obtains the device type.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char | 
Returns one of the following values:

**phone** (or **default**),

**wearable**,

**liteWearable**,

**tablet**,

**tv**,

**car**,

**smartVision**

 |

#### \[h2\]OH\_GetManufacture()

const char \*OH\_GetManufacture(void)

**Description**

Obtains the device manufacturer.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a device manufacturer. The value is of the string type. |

#### \[h2\]OH\_GetBrand()

const char \*OH\_GetBrand(void)

**Description**

Obtains the device brand.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a device brand. The value is of the string type. |

#### \[h2\]OH\_GetMarketName()

const char \*OH\_GetMarketName(void)

**Description**

Obtains the market name.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a market name. The value is of the string type. |

#### \[h2\]OH\_GetProductSeries()

const char \*OH\_GetProductSeries(void)

**Description**

Obtains the product series.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns the product series. The value is of the string type. |

#### \[h2\]OH\_GetProductModel()

const char \*OH\_GetProductModel(void)

**Description**

Obtains the product model.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a product model. The value is of the string type. |

#### \[h2\]OH\_GetSoftwareModel()

const char \*OH\_GetSoftwareModel(void)

**Description**

Obtains the software model.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a software model. The value is of the string type. |

#### \[h2\]OH\_GetHardwareModel()

const char \*OH\_GetHardwareModel(void)

**Description**

Obtains the hardware model.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a hardware model. The value is of the string type. |

#### \[h2\]OH\_GetBootloaderVersion()

const char \*OH\_GetBootloaderVersion(void)

**Description**

Obtains the Bootloader version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a Bootloader version. The value is of the string type. |

#### \[h2\]OH\_GetAbiList()

const char \*OH\_GetAbiList(void)

**Description**

Obtains the ABI list.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns an ABI list. The value is of the string type. |

#### \[h2\]OH\_GetSecurityPatchTag()

const char \*OH\_GetSecurityPatchTag(void)

**Description**

Obtains the security patch tag.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a security patch tag. The value is of the string type. |

#### \[h2\]OH\_GetDisplayVersion()

const char \*OH\_GetDisplayVersion(void)

**Description**

Obtains the display version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a display version. The value is of the string type. |

#### \[h2\]OH\_GetIncrementalVersion()

const char \*OH\_GetIncrementalVersion(void)

**Description**

Obtains the incremental version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns an incremental version. The value is of the string type. |

#### \[h2\]OH\_GetOsReleaseType()

const char \*OH\_GetOsReleaseType(void)

**Description**

Obtains the OS release type.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | 
Returns an OS release type. The options include **release**, **Beta**, and **Canary**.

A specific release type may be **release**, **Beta1**, or another similar type.

 |

#### \[h2\]OH\_GetOSFullName()

const char \*OH\_GetOSFullName(void)

**Description**

Obtains the OS full name.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns an OS full name. The value is of the string type. |

#### \[h2\]OH\_GetSdkApiVersion()

int OH\_GetSdkApiVersion(void)

**Description**

Obtains the SDK API version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns an SDK API version. |

#### \[h2\]OH\_GetFirstApiVersion()

int OH\_GetFirstApiVersion(void)

**Description**

Obtains the first API version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the first API version. |

#### \[h2\]OH\_GetVersionId()

const char \*OH\_GetVersionId(void)

**Description**

Obtains the version ID.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a version ID. The value is of the string type. |

#### \[h2\]OH\_GetBuildType()

const char \*OH\_GetBuildType(void)

**Description**

Obtains the build type.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a build type. The value is of the string type. |

#### \[h2\]OH\_GetBuildUser()

const char \*OH\_GetBuildUser(void)

**Description**

Obtains the build user.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a build user. The value is of the string type. |

#### \[h2\]OH\_GetBuildHost()

const char \*OH\_GetBuildHost(void)

**Description**

Obtains the build host.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a build host. The value is of the string type. |

#### \[h2\]OH\_GetBuildTime()

const char \*OH\_GetBuildTime(void)

**Description**

Obtains the build time.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns the build time. The value is of the string type. |

#### \[h2\]OH\_GetBuildRootHash()

const char \*OH\_GetBuildRootHash(void)

**Description**

Obtains the build root hash.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a build root hash. The value is of the string type. |

#### \[h2\]OH\_GetDistributionOSName()

const char \*OH\_GetDistributionOSName(void)

**Description**

Obtains the ISV distribution OS name. ISVs can use their own OS names.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | 
Returns an ISV distribution OS name.

If no ISV is specified, an empty string is returned.

 |

#### \[h2\]OH\_GetDistributionOSVersion()

const char \*OH\_GetDistributionOSVersion(void)

**Description**

Obtains the ISV distribution OS version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | 
Returns an ISV distribution OS version.

If no ISV is specified, the value of [OH\_GetOSFullName](#oh_getosfullname) is returned.

 |

#### \[h2\]OH\_GetDistributionOSApiVersion()

int OH\_GetDistributionOSApiVersion(void)

**Description**

Obtains the ISV distribution OS API version.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an ISV distribution OS API version.

If no ISV is specified, the value of [OH\_GetOSFullName](#oh_getosfullname) is returned.

 |

#### \[h2\]OH\_GetDistributionOSReleaseType()

const char \*OH\_GetDistributionOSReleaseType(void)

**Description**

Obtains the ISV distribution OS release type.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| const char | 
Returns an ISV distribution OS release type.

If no ISV is specified, the value of [OH\_GetOsReleaseType](#oh_getosreleasetype) is returned.

 |
