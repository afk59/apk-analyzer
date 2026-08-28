# Understanding the Logic for Checking HAP Uniqueness

A HAP is the basic unit for app installation. In the DevEco Studio project directory, one HAP corresponds to one module. During app packaging, a .hap file is generated for each module.

If an app has multiple modules, multiple .hap files are packed into a bundle (an .app file) when the app is released in AppGallery Connect. When distributed on the cloud or installed on a device, HAPs are used.

To ensure successful distribution and installation of an app, ensure that the module names, ability names, and the module of the **entry** type corresponding to the target device are unique.

DevEco Studio checks the HAP uniqueness during the build process. If the check fails, the build fails or an alarm is generated.

#### Checking Modules

The module names of an app must be unique for a device.

1.  Check **Name** of each module. The check is successful if the module names are different. If duplicate module names are detected, check the value of **deviceType**.
2.  Check **deviceType**. The check is successful if the modules do not have the same **deviceType**. If the modules have the same device type, check **distributionFilter**.
    
    As shown in the following example, module 1 and module 2 have different device types.
    
    // Module 1 and module 2 are configured with different device types.
    //Module1
    {
      "deviceType": \["tv", "tablet"\]
    }
    //Module2
    {
      "deviceType": \["car"\]
    }
    
    As shown in the following example, module 1 and module 2 have the same device type **tablet**.
    
    // Module 1 and module 2 contain device type tablet.
    //Module1
    {
      "deviceType": \["tv", "tablet"\]
    }
    //Module2
    {
      "deviceType": \["car", "tablet"\]
    }
    
3.  Check **distributionFilter**.
    
    **distributionFilter** contains the **apiVersion**, **screenShape**, **screenWindow**, **screenDensity**, and **countryCode** attributes.
    
    -   The check is successful if the modules have at least one different attribute value in **distributionFilter**.
    -   The check fails if all the attribute values in **distributionFilter** of the modules are the same.
    
    As shown in the following example, the two modules have the same **apiVersion**, **screenShape**, **screenWindow** and **screenDensity** but different **countryCode**s. The check is successful since the two modules can be distinguished by **countryCode**.
    
    // The check is successful because the two modules have different country codes in distributionFilters.
    //Module1
    {
      "distributionFilter": {
        "apiVersion" : {
          "policy": "include",
          "value": \[10,11\]
        },
        "screenShape": {
          "policy": "include",
          "value": \["rect"\]
        },
        "screenWindow": {
          "policy": "include",
          "value": \["454\*454", "466\*466"\]
        },
        "screenDensity": {
          "policy": "include",
          "value": \["ldpi", "xldpi"\]
        },
        "countryCode": {
          "policy": "include",
          "value": \["CN", "HK"\]
        }
      }
    }
    //Module2
    {
      "distributionFilter": {
        "apiVersion" : {
          "policy": "include",
          "value": \[10,11\]
        },
        "screenShape": {
          "policy": "include",
          "value": \["rect"\]
        },
        "screenWindow": {
          "policy": "include",
          "value": \["454\*454", "466\*466"\]
        },
        "screenDensity": {
          "policy": "include",
          "value": \["ldpi", "xldpi"\]
        },
        "countryCode": {
          "policy": "include",
          "value": \["USA", "UK"\]
        }
      }
    }
    

#### Checking Abilities

The ability names of an app must be unique for a device.

1.  Check **Name** of each ability. The check is successful if the ability names are different. If a duplicate ability name is detected, check **deviceType** of the module to which the ability belongs.
2.  Check **deviceType** of the module to which the ability belongs. The check is successful if the modules do not have the same **deviceType**. If a duplicate **deviceType** is detected, check **distributionFilter** of the module to which the ability belongs.
    
    As shown in the following example, the check is successful because the two abilities with the same name have different device types.
    
    // Although Ability1 and Ability2 have the same name, the deviceType values of the modules to which they belong are different. The check is successful.
    // Ability1
    {
      "module": {
        "name": "module\_sample1",
        "deviceType": \["tv", "tablet"\],
        "abilities": \[
          {
            "name": "ability\_sample"
          }
        \]
      }
    }
    // Ability2
    {
      "module": {
        "name": "module\_sample2",
        "deviceType": \["car"\],
        "abilities": \[
          {
            "name": "ability\_sample"
          }
        \]
      }
    }
    
