# How to Calculate the Validity Period for New Subscriptions upon Immediate Switch of Auto-Renewable Subscriptions?

When a subscription switch (from A to B) takes effect immediately, the remaining value of the original subscription's entitlement is automatically prorated and added to the new subscription. Therefore, the new subscription's validity period is determined by adding the prorated time derived from the original subscription's remaining entitlement to the new subscription's standard cycle duration.

For example, a user first purchased Subscription A (Standard Membership, CNY20/30 days). After using it for 15 days, they switch to Subscription B (Premium Membership, CNY60/30 days) within the same subscription group. At the time of the switch, the remaining entitlement of Subscription A is automatically prorated and converted into 5 days of validity for Subscription B. Therefore, the total validity period for Subscription B after the switch is 35 days, which is the sum of the 5 days granted from the prorated remaining entitlement of Subscription A and the new subscription's standard 30-day cycle.

The timeline (MM/dd) is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/y1_-NfevR6ubMKEOPCatDw/en-us_image_0000002510827043.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6166E91C8E1BEF701EBF2F1A21801E28DF5DC9F1D0F2683E196B8BF92210DE4D)

In the sandbox environment, the equivalent timeline (hh:mm:ss) is as follows, based on a conversion rate of 1 day in the production environment to 10 seconds in the sandbox environment:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iCzvF0xvRaGQepQKldahfA/en-us_image_0000002478627636.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C20D4B57EDDE154619C3A887EE37A81E2A1051832571FDAA1F31CCAE9D68FE77)
