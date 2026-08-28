# NDK-Related musl libc Interface Usage Restrictions

#### Overview

When developing an application using DevEco Studio or NDK, you may need to use the interface capabilities of musl libc. However, some interfaces of musl libc may be unavailable due to restrictions of multiple systems and environments. In this case, you can refer to this document to troubleshoot interface issues.

#### Seccomp-Affected musl Interfaces

## Determining Process Termination Due to Seccomp

-   Check the process fault logs. If the error cause is **signal:SIGSYS** and the stack top is in the ld-musl-{architecture}.so.1 library, the process termination may be caused by the Seccomp mechanism.
    
    cat /data/log/faultlog/faultlogger/cppcrash-xxxx
    
    Incorrect example:
    
    Process name:com.example.myapplication
    Reason:Signal:SIGSYS(UNKNOWN)
    Fault thread Info:
    Tid:13893, Name:e.myapplication
    #00 pc 000a5d30 /system/lib/ld-musl-arm.so.1(sethostname+16)(584c9d0a0e9000497bb0d66799a9526a)
    #01 pc 00002f68 /data/storage/el1/bundle/libs/arm/libentry.so(test()+64)
    

## Common Seccomp-Affected Interfaces

| Header File | musl Interface |
| :-- | :-- |
| fcntl.h | name\_to\_handle\_at |
| fcntl.h | open\_by\_handle\_at |
| grp.h | initgroups |
| grp.h | setgroups |
| sched.h | setns |
| sched.h | unshare |
| sys/fanotify.h | fanotify\_init |
| sys/fanotify.h | fanotify\_mark |
| sys/fsuid.h | setfsgid |
| sys/fsuid.h | setfsuid |
| sys/klog.h | klogctl |
| sys/mount.h | mount |
| sys/mount.h | umount2 |
| sys/mount.h | umount |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/reboot.h | reboot |
| sys/sem.h | semctl |
| sys/sem.h | semget |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmat |
| sys/shm.h | shmctl |
| sys/shm.h | shmdt |
| sys/shm.h | shmget |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| sys/swap.h | swapoff |
| sys/swap.h | swapon |
| time.h | clock\_settime |
| sys/time.h | settimeofday |
| sys/timex.h | adjtimex |
| sys/timex.h | clock\_adjtime |
| unistd.h | acct |
| unistd.h | chroot |
| unistd.h | pause |
| unistd.h | setdomainname |
| unistd.h | setegid |
| unistd.h | setgid |
| unistd.h | sethostname |
| unistd.h | setregid |
| unistd.h | setresgid |
| unistd.h | setreuid |
| unistd.h | setuid |
| None | pivot\_root |
| None | init\_module |
| None | delete\_module |

#### Kernel-Related musl Interfaces Not Opened to the Public

| Header File | musl Interface |
| :-- | :-- |
| sys/fanotify.h | fanotify\_init |
| sys/fanotify.h | fanotify\_mark |
| unistd.h | acct |

#### SELinux-Affected musl Interfaces

## Determining Interface Errors Caused by SELinux

-   Include the **errno.h** header file and check the errno error status code. If the error status code is EACCES, the interface error may be caused by the SELinux mechanism.

## Common SELinux-Affected Interfaces

| Header File | musl Interface |
| :-- | :-- |
| net/if.h | if\_indextoname |
| net/if.h | if\_nametoindex |
| pty.h | forkpty |
| pty.h | openpty |
| semaphore.h | sem\_open |
| semaphore.h | sem\_unlink |
| stdlib.h | ptsname |
| stdlib.h | ptsname\_r |
| stdlib.h | posix\_openpt |
| stdlib.h | unlockpt |
| stdio.h | popen |
| stdio.h | pclose |
| sys/ioctl.h | ioctl |
| sys/mman.h | shm\_open |
| sys/mman.h | shm\_unlink |
| sys/mount.h | mount |
| sys/mount.h | umount |
| sys/mount.h | umount2 |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/sem.h | semget |
| sys/sem.h | semctl |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmget |
| sys/shm.h | shmat |
| sys/shm.h | shmdt |
| sys/shm.h | shmctl |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| termios.h | tcgetattr |
| termios.h | tcsetattr |
| termios.h | tcsendbreak |
| termios.h | tcdrain |
| termios.h | tcflush |
| termios.h | tcflow |
| termios.h | tcgetsid |
| unistd.h | link |
| unistd.h | linkat |
| unistd.h | readlink |
| unistd.h | readlinkat |
| unistd.h | symlink |
| unistd.h | symlinkat |
| unistd.h | tcgetpgrp |
| unistd.h | tcsetpgrp |
| utmp.h | login\_tty |

#### Sandbox-Affected musl Interfaces

For details about the sandbox mechanism, see [Application Sandbox](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).

Include the **errno.h** header file and check the errno error status code. If the error status code is ENOENT, the interface error may be caused by the sandbox mechanism.

Common Sandbox-Affected Interfaces

| Header File | musl Interface |
| :-- | :-- |
| fcntl.h | open |
| fcntl.h | openat |
| nl\_types.h | catopen |
| stdio.h | fopen |
| stdio.h | freopen |
| stdio.h | rename |
| stdio.h | renameat |
| stdio.h | renameat2 |
| stdio.h | tmpfile |
| stdio.h | tmpfile64 |

#### No-Op or Default-Failure musl Interfaces

| Header File | musl Interface |
| :-- | :-- |
| netdb.h | getnetbyaddr |
| netdb.h | getnetbyname |
| stdio\_ext.h | \_\_fsetlocking |
| unistd.h | brk |
| utmp.h | getutent |
| utmp.h | pututline |
| utmp.h | setutent |
| utmp.h | pututline |
| utmp.h | utmpname |

#### musl Interfaces Requiring Special Permissions

Include the **errno.h** header file and check the errno error status code. If the error status code is EPERM, the interface error may be caused by the system capabilities security mechanism or other kernel security controls.

Common Capabilities-Affected Interfaces

| Header File | musl Interface | Capabilities Permission |
| :-- | :-- | :-- |
| None | pivot\_root | CAP\_SYS\_ADMIN |
| None | init\_module | CAP\_SYS\_MODULE |
| None | delete\_module | CAP\_SYS\_MODULE |
| fcntl.h | open\_by\_handle\_at | CAP\_DAC\_READ\_SEARCH |
| sys/klog.h | klogctl | CAP\_SYS\_ADMIN |
| sys/mount.h | mount | CAP\_SYS\_ADMIN |
| sys/mount.h | umount | CAP\_SYS\_ADMIN |
| sys/mount.h | umount2 | CAP\_SYS\_ADMIN |
| sys/reboot.h | reboot | CAP\_SYS\_BOOT |
| sys/swap.h | swapon | CAP\_SYS\_ADMIN |
| sys/swap.h | swapoff | CAP\_SYS\_ADMIN |
| sys/time.h | settimeofday | CAP\_SYS\_TIME |
| unistd.h | setdomainname | CAP\_SYS\_ADMIN |
| unistd.h | sethostname | CAP\_SYS\_ADMIN |
| unistd.h | chroot | CAP\_SYS\_CHROOT |
