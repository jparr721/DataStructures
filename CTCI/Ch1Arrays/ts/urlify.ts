function urlify(s: string): string {
  let last_index = 0;

  for (let i = s.length - 1; i > 0; i--) {
    if (s[i] != " ") {
      last_index = i;
      break;
    }
  }

  return s
    .split("")
    .reduce(
      (acc: any, cur: any, index: number) => {
        if (cur === " " && index < last_index) {
          acc.push("%20");
        } else {
          acc.push(cur);
        }
        return acc;
      },
      [] as Array<any>
    )
    .join("");
}

function urlifyClean(s: string): string {
  return s
    .trim()
    .split("")
    .reduce(
      (acc: any, cur: any) => {
        cur === " " ? acc.push("%20") : acc.push(cur);
        return acc;
      },
      [] as any[]
    )
    .join("");
}

console.log(urlify("www.a     bc.com     "));
console.log(urlifyClean("www.a     bc.com     "));
