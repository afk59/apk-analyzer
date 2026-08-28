# Launching EmbeddedUIExtensionAbility with EmbeddedComponent

ArkUI offers a subset of ArkTS capabilities on the native side, excluding features such as declarative UI syntax, custom struct components, and the preset UI component library.

Since API version 20, the ArkUI framework provides the capability to embed **EmbeddedComponent** components on the native side. This capability relies on the [EmbeddedComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-embedded-component) mechanism. **EmbeddedComponent** is used to embed UI content provided by another [EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability) component (within the same application) into the current page. EmbeddedUIExtensionAbility runs in an independent process, handling page layout and rendering. This functionality is primarily designed for modular development scenarios that require process isolation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ZpzwVuoJRxmuqZYGwvfYnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061941Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1CAA0A953881EAEAF3BDA39E54103FB27371131BD777D21C93AEA6C6EEAFEC6)

-   After creating [ArkUI\_EmbeddedComponentOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/i-arkui-nativemodule-arkui-embeddedcomponentoption) with [OH\_ArkUI\_EmbeddedComponentOption\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_create), use [OH\_ArkUI\_EmbeddedComponentOption\_SetOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonerror) to set the **onError** callback and [OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonterminated) to set the **onTerminated** callback. Use [OH\_ArkUI\_NodeUtils\_MoveTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_moveto) for node migration.
    
-   When the **onTerminated** callback is set using [OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_setonterminated), the returned **want** parameter contains only the key-value pairs returned by the provider. Nested parsing is not supported.
    
-   Call [OH\_ArkUI\_EmbeddedComponentOption\_Dispose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-type-h#oh_arkui_embeddedcomponentoption_dispose) to release memory when the **EmbeddedComponent** component is destroyed.
    
-   The **width** and **height** attributes must be explicitly set for **EmbeddedComponent** using [setAttribute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#setattribute).
    

This example demonstrates the basic usage of **EmbeddedComponent**. For details about ability usage, see [EmbeddedComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-embedded-component). The sample application's bundle name is "com.example.embeddeddemo", and the EmbeddedUIExtensionAbility to be launched within the same application is named "ExampleEmbeddedAbility". This sample requires multi-process permission and can only run on supported devices such as PCs and 2-in-1 devices.

#include <arkui/native\_node.h>
#include <arkui/native\_type.h>
#include <AbilityKit/ability\_base/want.h> // Include the ability want header file.

// Register events.
void onError(int32\_t code, const char \*name, const char \*message) {}
void onTerminated(int32\_t code, AbilityBase\_Want \*want) {}
const unsigned int LOG\_PRINT\_DOMAIN = 0xFF00;
#define SIZE\_300 300
#define SIZE\_401 401
#define SIZE\_480 480
// ···
    // Create a node.
    ArkUI\_NodeHandle embeddedNode = nodeAPI->createNode(ARKUI\_NODE\_EMBEDDED\_COMPONENT);
    // Set properties.
    AbilityBase\_Element Element = {.bundleName = "com.example.uiextensionandaccessibility",
                                   .abilityName = "ExampleEmbeddedAbility",
                                   .moduleName = "entry"};       // This API is provided by the ability subsystem.
    AbilityBase\_Want \*want = OH\_AbilityBase\_CreateWant(Element); // The API is provided by the ability subsystem.
    if (want == nullptr) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "AbilityBase\_Want", "~PluginManager");
    }
    ArkUI\_AttributeItem itemobjwant = {.object = want};
    nodeAPI->setAttribute(embeddedNode, NODE\_EMBEDDED\_COMPONENT\_WANT, &itemobjwant);

    auto embeddedNode\_option = OH\_ArkUI\_EmbeddedComponentOption\_Create();
    auto onErrorCallback = onError;
    auto onTerminatedCallback = onTerminated;
    OH\_ArkUI\_EmbeddedComponentOption\_SetOnError(embeddedNode\_option, onErrorCallback);
    OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated(embeddedNode\_option, onTerminatedCallback);

    ArkUI\_AttributeItem itemobjembeddedNode = {.object = embeddedNode\_option};
    nodeAPI->setAttribute(embeddedNode, NODE\_EMBEDDED\_COMPONENT\_OPTION, &itemobjembeddedNode);

    // Set basic attributes, such as width and height.
    ArkUI\_NumberValue value\[\] = {SIZE\_480};
    ArkUI\_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI\_NumberValue)};
    value\[0\].f32 = SIZE\_300;
    nodeAPI->setAttribute(embeddedNode, NODE\_WIDTH, &item);
    nodeAPI->setAttribute(embeddedNode, NODE\_HEIGHT, &item);

    // Create a Column node.
    ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
    nodeAPI->setAttribute(column, NODE\_WIDTH, &item);
    ArkUI\_NumberValue column\_bc\[\] = {{.u32 = 0xFFF00BB}};
    ArkUI\_AttributeItem column\_item = {column\_bc, 1};
    nodeAPI->setAttribute(column, NODE\_BACKGROUND\_COLOR, &column\_item);
    ArkUI\_AttributeItem column\_id = {.string = "Column\_CAPI"};
    nodeAPI->setAttribute(column, NODE\_ID, &column\_id);

    // Mount the component node to the parent node.
    nodeAPI->addChild(column, embeddedNode);
