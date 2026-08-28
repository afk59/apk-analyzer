# Solution Overview

Starting from API version 20, intents can be developed via decorators, allowing existing features to be quickly integrated into system entry points. You can customize intents and quickly integrate your features with them by adding link-, page-, or function-based decorators, easily making these features accessible to users through Intent Kits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Tfy6iaXdQDSKvW2ISN8Wjw/en-us_image_0000002402267805.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062127Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2EBBE81F8A7A20F1EC92DF3147CF85C0FA33497EE9DEAE45AA7221701F031E3 "Click to enlarge")

You can select different types of decorators to declare intents based on the features you want to offer.

-   Link-based decorator: @InsightIntentLink
    
    Add a decorator to an already implemented deep link or app link to open the target function page.
    

-   Page-based decorator: @InsightIntentPage
    
    Add a decorator to an already implemented page to open the target function page.
    

-   Function-based decorator: @InsightIntentFunction and @InsightIntentFunctionMethod
    
    Add the **@InsightIntentFunctionMethod** decorator to an already implemented function and add the **@InsightIntentFunction** decorator to the class to which the function belongs to declare the intent. In this way, the function can be executed.
