# Using fdsan

#### 1\. Introduction

File descriptor sanitizer (fdsan) is a tool used to detect mishandling of file descriptor ownership, which includes double-close and use-after-close. An FD can be a file, directory, network socket, or other I/O devices in an operating system. When a file or socket is opened in an application, an FD is generated. If the FD is repeatedly closed after use or is used after being closed, security risks such as file handle leaks and memory leaks may occur. This type of problems is difficult to locate and fix. That is why fdsan comes in handy.

#### 2\. Working Principle

fdsan provides functions to associate a file descriptor with an owner and enforces detection of file descriptor errors based on ownership. When a file is opened or created, the file descriptor returned is associated with a tag, which indicates the owner responsible for closing it. Before the file is closed, the tag associated with the file descriptor is checked to determine whether the owner is correct. If yes, the file can be closed. Otherwise, an exception will be thrown to trigger error handling.

A tag is of 64 bits, consisting of the following:

**type**: an 8-bit string indicating how a file descriptor is encapsulated for management. For example, **FDSAN\_OWNER\_TYPE\_FILE** indicates that the file descriptor is managed as a handle to a file. The value of **type** is defined in **fdsan\_owner\_type**.

**value**: a 56-bit string uniquely identifying a tag.

**Figure** Tag

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/B7RO9DJgQemIKGhcfiw8nA/en-us_image_0000002537765290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48BCDE7B9D60581D0AF105F8CD7DF172B28620D14C3F433A2661E71BAB13ABE0)

#### 3\. Available APIs

## fdsan\_set\_error\_level

enum fdsan\_error\_level fdsan\_set\_error\_level(enum fdsan\_error\_level new\_level);

**Description**

Sets an error level, which determines the processing behavior when an exception is detected. The default value is **FDSAN\_ERROR\_LEVEL\_WARN\_ALWAYS**.

**Parameters**

**fdsan\_error\_level**

| Value | Description |
| :-- | :-- |
| FDSAN\_ERROR\_LEVEL\_DISABLED | fdsan is disabled, that is, no processing is performed. |
| FDSAN\_ERROR\_LEVEL\_WARN\_ONCE | Give a warning in HiLog only when the error is detected for the first time and then continue execution with fdsan disabled (**FDSAN\_ERROR\_LEVEL\_DISABLED**). |
| FDSAN\_ERROR\_LEVEL\_WARN\_ALWAYS | Give a warning in HiLog only each time the error is detected. |
| FDSAN\_ERROR\_LEVEL\_FATAL | Call **abort** to terminate the process when the error is detected. |

**Return value**

Old **error\_level**.

## fdsan\_get\_error\_level

enum fdsan\_error\_level fdsan\_get\_error\_level();

**Description**

Obtains the current error level.

**Return value**

Current error level.

## fdsan\_create\_owner\_tag

uint64\_t fdsan\_create\_owner\_tag(enum fdsan\_owner\_type type, uint64\_t tag);

**Description**

Creates a tag for a file descriptor.

**Parameters**

**fdsan\_owner\_type**

| Value | Description |
| :-- | :-- |
| FDSAN\_OWNER\_TYPE\_GENERIC\_00 | Default type. |
| FDSAN\_OWNER\_TYPE\_GENERIC\_FF | Default type for invalid file descriptors. |
| FDSAN\_OWNER\_TYPE\_FILE | Type for a file, which can be opened by using **fopen()** or **fdopen()**. |
| FDSAN\_OWNER\_TYPE\_DIRECTORY | Type for a directory, which can be opened by using **opendir** or **fdopendir**. |
| FDSAN\_OWNER\_TYPE\_UNIQUE\_FD | Type for **unique\_fd**. This value is reserved. |
| FDSAN\_OWNER\_TYPE\_ZIPARCHIVE | Type for a .zip file. This value is reserved. |

**Return value**

Created tag, which can be used as an input of **fdsan\_exchange\_owner\_tag**.

## fdsan\_exchange\_owner\_tag

