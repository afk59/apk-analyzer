# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Lu1C6IETQyGw2TWnw44-rA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062351Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30BBAAE5FEDA52D6DE9FD112B55DFC974281BEBD2416FBF989B2E3B9F7B47448)

-   This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).
-   The error code mapping of Remote Communication Kit is in the format of 1007900000 + Curl error code. This section lists common error codes of Remote Communication Kit. For details about more error codes, please refer to [Curl Error Codes](https://curl.se/libcurl/c/libcurl-errors.html).

#### 1007900001 Unsupported Protocol

**Message**

Unsupported protocol.

**Description**

The server does not support this protocol version.

**Possible causes**

The input protocol version is not supported by the server.

**Solution**

Specify a protocol version supported by the server.

#### 1007900002 Initialization Failure

**Message**

Failed initialization

**Description**

The initialization failed.

**Possible causes**

Memory resource allocation failed.

**Solution**

Release memory resources to ensure that the available memory space is sufficient.

#### 1007900003 Invalid URL Format

**Message**

URL using bad/illegal format or missing URL.

**Description**

Invalid URL format.

**Possible causes**

The format of the input URL is incorrect.

**Solution**

Specify a URL of the correct format.

#### 1007900005 Failed to Resolve the Domain Name of the Proxy Server

**Message**

Couldn't resolve proxy name.

**Description**

The domain name of the proxy server cannot be resolved.

**Possible causes**

The URL of the proxy server is incorrect.

**Solution**

Specify a URL of the correct format.

#### 1007900006 Domain Name Resolution Failed

**Message**

Couldn't resolve host name.

**Description**

The domain name of the server cannot be resolved.

**Possible causes**

1.  The URL of the server is incorrect.
2.  The network is disconnected.

**Solution**

1.  Specify a URL of the correct format.
2.  Verify that the network is available.

#### 1007900007 Unable to Connect to the Server

**Message**

Couldn't connect to server.

**Description**

The server cannot be connected.

**Possible causes**

The network is disconnected.

**Solution**

Check the network connection.

#### 1007900008 Invalid Data Returned by the Server

**Message**

Weird server reply.

**Description**

The server returned invalid data.

**Possible causes**

The server encountered an error and returned data in non-HTTP format.

**Solution**

Check the server implementation.

#### 1007900009 Access to Remote Resources Denied

**Message**

Access denied to remote resource.

**Description**

Access to remote resources was rejected.

**Possible causes**

The access to the specified resource is rejected by the server.

**Solution**

Verify the HTTP request.

#### 1007900016 HTTP2 Framing Layer Error

**Message**

Error in the HTTP2 framing layer.

**Description**

An error occurred on the HTTP2 framing layer.

**Possible causes**

The server does not support HTTP2.

**Solution**

Capture and analyze packets to check whether HTTP2 is supported by the server.

#### 1007900018 Incomplete Data Returned by the Server

**Message**

Transferred a partial file.

**Description**

The data returned by the server is incomplete.

**Possible causes**

This problem is probable due to server implementation.

**Solution**

Check the server implementation.

#### 1007900023 Failure to Write the Received Data to the Disk/App Process

**Message**

Failed writing received data to disk/application.

**Description**

Received data failed to be written to the disk/app process.

**Possible causes**

The downloaded data size exceeds the upper limit.

**Solution**

When the data size is too large, you are advised to call [OnDataReceive](../rcp/document.md#section9264115918536) instead.

#### 1007900025 Upload Failure

**Message**

Upload failed (at start/before it took off).

**Description**

Upload failed.

**Possible causes**

The file is too large or the network is faulty. The server may reject the **STOR** command if FTP is used. The error buffer usually contains the reason from the server.

**Solution**

Check the file size and network status.

#### 1007900026 Failed to Open or Read Local Data from a File or App

**Message**

Failed to open/read local data from file/application.

**Description**

Failed to open or read local data from a file or app.

**Possible causes**

No file reading permission.

**Solution**

Check the permissions granted to the app.

#### 1007900027 Insufficient Memory

**Message**

Out of memory.

**Description**

The memory is insufficient.

**Possible causes**

The memory is insufficient.

**Solution**

Check the system memory.

#### 1007900028 Operation Timeout

**Message**

Timeout was reached.

**Description**

The operation timed out.

**Possible causes**

The TCP connection or the read/write operation times out.

**Solution**

Rectify the network connection error. If the error code 1007900028 is displayed for multiple times, you are advised to close the session and create a session again.

#### 1007900035 SSL Connection Error

**Message**

SSL connect error.

**Description**

SSL connection error.

**Possible causes**

The TLS version or TLS cipher suite is incorrectly configured.

**Solution**

Verify the TLS version and TLS cipher suite configuration.

#### 1007900037 File Reading Failure

**Message**

Couldn't read a file:// file.

**Description**

Failed to read a file.

**Possible causes**

1\. The file path is incorrect or the file does not exist.

2\. The permission on the file is insufficient.

3\. The path format is incorrect.

**Solution**

1\. Ensure that the file path is correct and the file exists.

2\. Ensure that the app process has the required operation permission on the file specified by the path.

3\. Ensure that the file path format is correct.

#### 1007900042 Operation Stopped by an App Callback

**Message**

Operation was aborted by an application callback.

**Description**

The operation was stopped by a callback function of the app.

**Possible causes**

The callback function contains abnormal logic processing, such as infinite loops, abnormal interruption, and time-consuming synchronous operations.

**Solution**

Check all callback functions and ensure that they do not contain any abnormal or redundant processing logic.

#### 1007900045 Local End Binding Failure

**Message**

Failed binding local connection end.

**Description**

Local end binding failed.

**Possible causes**

The specified network port or IP address does not exist or is unavailable.

**Solution**

Ensure that the network port or IP address exist and are available.

#### 1007900047 Redirections Reached the Maximum

**Message**

Number of redirects hit maximum amount.

**Description**

The number of redirections has reached the maximum.

**Possible causes**

Redirections are too frequent.

**Solution**

Check the server implementation.

#### 1007900049 Incorrect Option Format

**Message**

Malformed option provided in a setopt.

**Description**

The option format is incorrect.

**Possible causes**

The IP address format defined in [StaticDnsRule](../rcp/document.md#section47911616155511) or [DynamicDnsRule](../rcp/document.md#section8160554134811) is incorrect.

**Solution**

Ensure that the input parameter format of [StaticDnsRule](../rcp/document.md#section47911616155511) and [DynamicDnsRule](../rcp/document.md#section8160554134811) is correct.

#### 1007900052 Nothing Returned from Server

**Message**

Server returned nothing (no headers, no data).

**Description**

Nothing returned from server.

**Possible causes**

This problem is due to server implementation.

**Solution**

Check the server implementation.

#### 1007900055 Failed to Send Network Data

**Message**

Failed sending data to the peer.

**Description**

An error occurred while sending network data to the peer end.

**Possible causes**

The network is faulty.

**Solution**

Rectify the network connection error.

#### 1007900056 Failed to Receive Network Data

**Message**

Failure when receiving data from the peer.

**Description**

An error occurred while receiving network data from the peer end.

**Possible causes**

The network is faulty.

**Solution**

Rectify the network connection error.

#### 1007900058 Local SSL Certificate Error

**Message**

Problem with the local SSL certificate.

**Description**

The local SSL certificate is incorrect.

**Possible causes**

The SSL certificate format is incorrect.

**Solution**

Check the format of the SSL certificate.

#### 1007900059 Unable to Use the Specified SSL Password

**Message**

Couldn't use specified SSL cipher.

**Description**

Cannot use the specified SSL password.

**Possible causes**

The system does not support the cipher algorithm negotiated between the client and server.

**Solution**

Capture and analyze packets to check whether the cipher algorithm is supported.

#### 1007900060 Incorrect SSL Certificate or SSH Key of the Remote Server

**Message**

SSL peer certificate or SSH remote key was not OK.

**Description**

The SSL certificate or SSH key of the remote server is incorrect or invalid.

**Possible causes**

It is probable that the server identity verification fails because the certificate has expired.

**Solution**

Check the validity period of the certificate.

#### 1007900061 Unrecognized or Incorrect HTTP Encoding Format

**Message**

Unrecognized or bad HTTP Content or Transfer-Encoding.

**Description**

The HTTP encoding format cannot be identified or is incorrect.

**Possible causes**

The HTTP encoding format is incorrect.

**Solution**

Check the server implementation. Currently, only gzip encoding is supported.

#### 1007900063 Maximum File Size Exceeded

**Message**

Maximum file size exceeded.

**Description**

The file size exceeded the maximum.

**Possible causes**

The value of **content-length** is inconsistent with the actual file size.

**Solution**

Check the server implementation.

#### 1007900065 Sending Failure Due To Failed Data Flow Rollback

**Message**

Send failed since rewinding of the data stream failed.

**Description**

Sending failed because the data flow failed to be rolled back.

**Possible causes**

Data is retransmitted due to a network exception.

**Solution**

Ensure that the network connection is normal.

#### 1007900070 Insufficient Disk Space of the Server

**Message**

Disk full or allocation exceeded.

**Description**

The disk space of the server is insufficient.

**Possible causes**

The server disk is full.

**Solution**

Check the server disk space.

#### 1007900073 Uploaded File Already Exists

**Message**

Remote file already exists.

**Description**

The server finds that the uploaded file already exists.

**Possible causes**

The uploaded file already exists.

**Solution**

Check the server implementation.

#### 1007900077 No SSL CA Certificate or Access Permission

**Message**

Problem with the SSL CA cert (path? access rights?).

**Description**

The SSL CA certificate does not exist or the access permission is not available.

**Possible causes**

The certificate does not exist or the access permission is not available.

**Solution**

Check whether the SSL CA certificate exists or the access permission is granted.

#### 1007900078 URL Requested File Not Found

**Message**

Remote file not found.

**Description**

The file requested by the specified URL does not exist.

**Possible causes**

The file requested by the specified URL does not exist.

**Solution**

Check whether the file requested based on the specified URL exists.

#### 1007900089 Maximum Number of Connections Reached

**Message**

The max connection limit is reached.

**Description**

The number of connections has reached the upper limit.

**Possible causes**

The number of session connections has reached the upper limit. No connection is available.

**Solution**

Limit the number of concurrent requests that can be initiated at the same time, and free up a connection immediately after a request is complete.

#### 1007900090 Unmatching SSL Public Key and Fixed Public Key

**Message**

SSL public key does not match pinned public key.

**Description**

The SSL public key does not match the fixed public key.

**Possible causes**

1\. The server certificate has been changed and no longer matches the client certificate.

2\. The format of the client public key is incorrect.

**Solution**

1\. Ensure that the public key format is correct.

2\. Ensure that the public key used by the client is the same as that used by the server.

#### 1007900092 Stream Error at the HTTP/2 Layer

**Message**

Stream error in the HTTP/2 framing layer.

**Description**

A stream error occurred at the HTTP/2 layer.

**Possible causes**

1\. The HTTP/2 stream is closed by the server.

2\. The proxy server or firewall incorrectly intercepts or modifies the HTTP/2 stream.

**Solution**

1\. Check the reason why the server closes the HTTP/2 stream.

2\. Check the interception rules of the proxy server or firewall.

#### 1007900094 Identity Verification Failed

**Message**

An authentication function returned an error.

**Description**

Identity verification failed.

**Possible causes**

The specified identity verification field does not match that on the server.

**Solution**

Check whether the specified identity verification field matches that on the server.

#### 1007900095 HTTP/3 Error

**Message**

HTTP/3 error.

**Description**

An HTTP/3 error occurred.

**Possible causes**

The server or network does not support HTTP/3.

**Solution**

1\. Use the HTTP of an earlier version to initiate the request.

2\. Upgrade the HTTP protocol on the server.

#### 1007900097 Proxy Handshake Error

**Message**

proxy handshake error.

**Description**

A proxy handshake error occurred.

**Possible causes**

1\. The proxy server IP address or port number is incorrect.

2\. Proxy authentication failed.

3\. The proxy server rejected the connection.

**Solution**

1\. Verify the proxy server settings.

2\. Ensure that the proxy is available.

3\. Check the proxy server logs to locate the error cause.

#### 1007900100 Data Length Out of Range

**Message**

A value or data field grew larger than allowed.

**Description**

The data length is out of range.

**Possible causes**

The requested or uploaded data size is too large, exceeding the upper limit of the client or server.

**Solution**

1\. Use the streaming data transmission API.

2\. Ensure that uploaded or downloaded data size is within the allowed range.

#### 1007900999 Internal Error

**Message**

Internal Error.

**Description**

An internal error occurred.

**Possible causes**

An unknown error occurs in the system, and the request cannot be processed.

**Solution**

Restart the app or contact technical support for help.

#### 1007900998 Unsupported Request Method

**Message**

Method not supported.

**Description**

The method is not supported.

**Possible causes**

An unsupported API method or protocol is used.

**Solution**

Check the code or app to ensure that the method and protocol used are correct.

#### 1007900997 Invalid Content Type

**Message**

Invalid content type.

**Description**

Invalid content type.

**Possible causes**

The request uses an unsupported data format or content type.

**Solution**

Ensure that the content type and data format in the request are correct.

#### 1007900996 Unsupported Proxy Type

**Message**

Proxy type not supported.

**Description**

The proxy type is not supported.

**Possible causes**

An unsupported proxy type is used.

**Solution**

Change the proxy type or disable the proxy, and try again.

#### 1007900995 Failed to Obtain the System Proxy

**Message**

Get system proxy failed.

**Description**

Failed to obtain the system proxy.

**Possible causes**

The proxy is not configured correctly.

**Solution**

Ensure that the proxy is correctly configured.

#### 1007900994 Sessions Reached Maximum

**Message**

Sessions number reached limit.

**Description**

The number of sessions has reached the maximum.

**Possible causes**

Too many sessions have been created. A maximum of 1024 session instances can be created since version 5.1.0(18).

**Solution**

Reduce the number of sessions to 1024 or less.

#### 1007900993 Session Closed

**Message**

Session is closed.

**Description**

The session has been closed.

**Possible causes**

The session has been closed or is expired.

**Solution**

Open the session or create a new session, and try again.

#### **1007900992** Request Canceled

**Message**

Request is canceled.

**Description**

The request has been canceled.

**Possible causes**

The request times out or the network connection is interrupted.

**Solution**

Initiate the request again and ensure that the network connection is correct.

#### 1007900991 Response Sent by the Server Does Not Comply with Format Requirements or Specifications

**Message**

The response is invalid.

**Description**

The response returned by the server does not comply with the expected format or specifications and cannot be properly parsed or processed by the client.

**Possible causes**

The parameters or format of the request sent by the client does not comply with server requirements. As a result, the server returns an error response.

**Solution**

Verify that the request sent by the client is correct, with all required parameters set correctly and the format as expected.

#### 1007900988 File Opening Error

**Message**

Cannot open file.

**Description**

The file failed to be opened.

**Possible causes**

The app does not have the read and write permission on the file specified by the path.

**Solution**

Check whether the app has the read and write permission on the file specified by the path.

#### 1007900987 Directory Creation Error

**Message**

Cannot create directory.

**Description**

An error occurred during directory creation.

**Possible causes**

The app does not have the permission to create a directory under this path.

**Solution**

Check whether the app has the permission to create a directory under this path.

#### 1007900986 Cellular Connection Setup Timeout

**Message**

Cannot establish cellular link.

**Description**

When the cellular data connection is set up in **cellular** mode specified in [PathPreference](../rcp/document.md#section828055885811), the cellular data activation times out because requirements are not met.

**Possible causes**

A situation where cellular data cannot be activated occurs, for example, the user enables airplane mode or deactivates the SIM card.

**Solution**

Check the network settings and ensure that the cellular data activation conditions are met.

#### 1007900985 File System I/O Error

**Message**

File system IO error.

**Description**

File operation failed.

**Possible causes**

The file failed to be created, accessed, or deleted.

**Solution**

Check whether the file path is valid and whether the app has the permission to access the file path.

#### 1007900401 Parameter Setting Error

**Message**

Parameter error.

**Description**

Invalid parameter.

**Possible causes**

The cache storage path is not specified, or the cache storage limit is set to a negative value.

**Solution**

Ensure that the parameter settings are correct.

#### 201 Permission Denied

**Message**

Permission denied.

**Description**

The app does not have the permission or the permission configuration format is incorrect.

**Possible causes**

The permission configuration of the app is incorrect.

**Solution**

Ensure that the permission configuration is correct for the app.

#### 401 Parameter Error

**Message**

Parameter error.

**Description**

Invalid function input parameter.

**Possible causes**

The input parameter is invalid.

**Solution**

Ensure that the input parameter is correct.

#### 1007910001 Request Data Transmission Error

**Message**

Urpc some error.

**Description**

An error occurred during URPC data transmission.

**Possible causes**

For details, please check URPC logs.

**Solution**

Check URPC logs for fault locating.

#### 1007910002 Request Timeout

**Message**

Timeout was reached.

**Description**

The URPC request duration exceeds the timeout interval set in [UrpcConnectConfiguration](../urpc/document.md#section4802256134519).

**Possible causes**

1.  The request sending queue was blocked and the request failed to be sent.
2.  An exception occurred on the server and the response cannot be sent properly.

**Solution**

1.  For cause 1: Send the request again.
2.  For cause 2: Restart the server.

#### 1007910003 Request Canceled

**Message**

Request is cancel.

**Description**

The URPC request was canceled.

**Possible causes**

A URPC request was canceled because an associated resource was cleared.

**Solution**

Check whether resources are cleared before the request is completed.

#### 1007910004 Network Disconnected

**Message**

Urpc disconnect.

**Description**

The URPC was disconnected.

**Possible causes**

The network was disconnected.

**Solution**

Rectify the network connection error.

#### 1007910005 Too Many Requests

**Message**

Limit of request number.

**Description**

The number of URPC requests has reached the upper limit allowed by the server.

**Possible causes**

A large number of requests are sent without timely processing.

**Solution**

Check the request processing logic.

#### 1007910006 Request Too Large

**Message**

Limit of request size.

**Description**

The URPC request size has reached the upper limit of the system memory.

**Possible causes**

The size of the request exceeds the upper limit.

**Solution**

Check the request processing logic.

#### 1007910008 Failure to Resume Sending

**Message**

Resume transmit error.

**Description**

Data sending failed to be resumed in the resumable transmission scenario.

**Possible causes**

The transmission link is abnormal when resumable transmission is triggered.

**Solution**

Check logs on the request sender side.

#### 1007910099 Stub Query Failure upon Cancellation

**Message**

Urpc stub not found.

**Description**

No stub information is found when the **cancel** method is called.

**Possible causes**

The stub is destroyed too early.

**Solution**

Check whether the [UrpcStub](../urpc/document.md#section1671892662116) class is correctly declared and used.

#### 10079100997 Data Deserialization Failed

**Message**

Deserialize failed.

**Description**

Data deserialization failed.

**Possible causes**

The data content is incorrect for deserialization.

**Solution**

Check logs on the request sender side.

#### 10079100998 Remote Method Calling Error

**Message**

Function name error.

**Description**

The requested method name is incorrect.

**Possible causes**

The requested method name is incorrect.

**Solution**

Check the method name in the request.

#### 10079100999 UrpcStub Query Failure

**Message**

Urpc stub not found.

**Description**

UrpcStub is not correctly used.

**Possible causes**

UrpcStub is not correctly used.

**Solution**

Check whether the [UrpcStub](../urpc/document.md#section1671892662116) class is correctly declared and used.
