from django.shortcuts import get_object_or_404
from apps.chats.models import Chat


def get_all_chats() -> list[Chat]:
    return Chat.objects.all()


def get_chat_by_slug(slug: str) -> Chat:
    try:
        return Chat.objects.get(slug=slug)
    except Chat.DoesNotExist:
        # You can either return None, raise a 404, or create a default chat
        return get_object_or_404(Chat, slug=slug)
