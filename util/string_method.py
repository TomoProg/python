#-*- coding:utf-8 -*-

src_str = None
dest_str = None

# 結合
print("----- \"abc\" + \"def\" -----")
print("abc" + "def")
print()

# 繰り返し
print("----- \"abc\"*3 -----")
print("abc"*3)
print()

# 部分文字列取得
print("----- \"abcdefghi\"[3] -----")
print("abcdefghi"[3])
print()

print("----- \"abcdefghi\"[3:6] -----")
print("abcdefghi"[3:6])
print()

print("----- \"abcdefghi\"[-6] -----")
print("abcdefghi"[-6])
print()

# split
src_str = "abc def ghi"
dest_str = src_str.split()
print("----- split() -----")
print(src_str, "=>", dest_str)
print()

src_str = "abc,def"
dest_str = src_str.split(",")
print("----- split(\",\") -----")
print(src_str, "=>", dest_str)
print()

# strip
src_str = " abcdef  "
dest_str = src_str.strip()
print("----- strip() -----")
print("\"" + src_str + "\"", "=>", "\"" + dest_str + "\"")
print()

# rstrip
src_str = " abcdef  "
dest_str = src_str.rstrip()
print("----- rstrip() -----")
print("\"" + src_str + "\"", "=>", "\"" + dest_str + "\"")
print()

# lstrip
src_str = " abcdef  "
dest_str = src_str.lstrip()
print("----- lstrip() -----")
print("\"" + src_str + "\"", "=>", "\"" + dest_str + "\"")
print()

# len
print("----- len() -----")
print("len(\"abcdefg\"):%d" % len("abcdefg"))
print("len(\"あいうえお\"):%d" % len("あいうえお"))
print()

# count
print("----- count() -----")
print("\"abcabcabc\".count(\"abc\"):%d" % "abcabcabc".count("abc"))
print()

# find
print("----- find() -----")
print("\"abcdefghijk\".find(\"f\"):%d" % "abcdefghijk".find("f"))
print("\"abcdefghijk\".find(\"x\"):%d" % "abcdefghijk".find("x"))
print()

# replace
print("----- replace() -----")
print("\"abcdefghijk\".replace(\"de\", \"xx\")" + " => " + "abcdefghijk".replace("de", "xx"))
print()

# join
print("----- join() -----")
print("\",\".join(\"abcdefg\")" + " => " + ",".join("abcdefg"))
print()

