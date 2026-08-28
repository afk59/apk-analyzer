# Toybox

Toybox is a lightweight collection of Linux command line utilities. It combines many common Linux command line utilities into a single executable file.

#### Prerequisites

## Usage 1

-   Connect the device properly.
-   Run the **hdc shell** command to enter the command line execution mode.

## Usage 2

-   Enter the application sandbox.

#### Command Description

Toybox can be executed in either of the following ways:

-   Run the **toybox \[command\] \[arguments...\]** command.
    
-   Run the **\[command\] \[arguments...\]** command.
    

**\[command\]** can be any command supported by toybox. You can run the **toybox** command to query the supported commands.

**\[arguments...\]** are the parameters required by a \[command\].

## Help Command

toybox \[--long | --help | --version | \[command\] \[arguments...\]\]

| Option | Parameter | Description |
| :-- | :-- | :-- |
| \--help | NA | Displays the command help. |
| \--long | NA | Displays all supported commands along with their respective installation path. |
| \--version | NA | Displays the version number. |
| NA | NA | Displays all supported commands. |
| \[command\] | \[arguments\] | Runs a specific command. Most commands also support the **\--help** and **\--version** parameters. |

Format: help \[-ah\] \[command\]

| Parameter | Description |
| :-- | :-- |
| command | Displays the command help. **\[command\]** can be any command supported by toybox. |

| Option | Description |
| :-- | :-- |
| \-a | Displays the help information about all commands. |

## Mathematics and Basic Computer Functions

| Command | Description |
| :-- | :-- |
| ascii | 
Displays the ASCII code table.

usage: ascii

 |
| factor | 

Factors an integer.

usage: factor NUMBER...

 |
| mcookie | 

Generates a 128-bit strong random number.

usage: mcookie \[-vV\]

 |
| mkpasswd | 

Encrypts a password.

usage: mkpasswd \[-P FD\] \[-m TYPE\] \[-S SALT\] \[PASSWORD\] \[SALT\]

 |
| uuidgen | 

Creates and prints a new RFC4122 random UUID.

usage: uuidgen

 |

## Device Operations

| Command | Description |
| :-- | :-- |
| chvt | 
Switches to virtual device N.

usage: chvt N

 |
| chroot | 

Runs a command in the specified root directory.

usage: chroot NEWROOT \[COMMAND \[ARG...\]\]

 |
| clear | 

Clears the terminal.

usage: clear

 |
| nohup | 

Runs a command independent of the terminal.

usage: nohup COMMAND \[ARG...\]

 |
| tty | 

Displays the name of the device connected to the standard input device.

usage: tty \[-s\]

 |
| reset | 

Resets the terminal.

usage: reset

 |
| microcom | 

Runs a simple serial console.

usage: microcom \[-s SPEED\] \[-X\] DEVICE

 |

## sh Logical Commands

| Command | Description |
| :-- | :-- |
| false | 
Returns a non-zero value.

usage: false

 |
| sh | Starts the shell command interpreter. |
| test | 

Performs a test and returns **true** or **false**. If no parameter is carried, **false** is returned.

usage: test \[-bcdefghLPrSsuwx PATH\] \[-nz STRING\] \[-t FD\] \[X ?? Y\]

 |
| true | 

Returns zero.

usage: true

 |
| yes | 

Outputs lines repeatedly until it is killed. If no parameter is carried, **y** is returned.

usage: yes \[args...\]

 |

## System Operations

| Command | Description |
| :-- | :-- |
| acpi | 
Obtains the power supply and temperature status.

usage: acpi \[-abctV\]

 |
| arch | 

Prints the system name.

usage: arch

 |
| dmesg | 

Displays or controls the kernel ring buffer.

usage: dmesg \[-Cc\] \[-r | -t | -T\] \[-n LEVEL\] \[-s SIZE\] \[-w\]

 |
| dnsdomainname | 

Displays the system name, which is the same as the value of **hostname -d**.

usage: dnsdomainname

 |
| getconf | 

Obtains system configuration values. Some values require the **path** parameter.

usage: getconf -a \[PATH\] | -l | NAME \[PATH\]

 |
| env | 

Sets the environment for command execution or lists environment variables.

usage: env \[-i\] \[-u NAME\] \[NAME=VALUE...\] \[COMMAND \[ARG...\]\]

 |
| hostname | 

Obtains the current host name.

usage: hostname \[-bdsf\] \[-F FILENAME\] \[newname\]

 |
| insmod | 

Loads a kernel module.

usage: insmod MODULE \[MODULE\_OPTIONS\]

 |
| logger | 

Records system logs.

