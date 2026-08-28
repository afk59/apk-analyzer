# native\_render.h

#### Overview

Declares the APIs of **NativeRender**. For details, see [Building a Rendering Node](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-embed-render-components).

**File to include**: <arkui/native\_render.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 20

**Related module**: [ArkUI\_RenderNodeUtils](../../modules/arkui-rendernodeutils/document.md)

**Sample**: [NativeRenderNodeSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeRenderNodeSample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_RenderNode\*](../../structs/arkui-rendernodehandle/document.md) | ArkUI\_RenderNodeHandle | Defines a struct for the render node pointer. |
| [ArkUI\_RenderContentModifier\*](../../structs/arkui-rendercontentmodifierhandle/document.md) | ArkUI\_RenderContentModifierHandle | Defines a struct for the content modifier pointer. |
| [ArkUI\_FloatProperty\*](../../structs/arkui-floatpropertyhandle/document.md) | ArkUI\_FloatPropertyHandle | Defines a struct for the float property pointer. |
| [ArkUI\_Vector2Property\*](../../structs/arkui-vector2propertyhandle/document.md) | ArkUI\_Vector2PropertyHandle | Defines a struct for the 2D vector property pointer. |
| [ArkUI\_ColorProperty\*](../../structs/arkui-colorpropertyhandle/document.md) | ArkUI\_ColorPropertyHandle | Defines a struct for the color property pointer. |
| [ArkUI\_FloatAnimatableProperty\*](../../structs/arkui-floatanimatablepropertyhandle/document.md) | ArkUI\_FloatAnimatablePropertyHandle | Defines a struct for the animatable float property pointer. |
| [ArkUI\_Vector2AnimatableProperty\*](../../structs/arkui-vector2animatablepropertyhandle/document.md) | ArkUI\_Vector2AnimatablePropertyHandle | Defines a struct for the animatable 2D vector property pointer. |
| [ArkUI\_ColorAnimatableProperty\*](../../structs/arkui-coloranimatablepropertyhandle/document.md) | ArkUI\_ColorAnimatablePropertyHandle | Defines a struct for the animatable color property pointer. |
| [ArkUI\_RectShape](../../structs/arkui-rectshapeoption/document.md) | ArkUI\_RectShapeOption | Defines a struct for the rectangle shape configuration. |
| [ArkUI\_NodeBorderStyle](../../structs/arkui-nodeborderstyleoption/document.md) | ArkUI\_NodeBorderStyleOption | Defines a struct for the node border style configuration. |
| [ArkUI\_NodeBorderWidth](../../structs/arkui-nodeborderwidthoption/document.md) | ArkUI\_NodeBorderWidthOption | Defines a struct for the node border width configuration. |
| [ArkUI\_NodeBorderColor](../../structs/arkui-nodebordercoloroption/document.md) | ArkUI\_NodeBorderColorOption | Defines a struct for the node border color configuration. |
| [ArkUI\_NodeBorderRadius](../../structs/arkui-nodeborderradiusoption/document.md) | ArkUI\_NodeBorderRadiusOption | Defines a struct for the node border radius configuration. |
| [ArkUI\_CircleShape](../../structs/arkui-circleshapeoption/document.md) | ArkUI\_CircleShapeOption | Defines a struct for the circle shape configuration. |
| [ArkUI\_RoundRectShape](../../structs/arkui-roundrectshapeoption/document.md) | ArkUI\_RoundRectShapeOption | Defines a struct for the rounded rectangle shape configuration. |
| [ArkUI\_CommandPath](../../structs/arkui-commandpathoption/document.md) | ArkUI\_CommandPathOption | Defines a struct for the custom path configuration. |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | ArkUI\_RenderNodeMaskOption | Defines a struct for the render node mask configuration. |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md) | ArkUI\_RenderNodeClipOption | Defines a struct for the render node clip configuration. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AddRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)](#oh_arkui_rendernodeutils_addrendernode) | \- | Adds a child render node to the parent custom node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)](#oh_arkui_rendernodeutils_removerendernode) | \- | Removes the specified child render node from the parent node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearRenderNodeChildren(ArkUI\_NodeHandle node)](#oh_arkui_rendernodeutils_clearrendernodechildren) | \- | Clears child render nodes in the parent node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_Invalidate(ArkUI\_NodeHandle node)](#oh_arkui_rendernodeutils_invalidate) | \- | Marks the target node, triggering its lifecycle and child nodes to re-render. |
| [ArkUI\_RenderNodeHandle OH\_ArkUI\_RenderNodeUtils\_CreateNode()](#oh_arkui_rendernodeutils_createnode) | \- | Creates a render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_DisposeNode(ArkUI\_RenderNodeHandle node)](#oh_arkui_rendernodeutils_disposenode) | \- | Destroys the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AddChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)](#oh_arkui_rendernodeutils_addchild) | \- | Adds a child node to the target parent render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_InsertChildAfter(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child, ArkUI\_RenderNodeHandle sibling)](#oh_arkui_rendernodeutils_insertchildafter) | \- | Adds a child node after the target child node of the parent node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)](#oh_arkui_rendernodeutils_removechild) | \- | Removes a child node from the specified render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearChildren(ArkUI\_RenderNodeHandle node)](#oh_arkui_rendernodeutils_clearchildren) | \- | Clears all child nodes of the specified render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChild(ArkUI\_RenderNodeHandle node, int32\_t index, ArkUI\_RenderNodeHandle\* child)](#oh_arkui_rendernodeutils_getchild) | \- | Obtains the child node at the specified index. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFirstChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* child)](#oh_arkui_rendernodeutils_getfirstchild) | \- | Obtains the first child node of the specified render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetNextSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)](#oh_arkui_rendernodeutils_getnextsibling) | \- | Obtains the next sibling node of the specified node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPreviousSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)](#oh_arkui_rendernodeutils_getprevioussibling) | \- | Obtains the previous sibling node of the specified node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildren(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\*\* children, int32\_t\* count)](#oh_arkui_rendernodeutils_getchildren) | \- | Obtains all child render nodes of the parent render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildrenCount(ArkUI\_RenderNodeHandle node, int32\_t\* count)](#oh_arkui_rendernodeutils_getchildrencount) | \- | Obtains the number of child render nodes of the specified render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t color)](#oh_arkui_rendernodeutils_setbackgroundcolor) | \- | Sets the background color for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)](#oh_arkui_rendernodeutils_getbackgroundcolor) | \- | Obtains the background color of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t clipToFrame)](#oh_arkui_rendernodeutils_setcliptoframe) | \- | Sets whether to clip the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t\* clipToFrame)](#oh_arkui_rendernodeutils_getcliptoframe) | \- | Obtains whether the render node is clipped. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t clipToBounds)](#oh_arkui_rendernodeutils_setcliptobounds) | \- | Sets whether to clip to the bounds of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t\* clipToBounds)](#oh_arkui_rendernodeutils_getcliptobounds) | \- | Sets whether clipping to the bounds of the render node is enabled. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetOpacity(ArkUI\_RenderNodeHandle node, float opacity)](#oh_arkui_rendernodeutils_setopacity) | \- | Sets the opacity value for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetOpacity(ArkUI\_RenderNodeHandle node, float\* opacity)](#oh_arkui_rendernodeutils_getopacity) | \- | Obtains the opacity value of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetSize(ArkUI\_RenderNodeHandle node, int32\_t width, int32\_t height)](#oh_arkui_rendernodeutils_setsize) | \- | Sets the size for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetSize(ArkUI\_RenderNodeHandle node, int32\_t\* width, int32\_t\* height)](#oh_arkui_rendernodeutils_getsize) | \- | Obtains the size of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPosition(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)](#oh_arkui_rendernodeutils_setposition) | \- | Sets the position coordinates for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPosition(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)](#oh_arkui_rendernodeutils_getposition) | \- | Obtains the position coordinates of the render node. The coordinates are the position offset of the render node relative to its parent node after the layout. The unit is px. The coordinates are the result after the parent node lays out the node. Therefore, the **offset** attribute that takes effect after the layout and the **position** attribute that does not participate in the layout do not affect the coordinates. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPivot(ArkUI\_RenderNodeHandle node, float x, float y)](#oh_arkui_rendernodeutils_setpivot) | \- | Sets the pivot point for the transformation of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPivot(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](#oh_arkui_rendernodeutils_getpivot) | \- | Obtains the pivot point coordinates of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetScale(ArkUI\_RenderNodeHandle node, float x, float y)](#oh_arkui_rendernodeutils_setscale) | \- | Sets the scale factors for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetScale(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](#oh_arkui_rendernodeutils_getscale) | \- | Obtains the scale factors of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTranslation(ArkUI\_RenderNodeHandle node, float x, float y)](#oh_arkui_rendernodeutils_settranslation) | \- | Sets the translation offset for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetTranslation(ArkUI\_RenderNodeHandle node, float\* x, float\* y)](#oh_arkui_rendernodeutils_gettranslation) | \- | Obtains the translation offset of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetRotation(ArkUI\_RenderNodeHandle node, float x, float y, float z)](#oh_arkui_rendernodeutils_setrotation) | \- | Sets the rotation angles for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetRotation(ArkUI\_RenderNodeHandle node, float\* x, float\* y, float\* z)](#oh_arkui_rendernodeutils_getrotation) | \- | Obtains the rotation angles of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTransform(ArkUI\_RenderNodeHandle node, float\* matrix)](#oh_arkui_rendernodeutils_settransform) | \- | Sets the transformation matrix for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t color)](#oh_arkui_rendernodeutils_setshadowcolor) | \- | Sets the shadow color for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)](#oh_arkui_rendernodeutils_getshadowcolor) | \- | Obtains the shadow color of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)](#oh_arkui_rendernodeutils_setshadowoffset) | \- | Sets the shadow offset for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)](#oh_arkui_rendernodeutils_getshadowoffset) | \- | Obtains the shadow offset of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowAlpha(ArkUI\_RenderNodeHandle node, float alpha)](#oh_arkui_rendernodeutils_setshadowalpha) | \- | Sets the shadow alpha (transparency) for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowAlpha(ArkUI\_RenderNodeHandle node, float\* alpha)](#oh_arkui_rendernodeutils_getshadowalpha) | \- | Obtains the shadow alpha (transparency) of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowElevation(ArkUI\_RenderNodeHandle node, float elevation)](#oh_arkui_rendernodeutils_setshadowelevation) | \- | Sets the shadow elevation for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowElevation(ArkUI\_RenderNodeHandle node, float\* elevation)](#oh_arkui_rendernodeutils_getshadowelevation) | \- | Obtains the shadow elevation of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowRadius(ArkUI\_RenderNodeHandle node, float radius)](#oh_arkui_rendernodeutils_setshadowradius) | \- | Sets the shadow radius for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowRadius(ArkUI\_RenderNodeHandle node, float\* radius)](#oh_arkui_rendernodeutils_getshadowradius) | \- | Obtains the shadow radius of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\* borderStyle)](#oh_arkui_rendernodeutils_setborderstyle) | \- | Sets the border style for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\*\* borderStyle)](#oh_arkui_rendernodeutils_getborderstyle) | \- | Obtains the border style of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\* borderWidth)](#oh_arkui_rendernodeutils_setborderwidth) | \- | Sets the border width for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\*\* borderWidth)](#oh_arkui_rendernodeutils_getborderwidth) | \- | Obtains the border width of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\* borderColor)](#oh_arkui_rendernodeutils_setbordercolor) | \- | Sets the border color for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\*\* borderColor)](#oh_arkui_rendernodeutils_getbordercolor) | \- | Obtains the border color of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\* borderRadius)](#oh_arkui_rendernodeutils_setborderradius) | \- | Sets the border corner radius for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\*\* borderRadius)](#oh_arkui_rendernodeutils_getborderradius) | \- | Obtains the border corner radius of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMask(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeMaskOption\* mask)](#oh_arkui_rendernodeutils_setmask) | \- | Applies a mask to the render node using the mask configuration. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClip(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeClipOption\* clip)](#oh_arkui_rendernodeutils_setclip) | \- | Applies clipping to the render node using the clipping configuration. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMarkNodeGroup(ArkUI\_RenderNodeHandle node, bool markNodeGroup)](#oh_arkui_rendernodeutils_setmarknodegroup) | \- | Marks whether to prioritize drawing the node and its child nodes. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBounds(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y, int32\_t width, int32\_t height)](#oh_arkui_rendernodeutils_setbounds) | \- | Sets the bounds for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBounds(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y, int32\_t\* width, int32\_t\* height)](#oh_arkui_rendernodeutils_getbounds) | \- | Obtains the bounds of the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetDrawRegion(ArkUI\_RenderNodeHandle node, float x, float y, float w, float h)](#oh_arkui_rendernodeutils_setdrawregion) | \- | Sets the drawing region for the render node. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier(ArkUI\_RenderNodeHandle node, ArkUI\_RenderContentModifierHandle modifier)](#oh_arkui_rendernodeutils_attachcontentmodifier) | \- | Attaches a content modifier to the render node. |
| [ArkUI\_RenderContentModifierHandle OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier()](#oh_arkui_rendernodeutils_createcontentmodifier) | \- | Creates a content modifier. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeContentModifier(ArkUI\_RenderContentModifierHandle modifier)](#oh_arkui_rendernodeutils_disposecontentmodifier) | \- | Disposes of the content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatPropertyHandle property)](#oh_arkui_rendernodeutils_attachfloatproperty) | \- | Attaches a float property to the target content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2Property(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2PropertyHandle property)](#oh_arkui_rendernodeutils_attachvector2property) | \- | Attaches a 2D vector property to the target content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorPropertyHandle property)](#oh_arkui_rendernodeutils_attachcolorproperty) | \- | Attaches a color property to the target content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatAnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_attachfloatanimatableproperty) | \- | Attaches an animatable float property to the target content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2AnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_attachvector2animatableproperty) | \- | Attaches an animatable 2D vector property to the target content modifier. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorAnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_attachcoloranimatableproperty) | \- | Attaches an animatable color property to the target content modifier. |
| [ArkUI\_FloatPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatProperty(float value)](#oh_arkui_rendernodeutils_createfloatproperty) | \- | Creates a float property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float value)](#oh_arkui_rendernodeutils_setfloatpropertyvalue) | \- | Sets the value of the float property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float\* value)](#oh_arkui_rendernodeutils_getfloatpropertyvalue) | \- | Obtains the value of the float property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatProperty(ArkUI\_FloatPropertyHandle property)](#oh_arkui_rendernodeutils_disposefloatproperty) | \- | Disposes of the float property. |
| [ArkUI\_Vector2PropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2Property(float x, float y)](#oh_arkui_rendernodeutils_createvector2property) | \- | Creates a 2D vector property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float x, float y)](#oh_arkui_rendernodeutils_setvector2propertyvalue) | \- | Sets the value of the 2D vector property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float\* x, float\* y)](#oh_arkui_rendernodeutils_getvector2propertyvalue) | \- | Obtains the value of the 2D vector property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2Property(ArkUI\_Vector2PropertyHandle property)](#oh_arkui_rendernodeutils_disposevector2property) | \- | Disposes of the 2D vector property. |
| [ArkUI\_ColorPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorProperty(uint32\_t value)](#oh_arkui_rendernodeutils_createcolorproperty) | \- | Creates a color property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t value)](#oh_arkui_rendernodeutils_setcolorpropertyvalue) | \- | Sets the value of the color property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t\* value)](#oh_arkui_rendernodeutils_getcolorpropertyvalue) | \- | Obtains the value of the color property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeColorProperty(ArkUI\_ColorPropertyHandle property)](#oh_arkui_rendernodeutils_disposecolorproperty) | \- | Disposes of the color property. |
| [ArkUI\_FloatAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty(float value)](#oh_arkui_rendernodeutils_createfloatanimatableproperty) | \- | Creates an animatable float property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float value)](#oh_arkui_rendernodeutils_setfloatanimatablepropertyvalue) | \- | Sets the value of the animatable float property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float\* value)](#oh_arkui_rendernodeutils_getfloatanimatablepropertyvalue) | \- | Obtains the value of the animatable float property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatAnimatableProperty(ArkUI\_FloatAnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_disposefloatanimatableproperty) | \- | Disposes of the animatable float property. |
| [ArkUI\_Vector2AnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty(float x, float y)](#oh_arkui_rendernodeutils_createvector2animatableproperty) | \- | Creates an animatable 2D vector property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float x, float y)](#oh_arkui_rendernodeutils_setvector2animatablepropertyvalue) | \- | Sets the value of the animatable 2D vector property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float\* x, float\* y)](#oh_arkui_rendernodeutils_getvector2animatablepropertyvalue) | \- | Obtains the value of the animatable 2D vector property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2AnimatableProperty(ArkUI\_Vector2AnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_disposevector2animatableproperty) | \- | Disposes of the animatable 2D vector property. |
| [ArkUI\_ColorAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty(uint32\_t value)](#oh_arkui_rendernodeutils_createcoloranimatableproperty) | \- | Creates an animatable color property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t value)](#oh_arkui_rendernodeutils_setcoloranimatablepropertyvalue) | \- | Sets the value of the animatable color property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t\* value)](#oh_arkui_rendernodeutils_getcoloranimatablepropertyvalue) | \- | Obtains the value of the animatable color property. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeColorAnimatableProperty(ArkUI\_ColorAnimatablePropertyHandle property)](#oh_arkui_rendernodeutils_disposecoloranimatableproperty) | \- | Disposes of the animatable color property. |
| [int32\_t OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw(ArkUI\_RenderContentModifierHandle modifier, void\* userData, void (callback)(ArkUI\_DrawContext\* context, void userData))](#oh_arkui_rendernodeutils_setcontentmodifierondraw) | \- | Sets the **onDraw** callback function for the content modifier. |
| [ArkUI\_RectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRectShapeOption()](#oh_arkui_rendernodeutils_createrectshapeoption) | \- | Creates a rectangle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRectShapeOption(ArkUI\_RectShapeOption\* option)](#oh_arkui_rendernodeutils_disposerectshapeoption) | \- | Disposes of the rectangle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRectShapeOptionEdgeValue(ArkUI\_RectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)](#oh_arkui_rendernodeutils_setrectshapeoptionedgevalue) | \- | Sets the edge value for the rectangle shape option. |
| [ArkUI\_NodeBorderStyleOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption()](#oh_arkui_rendernodeutils_createnodeborderstyleoption) | \- | Creates a node border style option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption(ArkUI\_NodeBorderStyleOption\* option)](#oh_arkui_rendernodeutils_disposenodeborderstyleoption) | \- | Disposes of the node border style option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle(ArkUI\_NodeBorderStyleOption\* option, ArkUI\_BorderStyle edgeStyle, ArkUI\_EdgeDirection direction)](#oh_arkui_rendernodeutils_setnodeborderstyleoptionedgestyle) | \- | Sets the edge style for the node border style option. |
| [ArkUI\_NodeBorderWidthOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption()](#oh_arkui_rendernodeutils_createnodeborderwidthoption) | \- | Creates a node border width option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption(ArkUI\_NodeBorderWidthOption\* option)](#oh_arkui_rendernodeutils_disposenodeborderwidthoption) | \- | Disposes of the node border width option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth(ArkUI\_NodeBorderWidthOption\* option, float edgeWidth, ArkUI\_EdgeDirection direction)](#oh_arkui_rendernodeutils_setnodeborderwidthoptionedgewidth) | \- | Sets the edge width for the node border width option. |
| [ArkUI\_NodeBorderColorOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption()](#oh_arkui_rendernodeutils_createnodebordercoloroption) | \- | Creates a node border color option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption(ArkUI\_NodeBorderColorOption\* option)](#oh_arkui_rendernodeutils_disposenodebordercoloroption) | \- | Disposes of the node border color option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor(ArkUI\_NodeBorderColorOption\* option, uint32\_t edgeColor, ArkUI\_EdgeDirection direction)](#oh_arkui_rendernodeutils_setnodebordercoloroptionedgecolor) | \- | Sets the edge color for the node border color option. |
| [ArkUI\_NodeBorderRadiusOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderRadiusOption()](#oh_arkui_rendernodeutils_createnodeborderradiusoption) | \- | Creates a node border radius option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderRadiusOption(ArkUI\_NodeBorderRadiusOption\* option)](#oh_arkui_rendernodeutils_disposenodeborderradiusoption) | \- | Disposes of the node border radius option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderRadiusOptionCornerRadius(ArkUI\_NodeBorderRadiusOption\* option, uint32\_t cornerRadius, ArkUI\_CornerDirection direction)](#oh_arkui_rendernodeutils_setnodeborderradiusoptioncornerradius) | \- | Sets the corner radius for the node border radius option. |
| [ArkUI\_CircleShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCircleShapeOption()](#oh_arkui_rendernodeutils_createcircleshapeoption) | \- | Creates a circle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeCircleShapeOption(ArkUI\_CircleShapeOption\* option)](#oh_arkui_rendernodeutils_disposecircleshapeoption) | \- | Disposes of the circle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterX(ArkUI\_CircleShapeOption\* option, float centerX)](#oh_arkui_rendernodeutils_setcircleshapeoptioncenterx) | \- | Sets the x-coordinate of the center for the circle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterY(ArkUI\_CircleShapeOption\* option, float centerY)](#oh_arkui_rendernodeutils_setcircleshapeoptioncentery) | \- | Sets the y-coordinate of the center for the circle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionRadius(ArkUI\_CircleShapeOption\* option, float radius)](#oh_arkui_rendernodeutils_setcircleshapeoptionradius) | \- | Sets the radius value for the circle shape option. |
| [ArkUI\_RoundRectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRoundRectShapeOption()](#oh_arkui_rendernodeutils_createroundrectshapeoption) | \- | Creates a rounded rectangle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRoundRectShapeOption(ArkUI\_RoundRectShapeOption\* option)](#oh_arkui_rendernodeutils_disposeroundrectshapeoption) | \- | Disposes of the rounded rectangle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionEdgeValue(ArkUI\_RoundRectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)](#oh_arkui_rendernodeutils_setroundrectshapeoptionedgevalue) | \- | Sets the edge values for the rounded rectangle shape option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionCornerXY(ArkUI\_RoundRectShapeOption\* option, float x, float y, ArkUI\_CornerDirection direction)](#oh_arkui_rendernodeutils_setroundrectshapeoptioncornerxy) | \- | Sets the coordinates for the target corner. |
| [ArkUI\_CommandPathOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCommandPathOption()](#oh_arkui_rendernodeutils_createcommandpathoption) | \- | Creates a custom drawing path option. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeCommandPathOption(ArkUI\_CommandPathOption\* option)](#oh_arkui_rendernodeutils_disposecommandpathoption) | \- | Disposes of the custom drawing path option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetCommandPathOptionCommands(ArkUI\_CommandPathOption\* option, char\* commands)](#oh_arkui_rendernodeutils_setcommandpathoptioncommands) | \- | Sets the command values for the custom drawing path option. |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRectShape(ArkUI\_RectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodemaskoptionfromrectshape) | \- | Creates a mask from a rectangle shape. |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodemaskoptionfromroundrectshape) | \- | Creates a mask from a rounded rectangle shape. |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodemaskoptionfromcircleshape) | \- | Creates a mask from a circle shape. |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodemaskoptionfromovalshape) | \- | Creates a mask from an oval shape. |
| [ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCommandPath(ArkUI\_CommandPathOption\* path)](#oh_arkui_rendernodeutils_createrendernodemaskoptionfromcommandpath) | \- | Creates a mask from a custom drawing path. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeMaskOption(ArkUI\_RenderNodeMaskOption\* option)](#oh_arkui_rendernodeutils_disposerendernodemaskoption) | \- | Disposes of the render node mask option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionFillColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t fillColor)](#oh_arkui_rendernodeutils_setrendernodemaskoptionfillcolor) | \- | Sets the fill color for the render node mask option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t strokeColor)](#oh_arkui_rendernodeutils_setrendernodemaskoptionstrokecolor) | \- | Sets the stroke color for the render node mask option. |
| [void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeWidth(ArkUI\_RenderNodeMaskOption\* mask, float strokeWidth)](#oh_arkui_rendernodeutils_setrendernodemaskoptionstrokewidth) | \- | Sets the stroke width for the render node mask option. |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRectShape(ArkUI\_RectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodeclipoptionfromrectshape) | \- | Creates a render node clip option from a rectangle shape. |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodeclipoptionfromroundrectshape) | \- | Creates a render node clip option from a rounded rectangle shape. |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodeclipoptionfromcircleshape) | \- | Creates a render node clip option from a circle shape. |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)](#oh_arkui_rendernodeutils_createrendernodeclipoptionfromovalshape) | \- | Creates a render node clip option from an oval shape. |
| [ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCommandPath(ArkUI\_CommandPathOption\* path)](#oh_arkui_rendernodeutils_createrendernodeclipoptionfromcommandpath) | \- | Creates a render node clip option from a custom drawing path. |
| [void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeClipOption(ArkUI\_RenderNodeClipOption\* option)](#oh_arkui_rendernodeutils_disposerendernodeclipoption) | \- | Disposes of the render node clip option. |

#### Function Description

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AddRenderNode()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AddRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)

**Description**

Adds a child render node to the parent custom node.

The parent node supports only nodes of the **ARKUI\_NODE\_CUSTOM** type in [ArkUI\_NodeType](../native-node-h/document.md#arkui_nodetype). Each custom node can be mounted to only one **ArkUI\_RenderNodeHandle**. **customNode** cannot be mounted to another **ArkUI\_NodeHandle**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target parent node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) child | Child render node to be added. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node is not a custom node.

Returns [ARKUI\_ERROR\_CODE\_CHILD\_EXISTED](../native-type-h/document.md#arkui_errorcode) if the target node already has a child node.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_PARENT\_EXISTED](../native-type-h/document.md#arkui_errorcode) if the target rendering node already has a parent node.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the current render node originates from a FrameNode that has been either detached as a child node or destroyed. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_RemoveRenderNode()

int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle child)

**Description**

Removes the specified child render node from the parent node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target parent node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) child | Child render node to be removed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node is not a custom node.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_ClearRenderNodeChildren()

int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearRenderNodeChildren(ArkUI\_NodeHandle node)

**Description**

Clears child render nodes in the parent node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target parent node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node is not a custom node.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_Invalidate()

int32\_t OH\_ArkUI\_RenderNodeUtils\_Invalidate(ArkUI\_NodeHandle node)

**Description**

Marks the target node, triggering its lifecycle and child nodes to re-render.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateNode()

ArkUI\_RenderNodeHandle OH\_ArkUI\_RenderNodeUtils\_CreateNode()

**Description**

Creates a render node.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) | Target render node. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeNode()

int32\_t OH\_ArkUI\_RenderNodeUtils\_DisposeNode(ArkUI\_RenderNodeHandle node)

**Description**

Destroys the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AddChild()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AddChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)

**Description**

Adds a child node to the target parent render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) child | Child render node to be added. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the current render node originates from a FrameNode that has been either detached as a child node or destroyed. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_InsertChildAfter()

int32\_t OH\_ArkUI\_RenderNodeUtils\_InsertChildAfter(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child, ArkUI\_RenderNodeHandle sibling)

**Description**

Adds a child node after the target child node of the parent node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) child | Child render node to be added. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) sibling | Target child node, which is used to determine the reference sibling render node of the insertion position. If the node is not in the current child node list of **node**, the node is appended to the end. |
| **Return value** |  |

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the child node originates from a FrameNode and the corresponding FrameNode is no longer in the adopted state. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_RemoveChild()

int32\_t OH\_ArkUI\_RenderNodeUtils\_RemoveChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle child)

**Description**

Removes a child node from the specified render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) child | Child render node to be removed. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_ClearChildren()

int32\_t OH\_ArkUI\_RenderNodeUtils\_ClearChildren(ArkUI\_RenderNodeHandle node)

**Description**

Clears all child nodes of the specified render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetChild()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChild(ArkUI\_RenderNodeHandle node, int32\_t index, ArkUI\_RenderNodeHandle\* child)

**Description**

Obtains the child node at the specified index.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| int32\_t index | Zero-based index of the child node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\* child | Render node pointer used to receive the child node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](../native-type-h/document.md#arkui_errorcode) if the corresponding render child node is not found.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetFirstChild()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFirstChild(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* child)

**Description**

Obtains the first child node of the specified render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\* child | Render node pointer used to receive the first child node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](../native-type-h/document.md#arkui_errorcode) if the corresponding render child node is not found.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetNextSibling()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetNextSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)

**Description**

Obtains the next sibling node of the specified node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Reference node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\* sibling | Pointer to the render node, which is used to receive the next sibling node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](../native-type-h/document.md#arkui_errorcode) if the corresponding render child node is not found.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetPreviousSibling()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPreviousSibling(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\* sibling)

**Description**

Obtains the previous sibling node of the specified node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Reference node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\* sibling | Pointer to the render node, which is used to receive the previous sibling node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST](../native-type-h/document.md#arkui_errorcode) if the corresponding render child node is not found.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetChildren()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildren(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeHandle\*\* children, int32\_t\* count)

**Description**

Obtains all child render nodes of the parent render node. The caller is responsible for releasing the returned child node array.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\*\* children | Pointer array used to store all child render nodes. |
| int32\_t\* count | Pointer used to store the number of obtained child nodes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetChildrenCount()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetChildrenCount(ArkUI\_RenderNodeHandle node, int32\_t\* count)

**Description**

Obtains the number of child render nodes of the specified render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target parent render node. |
| int32\_t\* count | Pointer used to store the number of child nodes. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t color)

**Description**

Sets the background color for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| uint32\_t color | 
ARGB color value (32-bit unsigned integer).

Default value: **0x00000000**.

**Description of color byte layout**:

\- Bits 24-31: alpha channel (0x00 for fully transparent, 0xFF for fully opaque).

\- Bits 16-23: red channel.

\- Bits 8-15: green channel.

\- Bits 0-7: blue channel.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBackgroundColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBackgroundColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)

**Description**

Obtains the background color of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| uint32\_t\* color | 
Integer pointer used to store the obtained RGBA color value.

Default value: **0x00000000**.

**Description of color byte layout**:

\- Bits 24-31: alpha channel (0x00 for fully transparent, 0xFF for fully opaque).

\- Bits 16-23: red channel.

\- Bits 8-15: green channel.

\- Bits 0-7: blue channel.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetClipToFrame()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t clipToFrame)

**Description**

Sets whether to clip the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t clipToFrame | 
Whether to clip the current render node. **1**: Clip to frame. **0**: Do not clip.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetClipToFrame()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToFrame(ArkUI\_RenderNodeHandle node, int32\_t\* clipToFrame)

**Description**

Obtains whether the render node is clipped.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* clipToFrame | 
Integer pointer used to receive the clipping status (1 or 0).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetClipToBounds()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t clipToBounds)

**Description**

Sets whether to clip to the bounds of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t clipToBounds | 
Clipping flag. **1**: Clip to bounds. **0**: Do not clip.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetClipToBounds()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetClipToBounds(ArkUI\_RenderNodeHandle node, int32\_t\* clipToBounds)

**Description**

Sets whether clipping to the bounds of the render node is enabled.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* clipToBounds | 
Clipping flag. **1**: Clip to bounds. **0**: Do not clip.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetOpacity()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetOpacity(ArkUI\_RenderNodeHandle node, float opacity)

**Description**

Sets the opacity value for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float opacity | 
Opacity value (0.0–1.0).

Default value: **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetOpacity()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetOpacity(ArkUI\_RenderNodeHandle node, float\* opacity)

**Description**

Obtains the opacity value of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* opacity | 
Pointer used to store the opacity value (0.0–1.0).

Default value: **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetSize()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetSize(ArkUI\_RenderNodeHandle node, int32\_t width, int32\_t height)

**Description**

Sets the size for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t width | 
Width value (in px).

Default value: **0**, in px. The value must be greater than or equal to 0. If a negative value is passed, [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t height | 

Height value (in px).

Default value: **0**, in px. The value must be greater than or equal to 0. If a negative value is passed, [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetSize()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetSize(ArkUI\_RenderNodeHandle node, int32\_t\* width, int32\_t\* height)

**Description**

Obtains the size of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* width | 
Pointer used to store the width value (in px).

Default value: **0**, in px.

 |
| int32\_t\* height | 

Pointer used to store the height value (in px).

Default value: **0**, in px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetPosition()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPosition(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)

**Description**

Sets the position coordinates for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t x | 
X-coordinate (in px).

Default value: **0**, in px.

 |
| int32\_t y | 

Y-coordinate (in px).

Default value: **0**, in px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetPosition()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPosition(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)

**Description**

Obtains the position coordinates of the render node. The coordinates are the position offset of the render node relative to its parent node after the layout. The unit is px. The coordinates are the result after the parent node lays out the node. Therefore, the **offset** attribute that takes effect after the layout and the **position** attribute that does not participate in the layout do not affect the coordinates.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* x | 
Pointer used to store the x-coordinate (in px).

Default value: **0**, in px.

 |
| int32\_t\* y | 

Pointer used to store the y-coordinate (in px).

Default value: **0**, in px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetPivot()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetPivot(ArkUI\_RenderNodeHandle node, float x, float y)

**Description**

Sets the pivot point for the transformation of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float x | 
X-coordinate of the pivot point. Standard value range: 0.0–1.0.

Default value: **0.5**.

 |
| float y | 

Y-coordinate of the pivot point. Standard value range: 0.0–1.0.

Default value: **0.5**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetPivot()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetPivot(ArkUI\_RenderNodeHandle node, float\* x, float\* y)

**Description**

Obtains the pivot point coordinates of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* x | 
Pointer used to store the x-coordinate of the pivot point.

Default value: **0.5**.

 |
| float\* y | 

Pointer used to store the y-coordinate of the pivot point.

Default value: **0.5**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetScale()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetScale(ArkUI\_RenderNodeHandle node, float x, float y)

**Description**

Sets the scale factors for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float x | 
Scale factor on the x-axis.

Default value: **1**.

 |
| float y | 

Scale factor on the y-axis.

Default value: **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetScale()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetScale(ArkUI\_RenderNodeHandle node, float\* x, float\* y)

**Description**

Obtains the scale factors of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* x | 
Pointer used to store the scale factor on the x-axis.

Default value: **1**.

 |
| float\* y | 

Pointer used to store the scale factor on the y-axis.

Default value: **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetTranslation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTranslation(ArkUI\_RenderNodeHandle node, float x, float y)

**Description**

Sets the translation offset for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float x | 
Horizontal translation offset (in pixels).

Default value: **0**.

 |
| float y | 

Vertical translation offset (in pixels).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetTranslation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetTranslation(ArkUI\_RenderNodeHandle node, float\* x, float\* y)

**Description**

Obtains the translation offset of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* x | 
Pointer used to store the horizontal translation offset.

Default value: **0**.

 |
| float\* y | 

Pointer used to store the vertical translation offset.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRotation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetRotation(ArkUI\_RenderNodeHandle node, float x, float y, float z)

**Description**

Sets the rotation angles for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float x | 
Rotation angle around the x-axis (in degrees).

Default value: **0**.

 |
| float y | 

Rotation angle around the y-axis (in degrees).

Default value: **0**.

 |
| float z | 

Rotation angle around the z-axis (in degrees).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetRotation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetRotation(ArkUI\_RenderNodeHandle node, float\* x, float\* y, float\* z)

**Description**

Obtains the rotation angles of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* x | 
Pointer used to store the rotation angle around the x-axis (in degrees).

Default value: **0**.

 |
| float\* y | 

Pointer used to store the rotation angle around the y-axis (in degrees).

Default value: **0**.

 |
| float\* z | 

Pointer used to store the rotation angle around the z-axis (in degrees).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetTransform()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetTransform(ArkUI\_RenderNodeHandle node, float\* matrix)

**Description**

Sets the transformation matrix for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* matrix | Float array of 4x4 transformation matrix (16 consecutive values). |

The transformation matrix must be provided as 16 consecutive float values in row-major order:

\[m00, m01, m02, m03,

m10, m11, m12, m13,

m20, m21, m22, m23,

m30, m31, m32, m33\]

The matrix is represented as follows:

| m00 m01 m02 m03 |

| m10 m11 m12 m13 |

| m20 m21 m22 m23 |

| m30 m31 m32 m33 |

Matrix components:

| Matrix Element | Description |
| :-- | :-- |
| m00 | Scale value for the x-axis. The default value is **1** in the identity matrix. |
| m01 | Second value, affected by rotation or skewing around x, y, z axes. |
| m02 | Third value, affected by rotation around x, y, z axes. |
| m03 | Fourth value, affected by perspective projection. |
| m10 | Fifth value, affected by rotation or skewing around x, y, z axes. |
| m11 | Scale value for the y-axis. The default value is **1** in the identity matrix. |
| m12 | Seventh value, affected by rotation around x, y, z axes. |
| m13 | Eighth value, affected by perspective projection. |
| m20 | Ninth value, affected by rotation around x, y, z axes. |
| m21 | Tenth value, affected by rotation around x, y, z axes. |
| m22 | Scale value for the z-axis. The default value is **1** in the identity matrix. |
| m23 | Twelfth value, affected by perspective projection. |
| m30 | Translation value for the x-axis (in px). The default value is **0** in the identity matrix. |
| m31 | Translation value for the y-axis (in px). The default value is **0** in the identity matrix. |
| m32 | Translation value for the z-axis (in px). The default value is **0** in the identity matrix. |
| m33 | Valid in homogeneous coordinates, producing perspective projection effects. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetShadowColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t color)

**Description**

Sets the shadow color for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| uint32\_t color | 
ARGB color value (32-bit unsigned integer).

Default value: **0x00000000**.

**Description of color byte layout**:

\- Bits 24-31: alpha channel (0x00 for fully transparent, 0xFF for fully opaque).

\- Bits 16-23: red channel.

\- Bits 8-15: green channel.

\- Bits 0-7: blue channel.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetShadowColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowColor(ArkUI\_RenderNodeHandle node, uint32\_t\* color)

**Description**

Obtains the shadow color of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| uint32\_t\* color | 
Integer pointer used to store the obtained RGBA color value.

Default value: **0xFF000000**.

**Description of color byte layout**:

\- Bits 24-31: alpha channel (0x00 for fully transparent, 0xFF for fully opaque).

\- Bits 16-23: red channel.

\- Bits 8-15: green channel.

\- Bits 0-7: blue channel.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetShadowOffset()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y)

**Description**

Sets the shadow offset for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t x | 
Horizontal offset (in pixels).

Default value: **0**.

 |
| int32\_t y | 

Vertical offset (in pixels).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetShadowOffset()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowOffset(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y)

**Description**

Obtains the shadow offset of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* x | 
Pointer used to store the horizontal offset.

Default value: **0**, in px.

 |
| int32\_t\* y | 

Pointer used to store the vertical offset.

Default value: **0**, in px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetShadowAlpha()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowAlpha(ArkUI\_RenderNodeHandle node, float alpha)

**Description**

Sets the shadow alpha (transparency) for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float alpha | 
Shadow alpha value (0.0–1.0).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetShadowAlpha()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowAlpha(ArkUI\_RenderNodeHandle node, float\* alpha)

**Description**

Obtains the shadow alpha (transparency) of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* alpha | 
Pointer used to store the shadow alpha value.

Default value: **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetShadowElevation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowElevation(ArkUI\_RenderNodeHandle node, float elevation)

**Description**

Sets the shadow elevation for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float elevation | 
Elevation.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetShadowElevation()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowElevation(ArkUI\_RenderNodeHandle node, float\* elevation)

**Description**

Obtains the shadow elevation of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* elevation | 
Pointer used to store the elevation value.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetShadowRadius()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetShadowRadius(ArkUI\_RenderNodeHandle node, float radius)

**Description**

Sets the shadow radius for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float radius | 
Radius value.

Default value: **0**. The value must be greater than or equal to 0. If a negative value is passed, [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetShadowRadius()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetShadowRadius(ArkUI\_RenderNodeHandle node, float\* radius)

**Description**

Obtains the shadow radius of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float\* radius | 
Pointer used to store the radius value.

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\* borderStyle)

**Description**

Sets the border style for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderStyleOption](../../structs/arkui-nodeborderstyleoption/document.md)\* borderStyle | 
Pointer to the border style.

Default value in the struct pointer: [ARKUI\_BORDER\_STYLE\_SOLID](../native-type-h/document.md#arkui_borderstyle).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBorderStyle()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderStyle(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderStyleOption\*\* borderStyle)

**Description**

Obtains the border style of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderStyleOption](../../structs/arkui-nodeborderstyleoption/document.md)\*\* borderStyle | 
Pointer used to store the border style.

Default value in the struct pointer: [ARKUI\_BORDER\_STYLE\_SOLID](../native-type-h/document.md#arkui_borderstyle).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\* borderWidth)

**Description**

Sets the border width for the render node. The border width must be smaller than the node size.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderWidthOption](../../structs/arkui-nodeborderwidthoption/document.md)\* borderWidth | 
Pointer to the border width.

Default value in the struct pointer: **0**. Unit: px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBorderWidth()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderWidth(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderWidthOption\*\* borderWidth)

**Description**

Obtains the border width of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderWidthOption](../../structs/arkui-nodeborderwidthoption/document.md)\*\* borderWidth | 
Pointer used to store the border width.

Default value in the struct pointer: **0**. Unit: px.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBorderColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\* borderColor)

**Description**

Sets the border color for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderColorOption](../../structs/arkui-nodebordercoloroption/document.md)\* borderColor | 
Pointer to the border color.

Default value in the struct pointer: **0x00000000**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBorderColor()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderColor(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderColorOption\*\* borderColor)

**Description**

Obtains the border color of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderColorOption](../../structs/arkui-nodebordercoloroption/document.md)\*\* borderColor | 
Pointer used to store the border color.

Default value in the struct pointer: **0x00000000**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBorderRadius()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\* borderRadius)

**Description**

Sets the border corner radius for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderRadiusOption](../../structs/arkui-nodeborderradiusoption/document.md)\* borderRadius | 
Pointer to the border radius.

Default value in the struct pointer: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBorderRadius()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBorderRadius(ArkUI\_RenderNodeHandle node, ArkUI\_NodeBorderRadiusOption\*\* borderRadius)

**Description**

Obtains the border corner radius of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_NodeBorderRadiusOption](../../structs/arkui-nodeborderradiusoption/document.md)\*\* borderRadius | 
Pointer used to store the border corner radius.

Default value in the struct pointer: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetMask()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMask(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeMaskOption\* mask)

**Description**

Applies a mask to the render node using the mask configuration.

The mask is created as follows:

1.  Add brightness and a linear color filter to the mask layer.
2.  Draw the mask graphic under this filter.
3.  Use the original node image as the source color and the mask graphic as the target color, and blend them into a mask image using the [BlendMode.SRC\_IN](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/enums/document.md#blendmode) API.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md)\* mask | Pointer to the mask configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetClip()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetClip(ArkUI\_RenderNodeHandle node, ArkUI\_RenderNodeClipOption\* clip)

**Description**

Applies clipping to the render node using the clipping configuration.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* clip | Pointer to the clipping configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetMarkNodeGroup()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetMarkNodeGroup(ArkUI\_RenderNodeHandle node, bool markNodeGroup)

**Description**

Marks whether to prioritize drawing the node and its child nodes.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| bool markNodeGroup | 
Whether to prioritize drawing the node and its child nodes.

**true**: Enable drawing priority. **false**: Disable drawing priority.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetBounds()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetBounds(ArkUI\_RenderNodeHandle node, int32\_t x, int32\_t y, int32\_t width, int32\_t height)

**Description**

Sets the bounds for the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t x | 
X-coordinate of the upper left corner of the bounds, in pixels.

Default value: **0**.

 |
| int32\_t y | 

Y-coordinate of the upper left corner of the bounds, in pixels.

Default value: **0**.

 |
| int32\_t width | 

Width of the bounds (in pixels).

Default value: **0**. The value must be greater than or equal to 0. If a negative value is passed, [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t height | 

Height of the bounds (in pixels).

Default value: **0**. The value must be greater than or equal to 0. If a negative value is passed, [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](../native-type-h/document.md#arkui_errorcode) if the parameter value is out of range.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetBounds()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetBounds(ArkUI\_RenderNodeHandle node, int32\_t\* x, int32\_t\* y, int32\_t\* width, int32\_t\* height)

**Description**

Obtains the bounds of the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| int32\_t\* x | 
Pointer used to store the x-coordinate of the upper left corner of the bounds, in pixels.

Default value: **0**.

 |
| int32\_t\* y | 

Pointer used to store the y-coordinate of the upper left corner of the bounds, in pixels.

Default value: **0**.

 |
| int32\_t\* width | 

Pointer used to store the width of the bounds (in pixels).

Default value: **0**.

 |
| int32\_t\* height | 

Pointer used to store the height of the bounds (in pixels).

Default value: **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetDrawRegion()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetDrawRegion(ArkUI\_RenderNodeHandle node, float x, float y, float w, float h)

**Description**

Sets the drawing region for the render node. This drawing region is mainly used to address drawing issues caused by exceeding boundaries. When possible, set the size according to the actual drawing range.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| float x | X-coordinate of the upper left corner of the bounds, in pixels. |
| float y | Y-coordinate of the upper left corner of the bounds, in pixels. |
| float w | Width of the bounds (in pixels). |
| float h | Height of the bounds (in pixels). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachContentModifier(ArkUI\_RenderNodeHandle node, ArkUI\_RenderContentModifierHandle modifier)

**Description**

Attaches a content modifier to the render node.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md) node | Target render node. |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Content modifier. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE](../native-type-h/document.md#arkui_errorcode) if the target node originates from a FrameNode. This specification is supported since API version 22.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier()

ArkUI\_RenderContentModifierHandle OH\_ArkUI\_RenderNodeUtils\_CreateContentModifier()

**Description**

Creates a content modifier.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) | Content modifier. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeContentModifier()

void OH\_ArkUI\_RenderNodeUtils\_DisposeContentModifier(ArkUI\_RenderContentModifierHandle modifier)

**Description**

Disposes of the content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Content modifier. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachFloatProperty()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatPropertyHandle property)

**Description**

Attaches a float property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_FloatPropertyHandle](../../structs/arkui-floatpropertyhandle/document.md) property | Float property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachVector2Property()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2Property(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2PropertyHandle property)

**Description**

Attaches a 2D vector property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_Vector2PropertyHandle](../../structs/arkui-vector2propertyhandle/document.md) property | 2D vector property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachColorProperty()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorPropertyHandle property)