3.  Check **distributionFilter** of the module to which the ability belongs. The check is successful if the two abilities have at least one different **distributionFilter** attribute. Otherwise, the check fails.
    
    As shown in the following example, the two abilities with the same name and **deviceType** have different **distributionFilter** attributes. The check is successful.
    
    // Although Ability1 and Ability2 have the same ability name and the same deviceType, they have different distributionFilter attributes for the modules to which Ability1 and Ability2 belong.
    // Ability1
    {
      "module": {
        "name": "module\_sample",
        "deviceType": \["tv", "tablet"\],
        "metadata": \[
          {
            "name": "distributionFilter\_config",
            "resource": "$profile:distributionFilter\_config\_sample1"
          }
        \],
        "abilities": \[
          {
            "name": "ability\_sample"
          }
        \]
      }
    }
    // distributionFilter of the module to which Ability1 belongs.
    {
      "distributionFilter": {
        "apiVersion" : {
          "policy": "include",
          "value": \[10,11\]
        },
        "screenShape": {
          "policy": "include",
          "value": \["rect"\]
        },
        "screenWindow": {
          "policy": "include",
          "value": \["454\*454", "466\*466"\]
        },
        "screenDensity": {
          "policy": "include",
          "value": \["ldpi", "xldpi"\]
        },
        "countryCode": {
          "policy": "include",
          "value": \["CN", "HK"\]
        }
      }
    }
    
    // Ability2
    {
      "module": {
        "name": "module\_sample2",
        "deviceType":  \["tv", "tablet"\],
        "metadata": \[
          {
            "name": "distributionFilter\_config",
            "resource": "$profile:distributionFilter\_config\_sample2"
          }
        \],
        "abilities": \[
          {
            "name": "ability\_sample"
          }
        \]
      }
    }
    // distributionFilter of the module to which Ability2 belongs.
    {
      "distributionFilter": {
        "apiVersion" : {
          "policy": "include",
          "value": \[10,11\]
        },
        "screenShape": {
          "policy": "include",
          "value": \["rect"\]
        },
        "screenWindow": {
          "policy": "include",
          "value": \["454\*454", "466\*466"\]
        },
        "screenDensity": {
          "policy": "include",
          "value": \["ldpi", "xldpi"\]
        },
        "countryCode": {
          "policy": "include",
          "value": \["USA", "UK"\]
        }
      }
    }
    

#### Checking Entry

In a bundle, the target device has only one module of the **entry** type, and the modules of the **feature** type also have a module of the **entry** type on the target devices specified by **deviceType** and **distributionFilter**.

1.  Check that the modules of the **feature** type have a module of the **entry** type on the target devices specified by **deviceType** and **distributionFilter**.
    
    In the bundle shown in the following example, Module1 is of the **entry** type, and it supports tablets and wearables and can be distributed to circular and rectangular screens; Module2 is of the **feature** type and can be distributed to tablets and wearables with a rectangular screen. Since the tablets and wearables with a rectangular screen have Module1 of the **entry** type, the check is successful.
    
    // Module1 is of the entry type.
    {
      "module": {
        "name": "module\_sample1",
        "type": "entry",
        "deviceType": \["tablet", "wearable"\],
        "metadata": \[
          {
            "name": "distributionFilter\_config",
            "resource": "$profile:distributionFilter\_config1"
          }
        \]
      }
    }
    // distributionFilter of Module1 in distributionFilter\_config1.json.
    {
      "screenShape":{
        "policy": "include",
        "value": \["circle", "rect"\]
      }
    }
    // Module2 is of the feature type.
    {
      "module": {
        "name": "module\_sample2",
        "type": "feature",
        "deviceType": \["tablet", "wearable"\],
        "metadata": \[
          {
            "name": "distributionFilter\_config",
            "resource": "$profile:distributionFilter\_config2"
          }
        \]
      }
    }
    // distributionFilter of Module2 in distributionFilter\_config2.json.
    {
      "screenShape":{
        "policy": "include",
        "value": \["rect"\]
      }
    }
    
2.  Check that the target device has only one module of the **entry** type.
    
    1.  Check **deviceType** of the modules of the **entry** type. The check is successful if the modules do not have the same **deviceType**. If duplicate **deviceType** is detected, check **distributionFilter** of the modules.
        
        The bundle in the following example has two modules of the **entry** type: Module1 and Module2. The check is successful because the two modules have different device types.
        
        // Module1 is of the entry type.
        {
          "module": {
            "name": "module\_sample1",
            "type": "entry",
            "deviceType": \["tablet"\]
          }
        }
        // Module2 is of the entry type.
        {
          "module": {
            "name": "module\_sample2",
            "type": "entry",
            "deviceType": \["wearable"\]
          }
        }
        
    2.  Check **distributionFilter** of the modules of the **entry** type. The check is successful if the modules have at least one different **distributionFilter** attribute. Otherwise, the check fails.
        
        The bundle in the following example has two modules of the **entry** type: Module1 and Module2. Module1 and Module2 support the same type of device but different screen shapes. Therefore, the check is successful.
        
        // Module1 is of the entry type.
        {
          "module": {
            "name": "module\_sample1",
            "type": "entry",
            "deviceType": \["wearable"\],
            "metadata": \[
              {
                "name":"distributionFilter\_config",
                "resource": "$profile:distributionFilter\_sample1"
              }
            \]
          }
        }
        // distributionFilter of Module1 in distributionFilter\_sample1.json.
        {
          "distributionFilter": {
            "screenShape":{
              "policy": "include",
              "value": \["rect"\]
            }
          }
        }
        // Module2 is of the entry type.
        {
          "module": {
            "name": "module\_sample2",
            "type": "entry",
            "deviceType": \["wearable"\],
            "metadata": \[
              {
                "name":"distributionFilter\_config",
                "resource": "$profile:distributionFilter\_sample2"
              }
            \]
          }
        }
        // distributionFilter of Module2 in distributionFilter\_sample2.json.
        {
          "distributionFilter": {
            "screenShape":{
              "policy": "include",
              "value": \["circle"\]
            }
          }
        }
