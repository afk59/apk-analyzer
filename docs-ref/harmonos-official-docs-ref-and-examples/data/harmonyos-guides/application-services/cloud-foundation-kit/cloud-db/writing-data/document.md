# Writing Data

You can use [upsert()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section686153211276) to write one object or a group of objects to the current Cloud DB zone. If an object with the same primary key exists in the Cloud DB zone, the existing object will be updated. Otherwise, a new object will be written. The written data can be obtained from a new object or an object queried from the Cloud DB zone.

When you write a group of objects, the write operation is atomic. That is, all objects in the object list either are successfully written or fail to be written.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/uMaBa0ctQjWFRUVKcdke1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DBF3216F043AA172A707C2415E52BA5065288CF058B2747DA4BF40B8D0D7C87)

-   Objects to be written in a batch must belong to the same object type. Otherwise, the write operation will fail.
-   When a group of objects are written, the total data size must be less than or equal to 2 MB. Otherwise, the write operation will fail.
-   When a group of objects are written, the total number of data records must be less than or equal to 1000. Otherwise, the write operation will fail.
-   When calling the data writing method, there are two ways to return the result: either by returning a **Promise** object or by passing a **callback** object in the parameters. The following example explains the **Promise** approach in detail.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [initialized database access](../initializing-database-access/document.md).

#### Writing Data

The **Promise** object encapsulates the result of the write operation. You can use the **Promise** object to asynchronously listen to the execution result. If the execution succeeds, you can obtain the number of written objects. Otherwise, you can obtain the error information.

**Sample code:**

Write the **BookInfo** object into the Cloud DB zone. If the write operation succeeds, the number of written data records will be returned. Otherwise, an exception will be thrown.

// Update the borrower information of the _Journey to the West_.
async upsert() {
  try {
    let book = await this.queryBook('Journey to the West'); // Query information related to the _Journey to the West_.
    book.borrowerId = 1;
    book.borrowerName = 'Jim';
    book.borrowerTime = new Date();
    let record = await databaseZone.upsert(book);
    hilog.info(0x0000, 'testTag', \`Succeeded in upserting a book, result: ${JSON.stringify(record)}\`);
  } catch (err) {
    hilog.error(0x0000, 'testTag', \`Failed to upsert a book, code: ${err.code}, message: ${err.message}\`);
  }
}
