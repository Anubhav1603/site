from django.db import models

from pydis_site.apps.api.models.bot.message import Message
from pydis_site.apps.api.models.bot.message_deletion_context import MessageDeletionContext


class DeletedMessage(Message):
    deletion_context = models.ForeignKey(
        MessageDeletionContext,
        help_text="The deletion context this message is part of.",
        on_delete=models.CASCADE
    )