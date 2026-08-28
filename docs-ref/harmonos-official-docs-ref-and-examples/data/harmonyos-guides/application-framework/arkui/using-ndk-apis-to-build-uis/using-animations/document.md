# Using Animations

#### Using Property Animations

The [ArkUI](../../about-this-kit/document.md) development framework provides the property animation in the [NDK](../../../../ndk-development/about-this-kit/document.md) API to implement the component appearance/disappearance transition. Additionally, frame animation capabilities from the [ArkTS](../../../arkts/about-this-kit/document.md) side can be bridged through the Node-API to achieve animation effects on the native side.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2akbkFkgTWmnSFBlfw3dGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4778E30FD6BF59902FAAA2F13726CB043CFCBA0995B360E7BF82051180E8C3EC)

-   Obtain [this.getUIContext()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-api#getuicontext) from ArkTS and pass it to the native side.
    
-   On the native side, obtain the context using the [OH\_ArkUI\_GetContextFromNapiValue](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-napi-h#oh_arkui_getcontextfromnapivalue) API.
    
-   Animation property changes must be encapsulated within the callback of [ArkUI\_ContextCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback).
    
-   Ensure that the properties intended for animation have been set before the animation is executed.
    
-   This section demonstrates core API usage only. For the complete sample project, see [AnimationNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AnimationNDK).
    

With the global [animateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto) API, you can build explicit animations for state changes caused by closure code. Like property animations, layout changes such as width and height adjustments are animated directly to their final states.

1.  Create a [NodeContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-nodecontent) object in the .ets file and pass it as a parameter to the native method.
    
      // Initialize the NodeContent object.
      private rootSlot = new NodeContent();
      @State @Watch('changeNativeFlag') showNative: boolean = false;
    // ···
      changeNativeFlag(): void {
        // ···
        if (this.showNative) {
          // Pass the NodeContent object for the native side to create component mounting and display.
          nativeNode?.createNativeRoot(this.rootSlot);
        } else {
        // ···
        }
      }
    
2.  Parse **NodeContent** and convert it to the [ArkUI\_NodeContentHandle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h) object in C.
    
    // Obtain the NodeContent object.
    ArkUI\_NodeContentHandle contentHandle;
    OH\_ArkUI\_GetNodeContentFromNapiValue(env, args\[0\], &contentHandle);
    
3.  Obtain the [ArkUI\_NativeAnimateAPI\_1](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1) object.
    
    // Obtain the ArkUI\_NativeAnimateAPI.
    ArkUI\_NativeAnimateAPI\_1 \*animateApi = nullptr;
    OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_ANIMATE, ArkUI\_NativeAnimateAPI\_1, animateApi);
    
4.  Set the [ArkUI\_AnimateOption](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption) parameters using the provided C methods.
    
    // Set the animation parameters.
    ArkUI\_AnimateOption \*option = OH\_ArkUI\_AnimateOption\_Create();
    OH\_ArkUI\_AnimateOption\_SetDuration(option, NUM\_2000); // NUM\_2000 = 2000
    OH\_ArkUI\_AnimateOption\_SetTempo(option, 1.1);
    OH\_ArkUI\_AnimateOption\_SetCurve(option, ARKUI\_CURVE\_EASE);
    ArkUI\_CurveHandle cubicBezierCurve = OH\_ArkUI\_Curve\_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f);
    // Set the animation curve parameters, which take precedence over OH\_ArkUI\_AnimateOption\_SetCurve.
    OH\_ArkUI\_AnimateOption\_SetICurve(option, cubicBezierCurve);
    OH\_ArkUI\_AnimateOption\_SetDelay(option, NUM\_20); // NUM\_20 = 20
    OH\_ArkUI\_AnimateOption\_SetIterations(option, NUM\_1); // NUM\_1 = 1
    OH\_ArkUI\_AnimateOption\_SetPlayMode(option, ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE);
    ArkUI\_ExpectedFrameRateRange \*range = new ArkUI\_ExpectedFrameRateRange;
    range->min = NUM\_10; // NUM\_10 = 10
    range->max = NUM\_120; // NUM\_120 = 120
    range->expected = NUM\_60; // NUM\_60 = 60
    OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(option, range);
    
