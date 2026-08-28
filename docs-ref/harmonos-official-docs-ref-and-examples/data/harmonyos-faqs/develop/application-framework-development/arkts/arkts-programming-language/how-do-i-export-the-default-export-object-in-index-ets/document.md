# How do I export the default export object in Index.ets?

**Symptom**

// src/main/ets/api/AppInterfaces.ets
import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
export default new AppInterfaces() as AppInterfaces;
// Index.ets
export AppInterfaces from './src/main/ets/api/AppInterfaces';

The error message "Cannot find name 'AppInterfaces'." is displayed. <ArkTSCheck>

**Solution**

import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
let test = new AppInterfaces()
export default test;
