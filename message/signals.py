from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from message.models import Message


@receiver(post_save, sender=Message)
def send_email(sender, instance, created, **kwargs):
    if created:
        name_client = instance.name
        phone_client = instance.phone
        email_client = instance.email
        message_from_client = instance.message
        name_manager = instance.name_manager
        email_manager = instance.email_manager
        id_realty = instance.id_realty

        subject = f'Заявка от клиента {name_client}'
        html_message = render_to_string('email_template.html', {
            'name_client': name_client,
            'phone_client': phone_client,
            'email_client': email_client,
            'message_from_client': message_from_client,
            'name_manager': name_manager,
            'id_realty': id_realty,
        })
        plain_message = strip_tags(html_message)
        from_email = 'no_reply@realty.com'
        recipient_list = [email_manager]

        send_mail(
            subject,
            plain_message,
            from_email,
            recipient_list,
            html_message=html_message
        )
