# Requirements on the .shader File Format

In ArkGraphics 3D, .shader files are based on the JSON format and must adhere to JSON syntax. These files consist of the following sections:

#### compatibility\_info

-   Type: object
-   Description: declares shader version compatibility information to the engine. The following fields are used:
    
    "compatibility\_info": { "version": "22.00", "type": "shader" }
    
    This indicates that the shader description file is for engine version 22.00.

#### vert

-   Type: string
-   Description: specifies the vertex shader file used in the draw call for this shader.
-   Default value:
    
    "vert": "3dshaders://shader/core3d\_dm\_fw.vert.spv"
    
-   Custom path:
    
    "vert": "appshaders://yourDir/yourShader.vert.spv"
    
    Here, **yourDir/yourShader.vert.spv** is the path to the shader file within the file sandbox.

#### frag

-   Type: string
-   Description: specifies the fragment shader file used in the draw call for this shader.
-   Default value:
    
    "frag": "3dshaders://shader/core3d\_dm\_fw.frag.spv"
    
-   Custom path:
    
    "frag": "appshaders://yourDir/yourShader.frag.spv"
    
    Here, **yourDir/yourShader.frag.spv** is the path to the shader file within the file sandbox.

#### vertexInputDeclaration

-   Type: string
-   Description: specifies the layout of attributes in the input vertex data.
-   Constraints: The rendering engine does not support custom attribute layouts. Use the default value.
-   Default value:
    
    "vertexInputDeclaration": "3dvertexinputdeclarations://core3d\_dm\_fw.shadervid"
    

#### state

-   Type: object
-   Description: specifies the pipeline state for this rendering pipeline, including **rasterizationState**, **depthStencilState**, and **colorBlendState**.

## rasterizationState

Specifies the properties of the rasterization process. The options are as follows:

-   **enableDepthClamp**: specifies whether depth values are clamped during rendering. **true** if clamped, **false** otherwise. Currently, this property must be set to **false**.
    
-   **enableDepthBias**: specifies whether depth bias is applied during rendering. **true** if applied, **false** otherwise. Currently, this property must be set to **false**.
    
-   **enableRasterizerDiscard**: specifies whether the fragment stage of the draw call is skipped. **true** if skipped, **false** otherwise.
    
-   **polygonMode**: specifies the triangle filling mode in rasterization rendering. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "fill" | Fills the entire triangle. |
    | "line" | Draws only the edges of the triangle. |
    | "point" | Draws only the vertices of the triangle. |
    
-   **cullModeFlags**: specifies the culling mode in rasterization rendering. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "back" | Culls the back face. |
    | "front" | Culls the front face. |
    | "none" | No culling; renders both faces. |
    | "front\_and\_back" | Culls both front and back faces. |
    
-   **frontFace**: specifies which face of the triangle is considered the front. The following table lists the values and their meanings.
    
    | Value | Vertex Order | Description |
    | :-- | :-- | :-- |
    | "counter\_clockwise" | Counterclockwise | The front face is defined by counterclockwise vertex order. |
    | "clockwise" | Clockwise | The front face is defined by clockwise vertex order. |
    

## depthStencilState

Specifies the properties for depth and stencil testing. The options are as follows:

-   **enableDepthTest**: specifies whether depth testing is enabled. **true** if enabled, **false** otherwise. If enabled, non-transparent objects are rendered with occlusion based on their depth values. If disabled, objects are rendered in the order they are drawn.
-   **enableDepthWrite**: specifies whether the depth value of an object is written to the depth attachment during rendering. **true** if written, **false** otherwise.
-   **enableDepthBoundsTest**: specifies whether an additional depth range check is enabled on top of depth testing. Values outside the specified range fail the depth test. **true** if enabled, **false** otherwise. Currently, this property must be set to **false**.
-   **enableStencilTest**: specifies whether stencil testing is enabled. **true** if enabled, **false** otherwise. If enabled, only objects that pass the stencil test are rendered. If disabled, stencil testing is bypassed.
-   **depthCompareOp**: specifies the comparison operation of depth testing. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "never" | Never passes the depth test. |
    | "less" | Passes if the new depth is less than the current depth. |
    | "equal" | Passes if the new depth is equal to the current depth. |
    | "less\_or\_equal" | Passes if the new depth is less than or equal to the current depth. |
    | "greater" | Passes if the new depth is greater than the current depth. |
    | "not\_equal" | Passes if the new depth is not equal to the current depth. |
    | "greater\_or\_equal" | Passes if the new depth is greater than or equal to the current depth. |
    | "always" | Always passes the depth test. |
    