**Description**

Attaches a color property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_ColorPropertyHandle](../../structs/arkui-colorpropertyhandle/document.md) property | Color property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachFloatAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_FloatAnimatablePropertyHandle property)

**Description**

Attaches an animatable float property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_FloatAnimatablePropertyHandle](../../structs/arkui-floatanimatablepropertyhandle/document.md) property | Animatable float property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachVector2AnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_Vector2AnimatablePropertyHandle property)

**Description**

Attaches an animatable 2D vector property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_Vector2AnimatablePropertyHandle](../../structs/arkui-vector2animatablepropertyhandle/document.md) property | Animatable 2D vector property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty()

int32\_t OH\_ArkUI\_RenderNodeUtils\_AttachColorAnimatableProperty(ArkUI\_RenderContentModifierHandle modifier, ArkUI\_ColorAnimatablePropertyHandle property)

**Description**

Attaches an animatable color property to the target content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| [ArkUI\_ColorAnimatablePropertyHandle](../../structs/arkui-coloranimatablepropertyhandle/document.md) property | Animatable color property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateFloatProperty()

ArkUI\_FloatPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatProperty(float value)

**Description**

Creates a float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_FloatPropertyHandle](../../structs/arkui-floatpropertyhandle/document.md) | Float property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float value)

**Description**

