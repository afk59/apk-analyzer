# How do I merge two objects?

For performance purposes, ArkTS restricts the use of **Object.assign()** in ES6. If you need to extend object properties or merge two objects in an .ets file, implement the **assign** method.

1\. Customize the **assign** method.

function assign(target: Record<string, Object>, ...source: Object\[\]): Record<string, Object> {
  for (const items of source) {
    for (const key of Object.keys(items)) {
      target\[key\] = Reflect.get(items, key)
    }
  }
  return target;
}

2\. Use the **assign** method.

interface IMergeSub {
  testString: string,
  testObject?: IMergeSub,
  testArray?: Array<number>
}

interface IMerge {
  a: IMergeSub,
  b: IMergeSub\[\],
  c: string\[\],
  d: number
}

export function testAssign() {
  let objectOne: IMerge =
    {
      a: {
        testString: 'objectOne-a-testString',
        testObject: {
          testString: 'objectOne-a-testObject-testString'
        },
        testArray: \[1\]
      },
      b: \[{
        testString: 'objectOne-b-testString',
        testObject: {
          testString: 'objectOne-b-testObject-testString'
        },
        testArray: \[2\]
      }\],
      c: \['objectOne-c'\],
      d: 3
    }

  let objectTwo: Record<string, Object> = {
    'a': 'objectTwo-a',
    'c': \['objectTwo-c'\],
    'e': 1
  }

  let objectThree: Record<string, Object> = {
    'f': \['objectThree-f'\]
  }

  // Merge multiple objects, and the properties of both Object One and Object Two will be attached to Object Three. When the property names are the same, the properties of the object with the lower index will overwrite the properties of the previous object
  const multiObjectMerged = assign(objectThree, objectTwo, objectOne);
  console.log('multiObjectMerged is:' + JSON.stringify(multiObjectMerged));
  console.log('objectThree is:' + JSON.stringify(objectThree));

  // Merge the properties of Object One into Object Two, and the value of Object Two will change. When the property names are the same, Object One will overwrite the properties of Object Two
  const objectMerged = assign(objectTwo, objectOne);
  console.log('objectTwo is:' + JSON.stringify(objectTwo));
  console.log('objectMerged is:' + JSON.stringify(objectMerged));
}
