---
title: "SSH Jump"
subtitle: ""
date: 2020-06-04T22:48:55+08:00
lastmod: 2020-06-04T22:48:55+08:00
draft: false
author: ""
authorLink: ""
description: ""

tags: []
categories: []

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: ""
featuredImagePreview: ""

toc:
  enable: true
math:
  enable: false
lightgallery: false
license: ""
---

# SSH Jump

A while ago while taking CS2106 Operating Systems, I had to test my programs in
the designated server for students. However, this server is even inaccessible
from the NUS-wide WLAN, so we had to SSH into the course-specific server, let's
call it `2106-server`, first through a more general server called `sunfire`.

## SSH Keys

First things first, if you are still typing your passwords every time you are
ssh-ing into your servers, you are doing it *Wrong*. There is this thing called
`ssh-keygen`, which allows you to generate a public-private key pair, and once
you keep the private key and put the public key onto the server, you will never
have to type your password again, as long as you have the private key.

I always created my keys using RSA, since this encryption algorithm is widely
supported. If you have more time, you can take a look at ECDSA as well. Typing
either of the below lines should help you create your SSH key securely.

```bash
ssh-keygen -t rsa -b 4096
```

or

```bash
ssh-keygen -t ecdsa -b 521
```

The above process will tell you where your public and private keys are stored.

Now you can copy your public SSH key to the target machine:

```bash
ssh-copy-id -i ~/.ssh/id_rsa user@host
```

Where the script will actually infer the public key and push it onto the target
machine, dealing with duplication, creation of `~/.ssh` folder and whatnot. So
the next time, you can simply type

```bash
ssh my_user_name@host.example.com
```

and SSH into the target machine.

**What, that is not enough?**

## SSH Config File

The aim of this section is to teach you to do a shorter command with SSH, as
well as ridding you of the troubles of having to

1. Remember your username. Which one is it?
1. Remember your target machine's address. This is especially useful if you are
   dealing with IP addresses, which are a pain
1. Add a bunch of configs, which you can check at `man ssh_config`

 Credits to Hao Wei (`@angelsl`) for posting this awesome config for NUS
 computing users:

```
# ~/.ssh/config
Host xcn?? xcn??? xgp?? xgp??? sunfire sunfire0
    HostName %h.comp.nus.edu.sg
    User your_username
    IdentityFile ~/.ssh/id_rsa
```

which included a bunch of wildcards to access many of the computing clusters
with just one config entry. Save this to `~/.ssh/config` and thank Hao Wei, not
me.

Now, SSH-ing to hosts other than `sunfire` and `sunfire0` is just:

```bash
ssh -J sunfire xcnd0
```

, instead of the tedious

```bash
ssh -J sunfire_username@sunfire.comp.nus.edu.sg xcnd0_username@xcnd0.comp.nus.edu.sg
```

## Some other Quality of Life hints

1. Since `sunfire` is running SunOS, setting your `TERM=xterm` could give you
   some convenience such as clearing your prompt by pressing `C-l`. You can do
   that in bash by

   ```bash
   TERM=xterm ssh sunfire
   ```

   Or even aliasing your `ssh` to `TERM=xterm ssh` in your `~/.bashrc`
1. Have fun talking to (annoying) your friends by finding out their username
   through the command `w`, then writing to them by the command
   `write other_username` then typing your message. When you are done, you can
   just press `C-c` or `C-d`.
