# What should I do if garbled characters are displayed in HiLog information?

Currently, HiLog employs a binary format for data storage and uses a data dictionary. Therefore, if you directly decompress the logs, garbled characters will be displayed.

You can use the hilogtool.exe tool in the **DevEco Studio\\sdk\\default\\hms\\toolchains** directory and run the **hilogtool.exe parse** command to parse the logs.

@set Ymd=%date:~0,4%\_%date:~5,2%%date:~8,2%\_%time:~0,2%%time:~3,2%%time:~6,2%
@set Ymd=%Ymd: =0% 
@set Dir=LOG\_%YMD% md %Dir% hdc file recv /data/log/hilog/ .\\%Dir%\\ 
hilogtool parse -i .\\%Dir% -d .\\%Dir% 
pause

The preceding code is saved in the **get\_hilog.bat** file, which is stored in the same directory as the **hilogtool.exe** file. You can run the script file to download all log files and parse them.
