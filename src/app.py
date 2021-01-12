import asyncio
import logging
import argparse
from aiohttp import web

from .database import init_db, close_db
from .routes import urlsplit

async def init_signals(app: web.Application):
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)


async def web_app():
    app = web.Application()

    await init_signals(app)
    app.add_routes(urls)

    return app


_parser = argparse.ArgumentParser()


if __name__ == "__main__":
    args = _parser.parse_args()

    logging.basicConfig(level=args.log_level)
    try:
        web.run_app(
            asyncio.run(web_app()),
            host='0.0.0.0',
            port=args.port
        )

