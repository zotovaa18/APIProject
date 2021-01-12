from aiohttp.abc import Application

from .settings import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASS,
    DB_NAME
)


async def init_db(app: Application):
    pass


async def close_db(app: Application):
    pass

