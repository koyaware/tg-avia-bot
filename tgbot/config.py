from dataclasses import dataclass
from pathlib import Path

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from environs import Env
from redis import asyncio as aioredis

from tgbot.db import Database


BASE_DIR = (Path(__file__).resolve()).parent
SOURCE_DIR = (Path(__file__).resolve()).parent.parent / 'source'


@dataclass
class TgBot:
    token: str
    use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            use_redis=env.bool("USE_REDIS"),
        ),
    )


config = load_config(".env")
db = Database('database.db')
storage = RedisStorage2(host='localhost', port=6379, db=0) if config.tg_bot.use_redis else MemoryStorage()

ADMIN_IDS = [2420239, 627071371, ]


async def connect_to_redis():
    redis_pool = await aioredis.from_url('redis://localhost')
    return redis_pool

