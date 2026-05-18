{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE OverloadedStrings #-}
module TrieGen (genTrie) where

import Prelude (FilePath, Char, not, (<$>), ($), (<>), (&&), (.))
import qualified Data.Trie as Trie
import qualified Data.ByteString.Char8 as BS
import Language.Haskell.TH
import Language.Haskell.TH.Syntax
import Data.Text.Encoding (encodeUtf8, decodeUtf8)
import Data.Text (Text)
import Data.Text qualified as T
import Data.Maybe (Maybe(..), mapMaybe)

-- | Read a dictionary file and generate a Trie at compile time.
genTrie :: FilePath -> Q Exp
genTrie dictPath = do
    runIO $ BS.putStrLn $ "Reading dictionary: " <> BS.pack dictPath
    dict <- runIO (T.lines . decodeUtf8 <$> BS.readFile dictPath)

    let pairs = mapMaybe splitLine dict
        trie = Trie.fromList pairs
    liftTrie trie

splitLine :: Text -> Maybe (BS.ByteString, Char)
splitLine l =
  case T.splitOn "\t" l of
    [k, v] | not (T.null k) && not (T.null v) -> Just (encodeUtf8 k, T.head v)
    _ -> Nothing

-- Helper to lift a Trie into TH Exp
liftTrie :: Trie.Trie Char -> Q Exp
liftTrie t = [| Trie.fromList $(liftList (Trie.toList t)) |]
  where
    liftList :: [(BS.ByteString, Char)] -> Q Exp
    liftList xs = listE [ [| ($(litE (stringL (BS.unpack k))), $(lift v)) |] | (k, v) <- xs ]