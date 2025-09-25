import json
import redis

from config.settings.base import REDIS_URL


class RedisService:
    _URL = REDIS_URL

    def __init__(self):
        self.redis_client = redis.from_url(self._URL)

    async def store_message_in_redis(self, chat_slug: str, message: str, username: str):
        message_data = {
            "username": username,
            "message": message,
        }
        self.redis_client.lpush(f"chat:{chat_slug}", json.dumps(message_data))

    def get_chat_messages(self, chat_slug: str) -> list[dict]:
        redis_messages = self.redis_client.lrange(f"chat:{chat_slug}", 0, -1)
        return [json.loads(msg.decode("utf-8")) for msg in reversed(redis_messages)]
