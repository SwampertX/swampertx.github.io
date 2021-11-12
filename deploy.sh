#!/usr/bin/env bash
set -euo pipefail

hugo
rm -rf docs
cp -r public docs
git add .
git commit -m "Commit built site"
git push
