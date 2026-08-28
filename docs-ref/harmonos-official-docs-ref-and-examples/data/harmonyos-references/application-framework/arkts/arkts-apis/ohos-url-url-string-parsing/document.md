# @ohos.url (URL String Parsing)

The url module provides APIs for parsing URL strings and constructing [URL](#url) instances to process URL strings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/8dnHqyENTqGfIpB8pvcMOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84D65610741FE7F9971FF99570FF15A0CBF367877B5FE097C9713FCFEA310520)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { url } from '@kit.ArkTS';

#### URLParams9+

A utility class for parsing, constructing, and manipulating URL parameters. It provides a unified API to process parameters (such as query parameters and path parameters).

#### \[h2\]constructor9+

constructor(init?: string\[\]\[\] | Record<string, string> | string | URLParams)

A constructor used to create a **URLParams** instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| init | string\[\]\[\] | Record<string, string> | string | URLParams | No | 
Input parameter objects, which include the following:

\- **string\[\]\[\]**: two-dimensional string array.

\- **Record<string, string>**: list of objects.

\- **string**: string.

\- **URLParams**: object.

The default value is **null**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

// Construct a URLParams object in string\[\]\[\] mode.
let objectParams = new url.URLParams(\[ \['user1', 'abc1'\], \['query2', 'first2'\], \['query3', 'second3'\] \]);
// Construct a URLParams object in Record<string, string> mode.
let objectParams1 = new url.URLParams({"fod" : '1' , "bard" : '2'});
// Construct a URLParams object in string mode.
let objectParams2 = new url.URLParams('?fod=1&bard=2');
// Construct a URLParams object using the search property of the url object.
let urlObject = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
let objectParams3 = new url.URLParams(urlObject.search);
// Construct a URLParams object using the params property of the url object.
let urlObject1 = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
let objectParams4 = urlObject1.params;

#### \[h2\]append9+

append(name: string, value: string): void

Appends a key-value pair into the query string.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the key-value pair to append. |
| value | string | Yes | Value of the key-value pair to append. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.append('fod', '3');

#### \[h2\]delete9+

delete(name: string): void

Deletes key-value pairs of the specified key.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the key-value pairs to delete. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.delete('fod');

#### \[h2\]getAll9+

getAll(name: string): string\[\]

Obtains all the values based on the specified key.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | All the values obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3'); // Add a second value for the fod parameter.
console.info(params.getAll('fod').toString()) // Output \["1","3"\].

#### \[h2\]entries9+

entries(): IterableIterator<\[string, string\]>

Obtains an ES6 iterator. Each item of the iterator is an array, and the first and second fields of each array are the key and value respectively.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[string, string\]> | ES6 iterator. |

**Example**

let paramsObject = new url.URLParams("keyName1=valueName1&keyName2=valueName2");
let pair = paramsObject.entries();
for (let item of pair) {
    console.info(item\[0\] + '=' + item\[1\]);
}
// keyName1=valueName1
// keyName2=valueName2

#### \[h2\]forEach9+

forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void

Traverses the key-value pairs in the **URLSearchParams** instance by using a callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the key-value pairs in the **URLSearchParams** instance. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this object. |

**Table 1** callbackFn parameter description

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Value that is currently traversed. |
| key | string | Yes | Key that is currently traversed. |
| searchParams | [URLParams](#urlparams9) | Yes | Instance that invokes the **forEach** method. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

const myURLObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
myURLObject.params.forEach((value, name, searchParams) => {
    console.info(name, value, myURLObject.params === searchParams);
});

#### \[h2\]get9+

get(name: string): string | null

Obtains the value of the first key-value pair based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/CVv4wRfXRSmBgItXfqoWYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=587229D4482D63879337325EC4FF23C1D13F2D39454020BEE162DE17AFBE395B)

If the key-value pair does not exist, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key specified to obtain the value. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | null | The first value is returned. If no value is found, **null** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let paramsObject = new url.URLParams('name=Jonathan&age=18');
let name = paramsObject.get("name"); // is the string "Jonathan"
let age = paramsObject.get("age"); // is the string "18"
let getObj = paramsObject.get("abc"); // undefined

#### \[h2\]has9+

has(name: string): boolean

Checks whether a key has a value.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key specified to search for its value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value exists; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
let result = paramsObject.has('bard');

#### \[h2\]set9+

set(name: string, value: string): void

Sets the value for a key.

If key-value pairs matching the specified key exist, the value of the first key-value pair will be set to the specified value and other key-value pairs will be deleted. Otherwise, the key-value pair will be appended to the query string.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the value to set. |
| value | string | Yes | Value to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.set('baz', '3'); // Add a third parameter.

#### \[h2\]sort9+

sort(): void

Sorts all key-value pairs in this object based on the Unicode code points of the keys. This method uses a stable sorting algorithm. (The relative order between key-value pairs with equal keys is retained.)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Example**

let paramsObject = new url.URLParams("c=3&a=9&b=4&d=2"); // Create a test URLParams object
paramsObject.sort(); // Sort the key/value pairs
console.info(paramsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2

#### \[h2\]keys9+

keys(): IterableIterator<string>

Obtains an ES6 iterator that contains the keys of all the key-value pairs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<string> | An ES6 iterator that contains the keys of all the key-value pairs. |

**Example**

let paramsObject = new url.URLParams("key1=value1&key2=value2");
let keys = paramsObject.keys();
for (let key of keys) {
  console.info(key);
}
// key1
// key2

#### \[h2\]values9+

values(): IterableIterator<string>

Obtains an ES6 iterator that contains the values of all the key-value pairs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<string> | An ES6 iterator that contains the values of all the key-value pairs. |

**Example**

let paramsObject = new url.URLParams("key1=value1&key2=value2");
let values = paramsObject.values();
for (let value of values) {
  console.info(value);
}
// value1
// value2

#### \[h2\]\[Symbol.iterator\]9+

\[Symbol.iterator\](): IterableIterator<\[string, string\]>

Obtains an ES6 iterator. Each item of the iterator is an array, and the first and second fields of each array are the key and value respectively.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[string, string\]> | ES6 iterator. |

**Example**

const paramsObject = new url.URLParams('fod=bay&edg=bap');
let iter = paramsObject\[Symbol.iterator\]();
for (let pair of iter) {
  console.info(pair\[0\] + ', ' + pair\[1\]);
}
// fod, bay
// edg, bap

#### \[h2\]toString9+

toString(): string

Obtains search parameters that are serialized as a string and, if necessary, percent-encodes the characters in the string.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String of serialized search parameters, which is percent-encoded if necessary. |

**Example**

let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3');
console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'

#### URL

Provides APIs for parsing, constructing, standardizing, and encoding URL strings.

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hash | string | No | No | String that contains a harsh mark (#) followed by the fragment identifier of a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| host | string | No | No | Host information in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| hostname | string | No | No | Hostname (without the port) in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| href | string | No | No | String that contains the whole URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| origin | string | Yes | No | Read-only string that contains the Unicode serialization of the origin of the represented URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| password | string | No | No | Password in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| pathname | string | No | No | Path in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| port | string | No | No | Port in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| protocol | string | No | No | Protocol in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| search | string | No | No | Serialized query string in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| searchParams(deprecated) | [URLSearchParams](#urlsearchparamsdeprecated) | Yes | No | 
**URLSearchParams** object allowing access to the query parameters in a URL.

\- **NOTE**: This property is supported since API version 7 and is deprecated since API version 9. You are advised to use params9+ instead.

 |
| params9+ | [URLParams](#urlparams9) | Yes | No | **URLParams** object allowing access to the query parameters in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |
| username | string | No | No | Username in a URL. **Atomic service API**: This API can be used in atomic services since API version 11. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/gEUaIL80SWSlGiAlyrftjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7650F9F5F30140FD3BE6B21ADCAC3BA2598569118E579FE6029F57463BBB10D1)

When parsing a URL string, if the port specified in the input is the default port for the current protocol, it will be parsed as an empty string. The default ports are as follows.

| Protocol | Default Port |
| :-- | :-- |
| http: | 80 |
| https: | 443 |
| ftp: | 21 |
| gopher: | 70 |
| ws: | 80 |
| wss: | 443 |

**Example**

let that = url.URL.parseURL('http://username:password@host:8080/directory/file?foo=1&bar=2#fragment');
console.info("hash " + that.hash); // hash #fragment
console.info("host " + that.host); // host host:8080
console.info("hostname " + that.hostname); // hostname host
console.info("href " + that.href); // href http://username:password@host:8080/directory/file?foo=1&bar=2#fragment
console.info("origin " + that.origin); // origin http://host:8080
console.info("password " + that.password); // password password
console.info("pathname " + that.pathname); // pathname /directory/file
console.info("port " + that.port); // port 8080
console.info("protocol " + that.protocol); // protocol http:
console.info("search " + that.search); // search ?foo=1&bar=2
console.info("username " + that.username); // username username
// The return value of that.params is a URLParams object.
console.info("params: foo " + that.params.get("foo")); // params: foo 1

let urlObj = url.URL.parseURL('http://testhost:80/directory/file?foo=1');
console.info("port " + urlObj.port); // port
console.info("toString " + urlObj.toString()); // toString http://testhost/directory/file?foo=1

#### \[h2\]constructor(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/P41pSzM6Rgau_Tr1I4F_Ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4BF52D1FDA243803FF79A1322AFC9B65BB87E9E53A751CC7F66E0CD6A7EF41F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [parseURL9+](#parseurl9) instead.

constructor(url: string, base?: string | URL)

Creates a URL.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | 
A string representing an absolute or a relative URL.

In the case of a relative URL, you must specify **base** to parse the final URL.

In the case of an absolute URL, the passed **base** will be ignored.

 |
| base | string | URL | No | 

Either a string or an object. The default value is **undefined**.

\- **string**: string.

\- **URL**: URL object.

 |

**Example**

let mm = 'https://username:password@host:8080';
let a = new url.URL("/", mm); // Output 'https://username:password@host:8080/';
let b = new url.URL(mm); // Output 'https://username:password@host:8080/';
new url.URL('path/path1', b); // Output 'https://username:password@host:8080/path/path1';
let c = new url.URL('/path/path1', b);  // Output 'https://username:password@host:8080/path/path1';
new url.URL('/path/path1', c); // Output 'https://username:password@host:8080/path/path1';
new url.URL('/path/path1', a); // Output 'https://username:password@host:8080/path/path1';
new url.URL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output https://www.exampleUrl/path/path1
new url.URL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
new url.URL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
new url.URL('https://www.example.com', ); // Output https://www.example.com/
new url.URL('https://www.example.com', b); // Output https://www.example.com/

#### \[h2\]constructor9+

constructor()

A no-argument constructor used to create a URL. It returns a **URL** object after **parseURL** is called. It is not used independently.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

#### \[h2\]parseURL9+

static parseURL(url: string, base?: string | URL): URL

Parses a URL.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | 
A string representing an absolute or a relative URL.

In the case of a relative URL, you must specify **base** to parse the final URL.

In the case of an absolute URL, the passed **base** will be ignored.

 |
| base | string | URL | No | 

Either a string or an object. The default value is **undefined**.

\- **string**: string. If the first parameter is a relative URL, the parameter must comply with the URL standard.

\- **URL**: URL object.

\- This parameter is used when **url** is a relative URL.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [URL](#url) | **URL** object created. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/qyFFX5mVQ7yfG6bmPxn9wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDD04EB82073B1DA523FE7DE6B09487D320A411F9CF01CFEB74455BC82676002)

If **url** is a relative URL, the URL parsed by calling this API is not merely a concatenation of **url** and **base**. When **url** is a relative path, it is parsed relative to the current directory of the passed **base**, taking into account all path segments before the last slash in the path of **base**, but excluding the following part (see example url1). When **url** points to a root directory, it is parsed relative to the origin of **base** (see example url2).

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200002 | Invalid url string. |

**Example**

let mm = 'https://username:password@host:8080/test/test1/test3';
let urlObject = url.URL.parseURL(mm);
let result = urlObject.toString(); // Output 'https://username:password@host:8080/test/test1/test3'
// If url is a relative path, the path in the base parameter is test/test1, and the path of the parsed URL is /test/path2/path3.
let url1 = url.URL.parseURL('path2/path3', 'https://www.example.com/test/test1'); // Output 'https://www.example.com/test/path2/path3'
// If url is a root directory, the path in the base parameter is /test/test1/test3, and the path of the parsed URL is /path1/path2.
let url2 = url.URL.parseURL('/path1/path2', urlObject); // Output 'https://username:password@host:8080/path1/path2'
url.URL.parseURL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output 'https://www.exampleUrl/path/path1'
url.URL.parseURL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
url.URL.parseURL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
url.URL.parseURL('https://www.example.com', ); // Output 'https://www.example.com/'
url.URL.parseURL('https://www.example.com', urlObject); // Output 'https://www.example.com/'

#### \[h2\]toString

toString(): string

Converts the parsed URL into a string.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Target string. |

**Example**

const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = urlObject.toString(); // Output 'https://username:password@host:8080/directory/file?query=pppppp#qwer=da'

#### \[h2\]toJSON

toJSON(): string

Converts the parsed URL into a JSON string.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | JSON string. |

**Example**

const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = urlObject.toJSON();

#### URLSearchParams(deprecated)

Defines APIs for handling URL query strings. This class is deprecated since API version 9. You are advised to use [URLParams](#urlparams9) instead.

#### \[h2\]constructor(deprecated)

constructor(init?: string\[\]\[\] | Record<string, string> | string | URLSearchParams)

A constructor used to create a **URLSearchParams** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/X_t-BnFNRwikjBaszslW4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BD0C05E486CFC01968CC94FD958BCFC6FC037AB25DA0C0612E02ACC40B3EA36)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.constructor9+](#constructor9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| init | string\[\]\[\] | Record<string, string> | string | URLSearchParams | No | 
Input parameter objects, which include the following:

\- **string\[\]\[\]**: two-dimensional string array.

\- **Record<string, string>**: list of objects.

\- **string**: string.

\- **URLSearchParams**: object.

The default value is **undefined**.

 |

**Example**

let objectParams = new url.URLSearchParams(\[ \['user1', 'abc1'\], \['query2', 'first2'\], \['query3', 'second3'\] \]);
let objectParams1 = new url.URLSearchParams({"fod" : '1' , "bard" : '2'});
let objectParams2 = new url.URLSearchParams('?fod=1&bard=2');
let urlObject = new url.URL('https://developer.mozilla.org/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search);

#### \[h2\]append(deprecated)

append(name: string, value: string): void

Appends a key-value pair into the query string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/pLKu80vSTBuYRkPUaw29qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60E1A98C79572E1EEA97F3794B688EB74ABC5EDCB8F2CDCB9CC1C6A6D75B72E6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.append9+](#append9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the key-value pair to append. |
| value | string | Yes | Value of the key-value pair to append. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.append('fod', '3');

#### \[h2\]delete(deprecated)

delete(name: string): void

Deletes key-value pairs of the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/W_2MGt7PSwiXNZmO6QdyLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9A2F461609951AAB7F5F634C363502DC35F17A65902EE63D6012A99F01BB7AC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.delete9+](#delete9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the key-value pairs to delete. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.delete('fod');

#### \[h2\]getAll(deprecated)

getAll(name: string): string\[\]

Obtains all the key-value pairs based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/aeDv7dYpTn-DXPGly6MK8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA94DFEA8EC3851BDA764E5AFE305C812694E5BE1CC7098160DDBC19DDFAFA72)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.getAll9+](#getall9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | All key-value pairs matching the specified key. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search.slice(1));
params.append('fod', '3'); // Add a second value for the fod parameter.
console.info(params.getAll('fod').toString()) // Output \["1","3"\].

#### \[h2\]entries(deprecated)

entries(): IterableIterator<\[string, string\]>

Obtains an ES6 iterator. Each item of the iterator is an array, and the first and second fields of each array are the key and value respectively.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/JRlYEN54TIugupFInaSHwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DB59E909788AA49AE0F2C25B4E995F160AB3B6487B3038DC3E34C0554A8DBD)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.entries9+](#entries9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[string, string\]> | ES6 iterator. |

**Example**

let searchParamsObject = new url.URLSearchParams("keyName1=valueName1&keyName2=valueName2");
let iter = searchParamsObject.entries();
for (let pair of iter) {
  console.info(pair\[0\]+ ', '+ pair\[1\]);
}
// keyName1, valueName1
// keyName2, valueName2

#### \[h2\]forEach(deprecated)

forEach(callbackFn: (value: string, key: string, searchParams: URLSearchParams) => void, thisArg?: Object): void

Traverses the key-value pairs in the **URLSearchParams** instance by using a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/16WUp4jHSSaBgGLD60FpnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DB0CD69B5588DF1A407D7E580DCB2CD3DA4D528C58E9A7358DCC89C8436902E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.forEach9+](#foreach9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the key-value pairs in the **URLSearchParams** instance. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this object. |

**Table 1** callbackFn parameter description

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Value that is currently traversed. |
| key | string | Yes | Key that is currently traversed. |
| searchParams | [URLSearchParams](#urlsearchparamsdeprecated) | Yes | Instance that invokes the **forEach** method. |

**Example**

const myURLObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
myURLObject.searchParams.forEach((value, name, searchParams) => {
    console.info(name, value, myURLObject.searchParams === searchParams);
});

#### \[h2\]get(deprecated)

get(name: string): string | null

Obtains the value of the first key-value pair based on the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/frftHo-0Rea88Hfsq3TIWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E37324EB4103C38AC07FE65AAA7806E9C1F5D223EE24AA47C31D4A00FCB87BCB)

If the key-value pair does not exist, **undefined** is returned.

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.get9+](#get9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key specified to obtain the value. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | null | The first value is returned. If no value is found, **null** is returned. |

**Example**

let paramsObject = new url.URLSearchParams('name=Jonathan&age=18');
let name = paramsObject.get("name"); // is the string "Jonathan"
let age = paramsObject.get("age"); // is the string '18'
let getObj = paramsObject.get("abc"); // undefined

#### \[h2\]has(deprecated)

has(name: string): boolean

Checks whether a key has a value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/jdJQkcnVTEyuUPBFSlZYdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8EFFA1F888B9C1D2632E4C485021D220EF6AB21AC053F490DFAE88A9F05A3E9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.has9+](#has9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key specified to search for its value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the key has a value; otherwise, **false** is returned. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.has('bard') === true;

#### \[h2\]set(deprecated)

set(name: string, value: string): void

Sets the value for a key. If key-value pairs matching the specified key exist, the value of the first key-value pair will be set to the specified value and other key-value pairs will be deleted. Otherwise, the key-value pair will be appended to the query string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xiZcW6KQSlatrm5efmbfKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A2E3813D8C525FBE7938862E29AC7C52C6F317BA9469CD55A58BFB5C45627D0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.set9+](#set9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the value to set. |
| value | string | Yes | Value to set. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.set('baz', '3'); // Add a third parameter.

#### \[h2\]sort(deprecated)

sort(): void

Sorts all key-value pairs contained in this object based on the Unicode code points of the keys and returns undefined. This method uses a stable sorting algorithm, that is, the relative order between key-value pairs with equal keys is retained.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/fTzqIpiWThO2L3JMAhKhRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=124497456B53D3D7D77BAE849D52B7030CCAC5CC0559A81061DF38BA0269B412)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.sort9+](#sort9) instead.

**System capability**: SystemCapability.Utils.Lang

**Example**

let searchParamsObject = new url.URLSearchParams("c=3&a=9&b=4&d=2"); // Create a test URLSearchParams object
searchParamsObject.sort(); // Sort the key/value pairs
console.info(searchParamsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2

#### \[h2\]keys(deprecated)

keys(): IterableIterator<string>

Obtains an ES6 iterator that contains the keys of all the key-value pairs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/92jfZMBfQpi-pOTwp1xwvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55E35EA5BEF5A0588B12D5B5A2524B50E455FE0812158340029A61B7497E8532)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.keys9+](#keys9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<string> | ES6 iterator that contains the keys of all the key-value pairs. |

**Example**

let searchParamsObject = new url.URLSearchParams("key1=value1&key2=value2");
let keys = searchParamsObject.keys();
for (let key of keys) {
  console.info(key);
}
// key1
// key2

#### \[h2\]values(deprecated)

values(): IterableIterator<string>

Obtains an ES6 iterator that contains the values of all the key-value pairs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/_tFdYjrjQHWz4dfnt_h04g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94E7A59127E277E0F282E8E786B0D98794F71817C87C53619A6BF6D8C8680D1C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.values9+](#values9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<string> | ES6 iterator that contains the values of all the key-value pairs. |

**Example**

let searchParams = new url.URLSearchParams("key1=value1&key2=value2");
let values = searchParams.values();
for (let value of values) {
  console.info(value);
}
// value1
// value2

#### \[h2\]\[Symbol.iterator\](deprecated)

\[Symbol.iterator\](): IterableIterator<\[string, string\]>

Obtains an ES6 iterator. Each item of the iterator is an array, and the first and second fields of each array are the key and value respectively.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/A_r6I7FBTSWCxC_eqHRHSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F33FF549F618773540A774CF83A6FA2EDB01AE3F19F80C0C87E8E7B5B3D0505C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.\[Symbol.iterator\]9+](#symboliterator9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[string, string\]> | ES6 iterator. |

**Example**

const paramsObject = new url.URLSearchParams('fod=bay&edg=bap');
let pairs = paramsObject\[Symbol.iterator\]();
for (let pair of pairs) {
  console.info(pair\[0\] + ', ' + pair\[1\]);
}
// fod, bay
// edg, bap

#### \[h2\]toString(deprecated)

toString(): string

Obtains search parameters that are serialized as a string and, if necessary, percent-encodes the characters in the string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/z5Suki9PQou8fGU3IMC6wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9858F3CFFA980375FD932B88B951BB6C6372F58A0EAFAC9CFFA023F7BB20571B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [URLParams.toString9+](#tostring9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String of serialized search parameters, which is percent-encoded if necessary. |

**Example**

let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search.slice(1));
params.append('fod', '3');
console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
