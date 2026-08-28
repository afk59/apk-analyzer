# udmf\_meta.h

#### Overview

Declares the unified data types.

**File to include**: <database/udmf/udmf\_meta.h>

**Library**: libudmf.so

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Since**: 12

**Related module**: [UDMF](../../modules/udmf/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| UDMF\_META\_ENTITY "general.entity" | 
Generic type that represents all physical storage types. It is used to define physical properties of a type.

This type is uncategorized.

**Since**: 12

 |
| UDMF\_META\_OBJECT "general.object" | 

Generic type that represents all logical content types. It is used to define physical properties of a type.

This type is uncategorized.

**Since**: 12

 |
| UDMF\_META\_COMPOSITE\_OBJECT "general.composite-object" | 

Generic composite content type. For example, a PDF file that contains text and image.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_TEXT "general.text" | 

Generic text type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_PLAIN\_TEXT "general.plain-text" | 

Text without specific encoding or identifier.

This type belongs to **TEXT**.

**Since**: 12

 |
| UDMF\_META\_HTML "general.html" | 

HTML.

This type belongs to **TEXT**.

**Since**: 12

 |
| UDMF\_META\_HYPERLINK "general.hyperlink" | 

Hyperlink.

This type belongs to **TEXT**.

**Since**: 12

 |
| UDMF\_META\_XML "general.xml" | 

XML.

This type belongs to **TEXT**.

**Since**: 12

 |
| UDMF\_META\_SOURCE\_CODE "general.source-code" | 

Generic source code type.

This type belongs to **PLAIN\_TEXT**.

**Since**: 12

 |
| UDMF\_META\_SCRIPT "general.script" | 

Source code in any scripting language.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_SHELL\_SCRIPT "general.shell-script" | 

Shell script.

This type belongs to **SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_CSH\_SCRIPT "general.csh-script" | 

C shell script.

This type belongs to **SHELL\_SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_PERL\_SCRIPT "general.perl-script" | 

Perl script.

This type belongs to **SHELL\_SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_PHP\_SCRIPT "general.php-script" | 

PHP script.

This type belongs to **SHELL\_SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_PYTHON\_SCRIPT "general.python-script" | 

Python script.

This type belongs to **SHELL\_SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_RUBY\_SCRIPT "general.ruby-script" | 

Ruby script.

This type belongs to **SHELL\_SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_TYPE\_SCRIPT "general.type-script" | 

TypeScript source code.

This type belongs to **SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_JAVA\_SCRIPT "general.java-script" | 

JavaScript source code.

This type belongs to **SCRIPT**.

**Since**: 12

 |
| UDMF\_META\_C\_HEADER "general.c-header" | 

Header file in C.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_C\_SOURCE "general.c-source" | 

Source code in C.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_C\_PLUS\_PLUS\_HEADER "general.c-plus-plus-header" | 

Header file in C++.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_C\_PLUS\_PLUS\_SOURCE "general.c-plus-plus-source" | 

Source code in C++.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_JAVA\_SOURCE "general.java-source" | 

Source code in Java.

This type belongs to **SOURCE\_CODE**.

**Since**: 12

 |
| UDMF\_META\_EBOOK "general.ebook" | 

Generic eBook file format type.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_EPUB "general.epub" | 

Electronic publication (EPUB).

This type belongs to **EBOOK**.

**Since**: 12

 |
| UDMF\_META\_AZW "com.amazon.azw" | 

AZW.

This type belongs to **EBOOK**.

**Since**: 12

 |
| UDMF\_META\_AZW3 "com.amazon.azw3" | 

AZW3.

This type belongs to **EBOOK**.

**Since**: 12

 |
| UDMF\_META\_KFX "com.amazon.kfx" | 

KFX.

This type belongs to **EBOOK**.

**Since**: 12

 |
| UDMF\_META\_MOBI "com.amazon.mobi" | 

MOBI.

This type belongs to **EBOOK**.

**Since**: 12

 |
| UDMF\_META\_MEDIA "general.media" | 

Generic media type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_IMAGE "general.image" | 

Image.

This type belongs to **MEDIA**.

**Since**: 12

 |
| UDMF\_META\_JPEG "general.jpeg" | 

JPEG.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_PNG "general.png" | 

PNG.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_RAW\_IMAGE "general.raw-image" | 

Raw image.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_TIFF "general.tiff" | 

TIFF.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_BMP "com.microsoft.bmp" | 

BMP.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_ICO "com.microsoft.ico" | 

Windows icon.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_PHOTOSHOP\_IMAGE "com.adobe.photoshop-image" | 

Adobe Photoshop image.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_AI\_IMAGE "com.adobe.illustrator.ai-image" | 

Adobe Illustrator image (.ai).

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_WORD\_DOC "com.microsoft.word.doc" | 

Microsoft Word.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_EXCEL "com.microsoft.excel.xls" | 

Microsoft Excel.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_PPT "com.microsoft.powerpoint.ppt" | 

Microsoft PowerPoint presentation format.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_PDF "com.adobe.pdf" | 

PDF.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_POSTSCRIPT "com.adobe.postscript" | 

PostScript.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_ENCAPSULATED\_POSTSCRIPT "com.adobe.encapsulated-postscript" | 

Encapsulated PostScript.

This type belongs to **POSTSCRIPT**.

**Since**: 12

 |
| UDMF\_META\_VIDEO "general.video" | 

Base video type.

This type belongs to **MEDIA**.

**Since**: 12

 |
| UDMF\_META\_AVI "general.avi" | 

AVI.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_MPEG "general.mpeg" | 

MPEG-1 or MPEG-2.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_MPEG4 "general.mpeg-4" | 

MPEG-4.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_VIDEO\_3GPP "general.3gpp" | 

3GP (3GPP file format).

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_VIDEO\_3GPP2 "general.3gpp2" | 

3G2 (3GPP2 file format).

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WM "com.microsoft.windows-media-wm" | 

Windows WM format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMV "com.microsoft.windows-media-wmv" | 

Windows WMV format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMP "com.microsoft.windows-media-wmp" | 

Windows WMP format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_AUDIO "general.audio" | 

Generic audio type.

This type belongs to **MEDIA**.

**Since**: 12

 |
| UDMF\_META\_AAC "general.aac" | 

AAC.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_AIFF "general.aiff" | 

AIFF.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_ALAC "general.alac" | 

ALAC.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_FLAC "general.flac" | 

FLAC.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_MP3 "general.mp3" | 

MP3.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_OGG "general.ogg" | 

OGG.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_PCM "general.pcm" | 

PCM.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMA "com.microsoft.windows-media-wma" | 

Windows WMA format.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_WAVEFORM\_AUDIO "com.microsoft.waveform-audio" | 

Windows Waveform.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMX "com.microsoft.windows-media-wmx" | 

Windows WMX format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WVX "com.microsoft.windows-media-wvx" | 

Windows WVX format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_WINDOWS\_MEDIA\_WAX "com.microsoft.windows-media-wax" | 

Windows WAX format.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_GENERAL\_FILE "general.file" | 

Generic file type.

This type belongs to **ENTITY**.

**Since**: 12

 |
| UDMF\_META\_DIRECTORY "general.directory" | 

Generic directory type.

This type belongs to **ENTITY**.

**Since**: 12

 |
| UDMF\_META\_FOLDER "general.folder" | 

Generic folder type.

This type belongs to **DIRECTORY**.

**Since**: 12

 |
| UDMF\_META\_SYMLINK "general.symlink" | 

Generic symbolic type.

This type belongs to **ENTITY**.

**Since**: 12

 |
| UDMF\_META\_ARCHIVE "general.archive" | 

Generic archive file type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_BZ2\_ARCHIVE "general.bz2-archive" | 

BZ2.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_DISK\_IMAGE "general.disk-image" | 

Generic type of any file that can be mounted as a volume.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_TAR\_ARCHIVE "general.tar-archive" | 

TAR.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_ZIP\_ARCHIVE "general.zip-archive" | 

ZIP.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_JAVA\_ARCHIVE "com.sun.java-archive" | 

JAR (Java archive).

This type belongs to **ARCHIVE** and **EXECUTABLE**.

**Since**: 12

 |
| UDMF\_META\_GNU\_TAR\_ARCHIVE "org.gnu.gnu-tar-archive" | 

GUN archive.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_GNU\_ZIP\_ARCHIVE "org.gnu.gnu-zip-archive" | 

GZIP archive.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_GNU\_ZIP\_TAR\_ARCHIVE "org.gnu.gnu-zip-tar-archive" | 

GZIP TAR.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_CALENDAR "general.calendar" | 

Generic calendar type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_CONTACT "general.contact" | 

Generic contact type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_DATABASE "general.database" | 

Generic database file type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_MESSAGE "general.message" | 

Generic message type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_VCARD "general.vcard" | 

Generic electronic business card type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_NAVIGATION "general.navigation" | 

Generic navigation data type.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_LOCATION "general.location" | 

Location data.

This type belongs to **NAVIGATION**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_FORM "openharmony.form" | 

Widget defined for the system.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_APP\_ITEM "openharmony.app-item" | 

Home screen icon defined for the system.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_PIXEL\_MAP "openharmony.pixel-map" | 

Pixel map defined for the system.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_ATOMIC\_SERVICE "openharmony.atomic-service" | 

Atomic service type defined for the system.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_PACKAGE "openharmony.package" | 

Package (compressed folder) defined for the system.

This type belongs to **DIRECTORY**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_HAP "openharmony.hap" | 

Ability package defined for the system.

This type belongs to **OPENHARMONY\_PACKAGE**.

**Since**: 12

 |
| UDMF\_META\_SMIL "com.real.smil" | 

Synchronized Multimedia Integration Language (SMIL).

This type belongs to **XML**.

**Since**: 12

 |
| UDMF\_META\_MARKDOWN "general.markdown" | 

Markdown.

This type belongs to **PLAIN\_TEXT**.

**Since**: 12

 |
| UDMF\_META\_FAX "general.fax" | 

Generic type of the fax.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_JFX\_FAX "com.j2.jfx-fax" | 

J2 jConnect fax file format.

This type belongs to **FAX**.

**Since**: 12

 |
| UDMF\_META\_EFX\_FAX "com.js.efx-fax" | 

EFX file format.

This type belongs to **FAX**.

**Since**: 12

 |
| UDMF\_META\_XBITMAP\_IMAGE "general.xbitmap-image" | 

X BitMAP (XBM) used in the X Window system (X11).

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_TGA\_IMAGE "com.truevision.tga-image" | 

Tagged Graphics (TGA) format.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_SGI\_IMAGE "com.sgi.sgi-image" | 

Silicon Graphics image (SGI) format.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_OPENEXR\_IMAGE "com.ilm.openexr-image" | 

OpenXR image format.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_FLASHPIX\_IMAGE "com.kodak.flashpix.image" | 

FlashPix image format.

This type belongs to **IMAGE**.

**Since**: 12

 |
| UDMF\_META\_REALMEDIA "com.real.realmedia" | 

RealMedia format.

This type belongs to **VIDEO**.

**Since**: 12

 |
| UDMF\_META\_AU\_AUDIO "general.au-audio" | 

AU format.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_AIFC\_AUDIO "general.aifc-audio" | 

AIFC.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_SD2\_AUDIO "com.digidesign.sd2-audio" | 

Digidesign Sound Designer II (SDII).

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_REALAUDIO "com.real.realaudio" | 

RealAudio.

This type belongs to **AUDIO**.

**Since**: 12

 |
| UDMF\_META\_OPENXML "org.openxmlformats.openxml" | 

OpenXML base type.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_WORDPROCESSINGML\_DOCUMENT "org.openxmlformats.wordprocessingml.document" | 

WordProcessingML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_SPREADSHEETML\_SHEET "org.openxmlformats.spreadsheetml.sheet" | 

SpreadsheetML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_PRESENTATIONML\_PRESENTATION "org.openxmlformats.presentationml.presentation" | 

PresentationML format.

This type belongs to **OPENXML** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT "org.oasis.opendocument" | 

OpenDocument format for Office applications.

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT\_TEXT "org.oasis.opendocument.text" | 

OpenDocument format for word processing (text) documents.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT\_SPREADSHEET "org.oasis.opendocument.spreadsheet" | 

OpenDocument format for spreadsheets.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT\_PRESENTATION "org.oasis.opendocument.presentation" | 

OpenDocument format for presentations.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT\_GRAPHICS "org.oasis.opendocument.graphics" | 

OpenDocument format for graphics.

This type belongs to **OPENDOCUMENT** and **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENDOCUMENT\_FORMULA "org.oasis.opendocument.formula" | 

OpenDocument format for formula.

This type belongs to **OPENDOCUMENT**.

**Since**: 12

 |
| UDMF\_META\_STUFFIT\_ARCHIVE "com.allume.stuffit-archive" | 

Stuffit compression format (stuffit archive).

This type belongs to **ARCHIVE**.

**Since**: 12

 |
| UDMF\_META\_VCS "general.vcs" | 

VCalendar (VCS) format.

This type belongs to **CALENDAR** and **TEXT**.

**Since**: 12

 |
| UDMF\_META\_ICS "general.ics" | 

Internet Calendaring and Scheduling (ICS) format.

This type belongs to **CALENDAR** and **TEXT**.

**Since**: 12

 |
| UDMF\_META\_EXECUTABLE "general.executable" | 

Generic type of all executable files.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_PORTABLE\_EXECUTABLE "com.microsoft.portable-executable" | 

Microsoft Windows portable executable format.

This type belongs to **EXECUTABLE**.

**Since**: 12

 |
| UDMF\_META\_SUN\_JAVA\_CLASS "com.sun.java-class" | 

Java class file format.

This type belongs to **EXECUTABLE**.

**Since**: 12

 |
| UDMF\_META\_FONT "general.font" | 

Basic type of fonts.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_TRUETYPE\_FONT "general.truetype-font" | 

TrueType font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_TRUETYPE\_COLLECTION\_FONT "general.truetype-collection-font" | 

TrueType Collection font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_OPENTYPE\_FONT "general.opentype-font" | 

OpenType font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_POSTSCRIPT\_FONT "com.adobe.postscript-font" | 

PostScript font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_POSTSCRIPT\_PFB\_FONT "com.adobe.postscript-pfb-font" | 

PostScript Font Binary font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_POSTSCRIPT\_PFA\_FONT "com.adobe.postscript-pfa-font" | 

Adobe Type 1 font format.

This type belongs to **FONT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_HDOC "openharmony.hdoc" | 

Memo format defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_HINOTE "HarmonyOS.hinote" | 

Note format defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

 |
| UDMF\_META\_OPENHARMONY\_STYLED\_STRING "openharmony.styled-string" | 

Style string type defined for the system.

This type belongs to **COMPOSITE\_OBJECT**.

**Since**: 12

 |
| UDMF\_META\_OPENHARMONY\_WANT "openharmony.want" | 

Want defined for the system.

This type belongs to **OBJECT**.

**Since**: 12

 |
| UDMF\_META\_GENERAL\_FILE\_URI "general.file-uri" | 

File address type.

This type belongs to **TEXT**.

**Since**: 13

 |
| UDMF\_METE\_GENERAL\_CONTENT\_FORM "general.content-form" | 

Content card type.

This type belongs to **OBJECT**.

**Since**: 14

 |
