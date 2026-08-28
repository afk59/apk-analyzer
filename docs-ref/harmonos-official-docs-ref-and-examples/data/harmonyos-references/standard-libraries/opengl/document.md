# OpenGL

[OpenGL](https://www.khronos.org/opengl/) is a cross-platform graphics API that specifies a standard software interface for 3D graphics processing hardware. HarmonyOS now supports OpenGL 4.2.

#### Supported Capabilities and Devices

Supported capabilities:

-   OpenGL 3.0 is supported since API version 20.
    
-   OpenGL 4.2 is supported since API version 22.
    

Supported devices:

OpenGL is supported on PC devices starting from API version 20. Starting from API version 22, support for OpenGL is newly added on some tablet devices. Whether a specific tablet device supports this capability can be determined through the **OH\_Graphics\_QueryGL** API.

#### Checking the Support for OpenGL

Starting from API version 22, you can call the **OH\_Graphics\_QueryGL** API to check whether the device supports OpenGL and whether it needs to fall back to OpenGL ES.

**Device behavior differences**: The **OH\_Graphics\_QueryGL API** works properly on PCs and tablets but returns null on other devices.

Specific examples are as follows:

typedef EGLBoolean(&OH\_Graphics\_QueryGL\_FUNC)(void);
static napi\_value QueryGL(napi\_env env, napi\_callback\_info info)
{
    const char &r0 = u8"OH\_Graphics\_QueryGL does not exist. Use GLES";
    const char &r1 = u8"OH\_Graphics\_QueryGL exists; returns 0. Use GLES";
    const char &r2 = u8"OH\_Graphics\_QueryGL exists; returns 1. Use GL";
    napi\_value result = nullptr;
    napi\_status status = napi\_invalid\_arg;
    OH\_Graphics\_QueryGL\_FUNC OH\_Graphics\_QueryGL = (OH\_Graphics\_QueryGL\_FUNC)EglGetProcAddress("OH\_Graphics\_QueryGL");
    if (OH\_Graphics\_QueryGL) {
        if (OH\_Graphics\_QueryGL()) {
            status = napi\_create\_string\_utf8(env, r2, (size\_t)strlen(r2), &result);
        } else {
            status = napi\_create\_string\_utf8(env, r1, (size\_t)strlen(r1), &result);
        }
    } else {
        status = napi\_create\_string\_utf8(env, r0, (size\_t)strlen(r0), &result);
    }
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Failed to create UTF-8 string");
    }
    return result;
}

#### Symbols Exported from the Standard Library

[OpenGL Symbols Exported from Native APIs](../appendix/opengl-symbols/document.md)

#### OpenGL Extensions and Examples

For details about the OpenGL extensions and their usage, see [OpenGL ES Extensions](../opengl-es/document.md#opengl-es-extensions).

For details about how to use these extensions, see [OpenGL ES Example](../opengl-es/document.md#example).

#### Introducing OpenGL

To use OpenGL capabilities, you must add related dynamic link libraries (DLLs) and header files.

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libace\_ndk.z.so
libace\_napi.z.so
libGLv4.so
libEGL.so

**Including Header Files**

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <EGL/eglplatform.h>
#include <GL/gl.h>
#include <GL/glcorearb.h>

**Modifying the app.json5 Configuration File**

"appEnvironments": \[
 {
   "name":"NEED\_OPENGL",
   "value": "1"
 }
\],

#### References

To use the OpenGL API in your application development, familiarize yourself with the NDK development process and the **XComponent** usage, which are described in the following topics:

-   [Getting Started with the NDK](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-development-overview)
    
-   [Node-API](../node-api/document.md)
    
-   [XComponentNode](../../application-framework/arkui/arkts-api/apis-no-longer-maintained/xcomponentnode/document.md)
    
-   [XComponent](../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md)
