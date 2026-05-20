{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE OverloadedStrings #-}
import qualified Data.Trie as Trie
import Prelude (error, otherwise, fst)
import System.IO (IO)
import GHC.Num (Num(..))
import Data.Int (Int)
import Data.Char (Char)
import qualified Data.ByteString.Char8 as BS
import TrieGen (genTrie)
import System.Environment (getArgs)
import Data.Text.Encoding (decodeUtf8, encodeUtf8)
import qualified Data.Text as T
import Data.List (maximum)
import Data.Maybe (Maybe(..))
import Data.Functor ((<$>))
import Data.Function ((.), ($))
import Data.Foldable (Foldable(foldl'))
import Data.Monoid ((<>))

-- At compile time, embed the trie
myTrie :: Trie.Trie Char
myTrie = $(genTrie "data/toGlyphs.tsv")

maxKeyLen :: Int
maxKeyLen = maximum $ T.length . decodeUtf8 . fst <$> Trie.toList myTrie

-- deal with non ascii but valid inputs
normalize :: T.Text -> T.Text
normalize txt = foldl' (\acc (a, b) -> T.replace a b acc) txt l
  where
    l =
      [ ("ã", "an")
      , ("ĩ", "in")
      , ("ũ", "un")
      ] <>
      [ ("ə", "")
      , ("ʌ", "")
      , ("ɪ", "")
      , ("ʔ", "")
      ]

-- Longest match substitution
substitute :: T.Text -> T.Text
substitute = go
  where
    go txt
      | T.null txt = T.empty
      | otherwise =
          let candidates =
                [ (T.length prefix, v)
                | len <- [maxKeyLen, maxKeyLen-1 .. 1]
                , let prefix = T.take len txt
                , let normalizedPrefix = normalize prefix
                , let bsPrefix = encodeUtf8 normalizedPrefix
                , Just v <- [Trie.lookup bsPrefix myTrie]
                ]
          in case candidates of
            (len, v):_ -> T.cons v (go (T.drop len txt))
            []         -> T.cons (T.head txt) (go (T.tail txt))

main :: IO ()
main = do
  args <- getArgs
  let (inputPath, outputPath) = case args of
        [filePath] -> (filePath, "output.txt")
        [filePath, outPath] -> (filePath, outPath)
        _ -> error "Usage: myscript <input-file> [output-file]"
  input <- BS.readFile inputPath
  let inputText = decodeUtf8 input
  let outputText = substitute inputText
  BS.writeFile outputPath (encodeUtf8 outputText)
