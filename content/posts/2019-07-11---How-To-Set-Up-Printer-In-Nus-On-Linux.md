---
title: "How to set up printer in NUS on Linux"
date: "2019-07-11"
template: "post"
draft: false
slug: "/posts/how-to-set-up-printer-in-nus-on-linux"
category: Technology
tags: 
 - technology
 - guide
 - NUS
description: 
---

This is a step-by-step guide in setting up printing service in NUS. The general idea is that as linux users, we can follow the MacOS guides available, with some not-so-nice web interface to set it up.

A typical setup instruction looks like this:
[insert image here]

**What can we do?!** They all assume linux users are dangerous enough and know what they are doing. Buf **everyone starts somewhere!**

*Let this be the somewhere.*

[insert inspiring quote]

### Step 1: install CUPS

The Common Unis Printer Service (CUPS), an open source printer server developed by Apple, is what we will use today. To install, use your favourite package manager: we will demenstrate using Ubuntu below.

```bash
sudo apt install cups
```