5.  Set callback parameters.
    
    // Create and set user data for the completion callback.
    ArkUI\_AnimateCompleteCallback \*completeCallback = new ArkUI\_AnimateCompleteCallback;
    completeCallback->type = ARKUI\_FINISH\_CALLBACK\_REMOVED;
    // The AnimateData struct contains ArkUI\_AnimateOption\* option and ArkUI\_CurveHandle curve.
    AnimateData\* data = new AnimateData();
    data->option = option;
    data->curve = cubicBezierCurve;
    completeCallback->userData = reinterpret\_cast<void\*>(data);
    completeCallback->callback = \[\](void \*userData) {
        AnimateData\* data = reinterpret\_cast<AnimateData\*>(userData);
        if (data) {
            ArkUI\_AnimateOption\* option = data->option;
            ArkUI\_CurveHandle curve = data->curve;
            if (option) {
                OH\_ArkUI\_AnimateOption\_Dispose(option);
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                    "Init", "CXX OH\_ArkUI\_AnimateOption\_Dispose  success!");
            }
            if (curve) {
                OH\_ArkUI\_Curve\_DisposeCurve(curve);
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                    "Init", "CXX OH\_ArkUI\_Curve\_DisposeCurve  success!");
            }
            delete data; // Release the struct.
        }
    };
                
    // Set the closure function.
    static bool isback = true;
    ArkUI\_ContextCallback \*update = new ArkUI\_ContextCallback;
    update->callback = \[\](void \*user) {
        // Example of changing width and height properties
        if (isback) {
            g\_animateto\_button->SetWidth(NUM\_200); // NUM\_200 = 200
            g\_animateto\_button->SetHeight(NUM\_80); // NUM\_80 = 80
            g\_animateto\_button->SetBackgroundColor(0xFFA280FF);
        } else {
            g\_animateto\_button->SetWidth(NUM\_100); // NUM\_100 = 100
            g\_animateto\_button->SetHeight(NUM\_40); // NUM\_40 = 40
            g\_animateto\_button->SetBackgroundColor(0xFFFF2E77);
        }
        isback = !isback;
    };
    // Execute the animation with the set options and callbacks.
    animateApi->animateTo(context, option, update, completeCallback);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/aUAi0l51QSa16R398ENWCQ/en-us_image_0000002568684601.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C65B83890DCE33EB46D5DE2B11387A2C9DFD6990BF573A34110FEE87E3BBD6)
    

#### Using Component Appearance/Disappearance Transitions

Use **NODE\_XX\_TRANSITION** properties (where XX can be **OPACITY**, **TRANSLATE**, **SCALE**, **ROTATE**, or **MOVE**) to configure transition effects for components, enhancing user experience when components are added to or removed from containers. The [NODE\_TRANSFORM\_CENTER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h) property sets the center point for animations including **NODE\_SCALE\_TRANSITION** and **NODE\_ROTATE\_ROTATE**.

