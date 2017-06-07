from automatetheboringstuffwithpython.note_tools import print_head as ph

"""
C:\ is root for windows
/ is root for linux/mac

new volumes show as D:\, E:\, etc. on windows
OSX is /Volumes
Linux is /mnt (mounts)
"""

# Backslash on Windows and Forward Slash on OSX/Linux
print('***Blackslash on Windows and Forward Slash on OSX/Linux')
import os
print(os.path.join('usr', 'bin', 'spam')) # usr/bin/spam
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print (os.path.join('/home/richardhu/', filename))
	# /home/richardhu/accounts.txt
	# /home/richardhu/details.csv 
	# /home/richardhu/invite.docx

# The Current Working Directory
print('\n***The Current Working Directory')
print('Look in file to see notes')
"""
. = the current working directory
.. = the parent directory
"""

# Creating new folders with os.makedirs()
ph('Creating new folders with os.makedirs()')
os.makedirs('./delicious/walnut/waffles')

# The os.path module
