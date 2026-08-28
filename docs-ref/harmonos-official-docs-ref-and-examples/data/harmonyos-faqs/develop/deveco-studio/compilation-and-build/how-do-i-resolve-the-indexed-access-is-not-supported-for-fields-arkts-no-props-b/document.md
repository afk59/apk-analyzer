# How do I resolve the "Indexed access is not supported for fields(arkts-no-props-by-index)" error?

**Symptom**

Dynamically accessing fields of a class or interface results in a compilation error with the message: "Indexed access is not supported for fields (arkts-no-props-by-index)."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/j1IxPpTSSXm8e6yRtY67fQ/en-us_image_0000002229604089.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=048BDDAFA4B989CC4ACB343C63114C42D07D2700DC8A15699DB8430CA8D671B2)

**Solution**

Modify the code.

getValue(breakpoint: string): T {
  return Reflect.get(this.options, breakpoint) as T;
}
