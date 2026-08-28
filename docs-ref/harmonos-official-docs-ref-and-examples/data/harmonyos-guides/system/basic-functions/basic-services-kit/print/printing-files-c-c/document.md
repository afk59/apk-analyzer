# Printing Files (C/C++)

HarmonyOS provides two printing methods:

[Method 1](#step-3-starting-the-print-preview-page-to-send-print-jobs): An application calls an API to start the system print preview page and sends a print job for the rendered PDF file to a printer. This method is applicable to applications that require printing functionality but for which developers do not wish to develop a preview page.

[Method 2](#step-4-discovering-and-connecting-to-printers-to-send-print-jobs): An application calls the print APIs to discover and connect to printers and sends print jobs. This method is applicable to applications that have a developed preview page. Applications can call APIs to discover printers, obtain the printer capabilities, and construct a print job.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/rivi6uAVRhmbEccnWlgPwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0BA9908AB402E59115C6282ADD32C6DE117D76FEE58BA33189F56CB072AE1DA)

To use the print service, declare the ohos.permission.PRINT permission. For details, see [Declaring Permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

When the print service is no longer used, call **OH\_Print\_Release()** to release the print client resources and cancel event subscription.

#### How to Develop

## Step 1: Including header files.

#include <cstdint>
#include <cstdio>
#include <cwchar>
#include <vector>
#include <string>
#include "hilog/log.h"
#include "napi/native\_api.h"
#include "BasicServicesKit/ohprint.h"

## Step 2: Adding Dynamic Link Libraries to the CMake Script

target\_link\_libraries(entry PUBLIC
    libace\_napi.z.so
    libhilog\_ndk.z.so
    libohprint.so
)

## Step 3: Starting the Print Preview Page to Send Print Jobs

import { Context } from '@kit.AbilityKit';
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
    build() {
        Button("call native")
            .onClick(() => {
                let ctx = this.getUIContext().getHostContext(); // Obtain the context of the ability.
                if (ctx === undefined) {
                    console.error('get fileUri or context failed');
                    return;
                }
                testNapi.SetContext(ctx);                                 // Pass the context to the C++ side.
            });
    }
}

// Send the print task to the printer through system.
static void\* g\_context;
static char\* g\_currentJobId;

// Initialize the print service.
Print\_ErrorCode ret = OH\_Print\_Init();

static napi\_value SetContext(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    // Assume that napi\_get\_cb\_info is returned properly.
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Save the context for future use.
    napi\_status ret = napi\_unwrap(env, argv\[0\], &g\_context);
    return nullptr;
}

// Invoke the callback of the system print preview page when the page is started for the first time or the user changes the print parameters.
static void StartLayoutWriteCb(const char \*jobId,
                                uint32\_t fd,
                                const Print\_PrintAttributes \*oldAttrs,
                                const Print\_PrintAttributes \*newAttrs,
                                Print\_WriteResultCallback writeCallback)
{
    // Cache the unique task ID.
    g\_currentJobId = jobId;
    // Implement WriteFile() to obtain the print parameters before and after modification, render the file to be printed, and write data using a fd, for example, color mode or page number.
    uint32\_t retCode = WriteFile(fd, oldAttrs, newAttrs);
    // Notify the system that the file has been written.
    writeCallback(jobId, retCode);
}

// After the file is written, the system displays the print preview page. You can click Print to send the print job.
// Callback used to listen for the print job state changes based on the task ID.
static void JobStateChangedCb(const char \*jobId, uint32\_t state)
{
    // Logic for managing the print job state based on the task ID.
}

// Call the print API to display the print preview page.
char printJobName\[\] = "fileName";
Print\_PrintDocCallback printDocCallback = { StartLayoutWriteCb, JobStateChangedCb };
Print\_ErrorCode ret = OH\_Print\_StartPrintByNative(printJobName, printDocCallback, g\_context);

// Release resources when the print service is no longer used.
OH\_Print\_Release()

## Step 4: Discovering and Connecting to Printers to Send Print Jobs

// Initialize the print service.
Print\_ErrorCode ret = OH\_Print\_Init();

// Register the callback for the printer discovery event and start discovering printers.
static void PrinterDiscoveryCallback(Print\_DiscoveryEvent event, const Print\_PrinterInfo \*printerInfo)
{
    // Discover a printer. The device ID is used as the unique identifier.
    if (printerInfo == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0, "print c/c++", "printerInfo is nullptr");
        return;
    }
    // Implement the following callback logic based on the specific service scenario.
    switch (event) {
        // An event indicating that a printer is discovered.
        case PRINTER\_DISCOVERED:
            OnPrinterDiscovered(printerInfo);
            break;
        // An event indicating that a printer is lost.
        case PRINTER\_LOST:
            OnPrinterLost(printerInfo);
            break;
        // An event indicating that a printer is connecting, which is triggered by OH\_Print\_ConnectPrinter.
        case PRINTER\_CONNECTING:
            OnPrinterConnecting(printerInfo);
            break;
        // An event indicating that a printer is connected, which is triggered by OH\_Print\_ConnectPrinter.
        case PRINTER\_CONNECTED:
            OnPrinterConnected(printerInfo);
            break;
        default:
            break;
    }
}
Print\_PrinterDiscoveryCallback callback = PrinterDiscoveryCallback;
Print\_ErrorCode ret = OH\_Print\_StartPrinterDiscovery(callback);

// Obtain the printer properties through PrinterDiscoveryCallback and connect to the printer based on the printer ID.
// After the connection is successful, the PRINTER\_CONNECTED event is received.
Print\_ErrorCode ret = OH\_Print\_ConnectPrinter(printerInfo->printerId);

// Stop device discovery when this feature is not required.
Print\_ErrorCode ret = OH\_Print\_StopPrinterDiscovery();

// Obtain the added printer list.
Print\_StringList addedPrinterList = {0};
Print\_ErrorCode ret = OH\_Print\_QueryPrinterList(&addedPrinterList);
for (uint32\_t index = 0; index < addedPrinterList.count; index++) {
    Print\_PrinterInfo \*printerInfo = nullptr;
    // Obtain the printer properties using the name of an added printer.
    ret = OH\_Print\_QueryPrinterInfo(addedPrinterList\[index\], &printerInfo);
    // Service code.
    // Release resources after the printer properties are used.
    OH\_Print\_ReleasePrinterInfo(printerInfo);
}
// Release the added printer list.
OH\_Print\_ReleasePrinterList(&addedPrinterList);

// Send a print job.
// This example uses printerInfo->defaultValue as the print job parameter to send the task.
std::vector<uint32\_t> fdList = { 44, 45 };
Print\_PrintJob\* printJob = new Print\_PrintJob{ jobName,
                                               fdList.data(),
                                               static\_cast<uint32\_t>(fdList.size()),
                                               printerInfo->printerId,
                                               1, // Number of copies.
                                               printerInfo->defaultValue.defaultPaperSource,
                                               printerInfo->defaultValue.defaultMediaType,
                                               printerInfo->defaultValue.defaultPageSizeId,
                                               printerInfo->defaultValue.defaultColorMode,
                                               printerInfo->defaultValue.defaultDuplexMode,
                                               printerInfo->defaultValue.defaultResolution,
                                               printerInfo->defaultValue.defaultMargin,
                                               true,
                                               printerInfo->defaultValue.defaultOrientation,
                                               printerInfo->defaultValue.defaultPrintQuality,
                                               DOCUMENT\_FORMAT\_PDF,
                                               printerInfo->defaultValue.otherDefaultValues, };
Print\_ErrorCode ret = OH\_Print\_StartPrintJob(printJob);
delete printJob;

// Release resources when the print service is no longer used.
OH\_Print\_Release()
