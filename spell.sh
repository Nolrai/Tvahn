#!/bin/bash
# Highlights misspelled words in files using aspell and ripgrep.
# Usage: ./spell.sh <files>

rg --colors 'match:fg:red' -w -C1 -f <(cat "$@" | aspell list | sort -u) .
