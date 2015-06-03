import webbrowser
import time

num_breaks = 0
total_breaks = 3

print "This program started:", time.ctime()

while (num_breaks < total_breaks):
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=Nj8r3qmOoZ8")
        num_breaks = num_breaks + 1
        print 'One session complete at', time.ctime()
        print 'Session number:', num_breaks, 'of 3'

print "Done! Go for a run or something!"