usage: logger \[-s\] \[-t TAG\] \[-p \[FACILITY.\]PRIORITY\] \[message...\]

 |
| lsmod | 

Displays the loaded modules, as well as their sizes and dependencies.

usage: lsmod

 |
| mix | 

Displays the OSS audio channel or sets the volume.

usage: mix \[-d DEV\] \[-c CHANNEL\] \[-l VOL\] \[-r RIGHT\]

 |
| modinfo | 

Displays the kernel module information.

usage: modinfo \[-0\] \[-b basedir\] \[-k kernel\] \[-F field\] \[module | file...\]

 |
| nproc | 

Prints the number of processors.

usage: nproc \[--all\]

 |
| oneit | 

Runs a simple initialization program.

usage: oneit \[-p\] \[-c /dev/tty0\] command \[...\]

 |
| partprobe | 

Notifies the kernel that the partitioned table has changed.

usage: partprobe DEVICE...

 |
| pivot\_root | 

Modifies the root directory.

usage: pivot\_root OLD NEW

 |
| printenv | 

Prints environment variables.

usage: printenv \[-0\] \[env\_var...\]

 |
| reboot/halt/poweroff | 

Reboots, halts, or powers off a system.

usage: reboot/halt/poweroff \[-fn\]

 |
| rfkill | 

Enables or disables a wireless device.

usage: rfkill COMMAND \[DEVICE\]

 |
| rmmod | 

Uninstalls a kernel module.

usage: rmmod \[-wf\] \[MODULE\]

 |
| sendevent | 

Sends a Linux input event.

usage: sendevent DEVICE TYPE CODE VALUE

 |
| swapoff | 

Deactivates a swap space.

usage: swapoff swapregion

 |
| swapon | 

Activates a swap partition in a specified device or file.

usage: swapon \[-d\] \[-p priority\] filename

 |
| switch\_root | 

Switches to the root directory and runs a new init program.

usage: switch\_root \[-c /dev/console\] NEW\_ROOT NEW\_INIT...

 |
| uname | 

Prints system information.

usage: uname \[-asnrvm\]

 |
| vmstat | 

Prints virtual memory information.

usage: vmstat \[-n\] \[DELAY \[COUNT\]\]

 |

## Time and Date

| Command | Description |
| :-- | :-- |
| cal | 
Prints a calendar.

usage: cal \[\[month\] year\]

 |
| date | 

Sets or obtains the current date and time.

usage: date \[-u\] \[-r FILE\] \[-d DATE\] \[+DISPLAY\_FORMAT\] \[SET\]

 |
| hwclock | 

Obtains or sets the hardware clock.

usage: hwclock \[-rswtluf\]

 |
| sleep | 

Waits before exiting. The value can be a decimal. The optional suffix can be "m" (minute), "h" (hour), "d" (day), or "s" (second, default value).

usage: sleep DURATION

 |
| time | 

Runs the command line and reports the real time, user time, and system time (in seconds). The real time is the wall clock time, the user time is the actual CPU time spend in user-mode, and the system time is the actual CPU time sped in the kernel.

usage: time \[-pv\] COMMAND \[ARGS...\]

 |
| uptime | 

Displays the current time, how long the system has been running, the number of users, and the average system load in the past 1, 5, and 15 minutes.

usage: uptime \[-ps\]

 |
| usleep | 

Waits for the configured time before exiting, in microseconds.

usage: usleep MICROSECONDS

 |

## Login User Operations

| Command | Description |
| :-- | :-- |
| groups | 
Prints the group to which the user belongs.

usage: groups \[user\]

 |
| id | 

Prints the user and group ID.

usage: id \[-nGgru\] \[USER...\]

 |
| login | 

Logs in as a user.

usage: login \[-p\] \[-h host\] \[-f USERNAME\] \[USERNAME\]

 |
| logname/whoami | 

Prints the current user name.

usage: logname/whoami

 |
| passwd | 

Updates the authentication token of a user.

usage: passwd \[-a ALGO\] \[-dlu\] \[USER\]

 |
| who | 

Prints information about logged in users.

usage: who

 |
| w | 

Displays the user login information and login time.

usage: w

 |

## Process Operations

| Command | Description |
| :-- | :-- |
| chrt | 
Obtains or sets the scheduling policy and priority of a process.

usage: chrt \[-Rmofrbi\] {-p PID \[PRIORITY\] | \[PRIORITY COMMAND...\]}

 |
| iorenice | 

Displays or modifies the I/O priority of a process.

usage: iorenice PID \[CLASS\] \[PRIORITY\]

 |
| iotop | 

Sorts processes based on the I/O priority.

usage: iotop \[-AaKObq\] \[-n NUMBER\] \[-d SECONDS\] \[-p PID,\] \[-u USER,\]

 |
