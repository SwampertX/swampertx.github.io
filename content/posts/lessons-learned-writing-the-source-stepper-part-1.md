---
title: 'Lessons learned writing the Source Stepper - Part 1'
date: '2020-02-09'
template: 'post'
draft: false
slug: '/posts/lessons-learned-writing-the-source-stepper-part-1'
category: 'Programming'
tags:
  - 'lambda calculus'
  - 'functional programming'
  - 'programming language'
description: 'and what I understand about the substituter implementation of Source'
featuredImage: "/media/forest.png"
featuredImagePreview: "/media/forest.png"
---

In this part, I will talk about what is the Source Language, what is the Source Stepper,
and some primer knowledge to understanding how the Source Stepper Works.

![Source Stepper in action](/media/stepper.gif)

# What is the _Source Stepper_?

The _Source Stepper_ is an implementation of the [Source language][source-lang] that is purely based
on **[lambda calculus-style][lambda-calc] substitution rules.**
The [Source language][source-lang] is a family of languages, split into 4 chapters,
each a sub-language of the next, and all are **[EcmaScript2016][es2016]-compliant.**

This means, all programs written in Source would be a **valid JavaScript program**. Additionally,
it has [proper tail call optimizations][tail-call] and arrow functions. Proper tail call optimizations
would allow the code snippet below, written in [Source 1][s1], to only take up
**constant stack space.**

```js
function factorial(n) {
  // arrow functions are allowed
  const fac_helper = (n, res) => (n === 1 ? res : fac_helper(n - 1, n * res));
  // tail call optimization
  return fac_helper(n, 0);
}
```

## What is the Source language for?

![A familiar sight for CS1101S Students](/media/forest.png)
_Artwork that goes into the Source Academy, the immersive platform for CS1101S._

The [Source language][source-lang] was designed by [Prof Martin Henz][henz] for teaching the
CS1101S Programming Methodology class at the National University of Singapore, using a
JavaScript adaptaion of the famous [Structure and Interpretation of Computer Programs (SICP)][sicp]
textbook. In fact, the textbook
is [freely available][sicp-js] as PDF, EPUB, and Mobile-friendly Web editions.

# Why the _Source Stepper_?

A bit of background: the SICP textbook introduces the [Substitution Model](https://sicp.comp.nus.edu.sg/chapters/7)
of evaluation, similar
to the beta-reduction of lambda calculus, to explain the evaluation of programs without state
changes (ie. variables that change values etc). This Substitution Model of evalutaion persists
through the first 2 chapters of SICP-JS textbook.

The Source Stepper is hence designed to be a **debugger that shows each evaluation(substitution)
step** of the Substitution to the student, to aid the students in understanding the model,
as well as debugging their programs.

# How does the Source Stepper work?

## Background: Abstract Syntax Trees

Before this, I had to first understand how a program is represented. First, let us look at an
analogy:

An **essay** is made up of **paragraphs**, which in turn, contains any number of **sentences**. There are
many types of sentences (grammatically), and each contains a different combination of **phrases**,
like

```
(I) (go) (to the park) (for a walk) (on Sundays).
```

A **program**, is made of up of **source files**, which in turn, each source file contains any number
of **statements**. Each different statement, such as a function declaration statement, or a block
statement, are made up of different components of **statements/expressions**.

```js
// Source 1
// function statement
// "id" and "n" are identifiers, an expression
function id(n) {
  // block expression
  // return statement
  return n;
}
```

Here is a table to sum them up:

```
| Essay      | Program                | Remarks                                           |
| ---------- | ---------------------- | ------------------------------------------------- |
| Paragraphs | Source files           |                                                   |
| Sentences  | Statements             |                                                   |
| Phrases    | Statements/Expressions | A statement can contain other statements as well. |
```

Turns out, there is this [website (astexplorer.net)](https://astexplorer.net)
which helped me greatly in decomposing programs into ASTs. Plug in some programs and start
playing!

## Reduction and Substitution

Strictly speaking, the evaluation program can be expressed by this pseudocode:

```
function EvaluateProgram(program):
  while program is not empty:
    firstStatement = get first statement from program
    if firstStatement is irreducible:
      remove firstStatement from program
    else:
      reduced = reduce the first statement of program
      replace program's first statement with 'reduced'
    continue
```

And thus there are only two things we should decide:

1. What kind of statements are irreducible, and hence can be discarded?
2. How do you reduce a statement?

_Yee Jian has been busy with school work, and will update this post intermittently._

<!-- links below -->

[source-lang]: https://sicp.comp.nus.edu.sg/source/
[lambda-calc]: https://en.wikipedia.org/wiki/Lambda_calculus
[es2016]: https://www.ecma-international.org/ecma-262/7.0/index.html
[tail-call]: https://en.wikipedia.org/wiki/Tail_call
[s1]: https://sicp.comp.nus.edu.sg/source/source_1/
[henz]: https://www.comp.nus.edu.sg/~henz/
[sicp]: https://mitpress.mit.edu/sites/default/files/sicp/index.html
[sicp-js]: https://sicp.comp.nus.edu.sg/