## colorBlendState

Specifies the blending properties of the rendering source and destination, including **colorAttachments**, which specifies blending properties for color attachments. **colorAttachments** includes the following items:

-   **enableBlend**: specifies whether blending is enabled between the source and destination. **true** if enabled, **false** otherwise. If enabled, the source and destination are blended in the specified mode. If disabled, no blending is performed.
    
-   **colorWriteMask**: specifies the channel mask of the rendered color attachment. If a channel mask is specified, the channel is blended. If no channel mask is specified, no blending is performed. The value can be **r\_bit**, **g\_bit**, **b\_bit**, **a\_bit**, and any of their combinations using the vertical bar (|). The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "r\_bit" | Allows writing to or blending of the red channel. |
    | "g\_bit" | Allows writing to or blending of the green channel. |
    | "b\_bit" | Allows writing to or blending of the blue channel. |
    | "a\_bit" | Allows writing to or blending of the alpha channel. |
    
-   **srcColorBlendFactor**: specifies the blending factor of the source color channel. The following table lists the values and their meanings.
    
    | Value | Factor | Result | Use Case |
    | :-- | :-- | :-- | :-- |
    | "zero" | 0 | Source color x 0 = 0 | No new color is displayed. Only the background is retained. |
    | "one" | 1 | Source color × 1 = Source color | The new color is fully displayed, covering the background. |
    | "src\_color" | Source color | Source color × Source color | The new color is blended by its own color ratio. |
    | "one\_minus\_src\_color" | 1 - Source color | Source color × (1 - Source color) | The new color is blended by its remaining color ratio. |
    | "dst\_color" | Destination color | Source color x Destination color | The new color is blended by the background color ratio. |
    | "one\_minus\_dst\_color" | 1 - Destination color | Source color x (1 - Destination color) | The new color is blended by the background's remaining color ratio. |
    | "src\_alpha" | Source alpha | Source color x Source alpha | The new color is blended by its own alpha ratio. |
    | "one\_minus\_src\_alpha" | 1 - Source alpha | Source color × (1 - Source alpha) | The new color is blended by its remaining alpha ratio. |
    | "dst\_alpha" | Destination alpha | Source color × Destination alpha | The new color is blended by the background alpha ratio. |
    | "one\_minus\_dst\_alpha" | 1 - Destination alpha | Source color x (1 - Destination alpha) | The new color is blended by the background alpha's remaining ratio. |
    | "constant\_color" | Constant color | Source color x Constant color | The new color is blended by the constant color ratio. |
    | "one\_minus\_constant\_color" | 1 - Constant color | Source color x (1 - Constant color) | The new color is blended by the constant color's remaining ratio. |
    | "constant\_alpha" | Constant alpha | Source color x Constant alpha | The new color is blended by the constant alpha ratio. |
    | "one\_minus\_constant\_alpha" | 1 - Constant alpha | Source color x (1 - Constant alpha) | The new color is blended by the constant alpha's remaining ratio. |
    | "src\_alpha\_saturate" | min(Source alpha, 1 - Destination alpha) | Source color x min(Source alpha, 1 - Destination alpha) | The new color is blended by the minimum of source alpha and background's remaining alpha to avoid over-saturation. |
    | "src1\_color" | Second source color | Source color × Second source color | The new color is blended by the second source color ratio. |
    | "one\_minus\_src1\_color" | 1 - Second source color | Source color × (1 - Second source color) | The new color is blended by the second source color's remaining ratio. |
    | "src1\_alpha" | Second source alpha | Source color × Second source alpha | The new color is blended by the second source alpha ratio. |
    | "one\_minus\_src1\_alpha" | 1 - Second source alpha | Source color × (1 - Second source alpha) | The new color is blended by the second source alpha's remaining ratio. |
    