| ionice | 

Displays or modifies the I/O scheduling priority of a process.

usage: ionice \[-t\] \[-c CLASS\] \[-n LEVEL\] \[COMMAND...|-p PID\]

 |
| kill | 

Sends a signal to a process.

usage: kill \[-l \[SIGNAL\] | -s SIGNAL | -SIGNAL\] pid...

 |
| killall | 

Sends a signal (**SIGTERM** by default) to all processes with the given name.

usage: killall \[-l\] \[-iqv\] \[-SIGNAL | -s SIGNAL\] PROCESS\_NAME...

 |
| killall5 | 

Sends signals to all processes except the current session.

usage: killall5 \[-l \[SIGNAL\]\] \[-SIGNAL | -s SIGNAL\] \[-o PID\]...

 |
| pidof | 

Prints the PIDs of all processes with the given name.

usage: pidof \[-s\] \[-o omitpid\[,omitpid...\]\] \[NAME...\]

 |
| pkill | 

Kills a process by process name.

usage: pkill \[-fnovx\] \[-SIGNAL | -l SIGNAL\] \[PATTERN\] \[-G GID,\] \[-g PGRP,\] \[-P PPID,\] \[-s SID,\] \[-t TERM,\] \[-U UID,\] \[-u EUID,\]

 |
| pmap | 

Obtains the memory mapping of a process.

usage: pmap \[-xq\] \[pids...\]

 |
| ps | 

Displays information of a process.

usage: ps \[-AadefLlnwZ\] \[-gG GROUP,\] \[-k FIELD,\] \[-o FIELD,\] \[-p PID,\] \[-t TTY,\] \[-uU USER,\]

 |
| pwdx | 

Prints the working directory of a process.

usage: pwdx PID...

 |
| renice | 

Adjusts the priority of processes, process groups, and user-level processes.

usage: renice \[-gpu\] -n increment ID ...

 |
| setsid | 

Runs a command in a new session.

usage: setsid \[-t\] command \[args...\]

 |
| taskset | 

Starts a task that runs only on a specified processor, or modifies the processor affinity of an existing process.

usage: taskset \[-ap\] \[mask\] \[PID | cmd \[args...\]\]

 |
| timeout | 

Runs a command in a child process and if the command execution is not finished within a time limit, sends a signal. The value of **DURATION** can be a decimal. The optional suffix can be "m" (minute), "h" (hour), "d" (day), or "s" (second, default value).

usage: timeout \[-k DURATION\] \[-s SIGNAL\] DURATION COMMAND...

 |
| top | 

Displays process information in real time.

usage: top \[-Hhbq\] \[-k FIELD,\] \[-o FIELD,\] \[-s SORT\] \[-n NUMBER\] \[-m LINES\] \[-d SECONDS\] \[-p PID,\] \[-u USER,\]

 |
| nice | 

Runs a command with a specified priority.

usage: nice \[-n PRIORITY\] COMMAND \[ARG...\]

 |
| nsenter | 

Runs a command in a specific namespace.

usage: nsenter \[-t pid\] \[-F\] \[-i\] \[-m\] \[-n\] \[-p\] \[-u\] \[-U\] COMMAND...

 |
| ulimit/prlimit | 

Displays or sets the resource limit of a process.

usage: ulimit/prlimit \[-P PID\] \[-SHRacdefilmnpqrstuv\] \[LIMIT\]

 |
| unshare | 

Creates a namespace for a process. Some attributes are not shared with the parent process.

usage: unshare \[-imnpuUr\] COMMAND...

 |
| watch | 

Runs the specified commands at a given interval (specified by **\-n**, in seconds) and displays the execution result. You can press **q** to exit the command execution.

usage: watch \[-teb\] \[-n SEC\] PROG ARGS

 |
| xargs | 

Runs the command line one or more times, carrying parameters from the standard input device.

usage: xargs \[-0prt\] \[-s NUM\] \[-n NUM\] \[-E STR\] COMMAND...

 |

## Device Node Operations

| Command | Description |
| :-- | :-- |
| blkid | 
Prints information of the file system, such as type, tag, and UUID.

usage: blkid \[-s TAG\] \[-UL\] DEV...

 |
| blockdev | 

Invokes ioctl for the block device in each command.

usage: blockdev --OPTION... BLOCKDEV...

 |
| devmem | 

Reads and writes the physical address using **/dev/mem**.

usage: devmem ADDR \[WIDTH \[DATA\]\]

 |
| df | 

Displays the total, used, and free disk space of each file system passed in. If no parameter is carried, all loaded file systems are displayed.

