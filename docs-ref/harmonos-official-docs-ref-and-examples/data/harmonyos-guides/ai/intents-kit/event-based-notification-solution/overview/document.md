# Overview

An event-based notification is proactively pushed to users when updates that meet certain notification criteria occur in an app or atomic service. To implement event-based notifications, you need to share event information with Intents Kit. When the notification push criteria are met, a widget will be displayed to specified users through Celia Suggestions. In addition, users can also query the event content and status by voice input or keyword search.

Events are classified into user events and public events based on whether user IDs are specified.

**User events**: triggered by user behavior. Notifications are pushed to one or more specified users based on the user ID. For example, when a user purchases a coupon, the nearby discount service sends this event to the smart distribution platform. Intents Kit then notifies the user that the coupon is about to expire _X_ days before the expiration date.

**Public events**: If no user ID is specified, notifications will be pushed to users with the same characteristics. For example, the meteorological bureau shares a typhoon warning event with Intents Kit, which will push a typhoon warning to users who may be affected three days before the typhoon arrives. Notifications related to public events include disaster or fault warnings, program schedules, and sports event arrangements.
