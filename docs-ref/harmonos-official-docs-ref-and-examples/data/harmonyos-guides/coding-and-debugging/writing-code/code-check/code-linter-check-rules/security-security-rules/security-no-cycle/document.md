# @security/no-cycle

Disallow cyclic dependencies.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';

#### Example of Incorrect Code

// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/4bOJY6TeS36fyBm2vvCrbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062144Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=438132B200BFEFF4E41112F50B81E7E72BDB6B5B5480ACF491D822803DB218F5)

In the preceding example, the **foo.ets** file depends on the **bar.ets** file, and the **bar.ets** file also depends on the **foo.ets** file, resulting in a cyclic dependency.

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