usage: df \[-HPkhi\] \[-t type\] \[FILESYSTEM ...\]

 |
| du | 

Displays the disk usage with files and directories.

usage: du \[-d N\] \[-askxHLlmc\] \[file...\]

 |
| eject | 

Ejects a device, which is **/dev/cdrom** by default.

usage: eject \[-stT\] \[DEVICE\]

 |
| free | 

Displays the total, available, and used amount of physical memory and swap space.

usage: free \[-bkmgt\]

 |
| freeramdisk | 

Releases all memory of a specified RAM disk.

usage: freeramdisk \[RAM device\]

 |
| fsfreeze | 

Freezes or unfreezes a file system.

usage: fsfreeze {-f | -u} MOUNTPOINT

 |
| fstype | 

Prints the type of a file system.

usage: fstype DEV...

 |
| fsync | 

Synchronizes the file status with the storage device.

usage: fsync \[-d\] \[FILE...\]

 |
| i2cdetect | 

Detects an I2C device.

usage:

i2cdetect \[-ary\] BUS \[FIRST LAST\]

i2cdetect -F BUS

i2cdetect -l

 |
| i2cdump | 

Dumps all I2C registers.

usage: i2cdump \[-fy\] BUS CHIP

 |
| i2cget | 

Reads an I2C register.

usage: i2cget \[-fy\] BUS CHIP ADDR

 |
| i2cset | 

Writes data to an I2C register.

usage: i2cset \[-fy\] BUS CHIP ADDR VALUE... MODE

 |
| losetup | 

Sets a loop device.

usage: losetup \[-cdrs\] \[-o OFFSET\] \[-S SIZE\] {-d DEVICE... | -j FILE | -af | {DEVICE FILE}}

 |
| lspci | 

Displays PCI device information.

usage: lspci \[-ekmn\] \[-i FILE \]

 |
| lsusb | 

Displays USB device information.

usage: lsusb

 |
| makedevs | 

Creates a series of special files, including block device files and character device files.

usage: makedevs \[-d device\_table\] rootdir

 |
| mount | 

Mounts a new file system to the directory. If no parameter is carried, the existing mounts are displayed.

usage: mount \[-afFrsvw\] \[-t TYPE\] \[-o OPTION,\] \[\[DEVICE\] DIR\]

 |
| mountpoint | 

Checks whether a directory or device is a mount point.

usage:

mountpoint \[-qd\] DIR

mountpoint \[-qx\] DEVICE

 |
| sync | 

Writes cached data to disks.

usage: sync

 |
| sysctl | 

Reads and writes the system control data in **/proc/sys.**

usage: sysctl \[-aAeNnqw\] \[-p \[FILE\] | KEY\[=VALUE\]...\]

 |
| tunctl | 

Creates or deletes a TUN or TAP device.

usage: tunctl \[-dtT\] \[-u USER\] NAME

 |
| vconfig | 

Creates or deletes a virtual Ethernet device.

usage: vconfig COMMAND \[OPTIONS\]

 |
| umount | 

Unmounts a file system.

usage: umount \[-a \[-t TYPE\[,TYPE...\]\]\] \[-vrfD\] \[DIR...\]

 |

## Network Operations

| Command | Description |
| :-- | :-- |
| ftpget/ftpput | 
Communicates with an FTP server and supports operations such as reading, writing, and listing files. The **ftpget** command contains the **\-g** option. The **ftpput** command contains the **\-s** option.

usage: ftpget/ftpput \[-cvgslLmMdD\] \[-p PORT\] \[-P PASSWORD\] \[-u USER\] HOST \[LOCAL\] REMOTE

 |
| ifconfig | 

Displays or configures a network interface.

usage: ifconfig \[-aS\] \[INTERFACE \[ACTION...\]\]

 |
| nbd-client | 

Creates an NBD client.

usage: nbd-client \[-ns\] HOST PORT DEVICE

 |
| netstat | 

Displays network information.

usage: netstat \[-pWrxwutneal\]

 |
| ping/ping6 | 

Checks network connectivity. The **ping6** command contains the **\-6** option.

usage: ping/ping6 \[OPTIONS\] HOST

 |
| sntp | 

Runs an SNTP client.

usage: sntp \[-saSdDqm\] \[-r SHIFT\] \[-m ADDRESS\] \[-p PORT\] \[SERVER\]

 |
| telnet | 

Connects to a Telnet server.

usage: telnet HOST \[PORT\]

 |
| traceroute/traceroute6 | 

Traces the path that a message takes from your PC to a host. The **traceroute6** command contains the **\-6** option.

