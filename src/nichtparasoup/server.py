__all__ = ["Server"]

from typing import Dict, Any, Union

from .nichtparasoup import NichtParasoup

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException

from json import dumps as json_encode


class Server(object):
    def __init__(self, nichtparasoup: NichtParasoup):
        self.nichtparasoup = nichtparasoup

        self.url_map = Map([
            Rule('/get', endpoint=self.on_get),
        ])

    def __call__(self, environ: Dict[str, Any], start_response: Any) -> Any:
        return self.wsgi_app(environ, start_response)

    def dispatch_request(self, request: Request) -> Union[Response, HTTPException]:
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            response = endpoint(request, **values)  # type: Response
            return response
        except HTTPException as e:
            return e

    def wsgi_app(self, environ: Dict[str, Any], start_response: Any) -> Any:
        request = Request(environ)
        response = self.dispatch_request(request)
        if isinstance(response, Response):
            response.cache_control.no_cache = True
            response.cache_control.no_store = True
        return response(environ, start_response)

    def on_get(self, _: Request) -> Response:
        image = self.nichtparasoup.get_random_image()
        image_dict = dict() if not image else {
            "uri": image.uri,
            "source": image.source,
            "more": image.more,
        }
        return Response(json_encode(image_dict), mimetype='application/json')

    # TODO: write the other server functions
