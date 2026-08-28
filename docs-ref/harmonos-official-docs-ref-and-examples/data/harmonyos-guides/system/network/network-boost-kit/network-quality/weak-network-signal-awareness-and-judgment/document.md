# Weak Network Signal Awareness and Judgment

Based on [network quality assessment](../network-quality-assessment/document.md) and [network scenario identification](../network-scenario-identification/document.md), weak network signal awareness and judgment can be achieved through the following methods:

**Judgment based on real-time data**:

The device can determine whether the network signal is weak based on the network scenario identification information such as **NetworkScene.scene(weakSignal/congestion)**.

**Judgment based on prediction**:

The device can determine whether the device is about to enter an area where the network signal is weak based on prediction data such as **NetworkScene.weakSignalPrediction** returned during network scenario identification.

**Custom judgment**:

Your app can define a custom threshold for determining whether the network signal is weak based on network quality data such as **NetworkQos(linkUpBandwidth/linkDownBandwidth/rttMs/linkUpBufferDelayMs/linkUpBufferCongestionPercent)**.

You can choose one or more methods for your app based on your service needs.
