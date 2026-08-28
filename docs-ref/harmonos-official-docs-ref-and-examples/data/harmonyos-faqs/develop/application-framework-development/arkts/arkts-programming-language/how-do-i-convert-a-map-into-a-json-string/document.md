# How do I convert a map into a JSON string?

You can convert a map to a record and then use **JSON.stringify()** to convert the record to a JSON string. Refer to the code snippet below.

let mapSource = new Map<string, string>();
mapSource.set('name', 'name1');
mapSource.set('width', '100');
mapSource.set('height', '50');

let jsonObject: Record<string, Object> = {};
mapSource.forEach((value, key) => {
  if (key !== undefined && value !== undefined) {
    jsonObject\[key\] = value;
  }
})
let jsonInfo: string = JSON.stringify(jsonObject);

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Map to JSON')
        .onClick(() => {
          console.log('jsonInfo:', jsonInfo); // jsonInfo: {"name":"name1","width":"100","height":"50"}
        })
    }
  }
}
