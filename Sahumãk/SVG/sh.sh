set -e

cd myscript
cabal build
cp "$(cabal list-bin exe:myscript)" ../myscript.exe
cd ..
./myscript.exe syllables onsets/ vowels/

