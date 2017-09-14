#/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()