---
title: "Linux wired earphones white noise solution"
date: 2021-08-04T22:48:55+08:00
lastmod: 2021-08-04T22:48:55+08:00
summary: "TLDR: Try amixer -c0 set \"Auto-Mute Mode\" Enabled"

---

# There was white noise.

This is a short write-up on how I solve the issue in the title.

## How I solved it

I went to `alsamixer` and choose the correct sound card (HDA Intel PCH).

Then press right until you see the `Auto-Mute` option. **Enable** it.

That solved the issue for me.

## Some descriptions for original problem.

There was white noise whenever I plugged in my earphones. It didn't exit before this, and does not come out on speaker.
