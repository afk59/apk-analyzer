# HiDebug\_MallocDispatch

typedef struct HiDebug\_MallocDispatch {...} HiDebug\_MallocDispatch

#### Overview

Defines the struct types of the replaceable/restorable **HiDebug\_MallocDispatch** table of the application process.

**Since**: 20

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Function

| Name | Description |
| :-- | :-- |
| [void\* (\*malloc)(size\_t)](#malloc) | Pointer to the custom **malloc** function. |
| [void\* (\*calloc)(size\_t, size\_t)](#calloc) | Pointer to the custom **calloc** function. |
| [void\* (\*realloc)(void\*, size\_t)](#realloc) | Pointer to the custom **realloc** function. |
| [void (\*free)(void\*)](#free) | Pointer to the custom **free** function. |
| [void\* (\*mmap)(void\*, size\_t, int, int, int, off\_t)](#mmap) | Pointer to the custom **mmap** function. |
| [int (\*munmap)(void\*, size\_t)](#munmap) | Pointer to the custom **munmap** function. |

#### Member Function Description

#### \[h2\]malloc()

void\* (\*malloc)(size\_t)

**Description**

Pointer to the custom **malloc** function.

#### \[h2\]calloc()

void\* (\*calloc)(size\_t, size\_t)

**Description**

Pointer to the custom **calloc** function.

#### \[h2\]realloc()

void\* (\*realloc)(void\*, size\_t)

**Description**

Pointer to the custom **realloc** function.

#### \[h2\]free()

void (\*free)(void\*)

**Description**

Pointer to the custom **free** function.

#### \[h2\]mmap()

void\* (\*mmap)(void\*, size\_t, int, int, int, off\_t)

**Description**

Pointer to the custom **mmap** function.

#### \[h2\]munmap()

int (\*munmap)(void\*, size\_t)

**Description**

Pointer to the custom **munmap** function.