Sets the value of the float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatPropertyHandle](../../structs/arkui-floatpropertyhandle/document.md) property | Float property. |
| float value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetFloatPropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatPropertyValue(ArkUI\_FloatPropertyHandle property, float\* value)

**Description**

Obtains the value of the float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatPropertyHandle](../../structs/arkui-floatpropertyhandle/document.md) property | Float property. |
| float\* value | Pointer used to store the property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeFloatProperty()

void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatProperty(ArkUI\_FloatPropertyHandle property)

**Description**

Disposes of the float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatPropertyHandle](../../structs/arkui-floatpropertyhandle/document.md) property | Float property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateVector2Property()

ArkUI\_Vector2PropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2Property(float x, float y)

**Description**

Creates a 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float x | X-coordinate of the property. |
| float y | Y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_Vector2PropertyHandle](../../structs/arkui-vector2propertyhandle/document.md) | 2D vector property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetVector2PropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float x, float y)

**Description**

Sets the value of the 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2PropertyHandle](../../structs/arkui-vector2propertyhandle/document.md) property | 2D vector property. |
| float x | X-coordinate of the property. |
| float y | Y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetVector2PropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2PropertyValue(ArkUI\_Vector2PropertyHandle property, float\* x, float\* y)

**Description**

Obtains the value of the 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2PropertyHandle](../../structs/arkui-vector2propertyhandle/document.md) property | 2D vector property. |
| float\* x | Pointer used to store the x-coordinate of the property. |
| float\* y | Pointer used to store the y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeVector2Property()

