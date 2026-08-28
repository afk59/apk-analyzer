# Request Examples

#### Notification Message

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:0
 
// Request Body
{ 
  "payload": { 
    "notification": { 
      "category": "xxxxxx", // Set it to the actual notification message category.
      "title": "Common title", 
      "body": "Common body", 
      "clickAction": { 
        "actionType": 0
      },
      "style": 0, 
      "image":"https://lf\*\*\*\*\*\*\*246.png" 
    } 
  }, 
  "target": { 
    "token": \["MAAALgE4G98BAAAAst\*\*\*\*\*\*\*jg"\] 
  } 
}

## Receiving Notification Messages When the App is Running in the Foreground

Notification messages are displayed only when the app is running in the background. When the app is running in the foreground, even though notification messages are not displayed, the app can receive notification messages and complete service processing accordingly. For details, please refer to [notification message processing when the app is running in the foreground](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section99251359545).

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type: 0

// Request Body
{
  "payload": {
    **"notification": {**
      "category": "MARKETING",
      "title": "Common notification title",
      "body": "Common notification body",
      "clickAction": {
        "actionType": 0
      },
      "foregroundShow": false  // When this parameter is set to **false**, notification messages are not displayed when the app is running in the foreground. The default value is **true**, indicating that notification messages are displayed no matter whether the app is running in the foreground or background.
    **}**
  },
  "target": {
    "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
  },
  "pushOptions": {
    "testMessage": true,
    "ttl": 86400
  }
}

#### Widget Update Message

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:1
 
// Request Body
{ 
  "payload": { 
    "formData": { 
      "123": 96, 
      "class": "123" 
    }, 
    "version": 922337203, 
    "images": \[ 
      { 
        "keyName": "hello", 
        "url": "https://xxx.png", 
        "require": 1 
      } 
    \], 
    "formId": 0, 
    "moduleName": "testName", 
    "formName": "testFormName", 
    "abilityName": "testAbilityName"      
  }, 
  "pushOptions": { 
    "biTag": "this is bi", 
    "ttl": 666 
  }, 
  "target": { 
    "token": \[ 
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*ttQd4Tw" 
    \]   
  } 
}

#### Text-to-Speech Message

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:2
 
// Request Body
{ 
  "payload": { 
    "extraData": "Extension extra data", 
    "notification": { 
      "category": "PLAY\_VOICE", 
      "title": "Common title", 
      "body": "Common body", 
      "clickAction": { 
        "actionType": 0
      }, 
      "style": 0, 
      "image":"https://lf\*\*\*\*\*\*\*246.png" 
    } 
  }, 
  "target": { 
    "token": \["MAAALgE4G98BAAAAst\*\*\*\*\*\*\*jg"\] 
  } 
}

#### Background Message

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:6
 
// Request Body
{ 
  "payload": { 
    "extraData": "Carried data" 
  }, 
  "target": { 
    "token": \["MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"\] 
  } 
}

#### Live View Creation Message

## Flight Scenario (Event: FLIGHT)

Scheduled departure, using the left-right text template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"
 
// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* 
push-type:7 

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 1,
    "operation": 0,
    "event": "FLIGHT",
    "status": "DEPART", // Scheduled departure
    "activityData": {
      "notificationData": {
        "keywords": {
          "flightNo": "MU1471"
        },
        "type": 5,
        "contentTitle": "Flight {{status}}", // The flight is scheduled to depart.
        "contentText": \[
          {
            "text": "Flight number:"
          },
          {
            "text": "{{flightNo}}", // MU1471
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 0
        },
        "firstTextBlock": {
          "firstLine": "12:00",
          "secondLine": "Shanghai Hongqiao"
        },
        "lastTextBlock": {
          "firstLine": "14:20",
          "secondLine": "Chengdu Tianfu"
        },
        "displayHorizontalLine": true,
        "spaceIcon": "space.png", // The value is a file name in **/resources/rawfile**.
        "extend": {
          "type": 3,
          "pic": "flight.png", // The value is a file name in **/resources/rawfile**.
          "clickAction": {
            "actionType": 1,
            "action": "xxxxxxx"
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "remind": "EXPAND",
        "title": "Depart soon",
        "content": "Please go to the airport as soon as possible."
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

## Ride Hailing (Event: TAXI)

Driver on the way, using the progress visualization template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 2,
    "operation": 0,
    "event": "TAXI",
    "status": "DRIVER\_ON\_THE\_WAY", // Driver on the way
    "activityData": {
      "notificationData": {
        "type": 3,       
        "contentTitle": "{{status}}", // Driver on the way
        "contentText": \[
          {
            "text": "1.2 km"
          },
          {
            "text": "away",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | "
          },
          {
            "text": "5 minutes",
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 1, // Open a custom app page.
          "action": "xxxxxx" // Action corresponding to the ability of an in-app page.
        },
        "richProgress": {
          "type": 0,
          "nodeIcons": \["icon1.png", "icon2.png", "icon3.png"\], // The value is file names in **/resources/rawfile**.
          "indicatorIcon": "taxi.png", // The value is a file name in **/resources/rawfile**.
          "progress": 40,
          "indicatorType": 1,
          "color": "#FF317AF7",
          "bgColor": "#19000000"
        },
        "extend": {
          "type": 3,
          "pic": "phone.png", // The value is a file name in **/resources/rawfile**.
          "clickAction": {
            "actionType": 5, // Open the dialer screen.
            "data": {
              "tel": "138xxxxxxxx" // Set the **tel** field to a mobile number.
            }
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "remind": "EXPAND",
        "title": "Picking up",
        "content": "About 5 minutes"
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

## High-Speed Rail or Common Train (Event: TRAIN)

Scheduled departure, using the left-right text template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 3,
    "operation": 0,
    "event": "TRAIN",
    "status": "DEPART", // Scheduled departure
    "title": "The train is about to leave.",
    "content": "Please go to the railway station as soon as possible.",
    "activityData": {
      "notificationData": {
        "keywords": {
          "trainNo": "G1406"
        },
        "type": 5,        
        "contentTitle": "Train {{status}}", // The train is scheduled to depart.
        "contentText": \[
          {
            "text": "Train number:"
          },
          {
            "text": "{{trainNo}}", // G1406
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 0
        },
        "firstTextBlock": {
          "firstLine": "13:00",
          "secondLine": "Shanghai Hongqiao"
        },
        "lastTextBlock": {
          "firstLine": "14:20",
          "secondLine": "Nanjing South Railway Station"
        },
        "displayHorizontalLine": true,
        "spaceIcon": "space.png", // The value is a file name in **/resources/rawfile**.
        "extend": {
          "type": 3,
          "pic": "train.png", // The value is a file name in **/resources/rawfile**.
          "clickAction": {
            "actionType": 1,
            "action": "xxxxxxx"
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "remind": "EXPAND",
        "title": "Depart soon",
        "content": "Please go to the railway station as soon as possible.",
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

#### Live View Update Message

## Flight Scenario (Event: FLIGHT)

Checked in, using the left-right text template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"
 
// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* 
push-type:7 

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 1,
    "operation": 1,
    "event": "FLIGHT",
    "status": "CHECKED\_IN", // Checked in
    "version": 1,
    "activityData": {
      "notificationData": {
        "keywords": {
          "flightNo": "MU1471"
        },
        "type": 5,
        "contentTitle": "Boarding gate 88",
        "contentText": \[
          {
            "text": "{{status}} | " // Checked in
          },
          {
            "text": "{{flightNo}}", // MU1471
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 0
        },
        "firstTextBlock": {
          "firstLine": "12:00",
          "secondLine": "Shanghai Hongqiao"
        },
        "lastTextBlock": {
          "firstLine": "14:20",
          "secondLine": "Chengdu Tianfu"
        },
        "displayHorizontalLine": true,
        "spaceIcon": "space.png", // The value is a file name in **/resources/rawfile**.
        "extend": {
          "type": 3,
          "pic": "flight.png", // The value is a file name in **/resources/rawfile**.
          "clickAction": {
            "actionType": 1,
            "action": "xxxxxxx"
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "remind": "EXPAND",
        "title": "Boarding gate 88",
        "content": "Complete security check as soon as possible."
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

## Ride Hailing (Event: TAXI)

Heading to the destination, using the progress visualization template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 2,
    "operation": 1,
    "event": "TAXI",
    "status": "HEADING\_TO\_DESTINATION", // Heading to the destination
    "version": 1,
    "activityData": {
      "notificationData": {
        "type": 3,
        "contentTitle": "{{status}}", // Heading to the destination
        "contentText": \[
          {
            "text": "Remaining distance:"
          },
          {
            "text": "7.2 km",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | About"
          },
          {
            "text": "27 minutes",
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 1,
          "action": "xxxxxx"
        },
        "richProgress": {
          "type": 0,
          "nodeIcons": \["icon1.png", "icon2.png", "icon3.png"\], // The value is file names in **/resources/rawfile**.
          "indicatorIcon": "taxi.png", // The value is a file name in **/resources/rawfile**.
          "progress": 60,
          "indicatorType": 1,
          "color": "#FF317AF7",
          "bgColor": "#19000000"
        },
        "extend": {
          "type": 0
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "title": "27 minutes",
        "content": "Remaining distance: 7.2 km"
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

Trip completed, using the emphasized text template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 2,
    "operation": 1,
    "event": "TAXI",
    "status": "COMPLETED", // Trip completed
    "version": 2,
    "activityData": {
      "notificationData": {
        "type": 4,       
        "contentTitle": "{{status}}, Please pay the order.", // Trip completed. Please pay the order.
        "contentText": \[
          {
            "text": "Total distance:"
          },
          {
            "text": "10 km",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | Time required"
          },
          {
            "text": "30 minutes",
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 1,
          "action": "xxxxxx"
        },
        "singleTextBlock": { 
          "firstLine": "Total cost:", 
          "secondLine": "CNY35.2", 
          "underlineColor": "#FF317AF7" 
        }, 
        "descPic": "payment.png", // The value is a file name in **/resources/rawfile**.
        "extend": {
          "type": 0
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "title": "Pending payment",
        "content": "Cost: CNY35.2"
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

## High-Speed Rail or Common Train (Event: TRAIN)

Train on the move, using the left-right text template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7

// Request Body
{
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "payload": {
    "activityId": 3,
    "operation": 1,
    "event": "TRAIN",
    "status": "HEADING\_TO\_DESTINATION", // Train on the move
    "version": 1,
    "activityData": {
      "notificationData": {
        "keywords": {
          "trainNo": "G1406"
        },
        "type": 5,        
        "contentTitle": "{{status}}", // Train on the move
        "contentText": \[
          {
            "text": "Train number:"
          },
          {
            "text": "{{trainNo}}", // G1406
            "foregroundColor": "#FF317AF7"
          }
        \],
        "clickAction": {
          "actionType": 0
        },
        "firstTextBlock": {
          "firstLine": "13:00",
          "secondLine": "Shanghai Hongqiao"
        },
        "lastTextBlock": {
          "firstLine": "14:20",
          "secondLine": "Nanjing South Railway Station"
        },
        "displayHorizontalLine": true,
        "spaceIcon": "space.png", // The value is a file name in **/resources/rawfile**.
        "extend": {
          "type": 3,
          "pic": "train.png", // The value is a file name in **/resources/rawfile**.
          "clickAction": {
            "actionType": 1,
            "action": "xxxxxxx"
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "title": "On the move",
        "content": "Expected to arrive at 14:20."
      }
    }
  },
  "target": {
    "token": \[
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"
    \]
  }
}

## Live Scores (Event: SCORE)

Latest live scores, using the live scores template

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:7 
 
// Request Body
{ 
  "pushOptions": { 
    "ttl": 1000, 
    "biTag": "biTag" 
  }, 
  "payload": { 
    "activityId": 4, 
    "operation": 1, 
    "event": "SCORE", 
    "activityData": { 
      "notificationData": { 
        "type": 7,         
        "contentTitle": "Fourth period", 
        "contentText": \[ 
          { 
            "text": "XX",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " VS " 
          },
          {
            "text": "XX",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | Group stage match five" 
          }
        \], 
         "game": { 
            "host": { 
              "icon":"host.png", // The value is a file name in **/resources/rawfile**.
              "name": "Team A", 
              "score": "110" 
            }, 
            "guest": { 
              "icon":"guest.png", // The value is a file name in **/resources/rawfile**.
              "name": "Team B", 
              "score": "102" 
            }, 
            "competition": { 
              "desc": "Q4", 
              "time":"02:16" 
            } 
          },
        "displayHorizontalLine": true,
        "clickAction": {
          "actionType": 1,
          "action": "xxxxxxx"
        }
      }, 
      "capsuleData": { 
        "type": 1, 
        "status": 1, 
        "icon": "icon.svg", // The value is a file name in **/resources/rawfile**.
        "bgColor": "#FF317AF7",
        "title": "110:102", 
        "content": "Fourth period" 
      } 
    } 
  }, 
  "target": { 
    "token": \["MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq"\] 
  } 
}

#### In-App Call Message

// Request URL
POST "https://push-api.cloud.huawei.com/v3/3158882\*\*\*52863/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
push-type:10
 
// Request Body
{ 
  "pushOptions": { 
    "biTag": "biTag",
    "ttl": 30
  }, 
  "payload": { 
    "extraData": "Data transferred to an app."
  }, 
  "target": { 
    "token": \[ 
      "MAAALgE4G98BAAAAst\*\*\*\*\*\*\*\*\*\*\*\*jq" 
    \] 
  } 
}
