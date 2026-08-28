# Do ArkTS APIs support overloading?

ArkTS supports overloading in TS, that is, multiple overload signatures + implementation signature. Function signatures are used only for type check during build. They are not retained at runtime.

ArkTS does not support overloading of multiple function bodies. The sample code is as follows:

// declare 
function test(param: User): number; 
function test(param: number, flag: boolean): number; 
// implement 
function test(param: User | number, flag?: boolean) { 
  if (typeof param === 'number') { 
    return param + (flag ? 1 : 0) 
  } else { 
    return param.age 
  } 
}