void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2Property(ArkUI\_Vector2PropertyHandle property)

**Description**

Disposes of the 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2PropertyHandle](../../structs/arkui-vector2propertyhandle/document.md) property | 2D vector property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateColorProperty()

ArkUI\_ColorPropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorProperty(uint32\_t value)

**Description**

Creates a color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ColorPropertyHandle](../../structs/arkui-colorpropertyhandle/document.md) | Color property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetColorPropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t value)

**Description**

Sets the value of the color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorPropertyHandle](../../structs/arkui-colorpropertyhandle/document.md) property | Color property. |
| uint32\_t value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetColorPropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorPropertyValue(ArkUI\_ColorPropertyHandle property, uint32\_t\* value)

**Description**

Obtains the value of the color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorPropertyHandle](../../structs/arkui-colorpropertyhandle/document.md) property | Color property. |
| uint32\_t\* value | Pointer used to store the property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeColorProperty()

void OH\_ArkUI\_RenderNodeUtils\_DisposeColorProperty(ArkUI\_ColorPropertyHandle property)

**Description**

Disposes of the color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorPropertyHandle](../../structs/arkui-colorpropertyhandle/document.md) property | Color property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty()

ArkUI\_FloatAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateFloatAnimatableProperty(float value)

**Description**

Creates an animatable float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_FloatAnimatablePropertyHandle](../../structs/arkui-floatanimatablepropertyhandle/document.md) | Animatable float property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float value)

