# Scrap Your ORM

## 1

[Relations](https://en.wikipedia.org/wiki/Relational_model) aren't [objects](<https://en.wikipedia.org/wiki/Object_(computer_science)%3E>).  
Rows aren't objects.  
Tables aren't even objects[^1].  
A relational database (management system) _is_ an object, but **ORMs don't model the entire database**[^2][^3].

## 2

Your database—the database your code is interacting with—is at least a separate process; most commonly, it's running on a completely separate machine.

Your database is an _application_, one that has an _application programming interface_.

This low-level API includes things like escaping content and connection management. There are client libraries written for it; your ORM depends on one or more of them, opaquely.

## 3

Your database is _not_ your server. Data in your database is _not_ data in your process. That data is not coming from the cache, or from local memory at all. Moving data from or to your database is an API call.

The client library your ORM hides from you knows this. That is one reason your ORM hides the client library it uses from you.

To let you treat data that lives in the database the same as data that lives in local memory—to erase the distance between that separate entity and your code—is a promise your ORM makes.

## 4

The outcome of a database query is a snapshot of some portion of that database _at the time of the query_. Once a query has been executed and its result made visible, the connection to "the truth" has already been severed.

Objects initialized with the results of queries also lack that epistemic connection—the `email` field of a `Author` object varies in complete independence from the `email` column of the `authors` table.

Initializing objects with the results of queries is one of two things your ORM—the ORM library your code is using—does.

([Transactions](https://en.wikipedia.org/wiki/Database_transaction) are one affordance your database offers to mitigate issues this transiency can cause; there may be others depending on implementation. Since ORMs don't model
the database, taking advantage of said affordances is often unidiomatic and awkward, and not infrequently wholly infeasible.)

To write a changed field back into the database involves tearing the object apart and overwriting rows in the database, based on what is hoped to be a stable and unique set of identifiers.

## 5

Your database has another API: [SQL](https://en.wikipedia.org/wiki/SQL).

SQL is the _only_ way of interacting with the kind of RDBMS I'm talking about. There is no bytecode, no assembly. There are no macros or compiler flags.
There Is Only SQL.

(Actually, There Is Only SQL + whatever helpful commands are exposed by the RDMS's interactive mode—like `psql`'s backslash commands, `sqlite3`'s dot commands, or `mysql`'s "Database Administration Statements"—but since those commands are
interactive client only, there's no way or need to make use of them when writing code.)

SQL is a programming language that is interpreted by the database itself. There is more readable SQL and less readable SQL; there is more performant SQL and less performant SQL. There are ways you can architect
your tables etc. that make it easier or harder to write more or less readable or performant SQL in much the same way that there are ways you can architect your application towards similar ends.

(Among those helpful commands mentioned earlier are tools like `EXPLAIN`, available in both `psql` and `mysql`, that can help you write at least more performant SQL.)

Your ORM produces SQL based on your code that it then sends to your database via a client library.

Producing SQL based on your code and sending it to your database via a client library is the second of two things your ORM does.

You have no direct control over the SQL your ORM produces based on the code you write.

Your ORM does not show you the SQL it produces based on your code unless you specifically ask it to. It does not show you the SQL it produces because it is technically unnecessary to do so, and because the SQL it produces is usually
neither readable nor performant.

## 6

Because ORMs model tables, maintaining the illusion that its objects are "normal" usually results in producing SQL that retrieves every column, usually by name. Your ORM may also unexpectedly produce SQL that join on foreign keys,
leaving your HTTP server or machine learning application or CLI tool to deal with having a few hundred `Book`s in memory when it just wanted an `Author`'s address.

You can change your code to get your ORM not to produce SQL like that. If you don't change your code to get your ORM not to produce SQL like that, it will produce SQL like that.
The exact ways to change your code to get your ORM not to produce SQL like that might be unidiomatic and ill-documented.

## 7

Because ORMs model tables, idiomaticity and quality of documentation often correlates negatively to the conceptual distance from that focus.

Database-native functions are treated in a lax and piebald manner. An ORM may elevate favored SQL functions to named methods or other documented constructs; the rest are invoked "stringly" or ignored in favor of equivalent
database-external functions.

## 8

Another promise your ORM makes is to let you ignore which specific RDBMS implementation is running your database. People like this because despite the existence of
[an ANSI standard](https://blog.ansi.org/sql-standard-iso-iec-9075-2023-ansi-x3-135/) every RDBMS implements SQL a little bit differently.

Your ORM most values not being misunderstood.

This concern both limits its output to a kind of "simplified SQL" that often lacks in both readability and performance, and proscribes its "blessed"
(idiomatic, ergonomic, well-documented) API surface to favor easily-universalizable SQL constructs.

These constructs may or may not be well-suited for your use-cases. Your RDBMS may offer different and more fitting constructs.

You may be able to change your code to get your ORM to produce different, better-suited SQL. You may be able to change your code to get your ORM to make use of features specific to your RDBMS.
To do so is to force your ORM to break a promise; the ways in which you need to change your code will likely be unidiomatic and ill-documented, if they exist at all.

Your ORM is not a compiler.

## 9

Once your application progresses beyond the most trivial CRUD, there will come a day when Life and its exigencies will present to you and your ORM a problem.

It may be a problem of complexity or of scale or of performance; it may be a problem of presenting the contents of your database in a different way.

Whatever its nature, it will only be solved by you writing SQL.

## 10

Instead: Learn SQL. Understand the relational model. Befriend a client library.

Instead: Recognize the non-monism of your models. Know that to create is not to read is not update is not to delete.

Instead: Acknowledge separation. Accept distance. Embrace a third party.

Instead: Think about [Domains](https://en.wikipedia.org/wiki/Domain-driven_design). Think about [Repositories](https://martinfowler.com/eaaCatalog/repository.html).
Think about the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter) and the [Single-Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle).

Instead: Be thoughtful. Be deliberate. Be consistent. Be clear.

[^1]: A table that has no foreign key or sequence columns and none of whose columns are referenced by foreign keys on any other table could conceivably "count" as an object, but such a table is neither realistic nor particularly useful.

[^2]: At least not well—perhaps as a meager API begrudgingly exposed through a `Connection` object, or in a smattering of arcane methods indifferently stuffed in the back of the documentation.

[^3]: Henceforth, when I write "database," you will understand that I mean "relational database, such as [PostgreSQL](https://postgresql.org) or [MySQL](https://www.mysql.com)."

[^4]: Here and here alone can the definition be expanded out to things like Mongo or DynamoDB, although perhaps less relevantly so.
