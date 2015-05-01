#-*- coding:utf-8 -*-

# 結合
print("----- \"abc\" + \"def\" -----")
print("abc" + "def")

# 繰り返し
print("----- \"abc\"*3 -----")
print("abc"*3)

# 部分文字列取得
print("----- \"abcdefghi\"[3] -----")
print("abcdefghi"[3])

print("----- \"abcdefghi\"[3:6] -----")
print("abcdefghi"[3:6])

print("----- \"abcdefghi\"[-6] -----")
print("abcdefghi"[-6])

# split
print("----- split() -----")
print("abc def ghi".split())

print("----- split(\",\") -----")
print("abc,def".split(","))

# strip
print("----- strip() -----")
print(" abcdef  ".strip())

# rstrip
print("----- rstrip() -----")
print(" abcdef  ".rstrip())

# lstrip
print("----- lstrip() -----")
print(" abcdef  ".lstrip())

# len
print("----- len() -----")
print(len("abcdefg"))
print(len("あいうえお"))

# count
print("----- count() -----")
print("abcabcabc".count("abc"))

# find
print("----- find() -----")
print("abcdefghijk".find("f"))
print("abcdefghijk".find("x"))

# replace
print("----- replace() -----")
print("abcdefghijk".replace("de", "xx"))

# join
print("----- join() -----")
print(",".join("abcdefg"))