**Description**

Sets the value of the animatable float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatAnimatablePropertyHandle](../../structs/arkui-floatanimatablepropertyhandle/document.md) property | Animatable float property. |
| float value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetFloatAnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetFloatAnimatablePropertyValue(ArkUI\_FloatAnimatablePropertyHandle property, float\* value)

**Description**

Obtains the value of the animatable float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatAnimatablePropertyHandle](../../structs/arkui-floatanimatablepropertyhandle/document.md) property | Animatable float property. |
| float\* value | Pointer used to store the property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeFloatAnimatableProperty()

void OH\_ArkUI\_RenderNodeUtils\_DisposeFloatAnimatableProperty(ArkUI\_FloatAnimatablePropertyHandle property)

**Description**

Disposes of the animatable float property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_FloatAnimatablePropertyHandle](../../structs/arkui-floatanimatablepropertyhandle/document.md) property | Animatable float property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty()

ArkUI\_Vector2AnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateVector2AnimatableProperty(float x, float y)

**Description**

Creates an animatable 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float x | X-coordinate of the property. |
| float y | Y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_Vector2AnimatablePropertyHandle](../../structs/arkui-vector2animatablepropertyhandle/document.md) | Animatable 2D vector property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float x, float y)

**Description**

Sets the value of the animatable 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2AnimatablePropertyHandle](../../structs/arkui-vector2animatablepropertyhandle/document.md) property | Animatable 2D vector property. |
| float x | X-coordinate of the property. |
| float y | Y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetVector2AnimatablePropertyValue(ArkUI\_Vector2AnimatablePropertyHandle property, float\* x, float\* y)

