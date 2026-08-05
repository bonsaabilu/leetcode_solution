class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        def isInteger(token: str) -> bool:
            if not token:
                return False
            if token[0] in ['+', '-']:
                token = token[1:]
            return token.isdigit() and len(token) > 0

        def isDecimal(token: str) -> bool:
            if not token:
                return False
            if token[0] in ['+', '-']:
                token = token[1:]
            if '.' not in token:
                return False
            left, right = token.split('.', 1)
            # At least one side must have digits
            if left == '' and right == '':
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True

        # Split by exponent
        if 'e' in s or 'E' in s:
            base, exp = s.split('e', 1) if 'e' in s else s.split('E', 1)
            if not base or not exp:
                return False
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        else:
            return isInteger(s) or isDecimal(s)
