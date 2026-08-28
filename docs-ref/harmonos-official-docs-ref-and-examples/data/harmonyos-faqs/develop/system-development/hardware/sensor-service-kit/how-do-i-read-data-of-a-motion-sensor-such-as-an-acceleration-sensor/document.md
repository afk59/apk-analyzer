# How do I read data of a motion sensor such as an acceleration sensor?

1\. Import the **sensor** module.

import { sensor } from '@kit.SensorServiceKit';

2\. Register a callback to listen for acceleration sensor data.

try {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
    console.info('X-coordinate component: ' + data.x);
    console.info('Y-coordinate component: ' + data.y);
    console.info('Z-coordinate component: ' + data.z);
  }, { interval: 10000000 });
} catch (err) {
  console.error('On fail, errCode: ' + err.code + ' ,msg: ' + err.message);
}

**Reference**

[Sensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-sensor)