void fdsan\_exchange\_owner\_tag(int fd, uint64\_t expected\_tag, uint64\_t new\_tag);

**Description**

Modifies the tag of a file descriptor.

Locate the **FdEntry** based on the file descriptor and check whether the value of **close\_tag** is the same as that of **expected\_tag**. If yes, you can change the value of **FdEntry** with the value of **new\_tag** passed in.

If the value of **close\_tag** is not the same as that of **expected\_tag**, an error occurs. Perform error handling.

**Parameters**

| Value | Type | Description |
| :-- | :-- | :-- |
| fd | int | FD, which serves as an index of **FdEntry**. |
| expected\_tag | uint64\_t | Expected value of the tag. |
| new\_tag | uint64\_t | New value of the tag. |

## fdsan\_close\_with\_tag

int fdsan\_close\_with\_tag(int fd, uint64\_t tag);

**Description**

Closes a file descriptor based on the tag.

Locate the **FdEntry** based on the file descriptor. If **close\_tag** is the same as **tag**, the file descriptor can be closed. Otherwise, an exception occurs.

**Parameters**

| Value | Type | Description |
| :-- | :-- | :-- |
| fd | int | FD to close. |
| tag | uint64\_t | Expected tag. |

**Return value**

Returns **0** if the file descriptor is closed; returns **\-1** otherwise.

## fdsan\_get\_owner\_tag

uint64\_t fdsan\_get\_owner\_tag(int fd);

**Description**

Obtains tag information based on the given file descriptor.

Locate **FdEntry** based on the file descriptor and obtain **close\_tag**.

**Parameters**

| Value | Type | Description |
| :-- | :-- | :-- |
| fd | int | File descriptor. |

**Return value**

Tag of the file descriptor.

## fdsan\_get\_tag\_type

const char\* fdsan\_get\_tag\_type(uint64\_t tag);

**Description**

Obtains the file descriptor type based on the given tag.

The type information can be calculated based on the tag information.

**Parameters**

| Value | Type | Description |
| :-- | :-- | :-- |
| tag | uint64\_t | Owner tag. |

**Return value**

Type obtained.

## fdsan\_get\_tag\_value

uint64\_t fdsan\_get\_tag\_value(uint64\_t tag);

**Description**

Obtains the owner value based on the given tag.

The value contained in a tag can be obtained via offset calculation.

**Parameters**

| Value | Type | Description |
| :-- | :-- | :-- |
| tag | uint64\_t | Owner tag. |

**Return value**

Owner value obtained.

#### 4\. Example

Use fdsan to detect a double-close problem.

#include <unistd.h>
#include <fcntl.h>
#include <hilog/log.h>
#include <vector>
#include <thread>

void good\_write()
{
    sleep(1);
    int fd = open("log", O\_WRONLY | O\_APPEND);
    sleep(3);
    ssize\_t ret = write(fd, "fdsan test", 11);
    if (ret == -1) {
        OH\_LOG\_ERROR(LOG\_APP, "good write but failed?!");
    }
    close(fd);
}

void bad\_close()
{
    int fd = open("/dev/null", O\_RDONLY);
    close(fd);
    sleep(2);
    // This close is expected to be detected by fdsan.
    close(fd);
}

void functional\_test()
{
    std::vector<std::thread> threads;
    for (auto function : { good\_write, bad\_close }) {
        threads.emplace\_back(function);
    }
    for (auto& thread : threads) {
        thread.join();
    }
}

int main()
{
    functional\_test();
    return 0;
}

In this example, **good\_write** is used to open a file and write data to it; **bad\_close** is used to open a file and trigger a double-close problem. If the two threads run at the same time, the application execution is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/OicNFp0xTHqR3TG6ww2ucQ/en-us_image_0000002537925230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58C134F463B549FA75DC8F15E751AE555BD7F4AF62F11582EC2743DF07A7A91F)

