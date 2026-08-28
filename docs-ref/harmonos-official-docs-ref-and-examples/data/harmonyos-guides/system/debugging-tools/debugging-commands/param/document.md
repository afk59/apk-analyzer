# param

The param tool enables you to operate system parameters. It is valid only for standard-system devices.

#### Environment Setup

-   You have obtained the hdc tool to run hdc shell commands.
-   The device is properly connected.

#### Commands

| Command | Description |
| :-- | :-- |
| \-h | Obtains the commands supported by param. |
| ls \[-r\] \[name\] | Displays the information about the system parameter that matches the given name. If **\-r** is specified, the information is obtained based on the parameter permission; otherwise, the parameter information is directly obtained. |
| get \[name\] | Obtains the value of the system parameter with the given name. If no name is specified, the values of all system parameters are returned. |
| set name value | Sets the value for the system parameter with the given name. |
| wait name \[value\] \[timeout\] | Waits for the system parameter with the given name to match the specified value. Fuzzy match is supported. For example, **"\*"** indicates any value, and **"val\*"** indicates matching of only the first three val characters. **timeout** indicates the waiting time, in seconds. If it is not set, the default value 30s is used. |
| save | Persistently saves the parameters to the workspace. |

#### \-h

-   Obtains the commands supported by the param tool.
    
    param -h
    

#### ls

-   Displays the information about the system parameter that matches the given name.
    
    param ls \[-r\] \[name\]
    
    **Example**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/icHbtEdCSDWp1y6pFjuYrw/en-us_image_0000002568764871.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0584B76EF97C8131176F5413FAD2AC68152F45EB36143782ADF84BBECA2151DF)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/OrzTFAawQKGczLGlp207AQ/en-us_image_0000002537765146.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A58D45D2E2D1C4AC113BB1EB5D4864EBD27B587D15CEA3B68F919F740326846A)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/j7kG18mPSuOy6qaVF3p3zg/en-us_image_0000002537925086.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D257CFF853D5ED5C91494C210AB1D9ABBFBDE6F43D69DE852EE295FF2D0407E)
    

#### get

-   Obtains the value of the system parameter with the given name.
    
    param get \[name\]
    
    **Example**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/IlPhv3AzQ-2ZnxwrqeFJOQ/en-us_image_0000002568684863.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=745FF3BD1198282760BD4E67C2EDE8D460D1A950DAC7B140638299C6937646D4)
    

#### set name value

-   Sets the value for the system parameter with the given name.
    
    param set name value
    
    **Example**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/IrOmYwy_ShSidt5bLbi2Kg/en-us_image_0000002568764873.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0BAD707159D782D4D3E2422B8B22867A16EA9BE72C783E7E1822D4269AA834E)
    

#### wait name

-   Waits for the system parameter with the given name to match the specified value.
    
    param wait name \[value\] \[timeout\]
    
    **Example**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/pPtvHINZTpqXRJcLGnlW4Q/en-us_image_0000002537765148.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6E37D8D8EE2F0727F1E37F6F8997D9BC2C64264F5F2A1BC3F9F43AD57F6FE22)
    

#### save

-   Persistently saves the parameters to the workspace.
    
    param save
    
    **Example**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/eMqZuRB6S3GGNe1aXvtcGA/en-us_image_0000002537925088.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF630C5A5D5E674B3BFBE48CAA4CB6EF0654850263E181B1050AF7280FD017DF)
