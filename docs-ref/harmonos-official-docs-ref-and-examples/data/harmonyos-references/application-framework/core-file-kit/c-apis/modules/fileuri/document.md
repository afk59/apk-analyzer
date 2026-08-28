# fileUri

#### Overview

The **FileUri** module provides APIs for manipulating file Uniform Resource Identifiers (URIs).

It supports conversion between file URIs and paths, and verifies the validity of file URIs.

It is mainly used to verify the URI format and convert URIs. When files are shared between applications, the application sandbox path is converted into a URI based on specific rules.

You must ensure that all input parameters of the API are valid. The converted URI will be output regardless of whether it exists or not.

**System capability**: SystemCapability.FileManagement.AppFileService

**Since**: 12

#### Files

| Name | Description |
| :-- | :-- |
| [oh\_file\_uri.h](../../header-files/oh-file-uri-h/document.md) | Provides APIs for URI operations, including performing URI-path conversion, obtaining directory URIs, and verifying URIs. |
