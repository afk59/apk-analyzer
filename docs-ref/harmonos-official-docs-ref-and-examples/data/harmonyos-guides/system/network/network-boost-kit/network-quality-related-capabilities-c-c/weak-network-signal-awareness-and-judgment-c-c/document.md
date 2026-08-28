# Weak Network Signal Awareness and Judgment (C/C++)

Based on [network quality assessment](../network-quality-assessment-c-c/document.md) and [network scenario identification](../network-scenario-identification-c-c/document.md), weak network signal awareness and judgment can be achieved through the following methods:

**Judgment based on real-time data**:

The device can determine whether the network signal is weak based on the network scenario identification information such as **NetworkBoost\_Scene(NB\_SCENE\_WEAK\_SIGNAL/NB\_SCENE\_CONGESTION)**.

**Judgment based on prediction**:

The device can determine whether the device is about to enter an area where the network signal is weak based on prediction data such as **NetworkBoost\_WeakSignalPrediction** returned during network scenario identification.

**Custom judgment**:

Your app can define a custom threshold for determining whether the network signal is weak based on network quality data such as **NetworkBoost\_NetworkQos(linkUpBandwidth/linkDownBandwidth/rttMs/linkUpBufferDelayMs/linkUpBufferCongestionPercent)**.

You can choose one or more methods for your app based on your service needs.
