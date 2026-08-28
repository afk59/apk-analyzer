# How do I access static variables and methods of a class?

In ArkTS, static variables and methods belong to the class itself and cannot be accessed through **this**, which points to the class instance. To access static variables and static methods in a class, use the class name.

// Accessing static variables or executing static methods
class TestStatic {
  static aaa: string = '3333';

  static getAAA () {
    // console.log(this.aaa) Static variables cannot be accessed through this and can only be used in static methods
    return TestStatic.aaa;
  }
}
TestStatic.aaa;
