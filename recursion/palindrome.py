def isPalindrome(s):
    s = "".join([letter.lower() for letter in s if letter.isalnum()])
    if len(s) <= 0:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    return isPalindrome(s[1 : len(s) - 1])


print(isPalindrome("ABCDCBA"))