-   **dstColorBlendFactor**: specifies the blending factor of the destination color channel. The following table lists the values and their meanings.
    
    | Value | Factor | Result | Use Case |
    | :-- | :-- | :-- | :-- |
    | "zero" | 0 | Destination color × 0 = 0 | No background color is displayed. |
    | "one" | 1 | Destination color × 1 = Destination color | The background color remains unchanged. |
    | "src\_color" | Source color | Destination color × Source color | The background color is blended by the new color ratio. |
    | "one\_minus\_src\_color" | 1 - Source color | Destination color x (1 - Source color) | The background color is blended by the new color's remaining ratio. |
    | "dst\_color" | Destination color | Destination color x Destination color | The background color is blended by its own color ratio. |
    | "one\_minus\_dst\_color" | 1 - Destination color | Destination color x (1 - Destination color) | The background color is blended by its remaining color ratio. |
    | "src\_alpha" | Source alpha | Destination color x Source alpha | The background color is blended by the source alpha ratio. |
    | "one\_minus\_src\_alpha" | 1 - Source alpha | Destination color x (1 - Source alpha) | The background color is blended by the source alpha's remaining ratio. |
    | "dst\_alpha" | Destination alpha | Destination color x Destination alpha | The background color is blended by its own alpha ratio. |
    | "one\_minus\_dst\_alpha" | 1 - Destination alpha | Destination color x (1 - Destination alpha) | The background color is blended by its alpha's remaining ratio. |
    | "constant\_color" | Constant color | Destination color x Constant color | The background color is blended by the constant color ratio. |
    | "one\_minus\_constant\_color" | 1 - Constant color | Destination color x (1 - Constant color) | The background color is blended by the constant color's remaining ratio. |
    | "constant\_alpha" | Constant alpha | Destination color x Constant alpha | The background color is blended by the constant alpha ratio. |
    | "one\_minus\_constant\_alpha" | 1 - Constant alpha | Destination color x (1 - Constant alpha) | The background color is blended by the constant alpha's remaining ratio. |
    | "src\_alpha\_saturate" | min(Source alpha, 1 - Destination alpha) | Destination color x min(Source alpha, 1 - Destination alpha) | The background color is blended by the minimum of source alpha and background's remaining alpha to avoid over-saturation. |
    | "src1\_color" | Second source color | Destination color × Second source color | The background color is blended by the second source color ratio. |
    | "one\_minus\_src1\_color" | 1 - Second source color | Destination color × (1 - Second source color) | The background color is blended by the second source color's remaining ratio. |
    | "src1\_alpha" | Second source alpha | Destination color × Second alpha | The background color is blended by the second source alpha ratio. |
    | "one\_minus\_src1\_alpha" | 1 - Second source alpha | Destination color × (1 - Second source alpha) | The background color is blended by the second source alpha's remaining ratio. |
    
-   **colorBlendOp**: specifies the blending option for the source and destination color channels. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "add" | Adds the source and destination colors. |
    | "subtract" | Subtracts the destination color from the source color. |
    | "reverse\_subtract" | Subtracts the source color from the destination color. |
    | "min" | Takes the minimum of the source and destination colors. |
    | "max" | Takes the maximum of the source and destination colors. |
    
