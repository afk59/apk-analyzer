# native\_type.h

#### Overview

Defines the common types for the native module.

**File to include**: <arkui/native\_type.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [native\_type\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_Node](../../structs/arkui-node/document.md) | ArkUI\_Node | Defines an ArkUI native component object. |
| [ArkUI\_ContextCallback](../../structs/arkui-contextcallback/document.md) | ArkUI\_ContextCallback | Defines event callback. |
| [ArkUI\_NumberValue](../../structs/arkui-numbervalue/document.md) | ArkUI\_NumberValue | Provides the number types of ArkUI on the native side. |
| [ARKUI\_TextPickerRangeContent](../../structs/arkui-textpickerrangecontent/document.md) | ARKUI\_TextPickerRangeContent | Defines the struct of the single-column text picker with image resources. |
| [ARKUI\_TextPickerCascadeRangeContent](../../structs/arkui-textpickercascaderangecontent/document.md) | ARKUI\_TextPickerCascadeRangeContent | Defines the struct of the interconnected multi-column text picker. |
| [ArkUI\_ColorStop](../../structs/arkui-colorstop/document.md) | ArkUI\_ColorStop | Defines a gradient color stop. |
| [ArkUI\_Rect](../../structs/arkui-rect/document.md) | ArkUI\_Rect | Defines a mask area. |
| [ArkUI\_IntSize](../../structs/arkui-intsize/document.md) | ArkUI\_IntSize | Describes the width and height of a component. |
| [ArkUI\_IntOffset](../../structs/arkui-intoffset/document.md) | ArkUI\_IntOffset | Describes the position of a component. |
| [ArkUI\_Margin](../../structs/arkui-margin/document.md) | ArkUI\_Margin | Describes the margins of a component. |
| [ArkUI\_TranslationOptions](../../structs/arkui-translationoptions/document.md) | ArkUI\_TranslationOptions | Defines the translation options for component transition. |
| [ArkUI\_ScaleOptions](../../structs/arkui-scaleoptions/document.md) | ArkUI\_ScaleOptions | Defines the scaling options for component transition. |
| [ArkUI\_RotationOptions](../../structs/arkui-rotationoptions/document.md) | ArkUI\_RotationOptions | Defines the rotation options for component transition. |
| [ArkUI\_NativeDialog](../../structs/arkui-nativedialog/document.md) | ArkUI\_NativeDialog | Defines a custom dialog controller object for ArkUI on the native side. |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md) | ArkUI\_LayoutConstraint | Defines layout constraints for a component. |
| [ArkUI\_DrawContext](../../structs/arkui-drawcontext/document.md) | ArkUI\_DrawContext | Defines the component drawing context. |
| [ArkUI\_Node\*](../../structs/arkui-node--00020177/document.md) | ArkUI\_NodeHandle | Defines the pointer to the ArkUI native component object. |
| [ArkUI\_NativeDialog\*](../../structs/arkui-nativedialog--00020177/document.md) | ArkUI\_NativeDialogHandle | Defines the handle to the custom dialog box controller of ArkUI on the native side. |
| [ArkUI\_GridItemSize](../../structs/arkui-griditemsize/document.md) | ArkUI\_GridItemSize | Defines the return value structure for the **onGetIrregularSizeByIndex** callback in **Grid** layout options. |
| [ArkUI\_GridItemRect](../../structs/arkui-griditemrect/document.md) | ArkUI\_GridItemRect | Defines the return value structure for the **onGetRectByIndex** callback in **Grid** layout options. |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md) | ArkUI\_GridLayoutOptions | Defines the **Grid** layout options. |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md) | ArkUI\_WaterFlowSectionOption | Defines the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md) | ArkUI\_ListItemSwipeActionItem | Defines the item configuration for **ListItemSwipeActionOption**. |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md) | ArkUI\_ListItemSwipeActionOption | Defines the configuration for **ListItemSwipeActionOption**. |
| [ArkUI\_Context](../../structs/arkui-context/document.md) | ArkUI\_Context | Defines a context object of the ArkUI native UI. |
| [ArkUI\_Context\*](../../structs/arkui-context--00020177/document.md) | ArkUI\_ContextHandle | Defines the handle to the ArkUI native UI context. |
| [ArkUI\_NodeContent\*](../../structs/arkui-nodecontent/document.md) | ArkUI\_NodeContentHandle | Defines the handle to the ArkUI NodeContent instance on the native side. |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md) | ArkUI\_AlignmentRuleOption | Defines the alignment rule in the relative container. |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md) | ArkUI\_GuidelineOption | Defines the ID, direction, and position of a guideline. |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md) | ArkUI\_BarrierOption | Defines the ID, direction, and referenced component of a barrier. |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md) | ArkUI\_ImageAnimatorFrameInfo | Defines the image frame information. |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md) | ArkUI\_ListChildrenMainSize | Defines the **ChildrenMainSize** information of the **List** component. |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md) | ArkUI\_ProgressLinearStyleOption | Defines a struct for the linear progress indicator style. |
| [ArkUI\_CustomProperty](../../structs/arkui-customproperty/document.md) | ArkUI\_CustomProperty | Defines a struct for the custom property information. |
| [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md) | ArkUI\_HostWindowInfo | Defines a struct for the host window information. |
| [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) | ArkUI\_ActiveChildrenInfo | Defines a struct for active child node information. |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md) | ArkUI\_CrossLanguageOption | Defines a cross-language configuration option. |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md) | AbilityBase\_Want | Declares a **Want** object. |
| [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md) | ArkUI\_EmbeddedComponentOption | Defines the **EmbeddedComponentOption** parameter for **EmbeddedComponent**. |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md) | ArkUI\_AccessibilityState | Defines a struct for the component accessibility state. |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md) | ArkUI\_AccessibilityValue | Defines a struct for the component accessibility value. |
| [ArkUI\_SystemFontStyleEvent](../../structs/arkui-systemfontstyleevent/document.md) | ArkUI\_SystemFontStyleEvent | Defines a struct for the system font style event. |
| [ArkUI\_CustomSpanMeasureInfo](../../structs/arkui-customspanmeasureinfo/document.md) | ArkUI\_CustomSpanMeasureInfo | Defines a struct for the measurement information of a custom span. |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md) | ArkUI\_CustomSpanMetrics | Defines a struct for the measurement metrics of a custom span. |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md) | ArkUI\_CustomSpanDrawInfo | Defines a struct for the drawing information of a custom span. |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md) | ArkUI\_SwiperIndicator | Defines the style of the navigation indicator for the [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md) component. |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md) | ArkUI\_SwiperDigitIndicator | Defines the style of the digit navigation indicator for the **Swiper** component. |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md) | ArkUI\_SwiperArrowStyle | Defines the navigation arrow style for the **Swiper** component. |
| [ArkUI\_StyledString\_Descriptor](../../structs/arkui-styledstring-descriptor/document.md) | ArkUI\_StyledString\_Descriptor | Defines a struct for the styled string descriptor object supported by the text component. |
| [ArkUI\_SnapshotOptions](../../structs/arkui-snapshotoptions/document.md) | ArkUI\_SnapshotOptions | Defines snapshot options. |
| [ArkUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md) | ArkUI\_TextPickerRangeContentArray | Defines the data selection list for the text picker. |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md) | ArkUI\_TextCascadePickerRangeContentArray | Defines the content array for a multi-column cascading data picker. |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md) | ArkUI\_VisibleAreaEventOptions | Defines the created instance of visible area change event parameters. |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md) | ArkUI\_PositionEdges | Provides position parameters relative to the boundaries of the container's content area. |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md) | ArkUI\_PixelRoundPolicy | Defines a struct for the component pixel rounding policy. |
| [ArkUI\_ContentTransitionEffect](../../structs/arkui-contenttransitioneffect/document.md) | ArkUI\_ContentTransitionEffect | Defines the content transition effect. |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md) | ArkUI\_ShowCounterConfig | Defines the text input character counter configuration. |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md) | ArkUI\_TextMenuItem | Defines the text menu item structure. |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md) | ArkUI\_TextMenuItemArray | Defines the text menu item array structure. |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md) | ArkUI\_TextEditMenuOptions | Defines the text menu extension structure. |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md) | ArkUI\_TextSelectionMenuOptions | Defines the custom text selection menu structure. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_Alignment](#arkui_alignment) | ArkUI\_Alignment | Enumerates the alignment modes. |
| [ArkUI\_ImageRepeat](#arkui_imagerepeat) | ArkUI\_ImageRepeat | Enumerates the image repeat patterns. |
| [ArkUI\_FontStyle](#arkui_fontstyle) | ArkUI\_FontStyle | Enumerates the font styles. |
| [ArkUI\_FontWeight](#arkui_fontweight) | ArkUI\_FontWeight | Enumerates the font weights. |
| [ArkUI\_TextAlignment](#arkui_textalignment) | ArkUI\_TextAlignment | Enumerates text alignment modes. |
| [ArkUI\_TextVerticalAlignment](#arkui_textverticalalignment) | ArkUI\_TextVerticalAlignment | Enumerates text vertical alignment styles. |
| [ArkUI\_EnterKeyType](#arkui_enterkeytype) | ArkUI\_EnterKeyType | Enumerates the types of the Enter key for a single-line text box. |
| [ArkUI\_TextInputType](#arkui_textinputtype) | ArkUI\_TextInputType | Enumerates the input method type of a single-line text. |
| [ArkUI\_TextAreaType](#arkui_textareatype) | ArkUI\_TextAreaType | Enumerates the input method types of a multi-line text. |
| [ArkUI\_CancelButtonStyle](#arkui_cancelbuttonstyle) | ArkUI\_CancelButtonStyle | Enumerates the styles of the Cancel button. |
| [ArkUI\_XComponentType](#arkui_xcomponenttype) | ArkUI\_XComponentType | Enumerates the types of the **XComponent** component. |
| [ArkUI\_ProgressType](#arkui_progresstype) | ArkUI\_ProgressType | Enumerates the styles of the progress indicator. |
| [ArkUI\_TextDecorationType](#arkui_textdecorationtype) | ArkUI\_TextDecorationType | Enumerates the text decoration types. |
| [ArkUI\_TextDecorationStyle](#arkui_textdecorationstyle) | ArkUI\_TextDecorationStyle | Enumerates the text decoration styles. |
| [ArkUI\_TextCase](#arkui_textcase) | ArkUI\_TextCase | Enumerates the text cases. |
| [ArkUI\_CopyOptions](#arkui_copyoptions) | ArkUI\_CopyOptions | Enumerates the text copy and paste modes. |
| [ArkUI\_ShadowType](#arkui_shadowtype) | ArkUI\_ShadowType | Enumerates shadow types. |
| [ArkUI\_DatePickerMode](#arkui_datepickermode) | ArkUI\_DatePickerMode | Enumerates the column display modes of the date picker. |
| [ArkUI\_TextPickerRangeType](#arkui_textpickerrangetype) | ArkUI\_TextPickerRangeType | Enumerates the types of the text picker. |
| [ArkUI\_AccessibilityCheckedState](#arkui_accessibilitycheckedstate) | ArkUI\_AccessibilityCheckedState | Enumerates the accessibility check box states. |
| [ArkUI\_AccessibilityActionType](#arkui_accessibilityactiontype) | ArkUI\_AccessibilityActionType | Enumerates the accessibility action types. |
| [ArkUI\_EdgeEffect](#arkui_edgeeffect) | ArkUI\_EdgeEffect | Enumerates the effects used at the edges of the component when the boundary of the scrollable content is reached. |
| [ArkUI\_BarState](#arkui_barstate) | ArkUI\_BarState | Enumerates the text control scrollbar states. |
| [ArkUI\_EffectEdge](#arkui_effectedge) | ArkUI\_EffectEdge | Enumerates the edges for which the effect takes effect when the boundary of the scrollable content is reached. |
| [ArkUI\_ScrollDirection](#arkui_scrolldirection) | ArkUI\_ScrollDirection | Enumerates the scrolling directions of the [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md) component. |
| [ArkUI\_ScrollSnapAlign](#arkui_scrollsnapalign) | ArkUI\_ScrollSnapAlign | Enumerates the alignment modes of list items when scrolling ends. |
| [ArkUI\_ScrollBarDisplayMode](#arkui_scrollbardisplaymode) | ArkUI\_ScrollBarDisplayMode | Enumerates the scrollbar display modes. |
| [ArkUI\_Axis](#arkui_axis) | ArkUI\_Axis | Enumerates the scroll directions. |
| [ArkUI\_StickyStyle](#arkui_stickystyle) | ArkUI\_StickyStyle | Enumerates the modes for pinning the header to the top or the footer to the bottom. |
| [ArkUI\_ContentClipMode](#arkui_contentclipmode) | ArkUI\_ContentClipMode | Enumerates the content clipping modes of scrollable components. |
| [ArkUI\_WaterFlowLayoutMode](#arkui_waterflowlayoutmode) | ArkUI\_WaterFlowLayoutMode | Enumerates the layout modes of the [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md) component. |
| [ArkUI\_BorderStyle](#arkui_borderstyle) | ArkUI\_BorderStyle | Enumerates the border styles. |
| [ArkUI\_HitTestMode](#arkui_hittestmode) | ArkUI\_HitTestMode | Enumerates the hit test modes. |
| [ArkUI\_ShadowStyle](#arkui_shadowstyle) | ArkUI\_ShadowStyle | Enumerates shadow styles. |
| [ArkUI\_AnimationCurve](#arkui_animationcurve) | ArkUI\_AnimationCurve | Enumerates the animation curves. |
| [ArkUI\_SwiperArrow](#arkui_swiperarrow) | ArkUI\_SwiperArrow | Enumerates arrow styles of the navigation indicator. |
| [ArkUI\_SwiperNestedScrollMode](#arkui_swipernestedscrollmode) | ArkUI\_SwiperNestedScrollMode | Enumerates the nested scrolling modes of the **Swiper** component and its parent container. |
| [ArkUI\_PageFlipMode](#arkui_pageflipmode) | ArkUI\_PageFlipMode | Enumerates the page flipping modes using the mouse wheel for the **Swiper** component. |
| [ArkUI\_SwiperAnimationMode](#arkui_swiperanimationmode) | ArkUI\_SwiperAnimationMode | Enumerates the animation modes for the **Swiper** component when jumping to the page with the specified index. |
| [ArkUI\_AccessibilityMode](#arkui_accessibilitymode) | ArkUI\_AccessibilityMode | Enumerates the accessibility modes. |
| [ArkUI\_TextCopyOptions](#arkui_textcopyoptions) | ArkUI\_TextCopyOptions | Enumerates copy options, which define whether copy and paste is allowed for text content. |
| [ArkUI\_TextHeightAdaptivePolicy](#arkui_textheightadaptivepolicy) | ArkUI\_TextHeightAdaptivePolicy | Defines how the adaptive height is determined for the text. |
| [ArkUI\_ScrollNestedMode](#arkui_scrollnestedmode) | ArkUI\_ScrollNestedMode | Enumerates nested scrolling modes. |
| [ArkUI\_ScrollEdge](#arkui_scrolledge) | ArkUI\_ScrollEdge | Enumerates the edges to which the component scrolls. |
| [ArkUI\_ScrollAlignment](#arkui_scrollalignment) | ArkUI\_ScrollAlignment | Defines how the list item to scroll to is aligned with the container. |
| [ArkUI\_ScrollState](#arkui_scrollstate) | ArkUI\_ScrollState | Enumerates the scrolling states. |
| [ArkUI\_SliderBlockStyle](#arkui_sliderblockstyle) | ArkUI\_SliderBlockStyle | Enumerates the styles of the slider in the block direction. |
| [ArkUI\_SliderDirection](#arkui_sliderdirection) | ArkUI\_SliderDirection | Enumerates the scroll directions of the slider. |
| [ArkUI\_SliderStyle](#arkui_sliderstyle) | ArkUI\_SliderStyle | Enumerates the slider styles. |
| [ArkUI\_CheckboxShape](#arkui_checkboxshape) | ArkUI\_CheckboxShape | Enumerates the shapes of the check box. |
| [ArkUI\_AnimationPlayMode](#arkui_animationplaymode) | ArkUI\_AnimationPlayMode | Enumerates the animation playback modes. |
| [ArkUI\_ImageSize](#arkui_imagesize) | ArkUI\_ImageSize | Defines the image size. |
| [ArkUI\_AdaptiveColor](#arkui_adaptivecolor) | ArkUI\_AdaptiveColor | Enumerates the adaptive color modes. |
| [ArkUI\_ColorMode](#arkui_colormode) | ArkUI\_ColorMode | Enumerates the color modes. |
| [ArkUI\_SystemColorMode](#arkui_systemcolormode) | ArkUI\_SystemColorMode | Enumerates the system color modes. |
| [ArkUI\_BlurStyle](#arkui_blurstyle) | ArkUI\_BlurStyle | Enumerates the blur styles. |
| [ArkUI\_BlurStyleActivePolicy](#arkui_blurstyleactivepolicy) | ArkUI\_BlurStyleActivePolicy | Enumerates the activation policies for the background blur effect. |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) | ArkUI\_VerticalAlignment | Enumerates the vertical alignment modes. |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) | ArkUI\_HorizontalAlignment | Enumerates the alignment mode in the horizontal direction. |
| [ArkUI\_TextOverflow](#arkui_textoverflow) | ArkUI\_TextOverflow | Enumerates the display modes when the text is too long. |
| [ArkUI\_ImageSpanAlignment](#arkui_imagespanalignment) | ArkUI\_ImageSpanAlignment | Enumerates the alignment mode of the image with the text. |
| [ArkUI\_ObjectFit](#arkui_objectfit) | ArkUI\_ObjectFit | Enumerates the image filling effects of the [Image](../../../arkts-components/images-and-videos/image/document.md) component. |
| [ArkUI\_ImageInterpolation](#arkui_imageinterpolation) | ArkUI\_ImageInterpolation | Enumerates the image interpolation effects. |
| [ArkUI\_DynamicRangeMode](#arkui_dynamicrangemode) | ArkUI\_DynamicRangeMode | Enumerates the dynamic range modes (for example, SDR/HDR) for images, controlling the display range of image brightness and color gamut. |
| [ArkUI\_ImageRotateOrientation](#arkui_imagerotateorientation) | ArkUI\_ImageRotateOrientation | Enumerates image rotation directions. |
| [ArkUI\_BlendMode](#arkui_blendmode) | ArkUI\_BlendMode | Enumerates the blend modes. |
| [ArkUI\_Direction](#arkui_direction) | ArkUI\_Direction | Enumerates the modes in which components are laid out along the main axis of the container. |
| [ArkUI\_ItemAlignment](#arkui_itemalignment) | ArkUI\_ItemAlignment | Enumerates the modes in which components are laid out along the cross axis of the container. |
| [ArkUI\_ColorStrategy](#arkui_colorstrategy) | ArkUI\_ColorStrategy | Enumerates foreground and shadow colors. |
| [ArkUI\_FlexAlignment](#arkui_flexalignment) | ArkUI\_FlexAlignment | Enumerates the vertical alignment modes. |
| [ArkUI\_FlexDirection](#arkui_flexdirection) | ArkUI\_FlexDirection | Enumerates the directions of the main axis in the flex container. |
| [ArkUI\_FlexWrap](#arkui_flexwrap) | ArkUI\_FlexWrap | Defines whether the flex container has a single line or multiple lines. |
| [ArkUI\_Visibility](#arkui_visibility) | ArkUI\_Visibility | Enumerates the visibility values. |
| [ArkUI\_CalendarAlignment](#arkui_calendaralignment) | ArkUI\_CalendarAlignment | Enumerates the alignment modes between the calendar picker and the entry component. |
| [ArkUI\_MaskType](#arkui_masktype) | ArkUI\_MaskType | Enumerates the mask types. A mask is a means to limit the display area of a component. It uses a specific shape to crop the component content so that only the content in the mask area is visible. |
| [ArkUI\_ClipType](#arkui_cliptype) | ArkUI\_ClipType | Enumerates the clipping region types. |
| [ArkUI\_ShapeType](#arkui_shapetype) | ArkUI\_ShapeType | Enumerates custom shape types. |
| [ArkUI\_LinearGradientDirection](#arkui_lineargradientdirection) | ArkUI\_LinearGradientDirection | Enumerates the gradient directions. |
| [ArkUI\_WordBreak](#arkui_wordbreak) | ArkUI\_WordBreak | Enumerates the word break rules. |
| [ArkUI\_EllipsisMode](#arkui_ellipsismode) | ArkUI\_EllipsisMode | Enumerates the ellipsis positions. |
| [ArkUI\_ImageRenderMode](#arkui_imagerendermode) | ArkUI\_ImageRenderMode | Enumerates the image rendering modes. |
| [ArkUI\_TransitionEdge](#arkui_transitionedge) | ArkUI\_TransitionEdge | Enumerates the slide-in and slide-out positions of the component from the screen edge during transition. |
| [ArkUI\_FinishCallbackType](#arkui_finishcallbacktype) | ArkUI\_FinishCallbackType | Enumerates the callback types for [OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](../native-animate-h/document.md#oh_arkui_animatoroption_registeronfinishcallback) in an animation. |
| [ArkUI\_ListItemAlignment](#arkui_listitemalignment) | ArkUI\_ListItemAlignment | Enumerates the alignment modes of items along the cross axis. |
| [ArkUI\_BlendApplyType](#arkui_blendapplytype) | ArkUI\_BlendApplyType | Defines how the specified blend mode is applied. |
| [ArkUI\_LengthMetricUnit](#arkui_lengthmetricunit) | ArkUI\_LengthMetricUnit | Enumerates the component units. |
| [ArkUI\_TextInputContentType](#arkui_textinputcontenttype) | ArkUI\_TextInputContentType | Enumerates the autofill types. |
| [ArkUI\_BarrierDirection](#arkui_barrierdirection) | ArkUI\_BarrierDirection | Enumerates the barrier directions. |
| [ArkUI\_RelativeLayoutChainStyle](#arkui_relativelayoutchainstyle) | ArkUI\_RelativeLayoutChainStyle | Enumerates the chain styles. |
| [ArkUI\_TextInputStyle](#arkui_textinputstyle) | ArkUI\_TextInputStyle | Enumerates the text input styles. |
| [ArkUI\_KeyboardAppearance](#arkui_keyboardappearance) | ArkUI\_KeyboardAppearance | Enumerates the appearance modes of the keyboard when the text box is focused. |
| [ArkUI\_TextDataDetectorType](#arkui_textdatadetectortype) | ArkUI\_TextDataDetectorType | Enumerates the entity types of text recognition. |
| [ArkUI\_ButtonType](#arkui_buttontype) | ArkUI\_ButtonType | Enumerates the button types. |
| [ArkUI\_RenderFit](#arkui_renderfit) | ArkUI\_RenderFit | Enumerates the sizing and positioning behaviors of animated content in its final state. |
| [ArkUI\_SwiperIndicatorType](#arkui_swiperindicatortype) | ArkUI\_SwiperIndicatorType | Enumerates the navigation indicator types of the **Swiper** component. |
| [ArkUI\_AnimationDirection](#arkui_animationdirection) | ArkUI\_AnimationDirection | Enumerates the animation playback directions. |
| [ArkUI\_ListItemSwipeActionState](#arkui_listitemswipeactionstate) | ArkUI\_ListItemSwipeActionState | Enumerates the item states of [swipeAction](../../../arkts-components/scroll-and-swipe/listitem/document.md#swipeaction9) of the [Listitem](../../../arkts-components/scroll-and-swipe/listitem/document.md#listitem10) component. |
| [ArkUI\_ListItemSwipeEdgeEffect](#arkui_listitemswipeedgeeffect) | ArkUI\_ListItemSwipeEdgeEffect | Enumerates the item edge effects of [swipeAction](../../../arkts-components/scroll-and-swipe/listitem/document.md#swipeaction9) of the [Listitem](../../../arkts-components/scroll-and-swipe/listitem/document.md#listitem10) component. |
| [ArkUI\_ListItemSwipeActionDirection](#arkui_listitemswipeactiondirection) | ArkUI\_ListItemSwipeActionDirection | Enumerates the swipe action menu display directions for **ListItem** components. |
| [ArkUI\_AnimationStatus](#arkui_animationstatus) | ArkUI\_AnimationStatus | Enumerates the playback states of the frame-by-frame animation. |
| [ArkUI\_AnimationFillMode](#arkui_animationfillmode) | ArkUI\_AnimationFillMode | Enumerates the states before and after execution of the frame-by-frame animation. |
| [ArkUI\_ErrorCode](#arkui_errorcode) | ArkUI\_ErrorCode | Enumerates the error codes. |
| [ArkUI\_ScrollSource](#arkui_scrollsource) | ArkUI\_ScrollSource | Enumerates scroll sources. |
| [ArkUI\_SafeAreaType](#arkui_safeareatype) | ArkUI\_SafeAreaType | Enumerates the types of expanded safe areas. |
| [ArkUI\_SafeAreaEdge](#arkui_safeareaedge) | ArkUI\_SafeAreaEdge | Enumerates the edges for expanding the safe area. |
| [ArkUI\_FocusMove](#arkui_focusmove) | ArkUI\_FocusMove | Enumerates the focus movement directions. |
| [ArkUI\_ListItemGroupArea](#arkui_listitemgrouparea) | ArkUI\_ListItemGroupArea | Enumerates areas of the **ListItemGroup** component. |
| [ArkUI\_KeyboardAvoidMode](#arkui_keyboardavoidmode) | ArkUI\_KeyboardAvoidMode | Enumerates the soft keyboard avoidance modes. |
| [ArkUI\_HoverModeAreaType](#arkui_hovermodeareatype) | ArkUI\_HoverModeAreaType | Enumerates the types of display areas for the hover mode. |
| [ArkUI\_ExpandMode](#arkui_expandmode) | ArkUI\_ExpandMode | Enumerates the expansion mode of child nodes. |
| [ArkUI\_NavDestinationState](#arkui_navdestinationstate) | ArkUI\_NavDestinationState | Enumerates the **NavDestination** component states. |
| [ArkUI\_RouterPageState](#arkui_routerpagestate) | ArkUI\_RouterPageState | Enumerates the states of a page during routing. |
| [ArkUI\_UIState](#arkui_uistate) | ArkUI\_UIState | Enumerates the UI states of a component, used for handling state-specific styles. |
| [ArkUI\_FocusWrapMode](#arkui_focuswrapmode) | ArkUI\_FocusWrapMode | Enumerates the focus wrap mode of components. |
| [ArkUI\_ItemFillPolicy](#arkui_itemfillpolicy) | ArkUI\_ItemFillPolicy | Enumerates preset column layouts for different responsive breakpoints. |
| [ArkUI\_EdgeDirection](#arkui_edgedirection) | ArkUI\_EdgeDirection | Enumerates rectangle edge directions. |
| [ArkUI\_CornerDirection](#arkui_cornerdirection) | ArkUI\_CornerDirection | Enumerates corner directions. |
| [ArkUI\_LayoutPolicy](#arkui_layoutpolicy) | ArkUI\_LayoutPolicy | Enumerates layout policies. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy) | ArkUI\_PixelRoundCalcPolicy | Enumerates pixel rounding calculation policies. |
| [ArkUI\_GridItemStyle](#arkui_griditemstyle) | ArkUI\_GridItemStyle | Enumerates styles of grid items. |
| [ArkUI\_TextMenuItemId](#arkui_textmenuitemid) | ArkUI\_TextMenuItemId | Enumerates the IDs of text menu items. |
| [ArkUI\_TextSpanType](#arkui_textspantype) | ArkUI\_TextSpanType | Enumerates the text recognition types of a custom text selection menu. |
| [ArkUI\_TextResponseType](#arkui_textresponsetype) | ArkUI\_TextResponseType | Enumerates the response types of a custom text selection menu. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Create()](#oh_arkui_layoutconstraint_create) | \- | Creates layout constraints. |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Copy(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_copy) | \- | Performs a deep copy of a layout constraint. |
| [void\* OH\_ArkUI\_LayoutConstraint\_Dispose(ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_dispose) | \- | Disposes of a layout constraint pointer. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxWidth(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getmaxwidth) | \- | Obtains the maximum width using a layout constraint, in px. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinWidth(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getminwidth) | \- | Obtains the minimum width using a layout constraint, in px. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxHeight(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getmaxheight) | \- | Obtains the maximum height using a layout constraint, in px. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinHeight(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getminheight) | \- | Obtains the minimum height using a layout constraint, in px. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceWidth(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getpercentreferencewidth) | \- | Obtains the width percentage reference using a layout constraint. |
| [int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceHeight(const ArkUI\_LayoutConstraint\* Constraint)](#oh_arkui_layoutconstraint_getpercentreferenceheight) | \- | Obtains the height percentage reference using a layout constraint. |
| [void OH\_ArkUI\_LayoutConstraint\_SetMaxWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setmaxwidth) | \- | Sets the maximum width. |
| [void OH\_ArkUI\_LayoutConstraint\_SetMinWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setminwidth) | \- | Sets the minimum width. |
| [void OH\_ArkUI\_LayoutConstraint\_SetMaxHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setmaxheight) | \- | Sets the maximum height. |
| [void OH\_ArkUI\_LayoutConstraint\_SetMinHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setminheight) | \- | Sets the minimum height. |
| [void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setpercentreferencewidth) | \- | Sets the width percentage reference. |
| [void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)](#oh_arkui_layoutconstraint_setpercentreferenceheight) | \- | Sets the height percentage reference. |
| [void\* OH\_ArkUI\_DrawContext\_GetCanvas(ArkUI\_DrawContext\* context)](#oh_arkui_drawcontext_getcanvas) | \- | Obtains the pointer to a canvas for drawing, which can be converted into the **OH\_Drawing\_Canvas** in the **Drawing** module. |
| [ArkUI\_IntSize OH\_ArkUI\_DrawContext\_GetSize(ArkUI\_DrawContext\* context)](#oh_arkui_drawcontext_getsize) | \- | Obtains the size of a drawing area. |
| [ArkUI\_WaterFlowSectionOption\* OH\_ArkUI\_WaterFlowSectionOption\_Create()](#oh_arkui_waterflowsectionoption_create) | \- | Creates a water flow section configuration. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_Dispose(ArkUI\_WaterFlowSectionOption\* option)](#oh_arkui_waterflowsectionoption_dispose) | \- | Disposes of the pointer to a water flow section configuration. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetSize(ArkUI\_WaterFlowSectionOption\* option, int32\_t size)](#oh_arkui_waterflowsectionoption_setsize) | \- | Sets the array length for a water flow section configuration. |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetSize(ArkUI\_WaterFlowSectionOption\* option)](#oh_arkui_waterflowsectionoption_getsize) | \- | Obtains the array length for a water flow section configuration. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, int32\_t itemCount)](#oh_arkui_waterflowsectionoption_setitemcount) | \- | Sets the number of items in a water flow section. |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetItemCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](#oh_arkui_waterflowsectionoption_getitemcount) | \- | Obtains the number of items in the water flow section that matches the specified index. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, int32\_t crossCount)](#oh_arkui_waterflowsectionoption_setcrosscount) | \- | Sets the number of columns (in a vertical layout) or rows (in a horizontal layout) of a water flow. |
| [int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetCrossCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](#oh_arkui_waterflowsectionoption_getcrosscount) | \- | Obtains the number of columns (in a vertical layout) or rows (in a horizontal layout) of a water flow section. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float columnGap)](#oh_arkui_waterflowsectionoption_setcolumngap) | \- | Sets the gap between columns in the specified water flow section. |
| [float OH\_ArkUI\_WaterFlowSectionOption\_GetColumnGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](#oh_arkui_waterflowsectionoption_getcolumngap) | \- | Obtains the gap between columns in the water flow section that matches the specified index. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float rowGap)](#oh_arkui_waterflowsectionoption_setrowgap) | \- | Sets the gap between rows in the specified water flow section. |
| [float OH\_ArkUI\_WaterFlowSectionOption\_GetRowGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](#oh_arkui_waterflowsectionoption_getrowgap) | \- | Obtains the gap between rows in the water flow section that matches the specified index. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_SetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index,float marginTop, float marginRight, float marginBottom, float marginLeft)](#oh_arkui_waterflowsectionoption_setmargin) | \- | Sets the margins for the specified water flow section. |
| [ArkUI\_Margin OH\_ArkUI\_WaterFlowSectionOption\_GetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)](#oh_arkui_waterflowsectionoption_getmargin) | \- | Obtains the margins of the water flow section that matches the specified index. |
| [void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex (ArkUI\_WaterFlowSectionOption\* option, int32\_t index, float(\*callback)(int32\_t itemIndex))](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex) | \- | Obtains the main axis size of a specified water flow item based on **itemIndex** in the water flow section configuration. To use custom data in the callback, call [OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata). |
| [void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData (ArkUI\_WaterFlowSectionOption\* option, int32\_t index, void\* userData, float (\*callback)(int32\_t itemIndex, void\* userData))](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata) | \- | Obtains the main axis size of a specified water flow item based on **itemIndex** in the water flow section configuration. The difference between this API and [OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex) is that this API allows you to pass custom data (**userData**) and receive the data in the callback function. |
| [ArkUI\_GuidelineOption\* OH\_ArkUI\_GuidelineOption\_Create(int32\_t size)](#oh_arkui_guidelineoption_create) | \- | Creates a guideline configuration for this **RelativeContainer** component. |
| [void OH\_ArkUI\_GuidelineOption\_Dispose(ArkUI\_GuidelineOption\* guideline)](#oh_arkui_guidelineoption_dispose) | \- | Disposes of a guideline configuration. |
| [void OH\_ArkUI\_GuidelineOption\_SetId(ArkUI\_GuidelineOption\* guideline, const char\* value, int32\_t index)](#oh_arkui_guidelineoption_setid) | \- | Sets the ID of a guideline. |
| [void OH\_ArkUI\_GuidelineOption\_SetDirection(ArkUI\_GuidelineOption\* guideline, ArkUI\_Axis value, int32\_t index)](#oh_arkui_guidelineoption_setdirection) | \- | Sets the direction of a guideline. |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionStart(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](#oh_arkui_guidelineoption_setpositionstart) | \- | Sets the distance between a guideline and the left or top of the container. |
| [void OH\_ArkUI\_GuidelineOption\_SetPositionEnd(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)](#oh_arkui_guidelineoption_setpositionend) | \- | Sets the distance between a guideline and the right or bottom of the container. |
| [const char\* OH\_ArkUI\_GuidelineOption\_GetId(ArkUI\_GuidelineOption\* guideline, int32\_t index)](#oh_arkui_guidelineoption_getid) | \- | Obtains the ID of a guideline. |
| [ArkUI\_Axis OH\_ArkUI\_GuidelineOption\_GetDirection(ArkUI\_GuidelineOption\* guideline, int32\_t index)](#oh_arkui_guidelineoption_getdirection) | \- | Obtains the direction of a guideline. |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionStart(ArkUI\_GuidelineOption\* guideline, int32\_t index)](#oh_arkui_guidelineoption_getpositionstart) | \- | Obtains the distance between a guideline and the left or top of the container. |
| [float OH\_ArkUI\_GuidelineOption\_GetPositionEnd(ArkUI\_GuidelineOption\* guideline, int32\_t index)](#oh_arkui_guidelineoption_getpositionend) | \- | Obtains the distance between a guideline and the right or bottom of the container. |
| [ArkUI\_BarrierOption\* OH\_ArkUI\_BarrierOption\_Create(int32\_t size)](#oh_arkui_barrieroption_create) | \- | Creates a barrier configuration for this **RelativeContainer** component. |
| [void OH\_ArkUI\_BarrierOption\_Dispose(ArkUI\_BarrierOption\* barrierStyle)](#oh_arkui_barrieroption_dispose) | \- | Disposes of a barrier configuration. |
| [void OH\_ArkUI\_BarrierOption\_SetId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](#oh_arkui_barrieroption_setid) | \- | Sets the ID of a barrier. |
| [void OH\_ArkUI\_BarrierOption\_SetDirection(ArkUI\_BarrierOption\* barrierStyle, ArkUI\_BarrierDirection value, int32\_t index)](#oh_arkui_barrieroption_setdirection) | \- | Sets the direction of a barrier. |
| [void OH\_ArkUI\_BarrierOption\_SetReferencedId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)](#oh_arkui_barrieroption_setreferencedid) | \- | Sets the referenced components of a barrier. |
| [const char\* OH\_ArkUI\_BarrierOption\_GetId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](#oh_arkui_barrieroption_getid) | \- | Obtains the ID of a barrier. |
| [ArkUI\_BarrierDirection OH\_ArkUI\_BarrierOption\_GetDirection(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](#oh_arkui_barrieroption_getdirection) | \- | Obtains the direction of a barrier. |
| [const char\* OH\_ArkUI\_BarrierOption\_GetReferencedId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index , int32\_t referencedIndex)](#oh_arkui_barrieroption_getreferencedid) | \- | Obtains the referenced components of a barrier. |
| [int32\_t OH\_ArkUI\_BarrierOption\_GetReferencedIdSize(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)](#oh_arkui_barrieroption_getreferencedidsize) | \- | Obtains the number of referenced components of a barrier. |
| [ArkUI\_AlignmentRuleOption\* OH\_ArkUI\_AlignmentRuleOption\_Create()](#oh_arkui_alignmentruleoption_create) | \- | Creates an alignment rule configuration for this **RelativeContainer** component. |
| [void OH\_ArkUI\_AlignmentRuleOption\_Dispose(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_dispose) | \- | Disposes of an alignment rule configuration of this **RelativeContainer** component. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetStart(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](#oh_arkui_alignmentruleoption_setstart) | \- | Sets the left alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetEnd(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](#oh_arkui_alignmentruleoption_setend) | \- | Sets the right alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)](#oh_arkui_alignmentruleoption_setcenterhorizontal) | \- | Sets the horizontal center alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetTop(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](#oh_arkui_alignmentruleoption_settop) | \- | Sets the top alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBottom(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](#oh_arkui_alignmentruleoption_setbottom) | \- | Sets the bottom alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)](#oh_arkui_alignmentruleoption_setcentervertical) | \- | Sets the vertical center alignment mode of a relative layout. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option, float horizontal)](#oh_arkui_alignmentruleoption_setbiashorizontal) | \- | Sets the bias value of the component in the horizontal direction under the anchor constraints. |
| [void OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical(ArkUI\_AlignmentRuleOption\* option, float vertical)](#oh_arkui_alignmentruleoption_setbiasvertical) | \- | Sets the bias value of the component in the vertical direction under the anchor constraints. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetStartId(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getstartid) | \- | Obtains the ID of the left alignment anchor component. |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getstartalignment) | \- | Obtains the left alignment mode. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetEndId(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getendid) | \- | Obtains the ID of the right alignment anchor component. |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getendalignment) | \- | Obtains the right alignment mode. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getcenteridhorizontal) | \- | Obtains the ID of the horizontal center alignment anchor component. |
| [ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getcenteralignmenthorizontal) | \- | Obtains the horizontal center alignment mode. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetTopId(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_gettopid) | \- | Obtains the ID of the top alignment anchor component. |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_gettopalignment) | \- | Obtains the top alignment mode. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetBottomId(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getbottomid) | \- | Obtains the ID of the bottom alignment anchor component. |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getbottomalignment) | \- | Obtains the bottom alignment mode. |
| [const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getcenteridvertical) | \- | Obtains the ID of the vertical center alignment anchor component. |
| [ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getcenteralignmentvertical) | \- | Obtains the vertical center alignment mode. |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getbiashorizontal) | \- | Obtains the bias value in the horizontal direction. |
| [float OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical(ArkUI\_AlignmentRuleOption\* option)](#oh_arkui_alignmentruleoption_getbiasvertical) | \- | Obtains the bias value in the vertical direction. |
| [ArkUI\_SwiperIndicator\* OH\_ArkUI\_SwiperIndicator\_Create(ArkUI\_SwiperIndicatorType type)](#oh_arkui_swiperindicator_create) | \- | Creates a navigation indicator for the [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md) component. |
| [void OH\_ArkUI\_SwiperIndicator\_Dispose(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_dispose) | \- | Disposes of the navigation indicator of this **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetStartPosition(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setstartposition) | \- | Sets the distance between the navigation point and the left edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetStartPosition(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getstartposition) | \- | Obtains the distance between the navigation point and the left edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetTopPosition(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_settopposition) | \- | Sets the distance between the navigation point and the top edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetTopPosition(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_gettopposition) | \- | Obtains the distance between the navigation point and the top edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetEndPosition(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setendposition) | \- | Sets the distance between the navigation point and the right edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetEndPosition(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getendposition) | \- | Obtains the distance between the navigation point and the right edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetBottomPosition(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setbottomposition) | \- | Sets the distance between the navigation point and the bottom edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetBottomPosition(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getbottomposition) | \- | Obtains the distance between the navigation point and the bottom edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator, int32\_t ignoreSize)](#oh_arkui_swiperindicator_setignoresizeofbottom) | \- | Sets whether the **OH\_ArkUI\_SwiperIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator. |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getignoresizeofbottom) | \- | Checks whether the **OH\_ArkUI\_SwiperIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator. |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setitemwidth) | \- | Sets the width of a dot-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemWidth(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getitemwidth) | \- | Obtains the width of a dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setitemheight) | \- | Sets the height of a dot-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetItemHeight(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getitemheight) | \- | Obtains the height of a dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setselecteditemwidth) | \- | Sets the width of the selected dot-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getselecteditemwidth) | \- | Obtains the width of the selected dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)](#oh_arkui_swiperindicator_setselecteditemheight) | \- | Sets the height of the selected dot-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getselecteditemheight) | \- | Obtains the height of the selected dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetMask(ArkUI\_SwiperIndicator\* indicator, int32\_t mask)](#oh_arkui_swiperindicator_setmask) | \- | Sets whether to enable the mask for a dot-style navigation indicator for the **Swiper** component. |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMask(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getmask) | \- | Obtains whether the mask is enabled for a dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t color)](#oh_arkui_swiperindicator_setcolor) | \- | Sets the color of a dot-style navigation indicator for the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetColor(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getcolor) | \- | Obtains the color of a dot-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetSelectedColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t selectedColor)](#oh_arkui_swiperindicator_setselectedcolor) | \- | Sets the color of the selected dot-style navigation indicator for the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperIndicator\_GetSelectedColor(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getselectedcolor) | \- | Obtains the color of the selected dot-style navigation indicator of the **Swiper** component. |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator, int32\_t maxDisplayCount)](#oh_arkui_swiperindicator_setmaxdisplaycount) | \- | Sets the maximum number of dots for the dot-style navigation indicator. |
| [int32\_t OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getmaxdisplaycount) | \- | Obtains the maximum number of dots for the dot-style navigation indicator. |
| [ArkUI\_SwiperDigitIndicator \*OH\_ArkUI\_SwiperDigitIndicator\_Create()](#oh_arkui_swiperdigitindicator_create) | \- | Creates a digit-style navigation indicator for the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_Destroy(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_destroy) | \- | Disposes of the digit-style navigation indicator of this **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](#oh_arkui_swiperdigitindicator_setstartposition) | \- | Sets the start position of the digit-style navigation indicator for the **Swiper** component. This determines the distance from the left edge of the **Swiper** component. For right-to-left scripts, this determines the distance from the right edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getstartposition) | \- | Obtains the start position of the digit-style navigation indicator for the **Swiper** component. This indicates the distance from the left edge of the **Swiper** component. For right-to-left scripts, this indicates the distance from the right edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](#oh_arkui_swiperdigitindicator_settopposition) | \- | Sets the distance from the digit-style navigation indicator to the top edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_gettopposition) | \- | Obtains the distance from the digit-style navigation indicator to the top edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](#oh_arkui_swiperdigitindicator_setendposition) | \- | Sets the end position of the digit-style navigation indicator for the **Swiper** component. This determines the distance from the right edge of the **Swiper** component. For right-to-left scripts, this determines the distance from the left edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getendposition) | \- | Obtains the end position of the digit-style navigation indicator for the **Swiper** component. This indicates the distance from the right edge of the **Swiper** component. For right-to-left scripts, this indicates the distance from the left edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)](#oh_arkui_swiperdigitindicator_setbottomposition) | \- | Sets the distance from the digit-style navigation indicator to the bottom edge of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getbottomposition) | \- | Obtains the distance from the digit-style navigation indicator to the bottom edge of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t color)](#oh_arkui_swiperdigitindicator_setfontcolor) | \- | Sets the font color of the digit-style navigation indicator for the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getfontcolor) | \- | Obtains the font color of the digit-style navigation indicator for the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t selectedColor)](#oh_arkui_swiperdigitindicator_setselectedfontcolor) | \- | Sets the font color of the selected digit-style navigation indicator for the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getselectedfontcolor) | \- | Obtains the font color of the selected digit-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](#oh_arkui_swiperdigitindicator_setfontsize) | \- | Sets the font size of the digit-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getfontsize) | \- | Obtains the font size of the digit-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)](#oh_arkui_swiperdigitindicator_setselectedfontsize) | \- | Sets the font size of the selected digit-style navigation indicator for the **Swiper** component. |
| [float OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getselectedfontsize) | \- | Obtains the font size of the selected digit-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight fontWeight)](#oh_arkui_swiperdigitindicator_setfontweight) | \- | Sets the font weight of the digit-style navigation indicator for the **Swiper** component. |
| [ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getfontweight) | \- | Obtains the font weight of the digit-style navigation indicator of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight selectedFontWeight)](#oh_arkui_swiperdigitindicator_setselectedfontweight) | \- | Sets the font weight of the selected digit-style navigation indicator for the **Swiper** component. |
| [ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getselectedfontweight) | \- | Obtains the font weight of the selected digit-style navigation indicator of the **Swiper** component. |
| [ArkUI\_SwiperArrowStyle \*OH\_ArkUI\_SwiperArrowStyle\_Create()](#oh_arkui_swiperarrowstyle_create) | \- | Creates a navigation arrow for the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_Destroy(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_destroy) | \- | Destroys the navigation arrow pointer of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showBackground)](#oh_arkui_swiperarrowstyle_setshowbackground) | \- | Sets whether to display the background of the navigation arrow for the **Swiper** component. |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getshowbackground) | \- | Checks whether the background of the navigation arrow is displayed for the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showSidebarMiddle)](#oh_arkui_swiperarrowstyle_setshowsidebarmiddle) | \- | Sets the position of the navigation arrow for the **Swiper** component. |
| [int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getshowsidebarmiddle) | \- | Obtains the position of the navigation arrow for the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float backgroundSize)](#oh_arkui_swiperarrowstyle_setbackgroundsize) | \- | Sets the background size for the navigation arrow of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getbackgroundsize) | \- | Obtains the background size of the navigation arrow of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t backgroundColor)](#oh_arkui_swiperarrowstyle_setbackgroundcolor) | \- | Sets the background color for the navigation arrow of the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getbackgroundcolor) | \- | Obtains the background color of the navigation arrow of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float arrowSize)](#oh_arkui_swiperarrowstyle_setarrowsize) | \- | Sets the size for the navigation arrow of the **Swiper** component. |
| [float OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getarrowsize) | \- | Obtains the size of the navigation arrow of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t arrowColor)](#oh_arkui_swiperarrowstyle_setarrowcolor) | \- | Sets the color for the navigation arrow of the **Swiper** component. |
| [uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle)](#oh_arkui_swiperarrowstyle_getarrowcolor) | \- | Obtains the color of the navigation arrow of the **Swiper** component. |
| [void OH\_ArkUI\_SwiperIndicator\_SetSpace(ArkUI\_SwiperIndicator\* indicator, float space)](#oh_arkui_swiperindicator_setspace) | \- | Sets the spacing between navigation points. |
| [float OH\_ArkUI\_SwiperIndicator\_GetSpace(ArkUI\_SwiperIndicator\* indicator)](#oh_arkui_swiperindicator_getspace) | \- | Obtains the spacing between navigation points. |
| [void OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator, int32\_t ignoreSize)](#oh_arkui_swiperdigitindicator_setignoresizeofbottom) | \- | Sets whether the **OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator. |
| [int32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator)](#oh_arkui_swiperdigitindicator_getignoresizeofbottom) | \- | Checks whether the **OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator. |
| [ArkUI\_ListItemSwipeActionItem\* OH\_ArkUI\_ListItemSwipeActionItem\_Create()](#oh_arkui_listitemswipeactionitem_create) | \- | Creates a **ListItemSwipeActionItem** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_Dispose(ArkUI\_ListItemSwipeActionItem\* item)](#oh_arkui_listitemswipeactionitem_dispose) | \- | Disposes of a **ListItemSwipeActionItem** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetContent(ArkUI\_ListItemSwipeActionItem\* item, ArkUI\_NodeHandle node)](#oh_arkui_listitemswipeactionitem_setcontent) | \- | Sets the layout content for a **ListItemSwipeActionItem** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item, float distance)](#oh_arkui_listitemswipeactionitem_setactionareadistance) | \- | Sets the swipe distance threshold for deleting the list item. |
| [float OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item)](#oh_arkui_listitemswipeactionitem_getactionareadistance) | \- | Obtains the swipe distance threshold for deleting the list item. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](#oh_arkui_listitemswipeactionitem_setonenteractionarea) | \- | Sets the callback invoked each time the list item enters the delete area. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](#oh_arkui_listitemswipeactionitem_setonenteractionareawithuserdata) | \- | Sets the callback invoked each time the list item enters the delete area. User-defined data will be passed to the callback event. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](#oh_arkui_listitemswipeactionitem_setonaction) | \- | Sets the callback invoked when the list item is deleted while in the delete area. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](#oh_arkui_listitemswipeactionitem_setonactionwithuserdata) | \- | Sets the callback invoked when the list item is deleted while in the delete area. User-defined data will be passed to the callback event. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())](#oh_arkui_listitemswipeactionitem_setonexitactionarea) | \- | Sets the callback invoked each time the list item exits the delete area. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))](#oh_arkui_listitemswipeactionitem_setonexitactionareawithuserdata) | \- | Sets the callback invoked each time the list item exits the delete area. User-defined data will be passed to the callback event. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange (ArkUI\_ListItemSwipeActionItem\* item,void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState))](#oh_arkui_listitemswipeactionitem_setonstatechange) | \- | Sets the callback invoked when the swipe state of the list item changes. |
| [void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData (ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState, void\* userData))](#oh_arkui_listitemswipeactionitem_setonstatechangewithuserdata) | \- | Sets the callback invoked when the swipe state of the list item changes. User-defined data will be passed to the callback event. |
| [ArkUI\_ListItemSwipeActionOption\* OH\_ArkUI\_ListItemSwipeActionOption\_Create()](#oh_arkui_listitemswipeactionoption_create) | \- | Creates a **ListItemSwipeActionOption** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_Dispose(ArkUI\_ListItemSwipeActionOption\* option)](#oh_arkui_listitemswipeactionoption_dispose) | \- | Disposes of a **ListItemSwipeActionOption** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetStart(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](#oh_arkui_listitemswipeactionoption_setstart) | \- | Sets the layout content for the left edge (for a vertical layout) or top edge (for a horizontal layout) of a **ListItemSwipeActionItem** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)](#oh_arkui_listitemswipeactionoption_setend) | \- | Sets the layout content for the right edge (for a vertical layout) or bottom edge (for a horizontal layout) of a **ListItemSwipeActionItem** instance. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeEdgeEffect edgeEffect)](#oh_arkui_listitemswipeactionoption_setedgeeffect) | \- | Sets the effect used when the scroll boundary is reached. |
| [int32\_t OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option)](#oh_arkui_listitemswipeactionoption_getedgeeffect) | \- | Obtains the effect used when the scroll boundary is reached. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange(ArkUI\_ListItemSwipeActionOption\* option, void (\*callback)(float offset))](#oh_arkui_listitemswipeactionoption_setonoffsetchange) | \- | Sets the callback invoked when the scroll offset changes. |
| [void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData (ArkUI\_ListItemSwipeActionOption\* option, void\* userData, void (\*callback)(float offset, void\* userData))](#oh_arkui_listitemswipeactionoption_setonoffsetchangewithuserdata) | \- | Sets the callback invoked when the scroll offset changes. User-defined data will be passed to the callback event. |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Expand(ArkUI\_NodeHandle node, ArkUI\_ListItemSwipeActionDirection direction)](#oh_arkui_listitemswipeaction_expand) | \- | Expands the swipe action menu for the specified list item. |
| [int32\_t OH\_ArkUI\_ListItemSwipeAction\_Collapse(ArkUI\_NodeHandle node)](#oh_arkui_listitemswipeaction_collapse) | \- | Collapses the swipe action menu for the specified list item. |
| [ArkUI\_AccessibilityState\* OH\_ArkUI\_AccessibilityState\_Create(void)](#oh_arkui_accessibilitystate_create) | \- | Creates an accessibility state. |
| [void OH\_ArkUI\_AccessibilityState\_Dispose(ArkUI\_AccessibilityState\* state)](#oh_arkui_accessibilitystate_dispose) | \- | Disposes of the pointer to an accessibility state. |
| [void OH\_ArkUI\_AccessibilityState\_SetDisabled(ArkUI\_AccessibilityState\* state, int32\_t isDisabled)](#oh_arkui_accessibilitystate_setdisabled) | \- | Sets whether an accessibility state is disabled. |
| [int32\_t OH\_ArkUI\_AccessibilityState\_IsDisabled(ArkUI\_AccessibilityState\* state)](#oh_arkui_accessibilitystate_isdisabled) | \- | Obtains whether an accessibility state is disabled. |
| [void OH\_ArkUI\_AccessibilityState\_SetSelected(ArkUI\_AccessibilityState\* state, int32\_t isSelected)](#oh_arkui_accessibilitystate_setselected) | \- | Sets whether an accessibility state is selected. |
| [int32\_t OH\_ArkUI\_AccessibilityState\_IsSelected(ArkUI\_AccessibilityState\* state)](#oh_arkui_accessibilitystate_isselected) | \- | Obtains whether an accessibility state is selected. |
| [void OH\_ArkUI\_AccessibilityState\_SetCheckedState(ArkUI\_AccessibilityState\* state, int32\_t checkedState)](#oh_arkui_accessibilitystate_setcheckedstate) | \- | Sets the check box state of an accessibility state. |
| [int32\_t OH\_ArkUI\_AccessibilityState\_GetCheckedState(ArkUI\_AccessibilityState\* state)](#oh_arkui_accessibilitystate_getcheckedstate) | \- | Obtains the check box state of an accessibility state. |
| [ArkUI\_AccessibilityValue\* OH\_ArkUI\_AccessibilityValue\_Create(void)](#oh_arkui_accessibilityvalue_create) | \- | Creates an **AccessibilityValue** instance. |
| [void OH\_ArkUI\_AccessibilityValue\_Dispose(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_dispose) | \- | Disposes of the pointer to an **AccessibilityValue** instance. |
| [void OH\_ArkUI\_AccessibilityValue\_SetMin(ArkUI\_AccessibilityValue\* value, int32\_t min)](#oh_arkui_accessibilityvalue_setmin) | \- | Sets the minimum accessibility value. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetMin(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getmin) | \- | Obtains the minimum accessibility value. |
| [void OH\_ArkUI\_AccessibilityValue\_SetMax(ArkUI\_AccessibilityValue\* value, int32\_t max)](#oh_arkui_accessibilityvalue_setmax) | \- | Sets the maximum accessibility value. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetMax(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getmax) | \- | Obtains the maximum accessibility value. |
| [void OH\_ArkUI\_AccessibilityValue\_SetCurrent(ArkUI\_AccessibilityValue\* value, int32\_t current)](#oh_arkui_accessibilityvalue_setcurrent) | \- | Sets the current accessibility value. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetCurrent(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getcurrent) | \- | Obtains the current accessibility value. |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeMin(ArkUI\_AccessibilityValue\* value, int32\_t rangeMin)](#oh_arkui_accessibilityvalue_setrangemin) | \- | Sets the minimum value for accessibility information of the range-based component. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMin(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getrangemin) | \- | Obtains the minimum value for accessibility information of the range-based component. |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeMax(ArkUI\_AccessibilityValue\* value, int32\_t rangeMax)](#oh_arkui_accessibilityvalue_setrangemax) | \- | Sets the maximum value for accessibility information of the range-based component. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMax(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getrangemax) | \- | Obtains the maximum value for accessibility information of the range-based component. |
| [void OH\_ArkUI\_AccessibilityValue\_SetRangeCurrent(ArkUI\_AccessibilityValue\* value, int32\_t rangeCurrent)](#oh_arkui_accessibilityvalue_setrangecurrent) | \- | Sets the current value for accessibility information of the range-based component. |
| [int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeCurrent(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_getrangecurrent) | \- | Obtains the current value for accessibility information of the range-based component. |
| [void OH\_ArkUI\_AccessibilityValue\_SetText(ArkUI\_AccessibilityValue\* value, const char\* text)](#oh_arkui_accessibilityvalue_settext) | \- | Sets the text description of an **AccessibilityValue** instance. |
| [const char\* OH\_ArkUI\_AccessibilityValue\_GetText(ArkUI\_AccessibilityValue\* value)](#oh_arkui_accessibilityvalue_gettext) | \- | Obtains the text description of an **AccessibilityValue** instance. |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString(char\* src)](#oh_arkui_imageanimatorframeinfo_createfromstring) | \- | Creates an image frame information object based on an image path, with the image format being SVG, PNG, or JPG. |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor(ArkUI\_DrawableDescriptor\* drawable)](#oh_arkui_imageanimatorframeinfo_createfromdrawabledescriptor) | \- | Creates an image frame information object based on a **DrawableDescriptor** object, with the image format being Resource or PixelMap. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_dispose) | \- | Disposes of the pointer to an image frame information object. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t width)](#oh_arkui_imageanimatorframeinfo_setwidth) | \- | Sets the image width. |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_getwidth) | \- | Obtains the image width. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t height)](#oh_arkui_imageanimatorframeinfo_setheight) | \- | Sets the image height. |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_getheight) | \- | Obtains the image height. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t top)](#oh_arkui_imageanimatorframeinfo_settop) | \- | Sets the vertical coordinate of an image relative to the upper left corner of the component. |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_gettop) | \- | Obtains the vertical coordinate of an image relative to the upper left corner of the component. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t left)](#oh_arkui_imageanimatorframeinfo_setleft) | \- | Sets the horizontal coordinate of an image relative to the upper left corner of the component. |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_getleft) | \- | Obtains the horizontal coordinate of an image relative to the upper left corner of the component. |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t duration)](#oh_arkui_imageanimatorframeinfo_setduration) | \- | Sets the playback duration of an image. |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](#oh_arkui_imageanimatorframeinfo_getduration) | \- | Obtains the playback duration of an image. |
| [ArkUI\_ListChildrenMainSize\* OH\_ArkUI\_ListChildrenMainSizeOption\_Create()](#oh_arkui_listchildrenmainsizeoption_create) | \- | Creates a **ListChildrenMainSize** instance. |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose(ArkUI\_ListChildrenMainSize\* option)](#oh_arkui_listchildrenmainsizeoption_dispose) | \- | Disposes of a **ListChildrenMainSize** instance. |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option, float defaultMainSize)](#oh_arkui_listchildrenmainsizeoption_setdefaultmainsize) | \- | Sets the default size of the list item in the **List** component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width. |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option)](#oh_arkui_listchildrenmainsizeoption_getdefaultmainsize) | \- | Obtains the default size of the list item in the **List** component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width. |
| [void OH\_ArkUI\_ListChildrenMainSizeOption\_Resize(ArkUI\_ListChildrenMainSize\* option, int32\_t totalSize)](#oh_arkui_listchildrenmainsizeoption_resize) | \- | Adjusts the capacity of the children item size array in the **List** component along the main axis. |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_Splice(ArkUI\_ListChildrenMainSize\* option, int32\_t index, int32\_t deleteCount, int32\_t addCount)](#oh_arkui_listchildrenmainsizeoption_splice) | \- | Adjusts the children item size array in the **List** component along the main axis. |
| [int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index, float mainSize)](#oh_arkui_listchildrenmainsizeoption_updatesize) | \- | Updates the size at the specified index in the child item size array of the **List** component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width. |
| [float OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index)](#oh_arkui_listchildrenmainsizeoption_getmainsize) | \- | Obtains the size at the specified index in the child item size array of the **List** component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width. |
| [ArkUI\_CustomSpanMeasureInfo\* OH\_ArkUI\_CustomSpanMeasureInfo\_Create(void)](#oh_arkui_customspanmeasureinfo_create) | \- | Creates measurement information for this custom span. |
| [void OH\_ArkUI\_CustomSpanMeasureInfo\_Dispose(ArkUI\_CustomSpanMeasureInfo\* info)](#oh_arkui_customspanmeasureinfo_dispose) | \- | Disposes of measurement information of a custom span. |
| [float OH\_ArkUI\_CustomSpanMeasureInfo\_GetFontSize(ArkUI\_CustomSpanMeasureInfo\* info)](#oh_arkui_customspanmeasureinfo_getfontsize) | \- | Obtains the font size of the parent text node of a custom span. |
| [ArkUI\_CustomSpanMetrics\* OH\_ArkUI\_CustomSpanMetrics\_Create(void)](#oh_arkui_customspanmetrics_create) | \- | Creates measurement metrics for this custom span. |
| [void OH\_ArkUI\_CustomSpanMetrics\_Dispose(ArkUI\_CustomSpanMetrics\* metrics)](#oh_arkui_customspanmetrics_dispose) | \- | Disposes of measurement metrics of this custom span. |
| [int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetWidth(ArkUI\_CustomSpanMetrics\* metrics, float width)](#oh_arkui_customspanmetrics_setwidth) | \- | Sets the width for a custom span. |
| [int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetHeight(ArkUI\_CustomSpanMetrics\* metrics, float height)](#oh_arkui_customspanmetrics_setheight) | \- | Sets the height for a custom span. |
| [ArkUI\_CustomSpanDrawInfo\* OH\_ArkUI\_CustomSpanDrawInfo\_Create(void)](#oh_arkui_customspandrawinfo_create) | \- | Creates drawing information for this custom span. |
| [void OH\_ArkUI\_CustomSpanDrawInfo\_Dispose(ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_customspandrawinfo_dispose) | \- | Disposes of drawing information for this custom span. |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetXOffset(ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_customspandrawinfo_getxoffset) | \- | Obtains the x-axis offset of the custom span relative to the mounted component. |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineTop(ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_customspandrawinfo_getlinetop) | \- | Obtains the top margin of the custom span relative to the mounted component. |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineBottom(ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_customspandrawinfo_getlinebottom) | \- | Obtains the bottom margin of the custom span relative to the mounted component. |
| [float OH\_ArkUI\_CustomSpanDrawInfo\_GetBaseline(ArkUI\_CustomSpanDrawInfo\* info)](#oh_arkui_customspandrawinfo_getbaseline) | \- | Obtains the baseline offset of the custom span relative to the mounted component. |
| [void OH\_ArkUI\_CustomProperty\_Destroy(ArkUI\_CustomProperty\* handle)](#oh_arkui_customproperty_destroy) | \- | Destroys a **CustomProperty** instance. |
| [const char\* OH\_ArkUI\_CustomProperty\_GetStringValue(ArkUI\_CustomProperty\* handle)](#oh_arkui_customproperty_getstringvalue) | \- | Obtains the value of a custom property. |
| [const char\* OH\_ArkUI\_HostWindowInfo\_GetName(ArkUI\_HostWindowInfo\* info)](#oh_arkui_hostwindowinfo_getname) | \- | Obtains the window name from a **HostWindowInfo** object. |
| [void OH\_ArkUI\_HostWindowInfo\_Destroy(ArkUI\_HostWindowInfo\* info)](#oh_arkui_hostwindowinfo_destroy) | \- | Destroys a **HostWindowInfo** object. |
| [void OH\_ArkUI\_ActiveChildrenInfo\_Destroy(ArkUI\_ActiveChildrenInfo\* handle)](#oh_arkui_activechildreninfo_destroy) | \- | Destroys an **ActiveChildrenInfo** instance. |
| [ArkUI\_NodeHandle OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex(ArkUI\_ActiveChildrenInfo\* handle, int32\_t index)](#oh_arkui_activechildreninfo_getnodebyindex) | \- | Obtains the child node at the specified index in the specified **ActiveChildrenInfo** instance. |
| [int32\_t OH\_ArkUI\_ActiveChildrenInfo\_GetCount(ArkUI\_ActiveChildrenInfo\* handle)](#oh_arkui_activechildreninfo_getcount) | \- | Obtains the number of nodes in the specified **ActiveChildrenInfo** instance. |
| [ArkUI\_ProgressLinearStyleOption\* OH\_ArkUI\_ProgressLinearStyleOption\_Create(void)](#oh_arkui_progresslinearstyleoption_create) | \- | Creates a **ProgressLinearStyleOption** instance. |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_Destroy(ArkUI\_ProgressLinearStyleOption\* option)](#oh_arkui_progresslinearstyleoption_destroy) | \- | Destroys a **ProgressLinearStyleOption** instance. |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](#oh_arkui_progresslinearstyleoption_setsmootheffectenabled) | \- | Sets whether to enable the smooth progress effect. |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](#oh_arkui_progresslinearstyleoption_setscaneffectenabled) | \- | Sets whether to enable the scan effect. |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option, float strokeWidth)](#oh_arkui_progresslinearstyleoption_setstrokewidth) | \- | Sets the width of the progress indicator. |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option, float strokeRadius)](#oh_arkui_progresslinearstyleoption_setstrokeradius) | \- | Sets the corner radius of the progress indicator. |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](#oh_arkui_progresslinearstyleoption_getsmootheffectenabled) | \- | Obtains the enabled status of the smooth progress effect. |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](#oh_arkui_progresslinearstyleoption_getscaneffectenabled) | \- | Obtains the enabled status of the scan effect. |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option)](#oh_arkui_progresslinearstyleoption_getstrokewidth) | \- | Obtains the stroke width of the progress indicator. |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option)](#oh_arkui_progresslinearstyleoption_getstrokeradius) | \- | Obtains the corner radius of the progress indicator. |
| [ArkUI\_SnapshotOptions\* OH\_ArkUI\_CreateSnapshotOptions()](#oh_arkui_createsnapshotoptions) | \- | Creates a snapshot option object, which must be released using [OH\_ArkUI\_DestroySnapshotOptions()](#oh_arkui_destroysnapshotoptions) when no longer in use. |
| [void OH\_ArkUI\_DestroySnapshotOptions(ArkUI\_SnapshotOptions\* snapshotOptions)](#oh_arkui_destroysnapshotoptions) | \- | Destroys a snapshot option object. |
| [int32\_t OH\_ArkUI\_SnapshotOptions\_SetScale(ArkUI\_SnapshotOptions\* snapshotOptions, float scale)](#oh_arkui_snapshotoptions_setscale) | \- | Sets the scale property in the snapshot options. |
| [ArkUI\_CrossLanguageOption\* OH\_ArkUI\_CrossLanguageOption\_Create(void)](#oh_arkui_crosslanguageoption_create) | \- | Creates an instance of the cross-language configuration option. |
| [void OH\_ArkUI\_CrossLanguageOption\_Destroy(ArkUI\_CrossLanguageOption\* option)](#oh_arkui_crosslanguageoption_destroy) | \- | Destroys an instance of the cross-language configuration option. |
| [void OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option, bool enabled)](#oh_arkui_crosslanguageoption_setattributesettingstatus) | \- | Sets whether cross-language attribute setting is allowed in the configuration option. |
| [bool OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option)](#oh_arkui_crosslanguageoption_getattributesettingstatus) | \- | Checks whether cross-language attribute setting is allowed in the configuration option. |
| [ArkUI\_VisibleAreaEventOptions\* OH\_ArkUI\_VisibleAreaEventOptions\_Create()](#oh_arkui_visibleareaeventoptions_create) | \- | Creates an instance of visible area change event parameters. |
| [void OH\_ArkUI\_VisibleAreaEventOptions\_Dispose(ArkUI\_VisibleAreaEventOptions\* option)](#oh_arkui_visibleareaeventoptions_dispose) | \- | Disposes of an instance of visible area change event parameters. |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t size)](#oh_arkui_visibleareaeventoptions_setratios) | \- | Sets the threshold ratios for visible area changes. |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions \*option, int32\_t value)](#oh_arkui_visibleareaeventoptions_setexpectedupdateinterval) | \- | Sets the expected update interval for visible area changes. |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions \*option, bool measureFromViewport)](#oh_arkui_visibleareaeventoptions_setmeasurefromviewport) | \- | Sets the visible area calculation mode. |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t\* size)](#oh_arkui_visibleareaeventoptions_getratios) | \- | Obtains the threshold ratios for visible area changes. |
| [int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions\* option)](#oh_arkui_visibleareaeventoptions_getexpectedupdateinterval) | \- | Obtains the expected update interval for visible area changes. |
| [bool OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions\* option)](#oh_arkui_visibleareaeventoptions_getmeasurefromviewport) | \- | Obtains the visible area calculation mode. |
| [ArkUI\_TextPickerRangeContentArray\* OH\_ArkUI\_TextPickerRangeContentArray\_Create(int32\_t length)](#oh_arkui_textpickerrangecontentarray_create) | \- | Creates a **TextPickerRangeContent** array object. |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* icon, int32\_t index)](#oh_arkui_textpickerrangecontentarray_seticonatindex) | \- | Sets the icon data at the specified position in the **TextPickerRangeContent** array. |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* text, int32\_t index)](#oh_arkui_textpickerrangecontentarray_settextatindex) | \- | Sets the text data at the specified position in the **TextPickerRangeContent** array. |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_Destroy(ArkUI\_TextPickerRangeContentArray\* handle)](#oh_arkui_textpickerrangecontentarray_destroy) | \- | Destroys a **TextPickerRangeContent** array object. |
| [ArkUI\_TextCascadePickerRangeContentArray\* OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create(int32\_t length)](#oh_arkui_textcascadepickerrangecontentarray_create) | \- | Creates a **TextCascadePickerRangeContent** array object. |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, char\* text, int32\_t index)](#oh_arkui_textcascadepickerrangecontentarray_settextatindex) | \- | Sets the text data at the specified position in the **TextCascadePickerRangeContent** array. |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, ArkUI\_TextCascadePickerRangeContentArray\* child, int32\_t index)](#oh_arkui_textcascadepickerrangecontentarray_setchildatindex) | \- | Sets the child data at the specified position in the **TextCascadePickerRangeContent** array. |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy (ArkUI\_TextCascadePickerRangeContentArray\* handle)](#oh_arkui_textcascadepickerrangecontentarray_destroy) | \- | Destroys a **TextCascadePickerRangeContent** array object. |
| [ArkUI\_EmbeddedComponentOption\* OH\_ArkUI\_EmbeddedComponentOption\_Create()](#oh_arkui_embeddedcomponentoption_create) | \- | Creates an **EmbeddedComponent** option object. |
| [void OH\_ArkUI\_EmbeddedComponentOption\_Dispose(ArkUI\_EmbeddedComponentOption\* option)](#oh_arkui_embeddedcomponentoption_dispose) | \- | Disposes of an **EmbeddedComponent** option object. |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnError (ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, const char\* name, const char\* message))](#oh_arkui_embeddedcomponentoption_setonerror) | \- | Sets the **onError** callback for the **EmbeddedComponent** component. This callback is triggered when an error occurs during the running of the **EmbeddedComponent** component. |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated (ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, AbilityBase\_Want\* want))](#oh_arkui_embeddedcomponentoption_setonterminated) | \- | Sets the **onTerminated** callback for the **EmbeddedComponent** component. This callback is triggered when the **EmbeddedComponent** component exits properly. |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Create()](#oh_arkui_positionedges_create) | \- | Creates a **PositionEdges** object. |
| [ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Copy(const ArkUI\_PositionEdges\* edges)](#oh_arkui_positionedges_copy) | \- | Deeply copies a **PositionEdges** attribute object. |
| [void OH\_ArkUI\_PositionEdges\_Dispose(ArkUI\_PositionEdges\* edges)](#oh_arkui_positionedges_dispose) | \- | Disposes of the **PositionEdges** object. |
| [void OH\_ArkUI\_PositionEdges\_SetTop(ArkUI\_PositionEdges\* edges, float value)](#oh_arkui_positionedges_settop) | \- | Sets the value of the **PositionEdges** object in the top direction. |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetTop(ArkUI\_PositionEdges\* edges, float\* value)](#oh_arkui_positionedges_gettop) | \- | Obtains the value of the **PositionEdges** object in the top direction. |
| [void OH\_ArkUI\_PositionEdges\_SetLeft(ArkUI\_PositionEdges\* edges, float value)](#oh_arkui_positionedges_setleft) | \- | Sets the value of the **PositionEdges** object in the left direction. |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetLeft(ArkUI\_PositionEdges\* edges, float\* value)](#oh_arkui_positionedges_getleft) | \- | Obtains the value of the **PositionEdges** object in the left direction. |
| [void OH\_ArkUI\_PositionEdges\_SetBottom(ArkUI\_PositionEdges\* edges, float value)](#oh_arkui_positionedges_setbottom) | \- | Sets the value of the **PositionEdges** object in the bottom direction. |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetBottom(ArkUI\_PositionEdges\* edges, float\* value)](#oh_arkui_positionedges_getbottom) | \- | Obtains the value of the **PositionEdges** object in the bottom direction. |
| [void OH\_ArkUI\_PositionEdges\_SetRight(ArkUI\_PositionEdges\* edges, float value)](#oh_arkui_positionedges_setright) | \- | Sets the value of the **PositionEdges** object in the right direction. |
| [int32\_t OH\_ArkUI\_PositionEdges\_GetRight(ArkUI\_PositionEdges\* edges, float\* value)](#oh_arkui_positionedges_getright) | \- | Obtains the value of the **PositionEdges** object in the right direction. |
| [ArkUI\_PixelRoundPolicy\* OH\_ArkUI\_PixelRoundPolicy\_Create()](#oh_arkui_pixelroundpolicy_create) | \- | Creates a **PixelRoundPolicy** attribute object. |
| [void OH\_ArkUI\_PixelRoundPolicy\_Dispose(ArkUI\_PixelRoundPolicy\* policy)](#oh_arkui_pixelroundpolicy_dispose) | \- | Disposes of the **PixelRoundPolicy** object. |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](#oh_arkui_pixelroundpolicy_settop) | \- | Sets the top edge pixel rounding policy for the **PixelRoundPolicy** object. |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](#oh_arkui_pixelroundpolicy_gettop) | \- | Obtains the top edge pixel rounding policy from the **PixelRoundPolicy** object. |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](#oh_arkui_pixelroundpolicy_setstart) | \- | Sets the start edge pixel rounding policy for the **PixelRoundPolicy** object. |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](#oh_arkui_pixelroundpolicy_getstart) | \- | Obtains the start edge pixel rounding policy from the **PixelRoundPolicy** object. |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](#oh_arkui_pixelroundpolicy_setbottom) | \- | Sets the bottom edge pixel rounding policy for the **PixelRoundPolicy** object. |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](#oh_arkui_pixelroundpolicy_getbottom) | \- | Obtains the bottom edge pixel rounding policy from the **PixelRoundPolicy** object. |
| [void OH\_ArkUI\_PixelRoundPolicy\_SetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)](#oh_arkui_pixelroundpolicy_setend) | \- | Sets the end edge pixel rounding policy for the **PixelRoundPolicy** object. |
| [int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)](#oh_arkui_pixelroundpolicy_getend) | \- | Obtains the end edge pixel rounding policy from the **PixelRoundPolicy** object. |
| [ArkUI\_ContentTransitionEffect\* OH\_ArkUI\_ContentTransitionEffect\_Create(int32\_t type)](#oh_arkui_contenttransitioneffect_create) | \- | Creates a **ContentTransitionEffect** attribute object. |
| [ArkUI\_GridLayoutOptions\* OH\_ArkUI\_GridLayoutOptions\_Create()](#oh_arkui_gridlayoutoptions_create) | \- | Creates **Grid** layout options. |
| [void OH\_ArkUI\_GridLayoutOptions\_Dispose(ArkUI\_GridLayoutOptions\* option)](#oh_arkui_gridlayoutoptions_dispose) | \- | Disposes of **Grid** layout options. |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t size)](#oh_arkui_gridlayoutoptions_setirregularindexes) | \- | Sets the irregular grid item index array for the grid layout. |
| [int32\_t OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t\* size)](#oh_arkui_gridlayoutoptions_getirregularindexes) | \- | Obtains the irregular grid item index array for the grid layout. When **OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback** is not set, the grid item specified in this parameter occupies an entire row of the grid that scrolls vertically or an entire column of the grid that scrolls horizontally. |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemSize(\*callback)(int32\_t itemIndex, void\* userData))](#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback) | \- | Registers a callback to obtain the row and column span for the grid item at the specified index. |
| [void OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData))](#oh_arkui_gridlayoutoptions_registergetrectbyindexcallback) | \- | Registers a callback to obtain the starting row, starting column, row span, and column span for the grid item at the specified index. |
| [ArkUI\_TextMenuItem\* OH\_ArkUI\_TextMenuItem\_Create()](#oh_arkui_textmenuitem_create) | \- | Creates a text menu item object. |
| [void OH\_ArkUI\_TextMenuItem\_Dispose(ArkUI\_TextMenuItem\* textMenuItem)](#oh_arkui_textmenuitem_dispose) | \- | Releases a text menu item object. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetContent(ArkUI\_TextMenuItem\* item, const char\* content)](#oh_arkui_textmenuitem_setcontent) | \- | Sets the title of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetContent(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_textmenuitem_getcontent) | \- | Obtains the title of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetIcon(ArkUI\_TextMenuItem\* item, const char\* icon)](#oh_arkui_textmenuitem_seticon) | \- | Sets the icon path of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetIcon(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_textmenuitem_geticon) | \- | Obtains the icon path of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetLabelInfo(ArkUI\_TextMenuItem\* item, const char\* labelInfo)](#oh_arkui_textmenuitem_setlabelinfo) | \- | Sets the shortcut hint for a text menu item, for example, the shortcut hint for the **Copy** menu item can be set to **Ctrl+C**. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetLabelInfo(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_arkui_textmenuitem_getlabelinfo) | \- | Obtains the shortcut hint for a text menu item, for example, the shortcut hint for the **Copy** menu item is typically **Ctrl+C**. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetId(ArkUI\_TextMenuItem\* item, int32\_t id)](#oh_arkui_textmenuitem_setid) | \- | Sets the ID of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetId(const ArkUI\_TextMenuItem\* item, int32\_t\* id)](#oh_arkui_textmenuitem_getid) | \- | Obtains the ID of a text menu item. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetSize(ArkUI\_TextMenuItemArray\* items, int32\_t\* size)](#oh_arkui_textmenuitemarray_getsize) | \- | Obtains the size of the text menu item array. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetItem(ArkUI\_TextMenuItemArray\* items, int32\_t index, ArkUI\_TextMenuItem\*\* item)](#oh_arkui_textmenuitemarray_getitem) | \- | Obtains the text menu item at a specified index from the text menu item array. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Insert(ArkUI\_TextMenuItemArray\* items, ArkUI\_TextMenuItem\* item, int32\_t index)](#oh_arkui_textmenuitemarray_insert) | \- | Inserts a text menu item at a specified index into the text menu item array. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Erase(ArkUI\_TextMenuItemArray\* items, int32\_t index)](#oh_arkui_textmenuitemarray_erase) | \- | Deletes the text menu item at a specified index from the text menu item array. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Clear(ArkUI\_TextMenuItemArray\* items)](#oh_arkui_textmenuitemarray_clear) | \- | Clears all text menu items in the text menu item array. |
| [ArkUI\_TextEditMenuOptions\* OH\_ArkUI\_TextEditMenuOptions\_Create()](#oh_arkui_texteditmenuoptions_create) | \- | Creates a text menu extension object. |
| [void OH\_ArkUI\_TextEditMenuOptions\_Dispose(ArkUI\_TextEditMenuOptions\* editMenuOptions)](#oh_arkui_texteditmenuoptions_dispose) | \- | Releases a text menu extension object. |
| [typedef void (\*ArkUI\_TextCreateMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)](#arkui_textcreatemenucallback) | ArkUI\_TextCreateMenuCallback | Callback for the text menu creation event. This callback is triggered when a text menu is created, allowing you to set menu data in it. |
| [typedef void (\*ArkUI\_TextPrepareMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)](#arkui_textpreparemenucallback) | ArkUI\_TextPrepareMenuCallback | Callback for the text menu preparation event. This callback is called when the text selection area changes and before the menu is displayed, allowing you to set menu data in it. |
| [typedef bool (\*ArkUI\_TextMenuItemClickCallback)(const ArkUI\_TextMenuItem\* item,int32\_t start, int32\_t end, void\* userData)](#arkui_textmenuitemclickcallback) | ArkUI\_TextMenuItemClickCallback | Callback for the text menu item click event. This callback is called when a menu item is clicked. You can intercept the default processing behavior in this callback. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnCreateMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextCreateMenuCallback cb)](#oh_arkui_texteditmenuoptions_registeroncreatemenucallback) | \- | Registers the callback for creating text menus. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnPrepareMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextPrepareMenuCallback cb)](#oh_arkui_texteditmenuoptions_registeronpreparemenucallback) | \- | Registers the callback for preparing text menus. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnMenuItemClickCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextMenuItemClickCallback cb)](#oh_arkui_texteditmenuoptions_registeronmenuitemclickcallback) | \- | Registers the callback for text menu item clicks. |
| [ArkUI\_TextSelectionMenuOptions\* OH\_ArkUI\_TextSelectionMenuOptions\_Create()](#oh_arkui_textselectionmenuoptions_create) | \- | Creates a custom text selection menu object. |
| [void OH\_ArkUI\_TextSelectionMenuOptions\_Dispose(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions)](#oh_arkui_textselectionmenuoptions_dispose) | \- | Releases a custom text selection menu object. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType textSpanType)](#oh_arkui_textselectionmenuoptions_setspantype) | \- | Sets the text recognition type of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType\* spanType)](#oh_arkui_textselectionmenuoptions_getspantype) | \- | Obtains the text recognition type of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle node)](#oh_arkui_textselectionmenuoptions_setcontentnode) | \- | Sets the content node of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle\* node)](#oh_arkui_textselectionmenuoptions_getcontentnode) | \- | Obtains the content node of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType responseType)](#oh_arkui_textselectionmenuoptions_setresponsetype) | \- | Sets the response type of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType\* responseType)](#oh_arkui_textselectionmenuoptions_getresponsetype) | \- | Obtains the response type of a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))](#oh_arkui_textselectionmenuoptions_registeronmenushowcallback) | \- | Registers the callback for the event of showing a custom text selection menu. |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))](#oh_arkui_textselectionmenuoptions_registeronmenuhidecallback) | \- | Registers the callback for the event of hiding a custom text selection menu. |

#### Enum Description

#### \[h2\]ArkUI\_Alignment

enum ArkUI\_Alignment

**Description**

Enumerates the alignment modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ALIGNMENT\_TOP\_START = 0 | Top start. This is the default value. |
| ARKUI\_ALIGNMENT\_TOP = 1 | Top center. |
| ARKUI\_ALIGNMENT\_TOP\_END = 2 | Top end. |
| ARKUI\_ALIGNMENT\_START = 3 | Vertically centered start. |
| ARKUI\_ALIGNMENT\_CENTER = 4 | Horizontally and vertically centered. |
| ARKUI\_ALIGNMENT\_END = 5 | Vertically centered end. |
| ARKUI\_ALIGNMENT\_BOTTOM\_START = 6 | Bottom start. |
| ARKUI\_ALIGNMENT\_BOTTOM = 7 | Horizontally centered on the bottom. |
| ARKUI\_ALIGNMENT\_BOTTOM\_END = 8 | Bottom end. |

#### \[h2\]ArkUI\_ImageRepeat

enum ArkUI\_ImageRepeat

**Description**

Enumerates the image repeat patterns.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_IMAGE\_REPEAT\_NONE = 0 | The image is not repeatedly drawn. |
| ARKUI\_IMAGE\_REPEAT\_X = 1 | The image is repeatedly drawn only along the x-axis. |
| ARKUI\_IMAGE\_REPEAT\_Y = 2 | The image is repeatedly drawn only along the y-axis. |
| ARKUI\_IMAGE\_REPEAT\_XY = 3 | The image is repeatedly drawn along both axes. |

#### \[h2\]ArkUI\_FontStyle

enum ArkUI\_FontStyle

**Description**

Enumerates the font styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FONT\_STYLE\_NORMAL = 0 | Standard font style. |
| ARKUI\_FONT\_STYLE\_ITALIC = 1 | Italic font style. |

#### \[h2\]ArkUI\_FontWeight

enum ArkUI\_FontWeight

**Description**

Enumerates the font weights.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FONT\_WEIGHT\_W100 = 0 | 100 |
| ARKUI\_FONT\_WEIGHT\_W200 = 1 | 200 |
| ARKUI\_FONT\_WEIGHT\_W300 = 2 | 300 |
| ARKUI\_FONT\_WEIGHT\_W400 = 3 | 400 |
| ARKUI\_FONT\_WEIGHT\_W500 = 4 | 500 |
| ARKUI\_FONT\_WEIGHT\_W600 = 5 | 600 |
| ARKUI\_FONT\_WEIGHT\_W700 = 6 | 700 |
| ARKUI\_FONT\_WEIGHT\_W800 = 7 | 800 |
| ARKUI\_FONT\_WEIGHT\_W900 = 8 | 900 |
| ARKUI\_FONT\_WEIGHT\_BOLD = 9 | The font weight is bold. |
| ARKUI\_FONT\_WEIGHT\_NORMAL = 10 | The font weight is normal. |
| ARKUI\_FONT\_WEIGHT\_BOLDER = 11 | The font weight is bolder. |
| ARKUI\_FONT\_WEIGHT\_LIGHTER = 12 | The font weight is lighter. |
| ARKUI\_FONT\_WEIGHT\_MEDIUM = 13 | The font weight is medium. |
| ARKUI\_FONT\_WEIGHT\_REGULAR = 14 | The font weight is normal. |

#### \[h2\]ArkUI\_TextAlignment

enum ArkUI\_TextAlignment

**Description**

Enumerates text alignment modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_ALIGNMENT\_START = 0 | Aligned with the start. |
| ARKUI\_TEXT\_ALIGNMENT\_CENTER = 1 | Horizontally centered. |
| ARKUI\_TEXT\_ALIGNMENT\_END = 2 | Aligned with the end. |
| ARKUI\_TEXT\_ALIGNMENT\_JUSTIFY = 3 | Aligned with both margins. |

#### \[h2\]ArkUI\_TextVerticalAlignment

enum ArkUI\_TextVerticalAlignment

**Description**

Enumerates text vertical alignment styles.

**Since**: 20

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BASELINE = 0 | Aligned to the baseline. |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BOTTOM = 1 | Bottom aligned. |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_CENTER = 2 | The list item is centered along |
| ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_TOP = 3 | Top aligned. |

#### \[h2\]ArkUI\_TextContentAlign

enum ArkUI\_TextContentAlign

**Description**

Enumerates vertical alignment styles in the text content area.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_TOP = 0 | Top aligned. |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_CENTER = 1 | The list item is centered along |
| ARKUI\_TEXT\_CONTENT\_ALIGN\_BOTTOM = 2 | Bottom aligned. |

#### \[h2\]ArkUI\_EnterKeyType

enum ArkUI\_EnterKeyType

**Description**

Enumerates the types of the Enter key for a single-line text box.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ENTER\_KEY\_TYPE\_GO = 2 | The Enter key is labeled "Go." |
| ARKUI\_ENTER\_KEY\_TYPE\_SEARCH = 3 | The Enter key is labeled "Search." |
| ARKUI\_ENTER\_KEY\_TYPE\_SEND = 4 | The Enter key is labeled "Send." |
| ARKUI\_ENTER\_KEY\_TYPE\_NEXT = 5 | The Enter key is labeled "Next." |
| ARKUI\_ENTER\_KEY\_TYPE\_DONE = 6 | The Enter key is labeled "Done." |
| ARKUI\_ENTER\_KEY\_TYPE\_PREVIOUS = 7 | The Enter key is labeled "Previous." |
| ARKUI\_ENTER\_KEY\_TYPE\_NEW\_LINE = 8 | The Enter key is labeled "Return." |

#### \[h2\]ArkUI\_TextInputType

enum ArkUI\_TextInputType

**Description**

Enumerates the input method type of a single-line text.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXTINPUT\_TYPE\_NORMAL = 0 | Normal input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER = 2 | Number input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_PHONE\_NUMBER = 3 | Phone number input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_EMAIL = 5 | Email address input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_PASSWORD = 7 | Password input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD = 8 | Numeric password input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_SCREEN\_LOCK\_PASSWORD = 9 | Lock screen password input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_USER\_NAME = 10 | Username input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD = 11 | New password input mode. |
| ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_DECIMAL = 12 | Number input mode with a decimal point. |
| ARKUI\_TEXTINPUT\_TYPE\_ONE\_TIME\_CODE = 14 | 
Verification code input mode.

**Since**: 20

 |

#### \[h2\]ArkUI\_TextAreaType

enum ArkUI\_TextAreaType

**Description**

Enumerates the input method types of a multi-line text.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXTAREA\_TYPE\_NORMAL = 0 | Normal input mode. |
| ARKUI\_TEXTAREA\_TYPE\_NUMBER = 2 | Number input mode. |
| ARKUI\_TEXTAREA\_TYPE\_PHONE\_NUMBER = 3 | Phone number input mode. |
| ARKUI\_TEXTAREA\_TYPE\_EMAIL = 5 | Email address input mode. |
| ARKUI\_TEXTAREA\_TYPE\_ONE\_TIME\_CODE = 14 | 
Verification code input mode.

**Since**: 20

 |

#### \[h2\]ArkUI\_CancelButtonStyle

enum ArkUI\_CancelButtonStyle

**Description**

Enumerates the styles of the Cancel button.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_CANCELBUTTON\_STYLE\_CONSTANT = 0 | The Cancel button is always displayed. |
| ARKUI\_CANCELBUTTON\_STYLE\_INVISIBLE = 1 | The Cancel button is always hidden. |
| ARKUI\_CANCELBUTTON\_STYLE\_INPUT = 2 | The Cancel button is displayed when there is text input. |

#### \[h2\]ArkUI\_XComponentType

enum ArkUI\_XComponentType

**Description**

Enumerates the types of the **XComponent** component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_XCOMPONENT\_TYPE\_SURFACE = 0 | The custom content of EGL/OpenGL ES and media data is displayed individually on the screen. |
| ARKUI\_XCOMPONENT\_TYPE\_TEXTURE = 2 | The custom content of EGL/OpenGL ES and media data is grouped and displayed together with content of the component. |

#### \[h2\]ArkUI\_ProgressType

enum ArkUI\_ProgressType

**Description**

Enumerates the styles of the progress indicator.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_PROGRESS\_TYPE\_LINEAR = 0 | Linear type. |
| ARKUI\_PROGRESS\_TYPE\_RING = 1 | Ring style without scale marks. |
| ARKUI\_PROGRESS\_TYPE\_ECLIPSE = 2 | Eclipse style. |
| ARKUI\_PROGRESS\_TYPE\_SCALE\_RING = 3 | Ring style with scale marks. |
| ARKUI\_PROGRESS\_TYPE\_CAPSULE = 4 | Capsule style. |

#### \[h2\]ArkUI\_TextDecorationType

enum ArkUI\_TextDecorationType

**Description**

Enumerates the text decoration types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_DECORATION\_TYPE\_NONE = 0 | No text decoration. |
| ARKUI\_TEXT\_DECORATION\_TYPE\_UNDERLINE = 1 | Line under the text. |
| ARKUI\_TEXT\_DECORATION\_TYPE\_OVERLINE = 2 | Line over the text. |
| ARKUI\_TEXT\_DECORATION\_TYPE\_LINE\_THROUGH = 3 | Line through the text. |

#### \[h2\]ArkUI\_TextDecorationStyle

enum ArkUI\_TextDecorationStyle

**Description**

Enumerates the text decoration styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_DECORATION\_STYLE\_SOLID = 0 | Single solid line. |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DOUBLE = 1 | Double solid line. |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DOTTED = 2 | Dotted line. |
| ARKUI\_TEXT\_DECORATION\_STYLE\_DASHED = 3 | Dashed style. |
| ARKUI\_TEXT\_DECORATION\_STYLE\_WAVY = 4 | Wavy line. |

#### \[h2\]ArkUI\_TextCase

enum ArkUI\_TextCase

**Description**

Enumerates the text cases.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_CASE\_NORMAL = 0 | The original case of the text is retained. |
| ARKUI\_TEXT\_CASE\_LOWER = 1 | All letters in the text are in lowercase. |
| ARKUI\_TEXT\_CASE\_UPPER = 2 | All letters in the text are in uppercase. |

#### \[h2\]ArkUI\_CopyOptions

enum ArkUI\_CopyOptions

**Description**

Enumerates the text copy and paste modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_COPY\_OPTIONS\_NONE = 0 | Copy is not allowed. |
| ARKUI\_COPY\_OPTIONS\_IN\_APP = 1 | Intra-application copy is allowed. |
| ARKUI\_COPY\_OPTIONS\_LOCAL\_DEVICE = 2 | Intra-device copy is allowed. |
| ARKUI\_COPY\_OPTIONS\_CROSS\_DEVICE = 3 | Cross-device copy is allowed. |

#### \[h2\]ArkUI\_ShadowType

enum ArkUI\_ShadowType

**Description**

Enumerates shadow types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SHADOW\_TYPE\_COLOR = 0 | Color shadow. |
| ARKUI\_SHADOW\_TYPE\_BLUR = 1 | Blur shadow. |

#### \[h2\]ArkUI\_DatePickerMode

enum ArkUI\_DatePickerMode

**Description**

Enumerates the column display modes of the date picker.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_DATEPICKER\_MODE\_DATE = 0 | Default value. The date displays three columns: year, month, and day. |
| ARKUI\_DATEPICKER\_YEAR\_AND\_MONTH = 1 | The date displays two columns: year and month. |
| ARKUI\_DATEPICKER\_MONTH\_AND\_DAY = 2 | The date displays two columns: month and day. |

#### \[h2\]ArkUI\_TextPickerRangeType

enum ArkUI\_TextPickerRangeType

**Description**

Enumerates the types of the text picker.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE = 0 | Single-column text picker. |
| ARKUI\_TEXTPICKER\_RANGETYPE\_MULTI = 1 | Multi-column text picker. |
| ARKUI\_TEXTPICKER\_RANGETYPE\_RANGE\_CONTENT = 2 | Single-column text picker with image resources. |
| ARKUI\_TEXTPICKER\_RANGETYPE\_CASCADE\_RANGE\_CONTENT = 3 | Interconnected multi-column text picker. |

#### \[h2\]ArkUI\_AccessibilityCheckedState

enum ArkUI\_AccessibilityCheckedState

**Description**

Enumerates the accessibility check box states.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_UNCHECKED = 0 | The check box is not selected. |
| ARKUI\_ACCESSIBILITY\_CHECKED = 1 | The check box is selected. |

#### \[h2\]ArkUI\_AccessibilityActionType

enum ArkUI\_AccessibilityActionType

**Description**

Enumerates the accessibility action types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_ACTION\_CLICK = 1 << 0 | Tapping |
| ARKUI\_ACCESSIBILITY\_ACTION\_LONG\_CLICK = 1 << 1 | Long press |
| ARKUI\_ACCESSIBILITY\_ACTION\_CUT = 1 << 2 | Cut. |
| ARKUI\_ACCESSIBILITY\_ACTION\_COPY = 1 << 3 | Copy. |
| ARKUI\_ACCESSIBILITY\_ACTION\_PASTE = 1 << 4 | Paste. |

#### \[h2\]ArkUI\_EdgeEffect

enum ArkUI\_EdgeEffect

**Description**

Enumerates the effects used at the edges of the component when the boundary of the scrollable content is reached. The default value is **ARKUI\_EDGE\_EFFECT\_NONE** for the **Grid**, **Scroll**, and **WaterFlow** components, and **ARKUI\_EDGE\_EFFECT\_SPRING** for the **List** component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_EDGE\_EFFECT\_SPRING = 0 | Spring effect. When at one of the edges, the component can move beyond the bounds based on the initial speed or through touches, and produces a bounce effect when the user releases their finger. |
| ARKUI\_EDGE\_EFFECT\_FADE = 1 | Fade effect. When at one of the edges, the component produces a fade effect. |
| ARKUI\_EDGE\_EFFECT\_NONE = 2 | No effect when the component is at one of the edges. |

#### \[h2\]ArkUI\_BarState

enum ArkUI\_BarState

**Description**

Enumerates the text control scrollbar states.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_BAR\_STATE\_OFF = 0 | Not displayed. |
| ARKUI\_BAR\_STATE\_AUTO = 1 | Displayed when the screen is touched and hidden after 2s. |
| ARKUI\_BAR\_STATE\_ON = 2 | Always displayed. |

#### \[h2\]ArkUI\_EffectEdge

enum ArkUI\_EffectEdge

**Description**

Enumerates the edges for which the effect takes effect when the boundary of the scrollable content is reached.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_EFFECT\_EDGE\_START = 1 | Start edge. |
| ARKUI\_EFFECT\_EDGE\_END = 2 | End edge. |

#### \[h2\]ArkUI\_ScrollDirection

enum ArkUI\_ScrollDirection

**Description**

Enumerates the scrolling directions of the [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md) component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_DIRECTION\_VERTICAL = 0 | Vertical scrolling only. |
| ARKUI\_SCROLL\_DIRECTION\_HORIZONTAL = 1 | Horizontal scrolling only. |
| ARKUI\_SCROLL\_DIRECTION\_NONE = 3 | Scrolling disabled. |
| ARKUI\_SCROLL\_DIRECTION\_FREE = 4 | 
Free scrolling in both directions.

**Since**: 20

 |

#### \[h2\]ArkUI\_ScrollSnapAlign

enum ArkUI\_ScrollSnapAlign

**Description**

Enumerates the alignment modes of list items when scrolling ends.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE = 0 | No alignment mode. |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_START = 1 | The first item in the view is aligned at the start of the list. |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_CENTER = 2 | The middle items in the view are aligned in the center of the list. |
| ARKUI\_SCROLL\_SNAP\_ALIGN\_END = 3 | The last item in the view is aligned at the end of the list. |

#### \[h2\]ArkUI\_ScrollBarDisplayMode

enum ArkUI\_ScrollBarDisplayMode

**Description**

Enumerates the scrollbar display modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF = 0 | Not displayed. |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO = 1 | Displayed when the screen is touched and hidden after 2s. |
| ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_ON = 2 | Always displayed. |

#### \[h2\]ArkUI\_Axis

enum ArkUI\_Axis

**Description**

Enumerates scroll directions and [List](../../../arkts-components/scroll-and-swipe/list/document.md) component arrangement directions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_AXIS\_VERTICAL = 0 | Vertical scrolling only. This is the default value. |
| ARKUI\_AXIS\_HORIZONTAL = 1 | Horizontal scrolling only. |

#### \[h2\]ArkUI\_StickyStyle

enum ArkUI\_StickyStyle

**Description**

Enumerates the modes for pinning the header to the top or the footer to the bottom.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_STICKY\_STYLE\_NONE = 0 | [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) and [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) of [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) are not pinned to the top and bottom, respectively. |
| ARKUI\_STICKY\_STYLE\_HEADER = 1 | [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) of [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) is pinned to the top, and [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) is not pinned to the bottom. |
| ARKUI\_STICKY\_STYLE\_FOOTER = 2 | [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) of [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) is not pinned to the top, and [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) is pinned to the bottom. |
| ARKUI\_STICKY\_STYLE\_BOTH = 3 | [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) of [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) is pinned to the top, and [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions) is pinned to the bottom. |

#### \[h2\]ArkUI\_ContentClipMode

enum ArkUI\_ContentClipMode

**Description**

Enumerates the content clipping modes of scrollable components.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY = 0 | Clip to the content area only. |
| ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY = 1 | Clip to the component's boundary area. |
| ARKUI\_CONTENT\_CLIP\_MODE\_SAFE\_AREA = 2 | Clip to the safe area configured for the component. |

#### \[h2\]ArkUI\_WaterFlowLayoutMode

enum ArkUI\_WaterFlowLayoutMode

**Description**

Enumerates the layout modes of the [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md) component.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_ALWAYS\_TOP\_DOWN = 0 | Layout from top to bottom. In scenarios where column switching occurs, the layout starts from the first [water flow item](../../../arkts-components/scroll-and-swipe/flowitem/document.md) to the currently displayed [water flow item](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |
| ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_SLIDING\_WINDOW = 1 | Sliding window layout. In scenarios where column switching occurs, only the range of [water flow items](../../../arkts-components/scroll-and-swipe/flowitem/document.md) currently on display is re-laid out. As the user scrolls down with their finger, [water flow items](../../../arkts-components/scroll-and-swipe/flowitem/document.md) that enter the display range from above are subsequently laid out. |

#### \[h2\]ArkUI\_BorderStyle

enum ArkUI\_BorderStyle

**Description**

Enumerates the border styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_BORDER\_STYLE\_SOLID = 0 | Solid border. This is the default value. |
| ARKUI\_BORDER\_STYLE\_DASHED = 1 | Dashed border. |
| ARKUI\_BORDER\_STYLE\_DOTTED = 2 | Dotted border. |

#### \[h2\]ArkUI\_HitTestMode

enum ArkUI\_HitTestMode

**Description**

Enumerates the hit test modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_HIT\_TEST\_MODE\_DEFAULT = 0 | Both the node and its child node respond to the hit test of a touch event, but its sibling node is blocked from the hit test. The node itself and its child nodes respond to the hit test, but block the hit test of sibling nodes. It does not affect the hit test of ancestor nodes. |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK = 1 | The node itself responds to the hit test and blocks the hit test of child nodes, sibling nodes, and ancestor nodes. |
| ARKUI\_HIT\_TEST\_MODE\_TRANSPARENT = 2 | Both the node itself and its child nodes respond to the hit test and do not block the hit test of sibling nodes and ancestor nodes. |
| ARKUI\_HIT\_TEST\_MODE\_NONE = 3 | The node itself does not respond to the hit test and does not block the hit test of child nodes, sibling nodes, and ancestor nodes. |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK\_HIERARCHY = 4 | 
The node itself and its child nodes respond to the hit test, preventing all sibling nodes and parent nodes with lower priority from participating in the hit test.

**Since**: 20

 |
| ARKUI\_HIT\_TEST\_MODE\_BLOCK\_DESCENDANTS = 5 | 

The node itself does not respond to the hit test, and all its descendants (children, grandchildren, and more) also do not respond to the hit test. It does not affect the hit test of ancestor nodes.

**Since**: 20

 |

#### \[h2\]ArkUI\_ShadowStyle

enum ArkUI\_ShadowStyle

**Description**

Enumerates shadow styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_XS = 0 | 
Mini shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/pYqazYT8RSOs1mJbO2k2nA/en-us_image_0000002537926306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F38FFF84EC13669FB1DB1B95BFA39440415559FB31165C6306974ED23B39236D)

 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_SM = 1 | 

Small shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/b9AUGRqBRLmlObIPSN3lrg/en-us_image_0000002568686083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ED4570D97D714068C4F2101A18FA7479521D5D2A286E4E525854F15B3656FEF)

 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_MD = 2 | 

Medium shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/PwifoqZ6RK-YZTG5fpi_HA/en-us_image_0000002568766093.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C7875595D61C90E70B8AFF9800687E73A2CF61FD448785A210093AD3B2B7EA8)

 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_LG = 3 | 

Large shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Y9VH4OhUTwiWTZIVdGIJlQ/en-us_image_0000002537766368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D5C1EDE84C9204047E68EA6A074354FBA44F80CDC0EFD76B165E056624761E3)

 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_SM = 4 | 

Floating small shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/QmF39QBETNCK6moMzupAEA/en-us_image_0000002537926308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEEE7C8F33C3D6EAA7B265A5F2E5E5836BAD273C4129DF1B4930B3D3781DDFB3)

 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_MD = 5 | 

Floating medium shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/sdUKoKEmQ7KRfnYKOO66AQ/en-us_image_0000002568686085.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEF114394DD5E41DCD58B06F5A902E208DC40392E3126939BEFD8175E12510E3)

 |

#### \[h2\]ArkUI\_AnimationCurve

enum ArkUI\_AnimationCurve

**Description**

Enumerates the animation curves.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_CURVE\_LINEAR = 0 | The animation speed keeps unchanged. |
| ARKUI\_CURVE\_EASE = 1 | The animation starts slowly, accelerates, and then slows down towards the end. |
| ARKUI\_CURVE\_EASE\_IN = 2 | The animation starts at a low speed and then picks up speed until the end. |
| ARKUI\_CURVE\_EASE\_OUT = 3 | The animation ends at a low speed. |
| ARKUI\_CURVE\_EASE\_IN\_OUT = 4 | The animation starts and ends at a low speed, providing a smooth and natural transition. |
| ARKUI\_CURVE\_FAST\_OUT\_SLOW\_IN = 5 | The animation uses the standard curve |
| ARKUI\_CURVE\_LINEAR\_OUT\_SLOW\_IN = 6 | The animation uses the deceleration curve. |
| ARKUI\_CURVE\_FAST\_OUT\_LINEAR\_IN = 7 | The animation uses the acceleration curve. |
| ARKUI\_CURVE\_EXTREME\_DECELERATION = 8 | The animation uses the extreme deceleration curve. |
| ARKUI\_CURVE\_SHARP = 9 | The animation uses the sharp curve. |
| ARKUI\_CURVE\_RHYTHM = 10 | The animation uses the rhythm curve. |
| ARKUI\_CURVE\_SMOOTH = 11 | The animation uses the smooth curve. |
| ARKUI\_CURVE\_FRICTION = 12 | The animation uses the friction curve |

#### \[h2\]ArkUI\_SwiperArrow

enum ArkUI\_SwiperArrow

**Description**

Enumerates arrow styles of the navigation indicator.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SWIPER\_ARROW\_HIDE = 0 | The arrow is not displayed for the navigation indicator. |
| ARKUI\_SWIPER\_ARROW\_SHOW = 1 | The arrow is displayed for the navigation indicator. |
| ARKUI\_SWIPER\_ARROW\_SHOW\_ON\_HOVER = 2 | The arrow is displayed when the mouse pointer hovers over the navigation indicator. |

#### \[h2\]ArkUI\_SwiperNestedScrollMode

enum ArkUI\_SwiperNestedScrollMode

**Description**

Enumerates the nested scrolling modes of the **Swiper** component and its parent container.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY = 0 | The scrolling is contained within the **Swiper** component, and no scroll chaining occurs, that is, the parent container does not scroll when the component scrolling reaches the boundary. |
| ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_FIRST = 1 | The **Swiper** component scrolls first, and when it hits the boundary, the parent container scrolls. When the parent container hits the boundary, its edge effect is displayed. If no edge effect is specified for the parent container, the edge effect of the child component is displayed instead. |

#### \[h2\]ArkUI\_PageFlipMode

enum ArkUI\_PageFlipMode

**Description**

Enumerates the modes for flipping pages using the mouse wheel in the [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md) component.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_PAGE\_FLIP\_MODE\_CONTINUOUS = 0 | Continuous page flipping mode where multiple pages are turned continuously when the user scrolls the mouse wheel without interruption. |
| ARKUI\_PAGE\_FLIP\_MODE\_SINGLE = 1 | The system does not respond to other mouse wheel events until the page flipping animation ends. |

#### \[h2\]ArkUI\_SwiperAnimationMode

enum ArkUI\_SwiperAnimationMode

**Description**

Enumerates the animation modes for redirecting to a target page in the **Swiper** component.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_SWIPER\_NO\_ANIMATION = 0 | No animation is displayed for redirecting to a target page. |
| ARKUI\_SWIPER\_DEFAULT\_ANIMATION = 1 | An animation is displayed for redirecting to a target page. |
| ARKUI\_SWIPER\_FAST\_ANIMATION = 2 | First redirects to a position near the target page without animation, then animates to a target page. |

#### \[h2\]ArkUI\_AccessibilityMode

enum ArkUI\_AccessibilityMode

**Description**

Enumerates the accessibility modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_MODE\_AUTO = 0 | The mode is automatically set to enabled or disabled based on the component. |
| ARKUI\_ACCESSIBILITY\_MODE\_ENABLED = 1 | The component can be identified by the accessibility service. |
| ARKUI\_ACCESSIBILITY\_MODE\_DISABLED = 2 | The component cannot be identified by the accessibility service. |
| ARKUI\_ACCESSIBILITY\_MODE\_DISABLED\_FOR\_DESCENDANTS = 3 | The component and all its child components cannot be identified by the accessibility service. |

#### \[h2\]ArkUI\_TextCopyOptions

enum ArkUI\_TextCopyOptions

**Description**

Enumerates copy options, which define whether copy and paste is allowed for text content.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_COPY\_OPTIONS\_NONE = 0 | Copy is not allowed. |
| ARKUI\_TEXT\_COPY\_OPTIONS\_IN\_APP = 1 | Intra-application copy is allowed. |
| ARKUI\_TEXT\_COPY\_OPTIONS\_LOCAL\_DEVICE = 2 | Intra-device copy is allowed. |
| ARKUI\_TEXT\_COPY\_OPTIONS\_CROSS\_DEVICE = 3 | Cross-device copy is allowed. |

#### \[h2\]ArkUI\_TextHeightAdaptivePolicy

enum ArkUI\_TextHeightAdaptivePolicy

**Description**

Defines how the adaptive height is determined for the text.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST = 0 | Prioritize the **maxLines** settings. |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MIN\_FONT\_SIZE\_FIRST = 1 | Prioritize the **minFontSize** settings. |
| ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_LAYOUT\_CONSTRAINT\_FIRST = 2 | Prioritize the layout constraint settings in terms of height. |

#### \[h2\]ArkUI\_ScrollNestedMode

enum ArkUI\_ScrollNestedMode

**Description**

Enumerates nested scrolling modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_ONLY = 0 | The scrolling is contained within the component, and no scroll chaining occurs, that is, the parent component does not scroll when the component scrolling reaches the boundary. |
| ARKUI\_SCROLL\_NESTED\_MODE\_SELF\_FIRST = 1 | The component scrolls first, and when it hits the boundary, the parent component scrolls. When the parent component hits the boundary, its edge effect is displayed. If no edge effect is specified for the parent component, the edge effect of the child component is displayed instead. |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARENT\_FIRST = 2 | The parent component scrolls first, and when it hits the boundary, the component scrolls. When the component hits the boundary, its edge effect is displayed. If no edge effect is specified for the component, the edge effect of the parent component is displayed instead. |
| ARKUI\_SCROLL\_NESTED\_MODE\_PARALLEL = 3 | The component and its parent component scroll at the same time. When both the component and its parent component hit the boundary, the edge effect of the component is displayed. If no edge effect is specified for the component, the edge effect of the parent component is displayed instead. |

#### \[h2\]ArkUI\_ScrollEdge

enum ArkUI\_ScrollEdge

**Description**

Enumerates the edges to which the component scrolls.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_EDGE\_TOP = 0 | Top edge in the vertical direction. |
| ARKUI\_SCROLL\_EDGE\_BOTTOM = 1 | Bottom edge in the vertical direction. |
| ARKUI\_SCROLL\_EDGE\_START = 2 | Start position in the horizontal direction. |
| ARKUI\_SCROLL\_EDGE\_END = 3 | End position in the horizontal direction. |

#### \[h2\]ArkUI\_ScrollAlignment

enum ArkUI\_ScrollAlignment

**Description**

Defines how the list item to scroll to is aligned with the container.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_ALIGNMENT\_START = 0 | The start edge of the list item is flush with the start edge of the container. |
| ARKUI\_SCROLL\_ALIGNMENT\_CENTER = 1 | The list item is centered along the main axis of the container. |
| ARKUI\_SCROLL\_ALIGNMENT\_END = 2 | The end edge of the list item is flush with the end edge of the container. |
| ARKUI\_SCROLL\_ALIGNMENT\_AUTO = 3 | The list item is automatically aligned. If the item is fully contained within the display area, no adjustment is performed. Otherwise, the item is aligned so that its start or end edge is flush with the start or end edge of the container, whichever requires a shorter scrolling distance. |

#### \[h2\]ArkUI\_ScrollState

enum ArkUI\_ScrollState

**Description**

Enumerates the scrolling states.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_STATE\_IDLE = 0 | Idle. The container enters this state when an API in the controller is used to scroll the container or when the scrollbar is dragged. |
| ARKUI\_SCROLL\_STATE\_SCROLL = 1 | Scrolling. The container enters this state when the user drags the container to scroll. |
| ARKUI\_SCROLL\_STATE\_FLING = 2 | Inertial scrolling. The container enters this state when inertial scrolling occurs or when the container bounces back after being released from a fling. |

#### \[h2\]ArkUI\_SliderBlockStyle

enum ArkUI\_SliderBlockStyle

**Description**

Enumerates the styles of the slider in the block direction.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_DEFAULT = 0 | Round slider. |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE = 1 | Slider with an image background. |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE = 2 | Slider in a custom shape. |

#### \[h2\]ArkUI\_SliderDirection

enum ArkUI\_SliderDirection

**Description**

Enumerates the scroll directions of the slider.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SLIDER\_DIRECTION\_VERTICAL = 0 | Vertical direction. |
| ARKUI\_SLIDER\_DIRECTION\_HORIZONTAL = 1 | Horizontal direction. |

#### \[h2\]ArkUI\_SliderStyle

enum ArkUI\_SliderStyle

**Description**

Enumerates the slider styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SLIDER\_STYLE\_OUT\_SET = 0 | The slider is on the slider rail. |
| ARKUI\_SLIDER\_STYLE\_IN\_SET = 1 | The slider is in the slider rail. |
| ARKUI\_SLIDER\_STYLE\_NONE = 2 | There is no thumb. |

#### \[h2\]ArkUI\_CheckboxShape

enum ArkUI\_CheckboxShape

**Description**

Enumerates the shapes of the check box.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ArkUI\_CHECKBOX\_SHAPE\_CIRCLE = 0 | Circle. |
| ArkUI\_CHECKBOX\_SHAPE\_ROUNDED\_SQUARE = 1 | Rounded square. |

#### \[h2\]ArkUI\_AnimationPlayMode

enum ArkUI\_AnimationPlayMode

**Description**

Enumerates the animation playback modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL = 0 | The animation is played forwards. |
| ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE = 1 | The animation is played backwards. |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE = 2 | The animation plays in alternating loop mode. When the animation is played for an odd number of times, the playback is in forward direction. When the animation is played for an even number of times, the playback is in reverse direction. |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE\_REVERSE = 3 | The animation plays in reverse alternating loop mode. When the animation is played for an odd number of times, the playback is in reverse direction. When the animation is played for an even number of times, the playback is in forward direction. |

#### \[h2\]ArkUI\_ImageSize

enum ArkUI\_ImageSize

**Description**

Defines the image size.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_IMAGE\_SIZE\_AUTO = 0 | The original image aspect ratio is retained. |
| ARKUI\_IMAGE\_SIZE\_COVER = 1 | The image is scaled with its aspect ratio retained for both sides to be greater than or equal to the display boundaries. |
| ARKUI\_IMAGE\_SIZE\_CONTAIN = 2 | The image is scaled with its aspect ratio retained for the content to be completely displayed within the display boundaries. |

#### \[h2\]ArkUI\_AdaptiveColor

enum ArkUI\_AdaptiveColor

**Description**

Enumerates the adaptive color modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ADAPTIVE\_COLOR\_DEFAULT = 0 | Adaptive color mode is not used. |
| ARKUI\_ADAPTIVE\_COLOR\_AVERAGE = 1 | Adaptive color mode is used. |

#### \[h2\]ArkUI\_ColorMode

enum ArkUI\_ColorMode

**Description**

Enumerates the color modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_COLOR\_MODE\_SYSTEM = 0 | Following the system color mode. |
| ARKUI\_COLOR\_MODE\_LIGHT = 1 | Light color mode. |
| ARKUI\_COLOR\_MODE\_DARK = 2 | Dark color mode. |

#### \[h2\]ArkUI\_SystemColorMode

enum ArkUI\_SystemColorMode

**Description**

Enumerates the system color modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SYSTEM\_COLOR\_MODE\_LIGHT = 0 | Light mode. |
| ARKUI\_SYSTEM\_COLOR\_MODE\_DARK = 1 | Dark mode. |

#### \[h2\]ArkUI\_BlurStyle

enum ArkUI\_BlurStyle

**Description**

Enumerates the blur styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_BLUR\_STYLE\_THIN = 0 | 
Thin material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/kHg3_PvoSAuu37QCiAGFDg/en-us_image_0000002568766095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D1465CD83C08319B4CB9D18FB5785C88ED6E1DA357707FDA8D317773310E6C4)

 |
| ARKUI\_BLUR\_STYLE\_REGULAR = 1 | 

Regular material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/_bZr_tnSSeitcgJSnz_dGQ/en-us_image_0000002537766370.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6932466056AB83D12F5B5387A8F6968BBE0EA87B9EAC4205F832022AEC287942)

 |
| ARKUI\_BLUR\_STYLE\_THICK = 2 | 

Thick material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/IfjOb-wcSviEYpxJQBjDBw/en-us_image_0000002537926310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6098A845BADF7E231482F6FDFA9157D5E25F653912CB5424248C6143BD492DF7)

 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THIN = 3 | 

Material that creates the minimum depth of field effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/tcT06dylQ3ePz-3mpPzy4Q/en-us_image_0000002568686087.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23FB99F9703DEFA1E25F3BBB47D2DC9F88056038A704D34D8E37104569A29A1D)

 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_REGULAR = 4 | 

Material that creates a medium shallow depth of field effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qalcKu2KQD21Lk1CFgdo-w/en-us_image_0000002568766097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDCB197A8700780BFD3AEF0BD577138FD824ED14588C4115E74673A8B0F7F132)

 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THICK = 5 | 

Material that creates a high shallow depth of field effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/_TLff9jET2OMGpn_pOS8ig/en-us_image_0000002537766372.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F26A889885746ED9F0090A4D74D2A22F856197C2BDF6991232179C8FE0B5309)

 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_ULTRA\_THICK = 6 | 

Material that creates the maximum depth of field effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/u8rctQsXSQuEShOwJlPx7Q/en-us_image_0000002537926312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A145AFFA2FA4F705C57FF2A1EDC8CC07C11811F914784E20D32C83D8385EAAC2)

 |
| ARKUI\_BLUR\_STYLE\_NONE = 7 | 

No blur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/OE7TWm8cRrOJw9kw9jschA/en-us_image_0000002568686089.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABECC84FD87831C049B90003533F7051155A5A40E5A1F6178B55C5C8C2ED3316)

 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THIN = 8 | 

Component ultra-thin material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/NyxyjFXvSTaxTwL6Fln9DA/en-us_image_0000002568766099.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9882DC7A6EE8B6A95E49384921FB8F6A752D285E56F5AE8DD65C1815B30F657F)

 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THIN = 9 | 

Component thin material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/0jBAuZStTyGDbNS0orZ2-w/en-us_image_0000002537766374.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC095577CDD2E8CA9B7EFED416052AD707E8EE0A320C43BC931DD833B36D4231)

 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_REGULAR = 10 | 

Component regular material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/4bDkmig-SHecfFoQ5hPnFg/en-us_image_0000002537926314.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=050A54FFB58EEF37AEA10D0112DAB01D68711E7999C4A4096397256EC14157CA)

 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THICK = 11 | 

Component thick material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/YW3ve9WBRUagUSylLBUHAQ/en-us_image_0000002568686091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4121900503BF8D8D513710AFDD9B02AC1138C4DFB3A98838BC927DEAC54F6F8)

 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THICK = 12 | 

Component ultra-thick material.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/OqsiZMLzSIKTlq9KM59I4Q/en-us_image_0000002568766101.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=833730B27F921B654A343B3497A9EEA35988AB06598DB8968B2F15AC16DEBFD9)

 |

#### \[h2\]ArkUI\_BlurStyleActivePolicy

enum ArkUI\_BlurStyleActivePolicy

**Description**

Enumerates the activation policies for the background blur effect.

**Since**: 19

| Value | Description |
| :-- | :-- |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | The blur effect changes according to the window's focus state; it is inactive when the window is not in focus and active when the window is in focus. |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_ACTIVE = 1 | The blur effect is always active. |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_INACTIVE = 2 | The blur effect is always inactive. |

#### \[h2\]ArkUI\_VerticalAlignment

enum ArkUI\_VerticalAlignment

**Description**

Enumerates the vertical alignment modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_VERTICAL\_ALIGNMENT\_TOP = 0 | Top aligned. |
| ARKUI\_VERTICAL\_ALIGNMENT\_CENTER = 1 | Aligned with the center. This is the default alignment mode. |
| ARKUI\_VERTICAL\_ALIGNMENT\_BOTTOM = 2 | Bottom aligned. |

#### \[h2\]ArkUI\_HorizontalAlignment

enum ArkUI\_HorizontalAlignment

**Description**

Enumerates the alignment mode in the horizontal direction.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_START = 0 | Aligned with the start edge in the same direction as the language in use. |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER = 1 | Aligned with the center. This is the default alignment mode. |
| ARKUI\_HORIZONTAL\_ALIGNMENT\_END = 2 | Aligned with the end edge in the same direction as the language in use. |

#### \[h2\]ArkUI\_TextOverflow

enum ArkUI\_TextOverflow

**Description**

Enumerates the display modes when the text is too long.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_OVERFLOW\_NONE = 0 | Extra-long text is not clipped. |
| ARKUI\_TEXT\_OVERFLOW\_CLIP = 1 | Extra-long text is clipped. |
| ARKUI\_TEXT\_OVERFLOW\_ELLIPSIS = 2 | An ellipsis (...) is used to represent text overflow. |
| ARKUI\_TEXT\_OVERFLOW\_MARQUEE = 3 | Text continuously scrolls when text overflow occurs. |

#### \[h2\]ArkUI\_ImageSpanAlignment

enum ArkUI\_ImageSpanAlignment

**Description**

Enumerates the alignment mode of the image with the text.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BASELINE = 0 | The image is bottom aligned with the text baseline. |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BOTTOM | The image is bottom aligned with the text. |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_CENTER | The image is centered aligned with the text. |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_TOP | The image is top aligned with the text. |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_FOLLOW\_PARAGRAPH | 
The image alignment mode follows the text component's alignment mode.

**Since**: 20

 |

#### \[h2\]ArkUI\_ObjectFit

enum ArkUI\_ObjectFit

**Description**

Enumerates the image filling effects of the [Image](../../../arkts-components/images-and-videos/image/document.md) component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_OBJECT\_FIT\_CONTAIN = 0 | The image is scaled with its aspect ratio retained for the content to be completely displayed within the display boundaries. |
| ARKUI\_OBJECT\_FIT\_COVER = 1 | The image is scaled with its aspect ratio retained for both sides to be greater than or equal to the display boundaries. |
| ARKUI\_OBJECT\_FIT\_AUTO = 2 | The image is scaled automatically to fit the display area. |
| ARKUI\_OBJECT\_FIT\_FILL = 3 | The image is scaled to fill the display area, and its aspect ratio is not retained. |
| ARKUI\_OBJECT\_FIT\_SCALE\_DOWN = 4 | The image is displayed with its aspect ratio retained, in a size smaller than or equal to the original size. |
| ARKUI\_OBJECT\_FIT\_NONE = 5 | The original size is retained. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_START = 6 | Not resized, the image is aligned with the start edge of the top of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP = 7 | Not resized, the image is horizontally centered at the top of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_TOP\_END = 8 | Not resized, the image is aligned with the end edge at the top of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_START = 9 | Not resized, the image is vertically centered on the start edge of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_CENTER = 10 | Not resized, the image is horizontally and vertically centered in the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_END = 11 | Not resized, the image is vertically centered on the end edge of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_START = 12 | Not resized, the image is aligned with the start edge at the bottom of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM = 13 | Not resized, the image is horizontally centered at the bottom of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_AND\_ALIGN\_BOTTOM\_END = 14 | Not resized, the image is aligned with the end edge at the bottom of the container. |
| ARKUI\_OBJECT\_FIT\_NONE\_MATRIX = 15 | 
The image maintains its original size. Must be used with [NODE\_IMAGE\_IMAGE\_MATRIX](../native-node-h/document.md#arkui_nodeattributetype).

**Since**: 21

 |

#### \[h2\]ArkUI\_ImageInterpolation

enum ArkUI\_ImageInterpolation

**Description**

Enumerates the image interpolation effects. This attribute mitigates aliasing during image scaling. This attribute is not applicable to SVG images.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_IMAGE\_INTERPOLATION\_NONE = 0 | No image interpolation. |
| ARKUI\_IMAGE\_INTERPOLATION\_LOW = 1 | Low quality interpolation. |
| ARKUI\_IMAGE\_INTERPOLATION\_MEDIUM = 2 | Medium quality interpolation. |
| ARKUI\_IMAGE\_INTERPOLATION\_HIGH = 3 | High quality interpolation. This mode produces scaled images of the highest possible quality. |

#### \[h2\]ArkUI\_DynamicRangeMode

enum ArkUI\_DynamicRangeMode

**Description**

Enumerates the dynamic range modes (for example, SDR/HDR) for images, controlling the display range of image brightness and color gamut.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_HIGH = 0 | High dynamic range (HDR), representing the range between minimum and maximum brightness values in an image. A wider range makes image brightness closer to real-world conditions, preventing overexposure (all white) in bright environments and loss of detail (all black) in dark environments. |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_CONSTRAINT | Constrained high dynamic range, offering richer brightness and color than SDR while maintaining SDR compatibility. Typically used in scenarios requiring SDR backward compatibility. |
| ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD | Standard dynamic range (SDR), featuring a limited brightness range (typically 0-100 nits) with reduced contrast between bright and dark areas. Dark areas may lose detail to black, while bright areas may become overexposed to white. |

#### \[h2\]ArkUI\_ImageRotateOrientation

enum ArkUI\_ImageRotateOrientation

**Description**

Enumerates image rotation directions.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_ORIENTATION\_AUTO = 0 | Use EXIF metadata for display orientation, with support for rotation and mirroring. EXIF is a file format dedicated for photos taken by digital cameras and is used to record attributes and shooting data of the photos. |
| ARKUI\_ORIENTATION\_UP | Display original pixel data without transformation. |
| ARKUI\_ORIENTATION\_RIGHT | Display the image after rotating it 90 degrees clockwise. |
| ARKUI\_ORIENTATION\_DOWN | Display the image after rotating it 180 degrees clockwise. |
| ARKUI\_ORIENTATION\_LEFT | Display the image after rotating it 270 degrees clockwise. |
| ARKUI\_ORIENTATION\_UP\_MIRRORED | Display the image after flipping it horizontally. |
| ARKUI\_ORIENTATION\_RIGHT\_MIRRORED | Display the image after flipping it horizontally and then rotating it 90 degrees clockwise. |
| ARKUI\_ORIENTATION\_DOWN\_MIRRORED | Display the image after flipping it vertically. |
| ARKUI\_ORIENTATION\_LEFT\_MIRRORED | Display the image after flipping it horizontally and then rotating it 270 degrees clockwise. |

#### \[h2\]ArkUI\_BlendMode

enum ArkUI\_BlendMode

**Description**

Enumerates the blend modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_BLEND\_MODE\_NONE = 0 | The top image is superimposed on the bottom image without any blending. |
| ARKUI\_BLEND\_MODE\_CLEAR = 1 | The target pixels covered by the source pixels are erased by being turned to completely transparent. |
| ARKUI\_BLEND\_MODE\_SRC = 2 | r = s: Only the source pixels are displayed. |
| ARKUI\_BLEND\_MODE\_DST = 3 | r = d: Only the target pixels are displayed. |
| ARKUI\_BLEND\_MODE\_SRC\_OVER = 4 | r = s + (1 - sa) \* d: The source pixels are blended based on opacity and cover the target pixels. |
| ARKUI\_BLEND\_MODE\_DST\_OVER = 5 | r = d + (1 - da) \* s: The target pixels are blended based on opacity and cover on the source pixels. |
| ARKUI\_BLEND\_MODE\_SRC\_IN = 6 | r = s \* da: Only the part of the source pixels that overlap with the target pixels is displayed. |
| ARKUI\_BLEND\_MODE\_DST\_IN = 7 | r = d \* sa: Only the part of the target pixels that overlap with the source pixels is displayed. |
| ARKUI\_BLEND\_MODE\_SRC\_OUT = 8 | r = s \* (1 - da): Only the part of the source pixels that do not overlap with the target pixels is displayed. |
| ARKUI\_BLEND\_MODE\_DST\_OUT = 9 | r = d \* (1 - sa): Only the part of the target pixels that do not overlap with the source pixels is displayed. |
| ARKUI\_BLEND\_MODE\_SRC\_ATOP = 10 | r = s \* da + d \* (1 - sa): The part of the source pixels that overlap with the target pixels is displayed and the part of the target pixels that do not overlap with the source pixels are displayed. |
| ARKUI\_BLEND\_MODE\_DST\_ATOP = 11 | r = d \* sa + s \* (1 - da): The part of the target pixels that overlap with the source pixels and the part of the source pixels that do not overlap with the target pixels are displayed. |
| ARKUI\_BLEND\_MODE\_XOR = 12 | r = s \* (1 - da) + d \* (1 - sa): Only the non-overlapping part between the source pixels and the target pixels is displayed. |
| ARKUI\_BLEND\_MODE\_PLUS = 13 | r = min(s + d, 1): New pixels resulting from adding the source pixels to the target pixels are displayed. |
| ARKUI\_BLEND\_MODE\_MODULATE = 14 | r = s \* d: New pixels resulting from multiplying the source pixels with the target pixels are displayed. |
| ARKUI\_BLEND\_MODE\_SCREEN = 15 | r = s + d - s \* d: Pixels are blended by adding the source pixels to the target pixels and subtracting the product of their multiplication. |
| ARKUI\_BLEND\_MODE\_OVERLAY = 16 | The MULTIPLY or SCREEN mode is used based on the target pixels. |
| ARKUI\_BLEND\_MODE\_DARKEN = 17 | rc = s + d - max(s \* da, d \* sa), ra = kSrcOver: When two colors overlap, whichever is darker is used. |
| ARKUI\_BLEND\_MODE\_LIGHTEN = 18 | rc = s + d - min(s \* da, d \* sa), ra = kSrcOver: The darker of the pixels (source and target) is used. |
| ARKUI\_BLEND\_MODE\_COLOR\_DODGE = 19 | The colors of the target pixels are lightened to reflect the source pixels. |
| ARKUI\_BLEND\_MODE\_COLOR\_BURN = 20 | The colors of the target pixels are darkened to reflect the source pixels. |
| ARKUI\_BLEND\_MODE\_HARD\_LIGHT = 21 | The MULTIPLY or SCREEN mode is used, depending on the source pixels. |
| ARKUI\_BLEND\_MODE\_SOFT\_LIGHT = 22 | The LIGHTEN or DARKEN mode is used, depending on the source pixels. |
| ARKUI\_BLEND\_MODE\_DIFFERENCE = 23 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = kSrcOver: The final pixel is the result of subtracting the darker of the two pixels (source and target) from the lighter one. |
| ARKUI\_BLEND\_MODE\_EXCLUSION = 24 | rc = s + d - two(s \* d), ra = kSrcOver: The final pixel is similar to **DIFFERENCE**, but with less contrast. |
| ARKUI\_BLEND\_MODE\_MULTIPLY = 25 | r = s \* (1 - da) + d \* (1 - sa) + s \* d: The final pixel is the result of multiplying the source pixel by the target pixel. |
| ARKUI\_BLEND\_MODE\_HUE = 26 | The resultant image is created with the luminance and saturation of the source image and the hue of the target image. |
| ARKUI\_BLEND\_MODE\_SATURATION = 27 | The resultant image is created with the luminance and hue of the target image and the saturation of the source image. |
| ARKUI\_BLEND\_MODE\_COLOR = 28 | The resultant image is created with the saturation and hue of the source image and the luminance of the target image. |
| ARKUI\_BLEND\_MODE\_LUMINOSITY = 29 | The resultant image is created with the saturation and hue of the target image and the luminance of the source image. |

#### \[h2\]ArkUI\_Direction

enum ArkUI\_Direction

**Description**

Enumerates the modes in which components are laid out along the main axis of the container.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_DIRECTION\_LTR = 0 | Components are arranged from left to right. This is the default value. |
| ARKUI\_DIRECTION\_RTL = 1 | Components are arranged from right to left. |
| ARKUI\_DIRECTION\_AUTO = 3 | The system layout direction is used. |

#### \[h2\]ArkUI\_ItemAlignment

enum ArkUI\_ItemAlignment

**Description**

Enumerates the modes in which components are laid out along the cross axis of the container.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ITEM\_ALIGNMENT\_AUTO = 0 | The default configuration in the [Flex](../../../arkts-components/rows-columns-and-stacking/flex/document.md) container is used. This is the default value. |
| ARKUI\_ITEM\_ALIGNMENT\_START = 1 | The items in the flex container are aligned with the cross-start edge. |
| ARKUI\_ITEM\_ALIGNMENT\_CENTER = 2 | The items in the flex container are centered along the cross axis. |
| ARKUI\_ITEM\_ALIGNMENT\_END = 3 | The items in the flex container are aligned with the cross-end edge. |
| ARKUI\_ITEM\_ALIGNMENT\_STRETCH = 4 | The items in the flex container are stretched and padded along the cross axis. |
| ARKUI\_ITEM\_ALIGNMENT\_BASELINE = 5 | The items in the flex container are aligned in such a manner that their text baselines are aligned along the cross axis. |

#### \[h2\]ArkUI\_ColorStrategy

enum ArkUI\_ColorStrategy

**Description**

Enumerates foreground and shadow colors.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_COLOR\_STRATEGY\_INVERT = 0 | The foreground colors are the inverse of the component background colors. |
| ARKUI\_COLOR\_STRATEGY\_AVERAGE = 1 | The shadow colors of the component are the average color obtained from the component background shadow area. |
| ARKUI\_COLOR\_STRATEGY\_PRIMARY = 2 | The shadow colors of the component are the primary color obtained from the component background shadow area. |

#### \[h2\]ArkUI\_FlexAlignment

enum ArkUI\_FlexAlignment

**Description**

Enumerates the vertical alignment modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FLEX\_ALIGNMENT\_START = 1 | The child components are aligned with the start edge of the main axis. This is the default value. |
| ARKUI\_FLEX\_ALIGNMENT\_CENTER = 2 | The child components are aligned in the center of the main axis. |
| ARKUI\_FLEX\_ALIGNMENT\_END = 3 | The child components are aligned with the end edge of the main axis. |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_BETWEEN = 6 | The child components are evenly distributed along the main axis in [Flex](../../../arkts-components/rows-columns-and-stacking/flex/document.md). The space between any two adjacent components is the same. The first component is aligned with the main-start, and the last component is aligned with the main-end. |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_AROUND = 7 | The child components are evenly distributed along the main axis. The space between any two adjacent components is the same. The space between the first component and main-start, and that between the last component and cross-main are both half the size of the space between two adjacent components. |
| ARKUI\_FLEX\_ALIGNMENT\_SPACE\_EVENLY = 8 | The child components are evenly distributed along the main axis. The space between the first component and main-start, the space between the last component and main-end, and the space between any two adjacent components are the same. |

#### \[h2\]ArkUI\_FlexDirection

enum ArkUI\_FlexDirection

**Description**

Enumerates the directions of the main axis in the [Flex](../../../arkts-components/rows-columns-and-stacking/flex/document.md) container.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FLEX\_DIRECTION\_ROW = 0 | The child components are arranged in the same direction as the main axis runs down the rows. This is the default value. |
| ARKUI\_FLEX\_DIRECTION\_COLUMN = 1 | The child components are arranged in the same direction as the main axis runs down the columns. |
| ARKUI\_FLEX\_DIRECTION\_ROW\_REVERSE = 2 | The child components are arranged opposite to the **ROW** direction. |
| ARKUI\_FLEX\_DIRECTION\_COLUMN\_REVERSE = 3 | The child components are arranged opposite to the **COLUMN** direction. |

#### \[h2\]ArkUI\_FlexWrap

enum ArkUI\_FlexWrap

**Description**

Defines whether the flex container has a single line or multiple lines.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FLEX\_WRAP\_NO\_WRAP = 0 | The child components in the flex container are arranged in a single line, and they cannot overflow. This is the default value. |
| ARKUI\_FLEX\_WRAP\_WRAP = 1 | The child components in the flex container are arranged in multiple lines, and they may overflow. |
| ARKUI\_FLEX\_WRAP\_WRAP\_REVERSE = 2 | The child components in the flex container are reversely arranged in multiple lines, and they may overflow. |

#### \[h2\]ArkUI\_Visibility

enum ArkUI\_Visibility

**Description**

Enumerates the visibility values.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_VISIBILITY\_VISIBLE = 0 | The component is visible. |
| ARKUI\_VISIBILITY\_HIDDEN = 1 | The component is hidden, and a placeholder is used for it in the layout. |
| ARKUI\_VISIBILITY\_NONE = 2 | The component is hidden. It is not involved in the layout, and no placeholder is used for it. |

#### \[h2\]ArkUI\_CalendarAlignment

enum ArkUI\_CalendarAlignment

**Description**

Enumerates the alignment modes between the calendar picker and the entry component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_CALENDAR\_ALIGNMENT\_START = 0 | Left aligned. |
| ARKUI\_CALENDAR\_ALIGNMENT\_CENTER = 1 | Center aligned. |
| ARKUI\_CALENDAR\_ALIGNMENT\_END = 2 | Right aligned. |

#### \[h2\]ArkUI\_MaskType

enum ArkUI\_MaskType

**Description**

Enumerates the mask types. A mask is a means to limit the display area of a component. It uses a specific shape to crop the component content so that only the content in the mask area is visible.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_MASK\_TYPE\_RECTANGLE = 0 | Rectangle. |
| ARKUI\_MASK\_TYPE\_CIRCLE = 1 | Circle. |
| ARKUI\_MASK\_TYPE\_ELLIPSE = 2 | Ellipse. |
| ARKUI\_MASK\_TYPE\_PATH = 3 | Path. |
| ARKUI\_MASK\_TYPE\_PROGRESS = 4 | Progress indicator. |

#### \[h2\]ArkUI\_ClipType

enum ArkUI\_ClipType

**Description**

Enumerates the clipping region types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_CLIP\_TYPE\_RECTANGLE = 0 | Rectangle. |
| ARKUI\_CLIP\_TYPE\_CIRCLE = 1 | Circle. |
| ARKUI\_CLIP\_TYPE\_ELLIPSE = 2 | Ellipse. |
| ARKUI\_CLIP\_TYPE\_PATH = 3 | Path. |

#### \[h2\]ArkUI\_ShapeType

enum ArkUI\_ShapeType

**Description**

Enumerates custom shape types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SHAPE\_TYPE\_RECTANGLE = 0 | Rectangle. |
| ARKUI\_SHAPE\_TYPE\_CIRCLE = 1 | Circle. |
| ARKUI\_SHAPE\_TYPE\_ELLIPSE = 2 | Ellipse. |
| ARKUI\_SHAPE\_TYPE\_PATH = 3 | Path. |

#### \[h2\]ArkUI\_LinearGradientDirection

enum ArkUI\_LinearGradientDirection

**Description**

Enumerates the gradient directions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT = 0 | From right to left. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_TOP = 1 | From bottom to top. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT = 2 | From left to right. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_BOTTOM = 3 | From top to bottom. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_TOP = 4 | From lower right to upper left. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM = 5 | From upper right to lower left. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_TOP = 6 | From lower left to upper right. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_BOTTOM = 7 | From upper left to lower right. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_NONE = 8 | No gradient. |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM = 9 | Custom direction. |

#### \[h2\]ArkUI\_WordBreak

enum ArkUI\_WordBreak

**Description**

Enumerates the word break rules.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_WORD\_BREAK\_NORMAL = 0 | Word breaks can occur between any two characters for Chinese, Japanese, and Korean (CJK) text, but can occur only at a space character for non-CJK text (such as English). |
| ARKUI\_WORD\_BREAK\_BREAK\_ALL | Word breaks can occur between any two characters for non-CJK text. CJK text behavior is the same as for **NORMAL**. |
| ARKUI\_WORD\_BREAK\_BREAK\_WORD | This option has the same effect as **BREAK\_ALL** for non-CJK text, except that if it preferentially wraps lines at appropriate characters (for example, spaces) whenever possible. CJK text behavior is the same as for **NORMAL**. |
| ARKUI\_WORD\_BREAK\_HYPHENATION | 
Line breaks can occur between any two syllabic units for non-CJK text. CJK text behavior is the same as for **NORMAL**.

**Since**: 18

 |

#### \[h2\]ArkUI\_EllipsisMode

enum ArkUI\_EllipsisMode

**Description**

Enumerates the ellipsis positions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ELLIPSIS\_MODE\_START = 0 | An ellipsis is used at the start of the line of text. |
| ARKUI\_ELLIPSIS\_MODE\_CENTER | An ellipsis is used at the center of the line of text. |
| ARKUI\_ELLIPSIS\_MODE\_END | An ellipsis is used at the end of the line of text. |

#### \[h2\]ArkUI\_ImageRenderMode

enum ArkUI\_ImageRenderMode

**Description**

Enumerates the image rendering modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_IMAGE\_RENDER\_MODE\_ORIGINAL = 0 | Render image pixels as they are in the original source image. |
| ARKUI\_IMAGE\_RENDER\_MODE\_TEMPLATE = 1 | Render image pixels to create a monochrome template image. |

#### \[h2\]ArkUI\_TransitionEdge

enum ArkUI\_TransitionEdge

**Description**

Enumerates the slide-in and slide-out positions of the component from the screen edge during transition.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TRANSITION\_EDGE\_TOP = 0 | The component slides in and out from the top edge of the screen during transition. |
| ARKUI\_TRANSITION\_EDGE\_BOTTOM = 1 | The component slides in and out from the bottom edge of the screen during transition. |
| ARKUI\_TRANSITION\_EDGE\_START = 2 | The component slides in and out from the left edge of the screen during transition. |
| ARKUI\_TRANSITION\_EDGE\_END = 3 | The component slides in and out from the right edge of the screen during transition. |

#### \[h2\]ArkUI\_FinishCallbackType

enum ArkUI\_FinishCallbackType

**Description**

Enumerates the callback types for [OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](../native-animate-h/document.md#oh_arkui_animatoroption_registeronfinishcallback) in an animation.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_FINISH\_CALLBACK\_REMOVED = 0 | The callback is invoked when the entire animation is removed once it has finished. |
| ARKUI\_FINISH\_CALLBACK\_LOGICALLY = 1 | The callback is invoked when the animation logically enters the falling state, though it may still be in its long tail state. The long tail state refers to the residual change process before the animation is completely stopped. In this state, the value change of the animation is very small and close to the target value. |

#### \[h2\]ArkUI\_ListItemAlignment

enum ArkUI\_ListItemAlignment

**Description**

Enumerates the alignment modes of items along the cross axis. The default value is **ARKUI\_LIST\_ITEM\_ALIGNMENT\_START**.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_START = 0 | The [list items](../../../arkts-components/scroll-and-swipe/listitem/document.md#listitem10) are packed toward the start edge of the **List** component along the cross axis. |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_CENTER = 1 | The list items are centered in the **List** component along the cross axis. |
| ARKUI\_LIST\_ITEM\_ALIGNMENT\_END = 2 | The list items are packed toward the end edge of the **List** component along the cross axis. |

#### \[h2\]ArkUI\_BlendApplyType

enum ArkUI\_BlendApplyType

**Description**

Defines how the specified blend mode is applied.

**Since**: 12

| Value | Description |
| :-- | :-- |
| BLEND\_APPLY\_TYPE\_FAST = 0 | The content of the view is blended in sequence on the target image. |
| BLEND\_APPLY\_TYPE\_OFFSCREEN = 1 | The content of the component and its child components are drawn on the offscreen canvas, and then blended with the existing content on the canvas. |

#### \[h2\]ArkUI\_LengthMetricUnit

enum ArkUI\_LengthMetricUnit

**Description**

Enumerates the component units.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_LENGTH\_METRIC\_UNIT\_DEFAULT = -1 | Default, which is fp for fonts and vp for non-fonts. |
| ARKUI\_LENGTH\_METRIC\_UNIT\_PX = 0 | px. |
| ARKUI\_LENGTH\_METRIC\_UNIT\_VP = 1 | vp. |
| ARKUI\_LENGTH\_METRIC\_UNIT\_FP = 2 | fp. |

#### \[h2\]ArkUI\_TextInputContentType

enum ArkUI\_TextInputContentType

**Description**

Enumerates the autofill types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_USER\_NAME = 0 | Username. Password Vault, when enabled, can automatically save and fill in usernames. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PASSWORD | Password. Password Vault, when enabled, can automatically save and fill in passwords. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_NEW\_PASSWORD | New password. Password Vault, when enabled, can automatically generate a new password. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FULL\_STREET\_ADDRESS | Full street address. The scenario-based autofill feature, when enabled, can automatically save and fill in full street addresses. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_HOUSE\_NUMBER | House number. The scenario-based autofill feature, when enabled, can automatically save and fill in house numbers. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_DISTRICT\_ADDRESS | District and county. The scenario-based autofill feature, when enabled, can automatically save and fill in districts and counties. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_CITY\_ADDRESS | City. The scenario-based autofill feature, when enabled, can automatically save and fill in cities. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PROVINCE\_ADDRESS | Province. The scenario-based autofill feature, when enabled, can automatically save and fill in provinces. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_COUNTRY\_ADDRESS | Country. The scenario-based autofill feature, when enabled, can automatically save and fill in countries. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_FULL\_NAME | Full name. The scenario-based autofill feature, when enabled, can automatically save and fill in full names. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_LAST\_NAME | Last name. The scenario-based autofill feature, when enabled, can automatically save and fill in last names. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PERSON\_FIRST\_NAME | First name. The scenario-based autofill feature, when enabled, can automatically save and fill in first names. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PHONE\_NUMBER | Phone number. The scenario-based autofill feature, when enabled, can automatically save and fill in phone numbers. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PHONE\_COUNTRY\_CODE | Country code. The scenario-based autofill feature, when enabled, can automatically save and fill in country codes. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FULL\_PHONE\_NUMBER | Phone number with country code. The scenario-based autofill feature, when enabled, can automatically save and fill in phone numbers with country codes. |
| ARKUI\_TEXTINPUT\_CONTENT\_EMAIL\_ADDRESS | Email address. The scenario-based autofill feature, when enabled, can automatically save and fill in email addresses. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_BANK\_CARD\_NUMBER | Bank card number. The scenario-based autofill feature, when enabled, can automatically save and fill in bank card numbers. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ID\_CARD\_NUMBER | ID card number. The scenario-based autofill feature, when enabled, can automatically save and fill in ID card numbers. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_NICKNAME | Nickname. The scenario-based autofill feature, when enabled, can automatically save and fill in nicknames. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_DETAIL\_INFO\_WITHOUT\_STREET | Address information without street address. The scenario-based autofill feature, when enabled, can automatically save and fill in address information without street addresses. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FORMAT\_ADDRESS | Standard address. The scenario-based autofill feature, when enabled, can automatically save and fill in standard addresses. |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_PASSPORT\_NUMBER | 
Passport number. The scenario-based autofill feature, when enabled, can automatically save and fill in passport numbers.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_VALIDITY | 

Passport validity period. The scenario-based autofill feature, when enabled, can automatically save and fill in passport validity periods.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ISSUE\_AT | 

Passport place of issue. The scenario-based autofill feature, when enabled, can automatically save and fill in the place of issue for passports.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ORGANIZATION | 

Invoice title. The scenario-based autofill feature, when enabled, can automatically save and fill in invoice titles.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_TAX\_ID | 

Tax ID. The scenario-based autofill feature, when enabled, can automatically save and fill in tax IDs.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ADDRESS\_CITY\_AND\_STATE | 

Location. The scenario-based autofill feature, when enabled, can automatically save and fill in locations.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_FLIGHT\_NUMBER | 

Flight number. Currently not supported for automatic saving and auto-filling.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_NUMBER | 

Driver's license number. Currently not supported for automatic saving and auto-filling.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_FILE\_NUMBER | 

Driver's license file number. Currently not supported for automatic saving and auto-filling.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_PLATE | 

License plate number. The scenario-based autofill feature, when enabled, can automatically save and fill in license plate numbers.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_ENGINE\_NUMBER | 

Vehicle registration engine number. Currently not supported for automatic saving and auto-filling.

**Since**: 18

 |
| ARKUI\_TEXTINPUT\_CONTENT\_TYPE\_LICENSE\_CHASSIS\_NUMBER | 

Chassis number. Currently not supported for automatic saving and auto-filling.

**Since**: 18

 |

#### \[h2\]ArkUI\_BarrierDirection

enum ArkUI\_BarrierDirection

**Description**

Enumerates the barrier directions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_BARRIER\_DIRECTION\_START = 0 | The barrier is on the left side of all the referenced components specified by [referencedId](../../../arkts-components/rows-columns-and-stacking/relativecontainer/document.md#barrierstyle12). This is the default value. |
| ARKUI\_BARRIER\_DIRECTION\_END = 1 | The barrier is on the right side of all the referenced components specified by referencedId. |
| ARKUI\_BARRIER\_DIRECTION\_TOP = 2 | The barrier is at the top of all the referenced components specified by referencedId. |
| ARKUI\_BARRIER\_DIRECTION\_BOTTOM = 3 | The barrier is at the bottom of all the referenced components specified by referencedId. |

#### \[h2\]ArkUI\_RelativeLayoutChainStyle

enum ArkUI\_RelativeLayoutChainStyle

**Description**

Enumerates the chain styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD = 0 | Child components are evenly distributed among constraint anchors. This is the default value. |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_SPREAD\_INSIDE = 1 | All child components except the first and last ones are evenly distributed among constraint anchors. |
| ARKUI\_RELATIVE\_LAYOUT\_CHAIN\_STYLE\_PACKED = 2 | There is no gap between child components in the chain. |

#### \[h2\]ArkUI\_TextInputStyle

enum ArkUI\_TextInputStyle

**Description**

Enumerates the text input styles.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXTINPUT\_STYLE\_DEFAULT = 0 | Default style. The caret width is fixed at 1.5 vp, and the caret height is subject to the background height and font size of the selected text. |
| ARKUI\_TEXTINPUT\_STYLE\_INLINE | Inline input style. The background height of the selected text is the same as the height of the text box. |

#### \[h2\]ArkUI\_KeyboardAppearance

enum ArkUI\_KeyboardAppearance

**Description**

Enumerates the appearance modes of the keyboard when the text box is focused.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE = 0 | Default appearance mode, not using the immersive style. |
| ARKUI\_KEYBOARD\_APPEARANCE\_IMMERSIVE = 1 | Immersive style, following the system color mode. |
| ARKUI\_KEYBOARD\_APPEARANCE\_LIGHT\_IMMERSIVE = 2 | Immersive style in light mode. |
| ARKUI\_KEYBOARD\_APPEARANCE\_DARK\_IMMERSIVE = 3 | Immersive style in dark mode. |

#### \[h2\]ArkUI\_TextDataDetectorType

enum ArkUI\_TextDataDetectorType

**Description**

Enumerates the entity types of text recognition.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_PHONE\_NUMBER = 0 | Phone number. |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_URL | URL. |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_EMAIL | Email address. |
| ARKUI\_TEXT\_DATA\_DETECTOR\_TYPE\_ADDRESS | Address. |

#### \[h2\]ArkUI\_ButtonType

enum ArkUI\_ButtonType

**Description**

Enumerates the button types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_BUTTON\_TYPE\_NORMAL = 0 | Normal button (without rounded corners by default). |
| ARKUI\_BUTTON\_TYPE\_CAPSULE = 1 | Capsule-type button (the round corner is half of the height by default). |
| ARKUI\_BUTTON\_TYPE\_CIRCLE = 2 | Circle button. |
| ARKUI\_BUTTON\_ROUNDED\_RECTANGLE = 8 | 
Rounded rectangle button

**Since**: 19

 |

#### \[h2\]ArkUI\_RenderFit

enum ArkUI\_RenderFit

**Description**

Enumerates the sizing and positioning behaviors of animated content in its final state.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_RENDER\_FIT\_CENTER = 0 | The component's content stays at the final size and always aligned with the center of the component. |
| ARKUI\_RENDER\_FIT\_TOP = 1 | The component's content stays at the final size and always aligned with the top center of the component. |
| ARKUI\_RENDER\_FIT\_BOTTOM = 2 | The component's content stays at the final size and always aligned with the bottom center of the component. |
| ARKUI\_RENDER\_FIT\_LEFT = 3 | The component's content stays at the final size and always aligned with the left of the component. |
| ARKUI\_RENDER\_FIT\_RIGHT = 4 | The component's content stays at the final size and always aligned with the right of the component. |
| ARKUI\_RENDER\_FIT\_TOP\_LEFT = 5 | The component's content stays at the final size and always aligned with the upper left corner of the component. |
| ARKUI\_RENDER\_FIT\_TOP\_RIGHT = 6 | The component's content stays at the final size and always aligned with the upper right corner of the component. |
| ARKUI\_RENDER\_FIT\_BOTTOM\_LEFT = 7 | The component's content stays at the final size and always aligned with the lower left corner of the component. |
| ARKUI\_RENDER\_FIT\_BOTTOM\_RIGHT = 8 | The component's content stays at the final size and always aligned with the lower right corner of the component. |
| ARKUI\_RENDER\_FIT\_RESIZE\_FILL = 9 | The component's content is always resized to fill the component's content box, without considering its aspect ratio in the final state. |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN = 10 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. It is always aligned with the center of the component. |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_TOP\_LEFT = 11 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. When there is remaining space in the width direction of the component, the content is left-aligned with the component. When there is remaining space in the height direction of the component, the content is top-aligned with the component. |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_BOTTOM\_RIGHT = 12 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. When there is remaining space in the width direction of the component, the content is right-aligned with the component. When there is remaining space in the height direction of the component, the content is bottom-aligned with the component. |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER = 13 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. It is always aligned with the center of the component, so that its middle part is displayed. |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_TOP\_LEFT = 14 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. When there is remaining space in the width direction, the content is left-aligned with the component, so that its left part is displayed. When there is remaining space in the height direction, the content is top-aligned with the component, so that its top part is displayed. |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_BOTTOM\_RIGHT = 15 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. When there is remaining space in the width direction, the content is right-aligned with the component, so that its right part is displayed. When there is remaining space in the height direction, the content is bottom-aligned with the component, so that its bottom part is displayed. |

#### \[h2\]ArkUI\_SwiperIndicatorType

enum ArkUI\_SwiperIndicatorType

**Description**

Enumerates the navigation indicator types of the **Swiper** component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT = 0 | Dot type. |
| ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT = 1 | Digit type. |

#### \[h2\]ArkUI\_AnimationDirection

enum ArkUI\_AnimationDirection

**Description**

Enumerates the animation playback directions.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ANIMATION\_DIRECTION\_NORMAL = 0 | The animation plays in forward loop mode. |
| ARKUI\_ANIMATION\_DIRECTION\_REVERSE = 1 | The animation plays in reverse loop mode. |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE = 2 | The animation plays in alternating loop mode. When the animation is played for an odd number of times, the playback is in forward direction. When the animation is played for an even number of times, the playback is in reverse direction. |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE\_REVERSE = 3 | The animation plays in reverse alternating loop mode. When the animation is played for an odd number of times, the playback is in reverse direction. When the animation is played for an even number of times, the playback is in forward direction. |

#### \[h2\]ArkUI\_ListItemSwipeActionState

enum ArkUI\_ListItemSwipeActionState

**Description**

Enumerates the item states of [SwipeAction](../../../arkts-components/scroll-and-swipe/listitem/document.md#swipeaction9) of the [Listitem](../../../arkts-components/scroll-and-swipe/listitem/document.md#listitem10) component. The default value is **ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED**.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_COLLAPSED = 0 | Collapsed state. When the list item is swiped in the opposite direction of the main axis, the swipe action item is hidden. |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_EXPANDED = 1 | Expanded state. When the list item is swiped in the opposite direction of the main axis, the swipe action item is shown. |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_STATE\_ACTIONING = 2 | In-action state. The list item is in this state when it enters the delete area. |

#### \[h2\]ArkUI\_ListItemSwipeEdgeEffect

enum ArkUI\_ListItemSwipeEdgeEffect

**Description**

Enumerates the item edge effects of [swipeAction](../../../arkts-components/scroll-and-swipe/listitem/document.md#swipeaction9) of the **Listitem** component. The default value is **ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING**.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING = 0 | When the list item scrolls to the edge of the list, it can continue to scroll for a distance. |
| ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_NONE = 1 | The list item cannot scroll beyond the edge of the list. |

#### \[h2\]ArkUI\_ListItemSwipeActionDirection

enum ArkUI\_ListItemSwipeActionDirection

**Description**

Enumerates the swipe action menu display directions for **ListItem** components.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_START = 0 | For vertical lists: left side in LTR mode, right side in RTL mode. For horizontal lists: top side. |
| ARKUI\_LIST\_ITEM\_SWIPE\_ACTION\_DIRECTION\_END = 1 | For vertical lists: right side in LTR mode, left side in RTL mode. For horizontal lists: bottom side. |

#### \[h2\]ArkUI\_AnimationStatus

enum ArkUI\_AnimationStatus

**Description**

Enumerates the playback states of the frame-by-frame animation.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ANIMATION\_STATUS\_INITIAL = 0 | The animation is in the initial state. |
| ARKUI\_ANIMATION\_STATUS\_RUNNING = 1 | The animation is being played. |
| ARKUI\_ANIMATION\_STATUS\_PAUSED = 2 | The animation is paused. |
| ARKUI\_ANIMATION\_STATUS\_STOPPED = 3 | The animation is stopped. |

#### \[h2\]ArkUI\_AnimationFillMode

enum ArkUI\_AnimationFillMode

**Description**

Enumerates the states before and after execution of the frame-by-frame animation.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ANIMATION\_FILL\_MODE\_NONE = 0 | Before execution, the animation does not apply any styles to the target component. After execution, the animation restores the target component to its default state. |
| ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS = 1 | The target component retains the state set by the last keyframe encountered during execution of the animation. |
| ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS = 2 | The animation applies the values defined in the first relevantage keyframe once it is applied to the target component, and retains the values during the period set by [delay](../native-animate-h/document.md#oh_arkui_animateoption_setdelay). |
| ARKUI\_ANIMATION\_FILL\_MODE\_BOTH = 3 | The animation follows the rules of [ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](#arkui_animationfillmode) and [ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS](#arkui_animationfillmode) to extend the animation properties in both directions. |

#### \[h2\]ArkUI\_ErrorCode

enum ArkUI\_ErrorCode

**Description**

Enumerates the error codes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ERROR\_CODE\_NO\_ERROR = 0 | No error. |
| ARKUI\_ERROR\_CODE\_PARAM\_INVALID = 401 | Parameter error. |
| ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR = 500 | 
API initialization error.

**Since**: 18

 |
| ARKUI\_ERROR\_CODE\_INTERNAL\_ERROR = 100001 | 

Internal error, such as failure due to internal environment issues or operation failure caused by internal execution errors.

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_PARAM\_ERROR = 100023 | 

Parameter error. For details about the error code, see [100023 Parameter Error](../../../error-codes/ui/custom-node-error-codes/document.md#section100023-parameter-error).

**Since**: 21

 |
| ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID = 103501 | 

The **XComponent** is in an invalid or unsupported state. For details, see [XComponent Error Codes](../../../error-codes/ui/xcomponent-error-codes/document.md).

**Since**: 19

 |
| ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED = 106102 | The component does not support specific attributes or events. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md). |
| ARKUI\_ERROR\_CODE\_NOT\_SUPPROTED\_FOR\_ARKTS\_NODE = 106103 | The corresponding operations cannot be performed on the node created by ArkTS. For details about the error code, see [106103 Operation Not Allowed on Nodes Created by ArkTS](../../../error-codes/ui/custom-node-error-codes/document.md#section106103-operation-not-allowed-on-nodes-created-by-arkts). |
| ARKUI\_ERROR\_CODE\_ADAPTER\_NOT\_BOUND = 106104 | The adapter for lazy loading is not bound to the component. For details about the error code, see [106104 Adapter Not Bound](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106104-adapter-not-bound). |
| ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_EXIST = 106105 | The adapter already exists. For details about the error code, see [106105 Adapter Already Exists](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106105-adapter-already-exists). |
| ARKUI\_ERROR\_CODE\_CHILD\_NODE\_EXIST = 106106 | Failed to add the adapter because the corresponding node already has a subnode. For details about the error code, see [106106 Child Node Exists](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106106-child-node-exists). |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE = 106107 | The parameter length in the parameter event exceeds the limit. For details about the error code, see [106107 Index Out of Range](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106107-index-out-of-range). |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID = 106108 | The data does not exist in the component event. For details about the error code, see [106108 Data Not Found](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106108-data-not-found). |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_NO\_RETURN = 106109 | The component event does not support return values. For details about the error code, see [106109 Return Value Not Supported](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106109-return-value-not-supported). |
| ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE = 106110 | 

This event type is not supported. For details about the error code, see [106110 Unsupported Event Type](../../../error-codes/ui/nodeadapter-error-codes/document.md#section106110-unsupported-event-type).

**Since**: 21

 |
| ARKUI\_ERROR\_CODE\_NODE\_INDEX\_INVALID = 106200 | 

Invalid index.

For details about the error code, see [106200 Invalid Index Value](../../../error-codes/ui/router-error-codes/document.md#section106200-invalid-index-value).

 |
| ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED = 106201 | 

Failed to obtain the route navigation information.

For details about the error code, see [106201 Failed to Obtain Route Navigation Information](../../../error-codes/ui/router-error-codes/document.md#section106201-failed-to-obtain-route-navigation-information).

 |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR = 106202 | 

The passed buffer size is invalid (the data is too large).

For details about the error code, see [106202 Invalid Buffer Size](../../../error-codes/ui/router-error-codes/document.md#section106202-invalid-buffer-size).

 |
| ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE = 106203 | 

The passed node is not mounted to the component tree. For details about the error code, see [106203 Passed Node Not Mounted to Component Tree](../../../error-codes/ui/custom-node-error-codes/document.md#section106203-passed-node-not-mounted-to-component-tree).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD = 106204 | 

Operations on the provided node are not supported on non-UI threads. For details about the error code, see [106204 Operations on the Provided Node Not Supported on Non-UI Threads](../../../error-codes/ui/custom-node-error-codes/document.md#section106204-operations-on-the-provided-node-not-supported-on-non-ui-threads).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_FORCE\_DARK\_CONFIG\_INVALID = 106205 | 

The input parameter for the color inversion capability is incorrect. For details about the error code, see [106205 Invalid Input Parameter for the Color Inversion Capability](../../../error-codes/ui/color-inversion-error-codes/document.md#section106205-invalid-input-parameter-for-the-color-inversion-capability).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED = 106206 | 

The node has been accepted as an auxiliary node. For details about the error code, see [106206 The Node Has Been Accepted as an Auxiliary Node](../../../error-codes/ui/auxiliary-node-error-codes/document.md#section106206-the-node-has-been-accepted-as-an-auxiliary-node).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_NODE\_HAS\_PARENT = 106207 | 

The accepted node already has a parent node. For details about the error code, see [106207 The Auxiliary Node to Accept Has a Parent Node](../../../error-codes/ui/auxiliary-node-error-codes/document.md#section106207-the-auxiliary-node-to-accept-has-a-parent-node).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_BE\_ADOPTED = 106208 | 

The node cannot be accepted as an auxiliary node. For details about the error code, see [106208 The Node Cannot Be Accepted as an Auxiliary Node](../../../error-codes/ui/auxiliary-node-error-codes/document.md#section106208-the-node-cannot-be-accepted-as-an-auxiliary-node).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_ADOPT\_TO = 106209 | 

The node cannot accept other nodes. For details about the error code, see [106209 The Node Cannot Accept Other Nodes](../../../error-codes/ui/auxiliary-node-error-codes/document.md#section106209-the-node-cannot-accept-other-nodes).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_NOT\_IN\_ADOPTED\_CHILDREN = 106210 | 

The node is not an auxiliary node accepted by the target node. For details about the error code, see [106210 The Node Is Not an Affiliated Node Accepted by the Target Node](../../../error-codes/ui/auxiliary-node-error-codes/document.md#section106210-the-node-is-not-an-affiliated-node-accepted-by-the-target-node).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE = 106401 | 

The current node is not a custom node. For details, see [Render Node Error Codes](../../../error-codes/ui/render-node-error-codes/document.md).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_CHILD\_EXISTED = 106402 | 

The current node already has child nodes. For details, see [Render Node Error Codes](../../../error-codes/ui/render-node-error-codes/document.md).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_RENDER\_PARENT\_EXISTED = 106403 | 

The current render node has a parent component. For details, see [Render Node Error Codes](../../../error-codes/ui/render-node-error-codes/document.md).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST = 106404 | 

Corresponding render child node not found. For details, see [Render Node Error Codes](../../../error-codes/ui/render-node-error-codes/document.md).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE = 106405 | 

The parameter value is out of range. For details, see [Render Node Error Codes](../../../error-codes/ui/render-node-error-codes/document.md).

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE = 106406 | 

The current render node is obtained from the [FrameNode](../../structs/arkui-node--00020177/document.md). For details about the error code, see [106406 Current Render Node Is Obtained from FrameNode](../../../error-codes/ui/render-node-error-codes/document.md#section106406-current-render-node-is-obtained-from-framenode).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE = 106407 | 

The current render node is obtained from the [FrameNode](../../structs/arkui-node--00020177/document.md) and the [FrameNode](../../structs/arkui-node--00020177/document.md) has not been adopted as an affiliated node or has been disposed. For details about the error code, see [106407 Current Render Node Is Obtained from FrameNode and the FrameNode Is Disposed or No Longer Adopted](../../../error-codes/ui/render-node-error-codes/document.md#section106407-current-render-node-is-obtained-from-framenode-and-the-framenode-is-disposed-or-no-longer-adopted).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_RENDER\_NOT\_ADOPTED\_NODE = 106408 | 

The current node is not in the adopted state. For details about the error code, see [106408 Current Node Is Not in Adopted State](../../../error-codes/ui/render-node-error-codes/document.md#section106408-current-node-is-not-in-adopted-state).

**Since**: 22

 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE = 150001 | 

The current node is not focusable. For details about the error code, see [150001 Component Not Focusable](../../../error-codes/ui/focus-error-codes/document.md#section150001-component-not-focusable).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR = 150002 | 

An ancestor of the current node is not focusable. For details about the error code, see [150002 Ancestor Component Not Focusable](../../../error-codes/ui/focus-error-codes/document.md#section150002-ancestor-component-not-focusable).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT = 150003 | 

The current node does not exist. For details about the error code, see [150003 Component Does Not Exist](../../../error-codes/ui/focus-error-codes/document.md#section150003-component-does-not-exist).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_TIMEOUT = 160002 | 

Snapshot timed out. For details, see [Snapshot Error Codes](../../../error-codes/ui/snapshot-error-codes/document.md).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER = 180001 | The component is not a scrollable container. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md). |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH = 180002 | The buffer is not large enough. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md). |
| ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT = 180003 | 

The event is not a cloned event. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL = 180004 | 

The component status is abnormal. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md).

**Since**: 15

 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT = 180005 | 

No component hit to respond to the event. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md).

**Since**: 15

 |
| ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED = 180006 | 

Input event type not supported.

**Since**: 20

 |
| ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING = 180101 | 

Invalid styled string. For details, see [Styled String Error Codes](../../../error-codes/ui/styled-string-error-codes/document.md).

**Since**: 14

 |
| ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID = 190001 | 

Invalid UIContext object. For details, see [UI Context Error Codes](../../../error-codes/ui/ui-context-error-codes/document.md).

**Since**: 18

 |
| ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID = 190002 | 

Invalid callback function. For details, see [UI Context Error Codes](../../../error-codes/ui/ui-context-error-codes/document.md).

**Since**: 18

 |
| ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED = 180102 | 

The gesture recognizer type is not supported. For details, see [Interaction Event Error Codes](../../../error-codes/ui/interaction-event-error-codes/document.md).

**Since**: 18

 |
| ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED = 190004 | 

The operation is not allowed in the current phase. For details, see [Drag Event Error Codes](../../../error-codes/ui/drag-event-error-codes/document.md).

**Since**: 19

 |

#### \[h2\]ArkUI\_ScrollSource

enum ArkUI\_ScrollSource

**Description**

Enumerates scroll sources.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_SOURCE\_DRAG = 0 | Finger dragging. |
| ARKUI\_SCROLL\_SOURCE\_FLING = 1 | Inertia scrolling after finger dragging. |
| ARKUI\_SCROLL\_SOURCE\_EDGE\_EFFECT = 2 | [EdgeEffect.Spring](../../../arkts-components/common-definitions/enums/document.md#edgeeffect) for boundary crossing. |
| ARKUI\_SCROLL\_SOURCE\_OTHER\_USER\_INPUT = 3 | User input other than dragging, such as mouse wheel and keyboard events. |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR = 4 | Scrollbar dragging. |
| ARKUI\_SCROLL\_SOURCE\_SCROLL\_BAR\_FLING = 5 | Inertial scrolling after scrollbar dragging. |
| ARKUI\_SCROLL\_SOURCE\_SCROLLER = 6 | Scrolling by the scroll controller (without animation). |
| ARKUI\_SCROLL\_SOURCE\_ANIMATION = 7 | Scrolling by the scroll controller (with animation). |

#### \[h2\]ArkUI\_SafeAreaType

enum ArkUI\_SafeAreaType

**Description**

Enumerates the types of expanded safe areas.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SAFE\_AREA\_TYPE\_SYSTEM = 1 | Default non-safe area of the system, including the status bar and navigation bar. This is the default value. |
| ARKUI\_SAFE\_AREA\_TYPE\_CUTOUT = 1 << 1 | Non-safe area of the device, for example, the notch area. |
| ARKUI\_SAFE\_AREA\_TYPE\_KEYBOARD = 1 << 2 | Soft keyboard area. |

#### \[h2\]ArkUI\_SafeAreaEdge

enum ArkUI\_SafeAreaEdge

**Description**

Enumerates the edges for expanding the safe area.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_SAFE\_AREA\_EDGE\_TOP = 1 | Top edge. This is the default value. |
| ARKUI\_SAFE\_AREA\_EDGE\_BOTTOM = 1 << 1 | Bottom edge. |
| ARKUI\_SAFE\_AREA\_EDGE\_START = 1 << 2 | Start edge. |
| ARKUI\_SAFE\_AREA\_EDGE\_END = 1 << 3 | End edge. |

#### \[h2\]ArkUI\_FocusMove

enum ArkUI\_FocusMove

**Description**

Enumerates the focus movement directions.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_FOCUS\_MOVE\_FORWARD = 0 | Move focus forward. |
| ARKUI\_FOCUS\_MOVE\_BACKWARD = 1 | Move focus backward. |
| ARKUI\_FOCUS\_MOVE\_UP = 2 | Move focus up. |
| ARKUI\_FOCUS\_MOVE\_DOWN = 3 | Move focus down. |
| ARKUI\_FOCUS\_MOVE\_LEFT = 4 | Move focus left. |
| ARKUI\_FOCUS\_MOVE\_RIGHT = 5 | Move focus right. |

#### \[h2\]ArkUI\_ListItemGroupArea

enum ArkUI\_ListItemGroupArea

**Description**

Enumerates the areas in the [ListItemGroup](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md) component. The default value is **ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE**.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_LIST\_ITEM\_GROUP\_AREA\_OUTSIDE = 0 | Outside the area of the **ListItemGroup** component. |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_NONE = 1 | Area without the [header](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions), [footer](../../../arkts-components/scroll-and-swipe/listitemgroup/document.md#listitemgroupoptions), and [ListItem](../../../arkts-components/scroll-and-swipe/listitem/document.md#listitem10) in the **ListItemGroup** component. |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_ITEM = 2 | List item area of the **ListItemGroup** component. |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_HEADER = 3 | Header area of the **ListItemGroup** component. |
| ARKUI\_LIST\_ITEM\_SWIPE\_AREA\_FOOTER = 4 | Footer area of the **ListItemGroup** component. |

#### \[h2\]ArkUI\_KeyboardAvoidMode

enum ArkUI\_KeyboardAvoidMode

**Description**

Enumerates the soft keyboard avoidance modes.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_KEYBOARD\_AVOID\_MODE\_DEFAULT = 0 | Automatically avoids the soft keyboard and compresses the height when reaching the maximum limit. |
| ARKUI\_KEYBOARD\_AVOID\_MODE\_NONE = 1 | The layout is not adjusted to avoid the keyboard. |

#### \[h2\]ArkUI\_HoverModeAreaType

enum ArkUI\_HoverModeAreaType

**Description**

Enumerates the types of display areas for the hover mode.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_HOVER\_MODE\_AREA\_TYPE\_TOP = 0 | Upper half screen. |
| ARKUI\_HOVER\_MODE\_AREA\_TYPE\_BOTTOM = 1 | Lower half screen. |

#### \[h2\]ArkUI\_ExpandMode

enum ArkUI\_ExpandMode

**Description**

Enumerates the expansion mode of child nodes.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_NOT\_EXPAND = 0 | Child nodes are not expanded. |
| ARKUI\_EXPAND = 1 | Child nodes are expanded immediately upon rendering. |
| ARKUI\_LAZY\_EXPAND = 2 | Lazy expansion, indicating that child nodes are only expanded when needed. For details about the node expansion conditions, see [LazyForEach: Lazy Data Loading](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach). |

#### \[h2\]ArkUI\_NavDestinationState

enum ArkUI\_NavDestinationState

**Description**

Enumerates the states of the [NavDestination](../../../arkts-components/navigation-and-switching/navdestination/document.md) component.

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_SHOW = 0 | The **NavDestination** component is displayed. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_HIDE = 1 | The **NavDestination** component is hidden. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_APPEAR = 2 | The **NavDestination** component is mounted to the component tree. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_DISAPPEAR = 3 | The **NavDestination** component is unmounted from the component tree. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_SHOW = 4 | The **NavDestination** is about to be displayed. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_HIDE = 5 | The **NavDestination** is about to be hidden. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_APPEAR = 6 | The **NavDestination** is about to be mounted to the component tree. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_DISAPPEAR = 7 | The **NavDestination** component is about to be unmounted from the component tree. |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_BACK\_PRESS = 100 | The back button is pressed for the **NavDestination** component. |

#### \[h2\]ArkUI\_RouterPageState

enum ArkUI\_RouterPageState

**Description**

Enumerates the states of [Router Page](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-router/document.md).

**Since**: 12

| Value | Description |
| :-- | :-- |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_APPEAR = 0 | The page is about to be displayed. |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_DISAPPEAR = 1 | The page is about to be destroyed. |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_SHOW = 2 | The page is displayed. |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_HIDE = 3 | The page is hidden. |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_BACK\_PRESS = 4 | The back button is pressed for the page. |

#### \[h2\]ArkUI\_UIState

enum ArkUI\_UIState

**Description**

Enumerates the UI states of a component, used for handling state-specific styles.

**Since**: 20

| Value | Description |
| :-- | :-- |
| UI\_STATE\_NORMAL = 0 | Normal state. |
| UI\_STATE\_PRESSED = 1 << 0 | Pressed state. |
| UI\_STATE\_FOCUSED = 1 << 1 | Focused state. |
| UI\_STATE\_DISABLED = 1 << 2 | Disabled state. |
| UI\_STATE\_SELECTED = 1 << 3 | Selected state. This state is supported only by specific component types: **Checkbox**, **Radio**, **Toggle**, **List**, **Grid**, and **MenuItem**. |

#### \[h2\]ArkUI\_FocusWrapMode

enum ArkUI\_FocusWrapMode

**Description**

Enumerates the focus wrap modes for cross-axis arrow keys. The default value is **ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT** for the **Grid** and **List** components.

**Since**: 20

| Value | Description |
| :-- | :-- |
| ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT = 0 | Default mode, where focus does not wrap when arrow keys are used. |
| ARKUI\_FOCUS\_WRAP\_WITH\_ARROW = 1 | Auto mode, where focus wraps automatically when arrow keys are used. |

#### \[h2\]ArkUI\_ItemFillPolicy

enum ArkUI\_ItemFillPolicy

**Description**

Enumerates column count policies for different [responsive breakpoints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints).

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_ITEMFILLPOLICY\_NONE = -1 | No responsive breakpoint policy is set. |
| ARKUI\_ITEMFILLPOLICY\_DEFAULT = 0 | 
**List** or **Swiper** component: 1 column (SM or smaller), 2 columns (MD), 3 columns (LG or larger).

**Grid** or **WaterFlow** component: 2 columns (SM or smaller), 3 columns (MD), 5 columns (LG or larger).

 |
| ARKUI\_ITEMFILLPOLICY\_SM1MD2LG3 = 1 | 1 column (SM or smaller), 2 columns (MD), 3 columns (LG or larger). |
| ARKUI\_ITEMFILLPOLICY\_SM2MD3LG5 = 2 | 2 columns (SM or smaller), 3 columns (MD), 5 columns (LG or larger). |

#### \[h2\]ArkUI\_ScrollSnapAnimationSpeed

enum ArkUI\_ScrollSnapAnimationSpeed

**Description**

Enumerates scroll snap animation speeds for list components.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL = 0 | Normal scroll snap animation speed. |
| ARKUI\_SCROLL\_SNAP\_ANIMATION\_SLOW = 1 | Slow scroll snap animation speed. |

#### \[h2\]ArkUI\_EdgeDirection

enum ArkUI\_EdgeDirection

**Description**

Enumerates rectangle edge directions.

**Since**: 20

| Value | Description |
| :-- | :-- |
| ARKUI\_EDGE\_DIRECTION\_ALL = 0 | All four edges. |
| ARKUI\_EDGE\_DIRECTION\_LEFT = 1 << 0 | Left edge. |
| ARKUI\_EDGE\_DIRECTION\_RIGHT = 1 << 1 | Right edge. |
| ARKUI\_EDGE\_DIRECTION\_TOP = 1 << 2 | Top edge. |
| ARKUI\_EDGE\_DIRECTION\_BOTTOM = 1 << 3 | Bottom edge. |

#### \[h2\]ArkUI\_CornerDirection

enum ArkUI\_CornerDirection

**Description**

Enumerates corner directions.

**Since**: 20

| Value | Description |
| :-- | :-- |
| ARKUI\_CORNER\_DIRECTION\_ALL = 0 | All four corners. |
| ARKUI\_CORNER\_DIRECTION\_TOP\_LEFT = 1 << 0 | Upper left corner. |
| ARKUI\_CORNER\_DIRECTION\_TOP\_RIGHT = 1 << 1 | Upper right corner. |
| ARKUI\_CORNER\_DIRECTION\_BOTTOM\_LEFT = 1 << 2 | Lower left corner. |
| ARKUI\_CORNER\_DIRECTION\_BOTTOM\_RIGHT = 1 << 3 | Lower right corner. |

#### \[h2\]ArkUI\_LayoutPolicy

enum ArkUI\_LayoutPolicy

**Description**

Enumerates layout policies.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_LAYOUTPOLICY\_MATCHPARENT = 0 | The component size matches parent container dimensions. |
| ARKUI\_LAYOUTPOLICY\_WRAPCONTENT = 1 | The component size wraps its content, constrained by parent container bounds. |
| ARKUI\_LAYOUTPOLICY\_FIXATIDEALSIZE = 2 | The component size wraps its content, unconstrained by parent container bounds. |

#### \[h2\]ArkUI\_PixelRoundCalcPolicy

enum ArkUI\_PixelRoundCalcPolicy

**Description**

Enumerates pixel rounding calculation policies.

**Since**: 21

| Value | Description |
| :-- | :-- |
| ARKUI\_PIXELROUNDCALCPOLICY\_NOFORCEROUND = 0 | No forced rounding calculation. |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCECEIL = 1 | Round-up calculation. |
| ARKUI\_PIXELROUNDCALCPOLICY\_FORCEFLOOR = 2 | Round-down calculation. |

#### \[h2\]ArkUI\_GridItemAlignment

enum ArkUI\_GridItemAlignment

**Description**

Enumerates the alignment modes of the [GridItem](../../../arkts-components/scroll-and-swipe/griditem/document.md) component.

**Since**: 22

| Value | Description |
| :-- | :-- |
| GRID\_ITEM\_ALIGNMENT\_DEFAULT = 0 | Use the default alignment mode of the grid. |
| GRID\_ITEM\_ALIGNMENT\_STRETCH = 1 | Use the height of the tallest grid item in a row as the height for all other grid items in that row. |

#### \[h2\]ArkUI\_GridItemStyle

enum ArkUI\_GridItemStyle

**Description**

Enumerates styles of grid items.

**Since**: 22

| Value | Description |
| :-- | :-- |
| GRID\_ITEM\_STYLE\_NONE = 0 | No style. |
| GRID\_ITEM\_STYLE\_PLAIN = 1 | Hover or press style. |

#### \[h2\]ArkUI\_TextMenuItemId

enum ArkUI\_TextMenuItemId

**Description**

Enumerates the IDs of text menu items.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_CUT = 0 | Clip. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_COPY = 1 | Copy. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_PASTE = 2 | Paste. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SELECT\_ALL = 3 | Select all. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_COLLABORATION\_SERVICE = 4 | Collaboration service. For example, cross-device interaction, including cross-device camera access. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_CAMERA\_INPUT = 5 | Camera input. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_AI\_WRITER = 6 | AI-assisted writing. This menu item requires the large language model. If no large language model is available, this menu item does not take effect. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_TRANSLATE = 7 | Translate. The translation service is provided for the selected text. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SEARCH = 8 | Search. This menu item launches a browser to search for the selected text. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_SHARE = 9 | Share. This menu item launches a window for sharing the selected text. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_URL = 10 | Open a link. This menu item provides the redirection service for the selected URL, launching a browser search or application page. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_EMAIL = 11 | New Email. This menu item provides the redirection service for the selected email address, launching the email application. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_PHONE\_NUMBER = 12 | Call. This menu item provides the redirection service for the selected phone number, launching the phone dialer page. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_ADDRESS = 13 | Navigate. This menu item provides the redirection service for the selected address, launching the map application. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_DATA\_TIME = 14 | New event. This menu item provides the redirection service for the selected date and time, launching the page for creating a calendar event. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_ASK\_AI = 15 | Ask AI. This menu item provides the AI query capability for the selected text. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_APP\_RESERVED\_BEGIN = 10000 | Start ID of a custom menu item. In addition to the built-in menu item IDs, you can also customize menu item IDs. |
| ARKUI\_TEXT\_MENU\_ITEM\_ID\_APP\_RESERVED\_END = 20000 | End ID of a custom menu item. In addition to the built-in menu item IDs, you can also customize menu item IDs. |

#### \[h2\]ArkUI\_TextSpanType

enum ArkUI\_TextSpanType

**Description**

Enumerates the recognition types of a custom text selection menu.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_SPAN\_TYPE\_TEXT = 0 | Text. |
| ARKUI\_TEXT\_SPAN\_TYPE\_IMAGE = 1 | Image. |
| ARKUI\_TEXT\_SPAN\_TYPE\_MIXED = 2 | Mixed text and image. |
| ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT = 3 | If this type and other types are set, the menu corresponding to the type of the selected text is displayed after the text is selected. If this type is set but other types are not set, the menu corresponding to this type is displayed after the text is selected. For example, if there are two menus whose recognition types are **ARKUI\_TEXT\_SPAN\_TYPE\_TEXT** and **ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT** respectively, the menu corresponding to **ARKUI\_TEXT\_SPAN\_TYPE\_TEXT** is displayed when the text is selected, and the menu corresponding to **ARKUI\_TEXT\_SPAN\_TYPE\_DEFAULT** is displayed when the image is selected. |

#### \[h2\]ArkUI\_TextResponseType

enum ArkUI\_TextResponseType

**Description**

Enumerates the response types of a custom text selection menu.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK = 0 | The menu is displayed when the component is right-clicked. |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_LONG\_PRESS = 1 | The menu is displayed when the component is long-pressed. |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_SELECT = 2 | The menu is displayed when the component is selected. |
| ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT = 3 | If this type and other types are set, the menu corresponding to the type is displayed when the operation of another type is triggered. If this type is set but other types are not set, the menu corresponding to this type is displayed when an operation of another type is triggered. For example, if there are two menus whose response types are **ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK** and **ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT** respectively, the menu corresponding to **ARKUI\_TEXT\_RESPONSE\_TYPE\_RIGHT\_CLICK** is displayed when you right-click the menu, and the menu corresponding to **ARKUI\_TEXT\_RESPONSE\_TYPE\_DEFAULT** is displayed when you hold down the right mouse button. |

#### Function Description

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_Create()

ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Create()

**Description**

Creates layout constraints.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* | Pointer to the created layout constraint. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_Copy()

ArkUI\_LayoutConstraint\* OH\_ArkUI\_LayoutConstraint\_Copy(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Performs a deep copy of a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* | Pointer to the new layout constraint. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_Dispose()

void\* OH\_ArkUI\_LayoutConstraint\_Dispose(ArkUI\_LayoutConstraint\* Constraint)

**Description**

Disposes of a layout constraint pointer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Null pointer. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetMaxWidth()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxWidth(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the maximum width using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Maximum width, in pixels. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetMinWidth()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinWidth(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the minimum width using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Minimum width, in px. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetMaxHeight()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetMaxHeight(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the maximum height using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Maximum height, in px. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetMinHeight()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetMinHeight(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the minimum height using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Minimum height, in px. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceWidth()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceWidth(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the width percentage reference using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Width percentage reference. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceHeight()

int32\_t OH\_ArkUI\_LayoutConstraint\_GetPercentReferenceHeight(const ArkUI\_LayoutConstraint\* Constraint)

**Description**

Obtains the height percentage reference using a layout constraint.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Height percentage reference. |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetMaxWidth()

void OH\_ArkUI\_LayoutConstraint\_SetMaxWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the maximum width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Maximum width, in px. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetMinWidth()

void OH\_ArkUI\_LayoutConstraint\_SetMinWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the minimum width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Minimum width, in px. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetMaxHeight()

void OH\_ArkUI\_LayoutConstraint\_SetMaxHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the maximum height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Maximum height, in px. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetMinHeight()

void OH\_ArkUI\_LayoutConstraint\_SetMinHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the minimum height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Minimum height, in px. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceWidth()

void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceWidth(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the width percentage reference.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Width percentage reference. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceHeight()

void OH\_ArkUI\_LayoutConstraint\_SetPercentReferenceHeight(ArkUI\_LayoutConstraint\* Constraint, int32\_t value)

**Description**

Sets the height percentage reference.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_LayoutConstraint](../../structs/arkui-layoutconstraint/document.md)\* Constraint | Pointer to the layout constraint. |
| int32\_t value | Height percentage reference. The value range is \[0, +∞). |

#### \[h2\]OH\_ArkUI\_DrawContext\_GetCanvas()

void\* OH\_ArkUI\_DrawContext\_GetCanvas(ArkUI\_DrawContext\* context)

**Description**

Obtains the pointer to the canvas for drawing, which can be converted into the [OH\_Drawing\_Canvas](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-drawing-canvas/document.md) pointer of the graphics library for drawing.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawContext](../../structs/arkui-drawcontext/document.md)\* context | Pointer to the drawing context. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to the canvas for drawing. |

#### \[h2\]OH\_ArkUI\_DrawContext\_GetSize()

ArkUI\_IntSize OH\_ArkUI\_DrawContext\_GetSize(ArkUI\_DrawContext\* context)

**Description**

Obtains the size of a drawing area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawContext](../../structs/arkui-drawcontext/document.md)\* context | Pointer to the drawing context. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_IntSize](../../structs/arkui-intsize/document.md) | Size of the drawing area. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_Create()

ArkUI\_WaterFlowSectionOption\* OH\_ArkUI\_WaterFlowSectionOption\_Create()

**Description**

Creates the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_Dispose()

void OH\_ArkUI\_WaterFlowSectionOption\_Dispose(ArkUI\_WaterFlowSectionOption\* option)

**Description**

Disposes of the pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetSize()

void OH\_ArkUI\_WaterFlowSectionOption\_SetSize(ArkUI\_WaterFlowSectionOption\* option,int32\_t size)

**Description**

Sets the array length for a water flow section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t size | Size of the array. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetSize()

int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetSize(ArkUI\_WaterFlowSectionOption\* option)

**Description**

Obtains the length of the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration array.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Size of the array. If **\-1** is returned, an error code indicating failure is returned. The possible cause is that the **option** parameter is abnormal, for example, a null pointer. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount()

void OH\_ArkUI\_WaterFlowSectionOption\_SetItemCount(ArkUI\_WaterFlowSectionOption\* option,int32\_t index, int32\_t itemCount)

**Description**

Sets the number of [water flow items](../../../arkts-components/scroll-and-swipe/flowitem/document.md) in the section.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |
| int32\_t itemCount | Number of [water flow items](../../../arkts-components/scroll-and-swipe/flowitem/document.md) in the section. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetItemCount()

int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetItemCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)

**Description**

Obtains the number of [water flow items](../../../arkts-components/scroll-and-swipe/flowitem/document.md) at the corresponding index based on the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the target water flow section. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of items in the water flow section. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount()

void OH\_ArkUI\_WaterFlowSectionOption\_SetCrossCount(ArkUI\_WaterFlowSectionOption\* option,int32\_t index, int32\_t crossCount)

**Description**

Sets the number of columns (in a vertical layout) or rows (in a horizontal layout) of a water flow.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the target water flow section. |
| int32\_t crossCount | Number of columns or rows, depending on the layout direction. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetCrossCount()

int32\_t OH\_ArkUI\_WaterFlowSectionOption\_GetCrossCount(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)

**Description**

Obtains the number of layout grids at the corresponding index based on the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the target water flow section. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of columns or rows, depending on the layout direction. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap()

void OH\_ArkUI\_WaterFlowSectionOption\_SetColumnGap(ArkUI\_WaterFlowSectionOption\* option,int32\_t index, float columnGap)

**Description**

Sets the gap between columns in the specified water flow section.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the target water flow section. |
| float columnGap | Gap between columns. Unit: vp. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetColumnGap()

float OH\_ArkUI\_WaterFlowSectionOption\_GetColumnGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)

**Description**

Obtains the gap between columns in the water flow section that matches the specified index.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the target water flow section. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Gap between columns. Unit: vp. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap()

void OH\_ArkUI\_WaterFlowSectionOption\_SetRowGap(ArkUI\_WaterFlowSectionOption\* option,int32\_t index, float rowGap)

**Description**

Sets the gap between rows in the **FlowItem** section.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to a water flow section configuration. |
| int32\_t index | Index of the **FlowItem** section configuration array. |
| float rowGap | Gap between rows. Unit: vp. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetRowGap()

float OH\_ArkUI\_WaterFlowSectionOption\_GetRowGap(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)

**Description**

Obtains the gap between rows in the section at the corresponding index based on the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Gap between rows. Unit: vp. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_SetMargin()

void OH\_ArkUI\_WaterFlowSectionOption\_SetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index,float marginTop, float marginRight, float marginBottom, float marginLeft)

**Description**

Sets the margins for the specified water flow section.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |
| float marginTop | Top margin of [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |
| float marginRight | Right margin of [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |
| float marginBottom | Bottom margin of [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |
| float marginLeft | Left margin of [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_GetMargin()

ArkUI\_Margin OH\_ArkUI\_WaterFlowSectionOption\_GetMargin(ArkUI\_WaterFlowSectionOption\* option, int32\_t index)

**Description**

Obtains the top margin of the section at the corresponding index based on the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_Margin](../../structs/arkui-margin/document.md) | Margins. Unit: vp. |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex()

void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex(ArkUI\_WaterFlowSectionOption\* option,int32\_t index, float(\*callback)(int32\_t itemIndex))

**Description**

Obtains the main axis size of a specified water flow item based on **itemIndex** in the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. To use custom data in the callback, call [OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindexwithuserdata).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |
| callback | Callback used to return the result. **itemIndex** indicates the index of [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md). |

#### \[h2\]OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData()

void OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndexWithUserData(ArkUI\_WaterFlowSectionOption\* option, int32\_t index, void\* userData,float (\*callback)(int32\_t itemIndex, void\* userData))

**Description**

Obtains the main axis size of a specified water flow item based on **itemIndex** in the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. The difference between this API and [OH\_ArkUI\_WaterFlowSectionOption\_RegisterGetItemMainSizeCallbackByIndex](#oh_arkui_waterflowsectionoption_registergetitemmainsizecallbackbyindex) is that this API allows you to pass custom data (**userData**) and receive the data in the callback function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_WaterFlowSectionOption](../../structs/arkui-waterflowsectionoption/document.md)\* option | Pointer to the [FlowItem](../../../arkts-components/scroll-and-swipe/flowitem/document.md) section configuration. |
| int32\_t index | Index of the target water flow section. |
| void\* userData | Pointer to user-defined data, which will be passed back to the user in the callback. |
| callback | Callback used to return the result. **itemIndex**: index of the [water flow item](../../../arkts-components/scroll-and-swipe/flowitem/document.md); **userData**: user-defined data. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_Create()

ArkUI\_GuidelineOption\* OH\_ArkUI\_GuidelineOption\_Create(int32\_t size)

**Description**

Creates guideline options in [RelativeContainer](../../../arkts-components/rows-columns-and-stacking/relativecontainer/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t size | Number of guidelines. The value range is \[0, +∞). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* | Pointer to a guideline configuration. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_Dispose()

void OH\_ArkUI\_GuidelineOption\_Dispose(ArkUI\_GuidelineOption\* guideline)

**Description**

Disposes of a guideline configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_SetId()

void OH\_ArkUI\_GuidelineOption\_SetId(ArkUI\_GuidelineOption\* guideline, const char\* value, int32\_t index)

**Description**

Sets the ID of a guideline.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| const char\* value | Pointer to the ID, which must be unique and cannot be the same as the name of any component in the container. |
| int32\_t index | Index of the guideline. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_SetDirection()

void OH\_ArkUI\_GuidelineOption\_SetDirection(ArkUI\_GuidelineOption\* guideline, ArkUI\_Axis value, int32\_t index)

**Description**

Sets the direction of a guideline.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| [ArkUI\_Axis](#arkui_axis) value | Direction. |
| int32\_t index | Index of the guideline. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_SetPositionStart()

void OH\_ArkUI\_GuidelineOption\_SetPositionStart(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)

**Description**

Sets the distance between a guideline and the left or top of the container.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| float value | Distance between a guideline and the left or top edge of the container, in vp. |
| int32\_t index | Index of the guideline. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_SetPositionEnd()

void OH\_ArkUI\_GuidelineOption\_SetPositionEnd(ArkUI\_GuidelineOption\* guideline, float value, int32\_t index)

**Description**

Sets the distance between a guideline and the right or bottom of the container.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| float value | Distance between a guideline and the right or bottom edge of the container, in vp. |
| int32\_t index | Index of the guideline. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_GetId()

const char\* OH\_ArkUI\_GuidelineOption\_GetId(ArkUI\_GuidelineOption\* guideline, int32\_t index)

**Description**

Obtains the ID of a guideline.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| int32\_t index | Index of the guideline. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the guideline. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_GetDirection()

ArkUI\_Axis OH\_ArkUI\_GuidelineOption\_GetDirection(ArkUI\_GuidelineOption\* guideline, int32\_t index)

**Description**

Obtains the direction of a guideline.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| int32\_t index | Index of the guideline. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_Axis](#arkui_axis) | Direction. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_GetPositionStart()

float OH\_ArkUI\_GuidelineOption\_GetPositionStart(ArkUI\_GuidelineOption\* guideline, int32\_t index)

**Description**

Obtains the distance between the guideline and the left or top of the container.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| int32\_t index | Index of the guideline. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between the guideline and the left or top of the container. The unit is vp. |

#### \[h2\]OH\_ArkUI\_GuidelineOption\_GetPositionEnd()

float OH\_ArkUI\_GuidelineOption\_GetPositionEnd(ArkUI\_GuidelineOption\* guideline, int32\_t index)

**Description**

Obtains the distance between the guideline and the right or bottom of the container.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GuidelineOption](../../structs/arkui-guidelineoption/document.md)\* guideline | Pointer to a guideline configuration. |
| int32\_t index | Index of the guideline. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between the guideline and the right or bottom of the container. The unit is vp. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_Create()

ArkUI\_BarrierOption\* OH\_ArkUI\_BarrierOption\_Create(int32\_t size)

**Description**

Creates a barrier configuration for this **RelativeContainer** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t size | Number of barriers. The value range is \[0, +∞). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* | Pointer to the barrier configuration. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_Dispose()

void OH\_ArkUI\_BarrierOption\_Dispose(ArkUI\_BarrierOption\* barrierStyle)

**Description**

Disposes of a barrier configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_SetId()

void OH\_ArkUI\_BarrierOption\_SetId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)

**Description**

Sets the ID of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| const char\* value | Pointer to the ID, which must be unique and cannot be the same as the name of any component in the container. |
| int32\_t index | Index of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_SetDirection()

void OH\_ArkUI\_BarrierOption\_SetDirection(ArkUI\_BarrierOption\* barrierStyle, ArkUI\_BarrierDirection value, int32\_t index)

**Description**

Sets the direction of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| [ArkUI\_BarrierDirection](#arkui_barrierdirection) value | Direction. |
| int32\_t index | Index of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_SetReferencedId()

void OH\_ArkUI\_BarrierOption\_SetReferencedId(ArkUI\_BarrierOption\* barrierStyle, const char\* value, int32\_t index)

**Description**

Sets the referenced components of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| const char\* value | Pointer to the referenced component IDs. |
| int32\_t index | Index of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_GetId()

const char\* OH\_ArkUI\_BarrierOption\_GetId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)

**Description**

Obtains the ID of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| int32\_t index | Index of the barrier. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_GetDirection()

ArkUI\_BarrierDirection OH\_ArkUI\_BarrierOption\_GetDirection(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)

**Description**

Obtains the direction of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| int32\_t index | Index of the barrier. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_BarrierDirection](#arkui_barrierdirection) | Direction of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_GetReferencedId()

const char\* OH\_ArkUI\_BarrierOption\_GetReferencedId(ArkUI\_BarrierOption\* barrierStyle, int32\_t index , int32\_t referencedIndex)

**Description**

Obtains the referenced components of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| int32\_t index | Index of the barrier. |
| int32\_t referencedIndex | Index of the referenced component ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the referenced components of the barrier. |

#### \[h2\]OH\_ArkUI\_BarrierOption\_GetReferencedIdSize()

int32\_t OH\_ArkUI\_BarrierOption\_GetReferencedIdSize(ArkUI\_BarrierOption\* barrierStyle, int32\_t index)

**Description**

Obtains the number of referenced components of a barrier.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_BarrierOption](../../structs/arkui-barrieroption/document.md)\* barrierStyle | Pointer to the barrier configuration. |
| int32\_t index | Index of the barrier. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of referenced components of the barrier. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_Create()

ArkUI\_AlignmentRuleOption\* OH\_ArkUI\_AlignmentRuleOption\_Create()

**Description**

Creates an alignment rule configuration for this **RelativeContainer** component.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* | Pointer to the alignment rule information. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_Dispose()

void OH\_ArkUI\_AlignmentRuleOption\_Dispose(ArkUI\_AlignmentRuleOption\* option)

**Description**

Disposes of an alignment rule configuration of this **RelativeContainer** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetStart()

void OH\_ArkUI\_AlignmentRuleOption\_SetStart(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)

**Description**

Sets the left alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetEnd()

void OH\_ArkUI\_AlignmentRuleOption\_SetEnd(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)

**Description**

Sets the right alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal()

void OH\_ArkUI\_AlignmentRuleOption\_SetCenterHorizontal(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_HorizontalAlignment alignment)

**Description**

Sets the horizontal center alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetTop()

void OH\_ArkUI\_AlignmentRuleOption\_SetTop(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)

**Description**

Sets the top alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetBottom()

void OH\_ArkUI\_AlignmentRuleOption\_SetBottom(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)

**Description**

Sets the bottom alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical()

void OH\_ArkUI\_AlignmentRuleOption\_SetCenterVertical(ArkUI\_AlignmentRuleOption\* option, const char\* id, ArkUI\_VerticalAlignment alignment)

**Description**

Sets the vertical center alignment mode of a relative layout.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| const char\* id | Pointer to the ID of the component that functions as the anchor point. |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) alignment | Alignment mode relative to the anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal()

void OH\_ArkUI\_AlignmentRuleOption\_SetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option, float horizontal)

**Description**

Sets the bias value of the component in the horizontal direction under the anchor constraints.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| float horizontal | Bias value in the horizontal direction. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical()

void OH\_ArkUI\_AlignmentRuleOption\_SetBiasVertical(ArkUI\_AlignmentRuleOption\* option, float vertical)

**Description**

Sets the bias value of the component in the vertical direction under the anchor constraints.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |
| float vertical | Bias value in the vertical direction. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetStartId()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetStartId(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the left alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the left alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment()

ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetStartAlignment(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the left alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) | Alignment mode in left alignment parameters. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetEndId()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetEndId(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the right alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the right alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment()

ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetEndAlignment(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the right alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) | Right alignment mode. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdHorizontal(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the horizontal center alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the horizontal center alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal()

ArkUI\_HorizontalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentHorizontal(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the horizontal center alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_HorizontalAlignment](#arkui_horizontalalignment) | Horizontal center alignment mode. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetTopId()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetTopId(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the top alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the top alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment()

ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetTopAlignment(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the top alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) | Top alignment mode. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetBottomId()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetBottomId(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the bottom alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the bottom alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment()

ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetBottomAlignment(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the bottom alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) | Bottom alignment mode. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical()

const char\* OH\_ArkUI\_AlignmentRuleOption\_GetCenterIdVertical(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the vertical center alignment mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the ID of the vertical center alignment anchor component. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical()

ArkUI\_VerticalAlignment OH\_ArkUI\_AlignmentRuleOption\_GetCenterAlignmentVertical(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the ID of the vertical center alignment anchor component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_VerticalAlignment](#arkui_verticalalignment) | Vertical center alignment mode. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal()

float OH\_ArkUI\_AlignmentRuleOption\_GetBiasHorizontal(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the bias value in the horizontal direction.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Bias value in the horizontal direction. |

#### \[h2\]OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical()

float OH\_ArkUI\_AlignmentRuleOption\_GetBiasVertical(ArkUI\_AlignmentRuleOption\* option)

**Description**

Obtains the bias value in the vertical direction.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AlignmentRuleOption](../../structs/arkui-alignmentruleoption/document.md)\* option | Pointer to an alignment rule configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Bias value in the vertical direction. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_Create()

ArkUI\_SwiperIndicator\* OH\_ArkUI\_SwiperIndicator\_Create(ArkUI\_SwiperIndicatorType type)

**Description**

Creates a navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicatorType](#arkui_swiperindicatortype) type | Type of the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* | Pointer to the navigation indicator. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_Dispose()

void OH\_ArkUI\_SwiperIndicator\_Dispose(ArkUI\_SwiperIndicator\* indicator)

**Description**

Disposes of the navigation indicator of this **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetStartPosition()

void OH\_ArkUI\_SwiperIndicator\_SetStartPosition(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the distance between the navigation point and the left edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Distance between the navigation indicator and the left edge of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetStartPosition()

float OH\_ArkUI\_SwiperIndicator\_GetStartPosition(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the distance between the navigation point and the left edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between the navigation indicator and the left edge of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetTopPosition()

void OH\_ArkUI\_SwiperIndicator\_SetTopPosition(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the distance between the navigation point and the top edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Distance between a navigation indicator and the top edge of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetTopPosition()

float OH\_ArkUI\_SwiperIndicator\_GetTopPosition(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the distance between the navigation point and the top edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between a navigation indicator and the top edge of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetEndPosition()

void OH\_ArkUI\_SwiperIndicator\_SetEndPosition(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the distance between the navigation point and the right edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Distance between the navigation indicator and the right edge of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetEndPosition()

float OH\_ArkUI\_SwiperIndicator\_GetEndPosition(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the distance between the navigation point and the right edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between the navigation indicator and the right edge of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetBottomPosition()

void OH\_ArkUI\_SwiperIndicator\_SetBottomPosition(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the distance between the navigation point and the bottom edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Distance between a navigation indicator and the bottom edge of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetBottomPosition()

float OH\_ArkUI\_SwiperIndicator\_GetBottomPosition(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the distance between the navigation point and the bottom edge of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance between a navigation indicator and the bottom edge of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom()

void OH\_ArkUI\_SwiperIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator, int32\_t ignoreSize)

**Description**

Sets whether the **OH\_ArkUI\_SwiperIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| int32\_t ignoreSize | Whether to ignore the indicator size when positioning the indicator. The value **1** means to ignore the indicator size when positioning the indicator, and **0** means the opposite. Default value: **0**. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom()

int32\_t OH\_ArkUI\_SwiperIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperIndicator\* indicator)

**Description**

Checks whether the **OH\_ArkUI\_SwiperIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Whether to ignore the indicator size when positioning the indicator. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetItemWidth()

void OH\_ArkUI\_SwiperIndicator\_SetItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the width of a dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Width of the dot-style navigation indicator. Default value: **12**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetItemWidth()

float OH\_ArkUI\_SwiperIndicator\_GetItemWidth(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the width of a dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Width of the dot-style navigation indicator. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetItemHeight()

void OH\_ArkUI\_SwiperIndicator\_SetItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the height of a dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Height of the dot-style navigation indicator. Default value: **6**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetItemHeight()

float OH\_ArkUI\_SwiperIndicator\_GetItemHeight(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the height of a dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Height of the dot-style navigation indicator. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth()

void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the width of the selected dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Width of the dot-style navigation indicator. Default value: **12**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth()

float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemWidth(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the width of the selected dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Width of the dot-style navigation indicator. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight()

void OH\_ArkUI\_SwiperIndicator\_SetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator, float value)

**Description**

Sets the height of the selected dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float value | Height of the dot-style navigation indicator. Default value: **6**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight()

float OH\_ArkUI\_SwiperIndicator\_GetSelectedItemHeight(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the height of the selected dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Height of the dot-style navigation indicator. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetMask()

void OH\_ArkUI\_SwiperIndicator\_SetMask(ArkUI\_SwiperIndicator\* indicator, int32\_t mask)

**Description**

Sets whether to enable the mask for a dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| int32\_t mask | 
Whether to enable the mask. The value **1** means to enable, and **0** means the opposite.

Default value: **0**

 |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetMask()

int32\_t OH\_ArkUI\_SwiperIndicator\_GetMask(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains whether the mask is enabled for a dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | The value **1** indicates that the mask is enabled; the value **0** indicates that the mask is disabled. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetColor()

void OH\_ArkUI\_SwiperIndicator\_SetColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t color)

**Description**

Sets the color of a dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| uint32\_t color | 
Color, in 0xARGB format. For example, **0xFFFF0000** indicates red.

Default value: **'#1A182431'** (light gray)

 |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetColor()

uint32\_t OH\_ArkUI\_SwiperIndicator\_GetColor(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the color of a dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Color, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetSelectedColor()

void OH\_ArkUI\_SwiperIndicator\_SetSelectedColor(ArkUI\_SwiperIndicator\* indicator, uint32\_t selectedColor)

**Description**

Sets the color of the selected dot-style navigation indicator for the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| uint32\_t selectedColor | 
Color, in 0xARGB format. For example, **0xFFFF0000** indicates red.

Default value: **'#007DFF'** (blue)

 |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetSelectedColor()

uint32\_t OH\_ArkUI\_SwiperIndicator\_GetSelectedColor(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the color of the selected dot-style navigation indicator of the **Swiper** component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Color, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount()

int32\_t OH\_ArkUI\_SwiperIndicator\_SetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator, int32\_t maxDisplayCount)

**Description**

Sets the maximum number of dots for the dot-style navigation indicator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| int32\_t maxDisplayCount | Maximum number of navigation points. Value range: \[6, 9\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if **maxDisplayCount** is set to an invalid value.

 |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount()

int32\_t OH\_ArkUI\_SwiperIndicator\_GetMaxDisplayCount(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the maximum number of dots for the dot-style navigation indicator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Maximum number of navigation points. Value range: \[6, 9\]. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_Create()

ArkUI\_SwiperDigitIndicator \*OH\_ArkUI\_SwiperDigitIndicator\_Create()

**Description**

Creates a digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md) \* | Pointer to the digit-style navigation indicator. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_Destroy()

void OH\_ArkUI\_SwiperDigitIndicator\_Destroy(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Disposes of the digit-style navigation indicator of this **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition()

void OH\_ArkUI\_SwiperDigitIndicator\_SetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)

**Description**

Sets the distance between the digit-style navigation indicator and the left edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float value | 
Distance between the digit-style navigation indicator and the left edge of the **Swiper** component. For left-to-right scripts, set the distance between the digit-style navigation indicator and the left edge of the **Swiper** component. For right-to-left scripts, set the distance between the digit-style navigation indicator and the right side of the **Swiper** component.

Default value: **0**

Unit: vp

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition()

float OH\_ArkUI\_SwiperDigitIndicator\_GetStartPosition(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the distance between the digit-style navigation indicator and the left edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Distance between the digit-style navigation indicator and the left edge of the **Swiper** component. For left-to-right scripts, the distance between the digit-style navigation indicator and the left edge of the **Swiper** component is returned. For right-to-left scripts, the distance between the digit-style navigation indicator and the right side of the **Swiper** component is returned.

Unit: vp

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition()

void OH\_ArkUI\_SwiperDigitIndicator\_SetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)

**Description**

Sets the distance from the digit-style navigation indicator to the top edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float value | Distance from the digit-style navigation indicator to the top of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition()

float OH\_ArkUI\_SwiperDigitIndicator\_GetTopPosition(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the distance from the digit-style navigation indicator to the top edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance from the digit-style navigation indicator to the top of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition()

void OH\_ArkUI\_SwiperDigitIndicator\_SetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)

**Description**

Sets the distance between the digit-style navigation indicator and the right edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float value | 
Distance between the digit-style navigation indicator and the right edge of the **Swiper** component. For left-to-right scripts, set the distance between the digit-style navigation indicator and the right edge of the **Swiper** component. For right-to-left scripts, set the digit-style navigation indicator and the left edge of the **Swiper** component.

Default value: **0**

Unit: vp

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition()

float OH\_ArkUI\_SwiperDigitIndicator\_GetEndPosition(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the distance between the digit-style navigation indicator and the right edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Distance between the digit-style navigation indicator and the right edge of the **Swiper** component. For left-to-right scripts, the distance between the digit-style navigation indicator and the right edge of the **Swiper** component is returned. For right-to-left scripts, the digit-style navigation indicator and the left edge of the **Swiper** component is returned.

Unit: vp

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition()

void OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator, float value)

**Description**

Sets the distance from the digit-style navigation indicator to the bottom edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float value | Distance from the digit-style navigation indicator to the bottom of the **Swiper** component. Default value: **0**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition()

float OH\_ArkUI\_SwiperDigitIndicator\_GetBottomPosition(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the distance from the digit-style navigation indicator to the bottom edge of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Distance from the digit-style navigation indicator to the bottom of the **Swiper** component. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor()

void OH\_ArkUI\_SwiperDigitIndicator\_SetFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t color)

**Description**

Sets the font color of the digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| uint32\_t color | Color, in 0xARGB format. For example, **0xFFFF0000** indicates red. Default value: **0xFF182431**. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor()

uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetFontColor(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font color of the digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Color, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor()

void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator, uint32\_t selectedColor)

**Description**

Sets the font color of the selected digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| uint32\_t selectedColor | Color, in 0xARGB format. For example, **0xFFFF0000** indicates red. Default value: **0xFF182431**. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor()

uint32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontColor(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font color of the selected digit-style navigation indicator of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Color, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize()

void OH\_ArkUI\_SwiperDigitIndicator\_SetFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)

**Description**

Sets the font size of the digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float size | 
Font size, in fp.

Default value: **14**

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize()

float OH\_ArkUI\_SwiperDigitIndicator\_GetFontSize(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font size of the digit-style navigation indicator of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Font size, in fp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize()

void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator, float size)

**Description**

Sets the font size of the selected digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |
| float size | 
Font size, in fp.

Default value: **14**

 |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize()

float OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontSize(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font size of the selected digit-style navigation indicator of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Font size, in fp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetFontWeight()

void OH\_ArkUI\_SwiperDigitIndicator\_SetFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight fontWeight)

**Description**

Sets the font weight of the digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md) \*indicator | Pointer to the digit-style navigation indicator. |
| [ArkUI\_FontWeight](#arkui_fontweight) fontWeight | Font weight, specified using [ArkUI\_FontWeight](#arkui_fontweight). |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetFontWeight()

ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font weight of the digit-style navigation indicator of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_FontWeight](#arkui_fontweight) | Font weight, specified using [ArkUI\_FontWeight](#arkui_fontweight). |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontWeight()

void OH\_ArkUI\_SwiperDigitIndicator\_SetSelectedFontWeight(ArkUI\_SwiperDigitIndicator \*indicator, ArkUI\_FontWeight selectedFontWeight)

**Description**

Sets the font weight of the selected digit-style navigation indicator for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md) \*indicator | Pointer to the digit-style navigation indicator. |
| [ArkUI\_FontWeight](#arkui_fontweight) selectedFontWeight | Font weight, specified using [ArkUI\_FontWeight](#arkui_fontweight). |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontWeight()

ArkUI\_FontWeight OH\_ArkUI\_SwiperDigitIndicator\_GetSelectedFontWeight(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Obtains the font weight of the selected digit-style navigation indicator of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the digit-style navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_FontWeight](#arkui_fontweight) | Font weight, specified using [ArkUI\_FontWeight](#arkui_fontweight). |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_Create()

ArkUI\_SwiperArrowStyle \*OH\_ArkUI\_SwiperArrowStyle\_Create()

**Description**

Creates a navigation arrow for the **Swiper** component.

**Since**: 19

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md) \* | Pointer to the arrow object. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_Destroy()

void OH\_ArkUI\_SwiperArrowStyle\_Destroy(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Destroys the navigation arrow pointer of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground()

void OH\_ArkUI\_SwiperArrowStyle\_SetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showBackground)

**Description**

Sets whether to display the background of the navigation arrow for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| int32\_t showBackground | Whether to show the arrow background. The value **1** means to show the background, and **0** means the opposite. The default value is **0**. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground()

int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowBackground(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Checks whether the background of the navigation arrow is displayed for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Whether the arrow background is displayed. The value **1** means that the background is displayed, and **0** means the opposite. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle()

void OH\_ArkUI\_SwiperArrowStyle\_SetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle, int32\_t showSidebarMiddle)

**Description**

Sets the position of the navigation arrow for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| int32\_t showSidebarMiddle | Position of the arrow. **0**: The arrow is displayed on both sides of the navigation indicator. **1**: The arrow is displayed on both sides of the **Swiper** component. The default value is **0**. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle()

int32\_t OH\_ArkUI\_SwiperArrowStyle\_GetShowSidebarMiddle(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Obtains the position of the navigation arrow for the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Position of the arrow. **0**: The arrow is displayed on both sides of the navigation indicator. **1**: The arrow is displayed on both sides of the **Swiper** component. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize()

void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float backgroundSize)

**Description**

Sets the background size for the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| float backgroundSize | Background size of the arrow, in vp. Default value: 24 vp when displayed on both sides of the navigation indicator and 32 vp when displayed on both sides of the **Swiper** component. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize()

float OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundSize(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Obtains the background size of the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Background size of the arrow, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor()

void OH\_ArkUI\_SwiperArrowStyle\_SetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t backgroundColor)

**Description**

Sets the background color for the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| uint32\_t backgroundColor | Background color of the arrow, in 0xARGB format. For example, 0xFFFF0000 indicates red. Default value: **0x00000000** when displayed on both sides of the navigation indicator and **0x19182431** when displayed on both sides of the **Swiper** component. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor()

uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetBackgroundColor(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Obtains the background color of the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Background color of the arrow, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize()

void OH\_ArkUI\_SwiperArrowStyle\_SetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle, float arrowSize)

**Description**

Sets the size for the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| float arrowSize | 
Size of the arrow, in vp.

Default value: 18 vp when displayed on both sides of the navigation indicator and 24 vp when displayed on both sides of the **Swiper** component. When the navigation arrow background is displayed, the value of **arrowSize** is fixed at 3/4 of the value of [backgroundSize](#oh_arkui_swiperarrowstyle_setbackgroundsize).

 |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize()

float OH\_ArkUI\_SwiperArrowStyle\_GetArrowSize(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Obtains the size of the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Size of the arrow, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor()

void OH\_ArkUI\_SwiperArrowStyle\_SetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle, uint32\_t arrowColor)

**Description**

Sets the color for the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |
| uint32\_t arrowColor | 
Color of the navigation arrow, in 0xARGB format. For example, **0xFFFF0000** indicates red.

Default value: **'#182431'** (dark blue)

 |

#### \[h2\]OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor()

uint32\_t OH\_ArkUI\_SwiperArrowStyle\_GetArrowColor(ArkUI\_SwiperArrowStyle\* arrowStyle)

**Description**

Obtains the color of the navigation arrow of the **Swiper** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperArrowStyle](../../structs/arkui-swiperarrowstyle/document.md)\* arrowStyle | Pointer to the arrow object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Color of the arrow, in 0xARGB format. For example, 0xFFFF0000 indicates red. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_SetSpace()

void OH\_ArkUI\_SwiperIndicator\_SetSpace(ArkUI\_SwiperIndicator\* indicator, float space)

**Description**

Sets the spacing between navigation points.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| float space | Spacing between navigation points. Default value: **8**, in vp. |

#### \[h2\]OH\_ArkUI\_SwiperIndicator\_GetSpace()

float OH\_ArkUI\_SwiperIndicator\_GetSpace(ArkUI\_SwiperIndicator\* indicator)

**Description**

Obtains the spacing between navigation points.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperIndicator](../../structs/arkui-swiperindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Spacing between navigation points. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom()

void OH\_ArkUI\_SwiperDigitIndicator\_SetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator, int32\_t ignoreSize)

**Description**

Sets whether the **OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the navigation indicator. |
| int32\_t ignoreSize | Whether to ignore the indicator size when positioning the indicator. The value **1** means to ignore the indicator size when positioning the indicator, and **0** means the opposite. Default value: **0**. |

#### \[h2\]OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom()

int32\_t OH\_ArkUI\_SwiperDigitIndicator\_GetIgnoreSizeOfBottom(ArkUI\_SwiperDigitIndicator\* indicator)

**Description**

Checks whether the **OH\_ArkUI\_SwiperDigitIndicator\_SetBottomPosition** API ignores the indicator size when positioning the indicator.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SwiperDigitIndicator](../../structs/arkui-swiperdigitindicator/document.md)\* indicator | Pointer to the navigation indicator. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | The value **1** indicates that the navigation indicator size is ignored, and the value **0** indicates that the navigation indicator size is not ignored. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_Create()

ArkUI\_ListItemSwipeActionItem\* OH\_ArkUI\_ListItemSwipeActionItem\_Create()

**Description**

Creates a **ListItemSwipeActionItem** instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* | Pointer to the **ListItemSwipeActionItem** instance. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_Dispose()

void OH\_ArkUI\_ListItemSwipeActionItem\_Dispose(ArkUI\_ListItemSwipeActionItem\* item)

**Description**

Disposes of a **ListItemSwipeActionItem** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance to dispose of. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetContent()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetContent(ArkUI\_ListItemSwipeActionItem\* item, ArkUI\_NodeHandle node)

**Description**

Sets the layout content for a **ListItemSwipeActionItem** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Layout information. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item, float distance)

**Description**

Sets the swipe distance threshold for deleting the list item.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| float distance | Swipe distance threshold for deleting the list item, in vp. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance()

float OH\_ArkUI\_ListItemSwipeActionItem\_GetActionAreaDistance(ArkUI\_ListItemSwipeActionItem\* item)

**Description**

Obtains the swipe distance threshold for deleting the list item.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Swipe distance threshold for deleting the list item, in vp. The value **0** is returned if an exception occurs. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())

**Description**

Sets the callback invoked each time the list item enters the delete area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnEnterActionAreaWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))

**Description**

Sets the callback invoked each time the list item enters the delete area. User-defined data will be passed to the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| void\* userData | Pointer to the user-defined data. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnAction(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())

**Description**

Sets the callback invoked when the [list item](../../../arkts-components/scroll-and-swipe/listitem/document.md) is deleted while in the delete area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnActionWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))

**Description**

Sets the callback invoked when the list item is deleted while in the delete area. User-defined data will be passed to the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| void\* userData | Pointer to the user-defined data. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionArea(ArkUI\_ListItemSwipeActionItem\* item, void (\*callback)())

**Description**

Sets the callback invoked each time the list item exits the delete area.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnExitActionAreaWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(void\* userData))

**Description**

Sets the callback invoked each time the list item exits the delete area. User-defined data will be passed to the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| void\* userData | Pointer to the user-defined data. |
| callback | Callback event. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChange(ArkUI\_ListItemSwipeActionItem\* item,void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState))

**Description**

Sets the callback invoked when the swipe state of the list item changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| callback | Callback event. The input parameter is **swipeActionState**, indicating the swipe state of the list item. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData()

void OH\_ArkUI\_ListItemSwipeActionItem\_SetOnStateChangeWithUserData(ArkUI\_ListItemSwipeActionItem\* item,void\* userData, void (\*callback)(ArkUI\_ListItemSwipeActionState swipeActionState, void\* userData))

**Description**

Sets the callback invoked when the swipe state of the list item changes. User-defined data will be passed to the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the **ListItemSwipeActionItem** instance. |
| void\* userData | Pointer to the user-defined data. |
| callback | Callback event. The input parameter is **swipeActionState**, indicating the swipe state of the list item. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_Create()

ArkUI\_ListItemSwipeActionOption\* OH\_ArkUI\_ListItemSwipeActionOption\_Create()

**Description**

Creates a **ListItemSwipeActionOption** instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* | Pointer to the **ListItemSwipeActionOption** instance. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_Dispose()

void OH\_ArkUI\_ListItemSwipeActionOption\_Dispose(ArkUI\_ListItemSwipeActionOption\* option)

**Description**

Disposes of a **ListItemSwipeActionOption** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionOption** instance to dispose of. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_SetStart()

void OH\_ArkUI\_ListItemSwipeActionOption\_SetStart(ArkUI\_ListItemSwipeActionOption\* option, ArkUI\_ListItemSwipeActionItem\* item)

**Description**

Sets the layout content for the left edge (for a vertical layout) or top edge (for a horizontal layout) of a **ListItemSwipeActionItem** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the layout information. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd()

void OH\_ArkUI\_ListItemSwipeActionOption\_SetEnd(ArkUI\_ListItemSwipeActionOption\* option,ArkUI\_ListItemSwipeActionItem\* item)

**Description**

Sets the layout content for the right edge (for a vertical layout) or bottom edge (for a horizontal layout) of a **ListItemSwipeActionItem** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |
| [ArkUI\_ListItemSwipeActionItem](../../structs/arkui-listitemswipeactionitem/document.md)\* item | Pointer to the layout information. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect()

void OH\_ArkUI\_ListItemSwipeActionOption\_SetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option,ArkUI\_ListItemSwipeEdgeEffect edgeEffect)

**Description**

Sets the effect used when the scroll boundary is reached.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |
| [ArkUI\_ListItemSwipeEdgeEffect](#arkui_listitemswipeedgeeffect) edgeEffect | Effect used when the boundary of the scrolling area is reached. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect()

int32\_t OH\_ArkUI\_ListItemSwipeActionOption\_GetEdgeEffect(ArkUI\_ListItemSwipeActionOption\* option)

**Description**

Obtains the effect used when the scroll boundary is reached.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Effect used when the boundary of the scrolling area is reached. The default return value is [ARKUI\_LIST\_ITEM\_SWIPE\_EDGE\_EFFECT\_SPRING](#arkui_listitemswipeedgeeffect). |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange()

void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChange(ArkUI\_ListItemSwipeActionOption\* option,void (\*callback)(float offset))

**Description**

Sets the callback invoked when the scroll offset changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |
| callback | Callback event. **offset**: scroll offset, in vp. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData()

void OH\_ArkUI\_ListItemSwipeActionOption\_SetOnOffsetChangeWithUserData(ArkUI\_ListItemSwipeActionOption\* option,void\* userData, void (\*callback)(float offset, void\* userData))

**Description**

Sets the callback invoked when the scroll offset changes. User-defined data will be passed to the callback event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListItemSwipeActionOption](../../structs/arkui-listitemswipeactionoption/document.md)\* option | Pointer to the **ListItemSwipeActionItem** instance. |
| void\* userData | Pointer to the user-defined data. |
| callback | Callback event. **offset**: scroll offset, in vp. |

#### \[h2\]OH\_ArkUI\_ListItemSwipeAction\_Expand()

int32\_t OH\_ArkUI\_ListItemSwipeAction\_Expand(ArkUI\_NodeHandle node, ArkUI\_ListItemSwipeActionDirection direction)

**Description**

Expands the swipe action menu for the specified list item.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | **ListItem** node object. |
| [ArkUI\_ListItemSwipeActionDirection](#arkui_listitemswipeactiondirection) direction | Swipe action menu display direction for the **ListItem** component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](#arkui_errorcode) if the node object type is incorrect.

Returns [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](#arkui_errorcode) if the passed node is not mounted to the component tree when the API is called.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/pqyKqc53QMOX-LHwmN4y9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062303Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E8C81513A66D221DD204B16672D7E3AF3AF98DA715DCECC5469CC5BA15A8B2C)

-   If the **List** component's **NODE\_LIST\_CACHED\_COUNT** attribute is configured to preload **ListItem** child components, swipe action menus can be expanded for preloaded **ListItem** child components outside the visible area. Otherwise, child components outside the visible area cannot be expanded.

#### \[h2\]OH\_ArkUI\_ListItemSwipeAction\_Collapse()

int32\_t OH\_ArkUI\_ListItemSwipeAction\_Collapse(ArkUI\_NodeHandle node)

**Description**

Collapses the swipe action menu for the specified list item.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | **ListItem** node object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](#arkui_errorcode) if the node object type is incorrect.

Returns [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](#arkui_errorcode) if the passed node is not mounted to the component tree when the API is called.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_Create()

ArkUI\_AccessibilityState\* OH\_ArkUI\_AccessibilityState\_Create(void)

**Description**

Creates an accessibility state.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* | Pointer to the created accessibility state object. If a null pointer is returned, the creation fails. A possible cause is that the application address space is full. |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_Dispose()

void OH\_ArkUI\_AccessibilityState\_Dispose(ArkUI\_AccessibilityState\* state)

**Description**

Disposes of the pointer to an accessibility state.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_SetDisabled()

void OH\_ArkUI\_AccessibilityState\_SetDisabled(ArkUI\_AccessibilityState\* state, int32\_t isDisabled)

**Description**

Sets whether an accessibility state is disabled.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |
| int32\_t isDisabled | Whether the accessibility state is disabled. The value **1** means that the accessibility state is disabled, and **0** means the opposite. The default value is **0**. |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_IsDisabled()

int32\_t OH\_ArkUI\_AccessibilityState\_IsDisabled(ArkUI\_AccessibilityState\* state)

**Description**

Obtains whether an accessibility state is disabled.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Whether the accessibility state is disabled. The value **1** means that the accessibility state is disabled, and **0** means the opposite. The default value is **0**.

If the value of **state** is null, the default value is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_SetSelected()

void OH\_ArkUI\_AccessibilityState\_SetSelected(ArkUI\_AccessibilityState\* state, int32\_t isSelected)

**Description**

Sets whether an accessibility state is selected.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |
| int32\_t isSelected | Whether the accessibility state is selected. The value **1** means that the accessibility state is selected, and **0** means the opposite. The default value is **0**. |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_IsSelected()

int32\_t OH\_ArkUI\_AccessibilityState\_IsSelected(ArkUI\_AccessibilityState\* state)

**Description**

Obtains whether an accessibility state is selected.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Whether the accessibility state is selected. The value **1** means that the accessibility state is selected, and **0** means the opposite. The default value is **0**.

If the value of **state** is null, the default value is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_SetCheckedState()

void OH\_ArkUI\_AccessibilityState\_SetCheckedState(ArkUI\_AccessibilityState\* state, int32\_t checkedState)

**Description**

Sets the check box state of an accessibility state.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |
| int32\_t checkedState | Check box status. The parameter type is [ArkUI\_AccessibilityCheckedState](#arkui_accessibilitycheckedstate). The default value is **ARKUI\_ACCESSIBILITY\_UNCHECKED**. |

#### \[h2\]OH\_ArkUI\_AccessibilityState\_GetCheckedState()

int32\_t OH\_ArkUI\_AccessibilityState\_GetCheckedState(ArkUI\_AccessibilityState\* state)

**Description**

Obtains the check box state of an accessibility state.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityState](../../structs/arkui-accessibilitystate/document.md)\* state | Pointer to the created accessibility state object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Check box status. The parameter type is [ArkUI\_AccessibilityCheckedState](#arkui_accessibilitycheckedstate). The default value is **ARKUI\_ACCESSIBILITY\_UNCHECKED**.

If a parameter error occurs, the default value is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_Create()

ArkUI\_AccessibilityValue\* OH\_ArkUI\_AccessibilityValue\_Create(void)

**Description**

Creates an **AccessibilityValue** instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* | Pointer to the created **AccessibilityValue** instance. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_Dispose()

void OH\_ArkUI\_AccessibilityValue\_Dispose(ArkUI\_AccessibilityValue\* value)

**Description**

Disposes of the pointer to an **AccessibilityValue** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetMin()

void OH\_ArkUI\_AccessibilityValue\_SetMin(ArkUI\_AccessibilityValue\* value, int32\_t min)

**Description**

Sets the minimum accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |
| int32\_t min | Minimum value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetMin()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetMin(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the minimum accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Minimum value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetMax()

void OH\_ArkUI\_AccessibilityValue\_SetMax(ArkUI\_AccessibilityValue\* value, int32\_t max)

**Description**

Sets the maximum accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |
| int32\_t max | Maximum value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetMax()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetMax(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the maximum accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Maximum value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetCurrent()

void OH\_ArkUI\_AccessibilityValue\_SetCurrent(ArkUI\_AccessibilityValue\* value, int32\_t current)

**Description**

Sets the current accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |
| int32\_t current | Current value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetCurrent()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetCurrent(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the current accessibility value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Current value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetRangeMin()

void OH\_ArkUI\_AccessibilityValue\_SetRangeMin(ArkUI\_AccessibilityValue\* value, int32\_t rangeMin)

**Description**

Sets the minimum value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to set the minimum value. |
| int32\_t rangeMin | Minimum value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetRangeMin()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMin(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the minimum value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to obtain the minimum value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Minimum value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetRangeMax()

void OH\_ArkUI\_AccessibilityValue\_SetRangeMax(ArkUI\_AccessibilityValue\* value, int32\_t rangeMax)

**Description**

Sets the maximum value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to set the maximum value. |
| int32\_t rangeMax | Maximum value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetRangeMax()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeMax(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the maximum value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to obtain the minimum value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Maximum value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetRangeCurrent()

void OH\_ArkUI\_AccessibilityValue\_SetRangeCurrent(ArkUI\_AccessibilityValue\* value, int32\_t rangeCurrent)

**Description**

Sets the current value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to set the current value. |
| int32\_t rangeCurrent | Current value for the range-based component. The default value is **\-1**. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetRangeCurrent()

int32\_t OH\_ArkUI\_AccessibilityValue\_GetRangeCurrent(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the current value for accessibility information of the range-based component.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the accessibility information object of the range-based component for which you want to obtain the current value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Current value for the range-based component. The default value is **\-1**.

If a parameter error occurs, **\-1** is returned.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_SetText()

void OH\_ArkUI\_AccessibilityValue\_SetText(ArkUI\_AccessibilityValue\* value, const char\* text)

**Description**

Sets the text description of an **AccessibilityValue** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |
| const char\* text | Pointer to the text description. The default value is an empty string. |

#### \[h2\]OH\_ArkUI\_AccessibilityValue\_GetText()

const char\* OH\_ArkUI\_AccessibilityValue\_GetText(ArkUI\_AccessibilityValue\* value)

**Description**

Obtains the text description of an **AccessibilityValue** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityValue](../../structs/arkui-accessibilityvalue/document.md)\* value | Pointer to the created **AccessibilityValue** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | 
Pointer to the text description. The default value is an empty string.

If a parameter error occurs, a null pointer is returned.

 |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString()

ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString(char\* src)

**Description**

Creates an image frame information object based on an image path, with the image format being SVG, PNG, or JPG. Both relative and absolute paths in the application sandbox are supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* src | Pointer to the image path, which can be a relative or absolute path in the application sandbox. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* | Pointer to the image frame information object. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor()

ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor(ArkUI\_DrawableDescriptor\* drawable)

**Description**

Creates an image frame information object using an [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawable | Pointer to the **ArkUI\_DrawableDescriptor** object created using a PixelMap. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* | Pointer to the image frame information object. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Disposes of the pointer to an image frame information object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t width)

**Description**

Sets the image width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |
| int32\_t width | Image width, in px. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth()

int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Obtains the image width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Image width, in PX. If **imageInfo** is a null pointer, **0** is returned. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t height)

**Description**

Sets the image height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |
| int32\_t height | Image height, in px. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight()

int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Obtains the image height.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Image height, in PX. If **imageInfo** is a null pointer, **0** is returned. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t top)

**Description**

Sets the vertical coordinate of an image relative to the upper left corner of the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |
| int32\_t top | Vertical coordinate of the image relative to the upper left corner of the component, in px. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop()

int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Obtains the vertical coordinate of an image relative to the upper left corner of the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Vertical coordinate of the image relative to the upper left corner of the component, in px. If **imageInfo** is a null pointer, **0** is returned. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t left)

**Description**

Sets the horizontal coordinate of an image relative to the upper left corner of the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |
| int32\_t left | Horizontal coordinate of the image relative to the upper left corner of the component, in px. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft()

int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Obtains the horizontal coordinate of an image relative to the upper left corner of the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Horizontal coordinate of the image relative to the upper left corner of the component, in px. If **imageInfo** is a null pointer, **0** is returned. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration()

void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t duration)

**Description**

Sets the playback duration of an image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |
| int32\_t duration | Playback duration of an image, in ms. |

#### \[h2\]OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration()

int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)

**Description**

Obtains the playback duration of an image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ImageAnimatorFrameInfo](../../structs/arkui-imageanimatorframeinfo/document.md)\* imageInfo | Pointer to the image frame information object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Playback duration of the image, in milliseconds. If **imageInfo** is a null pointer, **0** is returned. |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_Create()

ArkUI\_ListChildrenMainSize\* OH\_ArkUI\_ListChildrenMainSizeOption\_Create()

**Description**

Creates a **ListChildrenMainSize** instance.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* | Pointer to the created **ListChildrenMainSize** instance. |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose()

void OH\_ArkUI\_ListChildrenMainSizeOption\_Dispose(ArkUI\_ListChildrenMainSize\* option)

**Description**

Disposes of a **ListChildrenMainSize** instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance to dispose of. |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize()

int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_SetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option, float defaultMainSize)

**Description**

Sets the default size of the list item in the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |
| float defaultMainSize | Default size of the list item along the main axis, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize()

float OH\_ArkUI\_ListChildrenMainSizeOption\_GetDefaultMainSize(ArkUI\_ListChildrenMainSize\* option)

**Description**

Obtains the default size of the list item in the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Default size of the list item along the main axis. The default value is **0**. The unit is [vp](../../../arkts-components/common-definitions/basic-types/document.md#vp10). If **option** is a null pointer, **\-1** is returned. |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_Resize()

void OH\_ArkUI\_ListChildrenMainSizeOption\_Resize(ArkUI\_ListChildrenMainSize\* option, int32\_t totalSize)

**Description**

Adjusts the capacity of the children item size array in the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |
| int32\_t totalSize | Capacity of the target array. |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_Splice()

int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_Splice(ArkUI\_ListChildrenMainSize\* option, int32\_t index, int32\_t deleteCount, int32\_t addCount)

**Description**

Adjusts the children item size array in the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |
| int32\_t index | Start index. |
| int32\_t deleteCount | Number of elements to be deleted from the start position. |
| int32\_t addCount | Number of elements to be added from the start position. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize()

int32\_t OH\_ArkUI\_ListChildrenMainSizeOption\_UpdateSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index, float mainSize)

**Description**

Updates the size at the specified index in the children item size array of the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |
| int32\_t index | Array index of the target element. |
| float mainSize | Size of the main axis, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize()

float OH\_ArkUI\_ListChildrenMainSizeOption\_GetMainSize(ArkUI\_ListChildrenMainSize\* option, int32\_t index)

**Description**

Obtains the size at the specified index in the children item size array of the [List](../../../arkts-components/scroll-and-swipe/list/document.md) component along the main axis. The vertical axis indicates the height, and the horizontal axis indicates the width.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ListChildrenMainSize](../../structs/arkui-listchildrenmainsize/document.md)\* option | Pointer to the **ListChildrenMainSize** instance. |
| int32\_t index | Array index of the target element. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Value at the specified index. If a parameter error occurs, **\-1** is returned. |

#### \[h2\]OH\_ArkUI\_CustomSpanMeasureInfo\_Create()

ArkUI\_CustomSpanMeasureInfo\* OH\_ArkUI\_CustomSpanMeasureInfo\_Create(void)

**Description**

Creates measurement information for this custom span.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMeasureInfo](../../structs/arkui-customspanmeasureinfo/document.md)\* | 
Pointer to the **CustomSpanMeasureInfo** instance.

If a null pointer is returned, the memory may be insufficient.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanMeasureInfo\_Dispose()

void OH\_ArkUI\_CustomSpanMeasureInfo\_Dispose(ArkUI\_CustomSpanMeasureInfo\* info)

**Description**

Disposes of measurement information of a custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMeasureInfo](../../structs/arkui-customspanmeasureinfo/document.md)\* info | Pointer to the measurement information of a custom span. |

#### \[h2\]OH\_ArkUI\_CustomSpanMeasureInfo\_GetFontSize()

float OH\_ArkUI\_CustomSpanMeasureInfo\_GetFontSize(ArkUI\_CustomSpanMeasureInfo\* info)

**Description**

Obtains the font size of the parent text node of a custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMeasureInfo](../../structs/arkui-customspanmeasureinfo/document.md)\* info | Pointer to the measurement information of a custom span. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Font size of the parent node text, in fp. If a parameter error occurs, **0.0f** is returned.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanMetrics\_Create()

ArkUI\_CustomSpanMetrics\* OH\_ArkUI\_CustomSpanMetrics\_Create(void)

**Description**

Creates measurement metrics for this custom span.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md)\* | 
Pointer to the **CustomSpanMetrics** instance.

If a null pointer is returned, the memory may be insufficient.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanMetrics\_Dispose()

void OH\_ArkUI\_CustomSpanMetrics\_Dispose(ArkUI\_CustomSpanMetrics\* metrics)

**Description**

Disposes of measurement metrics of this custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md)\* metrics | Pointer to the **CustomSpanMetrics** instance. |

#### \[h2\]OH\_ArkUI\_CustomSpanMetrics\_SetWidth()

int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetWidth(ArkUI\_CustomSpanMetrics\* metrics, float width)

**Description**

Sets the width for a custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md)\* metrics | Pointer to the **CustomSpanMetrics** instance. |
| float width | Width, in vp. The default value is **0.0f**. The negative value has the same effect as the default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanMetrics\_SetHeight()

int32\_t OH\_ArkUI\_CustomSpanMetrics\_SetHeight(ArkUI\_CustomSpanMetrics\* metrics, float height)

**Description**

Sets the height for a custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanMetrics](../../structs/arkui-customspanmetrics/document.md)\* metrics | Pointer to the **CustomSpanMetrics** instance. |
| float height | Height, in vp. The default value is **0.0f**. The negative value has the same effect as the default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_Create()

ArkUI\_CustomSpanDrawInfo\* OH\_ArkUI\_CustomSpanDrawInfo\_Create(void)

**Description**

Creates drawing information for this custom span.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* | 
Pointer to the **CustomSpanDrawInfo** instance.

If a null pointer is returned, the memory may be insufficient.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_Dispose()

void OH\_ArkUI\_CustomSpanDrawInfo\_Dispose(ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Disposes of drawing information for this custom span.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Pointer to the drawing information of a custom span. |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_GetXOffset()

float OH\_ArkUI\_CustomSpanDrawInfo\_GetXOffset(ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Obtains the x-axis offset of the custom span relative to the mounted component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Pointer to the drawing information of a custom span. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
X-axis offset, in px. If a parameter error occurs, **0.0f** is returned.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_GetLineTop()

float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineTop(ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Obtains the top margin of the custom span relative to the mounted component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Pointer to the drawing information of a custom span. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Top margin, in px. If a parameter error occurs, **0.0f** is returned.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_GetLineBottom()

float OH\_ArkUI\_CustomSpanDrawInfo\_GetLineBottom(ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Obtains the bottom margin of the custom span relative to the mounted component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Pointer to the drawing information of a custom span. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Bottom margin, in px. If a parameter error occurs, **0.0f** is returned.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomSpanDrawInfo\_GetBaseline()

float OH\_ArkUI\_CustomSpanDrawInfo\_GetBaseline(ArkUI\_CustomSpanDrawInfo\* info)

**Description**

Obtains the baseline offset of the custom span relative to the mounted component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomSpanDrawInfo](../../structs/arkui-customspandrawinfo/document.md)\* info | Pointer to the drawing information of a custom span. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | 
Baseline offset, in px. If a parameter error occurs, **0.0f** is returned.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CustomProperty\_Destroy()

void OH\_ArkUI\_CustomProperty\_Destroy(ArkUI\_CustomProperty\* handle)

**Description**

Destroys an [ArkUI\_CustomProperty](../../structs/arkui-customproperty/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomProperty](../../structs/arkui-customproperty/document.md)\* handle | Pointer to the instance to be destroyed. |

#### \[h2\]OH\_ArkUI\_CustomProperty\_GetStringValue()

const char\* OH\_ArkUI\_CustomProperty\_GetStringValue(ArkUI\_CustomProperty\* handle)

**Description**

Obtains the value of a custom property object.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomProperty](../../structs/arkui-customproperty/document.md)\* handle | Pointer to the custom property object. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the value of a custom property object. |

#### \[h2\]OH\_ArkUI\_HostWindowInfo\_GetName()

const char\* OH\_ArkUI\_HostWindowInfo\_GetName(ArkUI\_HostWindowInfo\* info)

**Description**

Obtains the window name in an [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md) object.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md)\* info | Pointer to the **HostWindowInfo** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the window name in the [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md) object. |

#### \[h2\]OH\_ArkUI\_HostWindowInfo\_Destroy()

void OH\_ArkUI\_HostWindowInfo\_Destroy(ArkUI\_HostWindowInfo\* info)

**Description**

Destroys an [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md) object.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md)\* info | Pointer to the [ArkUI\_HostWindowInfo](../../structs/arkui-hostwindowinfo/document.md) object to be destroyed. |

#### \[h2\]OH\_ArkUI\_ActiveChildrenInfo\_Destroy()

void OH\_ArkUI\_ActiveChildrenInfo\_Destroy(ArkUI\_ActiveChildrenInfo\* handle)

**Description**

Destroys an [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md)\* handle | Pointer to the [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance to be destroyed. |

#### \[h2\]OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex()

ArkUI\_NodeHandle OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex(ArkUI\_ActiveChildrenInfo\* handle, int32\_t index)

**Description**

Obtains the child node at the specified index in an [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md)\* handle | Pointer to the [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance from which the information is to be obtained. |
| int32\_t index | Index of the target child node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) | Handle to the child node at the specified index, or **nullptr** if an error occurs. |

#### \[h2\]OH\_ArkUI\_ActiveChildrenInfo\_GetCount()

int32\_t OH\_ArkUI\_ActiveChildrenInfo\_GetCount(ArkUI\_ActiveChildrenInfo\* handle)

**Description**

Obtains the number of nodes in an [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md)\* handle | Pointer to the [ArkUI\_ActiveChildrenInfo](../../structs/arkui-activechildreninfo/document.md) instance from which the information is to be obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of child nodes. The default value is **0**. |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_Create()

ArkUI\_ProgressLinearStyleOption\* OH\_ArkUI\_ProgressLinearStyleOption\_Create(void)

**Description**

Creates a **ProgressLinearStyleOption** instance.

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* | 
Pointer to the **ProgressLinearStyleOption** instance created.

If a null pointer is returned, the memory may be insufficient.

 |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_Destroy()

void OH\_ArkUI\_ProgressLinearStyleOption\_Destroy(ArkUI\_ProgressLinearStyleOption\* option)

**Description**

Destroys a **ProgressLinearStyleOption** instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled()

void OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)

**Description**

Sets whether to enable the smooth progress effect.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |
| bool enabled | 
Whether to enable the smooth effect. When this effect is enabled, the progress changes smoothly from the current value to the target value. When this effect is disabled, the progress changes abruptly to the target value.

**true**: The smooth effect is enabled.

**false**: The smooth effect is disabled.

The default value is **true**.

 |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled()

void OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)

**Description**

Sets whether to enable the scan effect.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |
| bool enabled | 
Whether to enable the scan effect.

**true**: The scan effect is enabled.

**false**: The scan effect is disabled.

The default value is **false**.

 |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth()

void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option, float strokeWidth)

**Description**

Sets the width of the progress indicator.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |
| float strokeWidth | Stroke width of the progress indicator, in vp. Percentage values are not supported. The default value is **4.0vp**. |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius()

void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option, float strokeRadius)

**Description**

Sets the corner radius of the progress indicator.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |
| float strokeRadius | Corner radius of the progress indicator, in vp. The value range is \[0, strokeWidth/2\]. Default value: **strokeWidth/2**. |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled()

bool OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)

**Description**

Obtains the enabled status of the smooth progress effect.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether the smooth effect is enabled.

**true**: The smooth effect is enabled.

**false**: The smooth effect is disabled.

The default value is **true**.

 |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled()

bool OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)

**Description**

Obtains the enabled status of the scan effect.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether the scan effect is enabled.

**true**: The scan effect is enabled.

**false**: The scan effect is disabled.

The default value is **false**.

 |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth()

float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option)

**Description**

Obtains the stroke width of the progress indicator.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Stroke width of the progress indicator, in vp. |

#### \[h2\]OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius()

float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option)

**Description**

Obtains the corner radius of the progress indicator.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ProgressLinearStyleOption](../../structs/arkui-progresslinearstyleoption/document.md)\* option | Pointer to a **ProgressLinearStyleOption** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Corner radius of the progress indicator, in vp. |

#### \[h2\]OH\_ArkUI\_CreateSnapshotOptions()

ArkUI\_SnapshotOptions\* OH\_ArkUI\_CreateSnapshotOptions()

**Description**

Creates a snapshot option object, which must be released using [OH\_ArkUI\_DestroySnapshotOptions()](#oh_arkui_destroysnapshotoptions) when no longer in use.

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_SnapshotOptions](../../structs/arkui-snapshotoptions/document.md)\* | Pointer to the created snapshot option object. If a null pointer is returned, creation failed, possibly due to insufficient memory. |

#### \[h2\]OH\_ArkUI\_DestroySnapshotOptions()

void OH\_ArkUI\_DestroySnapshotOptions(ArkUI\_SnapshotOptions\* snapshotOptions)

**Description**

Destroys a snapshot option object.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SnapshotOptions](../../structs/arkui-snapshotoptions/document.md)\* snapshotOptions | Pointer to the screenshot option. |

#### \[h2\]OH\_ArkUI\_SnapshotOptions\_SetScale()

int32\_t OH\_ArkUI\_SnapshotOptions\_SetScale(ArkUI\_SnapshotOptions\* snapshotOptions, float scale)

**Description**

Sets the scale property in the snapshot options.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_SnapshotOptions](../../structs/arkui-snapshotoptions/document.md)\* snapshotOptions | Pointer to the screenshot option. |
| float scale | Scale factor. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_CrossLanguageOption\_Create()

ArkUI\_CrossLanguageOption\* OH\_ArkUI\_CrossLanguageOption\_Create(void)

**Description**

Creates an instance of the cross-language configuration option.

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* | Pointer to the **ArkUI\_CrossLanguageOption** instance created. If a null pointer is returned, creation failed, possibly due to insufficient memory. |

#### \[h2\]OH\_ArkUI\_CrossLanguageOption\_Destroy()

void OH\_ArkUI\_CrossLanguageOption\_Destroy(ArkUI\_CrossLanguageOption\* option)

**Description**

Destroys an instance of the cross-language configuration option.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* option | Pointer to the cross-language configuration option instance to be destroyed. |

#### \[h2\]OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus()

void OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option, bool enabled)

**Description**

Sets whether cross-language attribute setting is allowed in the configuration option.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* option | Pointer to the cross-language configuration option instance. |
| bool enabled | Whether cross-language attribute setting is allowed. **true** means that cross-language attribute setting is allowed, and **false** means the opposite. The default value is **false**. |

#### \[h2\]OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus()

bool OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus(ArkUI\_CrossLanguageOption\* option)

**Description**

Checks whether cross-language attribute setting is allowed in the configuration option.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CrossLanguageOption](../../structs/arkui-crosslanguageoption/document.md)\* option | Pointer to the cross-language configuration option instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether cross-language attribute setting is allowed. **true** means that cross-language attribute setting is allowed, and **false** means the opposite. |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_Create()

ArkUI\_VisibleAreaEventOptions\* OH\_ArkUI\_VisibleAreaEventOptions\_Create()

**Description**

Creates an instance of visible area change event parameters.

**Since**: 17

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* | Pointer to the created instance of visible area change event parameters. |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_Dispose()

void OH\_ArkUI\_VisibleAreaEventOptions\_Dispose(ArkUI\_VisibleAreaEventOptions\* option)

**Description**

Disposes of an instance of visible area change event parameters.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters to be destroyed. |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios()

int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t size)

**Description**

Sets the threshold ratios for visible area changes.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters. |
| float\* value | Pointer to the array of threshold ratios. Each element represents a ratio of the component's visible area (that is, the area of the component that is visible on screen; only the area within the parent component is counted) to the component's total area. The value range of the threshold is \[0.0, 1.0\]. If the threshold set exceeds this range, the value **0.0** or **1.0** will be used. |
| int32\_t size | Size of the array of threshold ratios. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval()

int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions \*option, int32\_t value)

**Description**

Sets the expected update interval for visible area changes.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md) \*option | Pointer to the instance of visible area change event parameters. |
| int32\_t value | Expected update interval, in ms. Default value: **1000**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport()

int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_SetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions\* option, bool measureFromViewport)

**Description**

Sets the visible area calculation mode.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters. |
| bool measureFromViewport | 
Visible area calculation mode.

**true**: The calculation takes the parent component's **NODE\_CLIP** attribute into account. If the parent component's **NODE\_CLIP** attribute is **false**: Child components can render beyond the parent component's bounds, and the out-of-bounds area is counted as part of the visible area. If the parent component's **NODE\_CLIP** attribute is **true**: Child components are clipped to the parent component's bounds, and the out-of-bounds area is treated as invisible. **false**: The area beyond the parent component's bounds is directly treated as invisible, ignoring the parent component's **NODE\_CLIP** attribute.

Default value: **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios()

int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetRatios(ArkUI\_VisibleAreaEventOptions\* option, float\* value, int32\_t\* size)

**Description**

Obtains the threshold ratios for visible area changes.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters. |
| float\* value | Pointer to the array of threshold ratios. |
| int32\_t\* size | Pointer to the size of the array of threshold ratios. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode) if the provided buffer size is insufficient.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval()

int32\_t OH\_ArkUI\_VisibleAreaEventOptions\_GetExpectedUpdateInterval(ArkUI\_VisibleAreaEventOptions\* option)

**Description**

Obtains the expected update interval for visible area changes.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Expected update interval, in ms. Default value: **1000**. |

#### \[h2\]OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport()

bool OH\_ArkUI\_VisibleAreaEventOptions\_GetMeasureFromViewport(ArkUI\_VisibleAreaEventOptions\* option)

**Description**

Obtains the visible area calculation mode.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_VisibleAreaEventOptions](../../structs/arkui-visibleareaeventoptions/document.md)\* option | Pointer to the instance of visible area change event parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Visible area calculation mode.

**true**: The calculation takes the parent component's **NODE\_CLIP** attribute into account. If the parent component's **NODE\_CLIP** attribute is **false**: Child components can render beyond the parent component's bounds, and the out-of-bounds area is counted as part of the visible area. If the parent component's **NODE\_CLIP** attribute is **true**: Child components are clipped to the parent component's bounds, and the out-of-bounds area is treated as invisible. **false**: The area beyond the parent component's bounds is directly treated as invisible, ignoring the parent component's **NODE\_CLIP** attribute.

Default value: **false**.

 |

#### \[h2\]OH\_ArkUI\_TextPickerRangeContentArray\_Create()

ArkUI\_TextPickerRangeContentArray\* OH\_ArkUI\_TextPickerRangeContentArray\_Create(int32\_t length)

**Description**

Creates an object of the [TextPickerRangeContent](../../structs/arkui-textpickerrangecontentarray/document.md) array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t length | Length of the **TextPickerRangeContent** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md)\* | Pointer to an empty **TextPickerRangeContent** array. |

#### \[h2\]OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex()

void OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* icon, int32\_t index)

**Description**

Configures the icon data at a specified position in the **TextPickerRangeContent** array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md)\* handle | Pointer to the **TextPickerRangeContent** array. |
| char\* icon | Pointer to the icon path. |
| int32\_t index | Array index, starting from 0. |

#### \[h2\]OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex()

void OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* text, int32\_t index)

**Description**

Configures the text data at a specified position in the **TextPickerRangeContent** array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md)\* handle | Pointer to the **TextPickerRangeContent** array. |
| char\* text | Pointer to the text content. |
| int32\_t index | Position in the array, starting from 0. |

#### \[h2\]OH\_ArkUI\_TextPickerRangeContentArray\_Destroy()

void OH\_ArkUI\_TextPickerRangeContentArray\_Destroy(ArkUI\_TextPickerRangeContentArray\* handle)

**Description**

Destroys a **TextPickerRangeContent** array object.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextPickerRangeContentArray](../../structs/arkui-textpickerrangecontentarray/document.md)\* handle | Pointer to the **TextPickerRangeContent** array. |

#### \[h2\]OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create()

ArkUI\_TextCascadePickerRangeContentArray\* OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create(int32\_t length)

**Description**

Creates an object of the [TextCascadePickerRangeContent](../../structs/arkui-textcascadepickerrangecontentarray/document.md) array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t length | Length of the **TextPickerRangeContent** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md)\* | Pointer to an empty **TextCascadePickerRangeContent** array. |

#### \[h2\]OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex()

void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex(ArkUI\_TextCascadePickerRangeContentArray\* handle, char\* text, int32\_t index)

**Description**

Sets the text data at the specified position in the **TextCascadePickerRangeContent** array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md)\* handle | Pointer to the **TextCascadePickerRangeContentHandle** instance. |
| char\* text | Pointer to the text content. |
| int32\_t index | Position in the array, starting from 0. |

#### \[h2\]OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex()

void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex(ArkUI\_TextCascadePickerRangeContentArray\* handle, ArkUI\_TextCascadePickerRangeContentArray\* child, int32\_t index)

**Description**

Configures the child data at a specified position in the **TextCascadePickerRangeContent** array.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md)\* handle | Pointer to the **TextCascadePickerRangeContentHandle** instance. |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md)\* child | Pointer to the child node array. |
| int32\_t index | Position in the array, starting from 0. |

#### \[h2\]OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy()

void OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy(ArkUI\_TextCascadePickerRangeContentArray\* handle)

**Description**

Destroys a **TextCascadePickerRangeContent** array object.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextCascadePickerRangeContentArray](../../structs/arkui-textcascadepickerrangecontentarray/document.md)\* handle | Pointer to the **TextCascadePickerRangeContentHandle** instance. |

#### \[h2\]OH\_ArkUI\_EmbeddedComponentOption\_Create()

ArkUI\_EmbeddedComponentOption\* OH\_ArkUI\_EmbeddedComponentOption\_Create()

**Description**

Creates an **EmbeddedComponent** option object.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md)\* | Pointer to the **EmbeddedComponent** option object. |

#### \[h2\]OH\_ArkUI\_EmbeddedComponentOption\_Dispose()

void OH\_ArkUI\_EmbeddedComponentOption\_Dispose(ArkUI\_EmbeddedComponentOption\* option)

**Description**

Disposes of an **EmbeddedComponent** option object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md)\* option | Pointer to the target **EmbeddedComponent** option object. |

#### \[h2\]OH\_ArkUI\_EmbeddedComponentOption\_SetOnError()

void OH\_ArkUI\_EmbeddedComponentOption\_SetOnError(ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, const char\* name, const char\* message))

**Description**

Sets the [onError](../../../arkts-components/rendering-drawing/embeddedcomponent/document.md#onerror) callback for the **EmbeddedComponent** component. This callback is triggered when an error occurs during the running of the **EmbeddedComponent** component.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md)\* option | Pointer to the **EmbeddedComponent** option object. |
| void (\*callback)(int32\_t code, const char\* name, const char\* message) | 
User-defined callback function.

\- **code**: error code returned when the API call fails. For details about error codes, see [UIExtension Error Codes](../../../error-codes/ui/uiextension-error-codes/document.md).

\- **name**: error name returned when the API call fails.

\- **message**: detailed error message returned when the API call fails.

 |

#### \[h2\]OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated()

void OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated(ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, AbilityBase\_Want\* want))

**Description**

Sets the [onTerminated](../../../arkts-components/rendering-drawing/embeddedcomponent/document.md#onterminated) callback for the **EmbeddedComponent** component. This callback is triggered when the **EmbeddedComponent** component exits properly.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_EmbeddedComponentOption](../../structs/arkui-embeddedcomponentoption/document.md)\* option | Pointer to the **EmbeddedComponent** option object. |
| void (\*callback)(int32\_t code, [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want) | 
User-defined callback function.

\- **code**: result code returned when the started [EmbeddedUIExtensionAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-embeddeduiextensionability-extensionability-for-cross-process-u/document.md) exits. If the EmbeddedUIExtensionAbility exits by calling [terminateSelfWithResult](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#terminateselfwithresult), the result code is the value set by the EmbeddedUIExtensionAbility. If the EmbeddedUIExtensionAbility exits by calling [terminateSelf](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#terminateself), the result code is the default value **0**.

\- **want**: data returned when the EmbeddedUIExtensionAbility exits.

 |

#### \[h2\]OH\_ArkUI\_PositionEdges\_Create()

ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Create()

**Description**

Creates a **PositionEdges** object.

**Since**: 21

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* | Pointer to the **PositionEdges** object. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_Copy()

ArkUI\_PositionEdges\* OH\_ArkUI\_PositionEdges\_Copy(const ArkUI\_PositionEdges\* edges)

**Description**

Deeply copies a **PositionEdges** attribute object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* | Pointer to the new **PositionEdges** object. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_Dispose()

void OH\_ArkUI\_PositionEdges\_Dispose(ArkUI\_PositionEdges\* edges)

**Description**

Disposes of the **PositionEdges** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_SetTop()

void OH\_ArkUI\_PositionEdges\_SetTop(ArkUI\_PositionEdges\* edges, float value)

**Description**

Sets the value of the **PositionEdges** object in the top direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float value | Value of the **PositionEdges** object in the corresponding direction, in vp. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_GetTop()

int32\_t OH\_ArkUI\_PositionEdges\_GetTop(ArkUI\_PositionEdges\* edges, float\* value)

**Description**

Obtains the value of the **PositionEdges** object in the top direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float\* value | Pointer to the value of the **PositionEdges** object in the corresponding direction, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PositionEdges\_SetLeft()

void OH\_ArkUI\_PositionEdges\_SetLeft(ArkUI\_PositionEdges\* edges, float value)

**Description**

Sets the value of the **PositionEdges** object in the left direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float value | Value of the **PositionEdges** object in the corresponding direction, in vp. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_GetLeft()

int32\_t OH\_ArkUI\_PositionEdges\_GetLeft(ArkUI\_PositionEdges\* edges, float\* value)

**Description**

Obtains the value of the **PositionEdges** object in the left direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float\* value | Pointer to the value of the **PositionEdges** object in the corresponding direction, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PositionEdges\_SetBottom()

void OH\_ArkUI\_PositionEdges\_SetBottom(ArkUI\_PositionEdges\* edges, float value)

**Description**

Sets the value of the **PositionEdges** object in the bottom direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float value | Value of the **PositionEdges** object in the corresponding direction, in vp. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_GetBottom()

int32\_t OH\_ArkUI\_PositionEdges\_GetBottom(ArkUI\_PositionEdges\* edges, float\* value)

**Description**

Obtains the value of the **PositionEdges** object in the bottom direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float\* value | Pointer to the value of the **PositionEdges** object in the corresponding direction, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PositionEdges\_SetRight()

void OH\_ArkUI\_PositionEdges\_SetRight(ArkUI\_PositionEdges\* edges, float value)

**Description**

Sets the value of the **PositionEdges** object in the right direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float value | Value of the **PositionEdges** object in the corresponding direction, in vp. |

#### \[h2\]OH\_ArkUI\_PositionEdges\_GetRight()

int32\_t OH\_ArkUI\_PositionEdges\_GetRight(ArkUI\_PositionEdges\* edges, float\* value)

**Description**

Obtains the value of the **PositionEdges** object in the right direction.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PositionEdges](../../structs/arkui-positionedges/document.md)\* edges | Pointer to the **PositionEdges** object. |
| float\* value | Pointer to the value of the **PositionEdges** object in the corresponding direction, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_Create()

ArkUI\_PixelRoundPolicy\* OH\_ArkUI\_PixelRoundPolicy\_Create()

**Description**

Creates a **PixelRoundPolicy** attribute object.

**Since**: 21

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* | Pointer to the **PixelRoundPolicy** object. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_Dispose()

void OH\_ArkUI\_PixelRoundPolicy\_Dispose(ArkUI\_PixelRoundPolicy\* policy)

**Description**

Disposes of the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the target **PixelRoundPolicy** object. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_SetTop()

void OH\_ArkUI\_PixelRoundPolicy\_SetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)

**Description**

Sets the top edge pixel rounding policy for the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy) value | Specific pixel rounding policy. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_GetTop()

int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetTop(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)

**Description**

Obtains the top edge pixel rounding policy from the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy)\* value | Pointer to the specific pixel rounding policy. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_SetStart()

void OH\_ArkUI\_PixelRoundPolicy\_SetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)

**Description**

Sets the start edge pixel rounding policy for the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy) value | Specific pixel rounding policy. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_GetStart()

int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetStart(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)

**Description**

Obtains the start edge pixel rounding policy from the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy)\* value | Pointer to the specific pixel rounding policy. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_SetBottom()

void OH\_ArkUI\_PixelRoundPolicy\_SetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)

**Description**

Sets the bottom edge pixel rounding policy for the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy) value | Specific pixel rounding policy. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_GetBottom()

int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetBottom(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)

**Description**

Obtains the bottom edge pixel rounding policy from the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy)\* value | Pointer to the specific pixel rounding policy. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_SetEnd()

void OH\_ArkUI\_PixelRoundPolicy\_SetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy value)

**Description**

Sets the end edge pixel rounding policy for the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy) value | Specific pixel rounding policy. |

#### \[h2\]OH\_ArkUI\_PixelRoundPolicy\_GetEnd()

int32\_t OH\_ArkUI\_PixelRoundPolicy\_GetEnd(ArkUI\_PixelRoundPolicy\* policy, ArkUI\_PixelRoundCalcPolicy\* value)

**Description**

Obtains the end edge pixel rounding policy from the **PixelRoundPolicy** object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_PixelRoundPolicy](../../structs/arkui-pixelroundpolicy/document.md)\* policy | Pointer to the **PixelRoundPolicy** object. |
| [ArkUI\_PixelRoundCalcPolicy](#arkui_pixelroundcalcpolicy)\* value | Pointer to the specific pixel rounding policy. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_ContentTransitionEffect\_Create()

ArkUI\_ContentTransitionEffect\* OH\_ArkUI\_ContentTransitionEffect\_Create(int32\_t type)

**Description**

Creates a **ContentTransitionEffect** attribute object.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t type | Transition animation type. **0**: No transition animation. **1**: Fade-in and fade-out transition animation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ContentTransitionEffect](../../structs/arkui-contenttransitioneffect/document.md)\* | Pointer to the **ContentTransitionEffect** object. |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_Create()

ArkUI\_GridLayoutOptions\* OH\_ArkUI\_GridLayoutOptions\_Create()

**Description**

Creates **Grid** layout options.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* | Pointer to the **Grid** layout option. |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_Dispose()

void OH\_ArkUI\_GridLayoutOptions\_Dispose(ArkUI\_GridLayoutOptions\* option)

**Description**

Disposes of the **Grid** layout option.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* option | Pointer to the **Grid** layout option. |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes()

int32\_t OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t size)

**Description**

Sets the irregular grid item index array for the grid layout.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* option | Pointer to the **Grid** layout option. |
| uint32\_t\* irregularIndexes | Pointer to the **GridItem** index array. |
| int32\_t size | Size of the **GridItem** index array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes()

int32\_t OH\_ArkUI\_GridLayoutOptions\_GetIrregularIndexes(ArkUI\_GridLayoutOptions\* option, uint32\_t\* irregularIndexes, int32\_t\* size)

**Description**

Obtains the irregular grid item index array for the grid layout. When **OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback** is not set, the grid item specified in this parameter occupies an entire row of the grid that scrolls vertically or an entire column of the grid that scrolls horizontally.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* option | Pointer to the **Grid** layout option. |
| uint32\_t\* irregularIndexes | Pointer to the **GridItem** index array. |
| int32\_t size | Size of the **GridItem** index array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode) if the provided buffer size is insufficient.

A possible cause is that mandatory parameters are left unspecified.

 |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback()

void OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemSize (\*callback)(int32\_t itemIndex, void\* userData))

**Description**

Registers a callback to obtain the row and column span for the grid item at the specified index.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* option | Pointer to the **Grid** layout option. |
| void\* userData | Pointer to the user-defined data. |
| ArkUI\_GridItemSize (\*callback)(int32\_t itemIndex, void\* userData) | 
Callback that returns the row and column span for the grid item at the specified index.

**itemIndex**: grid item index, which must be within the range set by [OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes](#oh_arkui_gridlayoutoptions_setirregularindexes).

 |

#### \[h2\]OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback()

void OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback(ArkUI\_GridLayoutOptions\* option, void\* userData, ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData))

**Description**

Registers a callback to obtain the starting row, starting column, row span, and column span for the grid item at the specified index.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_GridLayoutOptions](../../structs/arkui-gridlayoutoptions/document.md)\* option | Pointer to the **Grid** layout option. |
| void\* userData | Pointer to the user-defined data. |
| ArkUI\_GridItemRect (\*callback)(int32\_t itemIndex, void\* userData) | 
Callback that returns the starting row, starting column, row span, and column span for the grid item at the specified index.

**itemIndex**: grid item index.

 |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_Create()

ArkUI\_ShowCounterConfig\* OH\_ArkUI\_ShowCounterConfig\_Create()

**Description**

Creates a text input counter configuration object.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* | Pointer to the text input counter configuration object. |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_Dispose()

void OH\_ArkUI\_ShowCounterConfig\_Dispose(ArkUI\_ShowCounterConfig\* config)

**Description**

Disposes of the text input counter configuration object.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* config | Pointer to the text input counter configuration object to be disposed. |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_SetCounterTextColor()

void OH\_ArkUI\_ShowCounterConfig\_SetCounterTextColor(ArkUI\_ShowCounterConfig\* config, uint32\_t color)

**Description**

Sets the text color of the counter when the text input has not reached the maximum character limit.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* config | Pointer to the text input counter configuration object. |
| uint32\_t color | Counter text color in 0xARGB format. |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_SetCounterTextOverflowColor()

void OH\_ArkUI\_ShowCounterConfig\_SetCounterTextOverflowColor(ArkUI\_ShowCounterConfig\* config, uint32\_t color)

**Description**

Sets the text color of the counter when the text input exceeds the maximum character limit.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* config | Pointer to the text input counter configuration object. |
| uint32\_t color | Counter text color in 0xARGB format. |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_GetCounterTextColor()

uint32\_t OH\_ArkUI\_ShowCounterConfig\_GetCounterTextColor(ArkUI\_ShowCounterConfig\* config)

**Description**

Obtains the text color of the counter when the text input has not reached the maximum character limit.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* config | Pointer to the text input counter configuration object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Counter text color in 0xARGB format. Returns **0** if no color has been set via [OH\_ArkUI\_ShowCounterConfig\_SetCounterTextColor](#oh_arkui_showcounterconfig_setcountertextcolor). |

#### \[h2\]OH\_ArkUI\_ShowCounterConfig\_GetCounterTextOverflowColor()

uint32\_t OH\_ArkUI\_ShowCounterConfig\_GetCounterTextOverflowColor(ArkUI\_ShowCounterConfig\* config)

**Description**

Obtains the text color of the counter when the text input exceeds the maximum character limit.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ShowCounterConfig](../../structs/arkui-showcounterconfig/document.md)\* config | Pointer to the text input counter configuration object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Counter text color in 0xARGB format. Returns **0** if no color has been set via [OH\_ArkUI\_ShowCounterConfig\_SetCounterTextOverflowColor](#oh_arkui_showcounterconfig_setcountertextoverflowcolor). |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_Create()

ArkUI\_TextMenuItem\* OH\_ArkUI\_TextMenuItem\_Create()

**Description**

Creates a text menu item.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* | Pointer to the **ArkUI\_TextMenuItem** object. |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_Dispose()

void OH\_ArkUI\_TextMenuItem\_Dispose(ArkUI\_TextMenuItem\* textMenuItem)

**Description**

Releases a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* textMenuItem | Pointer to the **ArkUI\_TextMenuItem** object. |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_SetContent()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetContent(ArkUI\_TextMenuItem\* item, const char\* content)

**Description**

Sets the title of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| const char\* content | Pointer to the title of a text menu item. The default value is an empty string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_GetContent()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetContent(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the title of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| char\* buffer | Pointer to the buffer. You can create it and allocate memory to store the title information of the text menu item. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | 
If the return value is [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode), the length of the data written to the buffer is returned.

If the return value is [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode), the minimum length required for writing the string to the buffer is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode) if the buffer size is insufficient.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_SetIcon()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetIcon(ArkUI\_TextMenuItem\* item, const char\* icon)

**Description**

Sets the icon path of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| const char\* icon | Pointer to the icon path of the text menu item. The default value is an empty string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_GetIcon()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetIcon(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the icon path of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| char\* buffer | Pointer to the buffer. You can create it and allocate memory to store the icon path of the text menu item. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | 
If the return value is [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode), the length of the data written to the buffer is returned.

If the return value is [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode), the minimum length required for writing the string to the buffer is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode) if the buffer size is insufficient.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_SetLabelInfo()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetLabelInfo(ArkUI\_TextMenuItem\* item, const char\* labelInfo)

**Description**

Sets the shortcut hint for a text menu item, for example, the shortcut hint for the **Copy** menu item can be set to **Ctrl+C**.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| const char\* labelInfo | Pointer to the shortcut hint of a text menu item. The default value is an empty string. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_GetLabelInfo()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetLabelInfo(const ArkUI\_TextMenuItem\* item, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the shortcut hint for a text menu item, for example, the shortcut hint for the **Copy** menu item is typically **Ctrl+C**.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| char\* buffer | Pointer to the buffer. You can create it and allocate memory to store the shortcut hint of the text menu item. |
| int32\_t bufferSize | Buffer size. |
| int32\_t\* writeLength | 
If the return value is [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode), the length of the data written to the buffer is returned.

If the return value is [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode), the minimum length required for writing the string to the buffer is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](#arkui_errorcode) if the buffer size is insufficient.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_SetId()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_SetId(ArkUI\_TextMenuItem\* item, int32\_t id)

**Description**

Sets the ID of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| int32\_t id | ID of a text menu item. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItem\_GetId()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItem\_GetId(const ArkUI\_TextMenuItem\* item, int32\_t\* id)

**Description**

Obtains the ID of a text menu item.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| int32\_t\* id | Pointer to the ID of a text menu item. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItemArray\_GetSize()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetSize(ArkUI\_TextMenuItemArray\* items, int32\_t\* size)

**Description**

Obtains the size of the text menu item array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object. |
| int32\_t\* size | Pointer to the size of the text menu item array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItemArray\_GetItem()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_GetItem(ArkUI\_TextMenuItemArray\* items, int32\_t index, ArkUI\_TextMenuItem\*\* item)

**Description**

Obtains the text menu item at a specified index from the text menu item array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object. |
| int32\_t index | Index position. |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\*\* item | Double pointer to the **ArkUI\_TextMenuItem** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItemArray\_Insert()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Insert(ArkUI\_TextMenuItemArray\* items, ArkUI\_TextMenuItem\* item, int32\_t index)

**Description**

Inserts a text menu item at a specified index into the text menu item array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object. |
| [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object. |
| int32\_t index | Index position of the text menu item to be inserted. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItemArray\_Erase()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Erase(ArkUI\_TextMenuItemArray\* items, int32\_t index)

**Description**

Deletes the text menu item at a specified index from the text menu item array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object. |
| int32\_t index | Index of the text menu item to be deleted. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextMenuItemArray\_Clear()

ArkUI\_ErrorCode OH\_ArkUI\_TextMenuItemArray\_Clear(ArkUI\_TextMenuItemArray\* items)

**Description**

Clears all text menu items in the text menu item array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextEditMenuOptions\_Create()

ArkUI\_TextEditMenuOptions\* OH\_ArkUI\_TextEditMenuOptions\_Create()

**Description**

Creates a text menu extension object.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md)\* editMenuOptions | Pointer to the **ArkUI\_TextEditMenuOptions** object. |

#### \[h2\]OH\_ArkUI\_TextEditMenuOptions\_Dispose()

void OH\_ArkUI\_TextEditMenuOptions\_Dispose(ArkUI\_TextEditMenuOptions\* editMenuOptions)

**Description**

Releases a text menu extension object.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md)\* editMenuOptions | Pointer to the **ArkUI\_TextEditMenuOptions** object. |

#### \[h2\]ArkUI\_TextCreateMenuCallback()

typedef void (\*ArkUI\_TextCreateMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)

**Description**

Callback for the text menu creation event. This callback is triggered when a text menu is created, allowing you to set menu data in it.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object, which is created and released by the system. You can call [OH\_ArkUI\_TextMenuItemArray\_Insert](#oh_arkui_textmenuitemarray_insert) and [OH\_ArkUI\_TextMenuItemArray\_Erase](#oh_arkui_textmenuitemarray_erase) to modify the array in the callback. |
| void\* userData | Pointer to the user-defined data. |

#### \[h2\]ArkUI\_TextPrepareMenuCallback()

typedef void (\*ArkUI\_TextPrepareMenuCallback)(ArkUI\_TextMenuItemArray\* items, void\* userData)

**Description**

Callback for the text menu preparation event. This callback is called when the text selection area changes and before the menu is displayed, allowing you to set menu data in it.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextMenuItemArray](../../structs/arkui-textmenuitemarray/document.md)\* items | Pointer to the **ArkUI\_TextMenuItemArray** object, which is created and released by the system. You can call [OH\_ArkUI\_TextMenuItemArray\_Insert](#oh_arkui_textmenuitemarray_insert) and [OH\_ArkUI\_TextMenuItemArray\_Erase](#oh_arkui_textmenuitemarray_erase) to modify the array in the callback. |
| void\* userData | Pointer to the user-defined data. |

#### \[h2\]ArkUI\_TextMenuItemClickCallback()

typedef bool (\*ArkUI\_TextMenuItemClickCallback)(const ArkUI\_TextMenuItem\* item,int32\_t start, int32\_t end, void\* userData)

**Description**

Callback for the text menu item click event. This callback is called when a menu item is clicked. You can intercept the default processing behavior in this callback.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkUI\_TextMenuItem](../../structs/arkui-textmenuitem/document.md)\* item | Pointer to the **ArkUI\_TextMenuItem** object, indicating the clicked text menu item. |
| int32\_t start | Start index of the selected text. |
| int32\_t end | End index of the selected text. |
| void\* userData | Pointer to the user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether to intercept the default processing behavior of the system.

**true**: Intercept the system's default processing behavior. For example, clicking text menu items such as **Paste** or **Copy** will only execute the custom processing behavior.

**false**: Do not intercept the system's default processing behavior. For example, clicking text menu items such as **Paste** or **Copy** will first execute the custom processing behavior and then the default processing behavior.

 |

#### \[h2\]OH\_ArkUI\_TextEditMenuOptions\_RegisterOnCreateMenuCallback()

ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnCreateMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextCreateMenuCallback cb)

**Description**

Registers the callback for creating text menus.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md)\* editMenuOptions | Pointer to the **ArkUI\_TextEditMenuOptions** object. |
| void\* userData | Pointer to the user-defined data. |
| [ArkUI\_TextCreateMenuCallback](#arkui_textcreatemenucallback) cb | Callback for creating text menus. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextEditMenuOptions\_RegisterOnPrepareMenuCallback()

ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnPrepareMenuCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextPrepareMenuCallback cb)

**Description**

Registers the callback for preparing text menus.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md)\* editMenuOptions | Pointer to the **ArkUI\_TextEditMenuOptions** object. |
| void\* userData | Pointer to the user-defined data. |
| [ArkUI\_TextPrepareMenuCallback](#arkui_textpreparemenucallback) cb | Callback for preparing text menus. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextEditMenuOptions\_RegisterOnMenuItemClickCallback()

ArkUI\_ErrorCode OH\_ArkUI\_TextEditMenuOptions\_RegisterOnMenuItemClickCallback(ArkUI\_TextEditMenuOptions\* editMenuOptions, void\* userData, ArkUI\_TextMenuItemClickCallback cb)

**Description**

Registers the callback for text menu item clicks.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextEditMenuOptions](../../structs/arkui-texteditmenuoptions/document.md)\* editMenuOptions | Pointer to the **ArkUI\_TextEditMenuOptions** object. |
| void\* userData | Pointer to the user-defined data. |
| [ArkUI\_TextMenuItemClickCallback](#arkui_textmenuitemclickcallback) cb | Callback for text menu item clicks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_Create()

ArkUI\_TextSelectionMenuOptions\* OH\_ArkUI\_TextSelectionMenuOptions\_Create();

**Description**

Creates a custom text selection menu.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_Dispose()

void OH\_ArkUI\_TextSelectionMenuOptions\_Dispose(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions)

**Description**

Releases a custom text selection menu object.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_SetSpanType()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType textSpanType)

**Description**

Sets the recognition type of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_TextSpanType](#arkui_textspantype) textSpanType | Recognition type of a custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_GetSpanType()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetSpanType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextSpanType\* spanType)

**Description**

Obtains the recognition type of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_TextSpanType](#arkui_textspantype)\* spanType | Pointer to the recognition type of a custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_SetContentNode()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle node)

**Description**

Sets the content node of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Content node of the custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_GetContentNode()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetContentNode(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_NodeHandle\* node)

**Description**

Obtains the content node of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md)\* node | Pointer to the content node of the custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_SetResponseType()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_SetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType responseType)

**Description**

Sets the response type of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_TextResponseType](#arkui_textresponsetype) responseType | Response type of the custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_GetResponseType()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_GetResponseType(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, ArkUI\_TextResponseType\* responseType)

**Description**

Obtains the response type of a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| [ArkUI\_TextResponseType](#arkui_textresponsetype)\* responseType | Pointer to the response type of the custom text selection menu. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))

**Description**

Registers the callback for the event of showing a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| void\* userData | Pointer to the user-defined data, which can be any value. After the setting, the value is returned through the callback. |
| void (\*callback)(int32\_t start, int32\_t end, void\* userData) | 
Callback for the event of showing a custom text selection menu.

**start**: start position of the selected text.

**end**: end position of the selected text.

**userData**: user-defined data, which corresponds to the input parameter **userData** of the **OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuShowCallback** API.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback()

ArkUI\_ErrorCode OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback(ArkUI\_TextSelectionMenuOptions\* selectionMenuOptions, void\* userData, void (\*callback)(int32\_t start, int32\_t end, void\* userData))

**Description**

Registers the callback for the event of hiding a custom text selection menu.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TextSelectionMenuOptions](../../structs/arkui-textselectionmenuoptions/document.md)\* selectionMenuOptions | Pointer to the **ArkUI\_TextSelectionMenuOptions** object. |
| void\* userData | Pointer to the user-defined data, which can be any value. After the setting, the value is returned through the callback. |
| void (\*callback)(int32\_t start, int32\_t end, void\* userData) | 
Callback for the event of hiding a custom text selection menu.

**start**: start position of the selected text.

**end**: end position of the selected text.

**userData**: user-defined data, which corresponds to the input parameter **userData** of the **OH\_ArkUI\_TextSelectionMenuOptions\_RegisterOnMenuHideCallback** API.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](#arkui_errorcode) | 
Return result.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](#arkui_errorcode) if a parameter error occurs.

 |
