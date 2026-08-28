# Configuring the Client ID

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, find your desired app, and click it to access the **Project settings** page. On the **General information** tab page, find the client ID under **App information**.
    
2.  In the _module.json5_ file of the **entry** module in the project, add the **metadata** section, in which you should set **name** to **client\_id** and **value** to the client ID obtained in the previous step.
    
    "module": {
      "name": "xxxx",
      "type": "entry",
      "description": "xxxx",
      "mainElement": "xxxx",
      "deviceTypes": \[\],
      "pages": "xxxx",
      "abilities": \[\],
      "metadata": \[ // Configure the following information:
        {
          "name": "client\_id",
          "value": "xxxxxx"
        }
      \]
    }
