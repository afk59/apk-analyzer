# Overview

When an app needs to obtain a user's risk level, it can use the user risk level retrieval capability provided by Account Kit to implement the following:

1.  App sign-in risk control: When the app is signed in using a HUAWEI ID, the risk level of the HUAWEI ID can be obtained, enabling protection against high-risk accounts and enhancing the app security.
2.  Marketing fraud prevention: During app marketing campaigns (for example, merchant's subsidies and coupon distribution), HUAWEI ID risk levels can be obtained to detect potential fraud. This safeguards marketing resources from abuse, minimizes financial losses due to security breaches, and ensures campaign effectiveness.

Account Kit provides the following risk levels:

| 
Risk Level

 | 

Description

 | 

Handling Suggestion

 |
| :-- | :-- | :-- |
| 

0

 | 

No obvious risks detected. For example, a user legally registers an account and uses a Huawei phone properly, without engaging in abnormal activities such as performing batch operations, using automation tools, and farming accounts.

 | 

Implement no restrictions on the behavior.

 |
| 

1

 | 

Low risk. Risks are detected and are rated as low risk after overall evaluation.

 | 

Implement simple verification through methods such as verification code and SMS or manual review.

 |
| 

2

 | 

Medium risk. Risks are detected and are rated as medium risk after overall evaluation.

 | 

Implement measures to avoid damage based on the service scenario. For example, reduce the likelihood of high-level rewards in marketing campaigns, downweight votes in ranking campaigns, and require secondary verification for registration and sign-in.

 |
| 

3

 | 

High risk. Risks are detected and are rated as high risk after overall evaluation.

 | 

Intercept the behavior. For example, return no prize or the smallest amount for red envelope campaigns, not count votes for ranking campaigns, require secondary verification for registration or sign-in, or carry out other high-risk operations.

 |
| 

4

 | 

Undetermined. The risk level is undetermined.

 | 

Implement measures based on the historical behavior of the account and the service scenario.

 |
