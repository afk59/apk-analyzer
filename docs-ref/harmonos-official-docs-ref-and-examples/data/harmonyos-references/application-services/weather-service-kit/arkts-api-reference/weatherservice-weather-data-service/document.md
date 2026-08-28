# weatherService (Weather Data Service)

This module provides the weather data service.

**Start version**: 5.0.0(12)

#### Module Import

import { weatherService } from '@kit.WeatherServiceKit';

#### weatherService.getWeather

getWeather(request: WeatherRequest): Promise<Weather>

Obtains weather data. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

**Parameter**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

request

 | 

[WeatherRequest](#section1992347172717)

 | 

Yes

 | 

Weather data request body.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Weather](#section157006480227)\>

 | 

Promise that returns the weather data object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1011900001](../arkts-api-error-codes/document.md#section19421613172910)

 | 

Capability is not configured.

 |
| 

[1011900002](../arkts-api-error-codes/document.md#section1210612513414)

 | 

The requested longitude and latitude grid point lacks data.

 |
| 

[1011900003](../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error.

 |
| 

[1011900004](../arkts-api-error-codes/document.md#section673773124213)

 | 

System error.

 |

**Example**:

// Import required modules.
import { weatherService } from '@kit.WeatherServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Initialize parameters.
let request: weatherService.WeatherRequest = {
  location: {
    latitude: 22.62,
    longitude: 114.07
  },
    // Specify the data you need to request. If this parameter is not set, all data supported will be returned by default.
  limitedDatasets: \[weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS\]
}

// Request and error handling.
try {
  let weather = await weatherService.getWeather(request);
  if (weather.current) {
    console.info('getWeather current temperature: ' + weather.current.temperature);
  }
  if (weather.alerts?.length) {
    console.info('getWeather alert: ' + weather.alerts\[0\].title);
  }
} catch (err) {
  err = err as BusinessError;
  console.error(\`getWeather failed. Code: ${err.code}, message: ${err.message}\`);
}

#### weatherService.getWeatherWithContext

getWeatherWithContext(context: common.Context, request: WeatherRequest): Promise<Weather>

Obtains weather data based on the context provided by the caller. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.2(14)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

Context. Currently, the options are [UIAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

 |
| 

request

 | 

[WeatherRequest](#section1992347172717)

 | 

Yes

 | 

Weather data request body.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Weather](#section157006480227)\>

 | 

Promise that returns the weather data object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1011900001](../arkts-api-error-codes/document.md#section19421613172910)

 | 

Capability is not configured.

 |
| 

[1011900002](../arkts-api-error-codes/document.md#section1210612513414)

 | 

The requested longitude and latitude grid point lacks data.

 |
| 

[1011900003](../arkts-api-error-codes/document.md#section140917121405)

 | 

Network error.

 |
| 

[1011900004](../arkts-api-error-codes/document.md#section673773124213)

 | 

System error.

 |

**Example**:

// Import required modules.
import { UIAbility } from '@kit.AbilityKit';
import { weatherService } from '@kit.WeatherServiceKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function getWeatherData(context: common.Context) {
  let request: weatherService.WeatherRequest = {
    location: {
      latitude: 22.62,
      longitude: 114.07
    },
    // Specify the data you need to request. If this parameter is not set, all data supported will be returned by default.
    limitedDatasets: \[weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS\]
  }

  // Request.
  let weather = await weatherService.getWeatherWithContext(context, request);

  // Request and error handling.
  try {
    if (weather.current) {
      console.info('getWeatherWithContext current temperature: ' + weather.current.temperature);
    }
    if (weather.alerts?.length) {
      console.info('getWeatherWithContext alert: ' + weather.alerts\[0\].title);
    }
  } catch (err) {
    err = err as BusinessError;
    console.error(\`getWeatherWithContext failed. Code: ${err.code}, message: ${err.message}\`);
  }
}

function executeGetWeather(context: common.Context) {
  taskpool.execute(getWeatherData, context);
}

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    executeGetWeather(this.context);
  }
}

#### WeatherRequest

Weather data request class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

location

 | 

[Location](#section188316932819)

 | 

No

 | 

No

 | 

Location information.

 |
| 

limitedDatasets

 | 

[Dataset](#section83091727192814)\[\]

 | 

No

 | 

Yes

 | 

Data type array. Only the data of the specified types is returned. If this parameter is not set or the array is empty, all data supported is returned by default.

 |

#### Location

Location information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

latitude

 | 

number

 | 

No

 | 

No

 | 

Latitude.

Value range: \[-90, 90\]

 |
| 

longitude

 | 

number

 | 

No

 | 

No

 | 

Longitude.

Value range: \[-180, 180\]

 |

#### Weather

Weather data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

current

 | 

[CurrentWeather](#section0966121642920)

 | 

No

 | 

Yes

 | 

Real-time weather. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).CURRENT.

 |
| 

daily

 | 

[Forecast](#section1528522182918)<[DailyWeather](#section123711629162919)\>

 | 

No

 | 

Yes

 | 

Multi-day weather forecasts. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).DAILY.

 |
| 

hourly

 | 

[Forecast](#section1528522182918)<[HourlyWeather](#section0211544202918)\>

 | 

No

 | 

Yes

 | 

Hourly weather forecast. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).HOURLY.

 |
| 

minute

 | 

[Forecast](#section1528522182918)<[MinuteWeather](#section938117524293)\>

 | 

No

 | 

Yes

 | 

Minutely precipitation forecast. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).MINUTE or there is no precipitation in the area in the short term.

 |
| 

alerts

 | 

[WeatherAlert](#section8376165133019)\[\]

 | 

No

 | 

Yes

 | 

Weather alert. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).ALERTS or there is no alert in the area currently.

 |
| 

indices

 | 

[WeatherIndex](#section1635416963019)\[\]

 | 

No

 | 

Yes

 | 

Weather index. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).INDICES.

 |
| 

tides

 | 

[Tide](#section1082471633017)\[\]

 | 

No

 | 

Yes

 | 

Tide. No data is returned if the value of **limitedDatasets** does not contain [Dataset](#section83091727192814).TIDES or there is no tidal station in the area.

 |
| 

metadata

 | 

[WeatherMetadata](#section19686182312309)

 | 

No

 | 

No

 | 

Weather metadata.

 |
| 

attributions

 | 

[WeatherAttribution](#section7105153453010)\[\]

 | 

No

 | 

No

 | 

Attribution of weather data.

 |

#### CurrentWeather

Real-time weather data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

temperature

 | 

number

 | 

No

 | 

No

 | 

Temperature.

Unit: °C

 |
| 

apparentTemperature

 | 

number

 | 

No

 | 

No

 | 

Apparent temperature.

Unit: °C

 |
| 

humidity

 | 

number

 | 

No

 | 

No

 | 

Relative humidity.

For example, if the humidity is 30%, the value **30** is returned.

 |
| 

pressure

 | 

number

 | 

No

 | 

No

 | 

Surface pressure.

Unit: hPa

 |
| 

pressureTrend

 | 

[PressureTrend](#section69911219313)

 | 

No

 | 

No

 | 

Pressure tendency.

 |
| 

wind

 | 

[Wind](#section2353114611314)

 | 

No

 | 

No

 | 

Wind strength and direction.

 |
| 

cloudCover

 | 

number

 | 

No

 | 

No

 | 

Cloud cover.

For example, if the cloud cover is 30%, the value **30** is returned.

 |
| 

condition

 | 

[WeatherCondition](#section10699512153212)

 | 

No

 | 

No

 | 

Weather phenomenon.

 |
| 

uvIndex

 | 

[UVIndex](#section7981132253218)

 | 

No

 | 

No

 | 

UV index.

 |
| 

aqi

 | 

[WeatherAqi](#section10621192719325)

 | 

No

 | 

Yes

 | 

Air quality.

 |
| 

visibility

 | 

number

 | 

No

 | 

No

 | 

Visibility.

Unit: km

 |
| 

updateTime

 | 

Date

 | 

No

 | 

No

 | 

Data update time in UTC.

 |
| 

expirationTime

 | 

Date

 | 

No

 | 

No

 | 

Data expiration time in UTC.

 |
| 

summary

 | 

string

 | 

No

 | 

Yes

 | 

Brief description of the real-time weather.

 |

#### Forecast<T>

Set of weather forecast data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

forecast

 | 

T\[\]

 | 

No

 | 

No

 | 

Forecast data set.

 |
| 

updateTime

 | 

Date

 | 

No

 | 

No

 | 

Data update time in UTC.

 |
| 

expirationTime

 | 

Date

 | 

No

 | 

No

 | 

Data expiration time in UTC.

 |
| 

summary

 | 

string

 | 

No

 | 

Yes

 | 

Brief description of the forecast data. The parameter value is returned only for minute-level precipitation forecast.

 |

#### DailyWeather

Multi-day weather data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

date

 | 

Date

 | 

No

 | 

No

 | 

Date of each day in UTC.

 |
| 

highTemperature

 | 

number

 | 

No

 | 

No

 | 

High temperature.

Unit: °C

 |
| 

lowTemperature

 | 

number

 | 

No

 | 

No

 | 

Low temperature.

Unit: °C

 |
| 

highApparentTemperature

 | 

number

 | 

No

 | 

No

 | 

High apparent temperature.

Unit: °C

 |
| 

lowApparentTemperature

 | 

number

 | 

No

 | 

No

 | 

Low apparent temperature.

Unit: °C

 |
| 

uvIndex

 | 

[UVIndex](#section7981132253218)

 | 

No

 | 

No

 | 

UV index.

 |
| 

aqi

 | 

[WeatherAqi](#section10621192719325)

 | 

No

 | 

Yes

 | 

Air quality.

 |
| 

visibility

 | 

number

 | 

No

 | 

No

 | 

Visibility.

Unit: km

 |
| 

moon

 | 

[MoonEvents](#section1446317353338)

 | 

No

 | 

No

 | 

Information such as moonrise/moonset time and moon phase.

 |
| 

sun

 | 

[SunEvents](#section1799124063311)

 | 

No

 | 

No

 | 

Sunrise/Sunset time.

 |
| 

daytimeForecast

 | 

[DayPartForecast](#section165511045173319)

 | 

No

 | 

No

 | 

Daytime weather data.

 |
| 

overnightForecast

 | 

[DayPartForecast](#section165511045173319)

 | 

No

 | 

No

 | 

Data of weather at night.

 |
| 

pressure

 | 

number

 | 

No

 | 

No

 | 

Surface pressure.

Unit: hPa

 |

#### HourlyWeather

Hourly weather data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

date

 | 

Date

 | 

No

 | 

No

 | 

Date in UTC, accurate to hour.

 |
| 

temperature

 | 

number

 | 

No

 | 

No

 | 

Temperature.

Unit: °C

 |
| 

apparentTemperature

 | 

number

 | 

No

 | 

No

 | 

Apparent temperature.

Unit: °C

 |
| 

humidity

 | 

number

 | 

No

 | 

No

 | 

Relative humidity.

For example, if the humidity is 30%, the value **30** is returned.

 |
| 

wind

 | 

[Wind](#section2353114611314)

 | 

No

 | 

No

 | 

Wind strength and direction.

 |
| 

cloudCover

 | 

number

 | 

No

 | 

No

 | 

Cloud cover.

For example, if the cloud cover is 30%, the value **30** is returned.

 |
| 

condition

 | 

[WeatherCondition](#section10699512153212)

 | 

No

 | 

No

 | 

Weather phenomenon.

 |
| 

uvIndex

 | 

[UVIndex](#section7981132253218)

 | 

No

 | 

No

 | 

UV level.

 |
| 

aqi

 | 

[WeatherAqi](#section10621192719325)

 | 

No

 | 

Yes

 | 

Air quality.

 |
| 

visibility

 | 

number

 | 

No

 | 

No

 | 

Visibility.

Unit: km

 |
| 

precipitationProbability

 | 

number

 | 

No

 | 

No

 | 

Precipitation probability.

 |
| 

precipitationAmount

 | 

number

 | 

No

 | 

No

 | 

Amount of precipitation.

Unit: mm

 |

#### MinuteWeather

Minutely precipitation data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

date

 | 

Date

 | 

No

 | 

No

 | 

Date in UTC, accurate to minute.

 |
| 

precipitation

 | 

[Precipitation](#section56681655183416)

 | 

No

 | 

No

 | 

Precipitation type.

 |
| 

precipitationIntensity

 | 

number

 | 

No

 | 

No

 | 

Precipitation density.

Value range: \[0, 1\]

 |

#### WeatherAlert

Weather alert class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

updateTime

 | 

Date

 | 

No

 | 

No

 | 

Data update time in UTC.

 |
| 

expirationTime

 | 

Date

 | 

No

 | 

No

 | 

Data expiration time in UTC.

 |
| 

id

 | 

string

 | 

No

 | 

No

 | 

Alert ID.

 |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Alert title.

 |
| 

region

 | 

string

 | 

No

 | 

Yes

 | 

Alert area.

 |
| 

level

 | 

[AlertLevel](#section1696618143515)

 | 

No

 | 

No

 | 

Alert level.

 |
| 

levelDescription

 | 

string

 | 

No

 | 

No

 | 

Warning level description.

 |
| 

type

 | 

[AlertType](#section162382144356)

 | 

No

 | 

No

 | 

Alert type.

 |
| 

typeDescription

 | 

string

 | 

No

 | 

No

 | 

Alert type description.

 |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Main body of the alert.

 |
| 

guide

 | 

string

 | 

No

 | 

Yes

 | 

Safety guide for the alert.

 |
| 

detailsUrl

 | 

string

 | 

No

 | 

Yes

 | 

Link to the alert details.

 |
| 

source

 | 

string

 | 

No

 | 

No

 | 

Alert source.

 |
| 

icon

 | 

[resourceManager.Resource](../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9)

 | 

No

 | 

Yes

 | 

Alert icon.

 |

#### WeatherIndex

Weather index data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

updateTime

 | 

Date

 | 

No

 | 

No

 | 

Data update time in UTC.

 |
| 

expirationTime

 | 

Date

 | 

No

 | 

No

 | 

Data expiration time in UTC.

 |
| 

type

 | 

[WeatherIndexType](#section13240134383517)

 | 

No

 | 

No

 | 

Index type.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Index name.

 |
| 

dailyItems

 | 

[DailyIndex](#section1130118559352)\[\]

 | 

No

 | 

No

 | 

Daily index details.

 |

#### Tide

Tide data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

updateTime

 | 

Date

 | 

No

 | 

No

 | 

Data update time in UTC.

 |
| 

expirationTime

 | 

Date

 | 

No

 | 

No

 | 

Data expiration time in UTC.

 |
| 

stationId

 | 

string

 | 

No

 | 

No

 | 

Tide station ID.

 |
| 

stationName

 | 

string

 | 

No

 | 

No

 | 

Tide station name.

 |
| 

hourlyTides

 | 

[HourlyTide](#section1911611318363)\[\]

 | 

No

 | 

No

 | 

Hourly tide data.

 |

#### WeatherMetadata

Weather metadata class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestTime

 | 

Date

 | 

No

 | 

No

 | 

API request time in UTC.

 |
| 

version

 | 

string

 | 

No

 | 

No

 | 

Weather Service Kit version.

 |
| 

timeZone

 | 

string

 | 

No

 | 

Yes

 | 

Time zone of the location to be queried.

 |

#### WeatherAttribution

Weather data attribution class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

serviceName

 | 

string

 | 

No

 | 

No

 | 

Name of a data provider.

 |
| 

legalPageUrl

 | 

string

 | 

No

 | 

No

 | 

Attribution page URL.

 |

#### Wind

Class of wind strength and direction data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

direction

 | 

[CompassDirection](#section415174943216)

 | 

No

 | 

No

 | 

Wind direction.

 |
| 

speed

 | 

number

 | 

No

 | 

No

 | 

Wind speed.

Unit: km/h

 |
| 

level

 | 

number

 | 

No

 | 

No

 | 

Wind scale.

 |
| 

gustDirection

 | 

[CompassDirection](#section415174943216)

 | 

No

 | 

Yes

 | 

Wind gust direction.

 |
| 

gustSpeed

 | 

number

 | 

No

 | 

Yes

 | 

Wind gust speed.

Unit: km/h

 |
| 

gustLevel

 | 

number

 | 

No

 | 

Yes

 | 

Wind gust scale.

 |

#### WeatherCondition

Weather phenomenon data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[ConditionType](#section1715644153214)

 | 

No

 | 

No

 | 

Type of the weather phenomenon.

 |
| 

icon

 | 

[resourceManager.Resource](../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9)

 | 

No

 | 

No

 | 

Icon of the weather phenomenon.

 |
| 

description

 | 

string

 | 

No

 | 

No

 | 

Description of the weather phenomenon.

 |

#### UVIndex

UV index data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

category

 | 

[ExposureCategory](#section34333283311)

 | 

No

 | 

No

 | 

UV exposure category.

 |
| 

value

 | 

number

 | 

No

 | 

No

 | 

UV level.

 |
| 

description

 | 

string

 | 

No

 | 

No

 | 

UV level description.

 |

#### WeatherAqi

Air quality data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

no2

 | 

number

 | 

No

 | 

Yes

 | 

NO2 concentration.

Unit: μg/m3

 |
| 

o3

 | 

number

 | 

No

 | 

Yes

 | 

Ozone concentration.

Unit: μg/m3

 |
| 

pm10

 | 

number

 | 

No

 | 

Yes

 | 

PM10 concentration.

Unit: μg/m3

 |
| 

pm25

 | 

number

 | 

No

 | 

Yes

 | 

PM2.5 concentration.

Unit: μg/m3

 |
| 

so2

 | 

number

 | 

No

 | 

Yes

 | 

SO2 concentration.

Unit: μg/m3

 |
| 

co

 | 

number

 | 

No

 | 

Yes

 | 

CO concentration.

Unit: μg/m3

 |
| 

aqiValue

 | 

number

 | 

No

 | 

No

 | 

Numeric value of air quality.

 |
| 

aqiCategory

 | 

[AqiCategory](#section13959324356)

 | 

No

 | 

No

 | 

Air quality category.

 |
| 

aqiDescription

 | 

string

 | 

No

 | 

No

 | 

Air quality category description.

 |

#### MoonEvents

Class of information such as moonrise/moonset time and moon phase.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

moonrise

 | 

Date

 | 

No

 | 

No

 | 

Moonrise time in UTC.

 |
| 

moonset

 | 

Date

 | 

No

 | 

No

 | 

Moonset time in UTC.

 |
| 

phase

 | 

[MoonPhase](#section1559611811347)

 | 

No

 | 

No

 | 

Moon phase.

 |
| 

illuminatedFraction

 | 

number

 | 

No

 | 

Yes

 | 

Percent of the moon illuminated.

For example, if the precent is 30%, the value **30** is returned.

 |
| 

age

 | 

number

 | 

No

 | 

Yes

 | 

Moon's age.

 |

#### MoonPhase

Moon phase information class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[MoonPhaseType](#section01843323411)

 | 

No

 | 

No

 | 

Type of the moon phase.

 |
| 

description

 | 

string

 | 

No

 | 

No

 | 

Description of the moon phase.

 |
| 

icon

 | 

[resourceManager.Resource](../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9)

 | 

No

 | 

No

 | 

Moon phase icon.

 |

#### SunEvents

Sunrise/Sunset information class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sunrise

 | 

Date

 | 

No

 | 

No

 | 

Sunrise time in UTC.

 |
| 

sunset

 | 

Date

 | 

No

 | 

No

 | 

Sunset time in UTC.

 |

#### DayPartForecast

Class of weather information in certain time segments of a day.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

wind

 | 

[Wind](#section2353114611314)

 | 

No

 | 

No

 | 

Wind strength and direction.

 |
| 

humidity

 | 

number

 | 

No

 | 

No

 | 

Relative humidity.

For example, if the humidity is 30%, the value **30** is returned.

 |
| 

cloudCover

 | 

number

 | 

No

 | 

No

 | 

Cloud cover.

For example, if the cloud cover is 30%, the value **30** is returned.

 |
| 

condition

 | 

[WeatherCondition](#section10699512153212)

 | 

No

 | 

No

 | 

Weather phenomenon.

 |
| 

precipitationProbability

 | 

number

 | 

No

 | 

No

 | 

Precipitation probability.

 |
| 

precipitationAmount

 | 

number

 | 

No

 | 

No

 | 

Amount of precipitation.

Unit: mm

 |
| 

rainfallProbability

 | 

number

 | 

No

 | 

Yes

 | 

Rainfall probability.

 |
| 

rainfallAmount

 | 

number

 | 

No

 | 

Yes

 | 

Rainfall amount.

Unit: mm

 |
| 

snowfallProbability

 | 

number

 | 

No

 | 

Yes

 | 

Snowfall probability.

 |
| 

snowfallAmount

 | 

number

 | 

No

 | 

Yes

 | 

Snowfall amount.

Unit: mm

 |

#### DailyIndex

Class of daily weather index data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

date

 | 

Date

 | 

No

 | 

No

 | 

Date of each day in UTC.

 |
| 

level

 | 

number

 | 

No

 | 

No

 | 

Index level.

 |
| 

levelDescription

 | 

string

 | 

No

 | 

No

 | 

Index level description.

 |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Index content.

 |

#### HourlyTide

Hourly tide data class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

date

 | 

Date

 | 

No

 | 

No

 | 

Date in UTC, accurate to hour.

 |
| 

category

 | 

[TideCategory](#section6932142214363)

 | 

No

 | 

Yes

 | 

Tide type.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Tidal height.

Unit: cm

 |

#### Dataset

Enumerates datasets.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CURRENT

 | 

0

 | 

Real-time weather.

 |
| 

DAILY

 | 

1

 | 

Multi-day weather forecast.

 |
| 

HOURLY

 | 

2

 | 

Hourly weather forecast.

 |
| 

MINUTE

 | 

3

 | 

Minute-level precipitation forecast.

 |
| 

ALERTS

 | 

4

 | 

Weather alert.

 |
| 

INDICES

 | 

5

 | 

Weather index.

 |
| 

TIDES

 | 

6

 | 

Tide.

 |

#### PressureTrend

Enumerates the types of pressure tendency.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined type.

 |
| 

FALLING

 | 

1

 | 

Falling.

 |
| 

RISING

 | 

2

 | 

Rising.

 |
| 

STEADY

 | 

3

 | 

Stable.

 |

#### ConditionType

Enumerates weather phenomenon types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined type.

 |
| 

SUNNY

 | 

1

 | 

Sunny.

 |
| 

MOSTLY\_SUNNY

 | 

2

 | 

Cloudy.

 |
| 

PARTLY\_SUNNY

 | 

3

 | 

Cloudy.

 |
| 

INTERMITTENT\_CLOUDS

 | 

4

 | 

Cloudy.

 |
| 

HAZY\_SUNSHINE

 | 

5

 | 

Haze.

 |
| 

MOSTLY\_CLOUDY

 | 

6

 | 

Cloudy.

 |
| 

CLOUDY

 | 

7

 | 

Cloudy.

 |
| 

OVERCAST

 | 

8

 | 

Overcast.

 |
| 

FOG

 | 

11

 | 

Fog.

 |
| 

SHOWERS

 | 

12

 | 

Shower.

 |
| 

MOSTLY\_CLOUDY\_WITH\_SHOWERS

 | 

13

 | 

Shower.

 |
| 

PARTLY\_SUNNY\_WITH\_SHOWERS

 | 

14

 | 

Shower.

 |
| 

T\_STORMS

 | 

15

 | 

Thundershower.

 |
| 

MOSTLY\_CLOUDY\_WITH\_T\_STORMS

 | 

16

 | 

Thundershower.

 |
| 

PARTLY\_SUNNY\_WITH\_T\_STORMS

 | 

17

 | 

Thundershower.

 |
| 

RAIN

 | 

18

 | 

Rainy.

 |
| 

FLURRIES

 | 

19

 | 

Snow flurry.

 |
| 

MOSTLY\_CLOUDY\_WITH\_FLURRIES

 | 

20

 | 

Snow flurry.

 |
| 

PARTLY\_SUNNY\_WITH\_FLURRIES

 | 

21

 | 

Snow flurry.

 |
| 

SNOW

 | 

22

 | 

Snowy.

 |
| 

MOSTLY\_CLOUDY\_WITH\_SNOW

 | 

23

 | 

Snowy.

 |
| 

ICE

 | 

24

 | 

Snowy.

 |
| 

SLEET

 | 

25

 | 

Sleet.

 |
| 

FREEZING\_RAIN

 | 

26

 | 

Rainy.

 |
| 

RAIN\_AND\_SNOW

 | 

29

 | 

Sleet.

 |
| 

HOT

 | 

30

 | 

Hot.

 |
| 

COLD

 | 

31

 | 

Cold.

 |
| 

WINDY

 | 

32

 | 

Windy.

 |
| 

CLEAR

 | 

33

 | 

Sunny.

 |
| 

MOSTLY\_CLEAR

 | 

34

 | 

Cloudy.

 |
| 

PARTLY\_CLOUDY

 | 

35

 | 

Cloudy.

 |
| 

INTERMITTENT\_CLOUDS\_NIGHT

 | 

36

 | 

Cloudy.

 |
| 

HAZY\_MOONLIGHT

 | 

37

 | 

Haze.

 |
| 

MOSTLY\_CLOUDY\_NIGHT

 | 

38

 | 

Cloudy.

 |
| 

PARTLY\_CLOUDY\_WITH\_SHOWERS

 | 

39

 | 

Shower.

 |
| 

MOSTLY\_CLOUDY\_WITH\_SHOWERS\_NIGHT

 | 

40

 | 

Shower.

 |
| 

PARTLY\_CLOUDY\_WITH\_T\_STORMS

 | 

41

 | 

Thundershower.

 |
| 

MOSTLY\_CLOUDY\_WITH\_T\_STORMS\_NIGHT

 | 

42

 | 

Thundershower.

 |
| 

MOSTLY\_CLOUDY\_WITH\_FLURRIES\_NIGHT

 | 

43

 | 

Snow flurry.

 |
| 

MOSTLY\_CLOUDY\_WITH\_SNOW\_NIGHT

 | 

44

 | 

Snowy.

 |
| 

THUNDERSHOWER\_WITH\_HAIL

 | 

45

 | 

Hail.

 |
| 

LIGHT\_RAIN

 | 

46

 | 

Light rain.

 |
| 

MODERATE\_RAIN

 | 

47

 | 

Moderate rain.

 |
| 

HEAVY\_RAIN

 | 

48

 | 

Heavy rain.

 |
| 

STORM

 | 

49

 | 

Rainstorm.

 |
| 

HEAVY\_STORM

 | 

50

 | 

Rainstorm.

 |
| 

SEVERE\_STORM

 | 

51

 | 

Severe rainstorm.

 |
| 

LIGHT\_SNOW

 | 

52

 | 

Snow flurry.

 |
| 

MODERATE\_SNOW

 | 

53

 | 

Moderate snow.

 |
| 

HEAVY\_SNOW

 | 

54

 | 

Heavy snow.

 |
| 

SNOWSTORM

 | 

55

 | 

Snowstorm.

 |
| 

DUST\_STORM

 | 

56

 | 

Sandstorm.

 |
| 

LIGHT\_TO\_MODERATE\_RAIN

 | 

57

 | 

Moderate rain.

 |
| 

MODERATE\_TO\_HEAVY\_RAIN

 | 

58

 | 

Heavy rain.

 |
| 

HEAVY\_RAIN\_TO\_STORM

 | 

59

 | 

Rainstorm.

 |
| 

STORM\_TO\_HEAVY\_STORM

 | 

60

 | 

Rainstorm.

 |
| 

HEAVY\_TO\_SEVERE\_STORM

 | 

61

 | 

Severe rainstorm.

 |
| 

LIGHT\_TO\_MODERATE\_SNOW

 | 

62

 | 

Moderate snow.

 |
| 

MODERATE\_TO\_HEAVY\_SNOW

 | 

63

 | 

Heavy snow.

 |
| 

HEAVY\_SNOW\_TO\_SNOWSTORM

 | 

64

 | 

Snowstorm.

 |
| 

DUST

 | 

65

 | 

Dust blow.

 |
| 

SAND

 | 

66

 | 

Sand blow.

 |
| 

SANDSTORM

 | 

67

 | 

Severe sandstorm.

 |
| 

DENSE\_FOGGY

 | 

68

 | 

Fog.

 |
| 

MODERATE\_FOGGY

 | 

69

 | 

Fog.

 |
| 

MODERATE\_HAZE

 | 

70

 | 

Haze.

 |
| 

HEAVY\_HAZE

 | 

71

 | 

Haze.

 |
| 

SEVERE\_HAZE

 | 

72

 | 

Haze.

 |
| 

HEAVY\_FOGGY

 | 

73

 | 

Fog.

 |
| 

SEVERE\_FOGGY

 | 

74

 | 

Fog.

 |
| 

OVERCAST\_NIGHT

 | 

75

 | 

Overcast.

 |
| 

BLOWING\_SNOW

 | 

76

 | 

Snow flurry.

 |

#### CompassDirection

Enumerates compass directions.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined direction.

 |
| 

NORTH

 | 

1

 | 

North.

 |
| 

NORTH\_EAST

 | 

2

 | 

Northeast.

 |
| 

EAST

 | 

3

 | 

East.

 |
| 

SOUTH\_EAST

 | 

4

 | 

Southeast.

 |
| 

SOUTH

 | 

5

 | 

South.

 |
| 

SOUTH\_WEST

 | 

6

 | 

Southwest.

 |
| 

WEST

 | 

7

 | 

West.

 |
| 

NORTH\_WEST

 | 

8

 | 

Northwest.

 |

#### ExposureCategory

Enumerates the UV exposure levels.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined level.

 |
| 

VERY\_LOW

 | 

1

 | 

Weakest.

 |
| 

LOW

 | 

2

 | 

Weak.

 |
| 

MODERATE

 | 

3

 | 

Moderate.

 |
| 

HIGH

 | 

4

 | 

Strong.

 |
| 

VERY\_HIGH

 | 

5

 | 

Very strong.

 |

#### MoonPhaseType

Enumerates moon phase categories.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined category.

 |
| 

NEW

 | 

1

 | 

New moon.

 |
| 

WAXING\_CRESCENT

 | 

2

 | 

Waxing crescent

 |
| 

FIRST\_QUARTER

 | 

3

 | 

First quarter moon.

 |
| 

WAXING\_GIBBOUS

 | 

4

 | 

Waxing gibbous moon.

 |
| 

FULL

 | 

5

 | 

Full moon.

 |
| 

WANING\_GIBBOUS

 | 

6

 | 

Waxing gibbous moon.

 |
| 

LAST\_QUARTER

 | 

7

 | 

Last quarter moon.

 |
| 

WANING\_CRESCENT

 | 

8

 | 

Waning crescent.

 |

#### Precipitation

Enumerates precipitation types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

No precipitation.

 |
| 

HAIL

 | 

1

 | 

Hail.

 |
| 

RAIN

 | 

2

 | 

Rain.

 |
| 

SLEET

 | 

3

 | 

Sleet.

 |
| 

SNOW

 | 

4

 | 

Snow.

 |

#### AlertLevel

Enumerates alert levels.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BLUE

 | 

1

 | 

Blue alert.

 |
| 

YELLOW

 | 

2

 | 

Yellow alert.

 |
| 

ORANGE

 | 

3

 | 

Orange alert.

 |
| 

RED

 | 

4

 | 

Red alert.

 |
| 

OTHER

 | 

5

 | 

Other.

 |
| 

WHITE

 | 

6

 | 

White alert.

 |
| 

BLACK

 | 

7

 | 

Black alert.

 |

#### AlertType

Enumerates alert types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

TYPHOON

 | 

1

 | 

Typhoon.

 |
| 

RAIN\_STORM

 | 

2

 | 

Rainstorm.

 |
| 

SNOW\_STORM

 | 

3

 | 

Snowstorm.

 |
| 

COLD\_WAVE

 | 

4

 | 

Cold wave.

 |
| 

GALE

 | 

5

 | 

Gale.

 |
| 

SAND\_STORM

 | 

6

 | 

Sandstorm.

 |
| 

HEAT\_WAVE

 | 

7

 | 

High temperature.

 |
| 

DROUGHT

 | 

8

 | 

Drought.

 |
| 

LIGHTNING

 | 

9

 | 

Lightning.

 |
| 

HAIL

 | 

10

 | 

Hail.

 |
| 

FROST

 | 

11

 | 

Frost.

 |
| 

HEAVY\_FOG

 | 

12

 | 

Heavy fog.

 |
| 

HAZE

 | 

13

 | 

Haze.

 |
| 

ROAD\_ICING

 | 

14

 | 

Icy roads.

 |
| 

OTHER

 | 

15

 | 

Other.

 |
| 

THUNDER\_AND\_GALE

 | 

17

 | 

Lightning and gale.

 |
| 

FOREST\_FIRE\_RISK

 | 

18

 | 

Forest fire risk.

 |
| 

COLD

 | 

19

 | 

Cold.

 |
| 

DUST\_HAZE

 | 

20

 | 

Dust haze.

 |
| 

COOLING

 | 

21

 | 

Temperature drop.

 |
| 

ROAD\_ICE\_AND\_SNOW

 | 

22

 | 

Icy and snow-covered roads.

 |
| 

DRY\_HOT\_WIND

 | 

23

 | 

Dry-hot wind.

 |
| 

HAZE\_VERY\_UNHEALTHY

 | 

24

 | 

Severe air pollution.

 |
| 

FROZEN

 | 

25

 | 

Freezing.

 |
| 

HEAVY\_FOG\_AT\_SEA

 | 

26

 | 

Fog at sea.

 |
| 

THUNDERSTORM\_AND\_GALE

 | 

27

 | 

Thunderstorm and gale.

 |
| 

CONTINUOUS\_LOW\_TEMPERATURE

 | 

28

 | 

Continuous low temperature.

 |
| 

THICK\_DUST

 | 

29

 | 

Thick dust.

 |
| 

TORNADO

 | 

30

 | 

Tornado.

 |
| 

LOW\_TEMPERATURE\_FREEZE\_INJURY

 | 

31

 | 

Low temperature leading to freeze injury.

 |
| 

GALE\_AT\_SEA

 | 

32

 | 

Gale at sea.

 |
| 

LOW\_TEMPERATURE\_FREEZING\_RAIN\_AND\_SNOW

 | 

33

 | 

Freezing weather with rain and snow.

 |
| 

SEVERE\_CONVECTION

 | 

34

 | 

Severe convective storm.

 |
| 

OZONE

 | 

35

 | 

Ozone.

 |
| 

HEAVY\_SNOW

 | 

36

 | 

Heavy snow.

 |
| 

HEAVY\_RAINFALL

 | 

37

 | 

Torrential rain.

 |
| 

STRONG\_COOLING

 | 

38

 | 

Steep temperature drop.

 |
| 

SNOW\_DISASTER

 | 

39

 | 

Blizzard.

 |
| 

FOREST\_GRASSLAND\_FIRE\_RISK

 | 

40

 | 

Forrest (grassland) fire risk.

 |
| 

THUNDERSTORM

 | 

41

 | 

Thunderstorm.

 |
| 

SEVERE\_COLD

 | 

42

 | 

Extremely cold.

 |
| 

SAND\_DUST

 | 

43

 | 

Sand and dust.

 |
| 

THUNDERSTORM\_AND\_GALE\_AT\_SEA

 | 

44

 | 

T-storm and gale at sea.

 |
| 

LIGHTNING\_AT\_SEA

 | 

45

 | 

Lightning at sea.

 |
| 

TYPHOON\_AT\_SEA

 | 

46

 | 

Typhoon at sea.

 |
| 

LOW\_TEMPERATURE

 | 

47

 | 

Low temperature.

 |
| 

GEOLOGICAL\_HAZARD

 | 

48

 | 

Geological hazard.

 |
| 

GEOLOGICAL\_HAZARD\_AND\_METEOROLOGICAL\_RISK

 | 

49

 | 

Geological hazard and meteorological risk.

 |
| 

FLUSH\_FLOOD

 | 

50

 | 

Mountain torrent.

 |
| 

GRASSLAND\_FIRE\_RISK

 | 

51

 | 

Grassland fire risk.

 |
| 

THUNDER\_RAIN\_AND\_GALE

 | 

52

 | 

T-storm and gale.

 |

#### AqiCategory

Enumerates air quality categories.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined category.

 |
| 

EXCELLENT

 | 

1

 | 

Excellent.

 |
| 

GOOD

 | 

2

 | 

Good.

 |
| 

SLIGHT

 | 

3

 | 

Lightly polluted.

 |
| 

MODERATE

 | 

4

 | 

Moderately polluted.

 |
| 

HEAVY

 | 

5

 | 

Heavily polluted.

 |
| 

SEVERE

 | 

6

 | 

Severely polluted.

 |

#### WeatherIndexType

Enumerates weather index types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined type.

 |
| 

DRESSING

 | 

1

 | 

Dressing index.

 |
| 

MOTION

 | 

2

 | 

Workout index.

 |
| 

COLD

 | 

3

 | 

Cold index.

 |
| 

CAR\_WASHING

 | 

4

 | 

Car washing index.

 |
| 

TOURISM

 | 

5

 | 

Tourism index.

 |
| 

SUN\_PROTECTION

 | 

7

 | 

Sun protection index.

 |
| 

FISHING

 | 

8

 | 

Fishing index.

 |
| 

MORNING\_EXERCISE

 | 

10

 | 

Morning exercise index.

 |
| 

ALLERGY

 | 

24

 | 

Allergy index.

 |
| 

SKIING

 | 

31

 | 

Ski index.

 |
| 

STARGAZING

 | 

34

 | 

Stargazing index.

 |

#### TideCategory

Enumerates tide types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Weather.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNDEFINED

 | 

0

 | 

Undefined type.

 |
| 

HIGH

 | 

1

 | 

High tide.

 |
| 

LOW

 | 

2

 | 

Low tide.

 |
