import smtplib
import email.message
from django.conf import settings

def fn_envia_mail(cad,asunto,destinatario):

	html="<html><head></head><body>"
	html=html+cad		
	html=html+"</body></html>"


	html = html.replace("\xa1", "")
	html = html.replace("\xbf", "")
	html = html.replace("\xd1", "N")
	html = html.replace("\xdc", "U")
	html = html.replace("\xf1", "n")
	html = html.replace("\x0a", "\n")

	html = html.replace("\xe1", "a")		
	html = html.replace("\xe9", "e")		
	html = html.replace("\xed", "i")		
	html = html.replace("\xf3", "o")				
	html = html.replace("\xfa", "u")


	html = html.replace("\xc1", "A")		
	html = html.replace("\xc9", "E")		
	html = html.replace("\xcd", "I")		
	html = html.replace("\xd3", "O")				
	html = html.replace("\xda", "U")
	server = smtplib.SMTP('smtp.gmail.com:587')
	msg = email.message.Message()
	msg['Subject'] = asunto
	msg['From']=settings.EMAIL_HOST_USER
	msg['To']=destinatario
	password = settings.EMAIL_HOST_PASSWORD
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(html)		
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()		
	# Login Credentials for sending the mail
	s.login(msg['From'], password)		
	s.sendmail(msg['From'], [msg['To']], msg.as_string())
	return 0