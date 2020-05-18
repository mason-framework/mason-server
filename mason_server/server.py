"""Main server."""

import mason
from mason.cli import cli

import sanic


app = sanic.Sanic()


@app.route('/schema')
async def get_schema(
        request: sanic.request.Request) -> sanic.response.HTTPResponse:
    """Returns the library schema."""
    del request  # Unused.
    return sanic.response.json(mason.dump_library())


@cli.command()
def serve():
    """Runs the server."""
    app.run(host='0.0.0.0', port=8000)
