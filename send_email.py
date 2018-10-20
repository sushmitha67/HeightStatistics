from email.mime.text import MIMEText
import smtplib
def send_email(email, height, average_height, count):
	from_email = "sushmithakundapura@gmail.com"
	from_password = "sushmi1995"
	to_email = email
	subject = "Height data"
	message = "Hey there, your height is <strong> %s </strong>.<br> Average height of all is <strong> %s </strong>. <br>And that is calculated out of  %s people" % (height, average_height, count)
	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['To'] = to_email
	msg['From'] = from_email
	gmail = smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.sendmail(from_email, to_email, msg.as_string()) 
