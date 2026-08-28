# How do I convert an HSP into a HAR?

**Solution**

1\. In the **module.json5** file of the HSP, change **"type": "shared"** to **"type": "har"** and delete the **deliveryWithInstall** and **pages** fields.

2\. In the **oh-package.json5** file of the HSP, delete the **packageType** field.

3\. Remove the pages from the HSP. If you want to use them as pages, change them to use named routing.

4\. Find the **hvigorfile.ts** file in the HSP directory and change **hspTasks** to **harTasks**.

5\. Compile the module.

If any other errors occur during compilation, follow the error messages to locate and fix the corresponding issues.
