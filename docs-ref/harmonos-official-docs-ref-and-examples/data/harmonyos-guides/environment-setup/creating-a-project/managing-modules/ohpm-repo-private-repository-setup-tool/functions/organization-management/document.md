# Organization Management

In ohpm, the package is named in the format of **@_<group>_/_<package\_name_\>** or **_<package\_name>_**.

_**group**_ indicates the organization, and _**package\_name**_ indicates the package name. If you want to upload a package that contains an organization (for example, **@ohos/axios**), you need to create the organization (for example, **ohos**) in ohpm-repo before uploading the package.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/K9V2zvt_Svyf1apnEJd5nw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0085EC553FEDD3DC514479946C25669F3052BFACFCADB09A5F6EC869D497CDDF)

When publishing a HAR/HSP package, you are advised to include the organization name in the package name (package\_name) to facilitate management and identification of third-party libraries.

In ohpm-repo, only organization members can upload packages of the organization. If a package does not belong to any organization, subsequent version updates can be uploaded only by the first uploader of the package. **Organize manage** is used to manage organization information.

-   On the **Organize manage** page of the administrator, the administrator can view information about all organizations and edit administrator information of any organization. In addition, you can add new organizations, search for existing organizations, and edit and delete managed organizations.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/_awfvfv_RFud5u7jpc2JjQ/en-us_image_0000002501068702.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=612C933CDE0E0F9DF59A0766A564085704797BFB263B32AE40E8241AE81ADC6C "Click to enlarge")
    

-   On the **Organize manage** page of a common user, you can view only the information about the organization to which the current user belongs, view and search for organizations, and edit and delete managed organizations.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/TNZMPYGzSKyi5YwTezLYsg/en-us_image_0000002500908860.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=655FA5F143084644C66AD530C8FF099FD288E6290CCE290943636A65D977C8BC "Click to enlarge")
    

1.  Click **Add**. The permission of an administrator user is required. The **Add organize** dialog box is displayed. You can create an organization. The following figure shows the page effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/yEimBzDqTZOG4UY1V7RdiA/en-us_image_0000002532668761.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBBA0112B0667EFA539A6157FE69AE77984233E4AB1D423E2F8E219FE88FF8A5 "Click to enlarge")
    
2.  Click **Details** to go to the organization details panel. There are three tab pages: **Describe**, **package**, and **Members**. The **Describe** tab page displays the basic information about the organization. The **package** tab page displays the information about all packages uploaded to the repository of the organization. The **Members** tab page is used by an administrator of an organization to manage members in the organization. You can enter a user name to add a member or remove a member from the organization.
    -   **Describe**: displays basic information about an organization.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/OtcPl39YTp2UgCF7SAim3Q/en-us_image_0000002532748697.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CECB32204C84DDFFA3FF7B185F9BB466E5C6E0E250286C2B0D58170719692B0A "Click to enlarge")
        
    -   **package**: displays information about all packages uploaded to the repository of the organization.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/GdheTpZZRX-mVWWrutiNBA/en-us_image_0000002501068698.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1C696A35A11F8B1C5F03A2AEA04470D7ECB76AFDD6A34C82773A2D321A50124 "Click to enlarge")
        
    -   **Members**: indicates the management of members in an organization by an administrator of the organization. The administrator can enter a user name to add a member to the organization or remove a member from the organization. An organization member has only the permission to view the organization member list.
        
        -   Page of an organization administrator
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Sb8i16l5SNWTr44q6dNrow/en-us_image_0000002500908850.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF9FFC556FE9DD154E4EE3B0C2305DB5DD598DF51DBC0D14CCDD9D8DE33F39E6 "Click to enlarge")
            
        
        -   Page of an organization member
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/4iFNgJm1SU2ogpiSxHCZXg/en-us_image_0000002501068680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0668AE6D2B15BE9E3A64A3FA2EF178CFBA5B9A7A28FC334C80DECC6F53C5C94D "Click to enlarge")
            
        
        -   Click **Add member**. The permission of the organization administrator user is required. After entering the user name, the user can be added to the organization and become a member of the organization. New organization members are automatically granted maintainer permissions on all existing packages within the organization.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Lm0DvOLORdG5Dv8qIYZ0VA/en-us_image_0000002532748707.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CD62AD61E848689BEBDDDE22AD252DA7734A26EE94077869E0CCAA204D722DF "Click to enlarge")
            
        -   Click **delete** an organization member. The permission of the organization administrator user is required. If a member to be deleted is an organization administrator and there are no other organization administrators, the member cannot be deleted. An organization must have at least one organization administrator. When a regular member is removed from the organization, any maintainer permissions they held on the organization's packages will be revoked. When an organization administrator is removed, any owner permissions they had on the organization's packages will be revoked.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/1Uu9l-mkSm6NaiPzLZ7KAw/en-us_image_0000002532748701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2BEE8CCD4B6E9EF62B60D61F20A91B755424F404EE255BC1DFA03198FFB9D71 "Click to enlarge")
            

3.  Click **Edit organize**. The permission of the organization administrator user is required. On the **Edit organize** panel, you can modify the name and description of an organization. If a package of the organization already exists in ohpm-repo (the number of components is not **0**), the name cannot be modified.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/X7hFzSHBRAKCR1VSqP-i7w/en-us_image_0000002532668755.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39433D651A94305256944E9979FF6BADC27B1CACDB4D7047E44157393056D62A "Click to enlarge")
    
4.  Click **Edit group admin**. The organization administrator details page is displayed. The permission of an administrator user is required. The administrator user can view the administrator list of an organization, and add or delete organization administrators.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/79uxKVrRQQKxLJVHeUdm_Q/en-us_image_0000002532748715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA73FEAD3E8DCC9A69D843D46A9467ED973C3C4F650DD93E97CCC77CC9FDD885 "Click to enlarge")
    
    -   Click **Add group admin**. Enter a user name to add the user as an organization administrator. New organization administrators are automatically granted owner permissions on all existing packages within the organization.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cJaiackYTzqbB-bynsldGg/en-us_image_0000002532748721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81BDE6D9197113FA624C9759ACDDB31B604382948BBE72236B60F73EE9280CF0 "Click to enlarge")
        
    
    -   Click **Delete**. If there is only one organization administrator, they cannot be deleted. An organization must have at least one organization administrator. When an organization administrator is removed, any owner permissions they had on the organization's packages will be revoked.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/LnOTPY0JRX-RKMsKSRL6WA/en-us_image_0000002532748711.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7CD4BC89E4119272FABCA6B063D30F9B81870DFF5D64A9264C3F384B7A2B417 "Click to enlarge")
        
5.  Click **Delete**. If a package of the organization already exists in ohpm-repo (the number of components is not **0**), the organization cannot be deleted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/EUc0o21PSnGHe0uA3VfHJQ/en-us_image_0000002532668743.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AC88A1FE52D9241AA68DBB11A3D0D7EAA118C911828CB50114A339C1A95A6CF "Click to enlarge")
    
6.  Click to search for an organization by organization name or organization administrator name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/61Ok7iEYT_6UVQDJy34HKw/en-us_image_0000002500908846.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE21953744B516E2CBFD82C097847C9F21DE7371C4958DA9F7CC2393916DAB63 "Click to enlarge")
