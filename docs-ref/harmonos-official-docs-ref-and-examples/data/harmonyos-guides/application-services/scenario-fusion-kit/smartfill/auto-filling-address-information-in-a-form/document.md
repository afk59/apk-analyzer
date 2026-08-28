# Auto-filling Address Information in a Form

If your app has an address filling form that uses the local address selector, you need to develop the fields in the form by yourself.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/9PbbarTlR8m1N262NHJubQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98F6C1A8E44EFC0581612CFF171D99E127FDA6DF5089A88CC54968654510C064)

-   Configure the approximate location permission [ohos.permission.APPROXIMATELY\_LOCATION](../../../../system/security/application-access-control/application-permission-management/application-permissions/open-user-grant-permissions/document.md#ohospermissionapproximately_location) in the **module.json5** file.
-   Enable [Map Kit](../../../map-kit/preparations/document.md#section16133115441516) for the local address selector.
-   Configure the [signing information and fingerprint](../../../account-kit/getting-started/configuring-signing-information-and-fingerprint/document.md).

#### Display Effect

Detailed address information in the address form can be automatically filled based on the local region. If the filled address information is incorrect, users can use the address selector to change it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jL3qdCPxRD2J0eCp_ooPpg/en-us_image_0000002503572061.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8501C15574B1528491BD18A38C32DD45B15E9967DE84DB409B0449AC48C059FE "Click to enlarge")

#### Sample Code

import { util } from '@kit.ArkTS';
import { i18n } from '@kit.LocalizationKit';
import { sceneMap, site } from '@kit.MapKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';
import { abilityAccessCtrl, autoFillManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
import { TextInputModifier } from '@kit.ArkUI';

const AUTHED = 0;
const TIME\_OUT = 100;
// Default longitude and latitude. The following uses the longitude and latitude of Tiananmen Square in Beijing as an example.
const INIT\_LAT = 39.5;
const INIT\_LON = 116.2;
const ENGLISH = 'en';
const SIMPLIFIED\_CHINESE = 'zh\_CN';
const PERMISSIONS: Array<Permissions> = \['ohos.permission.APPROXIMATELY\_LOCATION'\];
const ADMINISTRATIVE\_REGION: Array<string> =
  \['countryName', 'adminLevel1', 'adminLevel2', 'adminLevel3', 'adminLevel4'\];

interface PersonInfo {
  name?: string;
  phone?: string;
  email?: string;
  idCard?: string;
  region?: string;
  streetAddress?: string;
}

interface RequestParam {
  requestTag: string;
  requestText: string;
}

interface Location {
  latitude: number;
  longitude: number;
}

// Display the authorization pop-up.
async function reqPermissionsFromUser(permissions: Array<Permissions>,
  context: common.UIAbilityContext): Promise<PermissionRequestResult> {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  return await atManager.requestPermissionsFromUser(context, permissions);
}

// Throttle function.
function debounce(func: () => void, wait: number = TIME\_OUT): Function {
  let timeout: number | null = null;
  return () => {
    timeout && clearTimeout(timeout);
    timeout = setTimeout(() => {
      func();
      clearTimeout(timeout);
    }, wait);
  };
}

@Extend(Text)
function textStyle() {
  .width(64)
  .textAlign(TextAlign.End)
}

@Entry
@Component
struct Index {
  @State personInfo: PersonInfo = {};
  @State isClicked: boolean = false;
  // Whether the user has activated information input.
  private isUserInput: boolean = false;
  private location: Location = {
    latitude: INIT\_LAT,
    longitude: INIT\_LON,
  };
  private currentRequestTag: string = '';
  private handleAddressChange = (request: RequestParam) => {
    return debounce(async () => {
      this.autoCompleteAddress(request);
    });
  };

  aboutToAppear() {
    reqPermissionsFromUser(PERMISSIONS, this.getUIContext().getHostContext() as common.UIAbilityContext)
      .then((permissionRequestResult: PermissionRequestResult) => {
        if (permissionRequestResult.authResults\[0\] === AUTHED) {
          // The API for obtaining location information can be called only after authorization.
          geoLocationManager.getCurrentLocation((err, location: geoLocationManager.Location) => {
            if (err) {
              hilog.error(0x0000, 'testTag', \`Failed to get location, code: ${err?.code}, message: ${err?.message}\`);
              return;
            }
            hilog.info(0x0000, 'testTag', \`Succeeded in obtaining the current location of the user\`);
            this.location.latitude = location.latitude;
            this.location.longitude = location.longitude;
          })
        }
      })
      .catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed request permissions, code: ${err?.code}, message: ${err?.message}\`);
      })
  }

  public isUsLanguage(): boolean {
    let result: string = '';
    try {
      result = i18n.System.getSystemLanguage();
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'Failed to get system language');
    }
    return result.toLowerCase() === 'en-latn-us';
  }

  async autoCompleteAddress(request: RequestParam): Promise<void> {
    try {
      let params: site.SearchByTextParams = {
        query: request.requestText,
        // Longitude and latitude to which search suggestions need to be biased.
        location: {
          latitude: this.location.latitude,
          longitude: this.location.longitude
        },
        language: this.isUsLanguage() ? ENGLISH : SIMPLIFIED\_CHINESE,
        isChildren: true
      };
      const result = await site.searchByText(params);
      if (result.sites) {
        let region: string = '';
        let addressComponent = result.sites\[0\].addressComponent;
        // Traverse the administrative region levels of the current address.
        for (let item of ADMINISTRATIVE\_REGION) {
          if (addressComponent\[item\] === undefined) {
            break;
          }
          region += addressComponent\[item\];
        }
        // Prevent repeated searches that may lead to inconsistent results.
        if (request.requestTag === this.currentRequestTag) {
          this.personInfo.region = region;
        }
      }
    } catch (error) {
      hilog.error(0x0000, 'testTag', \`Failed to search location, code: ${error.code}, message: ${error.message}\`);
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in searching location');
  }

  onRegionClick(): void {
    // After an administrative region is selected, only the search results within the administrative region are displayed to prevent long query time.
    this.currentRequestTag = util.generateRandomUUID();
    let districtSelectOptions: sceneMap.DistrictSelectOptions = {
      countryCode: 'CN',
    };
    sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
      hilog.info(0x0000, 'testTag', 'SelectDistrict', 'Succeeded  in selecting district.');
      let region = '';
      for (let i = 0; i < data?.districts?.length; i++) {
        region += data.districts\[i\].name;
      }
      this.personInfo.region = region;
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', \`Failed to select district, code: ${err.code}, message: ${err.message}\`);
    });
  }

  searchRegionByAddress(val: string): void {
    let tag: string = util.generateRandomUUID();
    this.currentRequestTag = tag;
    let param: RequestParam = {
      requestTag: tag,
      requestText: val
    }
    // In the user manual input scenario, jitter handling needs to be implemented. For automatic filling of SmartFill, query is performed directly.
    if (this.personInfo.region && this.personInfo.region !== '') {
      return;
    }
    if (this.isUserInput) {
      this.handleAddressChange(param)();
    } else {
      this.autoCompleteAddress(param);
    }
  }

  build() {
    Column({ space: 8 }) {
      Row({ space: 8 }) {
        Text('Name').textStyle()
        TextInput({ text: this.personInfo.name, placeholder: 'Name' })
          .layoutWeight(1)
          .contentType(ContentType.PERSON\_FULL\_NAME)
          .onChange((val: string) => {
            this.personInfo.name = val;
          })
      }

      Row({ space: 8 }) {
        Text('Phone').textStyle()
        TextInput({ text: this.personInfo.phone, placeholder: 'Mobile number' })
          .layoutWeight(1)
          .contentType(ContentType.PHONE\_NUMBER)
          .onChange((val: string) => {
            this.personInfo.phone = val;
          })
      }

      Row({ space: 8 }) {
        Text('ID No.').textStyle()
        TextInput({ text: this.personInfo.idCard, placeholder: 'ID card information' })
          .layoutWeight(1)
          .contentType(ContentType.ID\_CARD\_NUMBER)
          .onChange((val: string) => {
            this.personInfo.idCard = val;
          })
      }

      Row({ space: 8 }) {
        Text('E-mail').textStyle()
        TextInput({ text: this.personInfo.email, placeholder: 'Email information' })
          .layoutWeight(1)
          .contentType(ContentType.EMAIL\_ADDRESS)
          .onChange((val: string) => {
            this.personInfo.email = val;
          })
      }

      Row({ space: 8 }) {
        Text('Region').textStyle()
        FunctionalInput({
          params: {
            // **InputType.SELECT\_DISTRICT** indicates the province/city/district selector input type.
            inputType: functionalInputComponentManager.InputType.SELECT\_DISTRICT,
            textInputValue: {
              text: this.personInfo.region,
              placeholder: 'Province, city, district, street',
            },
            // Adjust the TextInput style.
            inputAttributeModifier: new TextInputModifier()
              .backgroundColor(Color.Transparent)
              .onChange((value) => {
                if (value !== this.personInfo.region) {
                  this.personInfo.region = value;
                }
              })
          },
          // When **InputType** is set to **SELECT\_DISTRICT**, the callback must be **onSelectDistrict**.
          controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
            data: functionalInputComponentManager.DistrictSelectResult) => {
            if (err) {
              // Error processing.
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // Success processing.
            hilog.info(0x0000, "testTag", "succeeded in selecting district");
            this.personInfo.region = data.inputContent;
          })
        })
      }

      Row({ space: 8 }) {
        Text('Detailed address').textStyle()
        TextInput({ text: this.personInfo.streetAddress, placeholder: 'Street address' })
          .layoutWeight(1)
          .contentType(ContentType.DETAIL\_INFO\_WITHOUT\_STREET)
          .onDidInsert(() => {
            // Triggered when a user enters information using the input method.
            this.isUserInput = true;
          })
          .onDidDelete((val: DeleteValue) => {
            // Triggered when a user deletes information using the input method.
            if (val?.deleteValue?.length > 0) {
              this.isUserInput = true;
            }
          })
          .onChange((val: string) => {
            this.personInfo.streetAddress = val;
            if (val && val.trim().length > 0) {
              this.searchRegionByAddress(val);
            } else {
              this.currentRequestTag = util.generateRandomUUID();
              this.personInfo.region = '';
            }
            this.isUserInput = false;
          })
      }

      Button('Save')
        .width('50%')
        .onClick(() => {
          if (!this.isClicked) {
            this.isClicked = true;
            autoFillManager.requestAutoSave(this.getUIContext(), {
              onSuccess: () => {
                hilog.info(0x0000, 'testTag', 'Succeeded in saving request');
              },
              onFailure: () => {
                hilog.info(0x0000, 'testTag', 'Failed to save request');
              }
            });
            setTimeout(() => {
              this.isClicked = false;
            }, 2000);
          }
        })
    }
    .padding({ left: 16, right: 16 })
    .backgroundColor($r('sys.color.ohos\_id\_color\_list\_card\_bg'))
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/T_Ey6kt1S52Fn0Y4MJS7sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A890A89DA4423C122AA15B03162AE47498D8D1217E5173A5B28EDAA282AA60A)

In this example, the scenario-specific input component is used as the local address selector, which supports address filling based on SmartFill.
