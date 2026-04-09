{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TemplateHaskell #-}

import Prelude
import Data.List (isSuffixOf)
import System.Directory
import System.FilePath
import System.Environment
import System.Process ( readProcess, callProcess)
import qualified Data.ByteString.Char8 as BS8
import qualified Data.Array as Array
import Data.Array (Array, bounds)
import Data.Traversable (forM)
import Data.Foldable (forM_)

import Data.FileEmbed (embedFile)

svgprefix :: String
svgprefix = BS8.unpack $(embedFile $ "data" </> "prefix.txt")

svgsuffix :: String
svgsuffix = BS8.unpack $(embedFile $ "data" </> "suffix.txt")

main :: IO ()
main = do
  [outputFolder, onset, vowel] <- getArgs
  putStrLn $ "Output folder: " <> outputFolder
  putStrLn $ "Input folders: " <> unlines [onset, vowel]
  -- create output folder if it doesn't exist
  createDirectoryIfMissing True outputFolder
  -- combine SVGs from onset and vowel folders into output folder
  combineSVGs outputFolder onset vowel
  makeTable "Onsets" ((onset </>) <$> onsetOrder)
  makeTable "Nuclei" ((vowel </>) <$> nuclueusOrder2D)
  makeTable "Syllables" ((outputFolder </>) <$> syllableOrder2D)

-- | Pattern | Onset | Symbol |
-- | ------- | ----- | ------ |
-- |   1     | p     | ⚊      |
-- |  11     | t     | ⚌      |
-- |  91     | m     | ⚍      |
-- | 191     | n     | ☲      |
-- | 111     | h     | ☰      |
-- |   9     | k     | ⚋      |
-- |  19     | s     | ⚎      |
-- | 119     | ts    | ☴      |
-- |  99     | l     | ⚏      |
-- | 199     | r     | ☶      |

onsetOrder :: Array (Int, Int) String
onsetOrder = Array.listArray ((0, 0), (0, 9)) ["p", "t", "m", "n", "h", "k", "s", "ts", "l", "r"]

-- | Pattern | Value | Symbol  |
-- | ------- | ----- | -----   |
-- | 111     | i     | ☰      |
-- | 119     | ĩ     | ☴      |
-- | 191     | a     | ☲      |
-- | 199     | ã     | ☶      |
-- | 911     | o     | ☱      |
-- | 919     | e     | ☵      |
-- | 991     | u     | ☳      |
-- | 999     | ũ     | ☷      |

-- we use "in", "an", and "un" to represent the nasalized vowels, so the file names are ascii.

nuclueusOrder2D :: Array (Int, Int) String
nuclueusOrder2D = Array.listArray ((0, 0), (2, 7))
  $  vowelOrder
  ++ [addSimpleGlide v | v <- vowelOrder]
  ++ [addCrossGlide v | v <- vowelOrder]
  where
    vowelOrder = ["i", "in", "a", "an", "o", "e", "u", "un"]
    addSimpleGlide str =
      if head str `elem` ['i', 'e']
        then "y" <> str
        else "w" <> str
    addCrossGlide str =
      if head str `elem` ['i', 'e']
        then "w" <> str
        else "y" <> str

syllableOrder2D :: Array (Int, Int) String
syllableOrder2D = Array.listArray ((0, 0), (9, 23))
  [ o <> v
  | o <- Array.elems onsetOrder
  , v <- Array.elems nuclueusOrder2D
  ]

combineSVGs :: FilePath -> FilePath -> FilePath -> IO ()
combineSVGs outputFolder folderA folderB = do
  putStrLn $ "Combining SVGs from " <> folderA <> " and " <> folderB
  -- get all files in folderA and folderB
  filesA <- listDirectory folderA
  filesB <- listDirectory folderB
  -- filter for .svg files
  let svgFilesA = filter (isSuffixOf ".svg") filesA
      svgFilesB = filter (isSuffixOf ".svg") filesB
  -- combine each combination of files from A and B
  forM_ svgFilesA $ \fileA -> do
    forM_ svgFilesB $ \fileB -> do
      let outputFile = outputFolder </> (takeBaseName fileA ++ "_" ++ takeBaseName fileB ++ ".svg")
      combineSVG (folderA </> fileA) (folderB </> fileB) outputFile

combineSVG :: FilePath -> FilePath -> FilePath -> IO ()
combineSVG onsetFile vowelFile outputFile = do
  putStrLn $ "Combining " <> onsetFile <> " and " <> vowelFile <> " into " <> outputFile

  -- get the d attribute from the SVG files using rg (ripgrep)
  onsetPaths <- readProcess "rg" ["-o", "-r", "$1", " d=\"([^\"]*)\"", onsetFile] ""
  vowelPaths <- readProcess "rg" ["-o", "-r", "$1", " d=\"([^\"]*)\"", vowelFile] ""

  putStrLn $ "Extracted paths from " <> onsetFile <> ":\n" <> onsetPaths
  putStrLn $ "Extracted paths from " <> vowelFile <> ":\n" <> vowelPaths

  let paths = unwords (lines onsetPaths ++ lines vowelPaths)

  writeFile outputFile $ concat [svgprefix, paths, svgsuffix]

-- | Use ImageMagick's montage command to create a table of labeled images.
makeTable :: String -> Array (Int, Int) FilePath -> IO ()
makeTable tableName filePaths = do
  labledFiles <- filePaths `forM` \ path -> do
    let fileName = takeBaseName path
    addLable fileName fileName
  let tableDims = show (endRow - startRow + 1) <> "x" <> show (endCol - startCol + 1)
        where ((startRow, startCol), (endRow, endCol)) = bounds filePaths
  let montageArgs = Array.elems labledFiles <> ["-tile", tableDims, "-geometry", "+20+20", tableName <.> "png", "-title", tableName]
  callProcess "montage" montageArgs ""
  removeFile `forM_` labledFiles

-- | Add a label to the bottom of an image using ImageMagick's convert command.
addLable :: String -> String -> IO FilePath
addLable label path = do
  let outputFile = path <.> "labeled" <.> "png"
  callProcess "convert" [path, "-gravity", "north", "-pointsize", "20", "-annotate", "+0+10", label, outputFile] ""
  return outputFile
