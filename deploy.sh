#!/usr/bin/env bash
set -euo pipefail

hugo
git checkout master
git checkout hugo -- public
ls | rg -v public | xargs rm -r
mv -f public/* .
rm -rf public
git add .
git commit -m "Automated deployment by deploy.sh"
git push origin master
git checkout hugo
