+++
draft = true
date = 2023-09-09
layout = 'single'
title = 'Scrap Your ORM'
+++

## 0. Prelude
In my decade or so as a software developer, I've encountered multiple technologies that all roughly fit a similar mold&mdash;omnipresent but unloved, widely present but equally widely resented.
A common giveaway is how your (future) coworkers discuss them: a shrug; a half-chuckle; perhaps a vague reference to a long-buried ticket or branch that prompts a silent, dead-eyed stare.
We've all done it:

"Yeah...we use JIRA. Sorry..."

"We've been meaning to replace Celery, but..."

"We should discuss what to do about Redis for our next Tech Debt sprint (whenever that happens.)"

These we recognize, these we discuss; their harms are often discrete and bite-sized. When Redis crashes, or your job queue sends the same job twice, or tickets disappear, those are palpable harms.


There is another piece of our stacks that is equally malignant, but its harms are distributed and diaphonous, easily papered over or misattributed. It's not a specific program, or utility, or language,
or library. It could be called an "anti-pattern," but so doing might stretch the term beyond usefulness. It's been in every stack I've encountered, across multiple languages. If you're doing web development,
you're probably engaging with it every day.

I speak, of course, of the Object-Relational Mapper, or ORM.

It's Bad, and you should Stop Using It.

 
## 1. What?
If you don't know what an ORM is, [Wikipedia](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) defines it as

> a programming technique for converting data between a relational database and the heap of an object-oriented programming language. This creates, in effect, a virtual object database that can be used from within the programming language.

If you don't know what an ORM is but _do_ know what the `heap` is, your time will likely be better-spent finishing your CS201 assignment than reading the rest of this nonsense.
If you _don't_ know what the `heap` is (or you say you do but you couldn't necessarily, like, _explain_ it), I am pleased to tell you that you can preserve your ignorance a while longer.

The key is in the second part: `in effect, a virtual object database that can be used from within the programming language.`
That's the promise of ORMs: you can just put that scary ol' database into your Java/Python/TypeScript/Ruby/Rust/Haskell/Elixir/whatever program and Not Worry About It.

