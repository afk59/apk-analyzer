# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/VnTGJ1G8S2C7ogT1i3wr6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A1BE1D10DD32638496181C8D15CC7786B84D85CF8B23980EF472FD6FE893300)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### BlendMode

Enumerates the blend modes. A blend mode combines two colors (source color and destination color) in a specific way to create a new color. This is commonly used in graphics operations like overlaying, filtering, and masking. The blending process applies the same logic to the red, green, and blue color channels separately. The alpha channel, however, is handled according to the specific definitions of each blend mode.

For brevity, the following abbreviations are used:

**s**: source. **d**: destination. **sa**: source alpha. **da**: destination alpha.

The following abbreviations are used in the calculation result:

**r**: used when the calculation method is the same for the four channels (alpha, red, green, and blue channels). **ra**: used when only the alpha channel is manipulated. **rc**: used when the other three color channels are manipulated.

The table below shows the effect of each blend mode, where the yellow rectangle is the source and the blue circle is the destination.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| CLEAR | 0 | r = 0, sets the destination pixels to fully transparent. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5aH7zIfESfu5M3a5O1W7jQ/en-us_image_0000002537766416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B8DCE92DA8348E236C1C13E52E71A9341CAB481A0919DD4F1C458A1E30401BA) |
| SRC | 1 | r = s (all channels of the result equal those of the source), replaces the destination pixels with the source pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/cxRukZiTTTeVH9qiyc1jhw/en-us_image_0000002537926356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2ABA81DB59445E512A054E9D738555CADFE577C1F971C9806C7D44A05994AEE5) |
| DST | 2 | r = d (all channels of the result equal those of the destination), keeps the destination pixels unchanged. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/RYp7Sv1fRnqch9unrvDNeQ/en-us_image_0000002568686133.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFE30D6E781F47A681D21BFAF96F621004429AA23F82FE404264EEF1398521F3) |
| SRC\_OVER | 3 | r = s + (1 - sa) \* d, draws the source pixels over the destination pixels, considering the source's transparency. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/qDKb58GjT0CsKuQ_jUUASw/en-us_image_0000002568766143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D253F22601384646A2F8AC1A587105184F9BC98E20AAB1D70F16607F3F35314B) |
| DST\_OVER | 4 | r = d + (1 - da) \* s, draws the destination pixels over the source pixels, considering the destination's transparency. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/U___JwOWSEqbKI7oAqVChg/en-us_image_0000002537766418.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=414997E4B9968893515F9D56C6FEE0AE735DD75349037546DA765881FC656EBD) |
| SRC\_IN | 5 | r = s \* da, retains only the intersection of the source pixels with the opaque parts of the destination. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/jSjA2l3USNWmwbgTuM4LxA/en-us_image_0000002537926358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD55083A7937360247FF38613A21322397A888474B9A8123B8A8DA2FC7E8D276) |
| DST\_IN | 6 | r = d \* sa, retains only the intersection of the destination pixels with the opaque parts of the source. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8wocfBRDRfGm-zSQcU2yVw/en-us_image_0000002568686135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6659EE331DCABCF2B8C1535F414D6694B268A6C23A066D0374E57BF8712FDF43) |
| SRC\_OUT | 7 | r = s \* (1 - da), retains the parts of the source pixels that do not overlap with the destination. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/YHI4Nb6dRmS_LJ1m1p1QNA/en-us_image_0000002568766145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F595B00C6F3BBFFDBC36C795CA660BE3CC863BA7479D82D9E746190D3153961F) |
| DST\_OUT | 8 | r = d \* (1 - sa), retains the parts of the destination pixels that do not overlap with the source. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/fcg7q3o8SMiLpPjdCdts4A/en-us_image_0000002568766145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B0CFBBCD87B57DD775A139B64CF18DE6EDD7A112E3D9908AA6758777F461691) |
| SRC\_ATOP | 9 | r = s \* da + d \* (1 - sa), covers the destination pixels with the source pixels, showing the source only in the opaque parts of the destination. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/19EVhO08QjWrjARywGprnw/en-us_image_0000002537766420.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E254EB2BF55791E145C4A3B859A6EC8A76D5CE6E9876F65CA3DC501D93B00E0) |
| DST\_ATOP | 10 | r = d \* sa + s \* (1 - da), covers the source pixels with the destination pixels, showing the destination only in the opaque parts of the source. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/WSF-JSa_Q72NEfqmjzwmCA/en-us_image_0000002537926360.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68964C74ACD0D611AEB200C3DD49FC72A74AB96B56E8500E7CF85FEC53C5EE42) |
| XOR | 11 | r = s \* (1 - da) + d \* (1 - sa), shows only the non-overlapping parts of the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/BXCDwNOMQ2-eM8chI_NfPg/en-us_image_0000002568686137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=188A5A737574181714820A9DB76C17B6797F95379CF88616F882AC2065BEF6D8) |
| PLUS | 12 | r = min(s + d, 1), adds the color values of the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/kI1bP9hpQ5KqFnsjAlcnbg/en-us_image_0000002568766147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4021C45155DEB3EB75BC77732ADD05CD89D1A8536ED5178698261CCD544EBCD1) |
| MODULATE | 13 | r = s \* d, multiplies the color values of the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/P4PZ7SszQiiJlrhtVbVVwg/en-us_image_0000002537766422.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14CDB699B46CDC1B97086CD64ED9D6F486AD19627FBADFED757067761643D9D5) |
| SCREEN | 14 | r = s + d - s \* d, inverts the color values of the source and destination pixels, multiplies them, and then inverts the result, typically producing a brighter outcome. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/i9hxRtgeQ7WLCLj1qwG6Lw/en-us_image_0000002537926362.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED4FCD181F66B87D559661E3A95027AB4EEA94008A0CF689A748140887143B9A) |
| OVERLAY | 15 | Selectively applies **MULTIPLY** or **SCREEN** based on the brightness of the destination pixels, enhancing contrast. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/kij5HLy-Tjq1g9l8uhZMXQ/en-us_image_0000002568686139.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C490214EA3D50614EDE6DAA3D3AAC7909A794CF007574C556C2BF96183A8721) |
| DARKEN | 16 | rc = s + d - max(s \* da, d \* sa), ra = s + (1 - sa) \* d, takes the darker color values between the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VNms6ePERJGQaOjRC7AIQg/en-us_image_0000002568766149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A9A0D2BA4EDD8BCF6287BAC3B30DDC96159908EAD84413F6C9AF442EEC32866) |
| LIGHTEN | 17 | rc = s + d - min(s \* da, d \* sa), ra = s + (1 - sa) \* d, takes the lighter color values between the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/XH_Rvm5HRya9WDoWiNkg_g/en-us_image_0000002537766424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4CB75DFB35C120C07F2D1373278047C59149005C172547B4BEAAE5BC0184832) |
| COLOR\_DODGE | 18 | Brightens the destination pixels by reducing contrast to reflect the source pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BubEkSqRRnG9HaCIdHjSFA/en-us_image_0000002537926364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5317FABC4D7DBCF58F889946FC96CF26E2501560670103C814008D7DB93B218C) |
| COLOR\_BURN | 19 | Darkens the destination pixels by increasing contrast to reflect the source pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/UvEXfE_pSdeScyhZPQB4sg/en-us_image_0000002568686141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE549281EB50E23BD3E13821E65A2F6ADF8DF650252FC3311CD32F890F93644F) |
| HARD\_LIGHT | 20 | Selectively applies **MULTIPLY** or **SCREEN** based on the brightness of the source pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/AFQ0i7oFRleDTve7fpXAmA/en-us_image_0000002568766151.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A325E81B52521455BA5FAA65BEFD02B8E717D41F24502286DC2AB3E6F1BE441C) |
| SOFT\_LIGHT | 21 | Softly brightens or darkens the destination pixels based on the brightness of the source pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/FEYXPoRsQdGK7nt1A87Bpw/en-us_image_0000002537766426.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A829B504E543B506B46B0A3B4D2B9DB57DBC8271E2EFBA6F5CBE3CAF1C3EBE7D) |
| DIFFERENCE | 22 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = s + (1 - sa) \* d, calculates the difference between the color values of the source and destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/9T4oHDhUSqmXjVLfDsN5UA/en-us_image_0000002537766426.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D444837A10E64CB71F6877C121BA7C968557426317C58E832CC3923211FA6C95) |
| EXCLUSION | 23 | rc = s + d - two(s \* d), ra = s + (1 - sa) \* d, similar to **DIFFERENCE** but with lower contrast. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/pSBA1r8pTKWGHD5sA47-Wg/en-us_image_0000002537926366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7C8D2C746F6ACDAD6D8216A534BF18CC5D1EEBF8D40912E4B30B3BD990E73BF) |
| MULTIPLY | 24 | r = s \* (1 - da) + d \* (1 - sa) + s \* d, multiplies the color values of the source and destination pixels, typically resulting in a darker outcome. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/mmQwq6zfTimXW0UaRtAEwA/en-us_image_0000002568686143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=287EE5F988CA5BAD4C6A40FB811AAD6B89D32187B49670ECA80007790C3F74BA) |
| HUE | 25 | Uses the hue of the source pixels and the saturation and brightness of the destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/5OQmOzMlReWptMbUWf5AcQ/en-us_image_0000002568766153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC997EC99A40B2985306E47F827E2FA26BC4B77CA47F49B933974973D417CF2A) |
| SATURATION | 26 | Uses the saturation of the source pixels and the hue and brightness of the destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/hp2P_FhZSaSg9VHXPIvmjw/en-us_image_0000002537766428.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=415F02585E66A9707BBA81AB5EFF2AB20947E60CD6559527A2C25C7E9B14E89F) |
| COLOR | 27 | Uses the hue and saturation of the source pixels and the brightness of the destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/KhDcQihfQcGYVBB7mluG9g/en-us_image_0000002537926368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12958537BDED4EF4D218057FD4DC80448AC18B8BE151BAD56B1B5995D74E9B51) |
| LUMINOSITY | 28 | Uses the brightness of the source pixels and the hue and saturation of the destination pixels. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Zb6WNNurTGWfstKZnxxsaA/en-us_image_0000002568686145.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80885D6CE4C8F97A0D357D7CB5FCEB7847F8B21DFA2CE58C2D0F5FAF245DC93B) |

