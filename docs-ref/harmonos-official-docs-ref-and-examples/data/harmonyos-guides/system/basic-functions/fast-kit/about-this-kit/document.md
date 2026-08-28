# About This Kit

Fast Algorithms Supported by Theory (FAST) Kit provides algorithm acceleration capabilities for developers, built on the foundations of theoretical computer science (TCS). It currently exposes the Segment Map and Rectangular Partition Solver APIs to improve the app development experience and user experience.

Currently, FAST Kit includes the following functional domains:

-   Advanced Data Structure: It's designed to integrate advanced data structures backed by theoretical guarantees from TCS with modern hardware architectures. Currently, the [Segment Map Data Structure](../using-segmentmap-to-query-and-maintain-range-information/document.md) is provided.
-   Solver: It aims to apply the optimization capabilities from TCS and operations research (OR) to various scenarios in the HarmonyOS ecosystem. Currently, the [Rectangular Partition Solver](../using-rectpartition-to-solve-the-rectangular-partition-problem/document.md) is provided.

#### Use Cases

Grounded in TCS, FAST Kit leverages algorithmic optimization to provide acceleration capabilities that enhance app performance, computational workload management, and power efficiency. Currently, it offers the Advanced Data Structure (Segment Map) and Solver (Rectangular Partition Solver).

-   The Segment Map is a data structure designed for efficient management of interval information, supporting rapid range updates and queries on data sequences. Here are some typical use cases:
    -   Data visualization: Quickly responds to user requests for marking specific prices or time intervals in stock candlestick charts; efficiently renders the time intervals of a large number of tasks in Gantt charts or timelines.
    -   Resource monitoring and log analysis: Records the time intervals during which stutters or exceptions occur in app performance monitoring, facilitating aggregate analysis on time periods with high-frequency issues; tracks continuous dwell-time intervals on specific pages to analyze user behavior patterns.
    -   Game development: Manages multiple continuously effective skills or states in a game to check for overlaps or conflicts; projects objects onto axes as intervals to rapidly filter potential collision candidates.
-   The Rectangular Partition Solver is used to solve the rectangular partition problem. It takes a set of non-overlapping rectangles as input and computes a rectangular partitioning scheme to generate a minimum number of rectangles that cover the same total area. Here are some typical use cases:
    -   UI rendering and layout optimization: Merges the backgrounds of multiple adjacent UI controls into fewer viewport rectangles to reduce GPU drawing calls; merges the rendering areas of adjacent items in the virtual list to reduce the number of DOM elements or views.
    -   Game development: Merges adjacent terrains or passable areas to optimize collision detection; merges adjacent lighting impact areas to simplify lighting calculation.
    -   Document and table processing: Automatically merges adjacent cells of the same format in table applications; automatically merges multiple text labeling areas selected by a user into continuous areas.

#### Basic Concepts

Opaque configuration: An ABI-stable configuration abstraction mechanism where a library forward-declares configuration objects as incomplete types. External code interacts with these objects solely through pointer handles. Since the size, field layout, and interpretation rules are defined entirely within the library, the implementation details are fully decoupled from the caller. This ensures that the storage format and semantics can be modified in future versions without breaking binary compatibility.

#### Constraints

## Supported Countries and Regions

Currently, this kit is available only in the Chinese mainland.

## Supported Devices

Phones, tablets, and PCs/2-in-1 devices.

#### Emulator Support

This kit supports the Emulator, but there are some differences in feature support between real devices and the Emulator. For details, please refer to [Differences Between the Emulator and the Real Device](../../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section1227613205203).
