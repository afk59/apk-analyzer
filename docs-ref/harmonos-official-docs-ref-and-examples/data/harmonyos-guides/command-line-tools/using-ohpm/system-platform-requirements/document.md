# System Platform Requirements

ohpm can be used on Windows, macOS, and Linux.

ohpm builds dependencies through soft links or symbolic links. Different operating systems must meet the following requirements:

**Windows**

-   The type of the file system where the project code file is located must be NTFS (which is the default file system in Windows).
-   When source code dependency is used, the dependent source code module and the depended source code module must be in the same drive. Cross-drive dependency is not allowed.

**macOS**

-   The type of the file system where the project code file is located must be APFS (which is the default file system in macOS).
-   If a file system (such as FAT32 or exFAT) that does not support symbolic links is mounted to macOS, symbolic links cannot be created on the file system.

**Linux**

-   Common Linux file system types, such as EXT4, Btrfs, XFS, and ZFS, meet the requirements.
-   In some older or simpler file systems, there may be limitations that prevent the creation or correct resolution of symbolic links.
