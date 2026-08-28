# Drawing

#### Overview

The Drawing module provides the functions for 2D graphics rendering, text drawing, and image display.

It uses the physical pixel unit, px.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

#### Files

| Name | Description |
| :-- | :-- |
| [drawing\_bitmap.h](../../header-files/drawing-bitmap-h/document.md) | Declares the functions related to the bitmap in the drawing module. |
| [drawing\_brush.h](../../header-files/drawing-brush-h/document.md) | Declares the functions related to the brush in the drawing module. |
| [drawing\_canvas.h](../../header-files/drawing-canvas-h/document.md) | 
Declares the functions related to the canvas in the drawing module.

By default, the canvas has a black brush with anti-aliasing enabled but no any other style. This default brush takes effect only when no brush or pen is proactively set in the canvas.

 |
| [drawing\_color.h](../../header-files/drawing-color-h/document.md) | Declares the functions related to the color in the drawing module. |
| [drawing\_color\_filter.h](../../header-files/drawing-color-filter-h/document.md) | Declares the functions related to the color filter in the drawing module. |
| [drawing\_color\_space.h](../../header-files/drawing-color-space-h/document.md) | Declares the functions related to the color space in the drawing module. |
| [drawing\_error\_code.h](../../header-files/drawing-error-code-h/document.md) | Declares the functions related to the error code in the drawing module.include native\_drawing/drawing\_error\_code.h |
| [drawing\_filter.h](../../header-files/drawing-filter-h/document.md) | Declares the functions related to the filter in the drawing module. |
| [drawing\_font.h](../../header-files/drawing-font-h/document.md) | Declares the functions related to the font in the drawing module. |
| [drawing\_font\_collection.h](../../header-files/drawing-font-collection-h/document.md) | Declares the functions related to the font collection in the drawing module. |
| [drawing\_font\_mgr.h](../../header-files/drawing-font-mgr-h/document.md) | Declares the functions related to font management in the drawing module. The functions can be used to load fonts and match available fonts in the system. |
| [drawing\_gpu\_context.h](../../header-files/drawing-gpu-context-h/document.md) | Declares the functions related to the GPU context in the drawing module. |
| [drawing\_image.h](../../header-files/drawing-image-h/document.md) | Declares the functions related to the image in the drawing module. |
| [drawing\_image\_filter.h](../../header-files/drawing-image-filter-h/document.md) | Declares the functions related to the image filter in the drawing module. |
| [drawing\_mask\_filter.h](../../header-files/drawing-mask-filter-h/document.md) | Declares the functions related to the mask filter in the drawing module. |
| [drawing\_matrix.h](../../header-files/drawing-matrix-h/document.md) | Declares the functions related to the matrix in the drawing module. |
| [drawing\_memory\_stream.h](../../header-files/drawing-memory-stream-h/document.md) | Declares the functions related to the memory stream in the drawing module. |
| [drawing\_path.h](../../header-files/drawing-path-h/document.md) | Declares the functions related to the path in the drawing module. |
| [drawing\_path\_effect.h](../../header-files/drawing-path-effect-h/document.md) | Declares the functions related to the bitmap in the drawing module. |
| [drawing\_pen.h](../../header-files/drawing-pen-h/document.md) | Declares the functions related to the pen in the drawing module. |
| [drawing\_pixel\_map.h](../../header-files/drawing-pixel-map-h/document.md) | Declares the functions related to the pixel map in the drawing module. |
| [drawing\_point.h](../../header-files/drawing-point-h/document.md) | Declares the functions related to the coordinate point in the drawing module. |
| [drawing\_record\_cmd.h](../../header-files/drawing-record-cmd-h/document.md) | Declares the functions related to a recording command object. |
| [drawing\_rect.h](../../header-files/drawing-rect-h/document.md) | Declares the functions related to the rectangle in the drawing module. |
| [drawing\_region.h](../../header-files/drawing-region-h/document.md) | Declares the functions related to the region in the drawing module, including creating a region, setting the boundary, and destroying a region. |
| [drawing\_register\_font.h](../../header-files/drawing-register-font-h/document.md) | Declares the functions related to the font manager in the drawing module. |
| [drawing\_round\_rect.h](../../header-files/drawing-round-rect-h/document.md) | Declares the functions related to the rounded rectangle in the drawing module. |
| [drawing\_sampling\_options.h](../../header-files/drawing-sampling-options-h/document.md) | Declares the functions related to the sampling options in the drawing module. It is used for image or texture sampling. |
| [drawing\_shader\_effect.h](../../header-files/drawing-shader-effect-h/document.md) | Declares the functions related to the shader effect in the drawing module. |
| [drawing\_shadow\_layer.h](../../header-files/drawing-shadow-layer-h/document.md) | Declares the functions related to the shadow in the drawing module. |
| [drawing\_surface.h](../../header-files/drawing-surface-h/document.md) | Declares the functions related to the surface in the drawing module, including creating, destroying, and using the surface. |
| [drawing\_text\_blob.h](../../header-files/drawing-text-blob-h/document.md) | Declares the functions related to the text blob in the drawing module. |
| [drawing\_text\_declaration.h](../../header-files/drawing-text-declaration-h/document.md) | Declares the structs related to text in 2D drawing. |
| [drawing\_text\_font\_descriptor.h](../../header-files/drawing-text-font-descriptor-h/document.md) | Declares the capabilities of font information, such as obtaining font information and searching for a font. |
| [drawing\_text\_global.h](../../header-files/drawing-text-global-h/document.md) | Declares the functions related to global text information, for example, setting the high contrast mode for text rendering. |
| [drawing\_text\_line.h](../../header-files/drawing-text-line-h/document.md) | Declares the capabilities for obtaining the character position in a text line, obtaining the run information, and truncating text by line. |
| [drawing\_text\_lineTypography.h](../../header-files/drawing-text-linetypography-h/document.md) | Declares the functions related to line typography, including functions to determine the number of characters that can be formatted from a given position within the text. |
| [drawing\_text\_run.h](../../header-files/drawing-text-run-h/document.md) | Declares the capabilities of runs, such as obtaining the typographic boundary and drawing. |
| [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md) | Declares the functions related to typography in the drawing module. |
| [drawing\_typeface.h](../../header-files/drawing-typeface-h/document.md) | 

Declares the functions related to the typeface in the drawing module.

Different platforms have their own default typefaces. You can also parse the .ttf file to obtain the typefaces specified by the third party, such as SimSun and SimHei.

 |
| [drawing\_types.h](../../header-files/drawing-types-h/document.md) | Declares the data types of the canvas, brush, pen, bitmap, and path used to draw 2D graphics. |
