# What is the multithreading model of the system?

TaskPool APIs support multithreading development. Resident time-consuming tasks can use worker threads, with a maximum limit of 64.

It is recommended that the FFRT thread pool be used on the native side. There is no restriction on pthread.