The **open()** API returns file descriptors in sequence. After the main function is called, the first available file descriptor is **43**. When **bad\_close** is called, the file descriptor returned by **open()** for the first time is **43**. After **close()** is called, the file descriptor **43** becomes available. When **good\_write** is called, the **open()** function returns the first available file descriptor, that is, **43**. Since **bad\_close()** has the double-close problem, the file opened in another thread is incorrectly closed, causing a write failure.

The fdsan tool can detect such problems in two ways: using standard library APIs or implementing APIs with fdsan.

## Using Standard Library APIs

The **fopen**, **fdopen**, **opendir**, and **fdopendir** APIs in libc have integrated fdsan. Using these APIs instead of **open** can help detect file descriptor mishandling problems. For example, use **fopen** instead of **open**.

#include <stdio.h>
#include <errno.h>
#define TEMP\_FILE "/data/local/tmp/test.txt"

void good\_write()
{
    // fopen is protected by fdsan. Use fopen to replace open.
    // int fd = open(TEMP\_FILE, O\_RDWR);
    FILE \*f = fopen(TEMP\_FILE, "w+");
    if (f == NULL) {
        printf("fopen failed errno=%d\\n", errno);
        return;
    }
    // ssize\_t ret = write(fd, "fdsan test\\n", 11);
    int ret = fprintf(f, "fdsan test %d\\n", 11);
    if (ret < 0) {
        printf("fprintf failed errno=%d\\n", errno);
    }
    // close(fd);
    fclose(f);
}

## Log Information

Each file descriptor returned by **fopen** has a tag. When the file descriptor is closed by **close**, fdsan checks whether the file descriptor matches the tag. If the file descriptor does not match the tag, related log information is displayed by default. The log information for the preceding code is as follows:

\# hilog | grep MUSL-FDSAN
04-30 15:03:41.760 10933  1624 E C03f00/MUSL-FDSAN: attempted to close file descriptor 43,                             expected to be unowned, actually owned by FILE\* 0x00000000f7b90aa2

As indicated by the log, the file of **FILE** is closed by mistake. You can further locate the fault based on the address of **FILE**.

In addition, you can use **fdsan\_set\_error\_level** to set an error level. If **error\_level** is set to **FDSAN\_ERROR\_LEVEL\_FATAL**, fdsan also provides stack information for fault locating in addition to the log information. The following is an example of the stack information generated upon a crash after **error\_level** is set to **FDSAN\_ERROR\_LEVEL\_FATAL**:

Reason:Signal:SIGABRT(SI\_TKILL)@0x0000076e from:1902:20010043
Fault thread info:
Tid:15312, Name:e.myapplication
#00 pc 000e65bc /system/lib/ld-musl-arm.so.1(raise+176)(3de40c79448a2bbced06997e583ef614)
#01 pc 0009c3bc /system/lib/ld-musl-arm.so.1(abort+16)(3de40c79448a2bbced06997e583ef614)
#02 pc 0009de4c /system/lib/ld-musl-arm.so.1(fdsan\_error+116)(3de40c79448a2bbced06997e583ef614)
#03 pc 0009e2e8 /system/lib/ld-musl-arm.so.1(fdsan\_close\_with\_tag+836)(3de40c79448a2bbced06997e583ef614)
#04 pc 0009e56c /system/lib/ld-musl-arm.so.1(close+20)(3de40c79448a2bbced06997e583ef614)
#05 pc 000055d8 /data/storage/el1/bundle/libs/arm/libentry.so(bad\_close()+96)(f3339aac824c099f449153e92718e1b56f80b2ba)
#06 pc 00006cf4 /data/storage/el1/bundle/libs/arm/libentry.so(decltype(std::declval<void (\*)()>()()) std::\_\_n1::\_\_invoke\[abi:v15004\]<void (\*)()>(void (\*&&)())+24)(f3339aac824c099f449153e92718e1b56f80b2ba)
#07 pc 00006c94 /data/storage/el1/bundle/libs/arm/libentry.so(f3339aac824c099f449153e92718e1b56f80b2ba)
#08 pc 000067b8 /data/storage/el1/bundle/libs/arm/libentry.so(void\* std::\_\_n1::\_\_thread\_proxy\[abi:v15004\]<std::\_\_n1::tuple<std::\_\_n1::unique\_ptr<std::\_\_n1::\_\_thread\_struct, std::\_\_n1::default\_delete<std::\_\_n1::\_\_thread\_struct>>, void (\*)()>>(void\*)+100)(f3339aac824c099f449153e92718e1b56f80b2ba)
#09 pc 00105a6c /system/lib/ld-musl-arm.so.1(start+248)(3de40c79448a2bbced06997e583ef614)
#10 pc 000700b0 /system/lib/ld-musl-arm.so.1(3de40c79448a2bbced06997e583ef614)

