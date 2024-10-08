
from django.http import HttpResponse
from django.shortcuts import render

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email(request):
    if request.method == 'POST':
        to_email = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        username = '# Which enamel to go from'
        password = "# Same e-mail password"

        from_email = 'sfhrwyhrw<xxxaxdcadsc@gmail.com>'

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            print('Email sent successfully.')
        except Exception as e:
            print(f'Failed to send email. Error: {e}')
        finally:
            server.quit()
        return HttpResponse('Email sent!')

    return render(request, '/--/--/--/.html')

