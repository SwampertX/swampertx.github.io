---
title: "CS2103 in nVIM + CLI - Week 2"
date: "2019-09-13"
template: "post"
draft: false
category: "Technology"
tags:
 - NeoVim
 - Software Engineering
 - Technology
 - Vim
 - Java
 - Gradle
description: "Because you can. Also I wanna try out the limits of nVIM.
Java debugging in CLI? Let's see what can happen."
featuredImage: "/images/neovim-logo.png"
featuredImagePreview: "/images/neovim-logo.png"
---

Because you can. Also I wanna try out the limits of nVIM.
Java debugging in CLI? Let's see what can happen.

## 1. Setting up JDK11

Okay. You know what to do - your package manager has JDK11 ready for you - but what is
the name of the package?

```bash
apt-cache search java11
# aha! I see "openjdk-11-jdk"
sudo apt install openjdk-11-jdk
# 213MB. That's huge but okay done
which java
# /usr/bin/java . Okay we are done
java --version
# openjdk 13 2019-09-17
# uhh what??
```

Yeah, that could hapen if you have multiple versions of JDK on your machine.

**`update-alternatives` comes to the rescue!**

```bash
sudo update-alternatives --config java
# select the correct version, then press enter
java --version
# openjdk 11. Hooray!
```

What it does, is to create a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link)
from the specific version to `/usr/bin/java`, which is where the binary is accessed.
This makes `update-alternatives` a great way to swich between versions, especially when
there is a new GCC version that breaks many builds.

We are done with JDK11! Onwards------

## 2. Gradle

Luckily, the Duke project comes with gradle in the source code. Simply navigate to the root of the project folder, and you will find a `gradlew` executable. Simply run `./gradlew <command>`!

## 3. Git

Installing git is simple! It is just

```bash
sudo apt install git-all
git config --global user.name "Your Name"
git config --global user.email "Your email"
```

Done! Start using git.

## 4. Vim (or nVim)

This is the crucial part - we must harness the powerful plugins in to make our lives much easier, even easier than in IDEs, hopefully.

Things I have figured out:

- Asynchronous Linting
- Auto-formatting (on save or on type)

Things I have not:

- Debugging

Feel free to follow this section, as long as you have **Vim 8 or later**, or **NeoVim** installed on your machine! I will keep calling either of them vim, but what I refer to is any of these versions/flavours of vim.

### 4.1 Asynchronous Linting

When Vim meets VSCode - we have coc.nvim. Installing it using vim-plug is a breeze, just
prepend the following lines to your `~/.vimrc`:

```vimscript
" Use release branch
Plug 'neoclide/coc.nvim', {'branch': 'release'}
```

Remember to source the file (by typing `:so %` or restarting vim), and then install the plug
using `:PlugInstall`.

Great! You now have a full-featured language server on your vim, this provides a long-term support on your usage of vim as long as VSCode is still around.

**Next, we need to install [coc-java][coc-java]**.

Simply fire up your Vim, and type in `:CocInstall coc-java` to install the Java Language Server. Now you should start seeing markings on your vim if your code is illegal - if not try to type some garbage into your buffer, and Vim should complain. Congrats, you are done!

Now note that for more features of proper linting, you can look towards [Asynchronous Linting Engine (ALE)](https://github.com/dense-analysis/ale) for more information.

### 4.2 Auto-formatting

A crucial part is that there is a styleguide we should follow, and it resides in `/config/checkstyle` relative to the project root directory. Upon closer inspection, we realize that CS2103 is following the Google's Java Style Guide!

Following [coc-java][coc-java]'s README, we found this page detailing how to make [formatter settings](https://github.com/redhat-developer/vscode-java/wiki/Formatter-settings)! So we just need to type `:CocConfig` in Vim's normal mode (use tab for autocomplete, just type in a case-insensitive manner), and we will be led to an (perhaps empty) json file. Remember to have a top layer braces, and add in these two properties:

```json
{
  "java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml",
  "coc.preferences.formatOnSaveFiletypes": ["java"]
}
```

and voila! Your files will now be formatted whenever you save them. If you look under the [Supported Settings](https://github.com/neoclide/coc-java#supported-settings) header on [coc-java][coc-java]'s README, you can set all the settings the same way as we did in the `:CocConfig` just now.

As for the [Available Commands](https://github.com/neoclide/coc-java#available-commands) just above it, you can trigger any of them using `:CocCommand`, and then do a fuzzy search on your desired command. For example, we are looking for `java.action.organizeImports` specifically! What a godsend!

## Closing words

That will be all for now. If I discover more useful features, I will cover them here.

[coc-java]: https://github.com/neoclide/coc-java
