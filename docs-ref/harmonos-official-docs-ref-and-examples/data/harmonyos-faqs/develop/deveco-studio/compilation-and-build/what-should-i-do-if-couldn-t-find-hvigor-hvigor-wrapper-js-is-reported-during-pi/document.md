# What should I do if "Couldn't find hvigor/hvigor-wrapper.js" is reported during pipeline build?

1.  The hvigorw script depends on the **hvigor-wrapper.js** file.
2.  When a script is used for compilation outside a project:
    1.  Check whether the **hvigor-wrapper.js** file is in the **hvigor** folder of the project.
    2.  According to [Creating a Pipeline](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-command-line-building-app#section14397105115226), you need to run the **cd** command to go to the root directory of the project, and then call the commands of the **.hvigorw** file.
