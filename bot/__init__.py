from telegram.ext import CommandHandler
from .src.handlers.start import start


def register_handlers(app):
    app.add_handler(CommandHandler("start", start))