-   **srcAlphaBlendFactor**: specifies the blending factor of the source alpha channel. The following table lists the values and their meanings.
    
    | Value | Factor | Result | Use Case |
    | :-- | :-- | :-- | :-- |
    | "zero" | 0 | Source alpha x 0 = 0 | No new alpha is displayed, which is equivalent to clearing the alpha. |
    | "one" | 1 | Source alpha x 1 = Source alpha | The new alpha remains unchanged. |
    | "src\_color" | Source color | Source alpha x Source color | The new alpha is blended by its own color ratio. |
    | "one\_minus\_src\_color" | 1 - Source color | Source alpha x (1 - Source color) | The new alpha is blended by its remaining color ratio. |
    | "dst\_color" | Destination color | Source alpha x Destination color | The new alpha is blended by the background color ratio. |
    | "one\_minus\_dst\_color" | 1 - Destination color | Source alpha x (1 - Destination color) | The new alpha is blended by the background's remaining color ratio. |
    | "src\_alpha" | Source alpha | Source alpha x Source alpha | The new alpha is blended by its own alpha ratio. |
    | "one\_minus\_src\_alpha" | 1 - Source alpha | Source alpha x (1 - Source alpha) | The new alpha is blended by its remaining alpha ratio. |
    | "dst\_alpha" | Destination alpha | Source alpha x Destination alpha | The new alpha is blended by the background alpha ratio. |
    | "one\_minus\_dst\_alpha" | 1 - Destination alpha | Source alpha x (1 - Destination alpha) | The new alpha is blended by the background's remaining alpha ratio. |
    | "constant\_color" | Constant color | Source alpha x Constant color | The new alpha is blended by the constant color ratio. |
    | "one\_minus\_constant\_color" | 1 - Constant color | Source alpha x (1 - Constant color) | The new alpha is blended by the constant color's remaining ratio. |
    | "constant\_alpha" | Constant alpha | Source alpha x Constant alpha | The new alpha is blended by the constant alpha ratio. |
    | "one\_minus\_constant\_alpha" | 1 - Constant alpha | Source alpha x (1 - Constant alpha) | The new alpha is blended by the constant alpha's remaining ratio. |
    | "src\_alpha\_saturate" | min(Source alpha, 1 - Destination alpha) | Source alpha x min(Source alpha, 1 - Destination alpha) | The new alpha is blended by the minimum of source alpha and background's remaining alpha to avoid over-saturation. |
    | "src1\_color" | Second source color | Source alpha × Second source color | The new alpha is blended by the second source color ratio. |
    | "one\_minus\_src1\_color" | 1 - Second source color | Source alpha × (1 - Second source color) | The new alpha is blended by the second source color's remaining ratio. |
    | "src1\_alpha" | Second source alpha | Source alpha × Second source alpha | The new alpha is blended by the second source alpha ratio. |
    | "one\_minus\_src1\_alpha" | 1 - Second source alpha | Source alpha × (1 - Second source alpha) | The new alpha is blended by the second source alpha's remaining ratio. |
    
-   **dstAlphaBlendFactor**: specifies the blending factor of the destination alpha channel. The following table lists the values and their meanings.
    
    | Value | Factor | Result | Use Case |
    | :-- | :-- | :-- | :-- |
    | "zero" | 0 | Destination alpha x 0 = 0 | No background alpha is displayed, which is equivalent to clearing the alpha. |
    | "one" | 1 | Destination alpha x 1 = Destination alpha | The background alpha remains unchanged. |
    | "src\_color" | Source color | Destination alpha x Source color | The background alpha is blended by the new color ratio. |
    | "one\_minus\_src\_color" | 1 - Source color | Destination alpha x (1 - Source color) | The background alpha is blended by the new color's remaining ratio. |
    | "dst\_color" | Destination color | Destination alpha x Destination color | The background alpha is blended by its own color ratio. |
    | "one\_minus\_dst\_color" | 1 - Destination color | Destination alpha x (1 - Destination color) | The background alpha is blended by its remaining color ratio. |
    | "src\_alpha" | Source alpha | Destination alpha x Source alpha | The background alpha is blended by the source alpha ratio. |
    | "one\_minus\_src\_alpha" | 1 - Source alpha | Destination alpha x (1 - Source alpha) | The background alpha is blended by the source alpha's remaining ratio. |
    | "dst\_alpha" | Destination alpha | Destination alpha x Destination alpha | The background alpha is blended by its own alpha ratio. |
    | "one\_minus\_dst\_alpha" | 1 - Destination alpha | Destination alpha x (1 - Destination alpha) | The background alpha is blended by its remaining alpha ratio. |
    | "constant\_color" | Constant color | Destination alpha x Constant color | The background alpha is blended by the constant color ratio. |
    | "one\_minus\_constant\_color" | 1 - Constant color | Destination alpha x (1 - Constant color) | The background alpha is blended by the constant color's remaining ratio. |
    | "constant\_alpha" | Constant alpha | Destination alpha x Constant alpha | The background alpha is blended by the constant alpha ratio. |
    | "one\_minus\_constant\_alpha" | 1 - Constant alpha | Destination alpha x (1 - Constant alpha) | The background alpha is blended by the constant alpha's remaining ratio. |
    | "src\_alpha\_saturate" | min(Source alpha, 1 - Destination alpha) | Destination alpha x min(Source alpha, 1 - Destination alpha) | The background alpha is blended by the minimum of source alpha and background's remaining alpha to avoid over-saturation. |
    | "src1\_color" | Second source color | Destination alpha × Second source color | The background alpha is blended by the second source color ratio. |
    | "one\_minus\_src1\_color" | 1 - Second source color | Destination alpha × (1 - Second source color) | The background alpha is blended by the second source color's remaining ratio. |
    | "src1\_alpha" | Second source alpha | Destination alpha × Second source alpha | The background alpha is blended by the second source alpha ratio. |
    | "one\_minus\_src1\_alpha" | 1 - Second source alpha | Destination alpha × (1 - Second source alpha) | The background alpha is blended by the second source alpha's remaining ratio. |
    
