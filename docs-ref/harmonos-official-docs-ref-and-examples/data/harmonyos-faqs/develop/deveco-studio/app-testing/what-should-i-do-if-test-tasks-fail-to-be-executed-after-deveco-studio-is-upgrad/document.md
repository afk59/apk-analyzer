# What should I do if test tasks fail to be executed after DevEco Studio is upgraded?

**Symptom**

After DevEco Studio is upgraded, a test task fails to be run in an existing project.

**Solution**

The issue occurs because after DevEco Studio is upgraded, the test framework hypium version and the OpenHarmonyTestRunner template within the framework are incompatible with the original project. The recommended solutions are as follows:

-   Solution 1: Create a project in DevEco Studio after the upgrade, and migrate the original test tasks.
-   Solution 2: Upgrade the original project.
    -   Upgrade the Hypium plugin to the latest version in the project-level **oh-package.json5** file.
    -   Replace the **OpenHarmonyTestRunner** entry file template: Create a project and copy the **src/ohosTest/ets/testrunner/OpenHarmonyTestRunner.ets** file to the same directory in the original project.
    -   After replacing the files, you will still need to fix any errors based on the editor's error messages.