1.  Design an interactive UI with a button to manage the addition and removal of transition nodes. For details about how to obtain and use the ArkUI\_NodeContentHandle node, see [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).
    
    constexpr int32\_t BUTTON\_CLICK\_ID = 1;
    bool g\_flag = false;
    ArkUI\_NodeHandle parentNode;
    ArkUI\_NodeHandle childNode;
    ArkUI\_NodeHandle buttonNode;
    // ···
    void mainViewMethod(ArkUI\_NodeContentHandle handle)
    {
        ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        ArkUI\_NodeHandle column = nodeAPI->createNode(ARKUI\_NODE\_COLUMN);
        ArkUI\_NumberValue widthValue\[\] = {{.f32 = 500}};
        ArkUI\_AttributeItem widthItem = {.value = widthValue, .size = sizeof(widthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_WIDTH, &widthItem);
        ArkUI\_NumberValue heightValue\[\] = {{.f32 = 500}};
        ArkUI\_AttributeItem heightItem = {.value = heightValue, .size = sizeof(heightValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(column, NODE\_HEIGHT, &heightItem);
        ArkUI\_NodeHandle buttonShow = nodeAPI->createNode(ARKUI\_NODE\_BUTTON);
        ArkUI\_NumberValue buttonWidthValue\[\] = {{.f32 = 200}};
        ArkUI\_AttributeItem buttonWidthItem = {.value = buttonWidthValue,
                                               .size = sizeof(buttonWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(buttonShow, NODE\_WIDTH, &buttonWidthItem);
        ArkUI\_NumberValue buttonHeightValue\[\] = {{.f32 = 50}};
        ArkUI\_AttributeItem buttonHeightItem = {.value = buttonHeightValue,
                                                .size = sizeof(buttonHeightValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(buttonShow, NODE\_HEIGHT, &buttonHeightItem);
        ArkUI\_AttributeItem labelItem = {.string = "show"};
        nodeAPI->setAttribute(buttonShow, NODE\_BUTTON\_LABEL, &labelItem);
        ArkUI\_NumberValue buttonOpenTypeValue\[\] = {{.i32 = static\_cast<int32\_t>(ARKUI\_BUTTON\_TYPE\_NORMAL)}};
        ArkUI\_AttributeItem buttonOpenTypeItem = {.value = buttonOpenTypeValue,
                                                  .size = sizeof(buttonOpenTypeValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(buttonShow, NODE\_BUTTON\_TYPE, &buttonOpenTypeItem);
        ArkUI\_NumberValue buttonShowMarginValue\[\] = {{.f32 = 20}};
        ArkUI\_AttributeItem buttonShowMarginItem = {.value = buttonShowMarginValue,
                                                    .size = sizeof(buttonShowMarginValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(buttonShow, NODE\_MARGIN, &buttonShowMarginItem);
        nodeAPI->registerNodeEvent(buttonShow, NODE\_ON\_CLICK, BUTTON\_CLICK\_ID, nullptr);
        nodeAPI->addNodeEventReceiver(buttonShow, OnButtonShowClicked);
        parentNode = column;
        buttonNode = buttonShow;
        nodeAPI->addChild(column, buttonShow);
        OH\_ArkUI\_NodeContent\_AddNode(handle, column);
    }
    
2.  Create a node with the [NODE\_ROTATE\_TRANSITION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h), [NODE\_SCALE\_TRANSITION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h), and [NODE\_TRANSLATE\_TRANSITION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-node-h) properties. When the target node is mounted to or unmounted from the node tree, the transition animation is played.
    
    ArkUI\_NodeHandle CreateChildNode()
    {
        ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        ArkUI\_NodeHandle image = nodeAPI->createNode(ARKUI\_NODE\_IMAGE);
        ArkUI\_AttributeItem imageSrcItem = {.string = "/pages/common/scenery.jpg"};
        nodeAPI->setAttribute(image, NODE\_IMAGE\_SRC, &imageSrcItem);
        ArkUI\_NumberValue textWidthValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textWidthItem = {.value = textWidthValue,
                                             .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_WIDTH, &textWidthItem);
        ArkUI\_NumberValue textHeightValue\[\] = {{.f32 = 300}};
        ArkUI\_AttributeItem textHeightItem = {.value = textHeightValue,
                                              .size = sizeof(textWidthValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_HEIGHT, &textHeightItem);
        ArkUI\_NumberValue transformCenterValue\[\] = {0.0f, 0.0f, 0.0f, 0.5f, 0.5f};
        ArkUI\_AttributeItem transformCenterItem = {.value = transformCenterValue,
                                                   .size = sizeof(transformCenterValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_TRANSFORM\_CENTER, &transformCenterItem);
        ArkUI\_NumberValue rotateAnimationValue\[\] = {
            0.0f, 0.0f, 1.0f, 360.0f, 0.0f, {.i32 = 500}, {.i32 = static\_cast<int32\_t>(ARKUI\_CURVE\_SHARP)}};
        ArkUI\_AttributeItem rotateAnimationItem = {.value = rotateAnimationValue,
                                                   .size = sizeof(rotateAnimationValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_ROTATE\_TRANSITION, &rotateAnimationItem);
        ArkUI\_NumberValue scaleAnimationValue\[\] = {
            0.0f, 0.0f, 0.0f, {.i32 = 500}, {.i32 = static\_cast<int32\_t>(ARKUI\_CURVE\_SHARP)}};
        ArkUI\_AttributeItem scaleAnimationItem = {.value = scaleAnimationValue,
                                                  .size = sizeof(scaleAnimationValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_SCALE\_TRANSITION, &scaleAnimationItem);
        ArkUI\_NumberValue translateAnimationValue\[\] = {
            200, 200, 0.0f, {.i32 = 500}, {.i32 = static\_cast<int32\_t>(ARKUI\_CURVE\_SHARP)}};
        ArkUI\_AttributeItem translateAnimationItem = {.value = translateAnimationValue,
                                                      .size = sizeof(translateAnimationValue) / sizeof(ArkUI\_NumberValue)};
        nodeAPI->setAttribute(image, NODE\_TRANSLATE\_TRANSITION, &translateAnimationItem);
        return image;
    }
    
3.  Add logic for mounting and unmounting the transition node within the **Button** component event callback to control the appearance and disappearance of the transition node.
    
    void OnButtonShowClicked(ArkUI\_NodeEvent \*event)
    {
        if (!event) {
            return;
        }
        if (!childNode) {
            childNode = CreateChildNode();
        }
        ArkUI\_NativeNodeAPI\_1 \*nodeAPI = reinterpret\_cast<ArkUI\_NativeNodeAPI\_1 \*>(
            OH\_ArkUI\_QueryModuleInterfaceByName(ARKUI\_NATIVE\_NODE, "ArkUI\_NativeNodeAPI\_1"));
        if (g\_flag) {
            g\_flag = false;
            ArkUI\_AttributeItem labelItem = {.string = "show"};
            nodeAPI->setAttribute(buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
            nodeAPI->removeChild(parentNode, childNode);
        } else {
            g\_flag = true;
            ArkUI\_AttributeItem labelItem = {.string = "hide"};
            nodeAPI->setAttribute(buttonNode, NODE\_BUTTON\_LABEL, &labelItem);
            nodeAPI->addChild(parentNode, childNode);
        }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/PCPn__XzTaORMGKO9N4eHg/en-us_image_0000002568764611.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54124FF064C0103DA71FD8044D89B36A880780B55D1CA3E7574959387606568B)
    

#### Using Keyframe Animations

You can use the [keyframeAnimateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#keyframeanimateto) API to specify several keyframe states to create segmented animations. Like property animations, layout changes such as width and height adjustments are animated directly to their final states.

This example demonstrates how to use the [keyframeAnimateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#keyframeanimateto) API to set up keyframe animations. For the complete process of mounting a UI developed with NDK APIs to the ArkTS main page, see [Integrating with ArkTS Pages](../integrating-with-arkts-pages/document.md).

// ArkUIColumnNode is a project-encapsulated node type.
auto column = std::make\_shared<ArkUIColumnNode>();
// Set width to 300 (NUM\_300 = 300).
column->SetWidth(NUM\_300);
// Set height to 250 (NUM\_250 = 250).
column->SetHeight(NUM\_250);
// Create a text node with content "This is a keyframe animation."
auto textNode = std::make\_shared<ArkUITextNode>();
textNode->SetTextContent("This is a keyframe animation");
// Set width to 120 (NUM\_120 = 120).
textNode->SetWidth(NUM\_120);
// Set height to 120 (NUM\_120 = 120).
textNode->SetHeight(NUM\_50);
// Create a button that will be the target of the keyframe animation.
auto button = std::make\_shared<ArkUIButtonNode>();
// Set the initial width and height of the button (NUM\_100 = 100).
button->SetWidth(NUM\_100);
button->SetHeight(NUM\_100);
// Store the button as a global variable for use in onTouch registration.
g\_keyframe\_button = button;
// Register a click event for the button (NUM\_1 = 1).
button->RegisterNodeEvent(button->GetHandle(), NODE\_ON\_CLICK, NUM\_1, nullptr);
g\_keyframe\_text = std::make\_shared<ArkUITextNode>();
// This function encapsulates logic to print AnimateTo parameter values in a text component (to be implemented by the user based on specific requirements).
g\_keyframe\_text->KeyframeAnimatetoToString();
auto onTouch = \[\](ArkUI\_NodeEvent \*event) {
    // Trigger logic when the target button (NUM\_1 = 1) is clicked.
    if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_1) {
        // Obtain the context object.
        ArkUI\_ContextHandle context = nullptr;
        // g\_keyframe\_button (std::shared\_ptr<ArkUIButtonNode>) is a global variable that holds the button node instance for use in onTouch event registration.
        context = OH\_ArkUI\_GetContextByNode(g\_keyframe\_button->GetHandle());
        // Obtain the ArkUI\_NativeAnimateAPI.
        ArkUI\_NativeAnimateAPI\_1 \*animateApi = nullptr;
        OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_ANIMATE, ArkUI\_NativeAnimateAPI\_1, animateApi);
            
        // The following code is the key process for creating a keyframe animation, including setting keyframe animation parameters and starting the animation.
        // Set the ArkUI\_KeyframeAnimateOption parameters using the provided C APIs.
        // Number of keyframe animation states (NUM\_2 = 2, NUM\_500 = 500).
        ArkUI\_KeyframeAnimateOption \*option =  OH\_ArkUI\_KeyframeAnimateOption\_Create(NUM\_2);
        OH\_ArkUI\_KeyframeAnimateOption\_SetDelay(option, NUM\_500);
        // Duration for the first keyframe segment (NUM\_1000 = 1000, NUM\_0 = 0).
        OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(option, NUM\_1000, NUM\_0);
        // Duration for the second keyframe segment (NUM\_2000 = 2000, NUM\_1 = 1).
        OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(option, NUM\_2000, NUM\_1);
        // Animation playback iterations (NUM\_5 = 5).
        OH\_ArkUI\_KeyframeAnimateOption\_SetIterations(option, NUM\_5);
        ArkUI\_CurveHandle curve = OH\_ArkUI\_Curve\_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f);
        // Select the animation curves based on service requirements.
        ArkUI\_CurveHandle springCurve = OH\_ArkUI\_Curve\_CreateSpringCurve(0.5f, 4.0f, 1.2f, 0.0f);
        ArkUI\_CurveHandle springMotionCurve = OH\_ArkUI\_Curve\_CreateSpringMotion(0.5f, 0.6f, 0.0f);
        ArkUI\_CurveHandle responsiveSpringMotionCurve = OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion(0.5f,
            4.0f, 1.2f);
        ArkUI\_CurveHandle interpolatingSpringCurve = OH\_ArkUI\_Curve\_CreateInterpolatingSpring(0.5f,
            4.0f, 1.2f, 0.0f);
        OH\_ArkUI\_KeyframeAnimateOption\_SetCurve(option, curve, 1);
        OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(option, nullptr, \[\](void \*userData) {
              g\_keyframe\_button->SetWidth(NUM\_150);
        }, NUM\_0); // Callback for the first keyframe state (NUM\_150 = 150, NUM\_0 = 0).
        OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(option, nullptr, \[\](void \*userData) {
              g\_keyframe\_button->SetWidth(80);
        }, NUM\_1); // Callback for the second keyframe state (NUM\_1 = 1).
        KeyFrameAnimateToData\* data = new KeyFrameAnimateToData();
        data->option = option;
        data->curve = curve;
        OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback(option, nullptr, \[\](void \*user) {
            KeyFrameAnimateToData\* data = reinterpret\_cast<KeyFrameAnimateToData\*>(user);
            if (data) {
                ArkUI\_KeyframeAnimateOption\* option = data->option;
                ArkUI\_CurveHandle curve = data->curve;
                if (option) {
                    OH\_ArkUI\_KeyframeAnimateOption\_Dispose(option);
                    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                        "Init", "CXX OH\_ArkUI\_KeyframeAnimateOption\_Dispose  success!");
                }
                if (curve) {
                    OH\_ArkUI\_Curve\_DisposeCurve(curve);
                    OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN,
                        "Init", "CXX OH\_ArkUI\_Curve\_DisposeCurve  success!");
                }
                delete data; // Release the struct.
            }
        }); // Keyframe animation completion callback.
        ArkUI\_ExpectedFrameRateRange \*range = new ArkUI\_ExpectedFrameRateRange;
        range->max = NUM\_120; // NUM\_120 = 120
        range->expected = NUM\_60; // NUM\_60 = 60
        range->min = NUM\_30; // NUM\_30 = 30
        OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate(option, range); // Set the expected frame rate for keyframes.

        // Execute the animation with the set options and callbacks.
        animateApi->keyframeAnimateTo(context, option);
        auto delay = OH\_ArkUI\_KeyframeAnimateOption\_GetDelay(option);
        auto iter = OH\_ArkUI\_KeyframeAnimateOption\_GetIterations(option);
        auto expected = OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate(option); // Obtain the expected frame rate range from the keyframe animation parameters.
        auto dur0 = OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(option, NUM\_1); // NUM\_1 = 1
        auto dur1 = OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(option, NUM\_1);
        auto curves = OH\_ArkUI\_KeyframeAnimateOption\_GetCurve(option, NUM\_1); // Obtain the animation curve for a specific keyframe segment.
        g\_keyframe\_text->KeyframeAnimatetoToString(dur0, dur1, delay, iter, \*expected);
    }
};
// Register a callback function for the click event.
button->RegisterNodeEventReceiver(onTouch);
// Mount the button to the column and return the column node.
column->AddChild(g\_keyframe\_text);
column->AddChild(textNode);
column->AddChild(button);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/BkDdX_E8SnSFO5rwyDdQ8A/en-us_image_0000002537764886.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7454BA18E693CB54868CDD6EAF7C5735AAA10CEF2700DE26CC51A8B54A50DA6)

#### Using Frame Animations

Frame animation enables adjustment of animation properties on each frame through its per-frame callback mechanism. The [onFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-animate-h#oh_arkui_animatoroption_registeronframecallback) callback allows you to set attributes on each frame of the application in the frame animation, enabling a natural transition of component attributes and creating a smooth animation effect. For details about the frame animation APIs, see [createAnimator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#createanimator).

Compared with the property animation, the frame animation offers the benefits of real-time visibility into the animation process and allows you to modify UI values on the fly. In addition, it provides high responsiveness to events and can be paused as needed. However, it is worth noting that the frame animation may not deliver the same performance efficiency as the property animation. Therefore, where the property animation meets your requirements, you are advised to use the property animation APIs. For details about how to use the [animateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#animateto) API, see [Using Property Animations](#using-property-animations).

This example demonstrates how to use the [createAnimator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1#createanimator) API to set up frame animations. For the complete sample project, see [AnimationNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AnimationNDK).

std::shared\_ptr<ArkUIBaseNode> CreateAnimator()
{
    auto column = std::make\_shared<ArkUIColumnNode>();
    column->SetWidth(NUM\_300); // NUM\_300 = 300
    column->SetHeight(NUM\_250); // NUM\_250 = 250
    // Create a text node with content "This is an animator animation."
    auto textNode = std::make\_shared<ArkUITextNode>();
    textNode->SetTextContent("This is an animator animation");
    textNode->SetWidth(NUM\_120); // NUM\_120 = 120
    textNode->SetHeight(NUM\_50); // NUM\_50 = 50
    // Create createButton to initialize animator parameters.
    auto createButton = std::make\_shared<ArkUIButtonNode>();
    // Create a button that serves as the target of the animator animation.
    auto button = std::make\_shared<ArkUIButtonNode>();
    // Set the initial width and height of the button (NUM\_100 = 100).
    button->SetWidth(NUM\_100);
    button->SetHeight(NUM\_100);
    // Store the button as a global variable for use in onTouch registration.
    g\_animator\_button = button;
    // Register a click event for the button (NUM\_3 = 3).
    createButton->RegisterNodeEvent(createButton->GetHandle(), NODE\_ON\_CLICK, NUM\_3, nullptr);
    g\_animator\_text = std::make\_shared<ArkUITextNode>();
    g\_animator\_text->AnimatorToString();
    auto onTouch = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_3 = 3) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_3) {
            // Obtain the context object.
            static ArkUI\_ContextHandle context = nullptr;
            context = OH\_ArkUI\_GetContextByNode(g\_animator\_button->GetHandle());

            // Obtain the ArkUI\_NativeAnimateAPI.
            ArkUI\_NativeAnimateAPI\_1 \*animateApi = nullptr;
            OH\_ArkUI\_GetModuleInterface(ARKUI\_NATIVE\_ANIMATE, ArkUI\_NativeAnimateAPI\_1, animateApi);
            
            // The following demonstrates the key process for creating an Animator animation, including setting Animator animation parameters and starting the animation.
            // Set the ArkUI\_AnimatorOption parameters using the provided C APIs (NUM\_0 = 0).
            static ArkUI\_AnimatorOption \*option =  OH\_ArkUI\_AnimatorOption\_Create(NUM\_0); // Number of animator animation states.
            OH\_ArkUI\_AnimatorOption\_SetDuration(option, NUM\_2000); // NUM\_2000 = 2000
            OH\_ArkUI\_AnimatorOption\_SetDelay(option, NUM\_10); // NUM\_10 = 10
            OH\_ArkUI\_AnimatorOption\_SetIterations(option, NUM\_3); // NUM\_3 = 3
            OH\_ArkUI\_AnimatorOption\_SetFill(option, ARKUI\_ANIMATION\_FILL\_MODE\_NONE);
            OH\_ArkUI\_AnimatorOption\_SetDirection(option, ARKUI\_ANIMATION\_DIRECTION\_NORMAL);
            ArkUI\_CurveHandle curve = OH\_ArkUI\_Curve\_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f); // Create a cubic Bézier curve object.
            OH\_ArkUI\_AnimatorOption\_SetCurve(option, curve);
            OH\_ArkUI\_AnimatorOption\_SetBegin(option, NUM\_100); // NUM\_100 = 100
            OH\_ArkUI\_AnimatorOption\_SetEnd(option, NUM\_150); // NUM\_150 = 150
            ArkUI\_ExpectedFrameRateRange \*range = new ArkUI\_ExpectedFrameRateRange;
            range->max = NUM\_120; // NUM\_120 = 120
            range->expected = NUM\_60; // NUM\_60 = 60
            range->min = NUM\_30; // NUM\_30 = 30
            OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange(option, range);
            OH\_ArkUI\_AnimatorOption\_SetKeyframe(option, 0.5, 120.5, NUM\_0); // Set the keyframe parameters of the animator animation (NUM\_0 = 0).
            OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve(option, curve, NUM\_0); // Set the keyframe curve type of the animator animation.
            OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(option, nullptr, \[\](ArkUI\_AnimatorOnFrameEvent \*event)
            {
                OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(event); // Obtain the custom object from the animation event object.
                auto value = OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(event); // Obtain the current progress from the animation event object.
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_PRINT\_DOMAIN, "Init",
                    "CXX OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback  %{public}f", value);
                g\_animator\_button->SetWidth(value);
            });
            OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback(option, nullptr, \[\](ArkUI\_AnimatorEvent\* event)
            {
                OH\_ArkUI\_AnimatorEvent\_GetUserData(event); // Obtain the custom object from the animation event object.
            });
            OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback(option, nullptr, \[\](ArkUI\_AnimatorEvent\* event)
            {
            });
            OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback(option, nullptr, \[\](ArkUI\_AnimatorEvent\* event)
            {
            });
            // Execute the animation with the set options and callbacks.
            animatorHandle = animateApi->createAnimator(context, option);
            
            auto duration = OH\_ArkUI\_AnimatorOption\_GetDuration(option);
            auto delay = OH\_ArkUI\_AnimatorOption\_GetDelay(option);
            auto iterations = OH\_ArkUI\_AnimatorOption\_GetIterations(option);
            auto fill = OH\_ArkUI\_AnimatorOption\_GetFill(option);
            auto direction = OH\_ArkUI\_AnimatorOption\_GetDirection(option);
            auto curves = OH\_ArkUI\_AnimatorOption\_GetCurve(option); // Obtain the animator animation interpolation curve.
            auto begin = OH\_ArkUI\_AnimatorOption\_GetBegin(option);
            auto end = OH\_ArkUI\_AnimatorOption\_GetEnd(option); // Obtain the interpolation end point of the animator animation.
            auto expected = OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange(option); // Obtain the expected frame rate range from the keyframe animation parameters.
            auto keyframeTime = OH\_ArkUI\_AnimatorOption\_GetKeyframeTime(option, NUM\_0); // Obtain the keyframe time of the animator animation.
            auto keyframeValue = OH\_ArkUI\_AnimatorOption\_GetKeyframeValue(option, NUM\_0); // Obtain the keyframe value from the animator animation parameters.
            auto keyframeCurve = OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve(option, NUM\_0); // Obtain the keyframe interpolation curve of the animator animation.
            g\_animator\_text->AnimatorToString(duration, delay, iterations, fill, direction, begin,
                end, \*expected, keyframeTime, keyframeValue);
        }
    };

    // Register a callback function for the click event.
    createButton->RegisterNodeEventReceiver(onTouch);
    createButton->SetButtonLabel("create");
    // Create a container for storing the button.
    auto buttoColumn = std::make\_shared<ArkUIColumnNode>();
    buttoColumn->SetPadding(NUM\_30, false); // Set the layout padding (NUM\_30=30).
    buttoColumn->SetWidth(NUM\_300); // NUM\_300 = 300
    // Create a container for storing playButton.
    auto playButtonColumn = std::make\_shared<ArkUIColumnNode>();
    playButtonColumn->SetPadding(NUM\_10, false); // Set the layout padding (NUM\_10 = 10).
    playButtonColumn->SetWidth(NUM\_300); // NUM\_300 = 300
    // Set the animator play button.
    auto playButton = std::make\_shared<ArkUIButtonNode>();
    playButton->SetButtonLabel("play");
    playButton->RegisterNodeEvent(playButton->GetHandle(), NODE\_ON\_CLICK, NUM\_4, nullptr);
    auto onTouchPlay = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_4 = 4) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_4) {
            OH\_ArkUI\_Animator\_Play(animatorHandle);
        }
    };
    playButton->RegisterNodeEventReceiver(onTouchPlay);
    // Set the animator end button.
    auto finishButton = std::make\_shared<ArkUIButtonNode>();
    finishButton->SetButtonLabel("finish");
    finishButton->RegisterNodeEvent(finishButton->GetHandle(), NODE\_ON\_CLICK, NUM\_5, nullptr); // NUM\_5 = 5
    auto onTouchFinish = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_5 = 5) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_5) {
            OH\_ArkUI\_Animator\_Finish(animatorHandle);
        }
    };
    finishButton->RegisterNodeEventReceiver(onTouchFinish);
    // Create a container for storing resetButton.
    auto resetButtonColumn = std::make\_shared<ArkUIColumnNode>();
    resetButtonColumn->SetPadding(NUM\_10, false); // Set the layout padding (NUM\_10 = 10).
    resetButtonColumn->SetWidth(NUM\_300); // NUM\_300 = 300
    // Set the animator update button.
    auto resetButton = std::make\_shared<ArkUIButtonNode>();
    resetButton->SetButtonLabel("reset");
    resetButton->RegisterNodeEvent(resetButton->GetHandle(), NODE\_ON\_CLICK, NUM\_6, nullptr); // NUM\_6 = 6
    auto onTouchReset = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_6 = 6) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_6) {
            static ArkUI\_AnimatorOption \*option =  OH\_ArkUI\_AnimatorOption\_Create(NUM\_0); // Number of animator animation states.
            OH\_ArkUI\_AnimatorOption\_SetDuration(option, NUM\_1000); // NUM\_1000 = 1000
            OH\_ArkUI\_AnimatorOption\_SetDelay(option, NUM\_0);
            OH\_ArkUI\_AnimatorOption\_SetIterations(option, NUM\_4); // NUM\_4 = 4
            // Choose a curve based on actual service requirements for OH\_ArkUI\_AnimatorOption\_SetCurve.
            auto curve = OH\_ArkUI\_Curve\_CreateCurveByType(ARKUI\_CURVE\_EASE); // The animation starts slowly, accelerates, and then slows down towards the end.
            auto stepsCurve = OH\_ArkUI\_Curve\_CreateStepsCurve(NUM\_20, true); // Create a steps curve object (NUM\_20 = 20).
            OH\_ArkUI\_AnimatorOption\_SetCurve(option, curve);
            OH\_ArkUI\_AnimatorOption\_SetBegin(option, NUM\_200); // NUM\_200 = 200
            OH\_ArkUI\_AnimatorOption\_SetEnd(option, NUM\_100); // NUM\_100 = 100
            OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(option, nullptr, \[\](ArkUI\_AnimatorOnFrameEvent \*event)
            {
                OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(event); // Obtain the custom object from the animation event object.
                auto value = OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(event); // Obtain the current progress from the animation event object.
                g\_animator\_button->SetWidth(value);
            });
            OH\_ArkUI\_Animator\_ResetAnimatorOption(animatorHandle, option);
        }
    };
    resetButton->RegisterNodeEventReceiver(onTouchReset);
    // Set the animator pause button.
    auto pauseButton = std::make\_shared<ArkUIButtonNode>();
    pauseButton->SetButtonLabel("pause");
    pauseButton->RegisterNodeEvent(pauseButton->GetHandle(), NODE\_ON\_CLICK, NUM\_7, nullptr); // NUM\_7 = 7
    auto onTouchPause = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_7 = 7) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_7) {
            OH\_ArkUI\_Animator\_Pause(animatorHandle);
        }
    };
    pauseButton->RegisterNodeEventReceiver(onTouchPause);
    // Create a container for storing cancelButton.
    auto cancelButtonColumn = std::make\_shared<ArkUIColumnNode>();
    cancelButtonColumn->SetPadding(NUM\_10, false); // Set the layout padding (NUM\_10 = 10).
    cancelButtonColumn->SetWidth(NUM\_300); // NUM\_300 = 300
    // Set the animator cancel button.
    auto cancelButton = std::make\_shared<ArkUIButtonNode>();
    cancelButton->SetButtonLabel("cancel");
    cancelButton->RegisterNodeEvent(cancelButton->GetHandle(), NODE\_ON\_CLICK, NUM\_8, nullptr); // NUM\_8 = 8
    auto onTouchCancel = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_8 = 8) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_8) {
            OH\_ArkUI\_Animator\_Cancel(animatorHandle);
        }
    };
    cancelButton->RegisterNodeEventReceiver(onTouchCancel);
    // Set the animator reverse-play button.
    auto reverseButton = std::make\_shared<ArkUIButtonNode>();
    reverseButton->SetButtonLabel("reverse");
    reverseButton->RegisterNodeEvent(reverseButton->GetHandle(), NODE\_ON\_CLICK, NUM\_9, nullptr);
    auto onTouchReverse = \[\](ArkUI\_NodeEvent \*event) {
        // Trigger logic when the target button (NUM\_9 = 9) is clicked.
        if (OH\_ArkUI\_NodeEvent\_GetTargetId(event) == NUM\_9) {
            OH\_ArkUI\_Animator\_Reverse(animatorHandle);
        }
    };
    reverseButton->RegisterNodeEventReceiver(onTouchReverse);
    // Mount the button to the column and return the column node.
    column->AddChild(g\_animator\_text);
    column->AddChild(textNode);
    column->AddChild(button);
    buttoColumn->AddChild(createButton);
    playButtonColumn->AddChild(playButton);
    buttoColumn->AddChild(playButtonColumn);
    buttoColumn->AddChild(finishButton);
    resetButtonColumn->AddChild(resetButton);
    buttoColumn->AddChild(resetButtonColumn);
    buttoColumn->AddChild(pauseButton);
    cancelButtonColumn->AddChild(cancelButton);
    buttoColumn->AddChild(cancelButtonColumn);
    buttoColumn->AddChild(reverseButton);
    column->AddChild(buttoColumn);
    return column;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ULv_ES7TScCOaMht-rVPnA/en-us_image_0000002537924826.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061940Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF713180CE0743FD53F18BF4BFDA2811D569E0101EE8936DFF88DEB39B470AAB)