#### PathMeasureMatrixFlags12+

Enumerates the dimensions of matrix information in path measurement. It is often used in animation scenarios where objects move along a path.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| GET\_POSITION\_MATRIX | 0 | Matrix corresponding to the position information. |
| GET\_TANGENT\_MATRIX | 1 | Matrix corresponding to the tangent information. |
| GET\_POSITION\_AND\_TANGENT\_MATRIX | 2 | Matrix corresponding to the position and tangent information. |

#### SrcRectConstraint12+

Enumerates the constraints on the source rectangle. It is used to specify whether to limit the sampling range within the source rectangle when drawing an image on a canvas.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| STRICT | 0 | The sampling range is strictly confined to the source rectangle, resulting in a slow sampling speed. |
| FAST | 1 | The sampling range is not limited to the source rectangle and can extend beyond it, allowing for a high sampling speed. |

#### ShadowFlag12+

Enumerates the shadow drawing behaviors.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No shadow effect is used. |
| TRANSPARENT\_OCCLUDER | 1 | The occluder is translucent. |
| GEOMETRIC\_ONLY | 2 | Only the geometric shadow effect is used. |
| ALL | 3 | Shadow effects are combined, including the translucent occluder and geometric shadow. |

#### PathOp12+

Enumerates the path operation types. It is often used in path combination and clipping scenarios.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| DIFFERENCE | 0 | Difference operation. |
| INTERSECT | 1 | Intersection operation. |
| UNION | 2 | Union operation. |
| XOR | 3 | XOR operation. |
| REVERSE\_DIFFERENCE | 4 | Reverse difference operation. |

