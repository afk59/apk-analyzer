# Scenario-Specific Message

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/uf0m5Sl7RzWopoSLZ-11GA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B3F1827633FB790C8C7D7E434E5F83E99C02464CF3E0A91570403428251CFB6)

To ensure network security, Push Kit disabled the TLS 1.0 and TLS 1.1 protocols and unapproved cipher suites for related domains on November 30, 2022. As a result, apps using TLS versions earlier than 1.2 or unapproved cipher suites were no longer able to send push messages.

If your app accesses related domains using TLS 1.0 or 1.1, message sending may fail. Ensure that your environment is upgraded to TLS 1.2 or later.

-   **[Function](function/document.md)**  
    
-   **[Request Body Structure](request-body-structure/document.md)**  
    
-   **[Request Body Parameters](request-body-parameters/document.md)**  
    
-   **[Response Parameters](response-parameters/document.md)**  
    
-   **[Request Examples](request-examples/document.md)**  
    
-   **[Message Frequency Control](message-frequency-control/document.md)**
