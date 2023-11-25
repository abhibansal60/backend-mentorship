## Learning about Patterns

### Attribute Pattern

**When to use ?**

1. When we have big documents with similar fields and there are certain(subset) fields sharing common charachteristics, we want to sort or query on that subset of fields
2. The fields we need to sort are found in the subset of docs
3. Both the above conditions are met

If one of the above conditions is met we can consider Attribute patterns

Understanding [indexes](https://www.mongodb.com/docs/drivers/node/current/fundamentals/indexes/#:~:text=Indexes%20are%20data%20structures%20that,documents%20that%20match%20each%20query.) looks important in MongoDB
    - To improve query performance, build indexes on fields that appear often in your application's queries and operations that return sorted results


The examples and sample use cases are well-defined in the reference link below

_References from:_ https://www.mongodb.com/blog/post/building-with-patterns-the-attribute-pattern


### Bucket Patterns

**When to use ?**

1. Useful when we have to store [time series data](https://www.timescale.com/blog/time-series-data/)

E.g. Instead of storing data to db every minute or second we define a time interval and **bucket together** the data to be stored. This kind of data can be updated at a later stage as well. 

2. It also allows us to perform aggregation (pre-aggregation) of bucketed data.
3. As the information piles up awe can archive then data if retrieval is infrequent.

The examples and sample use cases are well-defined in the reference link below

_References from:_ https://www.mongodb.com/blog/post/building-with-patterns-the-bucket-pattern

### Extended Reference Pattern

**When to use ?**

1. When you have different entities(collections) talk to each other to provide meaningful information.
2. Performance can take a hit in if point 1 is true (As different kind of relations can exist JOINS, 1-N, N-N, N-1 etc.)
   
Note: In this pattern, instead of doing regular joins, some of that most frequently used **attributes among the collections are duplicated**, With duplication the problem of consistency may also arise so special care has to be taken choosing the attributes/fields.
The Extended Reference pattern is a wonderful solution when your application is experiencing many repetitive JOIN operations. It helps to keep data together and help to perform faster read operations

The examples and sample use cases are well-defined in the reference link below

_References from:_ https://www.mongodb.com/blog/post/building-with-patterns-the-extended-reference-pattern


Summary of the patterns can be found [here](https://www.mongodb.com/blog/post/building-with-patterns-a-summary)

### Polymorphic Pattern

**When to use ?**

1. When we have similar looking but not identical data We can go for this pattern.

It can be used for something like product catalogs

The examples and sample use cases are well-defined in the reference link below

_References from:_ https://www.mongodb.com/developer/products/mongodb/polymorphic-pattern/ 


### Tree Pattern

**When to use ?**

1. When there is a hierarchical relation between the entities.

This can also be used for product catalogs, adding product to a category, which can itself be a sub category 

_References from:_ https://www.mongodb.com/blog/post/building-with-patterns-the-tree-pattern
