# How do I parse a JSON string as an instance object?

**Question**

JSON data has to be converted into an instance object of an ArkTS class. You can use the properties of the instance object, and call the methods of the instance object. The nested object scenario is also involved.

In this case, you need to use the third-party libraries class-transformer and reflect-metadata (installed using **npm install**). Use @Type to specify the nested type and use **plainToClass** to convert a plain object into the corresponding instance object.

Refer to the sample code below:

import { Type, plainToClass } from 'class-transformer'
import "reflect-metadata"

// Assuming accepted JSON data
let testJSON: Record<string, ESObject> = {
  'id': 1,
  'firstName': "Johny",
  'lastName': "Cage",
  'age': 27,
  'arr': \[
    {
      'name': 'john'
    },
    {
      'name': 'tom'
    }
  \],
  'instanceA': {
    'name': 'john'
  },
}

// If there is a corresponding nested structure, the corresponding type needs to be specified
class A {
  name: string = 'john';

  getName(): string {
    return this.name
  }
}

// When attempting to convert an object with nested objects, it is necessary to know the object type to be converted and use the @ Type decorator to implicitly specify the object type contained in each attribute
class User {
  id: number = 0;
  firstName: string = '';
  lastName: string = '';
  age: number = 0;
  @Type(() => A)
  arr: A\[\] = \[new A()\]
  @Type(() => A)
  instanceA: A = new A();

  getName() {
    return this.firstName + " " + this.lastName;
  }

  isAdult() {
    return this.age > 36 && this.age < 60;
  }
}

@Entry
@Component
struct parsingJSONStringsIntoInstanceObjects {
  aboutToAppear(): void {
    const instance = plainToClass(User, testJSON);
    console.info('instance:' + JSON.stringify(instance))
  }

  build() {

  }
}
