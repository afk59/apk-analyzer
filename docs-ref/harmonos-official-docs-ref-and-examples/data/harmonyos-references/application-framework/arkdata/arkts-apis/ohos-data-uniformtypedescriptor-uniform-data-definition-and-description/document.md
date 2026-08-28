# @ohos.data.uniformTypeDescriptor (Uniform Data Definition and Description)

The **uniformTypeDescriptor** module abstracts and defines uniform data types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dZyk0XxGTO-gN4O1I3g2AQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA02C220D532FF02B0AE62D2A187987E62CB470DA6DC1DBC954B9936B4F1F4E6)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { uniformTypeDescriptor } from '@kit.ArkData';

#### UniformDataType

Enumerates the uniform data types. Some data types are related. For example, the JPEG type belongs to the IMAGE type. For more preset data types, see [Preset UTD List](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-list).

The following table lists the common uniform data types.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ENTITY11+ | 'general.entity' | 
Generic physical storage type.

This type is uncategorized.

 |
| OBJECT11+ | 'general.object' | 

Generic logical content type.

This type is uncategorized.

 |
| COMPOSITE\_OBJECT11+ | 'general.composite-object' | 

Generic composite content type. For example, a PDF file that contains text and image.

This type belongs to **OBJECT**.

 |
| TEXT | 'general.text' | 

Generic text type.

This type belongs to **OBJECT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PLAIN\_TEXT | 'general.plain-text' | 

Text without specific encoding or identifier.

This type belongs to **TEXT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HTML | 'general.html' | 

HTML.

This type belongs to **TEXT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HYPERLINK | 'general.hyperlink' | 

Hyperlink.

This type belongs to **TEXT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| XML11+ | 'general.xml' | 

XML.

This type belongs to **TEXT**.

 |
| XHTML12+ | 'general.xhtml' | 

XHTML.

This type belongs to **XML**.

 |
| RSS12+ | 'general.rss' | 

RSS.

This type belongs to **XML**.

 |
| SMIL12+ | 'com.real.smil' | 

Synchronized Multimedia Integration Language (SMIL).

This type belongs to **XML**.

 |
| SOURCE\_CODE11+ | 'general.source-code' | 

Generic source code type.

This type belongs to **TEXT**.

 |
| SCRIPT11+ | 'general.script' | 

Source code in any scripting language.

This type belongs to **SOURCE\_CODE**.

 |
| SHELL\_SCRIPT11+ | 'general.shell-script' | 

Shell script.

This type belongs to **SCRIPT**.

 |
| CSH\_SCRIPT11+ | 'general.csh-script' | 

C shell script.

This type belongs to **SHELL\_SCRIPT**.

 |
| PERL\_SCRIPT11+ | 'general.perl-script' | 

Perl script.

This type belongs to **SHELL\_SCRIPT**.

 |
| PHP\_SCRIPT11+ | 'general.php-script' | 

PHP script.

This type belongs to **SHELL\_SCRIPT**.

 |
| PYTHON\_SCRIPT11+ | 'general.python-script' | 

Python script.

This type belongs to **SHELL\_SCRIPT**.

 |
| RUBY\_SCRIPT11+ | 'general.ruby-script' | 

Ruby script.

This type belongs to **SHELL\_SCRIPT**.

 |
| TYPE\_SCRIPT11+ | 'general.type-script' | 

TypeScript source code.

This type belongs to **SOURCE\_CODE**.

 |
| JAVA\_SCRIPT11+ | 'general.java-script' | 

JavaScript source code.

This type belongs to **SOURCE\_CODE**.

 |
| CSS12+ | 'general.css' | 

CSS.

This type belongs to **SCRIPT**.

 |
| C\_HEADER11+ | 'general.c-header' | 

Header file in C.

This type belongs to **SOURCE\_CODE**.

 |
| C\_SOURCE11+ | 'general.c-source' | 

Source code in C.

This type belongs to **SOURCE\_CODE**.

 |
| C\_PLUS\_PLUS\_HEADER11+ | 'general.c-plus-plus-header' | 

Header file in C++.

This type belongs to **SOURCE\_CODE**.

 |
| C\_PLUS\_PLUS\_SOURCE11+ | 'general.c-plus-plus-source' | 

Source code in C++.

This type belongs to **SOURCE\_CODE**.

 |