#### PathIteratorVerb18+

Enumerates the path operation types contained in an iterator. It is used to read path operation instructions.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| MOVE | 0 | Sets the start point. |
| LINE | 1 | Adds a line segment. |
| QUAD | 2 | Adds a quadratic Bezier curve for smooth transitions. |
| CONIC | 3 | Adds a conic curve. |
| CUBIC | 4 | Adds a cubic Bezier curve for smooth transitions. |
| CLOSE | 5 | Closes a path. |
| DONE | CLOSE + 1 | The path setting is complete. |

#### TextEncoding

Enumerates the text encoding types.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_ENCODING\_UTF8 | 0 | One byte is used to indicate UTF-8 or ASCII characters. |
| TEXT\_ENCODING\_UTF16 | 1 | Two bytes are used to indicate most Unicode characters. |
| TEXT\_ENCODING\_UTF32 | 2 | Four bytes are used to indicate all Unicode characters. |
| TEXT\_ENCODING\_GLYPH\_ID | 3 | Two bytes are used to indicate the glyph index. |

#### ClipOp12+

Enumerates the canvas clipping modes.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| DIFFERENCE | 0 | Clips a specified area. That is, the difference set is obtained. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/ke3aKSaWRnCjE31wNlcM7g/en-us_image_0000002568766155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2927FCEC84B94A499D433D639811ED0EB5FE74581B9DACA64E10BEC55A2D1BF) |
| INTERSECT | 1 | Retains a specified area. That is, the intersection is obtained. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JTOfLdciQWeuFu7NjDT5CA/en-us_image_0000002537766430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AFF6F5AE587950A19F120A71638BBB62D66D8C20A182109063973AEE58D56AD) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dgQ76roYQEqrY1xc8X5XqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6453AA92CDA6FA605BE8EF4A51C86EF6DDFF8C24B6DCA06B3A0B21BCF342F7D)

