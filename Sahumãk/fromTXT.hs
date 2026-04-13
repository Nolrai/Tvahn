module Main where

import Prelude
import Text.Read (readMaybe)
import Data.List (sortBy)
import Numeric (readHex)
import Data.Char (chr)

-- this file converts a tsv file that starts like
-- # Codepoint	GlyphName	Category	SourceFile	SourceIndex
-- U+E800	on_p	onset	on_001_p.svg	index=1
-- U+E801	on_t	onset	on_002_t.svg	index=2
-- U+E802	on_m	onset	on_003_m.svg	index=3
-- into a list of lexurgy sound changes

main :: IO ()
main = do
  rows <- (splitOnTab <$>) . lines <$> readFile "Sahumank-mapping.txt"
  let outLines1 = sortBy inverseFst (handleRow <$> drop 1 rows)
  let clauses = map snd outLines1
  let start = "deromanize: "
  writeFile "out.lsc" (unlines $ start : clauses)

inverseFst :: (Int, String) -> (Int, String) -> Ordering
inverseFst (a, _) (b, _) = compare b a

handleRow :: [String] -> (Int, String)
handleRow [codePoint, glyphName, _category, _sourceFile, _sourceIndex] =
  case parseCodepoint codePoint of
    Just c ->
      let input = reverse . takeWhile (/= '_') . reverse $ glyphName
      in (length input, "\t" <> input <> " => " <> [c])
    Nothing -> error $ "Invalid codepoint: " <> codePoint
handleRow _ = error "Invalid row format"

parseCodepoint :: String -> Maybe Char
parseCodepoint ('U':'+' : s) =
  case readHex s of
    [(n, "")] -> Just (chr n)
    _         -> Nothing
parseCodepoint _ = Nothing

splitOnTab :: String -> [String]
splitOnTab [] = []
splitOnTab s = here : splitOnTab (drop 1 later)
  where
    (here, later) = break (== '\t') s