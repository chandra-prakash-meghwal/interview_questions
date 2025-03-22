"""
case1
input = 'a'
output = 'a'

case2
input = 'rabar'
output = 'rabar'

case3
input = 'rabara'
output = 'rabar'

case4
input = ''
output = ''

case5
input = 'abc'
output = 'a' // also can be 'b' or 'c'

case6
input = 'cabak'
output = 'aba'
"""

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def get_largest_palindrome_substring(s):
    """Find the largest palindrome substring in a given string."""
    largest_palindrome = ""
    
    # Iterate over all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            
            # Check if the substring is a palindrome
            if is_palindrome(substring):
                # Update the largest palindrome if necessary
                if len(substring) > len(largest_palindrome):
                    largest_palindrome = substring
                    
    return largest_palindrome

if __name__ == '__main__':
    s = 'cabak'
    print(get_largest_palindrome_substring(s))


if __name__ == '__main__':
    s = 'abc'
    print(get_large_palindrome_substring(s))
