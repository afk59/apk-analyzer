# PreviewChecker Inspection Rules

When DevEco Studio initiates a preview, an inspection by PreviewChecker will be executed. The preview can proceed only after the inspection is passed, which ensures that known scenarios that do not support previewing are identified before using the Previewer. If there are scenarios that do not support previewing, optimization suggestions will be provided.

#### @previewer/mandatory-default-value-for-local-initialization

For all components to be previewed, attributes that can be initialized locally must have a valid, runtime-independent default value. This is to ensure that the component can be rendered properly in cases of a missing or incomplete input parameter.

Example of incorrect code:

@Entry
@Component
struct Index {
  message?: string;
  @BuilderParam myBuilder: () => void;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}

Example of correct code:

@Builder function MyBuilderFunction(): void {}

@Entry
@Component
struct Index {
  message?: string = 'message';
  @Provide messageA: string = 'messageA';
  @StorageLink('varA') varA: number = 2;
  @StorageProp('languageCode') lang: string = 'en';
  @LocalStorageLink('PropA') storageLink1: number = 1;
  @LocalStorageProp('PropB') storageLink2: number = 2;
  @BuilderParam myBuilder: () => void = MyBuilderFunction;

  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}

#### @previewer/no-unallowed-decorator-on-root-component

Direct preview of child components that contain the @Consume, @Link, @ObjectLink, or @Prop decorator is not allowed. Create a parent component with complete, valid, and runtime-independent default values, and use this parent component to inspect the preview effect of the child components.

Example of incorrect code:

@Preview
@Component
struct LinkSample {
  @Link message: string;

  build() {
    Row() {
      Text(this.message)
    }
  }
}

Example of correct code:

@Entry
@Component
struct LinkSampleContainer {
  @State message: string = 'Hello World';

  build() {
    Row() {
      LinkSample({message: this.message})
    }
  }
}
 
@Component
struct LinkSample {
  @Link message: string;

  build() {
    Row() {
      Text(this.message)
    }
  }
}

#### @previewer/paired-use-of-consume-and-provide

This rule ensures that a component using @Consume can obtain valid values during preview. Without the corresponding @Provide definition, the @Consume component will fail to retrieve any valid value when previewed.

For API version 19 and earlier, @Consume-decorated variables do not support default values. Ensure that their ancestor components provide the corresponding @Provide property with a valid default value independent of runtime execution.

Since API version 20, @Consume-decorated variables support default values. You are advised to set default values for @Consume-decorated variables, or follow the implementation for API version 19 and earlier.

Example of incorrect code:

@Entry
@Component
struct Parent {
  build() {
    Column() {
      Child()
    }
  }
}
 
@Component
struct Child {
  @Consume message: string;
 
  build() {
    Text(this.message)
  }
}

Example 1 of correct code:

// Recommended for API version 20 and later.
@Entry
@Component
struct Parent {
  @Consume message: string = 'hello world';
  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
    }
  }
}

Example 2 of correct code:

// Applicable to all versions.
@Entry
@Component
struct Parent {
  @Provide message: string = 'hello world';
 
  build() {
    Column() {
      Child()
    }
  }
}
 
@Component
struct Child {
  @Consume message: string;
 
  build() {
    Text(this.message)
  }
}

#### @previewer/no-page-method-on-preview-component

Page methods such as **onPageShow** can be used only on @Entry decorated components. Page methods such as **onPageShow**, **onPageHide**, and **onBackPress** are only effective for @Entry decorated components. Instantiating them on non-routing components is not allowed.

Example of incorrect code:

@Preview
@Component
struct Index {
  @State message: string = 'Hello World';

  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}

  build() {
    Column() {
      Text(this.message)
    }
  }
}

Example of correct code:

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}

  build() {
    Column() {
      Text(this.message)
    }
  }
}

#### @previewer/no-page-import-unmocked-hsp

HSP modules must be mocked so that the interfaces in them can be properly initialized in the Previewer. If a page or component has any unmocked HSP module imported, it may not be rendered correctly in the preview. Components to be previewed and their dependencies should avoid referencing HSPs where possible. If an HSP must be referenced, a mock implementation should be provided. For more details on mock implementations, see [Mocking Preview Data](../mocking-preview-data/document.md).

Example of incorrect code:

import { add } from 'library'; // The module is not mocked.

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Text(this.message)
        .onClick(() => add(1, 2))
    }
  }
}

Example of correct code:

import { add } from 'library'; // The module is not mocked. For details about the mocking configuration, see the following code.

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Text(this.message)
        .onClick(() => add(1, 2))
    }
  }
}

Custom mocking configuration:

// src/mock/mock-config.json5
{
  "library": {
    "source": "src/mock/myhsp.mock.ets"
  },
}

// src/mock/myhsp.mock.ets
export function add(a: number, b: number): number {
  return a + b;
}
