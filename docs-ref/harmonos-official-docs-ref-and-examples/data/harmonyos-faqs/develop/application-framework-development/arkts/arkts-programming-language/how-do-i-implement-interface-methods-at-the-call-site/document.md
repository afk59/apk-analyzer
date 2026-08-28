# How do I implement interface methods at the call site?

The sample code is as follows:

// The custom interface is as follows:
export interface OnTrustListener {
  OnSuccess: (data: string) => void;
  OnError: (error: string) => void;
}

@Component
export struct InterfaceUse {
  private listener: OnTrustListener = {
    OnSuccess: (data: string) => {
      console.info('data is:' + data);
    },
    OnError: (error: string) => {
      console.info('error is:' + error);
    }
  };

  build() {
    Column() {
      Button('click me')
        .onClick((event: ClickEvent) => {
          this.listener.OnSuccess('success');
        })
    }
    .width('100%')
    .height('100%')
  }
}
