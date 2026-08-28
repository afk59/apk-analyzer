# How do I view the detailed build process?

In the **hvigor-config.json5** file under the **hvigor** directory, uncomment the line "logging": { // "level": "info" } by removing the '//' before it, and change the value from **'info'** to **'debug'**, so that it becomes **"logging": { "level": "debug" }**. With this change, you will be able to see the detailed build process.
