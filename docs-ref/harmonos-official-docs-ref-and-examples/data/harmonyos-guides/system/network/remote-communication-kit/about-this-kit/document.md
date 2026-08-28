# About This Kit

#### Overview

Remote Communication Kit provides the following network data request functions:

-   HTTP request capability: Remote Communication Kit offers a scenario-based HTTP communication capability. Compared with the HTTP request capability of Network Kit, Remote Communication Kit provides scenario-based APIs that are easier to employ, as described in [Supported HTTP Network Request Scenarios](#section123516402589). You can select the kit that best suits your needs.
-   Unified Remote Procedure Call (URPC): a high-performance RPC communication library. It is designed for implementing robust remote function calls and features resilience against weak network conditions and support for multi-path transmission (cellular network and Wi-Fi). You can complete remote procedure calls through the URPC with greater ease.

#### Relevant Concepts

HTTP is short for Hypertext Transfer Protocol, which is a protocol used to transfer data between a client and a server. It operates on a client-server model where the client initiates requests and the server returns responses.

An HTTP request is a client-initiated message to a server, involving the following basic parts:

-   Request method: method used by the client to send a request to the server, such as GET, POST, PUT, DELETE, OPTIONS, HEAD, and PATCH.
-   Uniform Resource Locator (URL): specifies the address of the resource to be accessed.
-   Request header: contains additional information, such as the request source, client browser type, language, and character set.
-   Request body: contains data sent from the client to the server, such as form data.
-   HTTP version: version number of the HTTP protocol, for example, HTTP/1.1 and HTTP/2.
-   Status code: code returned by the server in response to a request. For example, **200** indicates success and **404** indicates that the requested resource does not exist.
-   Response header: contains additional information, such as the server type, response date, and content type.
-   Response body: contains the data returned by the server to the client, such as HTML and JSON data.

| 
Request Method

 | 

Description

 |
| :-- | :-- |
| 

GET

 | 

Requests specific resources. Common scenario: obtaining resources such as web pages, images, and videos.

 |
| 

POST

 | 

Submits resources, which are usually forms. Common scenario: submitting data, such as form data and files.

 |
| 

OPTIONS

 | 

Obtains HTTP methods that a source supports. Common scenario: obtaining the HTTP methods supported by a resource, for example, the request methods of an API.

 |
| 

HEAD

 | 

Obtains the resource metadata, which functions similarly as the GET request, except that this method returns only metadata such as the response header. Common scenario: obtaining resource header information, such as the file size and modification time.

 |
| 

PUT

 | 

Updates a resource that already exists on the server by completely replacing the resource at the specified path. Common scenario: updating a resource, such as modifying a file or database record.

 |
| 

DELETE

 | 

Deletes a specified resource. Common scenario: deleting resources such as users and articles.

 |
| 

PATCH

 | 

Updates a part of a resource. Common scenario: updating only a part of a specified resource on the server, for example, updating only some attributes and fields of a resource. This method does not replace the entire resource.

 |

#### Supported HTTP Network Request Scenarios

| 
Scenario

 | 

Description

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

Sending PATCH requests

 | 

Request are sent in PATCH mode.

 | 

\-

 |
| 

Setting the base URL in a session

 | 

The base URL of a session will be automatically appended before the URL unless the URL is an absolute URL.

 | 

\-

 |
| 

Canceling automatic redirection

 | 

Automatic redirection of HTTP requests can be canceled.

 | 

\-

 |
| 

Intercepting requests/responses

 | 

Requests and responses can be intercepted before they arrive at the peer end.

 | 

\-

 |
| 

Canceling requests

 | 

Requests can be canceled before sending, during transfer, and after reception.

 | 

\-

 |
| 

Caching responses

 | 

Responses can be cached, which will be read first later.

 | 

The cache function takes effect when the process is started. The new cached data will replace the existing cached data.

 |
| 

Setting the response data type

 | 

The response data type can be defined, including string, object, and ArrayBuffer.

 | 

By default, the response body type is **ArrayBuffer**. The caller can retrieve data as an object or string by utilizing the **toJSON** or **toString** method of the response.

 |
| 

Custom Certificate Verification

 | 

The logic for verifying client and server certificates for connection can be customized.

 | 

\-

 |
| 

Skipping SSL verification

 | 

SSL certificate verification can be skipped for the server during SSL connection setup.

 | 

\-

 |
| 

Customizing DNS resolution

 | 

The DNS server can be customized, and static DNS rules can be configured.

 | 

\-

 |
| 

Capturing detailed tracing information

 | 

Detailed tracing information can be captured from HTTP requests, so you can collect information that can be used for debugging, performance analysis, and data stream tracing.

 | 

\-

 |
| 

Obtaining time-related information of HTTP requests

 | 

The time-related information in each phase of an HTTP request can be obtained.

 | 

\-

 |

#### Constraints

This kit supports phones, 2-in-1 devices, tablets, wearables, and (since 5.1.1(19)) TVs. Lite wearables are not supported currently.

#### Emulator Support

This kit supports Emulator-based development.
