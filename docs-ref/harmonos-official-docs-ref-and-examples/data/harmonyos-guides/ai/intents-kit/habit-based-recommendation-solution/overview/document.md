# Overview

Habit-based recommendation is a proactive prediction and recommendation made by HarmonyOS after learning users' behavior habits.

1.  You can share users' behavior in your app or atomic service with HarmonyOS so that HarmonyOS can learn users' behavior patterns based on the shared data.
2.  After HarmonyOS learns users' behavior patterns, it will recommend relevant features and attempt to provide detailed parameters to reduce the steps required for users to complete tasks.

Take listening to music as an example. Intents Kit has designed a unified intent—the playlist playing intent, which allows apps or atomic services to interact with HarmonyOS.

When a user plays a playlist using an app or atomic service, the app or atomic service can share this intent with Intents Kit, providing characteristics for learning, such as the start time, end time, playback duration, and playlist name. HarmonyOS will combine such data with collected underlying data, such as time, location, and device status, to understand the user's behavioral context. Finally, HarmonyOS combines the historically shared data from the app or atomic service to reconstruct a task for intent response and perform predictive recommendations. For example, after the user gets into a car every morning, HarmonyOS can recommend a 'Daily recommendation' playlist widget, which the user can play with one tap.