usage: traceroute \[-46FUIldnvr\] \[-f 1ST\_TTL\] \[-m MAXTTL\] \[-p PORT\] \[-q PROBES\] \[-s SRC\_IP\] \[-t TOS\] \[-w WAIT\_SEC\] \[-g GATEWAY\] \[-i IFACE\] \[-z PAUSE\_MSEC\] HOST \[BYTES\]

usage: traceroute6 \[-dnrv\] \[-m MAXTTL\] \[-p PORT\] \[-q PROBES\]\[-s SRC\_IP\] \[-t TOS\] \[-w WAIT\_SEC\] \[-i IFACE\] HOST \[BYTES\]

 |
| wget | 

Downloads resources from the network.

usage: wget \[OPTIONS\]... \[URL\]

\[OPTIONS\] = --max-redirect x -d -O filename -p data

 |

## File Operations

| Command | Description |
| :-- | :-- |
| awk | 
Filters and analyzes document content.

usage: awk \[-F sepstring\] \[-v assignment\]... program \[argument...\]

or: awk \[-F sepstring\] -f progfile \[-f progfile\]... \[-v assignment\]... \[argument...\]

 |
| base64 | 

Uses the Base64 algorithm for encryption and decryption.

usage: base64 \[-di\] \[-w COLUMNS\] \[FILE...\]

 |
| basename | 

Returns the non-directory portion of a path name after removing its suffix.

usage: basename \[-a\] \[-s SUFFIX\] NAME... | NAME \[SUFFIX\]

 |
| bunzip2 | 

Decompresses a .bz file.

usage: bunzip2 \[-cftkv\] \[FILE...\]

 |
| bzcat | 

Decompresses a listed file to the standard output.

usage: bzcat \[FILE...\]

 |
| cat | 

Copies (Concatenates) a file to a standard output device. If no file is specified, the command reads from the standard input device. "-" indicates a standard input device.

usage: cat \[-etuv\] \[FILE...\]

 |
| chattr | 

Modifies the file attributes of a Linux Ext2 file system.

usage: chattr \[-R\] \[-+=AacDdijsStTu\] \[-v version\] \[File...\]

 |
| chcon | 

Modifies the SELinux security context of a file.

usage: chcon \[-hRv\] CONTEXT FILE...

 |
| chgrp/chown | 

Modifies the group of a file.

usage: chgrp/chown \[-RHLP\] \[-fvh\] group file...

 |
| chmod | 

Changes the access mode of a file (recursively with **\-R**).

usage: chmod \[-R\] MODE FILE...

 |
| cksum | 

Outputs the checksum, length, and file name of a file using 32-bit CRC algorithm. If no file is specified, the command reads from the standard input device. "-" indicates a standard input device.

usage: cksum \[-IPLN\] \[file...\]

 |
| cmp | 

Compares the contents of two files. (If only one file is specified, the command compares the file contents with the contents of the standard input device). You can specify whether to skip a certain number of bytes at the beginning.

usage: cmp \[-l\] \[-s\] FILE1 \[FILE2 \[SKIP1 \[SKIP2\]\]\]

 |
| comm | 

Reads the contents from **FILE1** and **FILE2** in sequence and outputs three text columns: lines only in **FILE1**, lines only in **FILE2**, and lines in both files. "-" indicates a standard input device.

usage: comm \[-123\] FILE1 FILE2

 |
| count | 

Copies the standard input device to the standard output device and displays a simple progress indicator to the standard error output **stderr**.

usage: count

 |
| cp | 

Copies the contents from **SOURCE** to **DEST**. If there are multiple sources, **DEST** must be a directory.

usage: cp \[-adfHiLlnPpRrsTv\] \[--preserve=motcxa\] \[-t TARGET\] SOURCE... \[DEST\]

 |
| cpio | 

Reads and writes files from the **cpio** archive in the **newc** format.

usage: cpio -{o|t|i|p DEST} \[-v\] \[--verbose\] \[-F FILE\] \[--no-preserve-owner\]

\[ignored: -mdu -H newc\]

 |
| crc32 | 

Outputs the CRC32 checksum of each file.

usage: crc32 \[file...\]

 |
| cut | 

Prints selected parts of lines from each file to the standard output device. Each selection list is separated by a comma, which can be a number (counted from 1) or a range separated by a dash (where **X-** indicates X to the end of the line, and **\-X** indicates from the start to X).

usage: cut \[-Ds\] \[-bcfF LIST\] \[-dO DELIM\] \[FILE...\]

 |
| dd | 

Converts and copies a file. It can be used to create disk mirroring, back up data, and convert character encoding.

usage:

dd \[if=FILE\] \[of=FILE\] \[ibs=N\] \[obs=N\] \[iflag=FLAGS\] \[oflag=FLAGS\]

