B = input(" ")

if B in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
	print("%s vowel." % B)
elif B == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for constant.")
else:
	print("%s constant." % B)