**Description**

Obtains the value of the animatable 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2AnimatablePropertyHandle](../../structs/arkui-vector2animatablepropertyhandle/document.md) property | Animatable 2D vector property. |
| float\* x | Pointer used to store the x-coordinate of the property. |
| float\* y | Pointer used to store the y-coordinate of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeVector2AnimatableProperty()

void OH\_ArkUI\_RenderNodeUtils\_DisposeVector2AnimatableProperty(ArkUI\_Vector2AnimatablePropertyHandle property)

**Description**

Disposes of the animatable 2D vector property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_Vector2AnimatablePropertyHandle](../../structs/arkui-vector2animatablepropertyhandle/document.md) property | Animatable 2D vector property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty()

ArkUI\_ColorAnimatablePropertyHandle OH\_ArkUI\_RenderNodeUtils\_CreateColorAnimatableProperty(uint32\_t value)

**Description**

Creates an animatable color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ColorAnimatablePropertyHandle](../../structs/arkui-coloranimatablepropertyhandle/document.md) | Animatable color property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t value)

**Description**

Sets the value of the animatable color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorAnimatablePropertyHandle](../../structs/arkui-coloranimatablepropertyhandle/document.md) property | Animatable color property. |
| uint32\_t value | Property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetColorAnimatablePropertyValue(ArkUI\_ColorAnimatablePropertyHandle property, uint32\_t\* value)