\[bs=N\] \[count=N\] \[seek=N\] \[skip=N\]

\[conv=notrunc|noerror|sync|fsync\] \[status=noxfer|none\]

 |
| diff | 

Compares files or folders and outputs their differences.

usage: diff \[-abBdiNqrTstw\] \[-L LABEL\] \[-S FILE\] \[-U LINES\] FILE1 FILE2

 |
| dirname | 

Displays the directory portion of a path.

usage: dirname PATH...

 |
| dos2unix | 

Converts the newline format in a file from DOS "\\r\\n" to Unix "\\n". If no file is specified, the command reads from the standard input device. "-" indicates a standard input device.

usage: dos2unix \[FILE...\]

 |
| echo | 

Writes each parameter to the standard output device. Each parameter is separated by a space followed by a newline.

usage: echo \[-neE\] \[args...\]

 |
| grep/egrep/fgrep | 

Displays the lines that match a regular expression. If **\-e** is not specified, the first parameter is the regular expression to match. If no file is specified (or the file name is "-"), the command reads from the standard input device. If a match is found, 0 is returned. If no match is found, 1 is returned. If an error occurs during the command execution, 2 is returned.

The **egrep** command has the **\-E** option, and the **fgrep** command has the **\-F** option. The **\-E** and **\-F** options cannot be used at the same time.

usage: grep/egrep/fgrep \[-EFrivwcloqsHbhn\] \[-ABC NUM\] \[-m MAX\] \[-e REGEX\]... \[-MS PATTERN\]... \[-f REGFILE\] \[FILE\]...

 |
| gzip | 

Compresses a file.

usage: gzip \[-19cdfk\] \[FILE...\]

 |
| expand | 

Expands a tab to a space based on the input parameter.

usage: expand \[-t TABLIST\] \[FILE...\]

 |
| fallocate | 

Reserves space for a file in a file system.

usage: fallocate \[-l size\] \[-o offset\] file

 |
| file | 

Checks a file and describes its content type.

usage: file \[-bhLs\] \[file...\]

 |
| find | 

Finds a file in the directory.

usage: find \[-HL\] \[DIR...\] \[<options>\]

 |
| flock | 

Manages the advisory lock.

usage: flock \[-sxun\] fd

 |
| fmt | 

Reformats the input to a wordwrap of a given line length, preserves the existing indentation level, and writes it to the standard output device.

usage: fmt \[-w WIDTH\] \[FILE...\]

 |
| gunzip | 

Decompresses a file. If no file is specified, the command decompresses the standard input device as a standard output device. After the command is successfully executed, the input file is deleted and replaced with a new file without the file name extension .gz.

usage: gunzip \[-cfk\] \[FILE...\]

 |
| head | 

Copies the first line in a file to the standard output device. If no file is specified, the command reads from the standard input device. "-" indicates a standard input device.

usage: head \[-n number\] \[file...\]

 |
| hexedit | 

Edits a hexadecimal file. All modifications are written to disk immediately.

usage: hexedit FILENAME

 |
| iconv | 

Converts the encoding format of a file.

usage: iconv \[-f FROM\] \[-t TO\] \[FILE...\]

 |
| inotifyd | 

Runs a specified program when a file system event occurs.

usage: inotifyd PROG FILE\[:MASK\] ...

 |
| install | 

Copies a file and sets its attributes.

usage: install \[-dDpsv\] \[-o USER\] \[-g GROUP\] \[-m MODE\] \[-t TARGET\] \[SOURCE...\] \[DEST\]

 |
| link | 

Creates a hard link for a file.

usage: link FILE NEWLINK

 |
| ln | 

Creates a soft or hard link between **FROM** and **TO**.

usage: ln \[-sfnv\] \[-t DIR\] \[FROM...\] TO

 |
| ls | 

Lists the files or folders in the current directory.

usage: ls \[-ACFHLRSZacdfhiklmnpqrstux1\] \[--color\[=auto\]\] \[directory...\]

 |
| lsattr | 

Lists the file attributes on the Linux file system. The flag letters are defined in the chattr help.

usage: lsattr \[-Radlv\] \[Files...\]

 |
| lsof | 

Lists all open files that belong to the active processes, or lists the processes that use the listed file.

usage: lsof \[-lt\] \[-p PID1,PID2,...\] \[FILE...\]

 |
| md5sum | 

Calculates the hash of each input file. If no file is specified, the command reads from the standard input device. Each input file outputs a line of hash followed by a file name.

usage: md5sum \[-bcs\] \[FILE\]...

 |
| mkdir | 

Creates one or more directories.

usage: mkdir \[-vp\] \[-m mode\] \[dirname...\]

 |
| mkfifo | 

