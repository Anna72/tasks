class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = 0
        e = len(s) - 1
        while (b <= e):
            if (not s[b].isalnum()):
                b += 1
            else:
                if (not s[e].isalnum()):
                    e -= 1
                else: 
                    if (s[b].lower() != s[e].lower()):
                        return(False)
                    else:
                        b += 1
                        e -= 1
        return(True)
