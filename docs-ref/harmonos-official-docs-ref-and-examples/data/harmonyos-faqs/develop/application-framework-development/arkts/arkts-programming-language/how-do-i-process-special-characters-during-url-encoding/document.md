# How do I process special characters during URL encoding?

URL encoding supports only ASCII character set, including letters, digits, and some reserved characters. Other characters (such as spaces, Chinese characters, and special characters) must be encoded before being transmitted in URL. URL encoding rules are as follows:

-   **Unreserved character**
    
    These characters do not need to be encoded, including:
    
    1.  Letters: A to Z, a to z
    2.  Digits: 0 to 9
    3.  Symbols: -, \_, ., and ~

-   **Reserved character**
    
    These characters have special meanings and need to be encoded when they are used as data, including !, \*, ', (, ), ;, :, @, &, =, +, $, /,?, #, \[, and \]. For example, you can use **encodeURIComponent()** to escape '+' as '%2B'.
    
    @Entry
    @Component
    export struct HandlingSpecialCharactersForURLEncoding {
      @State message: string = 'encode';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                const originalString = '123+456';
                const encoded = encodeURIComponent(originalString);
                console.info(encoded); // output: '123%2B456'.
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

-   **Non-ASCII characters** (such as Chinese, Japanese, and emojis)
    
    You can first encode such characters into a sequence of bytes in UTF-8 format, and then percent-encode each byte.
