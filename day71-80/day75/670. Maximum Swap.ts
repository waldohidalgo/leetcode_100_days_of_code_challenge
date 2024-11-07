class Solution {
  maximumSwap(num: number): number {
    let s = num.toString().split("").map(Number);
    let n = s.length;

    if (n === 1) {
      return num;
    } else if (n === 2) {
      if (s[0] < s[1]) {
        [s[0], s[1]] = [s[1], s[0]];
        return parseInt(s.join(""), 10);
      } else {
        return num;
      }
    } else {
      let arr: [number, number][] = Array(n).fill([-1, -1]);

      for (let i = n - 2; i >= 0; i--) {
        arr[i] = arr[i + 1][0] >= s[i + 1] ? arr[i + 1] : [s[i + 1], i + 1];
      }

      for (let i = 0; i < n; i++) {
        let val = s[i];
        if (arr[i][0] > val) {
          [s[i], s[arr[i][1]]] = [s[arr[i][1]], s[i]];
          return parseInt(s.join(""), 10);
        }
      }
      return num;
    }
  }
}
