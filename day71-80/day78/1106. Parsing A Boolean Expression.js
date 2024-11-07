class Solution {
  parseBoolExpr(expression) {
    const parse = (expression) => {
      if (expression === "t") {
        return true;
      } else if (expression === "f") {
        return false;
      }

      if (expression[0] === "!") {
        return parseNot(expression.slice(2, -1));
      }

      if (expression[0] === "&") {
        return parseAnd(expression.slice(2, -1));
      }

      if (expression[0] === "|") {
        return parseOr(expression.slice(2, -1));
      }

      throw new Error("Expresión inválida");
    };

    const parseNot = (subExpr) => {
      return !parse(subExpr);
    };

    const parseAnd = (subExpr) => {
      const subExpressions = splitExpressions(subExpr);
      return subExpressions.every((expr) => parse(expr));
    };

    const parseOr = (subExpr) => {
      const subExpressions = splitExpressions(subExpr);
      return subExpressions.some((expr) => parse(expr));
    };

    const splitExpressions = (expression) => {
      const subExpressions = [];
      let balance = 0;
      let currentExpr = [];

      for (const char of expression) {
        if (char === "," && balance === 0) {
          subExpressions.push(currentExpr.join(""));
          currentExpr = [];
        } else {
          currentExpr.push(char);
          if (char === "(") {
            balance += 1;
          } else if (char === ")") {
            balance -= 1;
          }
        }
      }
      subExpressions.push(currentExpr.join(""));
      return subExpressions;
    };
    return parse(expression);
  }
}

sol = new Solution();
expression = "!(&(f,t))";
console.log(sol.parseBoolExpr(expression));
