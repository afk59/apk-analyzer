# How do I obtain the parameters passed by router.back?

In the **onPageShow** callback method, use the **getParams** method of the **Router** module to obtain the passed parameters. The code snippet is as follows:

class InfoTmp {
  age: number = 0
}

class RouTmp {
  id: object = () => {
  }
  info: InfoTmp = new InfoTmp()
}

const context = AppStorage.get("context") as UIContext;
const params: RouTmp = context.getRouter().getParams() as RouTmp; // Get the parameter object passed
const id: object = params.id // Get the value of the id property
const age: number = params.info.age // Get the value of the age property

**Reference**

[Page Redirection](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#page-redirection)
