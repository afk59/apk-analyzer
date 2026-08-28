# Rcp\_CertificateAuthority

#### Overview

CA used to verify the identity of a remote server.

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

char \* [content](#aca1038d6d4cc49da8dd95906030ed8ae)

 | 

A bundle of CA certificates for peer verification. The file must be in PEM format.

 |
| 

char \* [filePath](#abf23a6dbed9c18fd2a23fb21059abc2c)

 | 

CA certificate path for peer verification. The file must be in PEM format.

 |
| 

char \* [folderPath](#section1593319310222)

 | 

Path to the directory storing multiple CA certificates used for peer verification. Files in this directory must be in PEM format.

The file must be named with the hash of the subject name and the extension ".0".

 |

#### Member Variable Description

#### \[h2\]content

char\* Rcp\_CertificateAuthority::content

**Description**

A bundle of CA certificates for peer verification. The file must be in PEM format.

#### \[h2\]filePath

char\* Rcp\_CertificateAuthority::filePath

**Description**

CA certificate path for peer verification. The file must be in PEM format.

#### \[h2\]folderPath

char\* Rcp\_CertificateAuthority::folderPath

**Description**

Path to the directory storing multiple CA certificates used for peer verification. Files in this directory must be in PEM format.

The file must be named with the hash of the subject name and the extension ".0".
