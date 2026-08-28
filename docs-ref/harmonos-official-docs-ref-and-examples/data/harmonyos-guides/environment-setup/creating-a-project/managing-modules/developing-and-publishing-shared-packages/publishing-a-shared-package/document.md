# Publishing a Shared Package

You can publish a HAR for it to be installed and referenced by other developers. The following describes how to publish a HAR.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/mvUKznsuTRGuFg_wAde4EQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC2D2D98928721CB0E9E9901C6949E0DF8211B0A73C094BB2DCAD11691131F53)

To the OpenHarmony third-party library central repository mentioned below, only HARs can be published, but not HSPs. To share an HSP in an app, release it to a private repository. For details, see [ohpm-repo: Private Repository Setup Tool](../../ohpm-repo-private-repository-setup-tool/overview/document.md).

1.  Add the following files to the HAR module directory (in the same directory as the **src** folder):
    
    -   **README.md** file: contains the description, reference mode, and more necessary information of the HAR.
    -   **CHANGELOG.md** file: contains the version changes of the HAR.
    -   **LICENSE** file: contains the license of the HAR.
    
2.  [Rebuild the HAR module](../developing-a-static-shared-package/document.md#section7892044183814) to generate a .har file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/5DDJcYJJSn6Z-CYieRQg1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDE64D936555B53F09BE11BE32EC477B5EB65D277C246569EBC7F30317ACC18F)
    
    If the **version** field in the module-level **oh-package.json5** file of the HAR package is modified, choose **Build** > **Clean Project** in DevEco Studio and then perform a full rebuild.
    
3.  Run the following ssh-keygen command to generate public and private keys:
    
    ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh\_ohpm/mykey 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Xky4TaojTuy1ZWXvFsFXbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCEC36CEFD6AE7C7CCBA4C549CBED84487016B1F6AABE7F4CD66A1F6E34303F7)
    
    1.  **~/.ssh\_ohpm/mykey** is the path to the private key file **mykey**. Before running the command, ensure that the directory where you want to save the private key file exists.
    2.  The public key file in .pub format is stored in the same directory as the private key file.
    3.  As ohpm supports only key-based authentication, be sure to enter the password when generating the public and private keys.
    
4.  Log in to the [central repository for OpenHarmony third-party libraries](https://ohpm.openharmony.cn/#/en/home). Then click **Personal Center** in the upper-right corner of the home page, click the button to add an ohpm public key, and paste the content of the **mykey.pub** file to the public key text box.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/lJGCEH9kQs642TLXkoP21w/en-us_image_0000002500909886.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=777B7AA47A17C630B0FEB553EE005CA08E2F771FAE98A670B8E3AD80A428B0F6)
    
5.  Open the command line tool and run the following command to set the **key\_path** field in the .ohpmrc file to the path of the private key file:
    
    ohpm config set key\_path  ~/.ssh\_ohpm/mykey
    
6.  Return to the **Personal Center** page of the [central repository for OpenHarmony third-party libraries](https://ohpm.openharmony.cn/#/en/home), copy the publish ID, and paste it to the .ohpmrc file by running the following command:
    
    ohpm config set publish\_id your\_publish\_id
    
7.  Run the following command to publish the HAR:
    
    ohpm publish <HAR path>
