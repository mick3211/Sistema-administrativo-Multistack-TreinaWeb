from django.db.models.signals import post_save
from .models import Usuario
from django.core.mail import send_mail
from django.template.loader import render_to_string

def usuario_cadastrado(sender, instance, created, **kwargs):
    if created:
        assunto = 'Cadastro realizado com sucesso'
        corpo = ''
        destino = [instance.email,]
        remetente = 'mickaelfelizardo2008@gmail.com'
        mensagem_html = render_to_string('email_cadastro.html', {'usuario': instance})
        send_mail(assunto, corpo, remetente, destino, html_message=mensagem_html)

post_save.connect(usuario_cadastrado, sender=Usuario)