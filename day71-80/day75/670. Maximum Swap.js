var Solution = /** @class */ (function () {
  function Solution() {}
  Solution.prototype.maximumSwap = function (num) {
    var _a, _b;
    var s = num.toString().split("").map(Number);
    var n = s.length;
    if (n === 1) {
      return num;
    } else if (n === 2) {
      if (s[0] < s[1]) {
        (_a = [s[1], s[0]]), (s[0] = _a[0]), (s[1] = _a[1]);
        return parseInt(s.join(""), 10);
      } else {
        return num;
      }
    } else {
      var arr = Array(n).fill([-1, -1]);
      for (var i = n - 2; i >= 0; i--) {
        if (arr[i + 1][0] >= s[i + 1]) {
          arr[i] = arr[i + 1];
        } else {
          arr[i] = [s[i + 1], i + 1];
        }
      }
      for (var i = 0; i < n; i++) {
        var val = s[i];
        if (arr[i][0] > val) {
          (_b = [s[arr[i][1]], s[i]]), (s[i] = _b[0]), (s[arr[i][1]] = _b[1]);
          return parseInt(s.join(""), 10);
        }
      }
      return num;
    }
  };
  return Solution;
})();

sol = new Solution();
console.log(sol.maximumSwap(1993));