**Description**

Obtains the value of the animatable color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorAnimatablePropertyHandle](../../structs/arkui-coloranimatablepropertyhandle/document.md) property | Animatable color property. |
| uint32\_t\* value | Pointer used to store the property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeColorAnimatableProperty()

void OH\_ArkUI\_RenderNodeUtils\_DisposeColorAnimatableProperty(ArkUI\_ColorAnimatablePropertyHandle property)

**Description**

Disposes of the animatable color property.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ColorAnimatablePropertyHandle](../../structs/arkui-coloranimatablepropertyhandle/document.md) property | Animatable color property. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw()

int32\_t OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw(ArkUI\_RenderContentModifierHandle modifier, void\* userData, void (\*callback)(ArkUI\_DrawContext\* context, void\* userData))

**Description**

Sets the **onDraw** callback function for the content modifier.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderContentModifierHandle](../../structs/arkui-rendercontentmodifierhandle/document.md) modifier | Target content modifier. |
| void\* userData | Custom data to be passed to the callback. |
| void (callback)([ArkUI\_DrawContext](../../structs/arkui-drawcontext/document.md) context, void\* userData) | Callback for receiving drawing events. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRectShapeOption()

ArkUI\_RectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRectShapeOption()

**Description**

Creates a rectangle shape option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption](../../structs/arkui-rectshapeoption/document.md)\* | Pointer to the rectangle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeRectShapeOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeRectShapeOption(ArkUI\_RectShapeOption\* option)

**Description**

Disposes of the rectangle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption](../../structs/arkui-rectshapeoption/document.md)\* option | Pointer to the rectangle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRectShapeOptionEdgeValue()

void OH\_ArkUI\_RenderNodeUtils\_SetRectShapeOptionEdgeValue(ArkUI\_RectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)

**Description**

Sets the edge value for the rectangle shape option. When the left and top boundaries are set to negative values, part of the content that exceeds the node may fail to draw due to the layer overlay effect involved in display.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption](../../structs/arkui-rectshapeoption/document.md)\* option | Pointer to the rectangle shape option. |
| float edgeValue | Edge value to set. |
| [ArkUI\_EdgeDirection](../native-type-h/document.md#arkui_edgedirection) direction | Edge direction to apply the value. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption()

ArkUI\_NodeBorderStyleOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderStyleOption()

**Description**

Creates a node border style option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderStyleOption](../../structs/arkui-nodeborderstyleoption/document.md)\* | Pointer to the node border style option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderStyleOption(ArkUI\_NodeBorderStyleOption\* option)

**Description**

Disposes of the node border style option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderStyleOption](../../structs/arkui-nodeborderstyleoption/document.md)\* option | Pointer to the node border style option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle()

void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderStyleOptionEdgeStyle(ArkUI\_NodeBorderStyleOption\* option, ArkUI\_BorderStyle edgeStyle, ArkUI\_EdgeDirection direction)

**Description**

Sets the edge style for the node border style option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderStyleOption](../../structs/arkui-nodeborderstyleoption/document.md)\* option | Pointer to the node border style option. |
| [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle) edgeStyle | Edge border style value of the node border style option. |
| [ArkUI\_EdgeDirection](../native-type-h/document.md#arkui_edgedirection) direction | Edge direction. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption()

ArkUI\_NodeBorderWidthOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderWidthOption()

**Description**

Creates a node border width option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderWidthOption](../../structs/arkui-nodeborderwidthoption/document.md)\* | Pointer to the node border width option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderWidthOption(ArkUI\_NodeBorderWidthOption\* option)

**Description**

Disposes of the node border width option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderWidthOption](../../structs/arkui-nodeborderwidthoption/document.md)\* option | Pointer to the node border width option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth()

void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderWidthOptionEdgeWidth(ArkUI\_NodeBorderWidthOption\* option, float edgeWidth, ArkUI\_EdgeDirection direction)

**Description**

Sets the edge width for the node border width option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderWidthOption](../../structs/arkui-nodeborderwidthoption/document.md)\* option | Pointer to the node border width option. |
| float edgeWidth | 
Edge width of the node border width option.

Value range: \[0, +∞).

 |
| [ArkUI\_EdgeDirection](../native-type-h/document.md#arkui_edgedirection) direction | Edge direction. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption()

ArkUI\_NodeBorderColorOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderColorOption()

**Description**

Creates a node border color option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderColorOption](../../structs/arkui-nodebordercoloroption/document.md)\* | Pointer to the node border color option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderColorOption(ArkUI\_NodeBorderColorOption\* option)

**Description**

Disposes of the node border color option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderColorOption](../../structs/arkui-nodebordercoloroption/document.md)\* option | Pointer to the node border color option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor()

void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderColorOptionEdgeColor(ArkUI\_NodeBorderColorOption\* option, uint32\_t edgeColor, ArkUI\_EdgeDirection direction)

**Description**

Sets the edge color for the node border color option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderColorOption](../../structs/arkui-nodebordercoloroption/document.md)\* option | Pointer to the node border color option. |
| uint32\_t edgeColor | Edge color of the node border color option. |
| [ArkUI\_EdgeDirection](../native-type-h/document.md#arkui_edgedirection) direction | Edge direction. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderRadiusOption()

ArkUI\_NodeBorderRadiusOption\* OH\_ArkUI\_RenderNodeUtils\_CreateNodeBorderRadiusOption()

**Description**

Creates a node border radius option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderRadiusOption](../../structs/arkui-nodeborderradiusoption/document.md)\* | Pointer to the node border radius option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderRadiusOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeNodeBorderRadiusOption(ArkUI\_NodeBorderRadiusOption\* option)

**Description**

Disposes of the node border radius option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderRadiusOption](../../structs/arkui-nodeborderradiusoption/document.md)\* option | Pointer to the node border radius option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderRadiusOptionCornerRadius()

void OH\_ArkUI\_RenderNodeUtils\_SetNodeBorderRadiusOptionCornerRadius(ArkUI\_NodeBorderRadiusOption\* option, uint32\_t cornerRadius, ArkUI\_CornerDirection direction)

**Description**

