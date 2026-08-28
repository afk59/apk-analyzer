# Deleting Data

You can use the [delete()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section1630522892714) method to delete a single object or a group of objects. When deleting data, Cloud DB will delete the corresponding data based on the input object primary key and does not check whether other attributes of the object are consistent with the stored data. The delete operation is atomic. That is, all objects in the list either are deleted successfully or fail to be deleted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/FAJs54v6T1ONM8zGOCFUkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1354C0B08FAA9471E16D2352C9B262E950D5599D62F1DCF609DB9945BF747F78)

-   Objects to be deleted in a batch must belong to the same object type. Otherwise, the delete operation will fail.
-   When calling the data deletion method, there are two ways to return the result: either by returning a **Promise** object or by passing a **callback** object in the parameters. The following example explains the **Promise** approach in detail.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [initialized database access](../initializing-database-access/document.md).

#### Deleting Data

**Sample code:**

When you delete objects, the number of deleted objects will be returned if the deletion succeeds; otherwise, an exception will be thrown.

// If a book is lost, the librarian needs to delete the book from the **BookInfo** table.
async delete() {
  try {
    let book = new BookInfo(); 
    book.id = 3;
    let deleteNum = await databaseZone.delete(book);
    hilog.info(0x0000, 'testTag', \`Succeeded in deleting data, result: ${JSON.stringify(deleteNum)}\`);
  } catch (err) {
    hilog.error(0x0000, 'testTag', \`Failed to delete data, code: ${err.code}, message: ${err.message}\`);
  }
}
