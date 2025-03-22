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
"""
def is_palindrome(s):
    return s == s[::-1]
    

def get_large_palindrome_substring(s):
    ss1 = ''
    for i in range(len(s)):
        ss = s[i:]
        if is_palindrome(ss):
            ss1 = ss
            break
    
    
    ss2 = ''
    sr = s[::-1]
    for i in range(len(sr)):
        ss = sr[i:]
        if is_palindrome(ss):
            ss2 = ss
            break
    return ss1 if len(ss1)>len(ss2) else ss2


if __name__ == '__main__':
    s = 'abc'
    print(get_large_palindrome_substring(s))
