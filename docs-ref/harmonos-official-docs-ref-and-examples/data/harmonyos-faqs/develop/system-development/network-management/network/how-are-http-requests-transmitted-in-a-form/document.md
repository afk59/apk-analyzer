# How are HTTP requests transmitted in a form?

1.  In the HTTP message header, **Content-Type** is used to specify the media type. Set this parameter to **application/x-www-form-urlencoded**.
    
    import { http } from '@kit.NetworkKit';
    
    let options: http.HttpRequestOptions = {
      method: http.RequestMethod.GET,
      extraData: 'send message',
      header: { 'Content-Type': 'application/x-www-form-urlencoded' },
      readTimeout: 50000,
      connectTimeout: 50000
    }
    
2.  Configure request parameters in **extraData**. Currently, parameters of the string, object, and ArrayBuffer types are supported.
    
    let httpRequest = http.createHttp();
    let data = "user=Query&password=Admin123";
    httpRequest.request(
      'https:xxx',
      {
        method: http.RequestMethod.POST,
        // Optional, default is http.RequestMethod.GET//Developers can add header fields according to their own business needs
        header: { 'Content-Type': 'application/x-www-form-urlencoded' }, // This field is used to pass content when using POST requests
        extraData: data,
        connectTimeout: 60000, // Optional, default is 60000ms
        readTimeout: 60000, // Optional, default is 60000ms
      }, (err, data) => {
      if (!err) {
        // Data.read is the HTTP response content, which can be parsed according to business needs
        console.info('Result:' + JSON.stringify(data.result));
        console.info('code:' +
        JSON.stringify(data.responseCode)); // Data.reader is an HTTP response header that can be parsed according to business needs
        console.info('header:' + JSON.stringify(data.header));
        console.info('cookies:' +
        JSON.stringify(data.cookies)); // Starting from API8
      } else {
        console.info('error:' + JSON.stringify(err)); // Unsubscribe from HTTP response header events
        httpRequest.off('headersReceive'); // When the request is exhausted, call the destroy method to actively destroy it.
        httpRequest.destroy();
      }
    })
