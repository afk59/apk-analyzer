# Why does the files in the src/main/cpp directory of the Static Library module fail to be packaged into the HAR?

**Symptom**

Click **Build** > **Make Module ${libraryName}** to compile and build a HAR, but files in the **cpp** directory are not displayed in the build products.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/iQS9pY16Ra-YEML10yLtEg/en-us_image_0000002229758217.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=541E6C1D80F9BDE36849B71FC4285B05A938486F27F7E418C361B810FA0748C5)

**Solution**

If hvigor 2.5.0-s or later version is used, only the local dependencies in **dependencies** are packed into the .har file during compilation and build, the dependencies in **devDependencies** are not packaged into the .har file.

Move the local dependency in **devDependencies** to **dependencies** and recompile.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/PL2rjTx6TSKWeSt1HE1viQ/en-us_image_0000002229603749.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB07E8A77F9C3594881683456F7C6C25876B4C798F96DBEDFA07E787B721A816)
