# Node.js

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Entry Point Method

Define an entry point method as follows:

module.exports.myHandler = function(event, context, callback, logger)

-   **myHandler**: entry point method name.
-   **event**: JSON event object passed by the caller. For details, please refer to [event Object](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloudfunction-trigger-event-0000001620581529).
-   **context**: function context, which encapsulates the log API, callback API, environment variable **env**, and more.
-   **callback**: event handling result.
-   **logger**: API for recording logs.

**callback(object)** must be called explicitly to send the event handling result (any object that is compatible with **JSON.stringify**) to AppGallery Connect, which will then convert the result into a JSON string and send it back. Function execution is complete after **callback** is executed.

For complete sample code of a cloud function (Node.js 20._x_), please refer to [Sample Function](#en-us_topic_0000001658990474_section817193312817).

#### Recording Logs

You can call the **logger** API in your code to record logs. The API has been globally defined in the backend using **global.logger**. Currently, the following levels are supported:

-   logger.debug()
-   logger.error()
-   logger.warn()
-   logger.info()

#### Obtaining Environment Variables

You can use **context.env.key** in the code to access environment variables. The following is an example of obtaining the environment variable **env1**:

let env1 = context.env.env1;

If the environment variable is not set, **undefined** is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Bm0_0FTQTmeKkCqp_8zxtw/en-us_image_0000002474214361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC5A884798D85AD48709E76E95FD29D97941E8E12D642089666D16D829605568)

#### Troubleshooting

You can define your function code to capture an exception, encapsulate the captured exception into an **error** object, and send the **error** object to the caller. The exception captured by the system during function execution is also encapsulated into an **error** object and then sent back to the caller. The **error** object is defined as follows:

let error = {
    code: xxxxxx,
    message: "xxxxxxxx"
};

In the preceding information, **code** indicates the result code and **message** indicates the result code description.

The sample code is as follows:

try {
    logger.info(JSON.stringify(event));
    let result = { message: "success" };
    callback(result);
} catch (err) {
    let error = {
        code: 400,
        message: err.message
    };
    callback(error);
}

#### Sample Function

The following is a sample function:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ftjsHpAmTX24pNUC_eEquw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C08C2E87924283629A9968C2D1EEAA995C86B349D711C9A56EFE3BFAB86A004)

The return value type of the **myHandler()** entry point method in the sample code is for reference only. You can define it as needed.

/\*\*
 \* Describe the basic method of Cloud Functions.
 \*/

let myHandler = function (event, context, callback, logger) {
    // Display environment variables.
  let env1 = context.env.env1;

    // Display logs.
  logger.info("Test info log");
  logger.warn("Test warn log");
  logger.debug("Test debug log");
  logger.error("Test error log");

  logger.info("--------Start-------");
  try {
    let startTime = new Date().getTime();
    let endTime = startTime;
    let interval = 0;
    startTime = process.uptime() \* 1000;

        // Display input parameters and environment variables.
    logger.info("request: " + JSON.stringify(event.request));
    logger.info("env1: " + env1);

    endTime = process.uptime() \* 1000;
    interval = endTime - startTime;
    logger.info("intervalTime: " + interval);
    logger.info("--------Finished-------");

    let res = new context.HTTPResponse(context.env, {
      "res-type": "context.env",
      "faas-content-type": "json"
    }, "application/json", "200");
    res.body = { "intervalTime": interval };
    callback(res);
  } catch (error) {
    logger.error("--------Error-------");
    logger.error("error: " + error);
    callback(error);
  }
};

module.exports.myHandler = myHandler;

#### Preparing Your Function Deployment Package

The Node.js deployment package you upload must use the following structure. The code file (**handler.js** in this example) of the handler must be in the root directory of the ZIP package, and the dependencies must be placed in the **node\_modules** directory.

my-function.zip
  |---- handler.js
  |---- node\_modules
    |----async
    |----async-listener

You can run commands of the npm tool to install and manage dependencies. For example, run the **npm install _xxx_** command (no restriction on the execution path) to automatically install dependency **_xxx_** to the **node\_modules** folder in the root directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/uv8tCN9ZT5KUJoLCweHOYA/en-us_image_0000002474174521.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53D43C6F6EECE9CF66CD8E782F7183791F283AE9805F4ED85716837A7B3F9B60)
