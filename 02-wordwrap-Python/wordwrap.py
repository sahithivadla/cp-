# Write the function wordWrap(text, width) that takes a string of text (containing only lowercase letters
#  or spaces) and a positive integer width, and returns a possibly-multiline string that matches the
# original string, only with line wrapping at the given width. So wordWrap("abc", 3) just returns "abc",
# but wordWrap("abc",2) returns a 2-line string, with "ab" on the first line and "c" on the second line.
# After you complete word wrapping in this way, only then: All spaces at the start and end of each
# resulting line should be removed, and then all remaining spaces should be converted to dashes ("-"),
# so they can be easily seen in the resulting string. Here are some test cases for you:
# assert(wordWrap("  abcdefghij", 4)  ==  """\
# abcd
# efgh
# ij""")

# assert(wordWrap(" a b c de fgh ",  4)  ==  """\
# a-b-
# c-de
# -fgh""")


def fun_wordwrap(s, n):
	s = s.strip()
	print(s)
	if(" " in s):
		res =""
		for i in s:
			if(i == " "):
				res=res+"-"
			else:
				res=res+i
		s =res
	print(s)
	r =""
	k=0
	for i in range(0,len(s)):
		if(k==n):
			r=r+"\n"+s[i]
			k=0
		else:
			r=r+s[i]
		k=k+1
	return r



	return ""


