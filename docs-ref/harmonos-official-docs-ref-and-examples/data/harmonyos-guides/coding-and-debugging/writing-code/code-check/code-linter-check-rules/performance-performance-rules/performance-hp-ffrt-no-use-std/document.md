# @performance/hp-ffrt-no-use-std

Do not use synchronous APIs such as **std::xxx** in FFRT Worker threads. This rule applies only to C/C++ files.

In concurrency scenarios, modify the code according to this rule whenever possible.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/hp-ffrt-no-use-std": "suggestion",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition\_variable>
#include <unistd.h>
// ffrt header file
#include "ffrt/ffrt.h"
using namespace std;
int N = 100;
int M = 100;

_// std::mutex is used in ffrt::submit._
    void PositiveCase1(int temp) {
    ffrt::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            \[&\]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
_// std::condition\_variable is used in ffrt::submit._
    void PositiveCase2(int temp) {
    ffrt::condition\_variable cond;
    int a = 0;
    ffrt::mutex lock\_;
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<ffrt::mutex> lck(lock\_);
            cond.wait(lck, \[&\] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<ffrt::mutex> lck(lock\_);
            a = 1;
            cond.notify\_one();
        },
        {}, {});
    ffrt::wait();
}
_// std::usleep is used in ffrt::submit._
    void PositiveCase3(int temp) {
    ffrt::submit(
        \[&\]() {
        ffrt\_usleep(100);
        printf("test");
        ffrt\_yield();      
    }, {}, {});
}
_// pthread\_rwlock\_wrlock or pthread\_rwlock\_rdlock is used in ffrt::submit._
    void PositiveCase4(int temp) {
    int a = 0;
    ffrt\_rwlock\_t mtx;
    ffrt::submit(
        \[&\]() {
        int ret = ffrt\_rwlock\_wrlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
        a++;
        ret = ffrt\_rwlock\_unlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
    }, {}, {});
    ffrt::submit(
        \[&\]() {
        int ret = ffrt\_rwlock\_rdlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
        printf("sum is %d\\n", a);
        ret = ffrt\_rwlock\_unlock(&mtx);
        if (ret != ffrt\_success) {
            printf("error\\n");
        }
    }, {}, {});
}

#### Example of Incorrect Code

#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition\_variable>
#include <unistd.h>
// ffrt header file
#include "ffrt/ffrt.h" 
using namespace std;
int N = 100;
int M = 100;
_// std::mutex is used in ffrt::submit._
    void NegativeCase1(int temp) {
    std::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            \[&\]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
_// std::condition\_variable is used in ffrt::submit._
    void NegativeCase2(int temp) {
    std::condition\_variable cond;
    int a = 0;
    std::mutex lock\_;
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<std::mutex> lck(lock\_);
            cond.wait(lck, \[&\] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        \[&\]() {
            std::unique\_lock<std::mutex> lck(lock\_);
            a = 1;
            cond.notify\_one();
        },
        {}, {});
    ffrt::wait();
}
_// std::usleep is used in ffrt::submit._
    void NegativeCase3(int temp) {
    ffrt::submit(
        \[&\]() {
        usleep(100);
        printf("test");
        ffrt\_yield();
    }, {}, {});
}
_// pthread\_rwlock\_wrlock or pthread\_rwlock\_rdlock is used in ffrt::submit._
    void NegativeCase4(int temp) {
    int a = 0;
    pthread\_rwlock\_t mtx;
    ffrt::submit(
        \[&\]() {
        int ret = pthread\_rwlock\_wrlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
        a++;
        ret = pthread\_rwlock\_unlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
    }, {}, {});
    ffrt::submit(
        \[&\]() {
        int ret = pthread\_rwlock\_rdlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
        printf("sum is %d\\n", a);
        ret = pthread\_rwlock\_unlock(&mtx);
        if (ret != 0) {
            printf("error\\n");
        }
    }, {}, {});
}

#### Rule Set

plugin:@performance/recommended

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
