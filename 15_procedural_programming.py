# Algoritm for chacking if a word is palindrome

str = "racecar"

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) -1

    for char in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(isPalindrome("racecar"))