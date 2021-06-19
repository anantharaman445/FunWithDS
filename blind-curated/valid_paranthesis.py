
def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in ["(", "{", "["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            pop_ch = stack.pop()
            if pop_ch == '(' and ch != ')':
                return False 
            if pop_ch == '{' and ch != '}':
                return False
            if pop_ch == '[' and ch != ']':
                return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    
    print(isValid("{[]}"))