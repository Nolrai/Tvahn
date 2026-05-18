set -e

safe_rm() {
  for path in "$@"; do
    if [ -e "$path" ] || [ -L "$path" ]; then
      rm -I -- "$path"
    fi
  done
}

EXE_FILE="toGlyphs.exe"
OUT_FILE="example.txt"
IN_FILE="../../PSA/Conversation 1.txt"

cd myscript
cabal build
NEW=$(cabal list-bin myscript)
cd - >/dev/null

safe_rm "$EXE_FILE" "$OUT_FILE"
cp "$NEW" "$EXE_FILE"
./"$EXE_FILE" "$IN_FILE" "$OUT_FILE"
code ./example.glyphs