# How do I open a file on in C/C++?

Currently, the user path in a mobile phone cannot be opened in C. You can open the file in ArkTS to obtain the FD, pass the FD to C, and then open the file in C.

1\. Save an image in the user directory to the sandbox directory.

import { fileIo} from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import testNapi from 'libentry.so';
import { common } from '@kit.AbilityKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Open File';

  async open() {
    const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE; // Filter and select media file type as IMAGE
    photoSelectOptions.maxSelectNumber = 5; // Select the maximum number of media files
    let uris: Array<string> = \[\];
    const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    await photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      uris = photoSelectResult.photoUris;
      console.info('photoViewPicker.select to file succeed and uris are:' + uris);
    }).catch((err: BusinessError) => {
      console.error(\`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}\`);
    })
    try {
      let uri: string = uris\[0\];
      let file = fileIo.openSync(uri, fileIo.OpenMode.READ\_ONLY);
      console.info('file fd: ' + file.fd);
      let fd = file.fd
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext
      let filesDir = context.filesDir;
      fileIo.copyFileSync(fd, filesDir + '/test2.jpg')
      let file2 = fileIo.openSync(filesDir + '/test2.jpg', fileIo.OpenMode.READ\_ONLY);
      let file3 = fileIo.openSync(filesDir + '/test3.jpg', fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
      testNapi.ReadFile(file2.fd, file3.fd)
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`openSync failed, code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .onClick(() => {
        this.open();
      })
      .width('100%')
    }
    .height('100%')
  }
}

2\. Copy test2 in the sandbox directory to test3 in C.

static napi\_value OpenFile(unsigned int fd, unsigned int fd2) { 
    OH\_LOG\_INFO(LOG\_APP, "OpenFile"); 
 
    if (fd != -1) { 
        char buffer\[4096\]; 
        ssize\_t bytesRead; 
        // Read the file content into the buffer 
        bytesRead = read(fd, buffer, sizeof(buffer)); 
        if (bytesRead == -1) { 
            OH\_LOG\_INFO(LOG\_APP, "fail to read file"); 
            close(fd); // Close file descriptor 
            return nullptr; 
        } 
        while (bytesRead != 0) { 
            OH\_LOG\_INFO(LOG\_APP, "Read file size %{public}lu", bytesRead); 
            OH\_LOG\_INFO(LOG\_APP, "Read file cg"); 
            char \*pData1 = buffer; 
            OH\_LOG\_INFO(LOG\_APP, "file content: \\n%{public}s", pData1); 
            ssize\_t bytesWrite; 
            bytesWrite = write(fd2, pData1, bytesRead); 
            if (bytesWrite == -1) { 
                OH\_LOG\_INFO(LOG\_APP, "Writing file failed"); 
                close(fd2); // Close file descriptor 
                return nullptr; 
            } 
            bytesRead = read(fd, buffer, sizeof(buffer)); 
        } 
        // Close file descriptor 
        close(fd); 
        close(fd2); // Close file descriptor 
    } 
    return nullptr; 
} 
static napi\_value ReadFile(napi\_env env, napi\_callback\_info info) { 
    size\_t argc = 2; 
    napi\_value args\[2\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
    unsigned int fd = -1; 
    napi\_get\_value\_uint32(env, args\[0\], &fd); 
    unsigned int fd2 = -1; 
    napi\_get\_value\_uint32(env, args\[1\], &fd2); 
    OpenFile(fd, fd2); 
    return nullptr; 
}
