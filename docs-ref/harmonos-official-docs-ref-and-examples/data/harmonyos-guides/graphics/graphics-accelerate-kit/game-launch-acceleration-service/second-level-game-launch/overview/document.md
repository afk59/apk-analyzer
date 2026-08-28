# Overview

The second-level game launch function is supported since version 6.0.0(20).

With the second-level game launch function, your game can switch to a specific game scene upon user exit, and the system automatically creates a memory snapshot for this scene. During the next cold start, if no resources have been updated, your game can launch directly from the memory snapshot, skipping the lengthy loading process and delivering an instant launch and access experience.

#### Basic Concepts

| 
Concept

 | 

Description

 |
| :-- | :-- |
| 

Scene switching

 | 

When a user exits your game, it needs to switch to a specific scene so that the system can automatically create a memory snapshot for the scene. This allows your game to launch directly into the scene upon next cold start as long as there are no resource updates.

Since the game sign-in screen has the advantages of low memory usage and relatively stable running status, you are advised to save the **game sign-in screen** as a memory snapshot upon game exit. This can significantly reduce compatibility issues during the scene switching process.

 |