| JAVA\_SOURCE11+ | 'general.java-source' | 

Source code in Java.

This type belongs to **SOURCE\_CODE**.

 |
| TEX12+ | 'general.tex' | 

Source code in TEX format.

This type belongs to **SOURCE\_CODE**.

 |
| MARKDOWN12+ | 'general.markdown' | 

Markdown.

This type belongs to **TEXT**.

 |
| ASC\_TEXT12+ | 'general.asc-text' | 

ASCII.

This type belongs to **TEXT**.

 |
| RICH\_TEXT12+ | 'general.rich-text' | 

Rich text.

This type belongs to **TEXT**.

 |
| DELIMITED\_VALUES\_TEXT12+ | 'general.delimited-values-text' | 

Generic type of all delimited value texts.

This type belongs to **TEXT**.

 |
| COMMA\_SEPARATED\_VALUES\_TEXT12+ | 'general.comma-separated-values-text' | 

Comma-separated values (CSV).

This type belongs to **DELIMITED\_VALUES\_TEXT**.

 |
| TAB\_SEPARATED\_VALUES\_TEXT12+ | 'general.tab-separated-values-text' | 

Tab-separated values (TSV).

This type belongs to **DELIMITED\_VALUES\_TEXT**.

 |
| EBOOK11+ | 'general.ebook' | 

Generic eBook file format type.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| EPUB11+ | 'general.epub' | 

Electronic publication (EPUB).

This type belongs to **EBOOK**.

 |
| AZW11+ | 'com.amazon.azw' | 

AZW.

This type belongs to **EBOOK**.

 |
| AZW311+ | 'com.amazon.azw3' | 

AZW3.

This type belongs to **EBOOK**.

 |
| KFX11+ | 'com.amazon.kfx' | 

KFX.

This type belongs to **EBOOK**.

 |
| MOBI11+ | 'com.amazon.mobi' | 

MOBI.

This type belongs to **EBOOK**.

 |
| MEDIA11+ | 'general.media' | 

Generic media type.

This type belongs to **OBJECT**.

 |
| IMAGE | 'general.image' | 

Image.

This type belongs to **MEDIA**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| JPEG11+ | 'general.jpeg' | 

JPEG.

This type belongs to **IMAGE**.

 |
| PNG11+ | 'general.png' | 

PNG.

This type belongs to **IMAGE**.

 |
| RAW\_IMAGE11+ | 'general.raw-image' | 

Raw image.

This type belongs to **IMAGE**.

 |
| TIFF11+ | 'general.tiff' | 

TIFF.

This type belongs to **IMAGE**.

 |
| BMP11+ | 'com.microsoft.bmp' | 

BMP.

This type belongs to **IMAGE**.

 |
| ICO11+ | 'com.microsoft.ico' | 

Windows icon.

This type belongs to **IMAGE**.

 |
| PHOTOSHOP\_IMAGE11+ | 'com.adobe.photoshop-image' | 

Adobe Photoshop image.

This type belongs to **IMAGE**.

 |
| AI\_IMAGE11+ | 'com.adobe.illustrator.ai-image' | 

Adobe Illustrator image (.ai).

This type belongs to **IMAGE**.

 |
| FAX12+ | 'general.fax' | 

Generic type of the fax.

This type belongs to **IMAGE**.

 |
| JFX\_FAX12+ | 'com.j2.jfx-fax' | 

J2 jConnect fax file format.

This type belongs to **FAX**.

 |
| EFX\_FAX12+ | 'com.js.efx-fax' | 

EFX file format.

This type belongs to **FAX**.

 |
| XBITMAP\_IMAGE12+ | 'general.xbitmap-image' | 

X BitMAP (XBM) used in the X Window system (X11).

This type belongs to **IMAGE**.

 |
| GIF12+ | 'general.gif' | 

GIF.

This type belongs to **IMAGE**.

 |
| TGA\_IMAGE12+ | 'com.truevision.tga-image' | 

Tagged Graphics (TGA) format.

This type belongs to **IMAGE**.

 |
| SGI\_IMAGE12+ | 'com.sgi.sgi-image' | 

Silicon Graphics image (SGI) format.

This type belongs to **IMAGE**.

 |
| OPENEXR\_IMAGE12+ | 'com.ilm.openexr-image' | 

OpenXR image format.

This type belongs to **IMAGE**.

 |
