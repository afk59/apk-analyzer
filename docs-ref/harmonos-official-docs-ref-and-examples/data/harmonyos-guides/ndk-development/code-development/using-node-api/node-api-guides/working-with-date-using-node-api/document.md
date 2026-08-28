# Working with Date Using Node-API

#### Overview

Node-API provides APIs for processing ArkTS **Date** objects in C/C++. These APIs are useful for working with time- and date-related logic in the ArkTS module.

#### Basic Concepts

In Node-API, the value of a ArkTS **Date** object is the number of milliseconds elapsed since the Unix epoch (00:00:00 UTC on January 1, 1970).

The ArkTS **Date** object provides a way to represent and manage date and time in ArkTS. With the **Date** object, you can create an object that represents a specific time, perform date- and time-related calculations (such as adding or subtracting time intervals), and format date as a string for display.

With the functions for interacting with the **Date** object, the JSVM module can be closely integrated with the ArkTS environment to perform more complex date- and time-related operations.

#### Available APIs

The following table lists the APIs for manipulating ArkTS date in C/C++.

| API | Description |
| :-- | :-- |
| napi\_create\_date | Creates an ArkTS **Date** object. |
| napi\_get\_date\_value | Obtains the C equivalent of the given ArkTS **Date** object. |
| napi\_is\_date | Checks whether the given ArkTS value is a **Date** object. You can use this API to check the type of the parameter passed from ArkTS. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to promise development.

## napi\_create\_date

Use **napi\_create\_date** to create an ArkTS **Date** object from a C++ double value.

CPP code:

#include "napi/native\_api.h"

static napi\_value CreateDate(napi\_env env, napi\_callback\_info info)
{
    // Obtain the Unix timestamp passed in.
    double value = 1501924876711;
    // Call napi\_create\_date to convert the double value to an ArkTS object that indicates the date and time, and place the object in returnValue.
    napi\_value returnValue = nullptr;
    napi\_create\_date(env, value, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const createDate: () => Date;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_date: %{public}s', testNapi.createDate().toString());

## napi\_get\_date\_value

Use **napi\_get\_date\_value** to obtain the C++ double equivalent of the given ArkTS **Date** object.

CPP code:

#include <hilog/log.h>
#include "napi/native\_api.h"

static napi\_value GetDateValue(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Obtain the Unix timestamp passed in.
    double value = 0;
    napi\_status status = napi\_get\_date\_value(env, args\[0\], &value);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_get\_date\_value fail");
        return nullptr;
    }

    // Print the obtained Unix timestamp.
    OH\_LOG\_INFO(LOG\_APP, "Node-API gets unix time stamp is:%{public}lf.", value);

    // Convert the Unix timestamp to an ArkTS double value and put it in returnValue.
    napi\_value returnValue = nullptr;
    napi\_create\_double(env, value, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const getDateValue: (date: Date) => number | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  const date = new Date();
  hilog.info(0x0000, 'testTag', 'Node-API: output the Unix Time Stamp: %{public}d', date.getTime());
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_date\_value: %{public}d', testNapi.getDateValue(date));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_date\_value error: %{public}s', error.message);
}

## napi\_is\_date

Use **napi\_is\_date** to check whether an ArkTS value is an ArkTS **Date** object.

CPP code:

#include "napi/native\_api.h"

static napi\_value IsDate(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameter.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Call napi\_is\_date to check whether the input parameter is a Date object.
    bool result = false;
    napi\_status status = napi\_is\_date(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_date fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);

    return returnValue;
}

API declaration:

// index.d.ts
export const isDate: <T>(date: T) => boolean | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  let now: Date = new Date();
  let date = "123";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_date: %{public}s', testNapi.isDate(now));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_date: %{public}s', testNapi.isDate(date));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_date error: %{public}s', error.message);
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
