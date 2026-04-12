set -e

cd myscript
cabal build
NEW=$(cabal list-bin myscript)
cd -
cp $NEW myscript.exe
echo "Running $NEW" \"syllables\" \"onset\" \"nuclei\" $$
$NEW "syllables" "onsets" "nuclei" "$@"