# How do I configure dynamic dependencies in oh-package.json5?

In the **oh-package.json5** file:

-   **dependencies**: declares production dependencies, that is, HarmonyOS third-party libraries to be imported in the code, which are used in the build and running phases.
-   **devDependencies**: declares development dependencies, which are used in the development or testing phase of a project.
-   **dynamicDependencies**: configures HSP modules that are dynamically loaded.

The sample code is as follows:

{
  "name": "parameter-test",
  "version": "@param:version",
  "modelVersion": "5.0.4",
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  },
  "parameterFile": '.parameterFile/parameterFile.json5',// Enable parameterization and specify the path to the parameterized configuration file
}

**Reference**

[oh-package.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-oh-package-json5)

[Adding Dependencies](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-dependencies)
