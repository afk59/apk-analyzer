# App Database Access

Since DevEco Studio 6.0.2 Beta1, the Database Inspector has been added, allowing you to execute SQL statements directly in DevEco Studio to view and modify your app database. This eliminates the need to export the database locally, improving development and debugging efficiency. It currently supports SQLite and vector databases.

You can also view or modify databases using the CLI. For detailed instructions, see [vector-store Database Debugging Tool Guide](../../../application-framework/arkdata/arkdata-database-debugging-tool/vector-store-database-debugging-tool-guide/document.md) and [SQLite Debugging Tool](../../../application-framework/arkdata/sqlite-debugging-tool/document.md).

#### When to Use

-   When an application operation modifies the database content, you can check in real time whether the updated content meets expectations.
-   You can modify data in the database in real time to construct test scenarios, improving testing efficiency.

#### Constraints

-   The device system must be API version 22 or later. For systems below API version 22, SQLite databases are view-only and cannot be modified, and vector databases are not supported.
-   Apps signed with a release certificate are not supported.
-   Only databases under the **database** directory can be debugged.
-   Encrypted databases are not supported; use non-encrypted databases instead.
-   Databases for private users or multi-users are not supported; use the default users' databases instead.
-   Databases cannot be imported or exported.
-   SQL execution constraints:
    -   Execution of multiple SQL statements is not supported.
    -   If multiple SQL statements are present, executing only a single highlighted statement is not supported.
    -   SQL execution does not support history logging.
    -   SQL execution does not support transactions.

#### Procedure

1.  Choose **View** > **Tool Windows** > **Database Inspector** from the menu bar to open the Database Inspector.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/NsszfaALSoGaeSnOHnLe0g/en-us_image_0000002509551896.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81D736A1C030BF7EC0C1AF7EDDC981E15C29CAB7CB040BC705BB9D6239F50546)
    
    The functions of each area on the Database Inspector page are as follows: ① for device selection; ② for app package name selection; ③ for database and table information display; ④ for SQL execution and data viewing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/sKjXkDdoRje59Avqt9J5yw/en-us_image_0000002541071901.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DBFAFBF9A0FA5F495A28D0993895BBB8AF4542B6A9FBF9CE5E98161C88B2F47)
    
2.  Select a device (which must already be connected) from the drop-down list box.
3.  Select a package name and click **Connect to Databases** on the right to view the database information. (If DevEco Studio 6.0.2 Beta1 is used, click **Execute**.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/yZwjDfmRSpOqwaPaAPUolQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03EDF7CCD248E9AB21B52086CBED327DA9DB4D6A70DACE3BEFDA312747F6583C)
    
    Depending on the device's API version, the Database Inspector shows different database paths: for those earlier than API version 22, the database is downloaded to the local computer and its path is displayed; for API version 22 and above, the path shown is the one on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ErD5GxuBRL6rPODwb0EObA/en-us_image_0000002509551902.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9E6576E1D372EE5321191330ABF419676C9BFC74E605186BEF1EBDEF79A6118)
    
4.  Double-click a table name to display its data on the right side, with a default pagination of 20 rows per page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/N49qA6-mTdiIuxAltJ29Kg/en-us_image_0000002541071903.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3DE49B73F642E6343D3910152F3A0B665DD644754D3B75C2A9332D30A341849)
    
5.  Click **New Query** on the left side; an **SQL Editor** tab will appear on the right. Select the desired database, enter the SQL statement, and click **Execute** to view or modify data.
    
    After modifying data, click **Refresh Table** below the SQL input box to refresh the data on the page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/O2nuUbKTTDW34NObLg1HAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9510FD47FC1DC74CB64F38A0961077343588C35B51BEAEAB6F47CC36CA800970)
    
    -   After the data is modified via SQL or updated by the app, the data display page does not refresh automatically. You must re-execute the query statement or click the refresh button.
    -   Modifications must be made via SQL statements; direct editing within the data view is not supported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/1kD56XnSQoOjf_TkXTt44Q/en-us_image_0000002509551904.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9457B007D0D3D804081A3C724E751E8EE8805D329579F17C96B84CF0EB809385)