-   **alphaBlendOp**: specifies the blending option for the source and destination alpha channels. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "add" | Adds the source and destination alphas. |
    | "subtract" | Subtracts the destination alpha from the source alpha. |
    | "reverse\_subtract" | Subtracts the source alpha from the destination alpha. |
    | "min" | Takes the minimum of the source and destination alphas. |
    | "max" | Takes the maximum of the source and destination alphas. |
    

#### materialMetadata

-   Type: array<MaterialMetadata>
-   Description: specifies the metadata for rendering materials. Each MaterialMetadata object contains **name** and **customProperties**.

## name

Identifies the material component name. The current valid value is **MaterialComponent**.

## customProperties

Specifies custom properties passed during rendering. These custom properties are contained in a data array. Each object in the data array includes the following properties:

-   **name**: specifies the name of custom data passed during rendering, which corresponds to the data name in custom rendering.
    
-   **displayName**: specifies the name displayed in the 3D editor.
    
-   **type**: specifies the data type. The following table lists the values and their meanings.
    
    | Value | Description |
    | :-- | :-- |
    | "vec4" | 4D vector \[x, y, z, w\]. |
    | "vec3" | 3D vector \[x, y, z\]. |
    | "vec2" | 2D vector \[x, y\]. |
    | "float" | Floating-point number. |
    | "int" | Integer. |
    
-   **value**: The default value of the property.
    

#### Example

{
    "compatibility\_info" : { "version" : "22.00", "type" : "shader" },
    "vert": "3dshaders://shader/core3d\_dm\_fw.vert.spv",
    "frag": "appshaders://custom\_shader/custom\_material\_sample.frag.spv",
    "vertexInputDeclaration": "3dvertexinputdeclarations://core3d\_dm\_fw.shadervid",
    "state": {
        "rasterizationState": {
            "enableDepthClamp": false,
            "enableDepthBias": false,
            "enableRasterizerDiscard": false,
            "polygonMode": "fill",
            "cullModeFlags": "back",
            "frontFace": "counter\_clockwise"
        },
        "depthStencilState": {
            "enableDepthTest": true,
            "enableDepthWrite": true,
            "enableDepthBoundsTest": false,
            "enableStencilTest": false,
            "depthCompareOp": "less\_or\_equal"
        },
        "colorBlendState": {
            "colorAttachments": \[
                {
                    "enableBlend": true,
                    "colorWriteMask": "r\_bit|g\_bit|b\_bit|a\_bit",
                    "srcColorBlendFactor": "one",
                    "dstColorBlendFactor": "one\_minus\_src\_alpha",
                    "colorBlendOp": "add",
                    "srcAlphaBlendFactor": "one",
                    "dstAlphaBlendFactor": "one\_minus\_src\_alpha",
                    "alphaBlendOp": "add"
                }
            \]
        }
    },
    "materialMetadata": \[
        {
            "name": "MaterialComponent",
            "customProperties": \[
                {
                    "data": \[
                        {
                            "name": "vec\_1",
                            "displayName": "Color",
                            "type": "vec4",
                            "value" : \[1.0,1.0,1.0,1.0\]
                        },
                        {
                            "name": "time",
                            "displayName": "Time",
                            "type": "float",
                            "value": 0.0
                        },
                        {
                            "name": "dof",
                            "displayName": "Dof",
                            "type": "int",
                            "value": 1
                        },
                        {
                            "name": "motionblur",
                            "displayName": "MotionBlur",
                            "type": "int",
                            "value": 1
                        }
                    \]
                }
            \]
        }
    \]
}
