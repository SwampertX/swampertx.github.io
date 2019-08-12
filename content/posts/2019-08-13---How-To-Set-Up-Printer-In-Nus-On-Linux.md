---
title: "How to set up printer in NUS on Linux"
date: "2019-08-13"
template: "post"
draft: false
slug: "/posts/how-to-set-up-printer-in-nus-on-linux"
category: Technology
tags: 
 - technology
 - guide
 - NUS
description: "A step-by-step guide to setting up printer using CUPS and its web interface in Cinnamon College"
---

This is a step-by-step guide in setting up printing service in [Cinnamon College, NUS](http://www.usp.nus.edu.sg/life-at-usp/usp-housing-and-support/cinnamon-college-usp/).

The general idea is that as Linux users, we can follow the MacOS guides available, with some not-so-nice web interface to set it up.

A typical setup instruction looks like this:

![MacOS Printer Setup Instructions](/media/cups/cinna_printing_instructions.jpg)
*Credits: USP Survival Guide 290719v2.pdf*

**What can we do?!** They all assume linux users are dangerous enough and know what they are doing. But **everyone starts somewhere!**

*Let this be the somewhere.*

## Step 1: install CUPS

The [Common Unix Printer Service (CUPS)](https://www.cups.org), an open source printer server developed by Apple, is what we will use today. Install it using your favourite package manager: we will demonstrate using APT on Ubuntu below.

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

CUPS server runs on your local machine on port 631. Fire up your browser, and navigate to `localhost:631`.

![CUPS homepage](/media/cups/cups_home.jpg)

In the middle column, choose `Adding Printers and Classes`, then `Add Printer`.

You will be promted to key in your username and password, which refers to your current user (with sudo privileges. To check your username, open up a terminal and enter `whoami` to determine your username if you don't already know it.

## Step 4: Enter printer-specific information

![Choose the LPD protocol](/media/cups/cups_lpd.jpg)

As the printer is remotely connected via the same network, we will choose the `LPD/LPR Host or Printer` option in the radio list. Press continue.

![Enter the IP address](/media/cups/cups_lpd_ip.jpg)

In the connection textbox, enter the IP address of the printer prefaced by `lpd://`.
For Cinnamon College's printers, it happens to be `172.16.29.84` as of writing, so we will
enter `lpd://172.16.29.84`.

![Enter printer name, description and location](/media/cups/cups_printer_name.jpg)

Onto the next page, the **Name** textbox is the most important here. Refer to the MacOS 
instructions and you will find the name for your printer, such as `MONO-A4`. This will
determine which printer you set up.

For the **description** and **location** columns, you can enter whatever you like to help
you distinguish between the different printers you add to CUPS.

## Step 5: Select a PPD file for your printer
PostScript Printer Description (PPD) files are instruction sets created by printer vendors
to describe what their printers can do, and how to invoke these functions.

Refer again to the MacOS setup document, we are told to select a `Generic PostScript Printer`
PPD. Selecting the `Make` as `Generic`, I chose the PPD as below, because it seems to match
the description the most.

![Select the PPD for your printer](/media/cups/cups_ppd.jpg)

When you are done, click Add Printer.

## Step 6 (Optional): Add Default Options

![Default printer options](/media/cups/cups_default_options.jpg)

Just as what the page says. The `Query Printer for Default Options` button was not clear
in whether it worked, since the fields did not change after I click the button. But it could
be that we started with the printer's default options.

Friendly reminder: set double-sided printing as default to save the earth!!

Voila - now you are done! You can check your newly installed printer at `localhost:631/printers/<PRINTER-NAME>`, which is `localhost:631/printers/MONO-A4` in my case.

Hope this guide benefits you.