Sets the corner radius for the node border radius option. Note that the input parameter **cornerRadius** is of type uint32\_t, and only positive integers are supported.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeBorderRadiusOption](../../structs/arkui-nodeborderradiusoption/document.md)\* option | Pointer to the node border radius option. |
| uint32\_t cornerRadius | Corner radius of the node border radius option. |
| [ArkUI\_CornerDirection](../native-type-h/document.md#arkui_cornerdirection) direction | Edge direction. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateCircleShapeOption()

ArkUI\_CircleShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCircleShapeOption()

**Description**

Creates a circle shape option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* | Pointer to the circle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeCircleShapeOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeCircleShapeOption(ArkUI\_CircleShapeOption\* option)

**Description**

Disposes of the circle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* option | Pointer to the circle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterX()

void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterX(ArkUI\_CircleShapeOption\* option, float centerX)

**Description**

Sets the x-coordinate of the center for the circle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* option | Pointer to the circle shape option. |
| float centerX | X-coordinate of the center of the circle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterY()

void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionCenterY(ArkUI\_CircleShapeOption\* option, float centerY)

**Description**

Sets the y-coordinate of the center for the circle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* option | Pointer to the circle shape option. |
| float centerY | Y-coordinate of the center of the circle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionRadius()

void OH\_ArkUI\_RenderNodeUtils\_SetCircleShapeOptionRadius(ArkUI\_CircleShapeOption\* option, float radius)

**Description**

Sets the radius value for the circle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* option | Pointer to the circle shape option. |
| float radius | Radius, in pixels. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRoundRectShapeOption()

ArkUI\_RoundRectShapeOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRoundRectShapeOption()

**Description**

Creates a rounded rectangle shape option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption](../../structs/arkui-roundrectshapeoption/document.md)\* | Pointer to the rounded rectangle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeRoundRectShapeOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeRoundRectShapeOption(ArkUI\_RoundRectShapeOption\* option)

**Description**

Disposes of the rounded rectangle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption](../../structs/arkui-roundrectshapeoption/document.md)\* option | Pointer to the rounded rectangle shape option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionEdgeValue()

void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionEdgeValue(ArkUI\_RoundRectShapeOption\* option, float edgeValue, ArkUI\_EdgeDirection direction)

**Description**

Sets the edge values for the rounded rectangle shape option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption](../../structs/arkui-roundrectshapeoption/document.md)\* option | Pointer to the rounded rectangle shape option. |
| float edgeValue | Edge value to set. |
| [ArkUI\_EdgeDirection](../native-type-h/document.md#arkui_edgedirection) direction | Edge direction to apply the value. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionCornerXY()

void OH\_ArkUI\_RenderNodeUtils\_SetRoundRectShapeOptionCornerXY(ArkUI\_RoundRectShapeOption\* option, float x, float y, ArkUI\_CornerDirection direction)

**Description**

Sets the coordinates for the target corner.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption](../../structs/arkui-roundrectshapeoption/document.md)\* option | Pointer to the rounded rectangle shape option. |
| float x | X-coordinate of the target corner, in pixels. |
| float y | Y-coordinate of the target corner, in pixels. |
| [ArkUI\_CornerDirection](../native-type-h/document.md#arkui_cornerdirection) direction | Direction of the target corner. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateCommandPathOption()

ArkUI\_CommandPathOption\* OH\_ArkUI\_RenderNodeUtils\_CreateCommandPathOption()

**Description**

Creates a custom drawing path option.

**Since**: 20

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CommandPathOption](../../structs/arkui-commandpathoption/document.md)\* | Pointer to the custom drawing path option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeCommandPathOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeCommandPathOption(ArkUI\_CommandPathOption\* option)

**Description**

Disposes of the custom drawing path option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CommandPathOption](../../structs/arkui-commandpathoption/document.md)\* option | Pointer to the custom drawing path option. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetCommandPathOptionCommands()

void OH\_ArkUI\_RenderNodeUtils\_SetCommandPathOptionCommands(ArkUI\_CommandPathOption\* option, char\* commands)

**Description**

Sets the command values for the custom drawing path option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CommandPathOption](../../structs/arkui-commandpathoption/document.md)\* option | Pointer to the custom drawing path option. |
| char\* commands | Command values. The input parameter format is [<path>shape](../../../arkts-components/images-and-videos/svg-tags/document.md#basic-shapes). |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRectShape()

ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRectShape(ArkUI\_RectShapeOption\* shape)

**Description**

Creates a mask from a rectangle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption\*](../../structs/arkui-rectshapeoption/document.md) shape | Pointer to the rectangle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRoundRectShape()

ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)

**Description**

Creates a mask from a rounded rectangle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption\*](../../structs/arkui-roundrectshapeoption/document.md) shape | Pointer to the rounded rectangle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCircleShape()

ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)

**Description**

Creates a mask from a circle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption\*](../../structs/arkui-circleshapeoption/document.md) shape | Pointer to the circle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromOvalShape()

ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)

**Description**

Creates a mask from an oval shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption\*](../../structs/arkui-rectshapeoption/document.md) shape | Pointer to the oval shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCommandPath()

ArkUI\_RenderNodeMaskOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeMaskOptionFromCommandPath(ArkUI\_CommandPathOption\* path)

**Description**

Creates a mask from a custom drawing path.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CommandPathOption\*](../../structs/arkui-commandpathoption/document.md) path | Pointer to the custom drawing path option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md) | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeMaskOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeMaskOption(ArkUI\_RenderNodeMaskOption\* option)

**Description**

Disposes of the render node mask option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption\*](../../structs/arkui-rendernodemaskoption/document.md) option | Pointer to the render node mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionFillColor()

void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionFillColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t fillColor)

**Description**

Sets the fill color for the render node mask option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md)\* mask | Pointer to the render node mask. |
| uint32\_t fillColor | Fill color of the mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeColor()

void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeColor(ArkUI\_RenderNodeMaskOption\* mask, uint32\_t strokeColor)

**Description**

Sets the stroke color for the render node mask option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md)\* mask | Pointer to the render node mask. |
| uint32\_t strokeColor | Stroke color of the mask. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeWidth()

void OH\_ArkUI\_RenderNodeUtils\_SetRenderNodeMaskOptionStrokeWidth(ArkUI\_RenderNodeMaskOption\* mask, float strokeWidth)

**Description**

Sets the stroke width for the render node mask option. Drawing with the corresponding width is performed centered on the border path.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeMaskOption](../../structs/arkui-rendernodemaskoption/document.md)\* mask | Pointer to the render node mask. |
| float strokeWidth | 
Stroke width of the mask.

Value range: (0, +∞). If the value is a negative number or 0, the stroke width is set to 1 pixel during drawing.

 |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRectShape()

ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRectShape(ArkUI\_RectShapeOption\* shape)

**Description**

Creates a render node clip option from a rectangle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption](../../structs/arkui-rectshapeoption/document.md)\* shape | Pointer to the rectangle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRoundRectShape()

ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromRoundRectShape(ArkUI\_RoundRectShapeOption\* shape)

**Description**

Creates a render node clip option from a rounded rectangle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RoundRectShapeOption](../../structs/arkui-roundrectshapeoption/document.md)\* shape | Pointer to the rounded rectangle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCircleShape()

ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCircleShape(ArkUI\_CircleShapeOption\* shape)

**Description**

Creates a render node clip option from a circle shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CircleShapeOption](../../structs/arkui-circleshapeoption/document.md)\* shape | Pointer to the circle shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromOvalShape()

ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromOvalShape(ArkUI\_RectShapeOption\* shape)

**Description**

Creates a render node clip option from an oval shape.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RectShapeOption](../../structs/arkui-rectshapeoption/document.md)\* shape | Pointer to the oval shape option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCommandPath()

ArkUI\_RenderNodeClipOption\* OH\_ArkUI\_RenderNodeUtils\_CreateRenderNodeClipOptionFromCommandPath(ArkUI\_CommandPathOption\* path)

**Description**

Creates a render node clip option from a custom drawing path.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CommandPathOption](../../structs/arkui-commandpathoption/document.md)\* path | Pointer to the custom drawing path option. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeClipOption()

void OH\_ArkUI\_RenderNodeUtils\_DisposeRenderNodeClipOption(ArkUI\_RenderNodeClipOption\* option)

**Description**

Disposes of the render node clip option.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RenderNodeClipOption](../../structs/arkui-rendernodeclipoption/document.md)\* option | Pointer to the render node clip. |

#### \[h2\]OH\_ArkUI\_RenderNodeUtils\_GetRenderNode()

int32\_t OH\_ArkUI\_RenderNodeUtils\_GetRenderNode(ArkUI\_NodeHandle node, ArkUI\_RenderNodeHandle\* renderNode);

**Description**

Obtains the RenderNode of the target node. The target node has been adopted as an affiliated node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to **ArkUI\_NodeHandle**. |
| [ArkUI\_RenderNodeHandle](../../structs/arkui-rendernodehandle/document.md)\* renderNode | Pointer to **ArkUI\_RenderNodeHandle**, which specifies the RenderNode of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../native-type-h/document.md#arkui_errorcode) if C API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_RENDER\_NOT\_ADOPTED\_NODE](../native-type-h/document.md#arkui_errorcode) if this node is not accepted as a child node.

 |