The diagrams show the result of cropping a circle based on different enumerated values after a rectangle is cropped in INTERSECT mode. The green area is the final area obtained.

#### FilterMode12+

Enumerates the filter modes.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| FILTER\_MODE\_NEAREST | 0 | Nearest filter mode. |
| FILTER\_MODE\_LINEAR | 1 | Linear filter mode. |

#### PathDirection12+

Enumerates the directions of a closed contour.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| CLOCKWISE | 0 | Adds a closed contour clockwise. |
| COUNTER\_CLOCKWISE | 1 | Adds a closed contour counterclockwise. |

#### PathFillType12+

Enumerates the fill types of a path.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDING | 0 | Specifies that "inside" is computed by a non-zero sum of signed edge crossings. Specifically, draws a point and emits a ray in any direction. A count is used to record the number of intersection points of the ray and path, and the initial count is 0. When encountering a clockwise intersection point (the path passes from the left to the right of the ray), the count increases by 1. When encountering a counterclockwise intersection point (the path passes from the right to the left of the ray), the count decreases by 1. If the final count is not 0, the point is inside the path and needs to be colored. If the final count is 0, the point is not colored. |
| EVEN\_ODD | 1 | Specifies that "inside" is computed by an odd number of edge crossings. Specifically, draws a point and emits a ray in any direction. If the number of intersection points of the ray and path is an odd number, the point is considered to be inside the path and needs to be colored. If the number is an even number, the point is not colored. |
| INVERSE\_WINDING | 2 | Same as **WINDING**, but draws outside of the path, rather than inside. |
| INVERSE\_EVEN\_ODD | 3 | Same as **EVEN\_ODD**, but draws outside of the path, rather than inside. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/PbzfxeQ9SMOcHTFkB_7Hlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C72D1B379ABAAE75AEFA67FC9324FAD2F8C582962A072A87A368F90C9A2A2B62)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/qsO5EjrmQT2msqxNPAwhwg/en-us_image_0000002537926370.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1179CA1662D3C897B32F5C636D57F19B7311453AF10C932A621C303E2EF1998F)

As shown in the above figure, the path is a circle, the arrow indicates the path direction, **p** is any point "inside" the path, the blue line is the ray emitted from **p**, and the black arrow indicates the fill result using blue under the corresponding fill type. Under the **WINDING** fill rule, the number of intersection points of the ray and path is 2 (not 0), and therefore **p** is colored. Under the **EVEN\_ODD** filling rule, the number of intersection points of the ray and path is 2 (an even number), and therefore **p** is not colored.

#### PointMode12+

Enumerates the modes for drawing multiple points in an array.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| POINTS | 0 | Draws each point separately. |
| LINES | 1 | Draws every two points as a line segment. |
| POLYGON | 2 | Draws an array of points as an open polygon. |

#### FontEdging12+

Enumerates the font edging types.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| ALIAS | 0 | No anti-aliasing processing is used. |
| ANTI\_ALIAS | 1 | Uses anti-aliasing to smooth the jagged edges. |
| SUBPIXEL\_ANTI\_ALIAS | 2 | Uses sub-pixel anti-aliasing to provide a smoother effect for jagged edges. |

#### FontHinting12+

Enumerates the font hinting types.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No font hinting is used. |
| SLIGHT | 1 | Slight font hinting is used to improve contrast. |
| NORMAL | 2 | Normal font hinting is used to improve contrast. |
| FULL | 3 | Full font hinting is used to improve contrast. |

