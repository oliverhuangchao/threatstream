import threading
import pdb
check = {'aaa':'dream','bbb':'the','':''}
for i in check:
	print "%s --> %s" % (i,check[i])


class myThread (threading.Thread):
    def __init__(self, threadID, text):
        threading.Thread.__init__(self)
        self._id = threadID
        self._text = text
    
    def run(self):
		size = len(self._text)
		start = -1
		end = -1
		for i in range(size-1):
			if self._text[i:i+2] == '<%':
				start = i+2
			if self._text[i:i+2] == '%>':
				end = i
			if start >= 0 and end >= 0 and start<=end:
				if self._text[start:end] in check:
					#print ori[start:end]
					self._text = self._text[:start-2] + check[self._text[start:end]] + self._text[end+2:]
					start = -1
					end = -1
				else:
					print "--------------------------------"
					print "thread %d warning" % self._id 
					print "we need to update the dictionary for varible '%s'" % self._text[start:end]
					print "this thread end without any output"
					print "--------------------------------"
					return
		size = len(self._text)
		i = 0
		while i < size:
			if self._text[i:i+2] == '<%' or self._text[i:i+2] == '%>':
				if self._text[i+2] == ' ':
					self._text = self._text[:i] + self._text[i+3:]
				else:
					self._text = self._text[:i] + self._text[i+2:]
			else:
				i += 1
		print "finish thread %d" % self._id
		res_list[self._id] = self._text


ori = "I have a <%aaa%> that one day this nation will rise up and live out true meaning of its <%bbb%> creed \"We hold these truths to be self-evident, that all men are created equal.\" I have a <%aaa%> that one day on <%bbb%> red hills of Georgia, <%bbb%> sons of former slaves and <%bbb%> sons of former slave owners will be able to sit down together at <%bbb%> table of brotherhood. I have a <%aaa%> that one day even <%bbb%> state of Mississippi, a state sweltering with <%bbb%> heat of injustice, sweltering with <%bbb%> heat of oppression, will be transformed into an oasis of freedom and justice. I have a <%aaa%> that my four little children will one day live in a nation where they will not be judged by <%bbb%> color of their skin but by <%bbb%> content of their character."
#ori = "%> aaa <%aaa%> nie da %> <% va sadf <%%>"#%%%%>%%%>>>>>%<%<%"# hello <%aaa%> <%"
print ori
print "*****************"
print "output goes here" 

myLock = threading.Lock()
string_list = ori.split('.')
res_list = ["" for i in range(len(string_list))]
thread_list = []
threadID = 0

# start each sentence
for eachline in string_list:
	thread = myThread(threadID, eachline)
	thread.start()
	thread_list.append(thread)
	threadID += 1

for t in thread_list:
	t.join()

res = ''.join(res_list)
print "result is: %s" % res