The stack information provides information about **bad\_close** and all opened files, helping quickly locate faults.

**OpenFiles** lists all opened files.

**Field description**:

**fd->object description**: ID of the kernel object associated with the file descriptor **fd**.

**\[Content in square brackets\]**: Internal ID of the object, including the following:

-   For socket/pipe: Pseudo file system ID allocated by the kernel.
-   For a common file: Inode ID of the file system (data structure used by the OS to manage the file metadata and data blocks).
-   For **anon\_inode**: Object type name.

**native object of unknown type 0**: The tag value of the **fd** is 0.

OpenFiles:
0->/dev/null native object of unknown type 0
1->/dev/null native object of unknown type 0
2->/dev/null native object of unknown type 0
3->socket:\[28102\] native object of unknown type 0
4->socket:\[28103\] native object of unknown type 0
5->anon\_inode:\[eventpoll\] native object of unknown type 0
6->/sys/kernel/debug/tracing/trace\_marker native object of unknown type 0
7->anon\_inode:\[eventpoll\] native object of unknown type 0
8->anon\_inode:\[eventpoll\] native object of unknown type 0
9->/dev/console native object of unknown type 0
10->pipe:\[95598\] native object of unknown type 0
11->pipe:\[95598\] native object of unknown type 0
12->socket:\[18542\] native object of unknown type 0
13->pipe:\[96594\] native object of unknown type 0
14->socket:\[18545\] native object of unknown type 0
15->pipe:\[96594\] native object of unknown type 0
16->anon\_inode:\[eventfd\] native object of unknown type 0
17->/dev/binder native object of unknown type 0
18->/data/storage/el1/bundle/entry.hap native object of unknown type 0
19->anon\_inode:\[eventpoll\] native object of unknown type 0
20->anon\_inode:\[signalfd\] native object of unknown type 0
21->socket:\[29603\] native object of unknown type 0
22->anon\_inode:\[eventfd\] native object of unknown type 0
23->anon\_inode:\[eventpoll\] native object of unknown type 0
24->anon\_inode:\[eventfd\] native object of unknown type 0
25->anon\_inode:\[eventpoll\] native object of unknown type 0
26->anon\_inode:\[eventfd\] native object of unknown type 0
27->anon\_inode:\[eventpoll\] native object of unknown type 0
28->anon\_inode:\[eventfd\] native object of unknown type 0
29->anon\_inode:\[eventpoll\] native object of unknown type 0
30->anon\_inode:\[eventfd\] native object of unknown type 0
31->anon\_inode:\[eventpoll\] native object of unknown type 0
32->anon\_inode:\[eventfd\] native object of unknown type 0
33->anon\_inode:\[eventpoll\] native object of unknown type 0
34->anon\_inode:\[eventfd\] native object of unknown type 0
35->socket:\[97409\] native object of unknown type 0
36->socket:\[94716\] native object of unknown type 0
38->socket:\[94720\] native object of unknown type 0
40->/data/storage/el1/bundle/entry\_test.hap native object of unknown type 0
41->socket:\[95617\] native object of unknown type 0
42->/sys/kernel/debug/tracing/trace\_marker native object of unknown type 0
43->/dev/null FILE\* 4155724704
44->socket:\[94737\] native object of unknown type 0
45->pipe:\[95634\] native object of unknown type 0
46->pipe:\[95634\] native object of unknown type 0
47->pipe:\[95635\] native object of unknown type 0
49->pipe:\[95636\] native object of unknown type 0
50->pipe:\[95636\] native object of unknown type 0

