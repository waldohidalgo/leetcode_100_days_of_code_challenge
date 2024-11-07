function minimumMountainRemovals(nums: number[]): number {
  const n = nums.length;
  const lis = new Array(n).fill(1);
  const lds = new Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        lis[i] = Math.max(lis[i], lis[j] + 1);
      }
    }
  }

  for (let i = n - 2; i >= 0; i--) {
    for (let j = n - 1; j > i; j--) {
      if (nums[j] < nums[i]) {
        lds[i] = Math.max(lds[i], lds[j] + 1);
      }
    }
  }

  return (
    n -
    Math.max(
      ...Array.from({ length: n }, (_, i) =>
        lis[i] > 1 && lds[i] > 1 ? lis[i] + lds[i] - 1 : 0
      )
    )
  );
}
