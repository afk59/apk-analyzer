# @ohos.app.ability.InsightIntentDecorator (Intent Decorator)

The InsightIntentDecorator module provides several types of intent decorators for decorating classes or methods. You can [use these decorators to develop intents](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/insight-intent-decorator-development), define application functionalities as intents, and integrate them into AI entry points such as intelligent Q&A, intelligent search, and intelligent recommendation systems.

-   [@InsightIntentLink](#insightintentlink): decorates a URI in your application as an intent, enabling AI systems to quickly jump to your application via this intent. For details on the parameters supported by this decorator, see [LinkIntentDecoratorInfo](#linkintentdecoratorinfo).
-   [@InsightIntentPage](#insightintentpage): decorates a page in your application as an intent, enabling AI systems to swiftly navigate to that page. For details on the parameters supported by this decorator, see [PageIntentDecoratorInfo](#pageintentdecoratorinfo).
-   [@InsightIntentFunction](#insightintentfunction) and [@InsightIntentFunctionMethod](#insightintentfunctionmethod): The two decorators must be used together. [@InsightIntentFunction](#insightintentfunction) is used to decorate a class, and [@InsightIntentFunctionMethod](#insightintentfunctionmethod) is used to decorate a static function in that class. This setup defines the static function as an intent, enabling AI systems to execute it rapidly.
-   [@InsightIntentEntry](#insightintententry): decorates a class that inherits from [InsightIntentEntryExecutor](../ohos-app-ability-insightintententryexecutor-base-class-for-insightintententry-in/document.md) to implement intent operations and configure the ability on which the intent depends. This helps the AI entry point to easily invoke the associated ability and perform the intended action. For details on the parameters supported by this decorator, see [EntryIntentDecoratorInfo](#entryintentdecoratorinfo).
-   [@InsightIntentForm](#insightintentform): decorates a [FormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md) to specify the name of the widget bound to the FormExtensionAbility. This enables the AI entry point to add the widget via intent calls. For details on the parameters supported by this decorator, see [FormIntentDecoratorInfo](#formintentdecoratorinfo).
-   [@InsightIntentEntity](#insightintententity): decorates a class that inherits from [IntentEntity](../ohos-app-ability-insightintent-basic-definitions-of-insightintent-framework/document.md#intententity20) to define the class as an intent entity, which can pass parameters required for intent calls. For details on the parameters supported by this decorator, see [IntentEntityDecoratorInfo](#intententitydecoratorinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/YrtpiEmoRveT85h8ntaicg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BADD141970D3779149EBCCBE24F2248F371C015DF2F174AE233280166B5C6975)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Basic Concepts

Intents are divided into two types: standard intents and custom intents.

The system queries the standard intent list for a matching intent based on the **schema** and **intentVersion** fields in [IntentDecoratorInfo](#intentdecoratorinfo).

-   If a match is found, the intent is identified as a standard intent.
-   If no match is found, the intent is identified as a custom intent.

#### Modules to Import

import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry } from '@kit.AbilityKit';

#### @InsightIntentLink

Decorates a URI in the application as an intent, enabling AI systems to quickly jump to the application via this intent. For details on the parameters supported by this decorator, see [LinkIntentDecoratorInfo](#linkintentdecoratorinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/uXqTUrKtRbuQxKoH10TXTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C63EC35393CD649157042A836181FFFD5C852F8636DF4AE6691AA2B3AC2DB77)

The URI format must adhere to the requirements described in [Application Link Description](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-uri-config).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

Custom intent: The parameters of a custom intent must be passed in as a standard JSON schema data structure.

import { InsightIntentLink, LinkParamCategory } from '@kit.AbilityKit';

@InsightIntentLink({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: 'Play Music',
  displayDescription: 'Intent to play music',
  icon: $r('app.media.app\_icon'), // $r indicates a local icon, which must be defined in the resource catalog.
  llmDescription: 'Supports passing song names to play music',
  keywords: \['music playback', 'play music', 'PlayMusic'\],
  uri: 'https://www.example.com/music/',
  paramMappings: \[{
    paramName: 'songName',
    paramMappingName: 'music',
    paramCategory: LinkParamCategory.LINK
  }\],
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      }
    },
    'required': \['songName'\],
    'additionalProperties': false
  },
  result: {
    'type': 'object',
    'propertyNames': {
      'enum': \[
        'code',
        'result'
      \]
    },
    'required': \[
      'code',
      'result'
    \],
    'properties': {
      'code': {
        'description': 'Result code for job execution',
        'type': 'number'
      },
      'result': {}
    }
  }
})
export class ClassForLink {
  private \_playback: string = 'intention\_test';

  public set playback(value: string) {
    this.\_playback = value;
  }

  public get playback(): string {
    return this.\_playback;
  }

  constructor(playback: string) {
    this.\_playback = playback;
  }

  static Function1(playbackProgress: number, playback?: number): void {
    console.info(\`Function1, playbackProgress: ${playbackProgress}.\`);
  }
}

#### IntentDecoratorInfo

Common properties for intent decorators, used to define basic information about an intent (including the intent name and version number). It applies to all decorators provided by this module.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/HJVOq-oSTfGYB9m3Xqez5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22F3961715FFB0F014937D973C0D93E36EF0A204E29EC2DD2B4BE949F4B1BFE9)

If a matching intent is found in the standard intent list based on the **schema** and **intentVersion** fields, the system automatically populates the **intentName**, **domain**, **llmDescription**, **keywords**, **parameters**, and **result** fields with the values from the matching standard intent.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| intentName | string | No | No | Intent name, which is the unique identifier of an intent. |
| domain | string | No | No | Vertical domain of the intent. It is used to categorize intents by vertical fields (for example, video, music, and games). For details about the value range, see the vertical domain fields in [smart distribution features in different vertical domains](https://developer.huawei.com/consumer/en/doc/service/intents-ai-distribution-characteristic-0000001901922213#section2656133582215). |
| intentVersion | string | No | No | Version number of the intent. It is used to distinguish and manage intents when their capabilities evolve. |
| displayName | string | No | No | Name of the intent displayed to users. |
| displayDescription | string | No | Yes | Description of the intent displayed to users. |
| schema | string | No | Yes | Name of a standard intent schema. This field is required when you [access a standard intent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/insight-intent-definition#accessing-standard-intents). It is not required when you [create a custom intent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/insight-intent-definition#creating-custom-intents). For details about the standard intent list, see [Appendix: Standard Intent Access Specifications](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/insight-intent-access-specifications). |
| icon | ResourceStr | No | Yes | 
Icon of the intent. It is displayed in the AI entry point.

\- If the value is a string, the icon is read from a network resource.

\- If the value is a [resource](../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md), the icon is read from a local resource.

 |
| llmDescription | string | No | Yes | Function of an intent, which helps large language models understand the intent. |
| keywords | string\[\] | No | Yes | Search keywords for the intent. |
| parameters | Record<string, Object> | No | Yes | Data format of intent parameters, which is used to define the input data format during intent calls. |
| result | Record<string, Object> | No | Yes | Data format for the results returned by intent calls. It defines how the data should be structured. |

#### LinkIntentDecoratorInfo

**LinkIntentDecoratorInfo** inherits from [IntentDecoratorInfo](#intentdecoratorinfo) and describes the parameters supported by the [@InsightIntentLink](#insightintentlink) decorator, such as the URI information required for application redirection.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI information associated with the intent. |
| paramMappings | [LinkIntentParamMapping](#linkintentparammapping)\[\] | No | Yes | Mapping between intent parameters and URI information. |

#### LinkIntentParamMapping

**LinkIntentParamMapping** defines the mapping between intent parameters and URI information for the [@InsightIntentLink](#insightintentlink) decorator.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| paramName | string | No | No | Name of the intent parameter. |
| paramMappingName | string | No | Yes | Mapping name of the intent parameter. |
| paramCategory | [LinkParamCategory](#linkparamcategory) | No | Yes | 
Category of the intent parameter.

If an intent parameter is of the [LINK](#linkparamcategory) category, the system retrieves **paramMappingName** corresponding to **paramName** and appends it to the URI as a key-value pair (where **key** is the value of **paramMappingName**, and **value** is the intent parameter value).

If an intent parameter is of the [WANT](#linkparamcategory) category, the system retrieves **paramMappingName** corresponding to **paramName** and passes the mapping name and value using the **parameters** field in [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md).

 |

#### LinkParamCategory

Enumerates the intent parameter categories available for the [@InsightIntentLink](#insightintentlink) decorator. The enum is used to define how intent parameters should be passed.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

| Name | Value | Description |
| :-- | :-- | :-- |
| LINK | 'link' | Category of link. Intent parameters are appended to the end of a URI link and passed to the application via the URI. |
| WANT | 'want' | Category of want. Intent parameters are passed to the application through the **parameters** field in [Want](../../both-models-recommended/ohos-app-ability-want-want/document.md). |

#### @InsightIntentPage

Decorates a page in the application as an intent, enabling AI systems to swiftly navigate to that page. For details on the parameters supported by this decorator, see [PageIntentDecoratorInfo](#pageintentdecoratorinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/J6eJcx53TKm7hVcw83OYHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=410622556230D34F4D6B94FDC10072D6ED8C54D4E4F3C71A8597D8E6AC6631A0)

This decorator is only applicable to struct pages.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

import { InsightIntentPage } from '@kit.AbilityKit';

@Entry
@Component
@InsightIntentPage({
  intentName: 'SearchMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: 'Search Music',
  displayDescription: 'Intent to search music',
  schema: 'SearchMusic',
  uiAbility: 'Entry',
  pagePath: './ets/pages/Index',
  navigationId: '1',
  navDestinationName: 'PageOne',
})
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### PageIntentDecoratorInfo

**PageIntentDecoratorInfo** inherits from [IntentDecoratorInfo](#intentdecoratorinfo) and describes the parameters supported by the [@InsightIntentPage](#insightintentpage) decorator, such as the name of [NavDestination](../../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navdestination10) of the target page.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uiAbility | string | No | Yes | Name of the UIAbility bound to the intent. |
| pagePath | string | No | No | Path of the page bound to the intent. The page must be a file that actually exists. |
| navigationId | string | No | Yes | ID of the [Navigation](../../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#attributes) component bound to the intent. |
| navDestinationName | string | No | Yes | Name of the [NavDestination](../../../../arkui/arkts-components/navigation-and-switching/navigation/document.md#navdestination10) component bound to the intent. |

#### @InsightIntentFunction

This decorator must be used together with the [@InsightIntentFunctionMethod](#insightintentfunctionmethod) decorator.

This decorator is used to decorate a class, and [@InsightIntentFunctionMethod](#insightintentfunctionmethod) is used to decorate a static function in that class. This setup defines the static function as an intent, enabling AI systems to execute it rapidly.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

#### @InsightIntentFunctionMethod

This decorator must be used together with the [@InsightIntentFunction](#insightintentfunction) decorator.

[@InsightIntentFunction](#insightintentfunction) is used to decorate a class, and this decorator is used to decorate a static function in that class. This setup defines the static function as an intent, enabling AI systems to execute it rapidly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/X_D3fyl5TlqfZwRalmWD6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B774AA22F45718669C8EDEA35959868C0ED68F223378FC1F1C1A8E494D9A3D8F)

The class containing static methods must be exported using **export**.

Parameter names and types of a function must align with those specified in the intent definition.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

import { InsightIntentFunction, InsightIntentFunctionMethod } from '@kit.AbilityKit';

@InsightIntentFunction()
export class ClassForFuncDemo {
  @InsightIntentFunctionMethod({
  intentName: 'GetWeather',
  domain: 'LifeDomain',
  intentVersion: '1.0.1',
  displayName: 'Query weather',
  displayDescription: 'Display weather information',
  icon: $r('app.media.app\_icon'), // $r indicates a local icon, which must be defined in the resource catalog.
  llmDescription: 'Get weather of an location',
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Weather Schema',
    'description': 'A schema for get weather of an location',
    'properties': {
      'location': {
        'type': 'string',
        'description': 'The city and state, e.g. Hangzhou',
        'minLength': 1
      }
    },
    'required': \['location'\],
    'additionalProperties': false
  }
})
  static getWeather(location: string): string {
    console.info(\`location: ${location}\`);
    return 'The current temperature in Hangzhou is 24℃';
  }
}

#### FunctionIntentDecoratorInfo

Parameter type of the [@InsightIntentFunctionMethod](#insightintentfunctionmethod) decorator. All properties inherit from [IntentDecoratorInfo](#intentdecoratorinfo).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

#### @InsightIntentEntry

Decorates a class that inherits from [InsightIntentEntryExecutor](../ohos-app-ability-insightintententryexecutor-base-class-for-insightintententry-in/document.md) to implement intent operations and configure the ability on which the intent depends. This helps the AI entry point to easily invoke the associated ability and perform the intended action. For details on the parameters supported by this decorator, see [EntryIntentDecoratorInfo](#entryintentdecoratorinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/LAzRNOFpT3qs8jyYA6OFDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=808CD86B3F98558B94AD88F70B1B0764F247736580B991F17B792A5030E744E8)

-   If this decorator is used to access a standard intent, all mandatory parameters defined in the standard intent JSON schema must be implemented and their parameter types must match.
-   If this decorator is used to access a custom intent, all mandatory parameters defined in **parameters** must be implemented and their parameter types must match.
-   Classes decorated by this decorator must be exported using **export default**. Class properties are limited to basic types or intent entities, and the return value must be intent entities.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG\_TAG: string = 'testTag-EntryIntent';

// Use the @InsightIntentEntry decorator to define an intent.
@InsightIntentEntry({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: 'Play Music',
  displayDescription: 'Intent to play music',
  icon: $r('app.media.app\_icon'), // $r indicates a local icon, which must be defined in the resource catalog.
  llmDescription: 'Supports passing song names to play music',
  keywords: \['music playback', 'play music', 'PlayMusic'\],
  abilityName: 'EntryAbility',
  executeMode: \[insightIntent.ExecuteMode.UI\_ABILITY\_FOREGROUND\],
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      }
    },
    'required': \['songName'\]
  }
})
export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
  songName: string = '';

  onExecute(): Promise<insightIntent.IntentResult<string>> {
    hilog.info(0x0000, LOG\_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
    hilog.info(0x0000, LOG\_TAG, '%{public}s', JSON.stringify(this));
    let storage = new LocalStorage();
    storage.setOrCreate('songName', this.songName);
    // Start the PlayMusicPage page based on the executeMode parameter.
    if (this.executeMode == insightIntent.ExecuteMode.UI\_ABILITY\_FOREGROUND) {
      this.windowStage?.loadContent('pages/PlayMusicPage', storage);
    } else if (this.executeMode == insightIntent.ExecuteMode.UI\_EXTENSION\_ABILITY) {
      this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
    }
    // Define the intent execution result.
    let result: insightIntent.IntentResult<string> = {
      code: 123,
      result: 'result'
    }
    hilog.info(0x0000, LOG\_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
    // Return the intent execution result in Promise mode.
    return Promise.reject(result);
  }
}

#### EntryIntentDecoratorInfo

Inherits from [IntentDecoratorInfo](#intentdecoratorinfo) and is used to describe the parameters supported by the [@InsightIntentEntry](#insightintententry) decorator.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilityName | string | No | No | Name of the ability bound to the intent. |
| executeMode | [insightIntent.ExecuteMode](../ohos-app-ability-insightintent-basic-definitions-of-insightintent-framework/document.md#executemode)\[\] | No | No | Execution mode of the intent call, that is, execution mode supported when the bound ability is started. |

#### @InsightIntentForm

Decorates a [FormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md) to specify the name of the widget bound to the FormExtensionAbility. This enables the AI entry point to add the widget via intent calls. For details on the parameters supported by this decorator, see [FormIntentDecoratorInfo](#formintentdecoratorinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/_WyKx2kYRxGyMB8_Eh2mJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C40E7D10249BECF2AE3DC85A57FD49D9DC83E5CDF73BDA20E9DF7A2AE92875B)

For details about the requirements for defining widget names, see [Widget Configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#widget-configuration).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { insightIntent, Want, InsightIntentForm } from '@kit.AbilityKit';

// Use the @InsightIntentForm decorator to define a widget of the FormExtensionAbility as an intent.
@InsightIntentForm({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: 'Play Music',
  displayDescription: 'Intent to play music',
  icon: $r('app.media.app\_icon'), // $r indicates a local icon, which must be defined in the resource catalog.
  llmDescription: 'Supports passing song names to play music',
  keywords: \['music playback', 'play music', 'PlayMusic'\],
  parameters: {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      },
      'artist': {
        'type': 'object',
        'description': 'Information about the artist',
        'properties': {
          'country': {
            'type': 'string',
            'description': 'The artist\\'s country of origin',
            'default': 'zh'
          },
          'city': {
            'type': 'object',
            'description': 'The artist\\' city of origin'
          },
          'name': {
            'type': 'string',
            'description': 'The name of the artist',
            'minLength': 1
          }
        },
        'required': \['name'\]
      }
    },
    'required': \['songName'\]
  },
  formName: 'widget'
})
export default class EntryFormAbility extends FormExtensionAbility {
  songName: string = '';

  onAddForm(want: Want) {
    // This API is called to return the FormBindingData object.
    let formData = '';
    return formBindingData.createFormBindingData(formData);
  }
}

#### FormIntentDecoratorInfo

Inherits from [IntentDecoratorInfo](#intentdecoratorinfo) and is used to describe the parameters supported by the [@InsightIntentForm](#insightintentform) decorator.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formName | string | No | No | Name of the widget bound to the FormExtensionAbility. |

#### @InsightIntentEntity

Decorates a class that inherits from [IntentEntity](../ohos-app-ability-insightintent-basic-definitions-of-insightintent-framework/document.md#intententity20) to define the class as an intent entity, which can pass parameters required for intent calls. For details on the parameters supported by this decorator, see [IntentEntityDecoratorInfo](#intententitydecoratorinfo).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Example**

import { insightIntent, InsightIntentEntity } from '@kit.AbilityKit';

@InsightIntentEntity({
  entityCategory: 'artist entity category',
  parameters: {
    '$id': '/schemas/ArtistClassDef',
    'type': 'object',
    'description': 'Information about the artist',
    'properties': {
      'country': {
        'type': 'string',
        'description': 'The artist\\'s country of origin',
        'default': 'zh'
      },
      'city': {
        'type': 'string',
        'description': 'The artist\\'s city of origin'
      },
      'name': {
        'type': 'string',
        'description': 'The name of the artist',
        'minLength': 1
      }
    },
    'required': \['name'\]
  }
})
export class ArtistClassDef implements insightIntent.IntentEntity {
  entityId: string = 'id';
  name: string = '';
}

#### IntentEntityDecoratorInfo

Describes the parameters supported by the [@InsightIntentEntity](#insightintententity) decorator.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Properties**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| entityCategory | string | No | No | Category of the intent entity. Intents can be classified based on intent entity categories. |
| parameters | Record<string, Object> | No | Yes | Data format of the intent entity. |
