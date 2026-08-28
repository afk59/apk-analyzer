# List of Previewer-Capable APIs

#### Components

## ArkTS Components

| 
Component

 | 

API

 |
| :-- | :-- |
| 

Basic components

 | 

AlphabetIndexer

 |
| 

Blank

 |
| 

Button

 |
| 

Checkbox

 |
| 

CheckboxGroup

 |
| 

DataPanel

 |
| 

DatePicker

 |
| 

Divider

 |
| 

Gauge

 |
| 

Image

 |
| 

ImageAnimator

 |
| 

ImageSpan

 |
| 

LoadingProgress

 |
| 

Marquee

 |
| 

Menu

 |
| 

MenuItem

 |
| 

MenuItemGroup

 |
| 

Navigation

 |
| 

NavRouter

 |
| 

NavDestination

 |
| 

PatternLock

 |
| 

Progress

 |
| 

QRCode

 |
| 

Radio

 |
| 

Rating

 |
| 

ScrollBar

 |
| 

Search

 |
| 

Select

 |
| 

Slider

 |
| 

Span

 |
| 

Stepper

 |
| 

StepperItem

 |
| 

Text

 |
| 

TextArea

 |
| 

TextClock

 |
| 

TextInput

 |
| 

TextPicker

 |
| 

TextTimer

 |
| 

Toggle

 |
| 

Container components

 | 

Badge

 |
| 

Column

 |
| 

ColumnSplit

 |
| 

Counter

 |
| 

Flex

 |
| 

FlowItem

 |
| 

GridCol

 |
| 

GridRow

 |
| 

List

 |
| 

ListItem

 |
| 

ListItemGroup

 |
| 

Navigator

 |
| 

Panel

 |
| 

Refresh

 |
| 

RelativeContainer

 |
| 

Row

 |
| 

RowSplit

 |
| 

Scroll

 |
| 

SideBarContainer

 |
| 

Stack

 |
| 

Swiper

 |
| 

Tabs

 |
| 

TabContent

 |
| 

WaterFlow

 |
| 

Drawing components

 | 

Circle

 |
| 

Ellipse

 |
| 

Line

 |
| 

Polyline

 |
| 

Path

 |
| 

Rect

 |
| 

Shape

 |
| 

Canvas components

 | 

Canvas

 |
| 

CanvasGradient

 |
| 

CanvasPattern

 |
| 

CanvasRenderingContext2D

 |
| 

ImageBitmap

 |
| 

ImageData

 |
| 

Matrix2D

 |
| 

OffscreenCanvasRenderingContext2D

 |
| 

Path2D

 |

## JS Components

| 
Component

 | 

API

 |
| :-- | :-- |
| 

Basic components

 | 

button

 |
| 

chart

 |
| 

divider

 |
| 

image

 |
| 

image-animator

 |
| 

input

 |
| 

label

 |
| 

marquee

 |
| 

menu

 |
| 

option

 |
| 

picker

 |
| 

picker-view

 |
| 

piece

 |
| 

progress

 |
| 

qrcode

 |
| 

rating

 |
| 

search

 |
| 

select

 |
| 

slider

 |
| 

span

 |
| 

switch

 |
| 

text

 |
| 

textarea

 |
| 

toolbar

 |
| 

toolbar-item

 |
| 

toggle

 |
| 

Container components

 | 

badge

 |
| 

dialog

 |
| 

div

 |
| 

form

 |
| 

list

 |
| 

list-item

 |
| 

list-item-group

 |
| 

panel

 |
| 

popup

 |
| 

refresh

 |
| 

stack

 |
| 

stepper

 |
| 

stepper-item

 |
| 

swiper

 |
| 

tabs

 |
| 

tab-bar

 |
| 

tab-content

 |
| 

Canvas components

 | 

canvas

 |
| 

CanvasRenderingContext2D

 |
| 

Image

 |
| 

CanvasGradient

 |
| 

ImageData

 |
| 

Path2D

 |
| 

ImageBitmap

 |
| 

OffscreenCanvas

 |
| 

OffscreenCanvasRenderingContext2D

 |
| 

Grid components

 | 

grid-container

 |
| 

grid-row

 |
| 

grid-col

 |
| 

SVG components

 | 

svg

 |
| 

rect

 |
| 

circle

 |
| 

ellipse

 |
| 

path

 |
| 

line

 |
| 

polyline

 |
| 

polygon

 |
| 

text

 |
| 

tspan

 |
| 

textPath

 |
| 

animate

 |
| 

animateMotion

 |
| 

animateTransform

 |

#### APIs

## UI

| 
Module

 | 

API

 |
| :-- | :-- |
| 

@ohos.animator (Animation)

 | 

Animator

 |
| 

AnimatorResult

 |
| 

AnimatorOptions

 |
| 

@ohos.mediaquery (Media Query)

 | 

matchMediaSync

 |
| 

MediaQueryResult

 |
| 

MediaQueryListener

 |
| 

@ohos.promptAction (Dialog Box)

 | 

showToast

 |
| 

showDialog

 |
| 

showActionMenu

 |
| 

ShowToastOptions

 |
| 

Button

 |
| 

ShowDialogSuccessResponse

 |
| 

ShowDialogOptions

 |
| 

ActionMenuSuccessResponse

 |
| 

ActionMenuOptions

 |
| 

@ohos.router (Page Routing)

 | 

pushUrl

 |
| 

replaceUrl

 |
| 

back

 |
| 

clear

 |
| 

getLength

 |
| 

getState

 |
| 

enableAlertBeforeBackPage

 |
| 

disableAlertBeforeBackPage

 |
| 

getParams

 |
| 

RouterMode

 |
| 

RouterOptions

 |
| 

RouterState

 |
| 

EnableAlertOptions

 |

## Network Management

| 
Module

 | 

API

 |
| :-- | :-- |
| 

@ohos.net.http (Data Request)

 | 

http.createHttp

If HTTP requests require proxy configuration to access, the Previewer in API version 12 or later supports the use of the system's **http\_proxy**, **https\_proxy**, and **no\_proxy** environment variables.

 |

## Data Management

| 
Module

 | 

API

 |
| :-- | :-- |
| 

@ohos.data.preferences (User Preferences)

 | 

data\_preferences.getPreferences

 |
| 

data\_preferences.deletePreferences

 |
| 

data\_preferences.removePreferencesFromCache

 |
| 

Preferences

 |
| 

ValueType

 |

## File Management

Since DevEco Studio 6.0.0 Beta5, the file management APIs are available only during the preview or debug preview of HAPs/HSPs in the stage model. The **Enable file operation** option must be enabled first.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/uVZOWB78Qpq-a1rcSq-DZg/en-us_image_0000002532750511.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F345ABB53A0AED1F961F138A1E3FE2FF3BA1CC390EAB10C23362E8A7062246B "Click to enlarge")

| 
Module

 | 

API

 |
| :-- | :-- |
| 

@ohos.file.fs (File Management)

 | 

fs.open

 |
| 

fs.close

 |
| 

fs.fdatasync

 |
| 

fs.fsync

 |
| 

fs.read

 |
| 

fs.write

 |
| 

fs.mkdir

 |
| 

fs.mkdtemp

 |
| 

fs.rename

 |
| 

fs.rmdir

 |
| 

fs.unlink

 |
| 

fs.stat

 |
| 

fs.truncate

 |
