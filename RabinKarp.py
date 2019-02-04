# Rabin-Karp Algorithm Implementation
class RollingHash(object):
	"""Implements a Rolling Hash to be used in matching string algorithms"""
	def __init__(self, base, p):
		super(RollingHash, self).__init__()
		self.base = base
		self.p = p
		self.initial_str = ""
		self.initial_idx = 0
		self.hasher = 0
		self.pre = 1
		self.ibase = (base-1)%p

	# Append new character to be hashed and recalculate hash and pre value	
	def append(self, new):
		self.hasher = (self.hasher * self.base + new) % self.p
		self.pre = (self.pre * self.base) % self.p

	# Pop first character from set of characters to be hashed and recalculate hash and pre value
	def pop(self, old):
		self.hasher = (self.hasher - old * self.pre) % self.p
		self.pre = (self.pre * self.ibase) % self.p

	# Return the updated hash value of set of characters post append and pop process
	def hash(self):
		return self.hasher

	# Take in a initial set of characters and convert it to hash
	def stringToHashPattern(self, s):
		for x in s:
			self.append(ord(x))
		return self.hasher

	# Take in characters after initial and convert it to hash
	def stringToHashInitialWindow(self, s):
		for i in range (len(s)):
			self.append(ord(s[i]))
			self.initial_str = s[self.initial_idx]
		return self.hash

	def stringToHash(self, s, s_total):
		self.append(ord(s[-1]))
		self.pop(ord(self.initial_str))
		self.initial_idx += 1
		initial_str = s_total[self.initial_idx]
		return self.hash

# Function that finds whether or not pattern string exists in larger string using Rabin Karp
def RabinKarp(s, pattern):
	n = len(s)
	m = len(pattern)
	rhObj1 = RollingHash(256, 23)
	rhObj2 = RollingHash(256, 23)
	hpattern = rhObj1.stringToHashPattern(pattern)
	hwindow = rhObj2.stringToHashInitialWindow(s[0:m])
	for i in range(1, n-m+1):
		hs = rhObj2.stringToHash(s[i:i+m-1], s)
		if (hs == hpattern):
			if (s[i:i+m-1] == pattern):
				return True
	return False

def main():
	s = "Hello, how are you today?"
	pattern = "you"
	print(RabinKarp(s, pattern))
main()