# ContentType Scenarios

HUAWEI ID nickname

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

NICKNAME

 | 

Nickname, for example, Vivian.

 |

User name

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

PERSON\_FULL\_NAME

 | 

Full name, for example, John Smith.

 |
| 

PERSON\_LAST\_NAME

 | 

Last name, for example, Smith.

 |
| 

PERSON\_FIRST\_NAME

 | 

First name, for example, John.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/nf4h58t1Qti6WA68fAHIbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09FDCF9F44E7E7D5F16AAF6687CC3A8F062CB5DFDACAAC40514B83D925F483A9)

-   **PERSON\_FULL\_NAME** and the combination of **PERSON\_LAST\_NAME** and **PERSON\_FIRST\_NAME** cannot be used in the same form at the same time, except the scenario of passport information filling.
-   When collecting sensitive user data, you must clearly state the purpose and necessity of the request directly on the form page.

Contact information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

PHONE\_NUMBER

 | 

Mobile number, for example, 188\*\*\*\*\*\*88.

 |
| 

EMAIL\_ADDRESS

 | 

Email address, for example, a\*\*\*\*t@huawei.com.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/klEPCBaOQwesbdJ033v8WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B73CF4A701C38AAE0C24D9420A71B98089AF05A60C8D3E0CE6CE068CCD6C3090)

When collecting sensitive user data, you must clearly state the purpose and necessity of the request directly on the form page.

Identity information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

ID\_CARD\_NUMBER

 | 

ID card number, for example, 3201\*\*\*\*\*\*\*\*\*\*\*123.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/j5AjtY5xS0azXOkdi_CXBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77EA3FA9BAAF54F666BD0495CD96214D96CE20F851C11E8D41916C9F51D0B7A0)

**ID\_CARD\_NUMBER** currently supports suggestions and auto-filling only for ID card numbers. To support other certificates, you need to [dynamically change the value of ContentType](../changing-the-value-of-contenttype-dynamically/document.md) for input boxes based on your needs.

Passport information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

COUNTRY\_ADDRESS

 | 

Nationality, for example, **China**.

 |
| 

PASSPORT\_NUMBER

 | 

Passport number, for example, **G\*\*\*\*\*\*\*1**.

 |
| 

VALIDITY

 | 

Expiration date, for example, **2025-1-1**.

 |
| 

ISSUE\_AT

 | 

Place of issue, for example, **Guangdong**.

 |

License plate information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

LICENSE\_PLATE

 | 

License plate number, for example, **A\*\*\*\*\*1**.

 |

Address information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

FULL\_STREET\_ADDRESS

 | 

Detailed address with street information, for example, No. 98 Yulan Road, Yuhua Street.

 |
| 

FORMAT\_ADDRESS

 | 

Full address, for example, No.98 Yulan Road, Yuhua Street, Yuhuatai District, Nanjing City, Jiangsu Province, China.

 |
| 

DETAIL\_INFO\_WITHOUT\_STREET

 | 

Detailed address without street information, for example, No. 98 Yulan Road.

 |
| 

ADDRESS\_CITY\_AND\_STATE

 | 

Region, for example, Longgang District, Shenzhen, People's Republic of China.

 |

Invoice title information

| 
Parameter

 | 

Description

 |
| :-- | :-- |
| 

ORGANIZATION

 | 

Organization name, for example, **Shenzhen XX Co., Ltd**.

 |
| 

TAX\_ID

 | 

Tax ID, for example, **2020\*\*\*\*\*\*\*\*\*\*\*000**.

 |
