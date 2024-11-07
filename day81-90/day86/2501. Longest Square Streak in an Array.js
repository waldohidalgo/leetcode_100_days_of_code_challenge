/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function (nums) {
  const hashMap = {};

  for (const num of nums) {
    if (!(num in hashMap)) {
      hashMap[num] = 1;
    }
  }

  const initChecked = new Set();
  let maxStreak = -1;

  for (const num of nums) {
    if (initChecked.has(num)) {
      continue;
    }

    const sqrt = Math.sqrt(num);
    if (Number.isInteger(sqrt) && sqrt in hashMap) {
      continue;
    }

    let streak = 1;
    let current = num;

    while (current ** 2 in hashMap) {
      streak += 1;
      current = current ** 2;
    }

    if (streak >= 2 && streak > maxStreak) {
      maxStreak = streak;
    }

    if (maxStreak === 5) {
      return maxStreak;
    }
    initChecked.add(num);
  }

  return maxStreak;
};

const nums = [4, 3, 6, 16, 8, 2];
console.log(longestSquareStreak(nums));
