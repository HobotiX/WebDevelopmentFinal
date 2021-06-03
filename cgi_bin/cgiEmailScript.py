#!C:\Python27\python.exe -u

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import smtplib

form = cgi.FieldStorage()
emailFrom = form.getvalue("emailFrom","")
emailTo = "hobotix@ymail.com"
emailSubject = form.getvalue("emailSubject","")
emailBody = form.getvalue("emailBody","")


message = """From: From Person <{0}>
To: To Person <{1}><br>
MIME-Version: 1.0<br>
Content-type: text/html<br>
Subject: {2}<br>
Body: {3}
""".format(emailFrom, emailTo, emailSubject, emailBody)


try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(emailFrom, emailTo, message)         
   print "Successfully sent email"
except Exception:
   print "Error: unable to send email"
	
	
print """
<html>

<head><title>Sample CGI Email Response Script</title></head>

<body>
  <h3> Sample CGI Email Response Script </h3>
  <p>Your email would look roughly like this:
  <p>{0}</p>
</body>
</html>
""".format(message)