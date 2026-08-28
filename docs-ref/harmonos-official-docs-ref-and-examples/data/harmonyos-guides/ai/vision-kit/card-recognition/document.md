# Card Recognition

Since version 5.1.1(19), the **callback** parameter in the [CardRecognition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-card-recognition#section143611912403) API has been deprecated. Use the **onResult** parameter instead.

#### Use Cases

The card recognition control provides structured recognition services for ID cards, vehicle licenses, driver's licenses, passports, and bank cards. Currently, only second-generation ID cards in the Chinese mainland are supported, excluding bilingual text ID cards for ethnic minorities in China. The system can automatically determine the type of a card and return its structured information as well as image information.

In scenarios where the information about a certificate (such as an ID card or bank card) needs to be filled in, the card recognition control can be used to read the Optical Character Recognition (OCR) information and return the result. The front and back sides can be identified separately, or both sides can be identified at the same time.

**Figure 1** Example of bank card recognition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/8VKhNKFqR1GClqo3k-q92A/en-us_image_0000002271551973.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D27948B81ED51F49E1BFDA52DDDE127AE31A279DB1EB6F9926915031AEE109BF "Click to enlarge")

#### Restrictions

-   Supported languages: simplified Chinese and English
-   Currently, this capability supports only ID cards, vehicle licenses, driver's licenses, passports, and bank cards.
-   This control should not be blocked by another component or window.

#### API Description

