# How do I resolve the "@Consume/@Link decorated property <propertyName> not initialized" error during preview?

**Symptom**

During preview, a blank screen is displayed, and the error message "Preview failed. View details in the PreviewerLog window." is displayed in the upper part.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/KGNVuCr5SQKdJ-0x0zuNTg/en-us_image_0000002194317968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=218DF5FF7F8E042CFA35D8ECDE7A91B15B4ADF5DCB7C4849F5B5CF8AEDB8B9C6 "Click to enlarge")

The warning message "@Consume/@Link decorated property <propertyName> not initialized." is displayed in the PreviewerLog window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/pgvN0mVISyqPBJF4t7zA-A/en-us_image_0000002194158348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5983404F45EA236C83CF3EA6884C4919E1DD5D26873F8CE084DD1F051F2AF58B)

**Solution**

Since members decorated with @Consume/@Link need to be bound to the parent component and cannot complete initialization when previewed in isolation, previewing pages or components that contain members decorated with @Consume (or @Link) may result in a blank screen.

Avoid directly previewing such components. Instead, preview how they look through their parent components.

The sample code is as follows:

// Suggest adding @ Preview on ParentComp to preview the preview effect of ChildComp
@Preview
@Component
struct ParentComp {
  // @Provide decoration is provided by the entrance component ParentComp as its descendant component
  @Provide reviewVotes: number = 10;

  build() {
    Column() {
      Button(\`reviewVotes(${this.reviewVotes}), give +1\`)
        .onClick(() => this.reviewVotes += 1)
      ChildComp()
    }
  }
}

// @Preview is not recommended to directly preview ChildComp
@Component
struct ChildComp {
  // The variable decorated with '@Consume' is bound to the variable decorated with '@Provide' in its ancestor component ParentComp using the same attribute name
  @Consume reviewVotes: number;
  build() {
    Column() {
      Text(\`reviewVotes(${this.reviewVotes})\`)
      Button(\`reviewVotes(${this.reviewVotes}), give +1\`)
        .onClick(() => this.reviewVotes += 1)
    }
    .width('50%')
  }
}
