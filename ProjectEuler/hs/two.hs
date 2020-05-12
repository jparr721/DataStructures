-- fibbonaci
module Main where
import System.Environment

fib :: Int -> Integer
fib = (map f [0 ..] !!)
    where f 0 = 1
          f 1 = 2
          f n = fib(n - 1) + fib(n - 2)

main = do
  let fibs = sum (filter even [fib x | x <- [0..35]])
  print fibs
