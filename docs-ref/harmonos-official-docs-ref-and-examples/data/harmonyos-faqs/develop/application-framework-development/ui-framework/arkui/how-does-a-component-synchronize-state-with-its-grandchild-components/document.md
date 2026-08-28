# How does a component synchronize state with its grandchild components?

-   Method 1 (recommended): Use the @Provider and @Consumer decorators for data binding. In the parent component, use @Provider to provide the state. In the grandchild component, use @Consumer to consume the state and synchronize data.

1.  In the parent component, use @Provider to provide the **reviewVote** parameter, which will be passed down to the grandchild component.
    
    @Entry
    @ComponentV2
    struct Father{
      @Provider("reviewVote") reviewVotes: number = 0;
    
    
      build() {
        Column() {
          Son()
          Button(\`Father: ${this.reviewVotes}\`)
        }
      }
    }
    
2.  Include the grandchild component in the child component.
    
    @ComponentV2
    struct Son{
      build() {
        Column() {
          Grandson()
        }
      }
    }
    
3.  In the grandchild component, use @Consumer to receive the **reviewVote** parameter.
    
    @ComponentV2
    struct Grandson{
      @Consumer("reviewVote") reviewVotes: number = 0;
    
    
      build() {
        Column() {
          Button(\`Grandson: ${this.reviewVotes}\`)
        }.width('100%')
      }
    }
    

-   Method 2: Use the @Local decorator in the parent component, and the @Param decorator in the child and grandchild components.

1.  In the parent component (**Father**), use @Local to bind the **reviewVotes** parameter.
    
    @Entry
    @ComponentV2
    struct Father {
      @Local reviewVotes: number = 0;
    
    
      build() {
        Column() {
          Son({ reviewVotes: this.reviewVotes })
          Button(\`Father: ${this.reviewVotes}\`)
        }
      }
    }
    
2.  In the child component (**Son**), use @Param to receive the **reviewVotes** parameter from the parent component.
    
    @ComponentV2
    struct Son {
      @Require @Param reviewVotes: number = 1;
    
    
      build() {
        Column() {
          Grandson({ reviewVotes: this.reviewVotes })
        }
      }
    }
    
3.  In the grandchild component (**Grandson**), use @Param to receive the **reviewVotes** parameter passed from the child component.
    
    @ComponentV2
    struct Grandson {
      @Require @Param reviewVotes: number = 1;
    
    
      build() {
        Column() {
          Button(\`Grandson: ${this.reviewVotes}\`)
        }.width('100%')
      }
    }