#### FontMetricsFlags12+

Enumerates the font measurement flags, which is used to specify whether a field in the [FontMetrics](../interfaces-others/document.md#fontmetrics) struct is valid.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| UNDERLINE\_THICKNESS\_VALID | 1 << 0 | The **underlineThickness** field is valid. |
| UNDERLINE\_POSITION\_VALID | 1 << 1 | The **underlinePosition** field is valid. |
| STRIKETHROUGH\_THICKNESS\_VALID | 1 << 2 | The **strikethroughThickness** field is valid. |
| STRIKETHROUGH\_POSITION\_VALID | 1 << 3 | The **strikethroughPosition** field is valid. |
| BOUNDS\_INVALID | 1 << 4 | The boundary measurement values (such as **top**, **bottom**, **xMin**, and **xMax**) are invalid. |

#### RectType12+

Enumerates the types of rectangles used to fill the lattices. Used only in [Lattice](../class-lattice/document.md).

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Draws an image into the lattice. |
| TRANSPARENT | 1 | Sets the lattice to transparent. |
| FIXEDCOLOR | 2 | Draws the colors in the **fColors** array in [Lattice](../class-lattice/document.md) into a lattice. |

#### PathDashStyle18+

Enumerates the drawing styles for path effects.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| TRANSLATE | 0 | Translates only, not rotating with the path. |
| ROTATE | 1 | Rotates with the path. |
| MORPH | 2 | Rotates with the path and stretches or compresses at turns to enhance smoothness. |

#### TileMode12+

Enumerates the tile modes of the shader effect.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| CLAMP | 0 | Replicates the edge color if the shader effect draws outside of its original boundary. |
| REPEAT | 1 | Repeats the shader effect in both horizontal and vertical directions. |
| MIRROR | 2 | Repeats the shader effect in both horizontal and vertical directions, alternating mirror images. |
| DECAL | 3 | Renders the shader effect only within the original boundary. |

#### JoinStyle12+

Enumerates the join styles of a pen. The join style defines the shape of the joints of a polyline segment drawn by the pen.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| MITER\_JOIN | 0 | Mitered corner. If the angle of a polyline is small, its miter length may be inappropriate. In this case, you need to use the miter limit to limit the miter length. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7jPWXFh9TJqkj2-sT6mcsw/en-us_image_0000002568686147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACFE74A7F164C88B67D87258407DAFE8DB02D09748EB5189421E0ADB62CFC45E) |
| ROUND\_JOIN | 1 | Round corner. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/0jhMIG2SQWiN--jY5X8ifA/en-us_image_0000002568766157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41F0BFC127B0A6F85265AC605D8566714D3644C7F55B3F2B22F577406974264A) |
| BEVEL\_JOIN | 2 | Beveled corner. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/QFdRj7CkTpGoEx8d4JCq9w/en-us_image_0000002537766432.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9046A6F6D4AA98112BD8557D6CFD614BCC45F67746EB07A76AD749BC55BD2C96) |

#### CapStyle12+

Enumerates the cap styles of a pen. The cap style defines the style of both ends of a line segment drawn by the pen.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| FLAT\_CAP | 0 | There is no cap style. Both ends of the line segment are cut off square. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/rNlA1bD_QGmtwWrD17DOQw/en-us_image_0000002537926372.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=495C55DA9F9E67BBDF3680E93E2C401A499D21A6063011CA17DC2DCEA6B89ED5) |
| SQUARE\_CAP | 1 | Square cap style. Both ends have a square, the height of which is half of the width of the line segment, with the same width. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/zopW6Yf4TpaLq517Yxlqog/en-us_image_0000002568686149.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23946A4228DB60075689165ABF10AD8E67445DF68809B195602655A459CCFBE9) |
| ROUND\_CAP | 2 | Round cap style. Both ends have a semicircle centered, the diameter of which is the same as the width of the line segment. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mfIRzU7uRnGuO2CX0MxkIw/en-us_image_0000002568766159.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BAABED0D079F0C11FE244A4D1C6637A0B1E85A1F334596D71DD3C658A393907) |

#### BlurType12+

