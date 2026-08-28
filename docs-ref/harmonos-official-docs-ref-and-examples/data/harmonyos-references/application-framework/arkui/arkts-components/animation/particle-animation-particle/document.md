# Particle Animation (Particle)

Particle animation is an animation composed of a multitude of particles randomly generated within a certain range. The particles can be points or images. By animating different aspects of the particles, such as color, opacity, scale, velocity, acceleration, and spin angle, you can create engaging and dynamic aesthetics. For example, you can create an impressive snowfall animation by animating the particles – snowflakes.

The component used for producing particle animations is **Particle**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/db9scQglQZ6sgoCp1-XQ_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73ED9FB6E634534167E38BBD4376919C73051D40FB91B34301E15E825E8863B6)

-   This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.
    
-   If the screen is turned off and then turned on again, or the application is switched to the background and then brought back to the foreground, the particle animation will automatically pause.
    

#### Child Components

Not supported

#### APIs

interface ParticleInterface {
  <
    PARTICLE extends ParticleType,
    COLOR\_UPDATER extends ParticleUpdater,
    OPACITY\_UPDATER extends ParticleUpdater,
    SCALE\_UPDATER extends ParticleUpdater,
    ACC\_SPEED\_UPDATER extends ParticleUpdater,
    ACC\_ANGLE\_UPDATER extends ParticleUpdater,
    SPIN\_UPDATER extends ParticleUpdater
  >(particles: Particles<
      PARTICLE,
      COLOR\_UPDATER,
      OPACITY\_UPDATER,
      SCALE\_UPDATER,
      ACC\_SPEED\_UPDATER,
      ACC\_ANGLE\_UPDATER,
      SPIN\_UPDATER
    >): ParticleAttribute;
}

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| particles | 
[Particles](#particles18)<

[PARTICLE](#particletype),

[COLOR\_UPDATER](#particleupdater),

[OPACITY\_UPDATER](#particleupdater),

[SCALE\_UPDATER](#particleupdater),

[ACC\_SPEED\_UPDATER](#particleupdater),

[ACC\_ANGLE\_UPDATER](#particleupdater),

[SPIN\_UPDATER](#particleupdater)

\>

 | No | No | Particles. For details, see [Particles](#particles18). |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]disturbanceFields12+

disturbanceFields(fields: Array<DisturbanceFieldOptions>)

Sets the disturbance fields.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<[DisturbanceFieldOptions](#disturbancefieldoptions12)\> | Yes | Array of disturbance fields. |

#### \[h2\]emitter12+

emitter(value: Array<EmitterProperty>)

Sets the emitter parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[EmitterProperty](#emitterproperty12)\> | Yes | Array of emitter parameters to set. |

#### \[h2\]rippleFields22+

rippleFields(fields: Array<RippleFieldOptions>|undefined)

Sets the particle wave field. The wave field applies a force that changes according to the waveform to particles within the affected range, producing an effect similar to the spreading of ripples.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<[RippleFieldOptions](#ripplefieldoptions22)\>|undefined | Yes | Particle wave field array. You can set multiple particle wave fields in array form. If this parameter is set to undefined, no wave field is available. |

#### \[h2\]velocityFields22+

velocityFields(fields: Array<VelocityFieldOptions>|undefined)

Sets the particle velocity field. The velocity field applies a force to particles within the affected range, so that the particles move at the velocity specified by the velocity field in addition to their original velocity.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fields | Array<[VelocityFieldOptions](#velocityfieldoptions22)\>|undefined | Yes | Particle velocity field array. You can set multiple particle velocity fields in array form. If this parameter is set to undefined, there is no velocity field. |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### ParticleOptions

interface ParticleOptions<
  PARTICLE extends ParticleType,
  COLOR\_UPDATER extends ParticleUpdater,
  OPACITY\_UPDATER extends ParticleUpdater,
  SCALE\_UPDATER extends ParticleUpdater,
  ACC\_SPEED\_UPDATER extends ParticleUpdater,
  ACC\_ANGLE\_UPDATER extends ParticleUpdater,
  SPIN\_UPDATER extends ParticleUpdater
> {
  emitter: EmitterOptions<PARTICLE>;
  color?: ParticleColorPropertyOptions<COLOR\_UPDATER>;
  opacity?: ParticlePropertyOptions<number, OPACITY\_UPDATER>;
  scale?: ParticlePropertyOptions<number, SCALE\_UPDATER>;
  velocity?: VelocityOptions;
  acceleration?: AccelerationOptions<ACC\_SPEED\_UPDATER, ACC\_ANGLE\_UPDATER>;
  spin?: ParticlePropertyOptions<number, SPIN\_UPDATER>;
}

Sets particle parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| emitter | [EmitterOptions](#emitteroptions)<[PARTICLE](#particletype)\> | No | No | Particle emitter. |
| color | [ParticleColorPropertyOptions](#particlecolorpropertyoptions)<[COLOR\_UPDATER](#particleupdater)\> | No | Yes | 
Particle color.

**NOTE**

Default value: **{ range:\[Color.White,Color.White\] }.** Colors cannot be set for image particles.

 |
| opacity | [ParticlePropertyOptions](#particlepropertyoptions)<number, [OPACITY\_UPDATER](#particleupdater)\> | No | Yes | 

Particle opacity.

Default value: **{ range:\[1.0,1.0\] }**

 |
| scale | [ParticlePropertyOptions](#particlepropertyoptions)<number, [SCALE\_UPDATER](#particleupdater)\> | No | Yes | 

Particle scale.

Default value: **{ range:\[1.0,1.0\] }**

 |
| velocity | [VelocityOptions](#velocityoptions18) | No | Yes | 

Particle velocity.

**NOTE**

**speed** indicates the time rate at which the particle moves. **angle** indicates the direction (in angles) in which the particle moves, with the geometric center of the element as the coordinate origin and the horizontal direction as the x-axis. A positive number indicates clockwise rotation.

Default value: **{speed: \[0.0,0.0\],angle: \[0.0,0.0\] }**

 |
| acceleration | [AccelerationOptions](#accelerationoptions18)<[ACC\_SPEED\_UPDATER](#particleupdater), [ACC\_ANGLE\_UPDATER](#particleupdater)\> | No | Yes | 

Particle acceleration.

**NOTE**

**speed** indicates the acceleration speed, and **angle** indicates the acceleration direction (in angles).

Default value: **{ speed:{range:\[0.0,0.0\]},angle:{range:\[0.0,0.0\]} }**

 |
| spin | [ParticlePropertyOptions](#particlepropertyoptions)<number, [SPIN\_UPDATER](#particleupdater)\> | No | Yes | 

Particle spin angle.

Default value: **{range:\[0.0,0.0\]}**

Direction: A positive number indicates clockwise spinning, and a negative number indicates anticlockwise spinning.

 |

#### EmitterOptions

interface EmitterOptions<PARTICLE extends ParticleType> {
  particle: EmitterParticleOptions<PARTICLE>;
  emitRate?: number;
  shape?: ParticleEmitterShape;
  position?: ParticleTuple<Dimension, Dimension>;
  size?: ParticleTuple<Dimension, Dimension>;
  annulusRegion?: ParticleAnnulusRegion;
}

Particle emitter configuration.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| particle | [EmitterParticleOptions](#emitterparticleoptions18)<[PARTICLE](#particletype)\> | No | No | 
Particle configuration.

\- **type**: particle type, which can be **IMAGE** or **POINT**.

\- **config**: configuration of the particle type.

\- The value type of **config** is subject to the value of **type**.

1\. If the type is ParticleType.POINT, the config type is [PointParticleParameters](#pointparticleparameters).

2\. If the type is ParticleType.IMAGE, the config type is [ImageParticleParameters](#imageparticleparameters).

\- **count**: number of particles. The value is greater than or equal to -1. The value **\-1** indicates that the number of particles is infinite.

\- **lifetime**: lifetime of a single particle. The default value is **1000** (that is, 1000 ms, 1s). The value is greater than or equal to -1. The value **\-1** indicates that the lifetime of the particle is infinite. If the value specified is less than **\-1**, the default value is used.

Note: If you do not want the animation to keep playing, you are advised not to set the lifetime to –1, which may greatly affect the performance.

The **lifeTimeRange** parameter indicates the range of the particle lifetime. After this parameter is set, the lifetime of a particle is a random integer within the range of \[lifetime – lifeTimeRange, lifetime + lifeTimeRange\]. The default value of lifeTimeRange is 0. The value ranges from 0 to positive infinity. If it is set to a negative value, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| emitRate | number | No | Yes | 

Emit rate (that is, the number of particles emitted per second).

Default value: **5**. If the value specified is less than 0, the default value is used.

The **emitRate** value can significantly impact performance when it exceeds 5000; you are advised to set it to be less than 5000.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| shape | [ParticleEmitterShape](#particleemittershape) | No | Yes | 

Emitter shape.

Default value: ParticleEmitterShape.RECTANGLE

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| position | [ParticleTuple](#particletuple18)<[Dimension](../../common-definitions/basic-types/document.md#dimension10), [Dimension](../../common-definitions/basic-types/document.md#dimension10)\> | No | Yes | 

Emitter position (distance from the upper left corner of the component). The first parameter indicates the relative offset along the x-axis, and the second parameter indicates the relative offset along the y-axis.

Default value: **\[0.0, 0.0\]**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| size | [ParticleTuple](#particletuple18)<[Dimension](../../common-definitions/basic-types/document.md#dimension10), [Dimension](../../common-definitions/basic-types/document.md#dimension10)\> | No | Yes | 

Size of the emit window. The first parameter indicates the emitter width, and the second parameter indicates the emitter height.

Default value: **\['100%','100%'\]** (that is, the emission window occupies the entire Particle component.)

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| annulusRegion20+ | [ParticleAnnulusRegion](#particleannulusregion20) | No | Yes | 

Annulus emitter parameters. This parameter takes effect only when the emitter shape is annulus (that is, the shape parameter is ParticleEmitterShape.ANNULUS). For an annulus emitter, the shape information must be specified by the annulusRegion parameter, and the position and size parameters do not take effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ParticleConfigs

Sets particle configuration items.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| \[ParticleType.POINT\] | [PointParticleParameters](#pointparticleparameters) | No | No | Point particle configuration. |
| \[ParticleType.IMAGE\] | [ImageParticleParameters](#imageparticleparameters) | No | No | Image particle configuration. |

#### PointParticleParameters

Sets the radius of a particle.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | [VP](../../common-definitions/basic-types/document.md#vp10) | No | No | Particle radius. |

#### ImageParticleParameters

Sets the image options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Path to the image. Local and online sources are supported. For details about how to reference an image, see [Loading Image Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#loading-image-resources).

SVG images are not supported.

If the value of src does not change, the cached resource is preferentially used. As a result, resources cannot be dynamically switched. If you want to dynamically switch resources, you are advised to switch to different src values.

 |
| size | [ParticleTuple](#particletuple18)<[Dimension](../../common-definitions/basic-types/document.md#dimension10), [Dimension](../../common-definitions/basic-types/document.md#dimension10)\> | No | No | Image size. |
| objectFit | [ImageFit](../../common-definitions/enums/document.md#imagefit) | No | Yes | Image display mode. |

#### ParticleColorPropertyOptions

interface ParticleColorPropertyOptions<UPDATER extends ParticleUpdater> {
  range: ParticleTuple<ResourceColor, ResourceColor>;
  distributionType?: DistributionType;
  updater?: ParticleColorUpdaterOptions<UPDATER>;
}

Sets the particle color attribute updater configuration.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| range | [ParticleTuple](#particletuple18)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor), [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | No | No | 
Initial color range of the particle. The initial color of particles generated by the particle emitter is randomly selected in this range.

Default value: range:\[Color.White,Color.White\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| distributionType12+ | [DistributionType](#distributiontype12) | No | Yes | 

Type of random value distribution for the initial color of the particle. Both uniform distribution and normal (Gaussian) distribution are supported.

Default value: **DistributionType.UNIFORM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| updater | [ParticleColorUpdaterOptions](#particlecolorupdateroptions18)<[UPDATER](#particleupdater)\> | No | Yes | 

How the color property is updated. The available options of **type** are as follows:

1\. **ParticleUpdater.NONE**: The property does not change. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.NONE\].

2\. **ParticleUpdater.RANDOM**: The property changes randomly. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.RANDOM\].

3\. **ParticleUpdater.CURVE**: The property changes with the animation curve. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.CURVE\].

The default value of **type** is **ParticleUpdater.NONE**.

**NOTE**

When **type** is set to **ParticleUpdater.RANDOM** or **ParticleUpdater.CURVE**, the color configuration in **updater** has higher priority than that in **range**. During the animation time period configured in **updater**, the color configuration from **updater** is used. Outside of the animation time period configured in **updater**, the color configuration from **range** is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ParticleColorPropertyUpdaterConfigs

Sets the configuration of the particle color attribute updater.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| \[ParticleUpdater.NONE\] | void | No | No | The color does not change. |
| \[ParticleUpdater.RANDOM\] | [ParticleColorOptions](#particlecoloroptions18) | No | No | The color changes randomly, with the per-second change difference being a value randomly generated from the range. The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels. |
| \[ParticleUpdater.CURVE\] | Array<[ParticlePropertyAnimation](#particlepropertyanimation)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\>> | No | No | The color changes with the animation curve. The array type indicates that multiple animation segments can be set for the current property, for example, 0–3000 ms, 3000–5000 ms, and 5000–8000 ms. |

#### ParticlePropertyOptions

interface ParticlePropertyOptions<TYPE, UPDATER extends ParticleUpdater> {
  range: ParticleTuple<TYPE, TYPE>;
  updater?: ParticleUpdaterOptions<TYPE, UPDATER>;
}

Sets particle attributes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| range | [ParticleTuple](#particletuple18)<[TYPE](#particleupdater), [TYPE](#particleupdater)\> | No | No | 
Initial property value range of the particle. The initial property value of particles generated by the particle emitter is randomly selected in this range.

**NOTE**

If a property is set to an invalid value, the default value will be used. If the maximum value is less than the minimum value, the default range will be used. **TYPE** is number.

The default value varies by property:

1\. **opacity** property: **range:\[1.0,1.0\]**; the value range is \[0, 1\]; the default value is **1.0**.

2\. **scale** property: **range:\[1.0,1.0\]**; the value range is \[0, 10000\]; the default value is **1.0**.

3\. **acceleration** speed property: **range:\[0.0,0.0\]**; the value range is \[0, 10000\]; the default value is **0.0**.

4\. **acceleration** angle property: **range:\[0.0,0.0\]**; the value range is \[-10000, 10000\]; the default value is **0.0**.

5\. **spin** speed property: **range:\[0.0,0.0\]**; the value range is \[-10000, 10000\]; the default value is **0.0**.

 |
| updater | [ParticleUpdaterOptions](#particleupdateroptions18)<[TYPE](#particleupdater), [UPDATER](#particleupdater)\> | No | Yes | 

How the property is updated. The available options of **type** are as follows:

1\. **ParticleUpdater.NONE**: The property does not change. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.NONE\].

2\. **ParticleUpdater.RANDOM**: The property changes randomly. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.RANDOM\].

3\. **ParticleUpdater.CURVE**: The property changes with the animation curve. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.CURVE\].

The default value of **type** is **ParticleUpdater.NONE**.

 |

#### ParticlePropertyUpdaterConfigs

interface ParticlePropertyUpdaterConfigs<T> {
    \[ParticleUpdater.NONE\]: void;
    \[ParticleUpdater.RANDOM\]: ParticleTuple<T, T>;
    \[ParticleUpdater.CURVE\]: Array<ParticlePropertyAnimation<T>>;
}

Sets the particle property updater configuration.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| \[ParticleUpdater.NONE\] | void | No | No | The color does not change. |
| \[ParticleUpdater.RANDOM\] | [ParticleTuple](#particletuple18)<T, T> | No | No | 
The property changes randomly, with the per-second change difference being a value randomly generated from the range.

The target property value is obtained by applying the change difference to the current property value. For example, if the current property value is **0.2** and **config** is set to **\[0.1,1.0\]**, then:

1\. When the random change difference is 0.5, the target property value is 0.2 + 0.5 = 0.7.

2\. The change difference may also be a negative value. For example, if the current property value is **0.2** and **config** is set to **\[-3.0,2.0\]**, then when the random change difference is **\-2.0**, the target property value is 0.2 - 2.0 = -1.8.

**NOTE**

**config** sets the value range of the change difference. While the change difference does not have a maximum or minimum value limit, the target property value does. Therefore, if the target property value is greater than the maximum property value, the maximum property value will be used instead; if the target property value is less than the minimum property value, the minimum property value will be used instead. **T** represents a number.

For example, if the value range of **opacity** is **\[0.0, 1.0\]**, then if the target property value is greater than 1.0, **1.0** will be used instead.

 |
| \[ParticleUpdater.CURVE\] | Array<[ParticlePropertyAnimation](#particlepropertyanimation)<T>> | No | No | The property changes with the animation curve. The array type indicates that multiple animation segments can be set for the current property, for example, 0-3000 ms, 3000-5000 ms, and 5000-8000 ms. **T** represents a number. |

#### ParticlePropertyAnimation

interface ParticlePropertyAnimation<T> {
  from: T;
  to: T;
  startMillis: number;
  endMillis: number;
  curve?: Curve | ICurve;
}

Lifecycle of a particle attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| from | T | No | No | Initial value of the property. If the value is invalid, the default value will be used. |
| to | T | No | No | Target value of the property. If the value is invalid, the default value will be used. |
| startMillis | number | No | No | 
Start time of the animation.

Unit: ms.

Value range: \[0, +∞).

 |
| endMillis | number | No | No | 

End time of the animation.

Unit: ms.

Value range: \[0, +∞).

 |
| curve | [Curve](../../common-definitions/enums/document.md#curve) | [ICurve](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9) | No | Yes | 

Animation curve.

Default value: **Curve.Linear**

 |

#### ParticleType

Particle type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| POINT | 'point' | Point particle. |
| IMAGE | 'image' | Image particle. |

#### ParticleEmitterShape

Particle emitter shape.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| RECTANGLE | 'rectangle' | 
Rectangle.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CIRCLE | 'circle' | 

Circle.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ELLIPSE | 'ellipse' | 

Ellipse.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ANNULUS20+ | 'annulus' | 

Ring.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### DistributionType12+

Random distribution of the initial color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| UNIFORM | 0 | The initial color random values are distributed uniformly. |
| GAUSSIAN | 1 | The initial color random values are distributed according to a Gaussian distribution. |

#### ParticleUpdater

Particle change type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 'none' | No change. |
| RANDOM | 'random' | Random change. |
| CURVE | 'curve' | Change with the animation curve. |

#### DisturbanceFieldOptions12+

Sets the parameters of the disturbance field.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strength | number | No | Yes | 
Field strength, which indicates the intensity of the repulsive force from the center outward. The default value is **0**. Positive values indicate a repulsive force directed outward, while negative values indicate an attractive force directed inward.

Value range: (-∞, +∞).

 |
| shape | [DisturbanceFieldShape](#disturbancefieldshape12) | No | Yes | 

Shape of the field.

Default value: **DisturbanceFieldShape.RECT**

 |
| size | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<number> | No | Yes | 

Size of the field.

Default value: {width:0, height:0}.

Value range of **width** and **height**: \[0, +∞).

 |
| position | [PositionT](../../../arkts-api/ui/arkui/graphics/document.md#positiont12)<number> | No | Yes | 

Position of the field.

Default value: {x:0, y:0}.

Value range of **x** and **y**: (-∞, +∞).

 |
| feather | number | No | Yes | 

Feather value, which represents the degree of attenuation from the center of the field to its edges. The value is an integer ranging from 0 to 100. A value of 0 indicates that the field is rigid, and all particles within its range are repelled. The higher the feather value, the more gradual the field becomes, resulting in more particles close to the center point appearing within the field's range.

Default value: **0**.

 |
| noiseScale | number | No | Yes | 

Noise scale, used to control the overall size of the noise pattern. The value is greater than or equal to 0.

Default value: **1**.

 |
| noiseFrequency | number | No | Yes | 

Noise frequency. The higher the frequency, the finer the noise. The value is greater than or equal to 0.

Default value: **1**.

 |
| noiseAmplitude | number | No | Yes | 

Noise amplitude, which indicates the range of noise fluctuations. The greater the amplitude, the greater the difference between the noises. The value is greater than or equal to 0.

Default value: **1**.

 |

#### DisturbanceFieldShape12+

Particle shape.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| RECT | 0 | Rectangle. |
| CIRCLE | 1 | Circle. |
| ELLIPSE | 2 | Ellipse. |

#### EmitterProperty12+

Sets the emitter attributes.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | No | 
Index of the emitter based on the index array of the emitters in the initialization parameters. The value is rounded to the nearest whole number. The default value **0** is used in case of exceptions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| emitRate | number | No | Yes | 

Emit rate, that is, the number of particles emitted per second.

If no value is passed in, the current emit rate is retained. If a value less than 0 is passed in, the default value **5** is used. The **emitRate** value can significantly impact performance when it exceeds 5000; you are advised to set it to be less than 5000.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| position | [PositionT](../../../arkts-api/ui/arkui/graphics/document.md#positiont12)<number> | No | Yes | 

Array of emitter positions. Only the number type is supported.

If no value is passed in, the current emitter position is retained. Two valid values must be passed in; if either is an invalid value, **position** will not take effect.

Value range of **x** and **y**: (-∞, +∞).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| size | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<number> | No | Yes | 

Size of the emit window. Only the number type is supported.

If no value is passed in, the current emitter window size is retained. Two valid values greater than 0 must be passed in; if either is an invalid value, **size** will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| annulusRegion20+ | [ParticleAnnulusRegion](#particleannulusregion20) | No | Yes | 

Ring emitter parameters. The parameters take effect only when the emitter shape corresponding to index is ring.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ParticleTuple18+

declare type ParticleTuple<T1, T2> = \[T1, T2\];

Defines the tuple type representing a pair of animation parameters.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| \[T1, T2\] | A pair of animation parameters, which can be of any type. |

#### Particles18+

interface Particles<
  PARTICLE extends ParticleType,
  COLOR\_UPDATER extends ParticleUpdater,
  OPACITY\_UPDATER extends ParticleUpdater,
  SCALE\_UPDATER extends ParticleUpdater,
  ACC\_SPEED\_UPDATER extends ParticleUpdater,
  ACC\_ANGLE\_UPDATER extends ParticleUpdater,
  SPIN\_UPDATER extends ParticleUpdater
> {
  particles: Array<
    ParticleOptions<
      PARTICLE,
      COLOR\_UPDATER,
      OPACITY\_UPDATER,
      SCALE\_UPDATER,
      ACC\_SPEED\_UPDATER,
      ACC\_ANGLE\_UPDATER,
      SPIN\_UPDATER
    >
  >;
}

An array of particle options,

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/oVA6jPy-RJmH-rsh3z2FfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5EE8482C4B1520A65FCE462F9A6D9ECF2A07906A613EB777A48F79700686DAB)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| particles10+ | 
Array<

ParticleOptions<

PARTICLE,

COLOR\_UPDATER,

OPACITY\_UPDATER,

SCALE\_UPDATER,

ACC\_SPEED\_UPDATER,

ACC\_ANGLE\_UPDATER,

SPIN\_UPDATER

\>

\>

 | No | No | 

An array of particle options, each of which covers the emitter, color, opacity, scale, velocity, acceleration, and spin speed of particles. For details, see [ParticleOptions](#particleoptions).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### VelocityOptions18+

Particle velocity.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fGLaBvp8Rai1084i-de5Kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AFEB9DB1641BFD8A572B6184702524B91468900BE9C0C716A4319376E694468)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| speed10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | 
Time rate at which the particle moves.

Default value: **{range:\[0.0,0.0\]}**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| angle10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | 

Direction (in angles) in which the particle moves, with the geometric center of the element as the coordinate origin and the horizontal direction as the x-axis. A positive number indicates clockwise rotation.

Default value: **{range:\[0.0,0.0\]}**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### AccelerationOptions18+

declare interface AccelerationOptions<
  ACC\_SPEED\_UPDATER extends ParticleUpdater,
  ACC\_ANGLE\_UPDATER extends ParticleUpdater
> {
  speed?: ParticlePropertyOptions<number, ACC\_SPEED\_UPDATER>;
  angle?: ParticlePropertyOptions<number, ACC\_ANGLE\_UPDATER>;
}

Particle acceleration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/W46s5KhVT1-ou_GOpSp9Jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7231F28F11654A9639A97DB42777EAECDF9849FB8E443C3A173C8FFCD521F7A5)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| speed10+ | [ParticlePropertyOptions](#particlepropertyoptions)<number, [ACC\_SPEED\_UPDATER](#particleupdater)\> | No | Yes | 
Acceleration speed.

Default value: **{range:\[0.0,0.0\]}**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| angle10+ | [ParticlePropertyOptions](#particlepropertyoptions)<number, [ACC\_ANGLE\_UPDATER](#particleupdater)\> | No | Yes | 

Acceleration direction (in angles).

Default value: **{range:\[0.0,0.0\]}**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### EmitterParticleOptions18+

interface EmitterParticleOptions<PARTICLE extends ParticleType> {
  type: PARTICLE;
  config: ParticleConfigs\[PARTICLE\];
  count: number;
  lifetime?: number;
  lifetimeRange?: number;
}

Particle configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/3ulVLrbGQ0CETPBhpSb2gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D68CEE54E5DE3136D7CE0167CA504E7415BFA848976922269071DCCE263811F)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type10+ | [PARTICLE](#particletype) | No | No | 
Particle type, which can be **IMAGE** or **POINT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| config10+ | [ParticleConfigs](#particleconfigs)\[PARTICLE\] | No | No | 

Configuration of the particle type.

The value type of **config** is subject to the value of **type**.

1\. If the type is ParticleType.POINT, the config type is [PointParticleParameters](#pointparticleparameters).

2\. If the type is ParticleType.IMAGE, the config type is [ImageParticleParameters](#imageparticleparameters).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| count10+ | number | No | No | 

Number of particles. The value is greater than or equal to -1. The value **\-1** indicates that the number of particles is infinite.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lifetime10+ | number | No | Yes | 

Lifetime of a single particle. The default value is **1000** (that is, 1000 ms, 1s). The value is greater than or equal to -1. The value **\-1** indicates that the lifetime of the particle is infinite. If the value specified is less than **\-1**, the default value is used.

Note: If you do not want the animation to keep playing, you are advised not to set the lifetime to –1, which may greatly affect the performance.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lifetimeRange12+ | number | No | Yes | 

Random integer within the range of \[lifetime – lifetimeRange, lifetime + lifetimeRange\]. After lifetimeRange is set, the particle lifecycle is a random integer within the range. The default value is 0. The value range is from 0 to positive infinity. If it is set to a negative value, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ParticleUpdaterOptions18+

interface ParticleUpdaterOptions<TYPE, UPDATER extends ParticleUpdater> {
  type: UPDATER;
  config: ParticlePropertyUpdaterConfigs<TYPE>\[UPDATER\];
}

How the color property is updated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/i9KiDUomRqKmOmcsL-1Oog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DC203DEDA81D3606F6422021EADCDFEAB82D0B7DE9CCF3C3945BD56FD8ECCDD)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type10+ | [UPDATER](#particleupdater) | No | No | 
Type of property updating.

The default value of **type** is **ParticleUpdater.NONE**. **Atomic service API**: This API can be used in atomic services since API version 11.

 |
| config10+ | [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)<[TYPE](#particleupdater)\>\[[UPDATER](#particleupdater)\] | No | No | 

How the property is updated. The available options of **type** are as follows:

1\. **ParticleUpdater.NONE**: The property does not change. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.NONE\].

2\. **ParticleUpdater.RANDOM**: The property changes randomly. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.RANDOM\].

3\. **ParticleUpdater.CURVE**: The property changes with the animation curve. In this case, the **config** type is [ParticlePropertyUpdaterConfigs](#particlepropertyupdaterconfigs)\[ParticleUpdater.CURVE\]. **Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ParticleColorUpdaterOptions18+

interface ParticleColorUpdaterOptions<UPDATER extends ParticleUpdater> {
  type: UPDATER;
  config: ParticleColorPropertyUpdaterConfigs\[UPDATER\];
}

How the color property is updated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/EgZOuK7ET0OwvIPg2GbsSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FD25EA94B7EF6216DDDC9968737B5664E20060EE519B0E43DD0564EC1F8ADB4)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type10+ | [UPDATER](#particleupdater) | No | No | 
Type of property updating.

The default value of **type** is **ParticleUpdater.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| config10+ | [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[[UPDATER](#particleupdater)\] | No | No | 

The available options of **type** are as follows:

1\. **ParticleUpdater.NONE**: The property does not change. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.NONE\].

2\. **ParticleUpdater.RANDOM**: The property changes randomly. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.RANDOM\].

3\. **ParticleUpdater.CURVE**: The property changes with the animation curve. In this case, the **config** type is [ParticleColorPropertyUpdaterConfigs](#particlecolorpropertyupdaterconfigs)\[ParticleUpdater.CURVE\].

**NOTE**

When **type** is set to **ParticleUpdater.RANDOM** or **ParticleUpdater.CURVE**, the color configuration in **updater** has higher priority than that in **range**. During the animation period specified by updater, the color changes based on the color configuration in updater. Before the animation period specified by updater, the color changes based on the color configuration in range.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ParticleColorOptions18+

The color changes randomly, with the per-second change difference being a value randomly generated from the range. The target color is obtained by applying the change difference to the current color value of each of the R, G, B, A channels.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/BbOn_X0ZTFeTxU6m11CuKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E46E88376D2DF035A1E62DAEC08E716ABEC1954531BFAE8536FED03B6B61F10)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| r10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | Difference value for the red color channel. **Atomic service API**: This API can be used in atomic services since API version 11. |
| g10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | Difference value for the green color channel. **Atomic service API**: This API can be used in atomic services since API version 11. |
| b10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | Difference value for the blue color channel. **Atomic service API**: This API can be used in atomic services since API version 11. |
| a10+ | [ParticleTuple](#particletuple18)<number, number> | No | No | Difference value for the alpha (transparency) channel. **Atomic service API**: This API can be used in atomic services since API version 11. |

#### ParticleAnnulusRegion20+

Configures the annular emitter area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Zb92AXe2Q8iDohq5G8ApMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DB2C1EAB581C870BC19D0E7072B73932BB4F2065064B1041460815213BC9345)

-   If the value of outerRadius or innerRadius is less than 0 or uses the percentage unit, the value is considered as 0.
    
-   If the value of outerRadius is less than that of innerRadius, the smaller value is used as the new inner radius and the larger value is used as the new outer radius.
    
-   If the value of endAngle is less than that of startAngle, the smaller value is used as the new start angle and the larger value is used as the new end angle.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/6Et_WGZSTuqC9DdE-4mRrA/en-us_image_0000002537765902.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D8293DD75EF95CC534E50ED6953B2B3A635403EF04F6BDF7018AA74995B8357)

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| center | [PositionT](../../../arkts-api/ui/arkui/graphics/document.md#positiont12)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | No | Yes | Center coordinates of the ring. The upper left corner of the component is the origin of the coordinates. Default value: {x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)} |
| outerRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | No | Outer radius of the ring. |
| innerRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | No | Inner radius of the ring. |
| startAngle | number | No | Yes | 
Start angle of the ring.

Unit: kWh

Default value: **0**.

 |
| endAngle | number | No | Yes | 

End angle of the ring.

Unit: kWh

Default value: **360**

 |

#### Vector2T<T>22+

type Vector2T<T> = Vector2T<T>

Defines the Vector2T type. The Vector2T type contains two attribute values: x and y.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2T<T>](../../../arkts-api/ui/arkui/graphics/document.md#vector2tt12) | 
Represents a vector of the T type that contains two values: x and y. x indicates the value in the x-axis direction of the vector. y indicates the value in the y-axis direction of the vector.

Unit: vp

 |

#### FieldRegion22+

Defines the area information of the particle field.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| shape | [DisturbanceFieldShape](#disturbancefieldshape12) | No | Yes | 
Shape of the particle field.

Default value: DisturbanceFieldShape.RECT

 |
| position | [PositionT](../../../arkts-api/ui/arkui/graphics/document.md#positiont12)<number> | No | Yes | 

Center position of the particle field. The unit of coordinates is vp.

Default value: {x:0, y:0}

 |
| size | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<number> | No | Yes | 

Size of the particle field. The unit of the value is vp.

Default value: {width:0, height:0}

The value can be:

width: \[0, +∞)

height: \[0, +∞)

If the width or height of the size is set to a negative value, the default value of width or height is used.

 |

#### RippleFieldOptions22+

Parameter that describes the information about a particle disturbance field.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| amplitude | number | No | Yes | 
Amplitude of the wave in the particle disturbance field. The greater the amplitude, the stronger the force of the disturbance field.

Value range: \[0, +∞).

Default value: **0**.

If it is set to a negative value, the default value is used.

 |
| wavelength | number | No | Yes | 

Wavelength of the wave in the particle disturbance field, that is, the distance of a wave period. The greater the wavelength, the slower the wave changes with the distance, and the less obvious the disturbance.

Value range: \[0, +∞).

Default value: **0**.

If it is set to a negative value, the default value is used.

 |
| waveSpeed | number | No | Yes | 

Wave speed in the particle disturbance field. The greater the wave speed, the faster the wave changes with time, and the more obvious the disturbance.

Value range: \[0, +∞).

Default value: **0**.

If it is set to a negative value, the default value is used.

 |
| attenuation | number | No | Yes | 

Attenuation coefficient of the wave in the particle disturbance field. The greater the attenuation coefficient, the faster the wave attenuates with time.

Value range: \[0,1\].

Default value: 0.0

If the value is not within the specified range, the default value is used.

 |
| center | [PositionT](../../../arkts-api/ui/arkui/graphics/document.md#positiont12)<number> | No | Yes | 

Center position of the force generated by the disturbance field. The upper left corner of the component is the origin of coordinates. The unit of coordinates is vp.

Default value: {x:0, y:0}

 |
| region | [FieldRegion](#fieldregion22) | No | Yes | 

Information about the area affected by the disturbance field, including the shape, size, and center position of the area.

Default value: {shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}}

 |

#### VelocityFieldOptions22+

Parameter used to describe the velocity field of particles.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| velocity | [Vector2T](#vector2tt22)<number> | No | Yes | 
Velocity values in each direction of the velocity field. A particle can only obtain the velocity when it is within the velocity field. After the particle leaves the velocity field, it will not be affected by the velocity field and will not obtain the additional velocity.

Default value: {x:0, y:0}

 |
| region | [FieldRegion](#fieldregion22) | No | Yes | 

Information about the area affected by the velocity field, including the shape, size, and center position of the area.

Default value: {shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}}

 |

#### Example

## Example 1: Initializing Particles with Circular Shapes

This example demonstrates the basic usage of particle animations by initializing particles with circular shapes.

@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: \[
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 10// Point radius.
                },
                count: 500, // Total number of particles.
                lifetime: 10000, // Particle lifetime, in ms.
                lifetimeRange: 100// Range of particle lifetime values, in ms.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: \[0, 0\],
              shape: ParticleEmitterShape.RECTANGLE// Emitter shape.
            },
            color: {
              range: \[Color.Red, Color.Yellow\], // Initial color range.
              distributionType: DistributionType.GAUSSIAN, // Random distribution of initial color values.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: \[
                  {
                    from: Color.White, // Initial value of the change.
                    to: Color.Pink, // Target value of the change.
                    startMillis: 0, // Start time.
                    endMillis: 3000, // End time.
                    curve: Curve.EaseIn// Animation curve.
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                \]
              }
            },
            opacity: {
              range: \[0.0, 1.0\], // The initial value of particle opacity is randomly generated from the \[0.0, 1.0\] range.
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
            scale: {
              range: \[0.0, 0.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
            acceleration: {
              // Acceleration. speed indicates the acceleration speed, and angle indicates the acceleration direction.
              speed: {
                range: \[3, 9\],
                updater: {
                  type: ParticleUpdater.RANDOM, // The speed changes randomly.
                  config: \[1, 20\]
                }
              },
              angle: {
                range: \[90, 90\]
              }
            }

          }
        \]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/z2eR81GQTHeMV7UkCovTKQ/en-us_image_0000002537925842.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C612A94718FC55A2B847909564AB50AA1CC4602877A17E03ADAA1357CF872FB6)

## Example 2: Initializing Particles with Images

This example demonstrates the basic usage of particle animations by initializing particles with images.

@Entry
@Component
struct ParticleExample {
  @State
  myCount: number = 100
  flag: boolean = false;

  build() {
    Column() {
      Stack() {
        Particle({
          particles: \[
            {
              emitter: {
                particle: {
                  type: ParticleType.IMAGE,
                  config: {
                    src: $r("app.media.book"),
                    size: \[10, 10\]
                  },
                  count: this.myCount,
                  lifetime: 10000,
                  lifetimeRange: 100
                },
                emitRate: 3,
                shape: ParticleEmitterShape.CIRCLE
              },
              color: {
                range: \[Color.White, Color.White\]
              },
              opacity: {
                range: \[1.0, 1.0\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[
                    {
                      from: 0,
                      to: 1.0,
                      startMillis: 0,
                      endMillis: 6000
                    },
                    {
                      from: 1.0,
                      to: 0,
                      startMillis: 6000,
                      endMillis: 10000
                    }
                  \]
                }
              },
              scale: {
                range: \[0.1, 1.0\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[
                    {
                      from: 0,
                      to: 1.5,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }

                  \]
                }
              },
              acceleration: {
                speed: {
                  range: \[3, 9\],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: \[
                      {
                        from: 10,
                        to: 20,
                        startMillis: 0,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 10,
                        to: 2,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    \]
                  }
                },
                angle: {
                  range: \[0, 180\],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: \[{
                      from: 1,
                      to: 2,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    },
                      {
                        from: 50,
                        to: -50,
                        startMillis: 1000,
                        endMillis: 3000,
                        curve: Curve.EaseIn
                      },
                      {
                        from: 3,
                        to: 5,
                        startMillis: 3000,
                        endMillis: 8000,
                        curve: Curve.EaseIn
                      }
                    \]
                  }
                }
              },
              spin: {
                range: \[0.1, 1.0\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[
                    {
                      from: 0,
                      to: 360,
                      startMillis: 0,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              },
            }
            , {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.heart'),
                  size: \[10, 10\]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: \[Color.White, Color.White\]
            },
            opacity: {
              range: \[1.0, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                \]
              }
            },
            scale: {
              range: \[0.1, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                \]
              }
            },
            acceleration: {
              speed: {
                range: \[3, 9\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              },
              angle: {
                range: \[0, 180\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 10000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              }
            },
            spin: {
              range: \[0.1, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
          }, {
            emitter: {
              particle: {
                type: ParticleType.IMAGE,
                config: {
                  src: $r('app.media.sun'),
                  size: \[10, 10\]
                },
                count: this.myCount,
                lifetime: 10000,
                lifetimeRange: 100
              },
              emitRate: 3,
              shape: ParticleEmitterShape.CIRCLE
            },
            color: {
              range: \[Color.White, Color.White\]
            },
            opacity: {
              range: \[1.0, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 6000
                  },
                  {
                    from: 1.0,
                    to: 0,
                    startMillis: 6000,
                    endMillis: 10000
                  }
                \]
              }
            },
            scale: {
              range: \[0.1, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 2.0,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }

                \]
              }
            },
            acceleration: {
              speed: {
                range: \[3, 9\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[
                    {
                      from: 10,
                      to: 20,
                      startMillis: 0,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 10,
                      to: 2,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              },
              angle: {
                range: \[0, 180\],
                updater: {
                  type: ParticleUpdater.CURVE,
                  config: \[{
                    from: 1,
                    to: 2,
                    startMillis: 0,
                    endMillis: 1000,
                    curve: Curve.EaseIn
                  },
                    {
                      from: 50,
                      to: -50,
                      startMillis: 1000,
                      endMillis: 3000,
                      curve: Curve.EaseIn
                    },
                    {
                      from: 3,
                      to: 5,
                      startMillis: 3000,
                      endMillis: 8000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              }
            },
            spin: {
              range: \[0.1, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0,
                    to: 360,
                    startMillis: 0,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
          }
          \]
        }).width(300).height(300)

      }.width(500).height(500).align(Alignment.Center)
    }.width("100%").height("100%")

  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Tbyn1OjVSRGE0UmJGrKlkQ/en-us_image_0000002568685619.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF6E1D7517B9BB4BC45E286CB93C1E365D128EFFAD8D043E96CB606E705C11BD)

## Example 3: Changing Motion Trajectories with the Particle Disturbance Field

This example demonstrates how to change the motion trajectories of particles by applying disturbances through the particle disturbance field.

@Entry
@Component
struct ParticleExample3 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: \[
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 10// Point radius.
                },
                count: 500, // Total number of particles.
                lifetime: 10000// Particle lifetime, in ms.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: \[0, 0\],
              shape: ParticleEmitterShape.RECTANGLE// Emitter shape.
            },
            color: {
              range: \[Color.Red, Color.Yellow\], // Initial color range.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: \[
                  {
                    from: Color.White, // Initial value of the change.
                    to: Color.Pink, // Target value of the change.
                    startMillis: 0, // Start time.
                    endMillis: 3000, // End time.
                    curve: Curve.EaseIn// Animation curve.
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                \]
              }
            },
            opacity: {
              range: \[0.0, 1.0\], // The initial value of particle opacity is randomly generated from the \[0.0, 1.0\] range.
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
            scale: {
              range: \[0.0, 0.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
            acceleration: {
              // Acceleration. speed indicates the acceleration speed, and angle indicates the acceleration direction.
              speed: {
                range: \[3, 9\],
                updater: {
                  type: ParticleUpdater.RANDOM,
                  config: \[1, 20\]
                }
              },
              angle: {
                range: \[90, 90\]
              }
            }

          }
        \]
      }).width(300).height(300).disturbanceFields(\[{
        strength: 10,
        shape: DisturbanceFieldShape.RECT,
        size: { width: 100, height: 100 },
        position: { x: 100, y: 100 },
        feather: 15,
        noiseScale: 10,
        noiseFrequency: 15,
        noiseAmplitude: 5
      }\])
    }.width('100%').height('100%').align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/kV3mLf5VQeqj1y4d1eOUAw/en-us_image_0000002568765629.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A4DF1A1418C2D3B204D57EAC38B5D711AF6CC300DEAAD5123F2F46837921359)

## Example 4: Adjusting the Emitter Position

This example demonstrates how to adjust the position of the particle emitter through **emitter()**.

@Entry
@Component
struct ParticleExample4 {
  @State emitterProperties: Array<EmitterProperty> = \[
    {
      index: 0,
      emitRate: 100,
      position: { x: 60, y: 80 },
      size: { width: 200, height: 200 }
    }
  \];

  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: \[
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 5// Point radius.
                },
                count: 400, // Total number of particles.
                lifetime: -1// Particle lifetime. The value -1 indicates that the lifetime of the particle is infinite.
              },
              emitRate: 10, // Number of particles emitted per second.
              position: \[0, 0\], // Emitter position.
              shape: ParticleEmitterShape.CIRCLE// Emitter shape.
            },
            color: {
              range: \[Color.Red, Color.Yellow\], // Initial color range.
              updater: {
                type: ParticleUpdater.CURVE, // Change with the animation curve.
                config: \[
                  {
                    from: Color.White,
                    to: Color.Pink,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Pink,
                    to: Color.Orange,
                    startMillis: 3000,
                    endMillis: 5000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: Color.Orange,
                    to: Color.Pink,
                    startMillis: 5000,
                    endMillis: 8000,
                    curve: Curve.EaseIn
                  },
                \]
              }
            },
          },
        \]
      })
        .width(300)
        .height(300)
        .emitter(this.emitterProperties)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/xESPGBaTQ3SqZ-_8oxasIQ/en-us_image_0000002537765904.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9259540D7673D9AD56DB376C41603FB76DD9EA4810DA540BF7935DA070683FE)

## Example 5: Creating a Ring Emitter

This example describes the basic usage of creating a ring emitter.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ParticleExample5 {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor(Color.Black)
      Particle({
        particles: \[
          {
            emitter: {
              particle: {
                type: ParticleType.POINT, // Particle type.
                config: {
                  radius: 5 // Dot radius
                },
                count: 2000, // Total number of particles
                lifetime: 10000, // Particle lifetime, in ms.
                lifetimeRange: 100// Range of particle lifetime values, in ms.
              },
              emitRate: 100, // Number of particles emitted per second
              shape: ParticleEmitterShape.ANNULUS, // Ring emitter
              annulusRegion:{
                center:{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)}, // Coordinates of the center of the ring
                innerRadius:LengthMetrics.vp(100), // Outer radius of the ring
                outerRadius:LengthMetrics.vp(120), // Inner radius of the ring
                startAngle:0, // Start angle of the ring
                endAngle:360 // End angle of the ring
              }
            },
            color: {
              range: \[Color.Pink, Color.White\],
            },
            opacity: {
              range: \[0.0, 1.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 1.0,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  },
                  {
                    from: 1.0,
                    to: 0.0,
                    startMillis: 5000,
                    endMillis: 10000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
            scale: {
              range: \[0.0, 0.0\],
              updater: {
                type: ParticleUpdater.CURVE,
                config: \[
                  {
                    from: 0.0,
                    to: 0.5,
                    startMillis: 0,
                    endMillis: 3000,
                    curve: Curve.EaseIn
                  }
                \]
              }
            },
          }
        \]
      }).width(300).height(300)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Qm4zWZDCTHa9jtqVQRZ0AQ/en-us_image_0000002537925844.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=963ABC37A7D49988EE34B5F7EED17103E19693BBBAE56E4E0883EC00435BE5E9)

## Example 6: Updating the Ring Emitter

This example describes the basic usage of updating the ring emitter of a particle animation.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ParticleExample6 {

  @State radius: number = 1;
  @State shape: ParticleEmitterShape = ParticleEmitterShape.ANNULUS;
  @State emitRate: number = 200;
  @State count: number = 2000;
  private timerID: number = -1;
  private centerX: LengthMetrics = LengthMetrics.percent(0.5);
  private centerY: LengthMetrics = LengthMetrics.percent(0.5);
  private inRadius: LengthMetrics = LengthMetrics.vp(120);
  private outRadius: LengthMetrics = LengthMetrics.vp(120);
  private startAngle: number = 0;
  private endAngle: number = 90;
  @State emitterProperties: Array<EmitterProperty> = \[
    {
      index: 0,
      emitRate: 100,
      annulusRegion: {
        center:{x:this.centerX, y: this.centerY}, // Center coordinates of the ring
        outerRadius: this.outRadius, // Outer radius of the ring
        innerRadius: this.inRadius, // Inner radius of the ring
        startAngle: -90, // Start angle of the ring
        endAngle: 0 // End angle of the ring
      }
    }
  \]
  @State region: ParticleAnnulusRegion = {
    center:{x:this.centerX, y: this.centerY},
    outerRadius: this.outRadius,
    innerRadius: this.inRadius,
    startAngle: -90,
    endAngle: 0
  }

  aboutToDisappear(): void {
    // Clear the timer when the page is destroyed.
    if (this.timerID != -1) {
      clearInterval(this.timerID);
    }
  }

  build() {
    Column({ space: 10}) {
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)

        Particle({
          particles: \[
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // Particle type.
                  config: {
                    radius: this.radius // Dot radius
                  },
                  count: this.count, // Total number of particles
                  lifetime: -1 // Particle lifecycle. The value -1 indicates that the particle lifecycle is infinite.
                },
                emitRate: this.emitRate, // Number of particles emitted per second
                shape: this.shape, // Shape of the emitter
                annulusRegion: this.region
              },
              color: {
                range: \[Color.White, Color.Pink\], // Initial color range
              },
            },
          \]
        }).width('100%')
          .height('100%')
          .emitter(this.emitterProperties)
          .onClick(()=>{
            // Clear the existing timer.
            if (this.timerID != -1) {
              clearInterval(this.timerID);
            }

            // Create a timer (update every second).
            this.timerID = setInterval(() => {
              this.emitterProperties = \[
                {
                  index: 0,
                  emitRate: this.emitRate,
                  annulusRegion: {
                    center:{x:this.centerX, y: this.centerY},
                    outerRadius: this.outRadius,
                    innerRadius: this.inRadius,
                    startAngle: this.startAngle,
                    endAngle: this.endAngle
                  }
                }
              \];
              if (this.endAngle >= 270) {
                if (this.timerID != -1) {
                  clearInterval(this.timerID);
                }
                return;
              }
              // Update the angle value (30 degrees per second).
              this.startAngle += 30;
              this.endAngle += 30;
            }, 1000);

          })
      }
      .width('100%')
      .height('100%')
      .align(Alignment.Center)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/bIMrDIExS-ePAM3ju8K0LA/en-us_image_0000002568685621.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F5419E9B3B9ABF313E616B8B40EAB93351E6933596A830A91763D55CFF1C4D8)

## Example 7: Setting the Ripple Field and Velocity Field

Starting from API version 22, the ripple field and velocity field can be set for particles. This example shows how to use the rippleFields API to set the ripple field of particles to produce a ripple effect. The velocityFields API is used to set the velocity field of particles, so that the velocity specified by the velocity field is added to the original velocity of particles.

// xxx.ets
@Entry
@Component
struct ParticleExample {
  @State count: number = 1000
  @State particle: EmitterParticleOptions<ParticleType> = {
    type: ParticleType.POINT, // Particle type.
    config: {
      radius: 1 // Radius of the dot
    },
    count: this.count, // Total number of particles
    lifetime: 9000, //Particle lifetime, in ms
    lifetimeRange: 100 // Range of particle lifetime values, in ms.
  }
  build() {
    Column() {
      Text('Wave field')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: \[
            {
              emitter: {
                particle: this.particle,
                emitRate: 10000, //Number of particles emitted per second
                position: \[0, 0\],
                shape: ParticleEmitterShape.RECTANGLE // Emitter shape.
              },
              color: {
                range: \[Color.White, Color.White\], // initial color range
              },
              scale: {
                range: \[0.2, 1.5\], //Initial size range
              },
              opacity : {
                range: \[0.2, 0.8\], //Initial transparency range
              }
            }
          \]
        }).width(300).height(300)
          .rippleFields(\[
            {
              amplitude: 120, //Amplitude of the wave field
              wavelength: 500, //Wavelength of the wave field
              waveSpeed: 220, //Wave speed of the wave field
              center: { x: 150, y: 150 }, //Center of the force field of the wave field
              attenuation: 0, //Attenuation coefficient of the wave field over time
              region: {
                //Affected area of the wave field.
                shape: DisturbanceFieldShape.RECT, // Shape of the disturbance field's affected area
                position: { x: 150, y: 150 }, // Center of the disturbance field's affected area
                size: { width: 300, height: 300 } // Size of the disturbance field's affected area
              }
            }
          \])
      }.width("100%").height(300).align(Alignment.Center)
      Text ('Velocity field')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Stack() {
        Text()
          .width(300).height(300).backgroundColor(Color.Black)
        Particle({
          particles: \[
            {
              emitter: {
                particle: {
                  type: ParticleType.POINT, // Particle type.
                  config: {
                    radius: 2 // Radius of the dot
                  },
                  count: 1000, // Total number of particles
                  lifetime: 1000, // Particle lifetime, in ms
                  lifetimeRange: 0 // Particle lifetime range, in ms
                },
                emitRate: 120, // Number of particles emitted per second
                position: \[0, 0\],
                size: \[300, 300\],
                shape: ParticleEmitterShape.RECTANGLE // Emitter shape.
              },
              color: {
                range: \[Color.White, Color.White\], // Initial color range
              },
              opacity: {
                range: \[1.0, 1.0\],
                updater: {
                  type: ParticleUpdater.CURVE, // Transparency changes by curve
                  config: \[
                    {
                      from: 1.0,
                      to: 0.0,
                      startMillis: 0,
                      endMillis: 1000,
                      curve: Curve.EaseIn
                    }
                  \]
                }
              },
            }
          \]
        }).width(300).height(300)
          .margin({ top: 30 })
          .velocityFields(\[
            {
              velocity: { x: 100, y: 0 }, // Velocity of the velocity field
              region: {
                // Affected area of the velocity field
                shape: DisturbanceFieldShape.RECT, // Shape of the velocity field's affected area
                position: { x: 150, y: 150 }, // Center of the area affected by the velocity field
                size: { width: 200, height: 200 } // Size of the area affected by the velocity field.
              }
            }
          \])
      }.width("100%").height(300).align(Alignment.Center)
    }
  }
}
