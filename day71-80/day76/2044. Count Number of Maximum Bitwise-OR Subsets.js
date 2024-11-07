/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function (nums) {
  function getCombinations(arr, r) {
    const results = [];

    function combine(start, combination) {
      if (combination.length === r) {
        results.push([...combination]);
        return;
      }

      for (let i = start; i < arr.length; i++) {
        combination.push(arr[i]);
        combine(i + 1, combination);
        combination.pop();
      }
    }

    combine(0, []);
    return results;
  }
  let max_or = 0;
  let count = 0;
  for (let num of nums) {
    max_or |= num;
  }

  for (let r = 1; r <= nums.length; r++) {
    for (let comb of getCombinations(nums, r)) {
      let or = 0;
      for (let num of comb) {
        or |= num;
      }
      if (or === max_or) {
        count++;
      }
    }
  }
  return count;
};

console.log(countMaxOrSubsets([3, 2, 1, 5]));
