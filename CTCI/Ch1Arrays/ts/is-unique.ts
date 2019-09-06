function isUnique(str: string): Boolean {
  let sety = new Set();

  for (let s of str) {
    if (sety.has(s)) {
      return false;
    }

    sety.add(s);
  }
  return true;
}

console.log(isUnique("12344"));
console.log(isUnique("1234"));
