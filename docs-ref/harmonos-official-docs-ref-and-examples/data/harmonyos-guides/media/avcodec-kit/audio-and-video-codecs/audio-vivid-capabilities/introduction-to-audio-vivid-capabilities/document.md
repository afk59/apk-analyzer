# Introduction to Audio Vivid Capabilities

Audio Vivid is the world's first AI-driven audio codec standard. It is jointly formulated and released by the UHD World Association (UWA) and the Audio Video Coding Standard Working Group (AVS). This audio format contains audio Pulse-Code Modulation (PCM) data and metadata, offering a more immersive listening experience over traditional stereo sources. Audio Vivid contains metadata information of audio content sources, which can reproduce the true auditory sensations of the physical and perceptual world.

HarmonyOS builds a full-link HD spatial audio system that provides key capabilities such as Audio Vivid codec and spatial audio rendering algorithms. It gradually builds all-scenario spatial audio features on a variety of devices, upgrading from traditional stereo to 3D sound. This upgrade not only enhances the audio quality but also deepens the listener's spatial immersion.

HarmonyOS supports the playback of audio sources in Audio Vivid format and implements binaural spatial audio rendering and playback on headphones. It also supports spatial audio rendering and playback on mobile phones, tablets, PCs, and other devices with external speakers. The system's spatial audio rendering capabilities are seamlessly integrated, eliminating the need for specific adaptation.

With HarmonyOS HD spatial audio rendering capabilities, the human voice and various instrumental sounds in music are treated as independent sound objects, and their positions, movement tracks, volume levels, and distance are redefined to create a comprehensive surround sound experience for the listener, both around and above them. This enhances the spatial audio immersion, providing a sense of presence and artistic experience akin to being in a cinema or concert hall. The experience is further enhanced by using headphones with head tracking capabilities, which allows for dynamic sound repositioning relative to the listener's head movements, thus recreating a lifelike sense of presence.

This document describes how to use HarmonyOS to play audio files in Audio Vivid format from end to end.

The complete playback process includes calling the system codec capabilities for [demultiplexing](../audio-vivid-demultiplexing/document.md) and [decoding](../audio-vivid-decoding/document.md), and calling the system playback capabilities for [rendering and playback](../audio-vivid-playback/document.md).
