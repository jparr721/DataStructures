-- prime factors
module Main where

prime x = [

main = do
  let v = 13195
  let fac = [x | x <- [2..v], v `mod` x == 0]
  print fac
