# Why do navigations through the router fail?

**1\. The page in the HAR file does not use the named route for redirection**

Pages cannot be declared in the configuration file of the HAR file. However, the HAR file can contain pages navigated through named routes. For details, see [Named Route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route).

**2\. Import problem**

Check whether the corresponding page is correctly imported. You can check by referring to the configuration of [named route](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-routing#named-route).
