const sort = (s: string) =>
  s
    .split("")
    .sort()
    .join("");

function checkPermutation(s1: string, s2: string): Boolean {
  return sort(s1) === sort(s2);
}

console.log(checkPermutation("abcd", "bacd"));
console.log(checkPermutation("abcd", "defg"));
