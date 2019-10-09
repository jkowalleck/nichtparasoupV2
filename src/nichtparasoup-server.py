if __name__ == "__main__":
    from os.path import join as path_join
    from os.path import dirname

    from werkzeug.routing import Rule
    from werkzeug.serving import run_simple

    from nichtparasoup.nichtparasoup import NichtParasoup
    from nichtparasoup.server import Server
    from nichtparasoup.crawler.dummy import Dummy as DummyCrawler

    nichtparasoup = NichtParasoup()

    # @TODO write this foo based on some proper settings
    nichtparasoup.add_imagerawler(DummyCrawler('dummy1'), 1)
    nichtparasoup.add_imagerawler(DummyCrawler('dummy2'), 1)

    server = Server(nichtparasoup)

    server.url_map.add(Rule("/", redirect_to="/index.html"))  # type: ignore
    run_simple(
        '127.0.0.1', 5000,  # @TODO write this foo based on some proper settings
        server,
        static_files={"/": path_join(dirname(__file__), "server-static")},
        use_debugger=False
    )
