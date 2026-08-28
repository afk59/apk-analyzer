# How do I flush HiLog information?

Run the **hilog -w start -f ckTest -l 1M -n 5 -m zlib -j 11** command.

The log file is saved in the **/data/log/hilog/** directory.

Parameter description

\-w start starts a log flushing task; -w stop stops the task.
-f sets the log file name.
-l sets the size of a single log file. The unit can be B, KB, MB, or GB.
-n sets the maximum number of log files. When the number of log files exceeds the specified value, the earliest log file will be overwritten. The value range is \[2,1000\].
-m specifies the log file compression algorithm.
-j specifies the task ID. The value ranges from 10 to 0xffffffffff.
For more details about parameters, run the hilog --help command.