| FLASHPIX\_IMAGE12+ | 'com.kodak.flashpix.image' | 

FlashPix image format.

This type belongs to **IMAGE**.

 |
| WORD\_DOC11+ | 'com.microsoft.word.doc' | 

Microsoft Word.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| EXCEL11+ | 'com.microsoft.excel.xls' | 

Microsoft Excel.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| PPT11+ | 'com.microsoft.powerpoint.ppt' | 

Microsoft PowerPoint presentation format.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| WORD\_DOT12+ | 'com.microsoft.word.dot' | 

Microsoft Word template.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| POWERPOINT\_PPS12+ | 'com.microsoft.powerpoint.pps' | 

Microsoft PowerPoint slide show format.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| POWERPOINT\_POT12+ | 'com.microsoft.powerpoint.pot' | 

Microsoft PowerPoint template.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| EXCEL\_XLT12+ | 'com.microsoft.excel.xlt' | 

Microsoft Excel template.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| VISIO\_VSD12+ | 'com.microsoft.visio.vsd' | 

Microsoft Visio.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| PDF11+ | 'com.adobe.pdf' | 

PDF.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| POSTSCRIPT11+ | 'com.adobe.postscript' | 

PostScript.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| ENCAPSULATED\_POSTSCRIPT11+ | 'com.adobe.encapsulated-postscript' | 

Encapsulated PostScript.

This type belongs to **POSTSCRIPT**.

 |
| VIDEO | 'general.video' | 

Generic video type.

This type belongs to **MEDIA**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AVI11+ | 'general.avi' | 

AVI.

This type belongs to **VIDEO**.

 |
| MPEG11+ | 'general.mpeg' | 

MPEG-1 or MPEG-2.

This type belongs to **VIDEO**.

 |
| MPEG411+ | 'general.mpeg-4' | 

MPEG-4.

This type belongs to **VIDEO**.

 |
| VIDEO\_3GPP11+ | 'general.3gpp' | 

3GP (3GPP file format).

This type belongs to **VIDEO**.

 |
| VIDEO\_3GPP211+ | 'general.3gpp2' | 

3G2 (3GPP2 file format).

This type belongs to **VIDEO**.

 |
| TS12+ | 'general.ts' | 

MPEG-TS.

This type belongs to **VIDEO**.

 |
| MPEGURL\_VIDEO12+ | 'general.mpegurl-video' | 

MPEG video playlist format.

This type belongs to **VIDEO**.

 |
| WINDOWS\_MEDIA\_WM11+ | 'com.microsoft.windows-media-wm' | 

Windows WM format.

This type belongs to **VIDEO**.

 |
| WINDOWS\_MEDIA\_WMV11+ | 'com.microsoft.windows-media-wmv' | 

Windows WMV format.

This type belongs to **VIDEO**.

 |
| WINDOWS\_MEDIA\_WMP11+ | 'com.microsoft.windows-media-wmp' | 

Windows WMP format.

This type belongs to **VIDEO**.

 |
| WINDOWS\_MEDIA\_WVX11+ | 'com.microsoft.windows-media-wvx' | 

Windows WVX format.

This type belongs to **VIDEO**.

 |
| WINDOWS\_MEDIA\_WMX11+ | 'com.microsoft.windows-media-wmx' | 

Windows WMX format.

This type belongs to **VIDEO**.

 |
| REALMEDIA12+ | 'com.real.realmedia' | 

RealMedia format.

This type belongs to **VIDEO**.

 |
| MATROSKA\_VIDEO12+ | 'org.matroska.mkv' | 

MKV.

This type belongs to **VIDEO**.

 |
| FLASH12+ | 'com.adobe.flash' | 

Flash.

This type belongs to **VIDEO**.

 |
| AUDIO | 'general.audio' | 

Generic audio type.

This type belongs to **MEDIA**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AAC11+ | 'general.aac' | 

AAC.

This type belongs to **AUDIO**.

 |
| AIFF11+ | 'general.aiff' | 

AIFF.

This type belongs to **AUDIO**.

 |
| ALAC11+ | 'general.alac' | 

ALAC.

This type belongs to **AUDIO**.

 |
| FLAC11+ | 'general.flac' | 

FLAC.

This type belongs to **AUDIO**.

 |
| MP311+ | 'general.mp3' | 

MP3.

This type belongs to **AUDIO**.

 |
