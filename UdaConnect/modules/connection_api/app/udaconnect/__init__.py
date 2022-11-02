from app.udaconnect.model_connection import Connection  # noqa
from app.udaconnect.schema_connection import ConnectionSchema  # noqa

import sys, os
sys.path.append('app/udaconnect')

import app.udaconnect.person_pb2
import app.udaconnect.person_pb2_grpc


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