## Implementing APIs with fdsan

You can also implement APIs with fdsan by using the **fdsan\_exchange\_owner\_tag** and **fdsan\_close\_with\_tag** functions. The former can be used to set a tag for a file descriptor; the latter can be used to check the tag when a file is closed.

The following is an example:

#include <errno.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#include <utility>

struct fdsan\_fd {
    fdsan\_fd() = default;

    explicit fdsan\_fd(int fd)
    {
        reset(fd);
    }

    fdsan\_fd(const fdsan\_fd& copy) = delete;
    fdsan\_fd(fdsan\_fd&& move)
    {
        \*this = std::move(move);
    }

    ~fdsan\_fd()
    {
        reset();
    }

    fdsan\_fd& operator=(const fdsan\_fd& copy) = delete;
    fdsan\_fd& operator=(fdsan\_fd&& move)
    {
        if (this == &move) {
            return \*this;
        }
        reset();
        if (move.fd\_ != -1) {
            fd\_ = move.fd\_;
            move.fd\_ = -1;
            // Acquire ownership from the moved-from object.
            exchange\_tag(fd\_, move.tag(), tag());
        }
        return \*this;
    }

    int get()
    {
        return fd\_;
    }

    void reset(int new\_fd = -1)
    {
        if (fd\_ != -1) {
            close(fd\_, tag());
            fd\_ = -1;
        }
        if (new\_fd != -1) {
            fd\_ = new\_fd;
            // Acquire ownership of the presumably unowned fd.
            exchange\_tag(fd\_, 0, tag());
        }
    }

  private:
    int fd\_ = -1;

    // Use the address of object as the file tag
    uint64\_t tag()
    {
        return reinterpret\_cast<uint64\_t>(this);
    }

    static void exchange\_tag(int fd, uint64\_t old\_tag, uint64\_t new\_tag)
    {
        if (&fdsan\_exchange\_owner\_tag) {
            fdsan\_exchange\_owner\_tag(fd, old\_tag, new\_tag);
        }
    }

    static int close(int fd, uint64\_t tag)
    {
        if (&fdsan\_close\_with\_tag) {
            return fdsan\_close\_with\_tag(fd, tag);
        }
    }
};

In this example, **fdsan\_exchange\_owner\_tag** is used to bind a file descriptor and the address of a struct object. Then, **fdsan\_close\_with\_tag** is used to check whether the tag matches the file descriptor before the file is closed. The expected tag is the struct object address.

You can use the implemented API in the following code to detect and prevent file descriptor mishandling problems:

#define TEMP\_FILE "/data/local/tmp/test.txt"

void good\_write()
{
    // int fd = open(DEV\_NULL\_FILE, O\_RDWR);
    fdsan\_fd fd(open(TEMP\_FILE, O\_CREAT | O\_RDWR));
    if (fd.get() == -1) {
        printf("fopen failed errno=%d\\n", errno);
        return;
    }
    ssize\_t ret = write(fd.get(), "fdsan test\\n", 11);
    if (ret == -1) {
        printf("write failed errno=%d\\n", errno);
    }
    fd.reset();
}

When the application is executed, the double-close problem of another thread can be detected. For details, see [Log Information](#log-information). You can also set **error\_level** to **fatal** so that fdsan can proactively crash after detecting a crash.

#### 5\. Signal Safety of the close Function

In the POSIX standard, the **close** function is defined as an async-signal-safe function, which can be safely called in the signal handler. However, in the system implementation integrated with the File Descriptor Sanitizer (fdsan) mechanism, the **close** function is no longer signal-safe.

This is because the implementation of fdsan depends on the mmap system call, which is not a signal-safe function. Therefore, instead of using **close()** in the signal handler, you can use the system call to implement the same functionality.