| OGG11+ | 'general.ogg' | 

OGG.

This type belongs to **AUDIO**.

 |
| PCM11+ | 'general.pcm' | 

PCM.

This type belongs to **AUDIO**.

 |
| WINDOWS\_MEDIA\_WMA11+ | 'com.microsoft.windows-media-wma' | 

Windows WMA.

This type belongs to **AUDIO**.

 |
| WAVEFORM\_AUDIO11+ | 'com.microsoft.waveform-audio' | 

Windows Waveform.

This type belongs to **AUDIO**.

 |
| WINDOWS\_MEDIA\_WAX11+ | 'com.microsoft.windows-media-wax' | 

Windows WAX.

This type belongs to **AUDIO**.

 |
| AU\_AUDIO12+ | 'general.au-audio' | 

AU format.

This type belongs to **AUDIO**.

 |
| AIFC\_AUDIO12+ | 'general.aifc-audio' | 

AIFC.

This type belongs to **AUDIO**.

 |
| MPEGURL\_AUDIO12+ | 'general.mpegurl-audio' | 

MPEG audio playlist format.

This type belongs to **AUDIO**.

 |
| MPEG\_4\_AUDIO12+ | 'general.mpeg-4-audio' | 

MPEG-4.

This type belongs to **AUDIO**.

 |
| MP212+ | 'general.mp2' | 

MP2.

This type belongs to **AUDIO**.

 |
| MPEG\_AUDIO12+ | 'general.mpeg-audio' | 

MPEG audio format.

This type belongs to **AUDIO**.

 |
| ULAW\_AUDIO12+ | 'general.ulaw-audio' | 

ULAW.

This type belongs to **AUDIO**.

 |
| SD2\_AUDIO12+ | 'com.digidesign.sd2-audio' | 

Digidesign Sound Designer II (SDII).

This type belongs to **AUDIO**.

 |
| REALAUDIO12+ | 'com.real.realaudio' | 

RealAudio.

This type belongs to **AUDIO**.

 |
| MATROSKA\_AUDIO12+ | 'org.matroska.mka' | 

MKA.

This type belongs to **AUDIO**.

 |
| FILE | 'general.file' | 

Generic file type.

This type belongs to **ENTITY**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DIRECTORY11+ | 'general.directory' | 

Generic directory type.

This type belongs to **ENTITY**.

 |
| FOLDER | 'general.folder' | 

Generic folder type.

This type belongs to **DIRECTORY**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SYMLINK11+ | 'general.symlink' | 

Generic symbolic type.

This type belongs to **ENTITY**.

 |
| ARCHIVE11+ | 'general.archive' | 

Generic archive file type.

This type belongs to **OBJECT**.

 |
| BZ2\_ARCHIVE11+ | 'general.bz2-archive' | 

BZ2.

This type belongs to **ARCHIVE**.

 |
| OPG12+ | 'general.opg' | 

OPG.

This type belongs to **ARCHIVE**.

 |
| TAZ\_ARCHIVE12+ | 'general.taz-archive' | 

TAR.

This type belongs to **TAR\_ARCHIVE**.

 |
| WEB\_ARCHIVE12+ | 'general.web-archive' | 

MHTML format for web page archiving.

This type belongs to **ARCHIVE**.

 |
| DISK\_IMAGE11+ | 'general.disk-image' | 

Generic type of any file that can be mounted as a volume.

This type belongs to **ARCHIVE**.

 |
| ISO12+ | 'general.iso' | 

ISO image (optical disk image) format.

This type belongs to **DISK\_IMAGE**.

 |
| TAR\_ARCHIVE11+ | 'general.tar-archive' | 

TAR.

This type belongs to ARCHIVE.

 |
| ZIP\_ARCHIVE11+ | 'general.zip-archive' | 

ZIP.

This type belongs to **ARCHIVE**.

 |
| JAVA\_ARCHIVE11+ | 'com.sun.java-archive' | 

JAR (Java archive).

This type belongs to **ARCHIVE** and **EXECUTABLE**.

 |
| GNU\_TAR\_ARCHIVE11+ | 'org.gnu.gnu-tar-archive' | 

GNU.

This type belongs to **ARCHIVE**.

 |
| GNU\_ZIP\_ARCHIVE11+ | 'org.gnu.gnu-zip-archive' | 

GZIP archive.