{{< details summary="Aside: Abstractions & Patterns" emoji=":locomotive:" >}}
Any neurons pinging off of "put this thing between you and something you don't entirely understand to simplify it" aren't misguided: an ORM is, on some level, an implementation of the [GoF Facade Pattern](https://en.wikipedia.org/wiki/Facade_pattern),
and we can all agree that Abstractions Are Good. That being said, Bad ("Leaky") Abstractions Are Bad, and I shall endeavor to prove that ORMS make a collander look sea-worthy.
{{< /details >}}
 
 As darkly hinted at above, if you're in web dev, odds are you're already using an ORM, whether you know it as such or not. In the course of my decade or so in the field, I've worked with
 [Django](https://www.djangoproject.com), [SqlAlchemy](https://www.sqlalchemy.org), and [Prisma](https://www.prisma.io); read up on [Esqueleto](https://hackage.haskell.org/package/esqueleto) and [SeaORM](https://www.sea-ql.org/SeaORM/);
 and heard horror stories about [ActiveRecord](https://guides.rubyonrails.org/active_record_basics.html#what-is-active-record-questionmark). Maybe you've had the misfortune to use one of these,
 or Laravel/CakePHP, or Hibernate, or, or, or.
 
 The point is: ORMs are everywhere, and, as previously mentioned, are Bad.
 
 ## 2. Why?
 
 ### 2.1 Theory
 Let's start with the theoretical issues, because I'm writing this and they matter to me, at least.
 
 #### 2.1.1 The Database Model
 Modern "Relational" databases are built off of [theoretical work](https://en.wikipedia.org/wiki/Relational_model) by [E.F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd); the fundamental model is the `tuple`, an (internally) ordered, heterogenous
 collection of data. Similarly-shaped tuples can be collected into tables, and you can `select` data out of them, or `order` them, or `join` them together.
 
 All well and good.
 
 #### 2.1.2 The Object Model
 [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) emerged in the mid-60s as one possible solution to the threat of [spaghettification](https://en.wikipedia.org/wiki/Spaghetti_code)
 that lurks in every purely-imperative language. 
 
 {{< details summary="Nota Bene" emoji=":scroll:" >}}
 1. The Object-Oriented paradigm _immediately_ and _necessarily_ emerges from the [Algol](https://en.wikipedia.org/wiki/ALGOL) family of languages.
    There were no similar developments in the [ML](https://en.wikipedia.org/wiki/ML_(programming_language)) and [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)) families until [CLOS](https://en.wikipedia.org/wiki/Common_Lisp_Object_System) was added to Common Lisp in the '80s.
 2. While early OO languages like [Simula](https://en.wikipedia.org/wiki/Simula) predate [the earliest Relational Databases](https://en.wikipedia.org/wiki/IBM_Peterlee_Relational_Test_Vehicle) by roughly a decade, Codd is coming from a _very_ different place, both theoretically and practically, than the major movers and shakers in the OO sphere.
{{< /details >}}

Much like the aforementioned `heap`, OOP is one of those terms of art that get bandied about without much explanation; much like "agile," everyone does it, but nobody does it "right."[^1] As can be expected, precise definitions are hard to come by,
but here is the one I will use:

> 1. A program consists of `object`s
> 2. An `object` is a _program-level_[^2] constuct that "has `state`." `State` refers to data, usually but not always mutable, that is tied to or "owned by" the object.
> 3. `Object`s can `send` and `receive` `messages`, which are pieces of arbitrary data[^3]. How an `object` reacts to a `message` is determined _entirely_ by the `object`.

 {{< details summary="Hmm" emoji=":thinking:" >}}
Those of you familiar with modern OOP terminology might be having some brain fizzles; those of you with [Erlang](https://en.wikipedia.org/wiki/Erlang_(programming_language)) might be having some brain sparks. Good.
{{< /details >}}

It's admittedly more common nowadays to talk about `methods` than `messages`, but the concepts are roughly isomorphic: calling an object's method is just sending a specific message to that object. The complementary half is less
apparent in mixed-paradigm languages like Python or Ruby but more so in (often compiled) languages that still enforce a single entry point like C\+\+, where a program's call graph can easily be viewed as a network of sent and received messages.

I also didn't say anything about `inheritance`. This is intentional. While it's come to be closely associated with OOP, it's not a necessary or sufficient property; indeed, there's [evidence](https://www.cs.tufts.edu/comp/150FP/archive/kristen-nygaard/hopl-simula.pdf) that its
inclusion in Simula 67 was basically a hack. Furthermore, it's trivial to show that OOP inheritance has no equivalent of any kind in the relational model; such an exercise is left to the reader.

#### 2.1.3 The Impedance Mismatch
[From this perspective](https://youtu.be/hzzQ7hXQ7qk?si=ygMRhb0EgkJOEHpO), the seams and rough edges perhaps become more apparent. Simply put:

_A `row` is not an `object`._

How could it be? How can a `row` in a table be said to "send" or "receive" messages in any way? `insert` is the only "row-level" action available in an RDBMS; `delete`, `select`, and `update` all operate at, minimally, the table-level

"Aha!" you say, not being a dummy, "of course a `row` isn't an `object`, `table`s are `object`s!"

`table`s are certainly closer, my rhetorical non-dummy interlocutor. Indeed, here is a `table` that would meet the aforementioned criteria

```sql
CREATE TABLE object (
  id BIGINT UNIQUE
  x INTEGER
  words TEXT
 }
 ```
 
 Can we send it messages (`delete`, `insert`, `select`, `update`)? :check_mark:    
 Does it "own" its data? Sure, why not.
 
 Is it _useful_? :x:
 
 We can't have an auto-incrementing primary key, because that relies on a `sequence` exterior to our table. We can't have foreign keys, because their integrity also relies on data that doesn't "belong" to our table.
 
 So sure, we can create a trivial (in all senses) relational database that contains tables that technically meet the definition of `object`.
 

But an ORM doesn't model tables, it models rows, which we've pretty definitively proven are _nothing_ like `object`s.


### 2.2 Practice
ORMs are convenient in many ways. Being born out of web development, they reify and ease many of the facets of the usual opinion of web devs towards their databases: Weird Scary Places Where The Data Live. ORMs promise that you'll never
have to think about Gross Old SQL; you'll just use your Cool Modern Language and have all your data Right There.




[^1]: In this&mdash;and pretty much this alone&mdash;it is similar to the relational model.
[^2]: That is to say, _not_ represented at the assembler level, or indeed often in any [Intermediate Representation](https://en.wikipedia.org/wiki/Intermediate_representation) generated by the languages compiler or interpreter.
[^3]: Also program-level, for what it's worth.
