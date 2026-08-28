# How do I implement HTTP persistent connections?

You can use scheduled HTTP requests to simulate persistent connections. The code snippet is as follows:

import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
// Set the polling period to 5 seconds.
setTimeout(() => {
  httpRequest.request("EXAMPLE\_URL", {
    method: http.RequestMethod.GET,
    connectTimeout: 60000,
    readTimeout: 60000
  }, (err, data) => {
    if (!err) {
      console.info('Received data:', JSON.stringify(data.result));
    } else {
      console.info('Polling error:', JSON.stringify(err));
    }
  })
}, 5000)
