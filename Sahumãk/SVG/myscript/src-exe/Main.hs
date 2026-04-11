{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE RecordWildCards #-}

import Prelude
import Data.List (isSuffixOf, intercalate, nub)
import System.Directory
import System.FilePath
import System.Environment (getArgs)
import System.Exit
import System.Process ( readProcess, callProcess, readCreateProcessWithExitCode, proc)
import qualified Data.ByteString.Char8 as BS8
import qualified Data.Array as Array
import Data.Array (Array, bounds)
import Data.Traversable (forM)
import Data.Foldable (forM_)
import qualified Data.Text as T

import Data.FileEmbed (embedFile)
import Text.Printf

mergeTemplate, addLabelTemplate :: String
mergeTemplate = BS8.unpack $(embedFile "data/mergeTemplate.svg")
addLabelTemplate = BS8.unpack $(embedFile "data/addLabelTemplate.svg")

main :: IO ()
main = do
  [outputFolder, onset, vowel] <- getArgs
  putStrLn $ "Output folder: " <> outputFolder
  putStrLn $ "Input folders: " <> unlines [onset, vowel]
  -- create output folder if it doesn't exist
  createDirectoryIfMissing True outputFolder
  -- combine SVGs from onset and vowel folders into output folder
  normalizeSVGs onset
  normalizeSVGs vowel
  -- combineSVGs outputFolder onset vowel
  -- makeTable "Onsets" ((onset </>) <$> onsetOrder)
  makeTable "Nuclei" ((vowel </>) <$> nuclueusOrder2D)
  -- makeTable "Syllables" ((outputFolder </>) <$> syllableOrder2D)

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
    isFrontVowel ('i' : _) = True
    isFrontVowel ('e' : _) = True
    isFrontVowel _         = False
    vowelOrder = ["i", "in", "a", "an", "o", "e", "u", "un"]
    addSimpleGlide str =
      if isFrontVowel str
        then "y" <> str
        else "w" <> str
    addCrossGlide str =
      if isFrontVowel str
        then "w" <> str
        else "y" <> str

syllableOrder2D :: Array (Int, Int) String
syllableOrder2D = Array.listArray ((0, 0), (9, 23))
  [ o <> v
  | o <- Array.elems onsetOrder
  , v <- Array.elems nuclueusOrder2D
  ]

getPaths :: FilePath -> IO [String]
getPaths file = lines <$> readProcess "rg" ["-o", "-r", "$1", " d=\"([^\"]*)\"", file] ""

combineSVGs :: FilePath -> FilePath -> FilePath -> IO ()
combineSVGs outputFolder folderA folderB = do
  putStrLn $ "Combining SVGs from " <> folderA <> " and " <> folderB
  -- get all .svg files in folderA and folderB
  svgFilesA <- filter (".svg" `isSuffixOf`) <$> listDirectory folderA
  svgFilesB <- filter (".svg" `isSuffixOf`) <$> listDirectory folderB

  -- print the files found in each folder
  putStrLn $ "Files in " <> folderA <> ":\n" <> unlines svgFilesA
  putStrLn $ "Files in " <> folderB <> ":\n" <> unlines svgFilesB

  -- combine each combination of files from A and B
  forM_ svgFilesA $ \fileA -> do
    forM_ svgFilesB $ \fileB -> do
      let outputFile = outputFolder </> (takeBaseName fileA ++ takeBaseName fileB ++ ".svg")
      combineSVG (folderA </> fileA) (folderB </> fileB) outputFile

combineSVG :: FilePath -> FilePath -> FilePath -> IO ()
combineSVG onsetFile vowelFile outputFile = do
  putStrLn $ "Combining " <> onsetFile <> " and " <> vowelFile <> " into " <> outputFile

  -- get the d attribute from the SVG files using rg (ripgrep)
  onsetPaths <- getPaths onsetFile
  putStrLn $ "Extracted paths from " <> onsetFile <> ":\n" <> unlines onsetPaths

  vowelPaths <- getPaths vowelFile
  putStrLn $ "Extracted paths from " <> vowelFile <> ":\n" <> unlines vowelPaths

  let paths = unwords (onsetPaths ++ vowelPaths)

  writeFile outputFile $ printf mergeTemplate paths
  putStrLn $ "Written combined SVG to " <> outputFile

-- | Use ImageMagick's montage command to create a table of labeled images.
makeTable :: String -> Array (Int, Int) FilePath -> IO ()
makeTable tableName filePaths = do
  let svgFiles = (<.> "svg") <$> filePaths
  putStrLn $ "Creating table " <> tableName <> " with files:\n" <> unlines (Array.elems svgFiles)
  labledFiles <- svgFiles `forM` \ path -> do
    let fileName = takeBaseName path
    makeLabeledSVG path fileName "labeled.svg"

  let tableDims = show (endCol - startCol + 1) <> "x" <> show (endRow - startRow + 1)
        where ((startRow, startCol), (endRow, endCol)) = bounds filePaths
  let montageArgs :: [String] = Array.elems labledFiles <> ["-tile", tableDims, "-geometry", "+20+20", "-title", tableName, tableName <.> "png"]
  putStrLn $ "Running montage with arguments:\n" <> unlines montageArgs
  callProcess "montage" montageArgs
  -- removeFile `mapM_` labledFiles

makeLabeledSVG :: FilePath -> String -> FilePath -> IO FilePath
makeLabeledSVG inputFile label outputSufix = do
  let outputFile = inputFile -<.> outputSufix
  putStrLn $ "Adding label " <> label <> " to " <> inputFile <> " and saving as " <> outputFile
  let labelText = T.unpack label
  -- get the d attribute from the SVG file using rg (ripgrep)
  paths <- getPaths inputFile
  putStrLn $ "Extracted paths from " <> inputFile <> ":\n" <> unlines paths
  let pathsElems = mkPathElems paths
      svgContent = printf addLabelTemplate labelText pathsStr
  writeFile outputFile svgContent
  pure outputFile

makePathElems :: [String] -> String
makePathElems ds =
  unlines
    [ printf "<path style=\"fill:none;stroke:#000000;stroke-width:4;stroke-linecap:round;stroke-linejoin:round\" d=\"%s\" />" d
    | d <- ds
    ]

normalizeSVGs :: FilePath -> IO ()
normalizeSVGs folder = do
  putStrLn $ "Normalizing SVGs in folder: " <> folder

  haveTransform <- rgFiles "transform=" folder
  haveGrid      <- rgFiles "grid" folder

  let svgFiles = nub (haveTransform ++ haveGrid)

  putStrLn $ "SVG files to normalize:\n" <> unlines svgFiles

  let actions = intercalate ";"
        [ "select-all:groups"
        , "selection-ungroup"
        , "select-all:no-groups"
        , "object-to-path"
        , "com.klowner.filter.apply-transform"
        , "export-plain-svg"
        , "export-do"
        , "window-close"
        ]

  forM_ svgFiles $ \file -> do
    putStrLn $ "Normalizing " <> file

    let outFile = replaceExtension file "normalized.svg"
        inkscapeArgs =
          [ "-g"
          , file
          , "--export-type=svg"
          , "-o"
          , outFile
          , "--actions=" ++ actions
          ]

    putStrLn $ "Running Inkscape with arguments:\n" <> unlines inkscapeArgs
    callProcess "inkscape" inkscapeArgs

    -- Replace original file with normalized output
    renameFile outFile file

rgFiles :: String -> FilePath -> IO [FilePath]
rgFiles regexpr folder = do
  let p = proc "rg" ["-l", "-e", regexpr, folder]
  (exitCode, stdoutText, stderrText) <- readCreateProcessWithExitCode p ""

  case exitCode of
    ExitSuccess   -> pure (lines stdoutText)
    ExitFailure 1 -> pure []  -- no matches
    ExitFailure _ -> error $
      "rg failed for pattern " <> show regexpr <> ":\n" <> stderrText