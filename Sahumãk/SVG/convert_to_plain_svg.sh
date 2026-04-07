#!/bin/bash
# Batch convert all SVGs in the current directory from Inkscape SVG to Plain SVG
# Usage: ./convert_to_plain_svg.sh

for file in *.svg; do
  # Skip if no SVG files are found
  [ -e "$file" ] || continue
  # Output filename: add _plain before .svg
  out="${file%.svg}_plain.svg"
  inkscape "$file" --export-plain-svg --export-type=svg --export-filename="$out"

  echo "Converted $file -> $out"
  echo "----------------------------------------"
  mv "$out" "$file"
  echo "Overwrote $file with $out"

done


