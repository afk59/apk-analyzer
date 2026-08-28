# Does ArkTS support multiple inheritance?

ArkTS supports multiple inheritance for APIs and single inheritance for classes. Refer to the code snippet below.

class TestClassA {
  address: string = '';
}

class TestClassB {
  name: string = '';
}

// report errors: Classes can only extend a single class.
// class TestClassC extends TestClassA, TestClassB {
// }

interface AreaSize {
  calculateAreaSize(): number;
}

interface Cal {
  Sub(a: number, b: number): number;
}

interface Area extends AreaSize, Cal {
  areaName: string;
  length: number;
  width: number;
}
