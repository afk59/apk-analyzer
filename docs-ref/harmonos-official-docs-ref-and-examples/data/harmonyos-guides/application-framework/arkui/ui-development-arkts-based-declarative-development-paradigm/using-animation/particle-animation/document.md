# Particle Animation

[Particle animation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation) is created using the **Particle** component and consists of a multitude of particles that are randomly generated within a specified area. These particles can take the form of points, images, or other shapes. By animating different aspects of the particles, such as color, opacity, scale, velocity, acceleration, and spin angle, you can create engaging and dynamic visual effects. For example, you can simulate an impressive snowfall animation by animating the particles to represent snowflakes.

Below is a simple implementation of the particle animation:

@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor('rgb(240, 250, 255)')
      Particle({ particles: \[
        {
          emitter: {
            particle: {
              type: ParticleType.POINT, // Particle type.
              config: {
                radius: 5 // Point radius.
              },
              count: 100, // Total number of particles.
            },
          },
          color:{
            range:\['rgb(39, 135, 217)','rgb(0, 74, 175)'\], // Initial color range.
          },
        },
      \]
      }).width(250).height(250)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/VHpuTzo1TWqTPZyDlWZemA/en-us_image_0000002568764539.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=627A5AB2ED1D168BE0C0644390CC2528C5F0DF5B5F75CA85EB7C204095508B1C)

#### Implementing a Particle Emitter

A particle emitter in particle animation is primarily used to define the initial properties (such as type and position), of particles, control the rate of particle emission, and manage the lifecycle of the particles. You can update the position of the emitter by adjusting the emitter position, emission rate, and emission window size using the [emitter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation#emitter12) API.

// ...
@State emitterProperties: Array<EmitterProperty> = \[
  {
    index: 0,
    emitRate: 100,
    position: { x: 60, y: 80 },
    size: { width: 200, height: 200 }
  }
\]

Particle(...).width(300).height(300).emitter(this.emitterProperties) // Dynamically adjust the position of the particle emitter.
// ...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/wUOZbRl6RKugwmedhEwcnQ/en-us_image_0000002537764814.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CA3B16DBE7FEDAA5D22985E54BC2E61B5DB1A3B5D5D99CE27A995B4A5850AE8)

#### Setting the Particle Color

Use the [range](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation#particlecolorpropertyoptions) property to define the initial color range for particles, and the [distributionType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation#particlecolorpropertyoptions) property to specify how the initial color's random values are distributed. You can choose between uniform distribution or normal (Gaussian) distribution.

// ...
color: {
  range: \['rgb(39, 135, 217)','rgb(0, 74, 175)'\], // Initial color range.
  distributionType: DistributionType.GAUSSIAN // Random value distribution type of the initial color.
},
// ...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/h-77Gu4YSX6bFy1DiJ39Xw/en-us_image_0000002537924754.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE8F087854F049F3983D3EF252B5D22C5B046C3C8A692A020A377A98724EB50E)

#### Setting the Particle Lifetime

The lifetime of a particle, from creation to expiration, is used to specify how long a particle exists. Use the **lifetime** and **lifetimeRange** properties of [EmitterParticleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation#emitterparticleoptions18) to define the particle lifetime.

// ...
emitter: {
  particle: {
    // ...
    lifetime: 300, // Particle lifetime, in ms.
    lifetimeRange: 100 // Range of particle lifetime values, in ms.
  },
  emitRate: 10, // Number of particles emitted per second.
  position: \[0, 0\],
  shape: ParticleEmitterShape.RECTANGLE // Emitter shape.
},
color: {
  range: \['rgb(39, 135, 217)','rgb(0, 74, 175)'\], // Initial color range.
},
// ...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/ABkQYSGyQuqqewNUgHNpIQ/en-us_image_0000002568684531.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92EC85B9EB0AEC3CC85F3CC1DDF301CCC6D125826C963369CC301F078B63E9E4)

#### Setting the Particle Disturbance Field

A disturbance field is a mechanism used to influence the motion of particles in a particle animation. It works by applying specific forces to particles within a defined spatial area, thereby altering their trajectories and behaviors. This results in more complex and natural-looking animation effects, adding a touch of realism to the particle movement. Use [disturbanceFields](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-particle-animation#disturbancefields12) to set the disturbance field.

// ...
Particle({ particles: \[
  {
    emitter: // ...
    color: // ...
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
    acceleration: { // Acceleration. speed indicates the acceleration speed, and angle indicates the acceleration direction.
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
// ...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QFMcYCB4SOu5S9ixH64k6g/en-us_image_0000002568764541.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061937Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FE3CF49FC5B3D5350C41F235798E4B9D70B7B30B0380DE5A4E71A3F1D279A61)
