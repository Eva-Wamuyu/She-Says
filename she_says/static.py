from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

routes = [
    Mount('/static', router=StaticFiles(directory='static', name='static')),
]

router = Starlette(routes)