Creates a FIFO file (named pipe).

usage: mkfifo \[NAME...\]

 |
| mkswap | 

Creates a swap space in Linux.

usage: mkswap \[-L LABEL\] DEVICE

 |
| mktemp | 

Safely creates a file **DIR/TEMPLATE** and prints its name.

usage: mktemp \[-dqu\] \[-p DIR\] \[TEMPLATE\]

 |
| mknod | 

Creates a special file (**b** is a block device, **c** or **u** is a character device, and **p** is a named pipe).

usage: mknod \[-m MODE\] NAME TYPE \[MAJOR MINOR\]

 |
| more | 

Views a file one page at a time.

usage: more \[FILE...\]

 |
| mv | 

Moves or renames a file.

usage: mv \[-finTv\] \[-t TARGET\] SOURCE... \[DEST\]

 |
| nl | 

Adds a line number to an input file.

usage: nl \[-E\] \[-l #\] \[-b MODE\] \[-n STYLE\] \[-s SEPARATOR\] \[-v #\] \[-w WIDTH\] \[FILE...\]

 |
| od | 

Dumps data in octal/hexadecimal format.

usage: od \[-bcdosxv\] \[-j #\] \[-N #\] \[-w #\] \[-A doxn\] \[-t acdfoux\[#\]\]

 |
| paste | 

Merges corresponding lines from each input file.

usage: paste \[-s\] \[-d DELIMITERS\] \[FILE...\]

 |
| patch | 

Applies a diff file to one or more files.

usage: patch \[-d DIR\] \[-i file\] \[-p depth\] \[-Rlsu\] \[--dry-run\]

 |
| pgrep | 

Searches for a process. **PATTERN** is an extended regular expression used to check command names.

usage: pgrep \[-clfnovx\] \[-d DELIM\] \[-L SIGNAL\] \[PATTERN\] \[-G GID,\] \[-g PGRP,\] \[-P PPID,\] \[-s SID,\] \[-t TERM,\] \[-U UID,\] \[-u EUID,\]

 |
| printf | 

Uses printf in C to format and print parameters based on the **FORMAT**.

usage: printf FORMAT \[ARGUMENT...\]

 |
| pwd | 

Prints the working (current) directory.

usage: pwd \[-L | -P\]

 |
| readahead | 

Preloads a file to the disk cache.

usage: readahead FILE...

 |
| readlink | 

Prints what the symbolic link points to if no options are carried. If it is not a symbolic link, an error is returned.

usage: readlink FILE...

 |
| realpath | 

Displays the standard absolute path name.

usage: realpath FILE...

 |
| rev | 

Outputs each line in reverse order.

usage: rev \[FILE...\]

 |
| rm | 

Removes a file.

usage: rm \[-fiRrv\] FILE...

 |
| rmdir | 

Removes one or more directories.

usage: rmdir \[-p\] \[dirname...\]

 |
| sed | 

Stream editor that applies the edit script to the input line.

usage: sed \[-inrzE\] \[-e SCRIPT\]... | SCRIPT \[-f SCRIPT\_FILE\]... \[FILE...\]

 |
| seq | 

Counts in ascending order from the beginning (specified by **first**) to the end (specified by **last**). If no parameter is carried, the default value is 1. The parameter can be a negative number or a floating point number.

usage: seq \[-w | -f fmt\_str\] \[-s sep\_str\] \[first\] \[increment\] last

 |
| setfattr | 

Writes POSIX extended attributes.

usage: setfattr \[-h\] \[-x | -n NAME\] \[-v VALUE\] FILE...

 |
| sha1sum/sha256sum | 

Calculates the SHA hash value.

usage: sha?sum \[-bcs\] \[FILE\]...

 |
| shred | 

Deletes a file securely (overwrites the file content with random data).

usage: shred \[-fuz\] \[-n COUNT\] \[-s SIZE\] FILE...

 |
| sort | 

Sorts all lines of text from the input file (or standard input device) to the standard output device.

usage: sort \[-Mbcdfginrsuz\] \[FILE...\] \[-k#\[,#\[x\]\] \[-t X\]\] \[-o FILE\]

 |
| split | 

Copies input (or standard input device) data to a series of output (or "x") files with alphabetically increasing suffix (aa, ab, ac, ... az, ba, bb...).

usage: split \[-a SUFFIX\_LEN\] \[-b BYTES\] \[-l LINES\] \[INPUT \[OUTPUT\]\]

 |
| stat | 

Displays the status of a file or file system.

usage: stat \[-tfL\] \[-c FORMAT\] FILE...

 |
| strings | 

Displays printable strings in a binary file.

usage: strings \[-fo\] \[-t oxd\] \[-n LEN\] \[FILE...\]

 |
| tac | 

Outputs lines in reverse order.

usage: tac \[FILE...\]

 |
| tail | 

Copies the last lines in a file to the standard output device. "-" indicates a standard input device.

usage: tail \[-n|c NUMBER\] \[-f\] \[FILE...\]

 |
| tar | 

Creates, extracts, or lists files in a .tar file.

usage: tar \[-cxt\] \[-fvohmjkOS\] \[-XTCf NAME\] \[FILES\]

 |
| tee | 

Copies the standard input device to each listed file, and also to the standard output device. "-" indicates a standard output device.

usage: tee \[-ai\] \[file...\]

 |
| touch | 

Updates the access and modification time of each file to the current time.

usage: touch \[-amch\] \[-d DATE\] \[-t TIME\] \[-r FILE\] FILE...

 |
| truncate | 

Sets the length of the file, sparsely expanding if necessary.

usage: truncate \[-c\] -s SIZE file...

 |
| uniq | 

Reports or filters output duplicate lines in a file.

usage: uniq \[-cduiz\] \[-w maxchars\] \[-f fields\] \[-s char\] \[input\_file \[output\_file\]\]

 |
| unix2dos | 

Converts the newline format from Unix "\\n" to DOS "\\r\\n". If no file is specified, the command reads from the standard input device. "-" indicates a standard input device.

usage: unix2dos \[FILE...\]

 |
| unlink | 

Removes a file.

usage: unlink FILE

 |
| uudecode | 

Decodes a file from the standard input device (or INFILE).

usage: uudecode \[-o OUTFILE\] \[INFILE\]

 |
| uuencode | 

Encodes data on a standard input device (or file) and outputs the encoded data to a standard output device. The output contains **encode-filename**.

usage: uuencode \[-m\] \[file\] encode-filename

 |
| wc | 

Counts the number of lines, words, and characters in the input.

usage: wc -lwcm \[FILE...\]

 |
| which | 

Searches **$PATH** for executable files that match the specified file name.

usage: which \[-a\] filename ...

 |
| xxd | 

Displays the file content in hexadecimal format. If no file is specified, the command reads from the standard input device.

usage: xxd \[-c n\] \[-g n\] \[-i\] \[-l n\] \[-o n\] \[-p\] \[-r\] \[-s n\] \[file\]

 |
| zcat | 

Decompress the file to the standard output device. It is similar to **gzip -dc**.

usage: zcat \[FILE...\]

 |

#### FAQs

## What should I do if "Unknown command xxx" is displayed?

If the error message "Unknown command xxx" is displayed when you input **xxx**, **toybox xxx**, or **help xxx** in the command line, the toybox does not support the **xxx** command.

If the command is described in this topic, the command is not compiled. You are advised to ask questions in the HarmonyOS official forum.

## What should I do if "Operation not permitted" or "Permission denied" is displayed?

Toybox contains a large number of commands for operating files and processes. If you do not have the permission on the operated object, an error is reported.

1.  The permission is missing. Check whether you have the read, write, and execute permissions on the file and its folder.
2.  SELinux interception. You can search for the keyword "avc: denied" in the kernel log.

Example:

If error message similar to "avc: denied { xxx } for comm='ls' xxxxxx" is displayed, the **ls** command triggers SELinux interception.

If the permission is missing and you need to run this command, you are advised to ask questions in the HarmonyOS official forum.

## What should I do if other standard Linux errors are reported?

Most toybox commands are used to call the kernel. When an error occurs, **perror** is used to print the text corresponding to the Linux kernel error code.

Common errors are as follows: "File exists", "Not a directory", and "Read-only file system".

These errors are standard Linux errors. You can query the error causes by referring to related Linux documents. Check whether the command parameters or command format is correct based on the error information.

Example:

When a file is created in a read-only file system, the error message "Read-only file system" is displayed.

The **cat** command can be used to print a file. If you use this command to print a directory, the error message "Is a directory" is displayed.

If you run the **ls** command to view a file or directory that does not exist, the error message "No such file or directory" is displayed.

## What should I do if a command does not comply with the toybox description?

If the command parameters input in the shell are inconsistent with the toybox command parameters, the possible causes are as follows:

1.  The shell implementation instead of toybox is invoked.
    
    For commands such as **time**, **test**, **pwd**, **realpath**, **ulimit**, and **kill**, shell uses its own implementation.
    
    To invoke a toybox command, use the format of **toybox \[command\] \[arguments...\]**.
    
2.  The device does not configure this command for toybox, but has another implementation.
    
    To invoke a toybox command, use the format of **toybox \[command\] \[arguments...\]**.
