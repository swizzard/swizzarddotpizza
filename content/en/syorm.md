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
 Modern "Relational" databases are built off of theoretical work by [E.F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd); the fundamental model is the `tuple`, an (internally) ordered, heterogenous
 collection of data. Similarly-shaped tuples can be collected into tables, and you can `select` data out of them, or sort them, or `join` them together.
 
 All well and good.
 
 #### 2.1.2 The Object Model
 [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) emerged in the mid-60s as one possible solution to the threat of [spaghettification](https://en.wikipedia.org/wiki/Spaghetti_code)
 present in every purely-imperative language.
 
 {{< details summary="Aside: Paradigms" emoji=":locomotive:" >}}
It should be noted that the timeline 
{{< /details >}}
 
