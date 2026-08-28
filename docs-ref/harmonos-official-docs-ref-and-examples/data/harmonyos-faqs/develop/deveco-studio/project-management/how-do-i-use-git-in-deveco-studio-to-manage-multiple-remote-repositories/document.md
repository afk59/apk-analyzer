# How do I use Git in DevEco Studio to manage multiple remote repositories?

Add a remote repository:

1.  Right-click **Remote** to display the shortcut menu.
2.  Click **Manage Remotes** to open the **Git Remotes** window.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/HltNPZLDQROAD9HcCdnMYA/en-us_image_0000002194318352.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FF8344A321309A0880D57C4B2298CE3280DCF118719E32B3B02C024ED912DE8)
    
3.  Click the add button.
4.  Enter the remote repository name and URL.
5.  Click **OK** in the **Define Remote** dialog box. When prompted, enter the domain account and password.
6.  Click **OK** in the **Git Remotes** window.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/6B8kcYQWSrmF48lRpQbLVw/en-us_image_0000002229604125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA10A2554E085C884CCC5995978607F74FA58B4D633FF51610F4DFEE4E61409C "Click to enlarge")
    
7.  Click the pull icon as indicated below to obtain all remote records. The newly added remote repository is displayed in the submenu under **Remote**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/T7D7w8-yQOGFM44muwLG-w/en-us_image_0000002229758613.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A818BFD8A299ADB3FF55666D0F11ACA2281C388ED586E8DD126F3A9147987EB4)
    

Push your commit:

The process of pushing to a remote repository is similar to the standard process of pushing commits. To switch the remote repository, click the branch name (marked 1 in the figure below). To submit a pull request (PR), select the option marked 3.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Z6R1eGh6QuS4tDL_Ta6ttw/en-us_image_0000002194158744.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73E649DC9D1BF00BCC9F86742A15AA0C0BC8E9A330396E871991862ABA9F1E45 "Click to enlarge")

Switch the default associated remote repository:

Run the following command to switch the repository:

git branch hmos\_dev\_20230907 --set-upstream-to=codehub\_origin/hmos\_dev\_20230907
