#!/usr/bin/env runghc
module Main where

import System.Process
import System.FilePath
import System.Directory
import Prelude
import Control.Exception (catch, throwIO)

main :: IO ()
main = do
  files <- listDirectory "."
  let svgs = filter (\f -> takeExtension f == ".svg") files
  mapM_ optimizeSVG svgs

optimizeSVG :: FilePath -> IO ()
optimizeSVG file = body `catch` errorHandler
  where
  errorHandler :: IOError -> IO ()
  errorHandler e = do
    putStrLn $ "Error optimizing " ++ file ++ ": " ++ show e
    throwIO e
  body = do
    let outputFile = dropExtension file <> "_.svg"
    callProcess "python3" ["svg_abs_lines.py", file, outputFile]
    putStrLn $ "Optimized: " ++ file
    renameFile outputFile file