Barrera, Maribel
import sys

this is my line
"""
This script counts the lines in the standard input
Input: text from the system
"""

count = 0
for line in sys.stdin:
	count+=1
print(count, "lines in standard input")