This type belongs to **ARCHIVE**.

 |
| GNU\_ZIP\_TAR\_ARCHIVE11+ | 'org.gnu.gnu-zip-tar-archive' | 

GZIP TAR.

This type belongs to **ARCHIVE**.

 |
| OPENXML12+ | 'org.openxmlformats.openxml' | 

OpenXML base type.

This type belongs to **ARCHIVE**.

 |
| WORDPROCESSINGML\_DOCUMENT12+ | 'org.openxmlformats.wordprocessingml.document' | 

WordProcessingML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| SPREADSHEETML\_SHEET12+ | 'org.openxmlformats.spreadsheetml.sheet' | 

SpreadsheetML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| PRESENTATIONML\_PRESENTATION12+ | 'org.openxmlformats.presentationml.presentation' | 

PresentationML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| DRAWINGML\_VISIO12+ | 'org.openxmlformats.drawingml.visio' | 

DrawingML file format of Office Open XML (OOXML).

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| DRAWINGML\_TEMPLATE12+ | 'org.openxmlformats.drawingml.template' | 

DrawingML template format of OOXML.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| WORDPROCESSINGML\_TEMPLATE12+ | 'org.openxmlformats.wordprocessingml.template' | 

WordProcessingML template format of OOXML.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| PRESENTATIONML\_TEMPLATE12+ | 'org.openxmlformats.presentationml.template' | 

PresentationML template format of OOXML.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| PRESENTATIONML\_SLIDESHOW12+ | 'org.openxmlformats.presentationml.slideshow' | 

PresentationML slide show format of OOXML.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| SPREADSHEETML\_TEMPLATE12+ | 'org.openxmlformats.spreadsheetml.template' | 

SpreadsheetML template format of OOXML.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

 |
| OPENDOCUMENT12+ | 'org.oasis.opendocument' | 

OpenDocument format for Office applications.

This type belongs to **ARCHIVE**.

 |
| OPENDOCUMENT\_TEXT12+ | 'org.oasis.opendocument.text' | 

OpenDocument format for word processing (text) documents.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

 |
| OPENDOCUMENT\_SPREADSHEET12+ | 'org.oasis.opendocument.spreadsheet' | 

OpenDocument format for spreadsheets.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

 |
| OPENDOCUMENT\_PRESENTATION12+ | 'org.oasis.opendocument.presentation' | 

OpenDocument format for presentations.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

 |
| OPENDOCUMENT\_GRAPHICS12+ | 'org.oasis.opendocument.graphics' | 

OpenDocument format for graphics.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

 |
| OPENDOCUMENT\_FORMULA12+ | 'org.oasis.opendocument.formula' | 

OpenDocument format for formula.

This type belongs to **OPENDOCUMENT**.

 |
| STUFFIT\_ARCHIVE12+ | 'com.allume.stuffit-archive' | 

Stuffit compression format (stuffit archive).

This type belongs to **ARCHIVE**.

 |
| RAR\_ARCHIVE12+ | 'com.rarlab.rar-archive' | 

WinRAR.

This type belongs to **ARCHIVE**.

 |
| SEVEN\_ZIP\_ARCHIVE12+ | 'org.7-zip.7-zip-archive' | 

7-Zip.

This type belongs to **ARCHIVE**.

 |
| CALENDAR11+ | 'general.calendar' | 

Generic calendar type.

This type belongs to **OBJECT**.

 |
| VCS12+ | 'general.vcs' | 

VCalendar (VCS) format.

This type belongs to **CALENDAR** and **TEXT**.

 |
| ICS12+ | 'general.ics' | 

Internet Calendaring and Scheduling (ICS) format.

This type belongs to **CALENDAR** and **TEXT**.

 |
| CONTACT11+ | 'general.contact' | 

Generic contact type.

This type belongs to **OBJECT**.

 |
| DATABASE11+ | 'general.database' | 

Generic database file type.

This type belongs to **OBJECT**.

 |
| MESSAGE11+ | 'general.message' | 

Generic message type.

This type belongs to **OBJECT**.

 |
| EXECUTABLE12+ | 'general.executable' | 

Generic type of all executable files.

This type belongs to **OBJECT**.

 |
| PORTABLE\_EXECUTABLE12+ | 'com.microsoft.portable-executable' | 

Microsoft Windows portable executable format.

This type belongs to **EXECUTABLE**.

 |
