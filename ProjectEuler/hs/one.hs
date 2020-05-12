m3 x = x `mod` 3 == 0
m5 x = x `mod` 5 == 0

main = do
  let ls = sum[x | x <- [0..999], m3 x || m5 x]
  print ls
