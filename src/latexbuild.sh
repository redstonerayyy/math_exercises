#!/bin/sh

set -e

IN_DIR="./src"
BUILD_DIR="./build"
OUT_DIR="./material"

mkdir -p "$BUILD_DIR"

# get the latex files and their number
files="$(find "$IN_DIR")"
total="$(echo "$files" | grep -E '.tex$' | wc -l)"

# compile every file
i=1
for file in $files; do
    # we only care about .tex files
    [ "${file##*.}" = "tex" ] || continue

    echo "Converting file $i/$total: $file"
    # latex may hang up and wait for input, so we'll timeout here
    timeout \
        "5s" \
        pdflatex -output-directory "$BUILD_DIR" "$file" >/dev/null

    basename="${file##*/}"
    filename="${basename%.*}"
    folder="$(echo "${file%/*}" | sed -E 's/\.\/src//g')"

    # copy the file to its place in the folder structure
    mkdir -p "$OUT_DIR/$folder"
    cp "$BUILD_DIR/$filename.pdf" "$OUT_DIR/$folder/$filename.pdf"

    i=$((i+1))
done
