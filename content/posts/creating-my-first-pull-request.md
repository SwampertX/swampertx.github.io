---
title: "Creating My First Pull Request"
subtitle: ""
date: 2020-05-31T23:19:29+08:00
lastmod: 2020-05-31T23:19:29+08:00
draft: false
author: ""
authorLink: ""
description: 'How I contributed the first time to GitLab, and what it meant to me'

tags: ["Open Source", "gitlab", "Guide", "Reflection"]
categories: ["Open Source"]

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: "/images/gitlab-logo-white-rgb.png"
featuredImagePreview: "/images/gitlab-logo-white-rgb.png"

toc:
  enable: true
math:
  enable: false
lightgallery: false
license: ""
---

<!--more-->

A few months ago, I wrote my first pull request to GitLab. I was genuinely
thrilled seeing my own code being pushed to production, and I have learnt a lot
during the process too. Here's the story.

# Background

I spent my summer working on a web application in Rails, also the framework
GitLab is written in. I was already quite familiar with the basics of rails, the
Model-View-Controller paradigm, as well as using Git and the Pull Request
workflow. I think without these prior knowledge, it would be quite hard to even
do some proper code contribution, despite how sites often make them seem easy.

I say this because you will probably need to:

1. Know enough Git to rebase your branch as the master moves quickly and you
   branch fails many tests on the Pull Request, thereby blocking
2. Know enough of the framework to navigate around. I quickly found where to
   edit due to the thorough discussion on the issue, but the understanding of
   MVC and what parts they play in the app would help
3. Finally, know your way around the command line to clone the application,
   build it, read error messages in build and search for relevant solutions, as
   well as dealing with testing from the command line if you don't have an IDE
   feature to run all those for you.

# Finding the issue

GitLab, as an all-remote company, has excellent documentation on almost
everything - this includes workflow for community contributors. Reading the
contribution page several times, I think I roughly get what to do when I work on
an issue, although they tend to get very detailed such that they are
incomprehensible before having an issue to work on.

After that, I simply went to the issue page and filter out the
good-first-issues. Some rules when I choose an issue:

1. No one is working on the issue, or someone expressed interest long time ago
   without a pull request in sight. This is very common, and do look out to
   prevent duplicated effort
2. Interest in the topic you do.
3. Gauge your ability to deal with the issue. Do you roughly know what is
   happening? If you do, there is a good chance you can solve the problem faster
   than going clueless.
4. (Optional) Something that people are looking forward to having. The issue I
   found had 17 thumbs-up, which means users have expressed collective interest
   in the feature. You will definitely feel better if you can create impact for
   more.

# Working on it

I settled down on the issue https://gitlab.com/gitlab-org/gitlab/issues/22488.
It seems related to some Google Kubernetes Cluster engine settings, and even
after looking through the issue, I had no idea where to look for the file. I
sought help in the issue directly by asking.

Now, I would like to clarify that GitLab developers are being nice to first time
contributors by pointing the direction, but you should not assume every
developer or maintainer should do that for you. In fact, it is in their every
right to not do it - if not they would have solved the problem by themselves.

In finding the right file to deal with, it is an art and would pace the way of
you contributing back to the same repository in the future, as you gained a
little more experience with the structure of the codebase.

Fortunately, I was directly linked, not just to the directory, or the file, but
down to the line on which the changes should be made. And after scrutinizing the
issue thread and some GKE link in the thread, I think i found a solution!

After writing them down, I made sure to

1. Follow the coding standards
2. Read the contribution guide again, which reminded me I need a changelog
3. Write meaningful commit messages. When people look back to a commit as to why
   you did the change, it should tell a story rather than merely describing what
   you did: `Some Refactoring` is a horrible one, as opposed to `Creating a function for blah`
4. Write tests. This is also to help you ensure your changes work, and an
   existing test suite will help you to detect any regression errors.

However, note that systems as big as GitLab is almost impossible to test
locally, unless you have a powerful workstation to run them. It is often better
to read about what is the expected behavior, which I merely created the pull
request and let the Continuous Integration (CI) system to run my tests for me.

# Code review

Patiently wait for code review, but make sure to keep an open mind and assume
good intentions on feedback given. This can get really long, but I personally
learnt a lot from this process. In particular, I had problems testing the bug
fix I created because I do not have GKE properly setup for my system. When asked
for help online, a tagged engineer even show how to do the testing with a
script! That was really amazing and things for me to learn about the Gitlab
Development Kit (GDK).

At the last part, my tests kept failing for weird, unrelated reasons. At first
it was because my code was outdated with the master branch. I realized that a
software at such a scale could not possibly only accept pull requests for
updated branches - as long as there is no conflict, merging should be allowed,
even if your branch is not rebased.

Even after rebasing to the master branch, one of my tests failed. When told to
the reviewer, he found out that it was another bug that caused the failure, and
solved it himself. That was a happy story.

# Done!

Now my commit was accepted! It was shipped a few weeks later. I could not find
my name or feature in the GitLab blog post, but it was still a worthwhile
feeling seeing the current version number >= the version your commit was merged
into.

On hindsight, choosing a supporting community is important for first
contributors, since you will be expectedly lost, and good-willed mentors are the
best. Also make sure you spend some time looking through the codebase, since
asking right away in the issue without checking out the code is really an
irresponsible waste of the mentor's time.

# Will I do it again?

Of course! I use so much open source software in my daily life, it is my time to
contribute back. Sharing is caring!
