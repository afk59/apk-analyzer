# How is a callback function defined in ArkTS?

The following is an example:

1.  Define the callback function.
    
    // Define 2 parameters on the page, return empty callback function
    myCallback: (a: number,b: string) => void = () => {}
    
2.  Initialize the callback function by assigning values.
    
    aboutToAppear() {
      // Initialization of callback function
      this.myCallback = (a,b) => {
        console.info(\`handle myCallback a=${a},b=${b}\`)
      }
    }
