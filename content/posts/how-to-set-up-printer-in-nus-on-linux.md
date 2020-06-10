---
title: "How to set up printer in NUS on Linux"
subtitle: "UTown in particular"
date: "2020-06-04"
template: "post"
draft: false
category: Technology
tags: 
 - technology
 - guide
 - NUS
description: "A step-by-step guide to setting up printer using CUPS and its web interface in Cinnamon College"
featuredImage: "/images/cinnamon.jpg"
featuredImagePreview: "/images/cinnamon.jpg"
---

This is a step-by-step guide in setting up printing service in [Cinnamon
College,
NUS](http://www.usp.nus.edu.sg/life-at-usp/usp-housing-and-support/cinnamon-college-usp/).

The general idea is that as Linux users, we can follow the MacOS guides
available, with some not-so-nice web interface to set it up.

A typical setup instruction looks like this:

![MacOS Printer Setup Instructions](/media/cups/cinna_printing_instructions.jpg)
*Credits: USP Survival Guide 290719v2.pdf*

**What can we do?!** They all assume linux users are dangerous enough and know
what they are doing. But **everyone starts somewhere!**

*Let this be the somewhere.*

## Step 1: install CUPS

The [Common Unix Printer Service (CUPS)](https://www.cups.org), an open source
printer server developed by Apple, is what we will use today. Install it using
your favourite package manager: we will demonstrate using APT on Ubuntu below.

```bash
sudo apt install cups
```

## Step 2: Start the CUPS service

```bash
sudo systemctl enable cups
```

You can verify that the CUPS service is already running with

```
systemctl status cups
```

## Step 3: Use the web-based CUPS interface

CUPS server's web interface runs on your local machine on port 631. Fire up your
browser, and navigate to `localhost:631`.

![CUPS homepage](/media/cups/cups_home.jpg)

In the middle column, choose `Adding Printers and Classes`, then `Add Printer`.

You will be promted to key in your username and password, which refers to your
current user (with sudo privileges. To check your username, open up a terminal
and enter `whoami` to determine your username if you don't already know it.

## Step 4: Enter printer-specific information

![Choose the LPD protocol](/media/cups/cups_lpd.jpg)

As the printer is remotely connected via the same network, we will choose the
`LPD/LPR Host or Printer` option in the radio list. Press continue.

![Enter the IP address](/media/cups/cups_lpd_ip.jpg)

In the connection textbox, enter the IP address of the printserver and the
printer queue in the following format:

```
lpd://<ip_addr>/<queue>
```

For Cinnamon College's printers, it happens to be `172.16.29.84` as of writing,
so we will enter `lpd://172.16.29.84/MONO-A4` for the most used machine.

![Enter printer name, description and location](/media/cups/cups_printer_name.jpg)

_Errata: on the previous version of the post, I said the name is
important but **it is not**. The **queue** determines the printer, whereas
name is the just the printer name you see when you are at a printing dialog._

For the **name**, **description** and **location** columns, you can enter
whatever you like to help you distinguish between the different printers you add
to CUPS.

## Step 5: Select a PPD file for your printer
PostScript Printer Description (PPD) files are instruction sets created by
printer vendors to describe what their printers can do, and how to invoke these
functions.

Refer again to the MacOS setup document, we are told to select a `Generic
PostScript Printer` PPD. Selecting the `Make` as `Generic`, I chose the PPD as
below, because it seems to match the description the most.

![Select the PPD for your printer](/media/cups/cups_ppd2.jpg)

When you are done, click Add Printer.

## Step 6 (Optional): Add Default Options

![Default printer options](/media/cups/cups_default_options.jpg)

Just as what the page says. The `Query Printer for Default Options` button was
not clear in whether it worked, since the fields did not change after I click
the button. But it could be that we started with the printer's default options.

Friendly reminder: set double-sided printing as default to save the earth!!

Voila - now you are done! You can check your newly installed printer at
`localhost:631/printers/<PRINTER-NAME>`, which is
`localhost:631/printers/Cinna_MONO_A4` in my case.

![Printer status page](/media/cups/cups_printer_status.jpg)

Hope this guide benefits you. (*Updated 14 Aug 2019*)