Enumerates the blur types of a mask filter.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| NORMAL | 0 | Both the outer edges and the inner solid parts are blurred. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/DsLTNfBgRXapD6LX4a2Seg/en-us_image_0000002537766434.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C01A08EF21B0568E5B173AF2A87D61E31070B802BEC56F74C87366C11638C4) |
| SOLID | 1 | The inner solid part remains unchanged, while only the outer edges are blurred. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-Zw69e1ESgSJci2m9ydtsw/en-us_image_0000002537926374.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E61323C5DB79DFECA8F05044A3F974A45316FBBF029ECB922BD7D773822715CA) |
| OUTER | 2 | Only the outer edges are blurred, with the inner solid part being fully transparent. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/R1xCOkESSe24S4MPW6ZSdQ/en-us_image_0000002568686151.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A91B8C6CC68B158C5CE5BA98EDEA5DCDB5A14CB92E0838AD523E8C789D915B33) |
| INNER | 3 | Only the inner solid part is blurred, while the outer edges remain sharp. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uSFsmB-HQjmaH14yCPNM_Q/en-us_image_0000002568766161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A22342384A69BF75D649A33D19BF26810EA3262BEDDE41C0C24DFF71BA9AAFB1) |

#### ScaleToFit12+

Enumerates the modes of scaling a source rectangle into a destination rectangle.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| FILL\_SCALE\_TO\_FIT | 0 | Scales the source rectangle to completely fill the destination rectangle, potentially changing the aspect ratio of the source rectangle. |
| START\_SCALE\_TO\_FIT | 1 | Scales the source rectangle, preserving its aspect ratio, to align it to the upper left corner of the destination rectangle. |
| CENTER\_SCALE\_TO\_FIT | 2 | Scales the source rectangle, preserving its aspect ratio, to align it to the center of the destination rectangle. |
| END\_SCALE\_TO\_FIT | 3 | Scales the source rectangle, preserving its aspect ratio, to align it to the lower right corner of the destination rectangle. |

#### RegionOp12+

Enumerates the operations for combining two regions.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description | Diagram |
| :-- | :-- | :-- | :-- |
| DIFFERENCE | 0 | Difference operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zrcDViOxSKeqOWaeaplP-w/en-us_image_0000002537766436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35CDFD011E855F5832A64F676DF178D693AA7B87BD1EA3D9C00DFF1891940920) |
| INTERSECT | 1 | Intersect operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/d5AfioQWSbKJ5ZZk7DpxJg/en-us_image_0000002537926376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C459CFA59072A113F49BA1E7683875C4273DF12C7F178B458778F7DBD2F724F0) |
| UNION | 2 | Union operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/xW6YaeenSNWI3Fyt91VzKw/en-us_image_0000002568686153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A53840704BD1F90D75F15ADB909FD725C2945E6B5FDA05721C640D3E1F5027F3) |
| XOR | 3 | XOR operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Qckg9YHUS56tnkaIuG6fWQ/en-us_image_0000002568766163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB862B6FF56C6C81C15655975E4C8C3B24C9C03E9DDA71CBBA036807ABDAB3B6) |
| REVERSE\_DIFFERENCE | 4 | Reverse difference operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ACOOnwCeTL-V4LsCKHMDCQ/en-us_image_0000002537766438.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB154278C894844B31B713D6B5AD89677573B30B32DC1490533E57942A4005CE) |
| REPLACE | 5 | Replace operation. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/71XL7oOHRe6VYdkgIIU8pQ/en-us_image_0000002537926378.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B91AB739452CD50BDCF7C64926F5CF42969D39F476A6349C7D738881EAB40182) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/oIAtLF5bSLyy1IGGInI9RQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27FFF31AD3B67BF8CE3F1666B3656EF35FAF97C86A786AD87573216EAA7F81D4)

The schematic diagram shows the result obtained by combining a red region with a blue region at different operation mode. The green region is the region obtained.

#### CornerPos12+

Enumerates the corner positions of a rounded rectangle.

**System capability**: SystemCapability.Graphics.Drawing

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_LEFT\_POS | 0 | Top left corner of the rounded rectangle. |
| TOP\_RIGHT\_POS | 1 | Top right corner of the rounded rectangle. |
| BOTTOM\_RIGHT\_POS | 2 | Bottom right corner of the rounded rectangle. |
| BOTTOM\_LEFT\_POS | 3 | Bottom left corner of the rounded rectangle. |
