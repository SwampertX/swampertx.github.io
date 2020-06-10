---
title: 'CS2103 in NVim + CLI - A Post Reflection'
date: '2020-01-20'
template: 'post'
draft: false
slug: '/posts/cs2103-in-nvim-+-cli---a-post-reflection'
category: Technology
tags:
  - NeoVim
  - Software Engineering
  - Technology
  - Vim
  - Java
  - Gradle
description: 'The lessons I learned using both NeoVim and IntelliJ.'
featuredImage: "/images/neovim-logo.png"
featuredImagePreview: "/images/neovim-logo.png"
---

Now that **CS2103 Software Engineering** is over, is using NeoVim as a Java Editor worth it?

My answer: the learning was worth it, but the functionalities of IntelliJ totally crushed
Java development. It is _the killer app_ that you need, if you are doing serious Java development.

## The Pros and Cons with NVim

### Pros

Vim's many keybindings makes text editing enjoyable. With all the familiar jumps, yanking paragraphs,
search and replace - I absolutely loved the "fingers never leave the home row" experience.

With many other tools, such as fzf bindings for vim, and tim pope's commentary.vim, surround.vim and
https://github.com/wellle/targets.vim made editing a breeze.

Commenting out code is just `gc<object>`, and since Java has quite a bit of method chaining, using
targets.vim to clear out chained function call is just `di.` since method calls are chained by dots.

With a usual tiling manager, like the i3 that I am using, I am able to have a workspace with a regular
terminal running vim, a narrow terminal allow me to try things out in jshell or just build my project,
and tiled with the built project for manual testing. Most importantly, switching between them is a
breeze with the normal keybindings (self-defined, if need be)!

### Cons

COC's Java was really CPU intensive, there are many times it just hogs up the CPU and hangs the
nvim instance. I am not sure where the problem is, but I would imagine in a huge project this
is not feasible at all. Also when you switch between buffers, there will be some time when the
language server parses the new buffer and introduces waits around 3-4 seconds, which can be quite
unbearable to wait.

### The Pros and Cons with IntelliJ

A friend of mine, once a Java developer, saw me developing in NVim and hence convinced me to give
IntelliJ a whirl, showing me the power of the IDE itself. It certainly does not disappoint, and
even taught me new things about the whole `:CocAction` business.

### Pros

IntelliJ was the result of many, many years of development and is extremely feature rich.
I recommend anyone using IntelliJ take some time to go through a course, maybe a good
Video Tutorial series to learn some useful features before you start. It is a waste if you use
your IntelliJ just like a Gedit with a terminal and a file explorer.

For example, upon writing a few classes in Java you realized that they share some functionalities
and you would like to extract out a few functions from these classes into an Interface. IntelliJ
has it. You want to delete a class and all of its occurrences. In NVim, you can delete the class,
and use some command line tools like `grep` or `rg` to search for occurrences, and then delete them,
which although is possible, is a lot more work. Renaming a package and have to change all the
child classes's package declaracion? You can do it with one button in IntelliJ. In CLI, you probably
need some data wrangling skills, and with some sed magic and some Googling. In any case, IntelliJ
was way more powerful than I realized.

### Cons

As almost all IntelliJ users would complain - it is too memory-intensive. Also for such a huge
IDE, you will need some time to get used to the different key bindings, such as switching between
the editor and terminal, and I can't seem to remember them because they differ with my usual ones
a lot. Also auto format on save is not available out of the box and requires some keyboard macro
recording. Although I would say in the long run, these would be outweighed by the benefits if
you do Java programming for a living.

## Final reflection

I realized that there should have been a standard translation protocol which translates Java
checkstyle into a formatting standard, recognized by the IDEs. Currently users can import
styleguides (not checkstyle), which might conflict with a checkstyle file. Also checkstyle file
often warns for code-quality issues (such as trailing spaces, bracing, and comments), which
would be good if can be integrated by the IDE/NVim. Maybe there is one which I am not aware of,
but it would be really useful!

It was a long journey and I think I have discovered a bit more about NVim and Editors through
this little experiment.