| SUN\_JAVA\_CLASS12+ | 'com.sun.java-class' | 

Java class file format.

This type belongs to **EXECUTABLE**.

 |
| VCARD11+ | 'general.vcard' | 

Generic electronic business card type.

This type belongs to **OBJECT**.

 |
| NAVIGATION11+ | 'general.navigation' | 

Generic navigation data type.

This type belongs to **OBJECT**.

 |
| LOCATION11+ | 'general.location' | 

Location data.

This type belongs to **NAVIGATION**.

 |
| FONT12+ | 'general.font' | 

Basic type of fonts.

This type belongs to **OBJECT**.

 |
| TRUETYPE\_FONT12+ | 'general.truetype-font' | 

TrueType font format.

This type belongs to **FONT**.

 |
| TRUETYPE\_COLLECTION\_FONT12+ | 'general.truetype-collection-font' | 

TrueType Collection font format.

This type belongs to **FONT**.

 |
| OPENTYPE\_FONT12+ | 'general.opentype-font' | 

OpenType font format.

This type belongs to **FONT**.

 |
| POSTSCRIPT\_FONT12+ | 'com.adobe.postscript-font' | 

PostScript font format.

This type belongs to **FONT**.

 |
| POSTSCRIPT\_PFB\_FONT12+ | 'com.adobe.postscript-pfb-font' | 

PostScript Font Binary font format.

This type belongs to **FONT**.

 |
| POSTSCRIPT\_PFA\_FONT12+ | 'com.adobe.postscript-pfa-font' | 

Adobe Type 1 font format.

This type belongs to **FONT**.

 |
| OPENHARMONY\_FORM | 'openharmony.form' | 

Widget defined for the system.

This type belongs to **OBJECT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| OPENHARMONY\_APP\_ITEM | 'openharmony.app-item' | 

Home screen icon defined for the system.

This type belongs to **OBJECT**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| OPENHARMONY\_PIXEL\_MAP | 'openharmony.pixel-map' | 

Pixel map defined for the system.

This type belongs to **IMAGE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| OPENHARMONY\_ATOMIC\_SERVICE11+ | 'openharmony.atomic-service' | 

Atomic service type defined for the system.

This type belongs to **OBJECT**.

 |
| OPENHARMONY\_PACKAGE11+ | 'openharmony.package' | 

Package (compressed folder) defined for the system.

This type belongs to **DIRECTORY**.

 |
| OPENHARMONY\_HAP11+ | 'openharmony.hap' | 

Ability package defined for the system.

This type belongs to **OPENHARMONY\_PACKAGE**.

 |
| OPENHARMONY\_HDOC12+ | 'openharmony.hdoc' | 

Memo format defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| OPENHARMONY\_HINOTE12+ | 'HarmonyOS.hinote' | 

Note format defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| OPENHARMONY\_STYLED\_STRING12+ | 'openharmony.styled-string' | 

Style string type defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| OPENHARMONY\_WANT12+ | 'openharmony.want' | 

Want defined for the system.

This type belongs to **OBJECT**.

 |
| OFD12+ | 'general.ofd' | 

Open Fixed-layout Document (OFD).

This type belongs to **COMPOSITE\_OBJECT**.

 |
| CAD12+ | 'general.cad' | 

Generic type of all computer-aided design types.

This type belongs to **OBJECT**.

 |
| OCTET\_STREAM12+ | 'general.octet-stream' | 

Any binary data type.

This type belongs to **OBJECT**.

 |
| FILE\_URI15+ | 'general.file-uri' | 

File address type.

This type belongs to **TEXT**.

 |
| CONTENT\_FORM15+ | 'general.content-form' | 

Content widget type.

This type belongs to **OBJECT**.

 |

#### TypeDescriptor11+

Represents a class for defining a uniform data type. It provides properties and methods for describing a uniform data type and its relationship with other uniform data types.

