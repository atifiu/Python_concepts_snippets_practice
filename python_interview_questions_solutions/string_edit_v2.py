## Interview question Dec 2023 Agoda: you have two strings and have to find if they are same and you are allowed to make one edit
## i.e. delete 1 char, insert 1 char or repalce 1 char. Return True if two strings are same else return False.

# Python program to check if given two strings are
# at distance one

# Returns true if edit distance between s1 and s2 is
# one, else false
def isEditDistanceOne(s1, s2):

	# Find lengths of given strings
	m = len(s1)
	n = len(s2)

	# If difference between lengths is more than 1,
	# then strings can't be at one distance
	if abs(m - n) > 1:
		return False

	count = 0 # Count of isEditDistanceOne

	i = 0
	j = 0
	while i < m and j < n:
		# If current characters dont match
		if s1[i] != s2[j]:
			if count == 1:
				return False

			# If length of one string is
			# more, then only possible edit
			# is to remove a character
			if m > n:
				i+=1
			elif m < n:
				j+=1
			else: # If lengths of both strings is same
				i+=1
				j+=1

			# Increment count of edits
			count+=1

		else: # if current characters match
			i+=1
			j+=1

	# if last character is extra in any string
	if i < m or j < n:
		count+=1
  
	if count <= 1:
		return True
	else:
		return False
     
 





print(isEditDistanceOne("abc", "abc")) # true
print(isEditDistanceOne("abcd", "abc")) # true
print(isEditDistanceOne("abxd", "abcd")) #true
print(isEditDistanceOne("abcd", "abxcd")) # true
print(isEditDistanceOne("abcde", "abc")) #false
print(isEditDistanceOne("axy", "abc")) # false
print(isEditDistanceOne("zxy", "abc")) # false