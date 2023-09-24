from django.core.management.base import BaseCommand
from django.conf import settings
import telebot


class Command(BaseCommand):
    help = 'Set the Telegram bot webhook'

    def handle(self, *args, **kwargs):
        bot = telebot.TeleBot(settings.BOT_TOKEN)
        webhook_address = settings.TELEGRAM_BOT_WEBHOOK_URL

        try:
            bot.remove_webhook()
            bot.set_webhook(webhook_address)
            self.stdout.write(self.style.SUCCESS('Webhook set successfully!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to set webhook: {e}'))
