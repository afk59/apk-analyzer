# Streaming

#### Use Case

HTTP streaming allows the client and server to exchange data in a stream format without waiting for all the data to be ready, which can significantly improve user experience. This mode is suitable for scenarios such as uploading and downloading large files, live streaming, and real-time data updates.

#### Constraints

The capability of synchronous reads and writes in stream format supports phones, 2-in-1 devices, tablets, wearables, and (since 5.1.1(19)) TVs.

#### Buffer-based Streaming

## API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section127952271692).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

write(buffer: string | ArrayBuffer): void

 | 

Writes a data segment to the queue, which will be sent by an I/O thread of the framework at a proper time.

 |
| 

read(buffer: ArrayBuffer): Promise<number>

 | 

Reads data from a file.

 |

## Example

1.  Import the required module.
    
    import { rcp } from '@kit.RemoteCommunicationKit';
    
2.  Use **rcp.NetworkInputQueue** to create a synchronous write queue object to implement synchronous writing.
    
    export const testNetworkInputQueue = () => {
      // Create a synchronous write queue object.
      const networkInputQueue = new rcp.NetworkInputQueue();
      // Simulate the scenario where a file is uploaded using synchronous read/write streams and write the file to the synchronous write queue **networkInputQueue**.
      let counter = 0;
      const interval = setInterval(() => {
        // Add data to the synchronous write queue.
        networkInputQueue.write('a counter ' + counter++);
        console.info(\`networkInputQueue write\`);
        if (counter === 10) {
          clearInterval(interval);
          // Close the synchronous write queue.
          networkInputQueue.close();
        }
      }, 1000);
      try {
        // Create a session.
        const session = rcp.createSession();
        console.info(\`Post start.\`);
        // Send a request. The related data is uploaded while being written to the **networkInputQueue**.
        session.post('https://httpbin.org/anything', networkInputQueue).then((response) => {
          // Result status code.
          console.info(\`Response status code is: ${response.statusCode}\`);
          if (response && response.statusCode === 200) {
            console.info(\`Post succeeded! response: ${response.toString()}\`);
          } else {
            console.error(\`Post failed.\`);
          }
          session.close();
        }).catch((error: Error) => {
          console.error(\`Post error: ${JSON.stringify(error)}\`);
          session.close();
        });
      } catch (error) {
        console.error(\`create session error: ${JSON.stringify(error)}\`);
      }
    }
    
3.  Use **rcp.NetworkOutputQueue** to create a synchronous read queue object to implement synchronous reading.
    
    export const testNetworkOutputQueue = () => {
      // Create a synchronous read queue object.
      const networkOutputQueue = new rcp.NetworkOutputQueue();
      // Create a session.
      try {
        const session = rcp.createSession();
        // Configure the size of the request stream data.
        const numOfChunks = 10;
        const chunkLength = 1000;
        const totalBytes = numOfChunks \* chunkLength;
        // Send a request. The response data is temporarily stored in the synchronous read queue **networkOutputQueue**.
        session.get('https://httpbin.org/bytes/' + totalBytes.toString(), networkOutputQueue).then((response) => {
          if (response && response.statusCode === 200) {
            console.info(\`get byts succeeded.\`);
          } else {
            console.error(\`get byts failed.\`);
          }
          session.close();
        }).catch((err: Error) => {
          console.error(\`get byts error: ${err.message}\`);
          session.close();
        });
        // Read data from the **networkOutputQueue** queue cyclically to retrieve response data. For example, read 1000 bytes of data every 1000 milliseconds.
        let totalGetLength = 0;
        const intervalId = setInterval(() => {
          // Process the read data based on your service needs.
          const chunk = networkOutputQueue.read(chunkLength);
          totalGetLength += chunk.byteLength;
          console.info(\`get byts totalGetLength: ${totalGetLength}\`);
          // Clear the timer after data reading is complete.
          if (totalGetLength === totalBytes) {
            clearInterval(intervalId);
            console.info(\`get byts finished.\`);
          }
        }, 1000);
      } catch (error) {
        console.error(\`create session error: ${JSON.stringify(error)}\`);
      }
    }
    

#### Callback-based Streaming

## API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section187981940151318).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

uploadFromStream(url: [URLOrString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section320653742718), uploadFrom: [UploadFromStream](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section187981940151318)): Promise<[Response](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section156381815599)\>

 | 

Uploads data via streams.

 |
| 

downloadToStream(url: [URLOrString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section320653742718), downloadTo: [DownloadToStream](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section1790033215431)): Promise<[Response](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section156381815599)\>

 | 

Downloads data via streams.

 |

## Example

1.  Import the required module.
    
    import { rcp } from '@kit.RemoteCommunicationKit';
    import fs from '@ohos.file.fs';
    
2.  Define the **FdReadStream** class and implement the **rcp.ReadStream** API to read data from streams.
    
    class FdReadStream implements rcp.ReadStream {
      readonly fd: number;
    
      constructor(fd: number) {
        this.fd = fd;
      }
    
      async read(buffer: ArrayBuffer): Promise<number> {
        return fs.read(this.fd, buffer);
      }
    }
    
3.  Call the **uploadFromStream** API to upload data via streams.
    
    export function testUploadFromStream(uploadFilePath: string) {
      try {
        // Create a session.
        const session = rcp.createSession();
        // Open the file based on the path of the file to be uploaded.
        const file = fs.openSync(uploadFilePath, fs.OpenMode.READ\_ONLY);
        // File reading stream.
        const fileStream = new rcp.UploadFromStream(new FdReadStream(file.fd));
        // Upload data via streams.
        session.uploadFromStream('https://httpbin.org/anything', fileStream).then((resp) => {
          console.info(\`testUploadFromStream response: ${JSON.stringify(resp)}\`);
          if (resp && resp.statusCode === 200) {
            console.info(\`testUploadFromStream succeeded.\`);
          } else {
            console.error(\`testUploadFromStream failed.\`);
          }
          // Close the file and session after the upload is complete.
          fs.closeSync(file.fd);
          session.close();
        }).catch((error: Error) => {
          console.error(\`testUploadFromStream error: ${JSON.stringify(error)}\`);
          fs.closeSync(file.fd);
          session.close();
        });
      } catch (error) {
        console.error(\`testUploadFromStream error: ${JSON.stringify(error)}\`);
      }
    }
    
4.  Define the **FdWriteStream** class and implement the **WriteStream** API to write data via streams.
    
    class FdWriteStream implements rcp.WriteStream {
      readonly fd: number;
    
      constructor(fd: number) {
        this.fd = fd;
      }
    
      async write(buffer: ArrayBuffer): Promise<number | void> {
        return fs.write(this.fd, buffer);
      }
    }
    
5.  Call the **downloadToStream** API to download data via streams.
    
    export function testDownloadToStream(downloadToPath: string) {
      try {
        // Create a session.
        const session = rcp.createSession();
        // Open the file based on the path of the file to be downloaded.
        const file = fs.openSync(downloadToPath, fs.OpenMode.CREATE | fs.OpenMode.WRITE\_ONLY);
        // Write the file data to streams. 
        const fileStream = { kind: 'stream', stream: new FdWriteStream(file.fd) } as rcp.DownloadToStream
        // Download data via streams.
        session.downloadToStream('https://httpbin.org/bytes/', fileStream)
          .then((resp) => {
            console.info(\`testDownloadToStream response: ${JSON.stringify(resp)}\`);
            if (resp && resp.statusCode === 200) {
              console.info(\`testDownloadToStream succeeded.\`);
            } else {
              console.error(\`testDownloadToStream failed.\`);
            }
            // Close the file and session after the download is complete.
            fs.close(file.fd);
            session.close();
          })
          .catch((error: Error) => {
            console.error(\`testDownloadToStream error: ${JSON.stringify(error)}\`);
            fs.close(file.fd);
            session.close();
          })
      } catch (err) {
        console.error(\`testDownloadToStream error: ${JSON.stringify(err)}\`);
      }
    }
