set -e

cd myscript
cabal build
NEW=$(cabal list-bin myscript)
cd -
rm toGlyphs.exe example.glyphs
cp $NEW toGlyphs.exe
./toGlyphs.exe ../../PSA/Conversation\ 1.txt ./example.glyphs
code ./example.glyphs