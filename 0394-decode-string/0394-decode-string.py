class Solution:
    def decodeString(self, s: str) -> str:
     
     stack = []
     for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            # Build the substring inside brackets
            a = ""
            while stack[-1] != '[':
                a = stack.pop() + a
            stack.pop()  # Remove the '['

            # Build the multiplier (digit part)
            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier

            # Set multiplier to 1 if it's empty
            multiplier = int(multiplier) if multiplier else 1

            # Append the expanded string
            stack.append(a * multiplier)

     return "".join(stack)