#### \[h2\]Properties

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| typeId11+ | string | No | No | ID of the uniform data type (that is, the enum value in [UTD list](#uniformdatatype)), or a custom UTD. |
| belongingToTypes11+ | Array<string> | No | No | Data types to which the uniform data type belongs. |
| description11+ | string | No | No | Brief description of the uniform data type. |
| referenceURL11+ | string | No | No | URL of the link to the reference (detailed information) of the uniform data type. |
| iconFile11+ | string | No | No | File path of the default icon for the uniform data type. An empty string means the uniform data type has no default icon. The application can determine whether to use the default icon. |
| filenameExtensions12+ | Array<string> | No | No | List of file name extensions associated with the uniform data type. |
| mimeTypes12+ | Array<string> | No | No | List of MIME types associated with the uniform data type. |

#### \[h2\]belongsTo11+

belongsTo(type: string): boolean

Checks whether this data type belongs to the specified uniform data type.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](#uniformdatatype). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data type belongs to or is the same as the specified uniform data type; returns **false** if they are not related. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.belongsTo('general.source-code');
    if(ret) {
        console.info('type general.type-script belongs to type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`belongsTo throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### \[h2\]isLowerLevelType11+

isLowerLevelType(type: string): boolean

Checks whether this data type is a lower-level type of the specified uniform data type. For example, **TYPE\_SCRIPT** is a lower-level type of **SOURCE\_CODE**, and **TYPE\_SCRIPT** and **SOURCE\_CODE** are lower-level types of **TEXT**.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](#uniformdatatype). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data type is a lower-level type of the specified uniform data type; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let ret = typeObj.isLowerLevelType('general.source-code');
    if(ret) {
        console.info('type general.type-script is lower level type of type general.source-code');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`isLowerLevelType throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### \[h2\]isHigherLevelType11+

isHigherLevelType(type: string): boolean

Checks whether this data type is a higher-level type of the specified uniform data type. For example, **SOURCE\_CODE** is a higher-level type of **TYPE\_SCRIPT**, and **TEXT** is a higher-level type of **SOURCE\_CODE** and **TYPE\_SCRIPT**.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Uniform data type specified, which is a value of [UniformDataType](#uniformdatatype). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data type is a higher-level type of the specified uniform data type; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.source-code');
    let ret = typeObj.isHigherLevelType('general.type-script');
    if(ret) {
        console.info('type general.source-code is higher level type of type general.type-script');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`isHigherLevelType throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### \[h2\]equals11+

equals(typeDescriptor: TypeDescriptor): boolean

Checks whether this data type is the same as the specified uniform data type. That is, compares **typeId**s of two [TypeDescriptor](#typedescriptor11) objects.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| typeDescriptor | [TypeDescriptor](#typedescriptor11) | Yes | Uniform data type to compare. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the type IDs are the same; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try{
    let typeA : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.type-script');
    let typeB : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('general.python-script');
    if(!typeA.equals(typeB)) {
      console.info('typeA is not equal to typeB');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### uniformTypeDescriptor.getTypeDescriptor11+

getTypeDescriptor(typeId: string): TypeDescriptor

Obtains the **TypeDescriptor** object based on the uniform data type ID.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| typeId | string | Yes | [Uniform data type ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors). |

**Return value**

| Type | Description |
| :-- | :-- |
| [TypeDescriptor](#typedescriptor11) | **TypeDescriptor** object obtained. If the uniform data type does not exist, **null** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeObj : uniformTypeDescriptor.TypeDescriptor = uniformTypeDescriptor.getTypeDescriptor('com.adobe.photoshop-image');
    if (typeObj) {
        let typeId = typeObj.typeId;
        let belongingToTypes = typeObj.belongingToTypes;
        let description = typeObj.description;
        let referenceURL = typeObj.referenceURL;
        let iconFile = typeObj.iconFile;
        let filenameExtensions = typeObj.filenameExtensions;
        let mimeTypes = typeObj.mimeTypes;
        console.info(\`typeId: ${typeId}, belongingToTypes: ${belongingToTypes}, description: ${description}, referenceURL: ${referenceURL}, iconFile: ${iconFile}, filenameExtensions: ${filenameExtensions}, mimeTypes: ${mimeTypes}\`);
    } else {
        console.info('type com.adobe.photoshop-image does not exist');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getTypeDescriptor throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### uniformTypeDescriptor.getUniformDataTypeByFilenameExtension11+

getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string

Obtains the uniform data type ID based on the given file name extension and data type. If there are multiple uniform data type IDs matching the conditions, the first one is returned.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filenameExtension | string | Yes | File name extension. |
| belongsTo | string | No | ID of the uniform data type, to which the data type to be obtained belongs. This parameter has no default value. If it is not specified, the [uniform data type ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors) is queried based on the file name extension. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the uniform data type that matches the specified file name extension and **belongsTo** (if specified). If no match is found, the data type dynamically generated based on the rules specified by the input parameters is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.ts', 'general.source-code');
    if(typeId) {
        console.info('typeId is general.type-script');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} \`);
}

// If no uniform data type ID is found based on ".myts" and "general.plain-text", the type generated based on the input parameters is returned.
try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.myts', 'general.plain-text');
    if(typeId) {
        console.info('typeId is flex.\*\*\*\*\*\*\*\*\*\*\*\*');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### uniformTypeDescriptor.getUniformDataTypeByMIMEType11+

getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string

Obtains the uniform data type ID based on the given MIME type and data type. If there are multiple uniform data type IDs matching the conditions, the first one is returned.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type. |
| belongsTo | string | No | ID of the uniform data type, to which the data type to be obtained belongs. This parameter has no default value. If it is not specified, the [uniform data type ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors) is queried based on the MIME name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the uniform data type that matches the specified MIME type and **belongsTo** (if specified). If no match is found, the data type dynamically generated based on the rules specified by the input parameters is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByMIMEType('image/jpeg', 'general.image');
    if(typeId) {
        console.info('typeId is general.jpeg');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypeByMIMEType throws an exception. code is ${error.code}, message is ${error.message} \`);
}

// If no uniform data type ID is found based on "image/myimage" and "general.image", the type generated based on the input parameters is returned.
try {
    let typeId = uniformTypeDescriptor.getUniformDataTypeByMIMEType('image/myimage', 'general.image');
    if(typeId) {
        console.info('typeId is flex.\*\*\*\*\*\*\*\*\*\*\*\*');
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypeByMIMEType throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### uniformTypeDescriptor.getUniformDataTypesByFilenameExtension13+

getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>

Obtains the uniform data type IDs based on the given file name extension and data type.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filenameExtension | string | Yes | File name extension. |
| belongsTo | string | No | ID of the uniform data type, to which the data type to be obtained belongs. This parameter has no default value. If it is not specified, the [uniform data type ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors) is queried based on the file name extension. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Uniform data type IDs that match the specified file name extension and **belongsTo** (if specified). If no match is found, the data types dynamically generated based on the rules specified by the input parameters are returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeIds = uniformTypeDescriptor.getUniformDataTypesByFilenameExtension('.ts', 'general.source-code');
    for (let typeId of typeIds) {
        console.info(\`typeId is ${typeId}\`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypesByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} \`);
}

// If no uniform data type ID is found based on ".myts" and "general.plain-text", the types generated based on the input parameters are returned.
try {
    let flexTypeIds = uniformTypeDescriptor.getUniformDataTypesByFilenameExtension('.myts', 'general.plain-text');
    for (let flexTypeId of flexTypeIds) {
        console.info(\`typeId is flex type, flex typeId is ${flexTypeId}\`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypesByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} \`);
}

#### uniformTypeDescriptor.getUniformDataTypesByMIMEType13+

getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string>

Obtains the uniform data type IDs based on the given MIME type and data type.

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type. |
| belongsTo | string | No | ID of the uniform data type, to which the data type to be obtained belongs. This parameter has no default value. If it is not specified, the [uniform data type ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors) is queried based on the MIME name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Uniform data type IDs that match the specified MIME type and **belongsTo** (if specified). If no match is found, the data types dynamically generated based on the rules specified by the input parameters are returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let typeIds = uniformTypeDescriptor.getUniformDataTypesByMIMEType('text/plain', 'general.text');
    for (let typeId of typeIds) {
        console.info(\`typeId is ${typeId}\`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypesByMIMEType throws an exception. code is ${error.code}, message is ${error.message} \`);
}

// If no uniform data type ID is found based on "image/myimage" and "general.image", the types generated based on the input parameters are returned.
try {
    let flexTypeIds = uniformTypeDescriptor.getUniformDataTypesByMIMEType('image/myimage', 'general.image');
    for (let flexTypeId of flexTypeIds) {
        console.info(\`typeId is flex type, flex typeId is ${flexTypeId}\`);
    }
} catch(e) {
    let error: BusinessError = e as BusinessError;
    console.error(\`getUniformDataTypesByMIMEType throws an exception. code is ${error.code}, message is ${error.message} \`);
}
