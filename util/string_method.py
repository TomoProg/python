#-*- coding:utf-8 -*-

# 結合
print("----- \"abc\" + \"def\" -----")
print("abc" + "def")
# "abcdef"

# 繰り返し
print("----- \"abc\"*3 -----")
print("abc"*3)
# "abcabcabc"

# 部分文字列取得
print("----- \"abcdefghi\"[3] -----")
print("abcdefghi"[3])
# "d"

print("----- \"abcdefghi\"[3:6] -----")
print("abcdefghi"[3:6])
# "def"

print("----- \"abcdefghi\"[-6] -----")
print("abcdefghi"[-6])
# "d"

# split
print("----- split() -----")
print("abc def ghi".split())
# ["abc", "def", "ghi"]

print("----- split(\",\") -----")
print("abc,def".split(","))
# ["abc", "def"]

# strip
print("----- strip() -----")
print(" abcdef  ".strip())
# "abcdef"

# rstrip
print("----- rstrip() -----")
print(" abcdef  ".rstrip())
# " abcdef"

# lstrip
print("----- lstrip() -----")
print(" abcdef  ".lstrip())
# "abcdef  "

# len
print("----- len() -----")
print(len("abcdefg"))
print(len("あいうえお"))
# 7
# 5

# count
print("----- count() -----")
print("abcabcabc".count("abc"))
# 3

# find
print("----- find() -----")
print("abcdefghijk".find("f"))
print("abcdefghijk".find("x"))
# 5
# -1

# replace
print("----- replace() -----")
print("abcdefghijk".replace("de", "xx"))
# "abcxxfghijk"

# join
print("----- join() -----")
print(",".join("abcdefg"))
# "a,b,c,d,e,f,g"

