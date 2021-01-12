from typing import Iterable, Mapping, Callable
import functools

from aiohttp import web


class RequiredPostParameters:
    """Decorator for web handlers, that checks request body before handler call

    Checks, whether request body is valid json, containing defined
    toplevel parameters. If request is not valid, returns 400 response
    without handler call.

    Places "body" param in request.

    Attributes:
        params: parameters to check.

    """

    def __init__(self, param_list: Iterable[str]):
        self.params = param_list

    @property
    def explanation_body(self) -> Mapping[str, str]:
        """Helper property to get dict with "Error" key

        """

        return {"Error": f"Required parameters: {', '.join(self.params)}."}

    def __call__(
        self, f: Callable[[web.Request], web.Response]
    ) -> Callable[[web.Request], web.Response]:

        @functools.wraps(f)
        async def check_params(request: web.Request) -> web.Response:
            if not request.body_exists:
                return web.json_response(self.explanation_body, status=400)

            try:
                body = await request.json()
            except ValueError:
                    return web.json_response(self.explanation_body, status=400)

            for param in self.params:
                if param not in body:
                    return web.json_response(self.explanation_body, status=400)

            request["body"] = body
            return await f(request)

        return check_params  # type: Callable[[web.Request], web.Response]

