# What data formats are supported by extraData in an HTTP network request?

**extraData** indicates additional data in an HTTP request. It varies depending on the HTTP request method.

-   If the HTTP request uses a POST or PUT method, this parameter serves as the content of the HTTP request.
-   If the HTTP request uses a GET, OPTIONS, DELETE, TRACE, or CONNECT method, this parameter is a supplemental parameter for the HTTP request and will be appended to the URL when the request is sent.
-   For a string object, you need to encode the object before passing it to the HTTP request.
