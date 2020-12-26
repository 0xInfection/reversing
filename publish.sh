#!/bin/sh

# gh-pages branch
git checkout gh-pages
# building the gitbook
gitbook build

# copy up things
cp -R _book/* .

# clean things up quickly
git clean -fx _book

# add and commit
git add .
git commit -m 'updated gitbook'