# What should I do if "Schema validate failed" is reported during compilation?

**Symptom**

"Schema validate failed" is reported during compilation in DevEco Studio.

**Solution**

Locate the fault based on the error information as the fields in the configuration file are missing or misspelled.

For example, if **name** in the **abilities** tag in **module.json5** file is misspelled as **nam**, information similar to the following is displayed:

Detail: Please check the following fields.
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'srcEntrance' },
  message: "must have required property 'srcEntrance'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'oneOf',
  params: { passingSchemas: null },
  message: 'must match exactly one schema in oneOf',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'enum',
  params: {
    allowedValues: \[
      'priority',
      'name',
      'srcEntrance',
      'srcEntry',
      'launchType',
      'description',
      'icon',
      'label',
      'permissions',
      'metadata',
      'visible',
      'exported',
      'skills',
      'backgroundModes',
      'continuable',
      'startWindowIcon',
      'startWindowBackground',
      'removeMissionAfterTerminate',
      'orientation',
      'supportWindowMode',
      'maxWindowRatio',
      'minWindowRatio',
      'maxWindowWidth',
      'minWindowWidth',
      'maxWindowHeight',
      'minWindowHeight',
      'excludeFromMissions'
    \]
  },
  message: 'must be equal to one of the allowed values',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'propertyNames',
  params: { propertyName: 'nam' },
  message: 'property name must be valid',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 

The preceding information is used as an example to explain the meaning of keywords in the error information, helping you locate and rectify the fault.

-   **instancePath**: location of the error in the file; **'module.abilities\[0\]'**: the first **abilities** in the **module.json5** file.
-   **keyword**: optional properties of the current error field, including **required**, **oneOf**, **enum**, and **propertyNames**.
    -   **required**: indicates that the field is mandatory. If the field is missing or incorrectly spelled, the property configuration fails.
    -   **oneOf**: indicates that the current configuration does not meet the **oneOf** requirement. You can locate the error reported on the **abilities** tag through the **instancePath** key word. In DevEco Studio, press **Ctrl** and click **abilities** to go to the corresponding **module.json** file. You can see that one of the following two groups must be configured. By comparison, the **name** property is not configured due to misspelling.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/lVFRJKU_S2mGx_gtu-r9vg/en-us_image_0000002194158784.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53F89E540BB73665E58A6E2A06EFB187E00839AE71AC110CFB61C52097D9F4D2)
        
    -   **enum**: all configurable properties. You can determine the correct property format based on the enumerated values.
    -   **propertyNames**: When the field is misspelled, **propertyName: 'nam'** indicates that **nam** is misspelled.
-   **params**: Different keywords correspond to different detailed descriptions. For example, when **keyword** is **required**, **missingProperty: 'name'** in **params** indicates that the **name** property is missing.
-   **message**: description of the modification requirements. For example, when **keyword** is **required**, **message** indicates that the **name** property is required.
-   **location**: specific location of the error. Click this keyword to locate the error.
