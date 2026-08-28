# How do I implement anonymous inner classes?

ArkTS does not support anonymous classes. Use nested classes instead. The type of an object created using an anonymous class is unknown. This conflicts with ArkTS's lack of support for structural typing and the type of object literals. The sample code is as follows:

class A {
  foo() {
    class B {
      v: number = 123;
    }
    let b = new B();
  }
}

Alternatively, you can write the following code:

export interface AnonymousInnerClass<T> {
  onSuccess: (t: T) => void;
  onFailed: (code: string, reason: string) => void;
}

let AnonymousInnerClassInstance: AnonymousInnerClass<void> = {
  onSuccess: () => {
    console.log('success');
  },
  onFailed: () => {
    console.log('failed');
  }
}
