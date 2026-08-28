# Service Updates Parameters

#### Service Updates Sending Scenarios

| 
Scenario

 | 

Scenario ID (sceneId)

 | 

Subscenario

 | 

Subscenario ID (subSceneId)

 | 

Remarks

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Takeout

 | 

10001

 | 

Takeout self-pickup

 | 

100010001

 | 

Self-pickup subscenario under the takeout scenario.

 |
| 

Takeout delivery

 | 

100010002

 | 

Delivery subscenario under the takeout scenario.

 |

#### Takeout Self-Pickup Structure

## Parameters of TimelineStatusContent

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

status

 | 

Integer

 | 

Subscenario status in a specified scenario for service updates. For example, for the "Pending payment" status in the takeout self-pickup subscenario under the takeout scenario, the value of **status** is **1**. For details about the parameter values, please refer to [Requirements for Sending Service Updates Parameters in Specified States](#section323244401911).

The options are as follows:

-   **1**: pending payment
-   **2**: order placed
-   **3**: in preparation
-   **4**: ready for pickup
-   **5**: order completed
-   **6**: order canceled

NOTICE:

Send requests based on the mandatory parameter and optional parameter requirements in different states.

 |
| 

orderTime

 | 

Long

 | 

Time when an order is placed. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

amount

 | 

String

 | 

Amount, including the currency. The value is provided by a merchant. The value contains a maximum of 16 characters. Example: $20.00

 |
| 

productCount

 | 

Integer

 | 

Product quantity. The value ranges from 0 to 2147483647.

 |
| 

productName

 | 

String

 | 

Product name. The value contains a maximum of 256 characters.

 |
| 

productImg

 | 

String

 | 

Image SKU ID, which is a unique resource ID allocated by the system for merchant image hosting. You need to provide an image to [apply for the permission](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section592010820304) and obtain the image SKU ID. The value contains a maximum of 128 characters. Example: Image\_001

NOTE:

To change or add an image, you need to provide the image to [apply for image resource hosting](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section19921168203013) and obtain the SKU ID again.

 |
| 

merchantName

 | 

String

 | 

Merchant name. The value contains a maximum of 256 characters.

 |
| 

paymentEndTime

 | 

String

 | 

Payment end time. The value contains a maximum of 32 characters. Example: Please pay before 17:15.

 |
| 

remainOrders

 | 

String

 | 

Number of orders to be prepared. The value contains a maximum of 16 characters. Example: 3 orders/5 cups

 |
| 

pickupNumber

 | 

String

 | 

Pickup number. The value contains a maximum of 16 characters. Example: 1234

 |
| 

pickupTime

 | 

String

 | 

Expected pickup time. The value contains a maximum of 32 characters. Example: 14:00

 |
| 

waitTime

 | 

String

 | 

Estimated waiting time. The value contains a maximum of 16 characters. Example: 20-30 minutes

 |
| 

cancelTime

 | 

Long

 | 

Time when an order is canceled. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

cancelReason

 | 

String

 | 

Cancellation reason. The value contains a maximum of 256 characters.

 |
| 

clickAction

 | 

[ClickAction](#section983132018251) Object

 | 

Action to be triggered upon widget tapping. For details, please refer to [ClickAction](#section983132018251).

 |
| 

button

 | 

[ClickAction](#section983132018251) Object

 | 

Action to be triggered upon widget button tapping. For details, please refer to [ClickAction](#section983132018251).

 |
| 

appendButtons

 | 

Array \[[ClickAction](#section983132018251)\]

 | 

List of actions to be triggered upon button tapping on the retention page. For details, please refer to [ClickAction](#section983132018251).

 |

## Requirements for Sending Service Updates Parameters in Specified States

| 
Status

 | 

Description

 | 

Status Node Type

 | 

Mandatory Parameters

 | 

Optional Parameters

 | 

Remarks

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

1

 | 

Pending payment

 | 

Start node

 | 

status

paymentEndTime

amount

productImg

productCount

productName

merchantName

orderTime

clickAction

 | 

button

appendButtons

 | 

Service updates messages must start with the start node.

 |
| 

2

 | 

Order placed

 | 

Start node

 | 

status

pickupTime

amount

productName

merchantName

productImg

productCount

orderTime

clickAction

 | 

pickupNumber

button

appendButtons

 | 

Service updates messages must start with the start node.

 |
| 

3

 | 

In preparation

 | 

Intermediate node

 | 

status

pickupNumber

amount

productName

merchantName

productImg

productCount

orderTime

clickAction

remainOrders

 | 

button

appendButtons

waitTime

pickupTime

 | 

\-

 |
| 

4

 | 

Ready for pickup

 | 

Intermediate node

 | 

status

pickupNumber

amount

productName

merchantName

productImg

productCount

orderTime

clickAction

 | 

button

appendButtons

 | 

\-

 |
| 

5

 | 

Order completed

 | 

End node

 | 

status

amount

productName

merchantName

productImg

productCount

orderTime

clickAction

 | 

pickupNumber

button

appendButtons

 | 

Service updates end state. After an order is completed, the end state information must be pushed.

 |
| 

6

 | 

Order canceled

 | 

End node

 | 

status

amount

productName

merchantName

productImg

productCount

orderTime

cancelReason

cancelTime

clickAction

 | 

button

appendButtons

 | 

Service updates end state. After an order is canceled, the end state information must be pushed.

 |

#### Takeout Delivery Structure

## Parameters of TimelineStatusContent

| 
Parameter

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

status

 | 

Integer

 | 

Subscenario status in a specified scenario for service updates. For example, for the "In preparation" status in the takeout delivery subscenario under the takeout scenario, the value of **status** is **3**. For details about the parameter values, please refer to [Requirements for Sending Service Updates Parameters in Specified States](#section14839531235).

The options are as follows:

-   **1**: pending payment
-   **2**: order placed
-   **3**: in preparation
-   **4**: ready for pickup
-   **5**: rider accepted order
-   **6**: rider on the way to store
-   **7**: rider arrived at store
-   **8**: delivery in progress
-   **9**: delivered
-   **10**: order completed
-   **11**: order canceled

NOTICE:

Send requests based on the mandatory parameter and optional parameter requirements in different states.

 |
| 

amount

 | 

String

 | 

Amount. The value contains a maximum of 16 characters. Example: $20.00

 |
| 

paymentEndTime

 | 

String

 | 

Payment end time. The value contains a maximum of 32 characters. Example: Please pay before 17:15.

 |
| 

productImg

 | 

String

 | 

Image SKU ID, which is a unique resource ID allocated by the system for merchant image hosting. You need to provide an image to [apply for the permission](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section592010820304) and obtain the image SKU ID. The value contains a maximum of 128 characters. Example: Image\_001

NOTE:

To change or add an image, you need to provide the image to [apply for image resource hosting](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section19921168203013) and obtain the SKU ID again.

 |
| 

productCount

 | 

Integer

 | 

Product quantity. The value ranges from 0 to 2147483647.

 |
| 

productName

 | 

String

 | 

Product name. The value contains a maximum of 256 characters.

 |
| 

merchantName

 | 

String

 | 

Merchant name. The value contains a maximum of 256 characters.

 |
| 

customerAddress

 | 

String

 | 

Delivery address. The value contains a maximum of 256 characters.

 |
| 

orderTime

 | 

Long

 | 

Time when an order is placed. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

deliveryTime

 | 

String

 | 

Estimated delivery time. The value contains a maximum of 32 characters. Example 18:10

 |
| 

waitTime

 | 

String

 | 

Estimated waiting time. The value contains a maximum of 16 characters. Example: 20-30 minutes

 |
| 

realDeliveryTime

 | 

Long

 | 

Actual delivery time. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

remainOrders

 | 

String

 | 

Number of orders to be prepared. The value contains a maximum of 16 characters. Example: 3 orders/5 cups

 |
| 

cancelReason

 | 

String

 | 

Cancellation reason. The value contains a maximum of 256 characters.

 |
| 

cancelTime

 | 

Long

 | 

Time when an order is canceled. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

riderName

 | 

String

 | 

Rider name. The value contains a maximum of 16 characters.

 |
| 

riderReceiveTime

 | 

Long

 | 

Time when a rider accepts an order. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

riderPickupTime

 | 

Long

 | 

Time when a rider picks up products. The value is a timestamp accurate to seconds. Example: 1716867321

 |
| 

takeawayCabinet

 | 

String

 | 

Delivery locker. The value contains a maximum of 256 characters. Example: No.2 grid of delivery locker 1

 |
| 

pickupNumber

 | 

String

 | 

Pickup number. The value contains a maximum of 16 characters. Example: 1234

 |
| 

clickAction

 | 

[ClickAction](#section983132018251) Object

 | 

Action to be triggered upon widget tapping. For details, please refer to [ClickAction](#section983132018251).

 |
| 

button

 | 

[ClickAction](#section983132018251) Object

 | 

Action to be triggered upon widget button tapping. For details, please refer to [ClickAction](#section983132018251).

 |
| 

appendButtons

 | 

Array \[[ClickAction](#section983132018251)\]

 | 

List of actions to be triggered upon button tapping on the retention page. For details, please refer to [ClickAction](#section983132018251).

 |

## Requirements for Sending Service Updates Parameters in Specified States

| 
Status

 | 

Description

 | 

Status Node Type

 | 

Mandatory Parameters

 | 

Optional Parameters

 | 

Remarks

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

1

 | 

Pending payment

 | 

Start node

 | 

status

paymentEndTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

button

appendButtons

 | 

Service updates messages must start with the start node.

 |
| 

2

 | 

Order placed

 | 

Start node

 | 

status

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

deliveryTime

pickupNumber

button

appendButtons

 | 

Service updates messages must start with the start node.

 |
| 

3

 | 

In preparation

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

remainOrders

clickAction

 | 

pickupNumber

button

appendButtons

waitTime

 | 

\-

 |
| 

4

 | 

Ready for pickup

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

5

 | 

Rider accepted order

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

6

 | 

Rider on the way to store

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

7

 | 

Rider arrived at store

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

8

 | 

Delivery in progress

 | 

Intermediate node

 | 

status

deliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

9

 | 

Delivered

 | 

Intermediate node

 | 

status

realDeliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

pickupNumber

button

appendButtons

 | 

\-

 |
| 

10

 | 

Order completed

 | 

End node

 | 

status

realDeliveryTime

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

clickAction

 | 

button

appendButtons

 | 

Service updates end state. After an order is completed, the end state information must be pushed.

 |
| 

11

 | 

Order canceled

 | 

End node

 | 

status

cancelReason

amount

productImg

productCount

productName

merchantName

orderTime

customerAddress

cancelTime

clickAction

 | 

button

appendButtons

 | 

Service updates end state. After an order is canceled, the end state information must be pushed.

 |

#### Common Parameter Structure

## ClickAction

<table><tbody><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>Parameter</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>Mandatory</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>Type</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>Description</p></td></tr><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>type</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>Yes</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>Integer</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>Redirection action to be triggered upon message tapping. The options are as follows:</p><p><strong>0</strong>: Open the home page of the current atomic service.</p><p><strong>1</strong>: Open a specific page of the current atomic service.</p></td></tr><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>text</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>No</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>String</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>Button text. In the button tapping scenario, this parameter is mandatory (no more than four characters).</p></td></tr><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>action</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>No</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>String</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>Action corresponding to the ability of an in-app page. When <strong>type</strong> is set to <strong>1</strong>, either <strong>action</strong> or <strong>uri</strong> must be set. When both <strong>action</strong> and <strong>uri</strong> are set, <strong>uri</strong> is preferentially used to query the in-app page.</p></td></tr><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>uri</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>No</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>String</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>URI corresponding to the ability of an in-app page. When <strong>type</strong> is set to <strong>1</strong>, either <strong>action</strong> or <strong>uri</strong> must be set.</p></td></tr><tr><td class="cellrowborder" valign="top" width="13.950000000000001%"><p>data</p></td><td class="cellrowborder" valign="top" width="14.23%"><p>No</p></td><td class="cellrowborder" valign="top" width="12.15%"><p>Object</p></td><td class="cellrowborder" valign="top" width="59.67%"><p>When <strong>type</strong> is set to <strong>0</strong> or <strong>1</strong>, this parameter is used to transfer data to an atomic service after a button is tapped. The value must be in the key-value format and contains a maximum of 1024 bytes. Example: {"key1": "value1", "key2": "value2"}</p></td></tr></tbody></table>
