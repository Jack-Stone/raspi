#coding=utf-8

'''
assignment R2-3, track interesting message in Twitter by using twython.
'''

from twython import TwythonStreamer
def count():
	global n
	n = n+1
	if ( n > 2 ):
		print "Ian G. Harris is popular!"
				
		
class MyStreamer(TwythonStreamer):

	def on_success(self, data):
		if 'text' in data:
			print("Found it.")
			count()
			print data['text'].encode('utf-8')



C_K = raw_input('Enter consumer key:')
C_S = raw_input('Enter consumer secret:')
A_K = raw_input('Enter access token key:')
A_S = raw_input('Enter access token secret:')

n = 0

try:
	stream = MyStreamer(C_K, C_S, A_K, A_S)
	stream.statuses.filter(track = "Ian G. Harris")
	
except KeyboardInterrupt:
	exit()









