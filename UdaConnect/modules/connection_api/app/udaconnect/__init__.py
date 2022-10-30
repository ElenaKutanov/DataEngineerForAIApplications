from app.udaconnect.model_connection import Connection  # noqa
from app.udaconnect.schema_connection import ConnectionSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
