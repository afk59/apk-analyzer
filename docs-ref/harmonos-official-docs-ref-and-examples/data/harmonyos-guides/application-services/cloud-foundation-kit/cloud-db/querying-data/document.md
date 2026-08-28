# Querying Data

Cloud DB uses the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query objects and provides various query predicates, such as [equalTo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section9706571488), [notEqualTo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section16955165444812), and [in()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section6276103955110). By using one or more chain query conditions, you can query objects that meet the specific query conditions from a Cloud DB zone, or sort query results or limit the number of returned query results by using the corresponding predicates. For details about query conditions, please refer to [DatabaseQuery](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section76501736191415).

The app directly queries data from the server in the Cloud DB zone on the cloud and does not cache data locally.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/yVcqD2LSQDWFXI8WkJbCmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA1CB594F94CA6D1E5B978D389D92DDDD74B81D69863F817A1633DB5CB0ED2FD)

-   You can query the data of only one object type at a time.

-   When calling the data query method, there are two ways to return the result: either by returning a **Promise** object or by passing a **callback** object in the parameters. The following example explains the **Promise** approach in detail.

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [initialized database access](../initializing-database-access/document.md).

#### Simple Query

You can obtain all objects of an object type when no query conditions are set. You can also specify a query condition to obtain desired objects.

-   Query all data of the **BookInfo** object type.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    async queryAll() {
      try {
        let resultArray = await databaseZone.query(condition);
        hilog.info(0x0000, 'testTag', \`Succeeded in querying data, result: ${JSON.stringify(resultArray)}\`);
      } catch (err) {
        hilog.error(0x0000, 'testTag', \`Failed to query data, code: ${err.code}, message: ${err.message}\`);
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/pcxhKdUtSvmCuiCrtJ-56g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F7070E0517208227697B47B0BA7EE1A1E5DB6B7915E143F55AEE509517EBEC2)
    
    In the future, HiLog needs to be imported from **@kit.PerformanceAnalysisKit**, and this will not be shown in the sample code.
    
-   Asynchronously listen to books with the specified **bookName**.
    
    async queryBook(bookName: string): Promise<BookInfo> {
      try {
        condition.equalTo('bookName', bookName);
        let resultArray = await databaseZone.query(condition);
        let bookInfo = resultArray\[0\];
        hilog.info(0x0000, 'testTag', \`Succeeded in querying data, result: ${JSON.stringify(resultArray)}\`);
        return Promise.resolve(bookInfo);
      } catch (err) {
        hilog.error(0x0000, 'testTag', \`Failed to query data, code: ${err.code}, message: ${err.message}\`);
        return Promise.reject(err);
      }
    }
    

#### Compound Query

You can use multiple chain query conditions to obtain desired objects. By default, multiple chain conditions are connected using the AND operation.

-   Construct query conditions: **bookName** contains **Database** and **price** is higher than 20.0 and lower than 50.0. Then call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books.
    
    condition.contains('bookName', 'Database')
      .greaterThan('price', 20.0)
      .and()
      .lessThan('price', 50.0);
    let resultArray = await databaseZone.query(condition);
    
-   Construct query conditions: **bookName** contains **Database** and **price** is lower than 20.0 or higher than 50.0. Then call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books.
    
    condition.contains('bookName', 'Database')
      .lessThan('price', 20.0)
      .or()
      .greaterThan('price', 50.0);
    let resultArray = await databaseZone.query(condition);
    
-   Construct query conditions: **bookName** contains **A Tale of Two Cities**, **author** is **Charles Dickens**, and **price** is higher than 60.0. Then call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books.
    
    condition.contains('bookName', 'A Tale of Two Cities')
             .equalTo('author', 'Charles Dickens')
      .greaterThan('price', 60.0);
    let resultArray = await databaseZone.query(condition);
    
-   Construct query conditions: **bookName** contains **Autobiography**, **author** is **William Shakespeare** or **Charles Dickens**, and **price** is higher than 60.0. Then call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books.
    
    condition.contains('bookName', 'Autobiography')
      .beginGroup()
             .equalTo('author', 'William Shakespeare')
      .or()
             .equalTo('author', 'Charles Dickens')
      .endGroup()
      .greaterThan('price', 60.0);
    let resultArray = await databaseZone.query(condition);
    
-   Construct query conditions: **bookName** contains **Database** and **borrowerTime** is within a specified period. Then call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books. When building query conditions for Date-type fields (for example, when using **greaterThan()**, **greaterThanOrEqualTo()**, **lessThan()**, **lessThanOrEqualTo()**, **equalTo()**, or **notEqualTo()**), you need to call the **getTime()** method to convert the Date object into a number.
    
    let begin = (new Date("2025-12-29T08:00:00.000+08:00")).getTime();
    let end = (new Date("2025-12-31T08:00:00.000+08:00")).getTime();
    condition.contains('bookName', 'Database')
      .greaterThan('borrowerTime', begin)
      .and()
      .lessThan('borrowerTime', end);
    let resultArray = await databaseZone.query(condition);
    

#### Sorting Data

You can use [orderByAsc()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section0344144315513) or [orderByDesc()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section1754544435111) to sort the objects in the query result set in ascending or descending order by a certain field. The sorting predicate must be placed after other query predicates and before the predicate that limits the number of returned query results.

condition.lessThan('price', 50.0)
  .orderByDesc('price');
let resultArray = await databaseZone.query(condition);

#### Random Query

From version 6.0.1(21), the random query function is supported.

You can use [orderByRandom()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section19149641220) to display objects in the query result set in random order.

This method applies to scenarios such as recommending random content or playing random audio and video.

condition.orderByRandom()
  .limit(10);
let resultArray = await databaseZone.query(condition);

#### Limiting the Number of Returned Query Results

During data query, you can use [limit()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section9232724175819) to limit the start position and number of query results to be returned, implementing data pagination. For example, use it together with the sorting query predicate to obtain top _N_ data records.

To limit the number of returned query results, the limiting predicate should be placed after all other query predicates.

-   Construct query conditions and call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method. Here, books cheaper than 50.0 are queried, and only the first 10 records are displayed.
    
    condition.lessThan('price', 50.0)
      .limit(10);
    let resultArray = await databaseZone.query(condition);
    
-   Construct query conditions, call the [query()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section390417613213) method to query books, and sort the query results in descending order of price. Here, books cheaper than 50.0 are queried, and only 10 records from the sixth record are displayed.
    
    condition.lessThan('price', 50.0)
      .orderByDesc('price')
      .limit(10, 6);
    let resultArray = await databaseZone.query(condition);
    

#### Performing Calculations Based on the Query Result

When querying data, you can use [calculateQuery()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section1248132432017) to perform arithmetic calculation on a field in the query result object and return the calculation result.

Construct query conditions and call the [calculateQuery()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-clouddatabase#section1248132432017) method to query all books cheaper than 50.0 and calculate the average price of these books.

async calculateQuery() {
  try {
    condition.lessThan('price', 50.0);
    let resultNum = await databaseZone.calculateQuery(condition, 'price', cloudDatabase.QueryCalculate.AVERAGE);
    hilog.info(0x0000, 'testTag', \`Succeeded in calculating queried data, result: ${JSON.stringify(resultNum)}\`);
  } catch (err) {
    hilog.error(0x0000, 'testTag', \`Failed to calculate queried data, code: ${err.code}, message: ${err.message}\`);
  }
}
