from django.shortcuts import render


def loan_details_email():
    email = EmailMessage(
        'Loan Details',
        'Loan Disbursed',
        settings.EMAIL_HOST_USER,
        ['shubhamsoitkar555@gmail.com']
    )
    email.fail_silently = True
    email.content_subtype = 'pdf'
    email.attach_file = ('templates/Accounts_Head/pdfgenerator.html')
    email.send()
    return 'f Email Sent'