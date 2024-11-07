class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(expression: str) -> bool:
            if expression == 't':
                return True
            elif expression == 'f':
                return False

            if expression[0] == '!':
                return parse_not(expression[2:-1])  

            if expression[0] == '&':
                return parse_and(expression[2:-1])  

            if expression[0] == '|':
                return parse_or(expression[2:-1])  

            raise ValueError("Expresión inválida")
        
        def parse_not(subExpr: str) -> bool:  
            return not parse(subExpr)

        def parse_and(subExpr: str) -> bool:   
            sub_expressions = split_expressions(subExpr)
            return all(parse(expr) for expr in sub_expressions)

        def parse_or(subExpr: str) -> bool:
            sub_expressions = split_expressions(subExpr)
            return any(parse(expr) for expr in sub_expressions)

        def split_expressions(expression: str) -> list:
            sub_expressions = []
            balance = 0
            current_expr = []
            for char in expression:
                if char == ',' and balance == 0:
                    sub_expressions.append(''.join(current_expr))
                    current_expr = []
                else:
                    current_expr.append(char)
                    if char == '(':
                        balance += 1
                    elif char == ')':
                        balance -= 1
            sub_expressions.append(''.join(current_expr))  
            return sub_expressions
        return parse(expression)


sol=Solution()
expression="!(&(f,t))"
print(sol.parseBoolExpr(expression))