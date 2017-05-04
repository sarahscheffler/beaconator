#!/usr/bin/python
#TODO: holy crap let's make this flow less bad.  we shouldn't have to return an entire webpage from here, in print statements no less.

import cgi, cgitb

form = cgi.FieldStorage()
myvar = form.getvalue('option1')

#TODO: yikes
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "</head>"
print "<body>"
print "Last letter was: %s" % myvar[-1]
print "</body>"
print "</html>"
