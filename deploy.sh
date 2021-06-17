#!/usr/bin/env bash
set -euo pipefail

git add .
git commit -m "Automated commit by deploy.sh"
git push origin hugo
hugo
git checkout master
mv -f public/* .
rm -rf public
git add .
git commit -m "Automated deployment by deploy.sh"
git push origin master
git checkout hugo
