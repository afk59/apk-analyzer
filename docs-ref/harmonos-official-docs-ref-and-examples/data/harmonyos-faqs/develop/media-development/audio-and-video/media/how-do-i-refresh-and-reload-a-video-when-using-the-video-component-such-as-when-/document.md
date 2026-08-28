# How do I refresh and reload a video when using the Video component, such as when there is a network exception causing playback failures?

You can first set the URL to an empty string and then change it back to the original value. The sample code is as follows:

@Component
export struct VideoErrorReload {
  @State url: string = 'https://\*\*\*\*\*\*';

  build() {
    Column({ space: 20 }) {
      Video({ src: this.url })
        .height(300)

      Button('Reload URL')
        .onClick(() => {
          let temp = this.url;
          this.url = '';
          setTimeout(() => {
            this.url = temp;
          }, 100);
        })
    }
  }
}
