# Using System Pickers

You can use system Pickers (such as **DocumentViewPicker**, **PhotoViewPicker**, or **ContactsPicker**) to simplify the process for the user to select documents, photos, or contacts. After an application starts a system Picker and the user selects resources from the Picker, the selection result is returned to the application.

Each Picker is implemented by an independent system process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/98WvLnezRgCC9mlFpICrGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4DCCC16358DC900BA2DA3380D3885127AB7E0581727337842488E8BE5362C4C)

The system Pickers have been pre-authorized with permissions. When using a Picker, the application can temporarily access the corresponding resources without requesting the permission. For example, before accessing a user's image, an application normally needs the permission for reading images. By using the photo Picker, the application can directly access the image selected by the user.

System Pickers are integrated into system applications as a means to start system resources. For details, see [Starting a System Application](../../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-a-system-application/document.md).
