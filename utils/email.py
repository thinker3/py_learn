#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from utils import get_abs_path


def send(user, password, receiver, host='smtp.qq.com', port=25):
    sender = '%s@qq.com' % user
    content = MIMEMultipart('related')
    content['Subject'] = u'send embedded image'
    content['From'] = sender
    content['To'] = receiver

    body = '<html><img src="cid:logo.png"></html>'
    html = MIMEText(body, 'html', 'utf-8')
    content.attach(html)

    logo_filename = 'logo.png'
    mail_logo_path = get_abs_path(['static', 'img', logo_filename])
    fp = open(mail_logo_path, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', logo_filename)
    content.attach(img)

    smtp = smtplib.SMTP()
    smtp.connect(host=host, port=port)
    smtp.login(user=user, password=password)
    smtp.sendmail(sender, receiver, content.as_string())
    smtp.quit()
