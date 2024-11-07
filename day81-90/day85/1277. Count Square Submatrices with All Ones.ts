function countSquares(matrix: number[][]): number {
  const m: number = matrix.length;
  const n: number = matrix[0].length;
  let totalSquares: number = 0;

  for (let i: number = 0; i < m; i++) {
    for (let j: number = 0; j < n; j++) {
      if (matrix[i][j] == 1) {
        if (i > 0 && j > 0) {
          matrix[i][j] =
            Math.min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) +
            1;
        }
        totalSquares += matrix[i][j];
      }
    }
  }

  return totalSquares;
}
