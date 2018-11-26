from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to,**kwargs):
    sender_mail = "wawerubenson47@gmail.com"

    email = Message(subject, sender = sender_mail, recipients = [to])
    email.body = render_template(template + ".txl", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
