# How does the Text component load Unicode characters?

To display Unicode characters in a **Text** component, you can use string literals with escaped Unicode codes within the **content** parameter of the component. The sample code snippet is as follows:

@Entry
@Component
struct TextView {
  build() {
    Column() {
      Text("\\u{1F468}\\u200D\\u{1F469}\\u200D\\u{1F467}\\u200D\\u{1F466}")
        .width(100)
        .height(100)
        .fontSize(50)
    }
  }
}

Converting a character string to Unicode code:

let chineseStr: string = "Chinese";
const encodedStr = Array.from(chineseStr).map(char =>\`\\\\u${char.codePointAt(0)!.toString(16).padStart(4, '0')}\`).join("");

Converting Unicode code to a character string:

let unicodeStr: string = "\\\\u4e2d\\\\u6587";
const decodedStr = unicodeStr.replace(/\\\\u(\[\\dA-Fa-f\]{4})/g,(\_,p1:string) => String.fromCodePoint(parseInt(p1, 16)));