The following lists only some main APIs called in the demo. For details about all APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-card-recognition).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[CardRecognition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-card-recognition#section143611912403)

 | 

Card recognition control.

 |
| 

[CardRecognitionResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-card-recognition#section161551745133610)

 | 

Card recognition result.

 |

#### Development Procedure

1.  Add classes related to the card recognition control to a project.
    
    import { CardRecognition, CardRecognitionResult, CardType, CardSide, CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from "@kit.VisionKit";
    
2.  Configure a UI layout, select the types and sides of cards to be recognized, set related parameters, and obtain return values through callbacks.
    
    The following is the sample code of ID cards, bank cards, passports, driver's licenses, and vehicle licenses.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'CardRecognition'
    
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          // ID card.
          CardRecognition({
            supportType: CardType.CARD\_ID,
            // Both sides of an ID card can be recognized.
            cardSide: CardSide.DEFAULT,
            cardRecognitionConfig: {
              defaultShootingMode: ShootingMode.MANUAL,
              isPhotoSelectionSupported: true
            },
            onResult: ((params: CardRecognitionResult) => {
              hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
              hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
              hilog.info(0x0001, TAG, \`params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}\`)
              hilog.info(0x0001, TAG, \`params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}\`)
            })
          })
        }
        .height('100%')
        .width('100%')
      }
    }
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'CardRecognition'
    
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          // Bank card.
          CardRecognition({
            supportType: CardType.CARD\_BANK,
            // One side of a bank card can be recognized.
            cardSide: CardSide.FRONT,
            cardRecognitionConfig: {
              defaultShootingMode: ShootingMode.MANUAL,
              isPhotoSelectionSupported: true,
              cardContentConfig: { bankCard: { isBankNumberDialogShown: true} }
            },
            onResult: ((params: CardRecognitionResult) => {
              hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
              hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
              hilog.info(0x0001, TAG, \`params cardInfo: ${JSON.stringify(params.cardInfo?.main)}\`)
            })})
        }
        .height('100%')
        .width('100%')
      }
    }
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'CardRecognition'
    
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          // Passport.
          CardRecognition({
            supportType: CardType.CARD\_PASSPORT,
            // One side of a passport can be recognized.
            cardSide: CardSide.FRONT,
            cardRecognitionConfig: {
              defaultShootingMode: ShootingMode.MANUAL,
              isPhotoSelectionSupported: true
            },
            onResult: ((params: CardRecognitionResult) => {
              hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
              hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
              hilog.info(0x0001, TAG, \`params cardInfo: ${JSON.stringify(params.cardInfo?.main)}\`)
            })})
        }
        .height('100%')
        .width('100%')
      }
    }
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'CardRecognition'
    
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          // Driver's license.
          CardRecognition({
            supportType: CardType.CARD\_DRIVER\_LICENSE,
            // Both sides of a driver's license can be recognized.
            cardSide: CardSide.DEFAULT,
            cardRecognitionConfig: {
              defaultShootingMode: ShootingMode.MANUAL,
              isPhotoSelectionSupported: true
            },
            onResult: ((params: CardRecognitionResult) => {
              hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
              hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
              hilog.info(0x0001, TAG, \`params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}\`)
              hilog.info(0x0001, TAG, \`params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}\`)
            })
          })
        }
        .height('100%')
        .width('100%')
      }
    }
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'CardRecognition'
    
    @Entry
    @Component
    struct Index {
      build() {
        Column() {
          // Vehicle license.
          CardRecognition({
            supportType: CardType.CARD\_VEHICLE\_LICENSE,
            // Both sides of a vehicle license can be recognized.
            cardSide: CardSide.DEFAULT,
            cardRecognitionConfig: {
              defaultShootingMode: ShootingMode.MANUAL,
              isPhotoSelectionSupported: true
            },
            onResult: ((params: CardRecognitionResult) => {
              hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
              hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
              hilog.info(0x0001, TAG, \`params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}\`)
              hilog.info(0x0001, TAG, \`params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}\`)
            })
          })
        }
        .height('100%')
        .width('100%')
      }
    }
    

#### Development Example

## Index.ets

// The development example of card recognition is implemented on two screens. One is the entry screen, and the other is the implementation screen.
// The entry screen needs to introduce the implementation screen. In the following example, the implementation screen file name is **CardDemoPage**.
import { CardDemoPage } from './CardDemoPage'

@Entry
@Component
struct MainPage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack()

  @Builder
  PageMap(name: string) {
    if (name === 'cardRecognition') {
      CardDemoPage()
    }
  }

  // Button on the card recognition entry screen.
  build() {
    Navigation(this.pathStack) {
      Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
        .width('50%')
        .height(40)
        .onClick(() => {
          this.pathStack.pushPath({ name: 'cardRecognition' })
        })
    }.title('Card recognition control demo').navDestination(this.PageMap)
    .mode(NavigationMode.Stack)
  }
}

## CardDemoPage.ets

// Card recognition implementation screen, and its file name is **CardDemoPage**. This screen needs to be introduced by the entry screen.
import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from "@kit.VisionKit"
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'CardRecognitionPage'

// Card recognition screen, which is used to load **uiExtensionAbility**.
@Component
export struct CardDemoPage {
  @State cardDataSource: Record<string, string>\[\] = \[\]
  @Consume('pathStack') pathStack: NavPathStack

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Top }) {
        Stack() {
          this.cardDataShowBuilder()
        }
        .width('80%')
        .height('80%')

        CardRecognition({
          // Here, the ID card type is used as an example.
          supportType: CardType.CARD\_ID,
          cardSide: CardSide.DEFAULT,
          cardRecognitionConfig: {
            defaultShootingMode: ShootingMode.MANUAL,
            isPhotoSelectionSupported: true
          },
          onResult: ((params: CardRecognitionResult) => {
            hilog.info(0x0001, TAG, \`params code: ${params.code}\`)
            if (params.code !== 200) {
              this.pathStack.pop()
            }
            hilog.info(0x0001, TAG, \`params cardType: ${params.cardType}\`)
            if (params.cardInfo?.front !== undefined) {
              this.cardDataSource.push(params.cardInfo?.front)
            }

            if (params.cardInfo?.back !== undefined) {
              this.cardDataSource.push(params.cardInfo?.back)
            }

            if (params.cardInfo?.main !== undefined) {
              this.cardDataSource.push(params.cardInfo?.main)
            }
            hilog.info(0x0001, TAG, \`params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}\`)
            hilog.info(0x0001, TAG, \`params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}\`)
          })
        })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .hideTitleBar(true)
  }

  @Builder
  cardDataShowBuilder() {
    List() {
      ForEach(this.cardDataSource, (cardData: Record<string, string>) => {
        ListItem() {
          Column() {
            Image(cardData.cardImageUri)
              .objectFit(ImageFit.Contain)
              .width(100)
              .height(100)

            Text(JSON.stringify(cardData))
              .width('100%')
              .fontSize(12)
          }
        }
      })
    }
    .listDirection(Axis.Vertical)
    .alignListItem(ListItemAlign.Center)
    .margin({
      top: 50
    })
    .width('100%')
    .height('100%')
  }
}
