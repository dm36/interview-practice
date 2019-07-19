# roman numerals represented by seven different symbols
# I, V, X, L, C, D, M
# 1, 5, 10, 50, 100, 500, 1000

# two is written as II, twelve is written as X + II, 27
# is written as XXVII, XX + V + II

# largest to smallest from left to right

# four is not IIII- number four is written as IV
# number nine is represented as IX

# subtraction is used:
# if I can be placed before V and X to make 4 and 9
# X can be placed before L and C (50 and 100) to make
# 40 and 90
# C can be placed before D (500) and M (1000) to make
# 400 and 900

# so have to consider IV, IX, XL, XC, CD, CM

# roman numeral -> integer

# go through each character in the string
# left to right


def romanToInt(s):
    subs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    val = 0

    while i < len(s):
        if i < len(s) - 1 and s[i] in ['I', 'X', 'C'] and (s[i] + s[i+1]) in subs:
            val += subs[s[i] + s[i+1]]
            i += 2
        else:
            val += symbol[s[i]]
            i += 1
    return (val)

# class Solution:
# # @param {string} s
# # @return {integer}
# def romanToInt(self, s):
#     roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
#     z = 0
#     for i in range(0, len(s) - 1):
#         if roman[s[i]] < roman[s[i+1]]:
#             z -= roman[s[i]]
#         else:
#             z += roman[s[i]]
#     return z + roman[s[-1]]

# d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#
# def romanToInt(self, s):
#     res, p = 0, 'I'
#     for c in s[::-1]:
#         res, p = res - d[c] if d[c] < d[p] else res + d[c], c
#     return res
#

# replace short forms with long forms
# look at the double replace
# seems to order the replaces from low to high value

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number
#
# if you see an I followed by a V
# you would get 6 if you handled that ordinarily-
# but you really want 4- which is why we
# subtract 2 from the sum

# same idea for the rest

# public int romanToInt(String s) {
#      int sum=0;
#     if(s.indexOf("IV")!=-1){sum-=2;}
#     if(s.indexOf("IX")!=-1){sum-=2;}
#     if(s.indexOf("XL")!=-1){sum-=20;}
#     if(s.indexOf("XC")!=-1){sum-=20;}
#     if(s.indexOf("CD")!=-1){sum-=200;}
#     if(s.indexOf("CM")!=-1){sum-=200;}
#
#     char c[]=s.toCharArray();
#     int count=0;
#
#    for(;count<=s.length()-1;count++){
#        if(c[count]=='M') sum+=1000;
#        if(c[count]=='D') sum+=500;
#        if(c[count]=='C') sum+=100;
#        if(c[count]=='L') sum+=50;
#        if(c[count]=='X') sum+=10;
#        if(c[count]=='V') sum+=5;
#        if(c[count]=='I') sum+=1;
#
#    }
#
#    return sum;
#
# }

# public static int romanToInt(String s) {
# 	int res = 0;
# 	for (int i = s.length() - 1; i >= 0; i--) {
# 		char c = s.charAt(i);
# 		switch (c) {
# 		case 'I':
# 			res += (res >= 5 ? -1 : 1);
# 			break;
# 		case 'V':
# 			res += 5;
# 			break;
# 		case 'X':
# 			res += 10 * (res >= 50 ? -1 : 1);
# 			break;
# 		case 'L':
# 			res += 50;
# 			break;
# 		case 'C':
# 			res += 100 * (res >= 500 ? -1 : 1);
# 			break;
# 		case 'D':
# 			res += 500;
# 			break;
# 		case 'M':
# 			res += 1000;
# 			break;
# 		}
# 	}
# 	return res;
# }

print (romanToInt('III'))
print (romanToInt('IV'))
print (romanToInt('IX'))
print (romanToInt('LVIII'))
print (romanToInt('MCMXCIV'))
