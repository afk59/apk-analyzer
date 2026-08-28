# About This Kit

Reader Kit provides you with the capabilities to parse, typeset, and interact with eBooks in various formats. You can quickly build book reading capabilities by leveraging the Reader Kit's features and components.

#### Capabilities

Reader Kit provides the following capabilities:

-   Parsing for a wide range of book formats, such as TXT, EPUB, MOBI, AZW, and AZW3, enabling the extraction of book information including the book title, author, cover, catalog item list, and body content.
-   Pagination for standard TXT and rich text content (HTML+CSS), employing simulated and swipe page-turning techniques, along with pagination snapshots and detailed pagination information.
-   Reading page component (**ReadPageComponent**), which supports the display of book content, offers a variety of page-turning interactions and animations, and provides the progress and behavior perception capabilities required by the reader during the page-turning process.

#### Highlights

-   Support parsing of various eBook formats and provides standardized book information and content data.
-   Ensure W3C-compliant typesetting for rich text (HTML+CSS), with optimized algorithms to increase typesetting speed and efficiency.
-   Support not only system fonts but also extended custom fonts, catering to users' personalized preferences.
-   Provide the reading page component (**ReadPageComponent**) that offers comprehensive reading interaction capabilities, supports multiple page-turning modes, and utilizes OpenGL (C/C++) to render page-turning animations, delivering a more seamless and smoother reading experience.

#### Basic Concepts

-   ReadPageComponent
    
    Reading page component encapsulated in Reader Kit. It supports the display of book content, offers a variety of page-turning interactions and animations, and provides the progress and behavior perception capabilities required by the reader during the page-turning process. For details, please refer to [ReadPageComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-api-readpagecomponent) (ets).
    
-   BookParser
    
    eBook parsing engine, which provides parsing capabilities for eBooks in TXT, EPUB, MOBI, AZW, and AZW3 formats. For details, please refer to [bookParser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-book-parser).
    
-   Spine
    
    Spine of a book, which connects the front and back covers of a paperback or hardcover. It usually has key information such as the book title, author's name, and publisher's name printed on it. In Reader Kit, the spine defines the reading sequence of book content. Each [SpineItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-book-parser#section1029864651619) indicates a readable content node, identifying a readable content resource.
    

#### Constraints

-   Reader Kit can process only books stored as local files and does not support online file streams. Each book file must be stored in a distinct directory of the app sandbox.
-   Reader Kit does not offer DRM protection during book processing.
-   Only book files in TXT, EPUB, MOBI, AZW, and AZW3 formats can be parsed. Parsing books in non-standard formats may throw exceptions. You need to capture and process these errors.
-   The typesetting engine and interaction functionalities must be used together with Reader Kit's reading page component **ReadPageComponent**.

## Device Restrictions

Reader Kit applies only to phones, PCs/2-in-1 devices, and tablets running HarmonyOS NEXT 5.0.4 or later. **It is not supported on emulators** currently.

## Supported Countries/Regions

Currently, Reader Kit is available only in the Chinese mainland.

#### Sample Code

This guide provides only code snippets. For the complete sample code, please refer to [CodeLabs](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-ReaderKit) or [Sample Code](https://gitcode.com/HarmonyOS_Samples/readerkit_samplecode_arkts). The complete code provides practice examples for scenarios such as importing local books, building a reader, creating a directory list, and modifying reading settings, helping you better use Reader Kit APIs.
