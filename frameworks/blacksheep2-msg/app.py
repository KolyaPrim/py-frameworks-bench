from typing import TypeVar, Any

import time
from uuid import uuid4

import orjson
from blacksheep import Application, get, post, put, FromFiles, Request
from blacksheep.server.responses import html, json, bad_request, text, unauthorized
from blacksheep.server.bindings import Binder, FromJSON, BoundValue
import msgspec.msgpack
from blacksheep import Response, Content
from msgspec import Struct


encoder = msgspec.msgpack.Encoder()


app = Application()


# first add ten more routes to load routing system
# ------------------------------------------------
def req_ok(request):
    return html('ok')


for n in range(5):
    app.router.add_get(f"/route-{n}", req_ok)
    app.router.add_get(f"/route-dyn-{n}/<part>", req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@get('/html')
async def view_html(request):
    """Return HTML content and a custom header."""
    response = html("<b>HTML OK</b>")
    response.add_header(b'x-time', f"{time.time()}".encode())
    return response


@post('/upload')
async def view_upload(files: FromFiles):
    """Load multipart data and store it as a file."""
    formdata = files.value
    if formdata is None:
        return bad_request()

    with open(f"./{uuid4().hex}", 'w', encoding='utf-8') as target:
        target.write(formdata[0].data.decode())

    return text(target.name)


from blacksheep.settings.json import json_settings



def custom_dumps(value):
    return orjson.dumps(value).decode("utf8")


def my_json(data: Any, status: int = 200) -> Response:
    """
    Returns a response with application/json content,
    and given status (default HTTP 200 OK).
    """
    return Response(
        status,
        None,
        Content(
            b"application/json",
            orjson.dumps(data),
        ),
    )


json_settings.use(
    loads=orjson.loads,
    dumps=custom_dumps,
)


@put('/api/users/{int:user}/records/{int:record}')
async def view_api(request):
    """Check headers for authorization, load JSON/query data and return as JSON."""
    if not request.headers.get(b'authorization'):
        return unauthorized()

    return my_json({
        'params': {k: int(v) for k, v in request.route_values.items()},
        'query': dict(request.query),
        'data': await request.json(),
    })
