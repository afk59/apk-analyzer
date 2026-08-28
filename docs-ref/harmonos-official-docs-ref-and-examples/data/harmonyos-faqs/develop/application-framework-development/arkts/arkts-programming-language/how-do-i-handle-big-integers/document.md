# How do I handle big integers?

Use **BigInt** to handle big integers.

**BigInt** can represent an integer of any size. When using **BigInt**, you need to append the suffix **n** to the integer literal or use the **BigInt()** constructor.

Refer to the code snippet below.

@Entry
@Component
struct BigIntNum {
  build() {
    Row() {
      Column() {
        Button('BigInt num')
          .onClick(() => {
            let bigIntNum: bigint = 12345678901234567890n; // Add n suffix after integer
            let anotherBigInt: bigint = BigInt(9007199254740992); // Use BigInt() constructor
            let sumBigInt: bigint = bigIntNum + anotherBigInt;
            console.info('bigIntNum:' + bigIntNum);
            console.info('anotherBigInt:' + anotherBigInt);
            console.info('bigIntNum + anotherBigInt:' + sumBigInt);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
