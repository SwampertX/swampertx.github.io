---
title: Projects
template: page
---

[view-on-gh-badge]: https://img.shields.io/badge/view%20on-Github-blue.svg

### [Source Stepper](./stepper.html)

[![Github][view-on-gh-badge]][stepper-gh]
[![Source Academy][sa-badge]][sa-link]
[![Source Stepper in Action: Factorial(10)](/media/stepper.gif)](/media/stepper.gif)
[Try out the substituter!](sa-link)

A lambda-calculus based interpreter for the [Source
language](https://sicp.comp.nus.edu.sg/source/), a sublanguage of JavaScript,
written in TypeScript.

This interpreter steps through and records each reduction step of the program.
It can be used for the first 2 chapters of the source language ([Source
§1](https://sicp.comp.nus.edu.sg/source/source_1/), [Source
§2](https://sicp.comp.nus.edu.sg/source/source_2/)) as state changes are not
allowed in these languages. Idempotency of pure functions ensures the
lambda-calculus based reduction rules evaluate the program correctly.

I plan to write an article that explains the workings of this interpreter soon.

<!--
TODO: add link after article
I wrote a blog post on how the stepper works here.
-->

[stepper-gh]: https://github.com/source-academy/js-slang
[sa-badge]: https://img.shields.io/badge/Source%20Academy-ready-brightgreen.svg
[sa-link]: https://sourceacademy.nus.edu.sg/playground#chap=2&exec=1000&ext=NONE&prgrm=GYVwdgxgLglg9mABMAhtOAnGKA2AKMASkQG8AoRSxDAUyhAySQF5XEAGCq7gfkQEYu3SgC5ESAFTI0UTNnxgAtP0IBuMgF8yqdFlx5%2B7NUA

### Dotfiles

[![Github][view-on-gh-badge]][dotfiles-gh]

I am now tracking my dotfiles! I also included automated backup and install
scripts. Tested on a VM.

[dotfiles-gh]: https://github.com/swampertx/dotfiles

### Cinnabot

[![Github][view-on-gh-badge]][cinnabot-gh]
[![Telegram][cinnabot-tele-badge]][cinnabot-tele]

A Telegram bot written in GoLang to serve the residents of [Cinnamon College](http://www.usp.nus.edu.sg/).

It can query for:

- NUS Internal Shuttle Bus timings
- Singapore Public Bus timings
- Cinnamon College events and venue usage
- Frequently accessed links for USP students

[cinnabot-gh]: https://github.com/usdevs/cinnabot
[cinnabot-tele-badge]: https://img.shields.io/badge/telegram-ready-brightgreen.svg
[cinnabot-tele]: https://t.me/cinnabot

### Some little scripts

#### [IVLE Downloader (Deprecated)](https://github.com/SwampertX/ivle-downloader)

[![Github][view-on-gh-badge]](https://github.com/SwampertX/ivle-downloader)

A downloader I forked to automate the downloading of files from IVLE, my
university's learning management system.

IVLE has been replaced by [LumiNUS](https://luminus.nus.edu.sg) since Aug 2019.
For a LumiNUS downloader, please check out
[fluminurs](https://github.com/indocomsoft/fluminurs)!

#### [CS2040 judging bash script](https://github.com/SwampertX/nus-scripts/blob/master/codecrunch/check_java.md)

[![Github][view-on-gh-badge]](https://github.com/SwampertX/nus-scripts/tree/master/codecrunch)

![A screenshot of the bash script to automate checking.](/media/check_java.gif)
_A screenshot of the bash script to automate checking._

