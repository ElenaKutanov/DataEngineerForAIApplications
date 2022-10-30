from __future__ import annotations

from dataclasses import dataclass

from app import db  # noqa
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.udaconnect.model_person import Person
from app.udaconnect.model_location import Location


@dataclass
class Connection:
    location: Location
    person: Person
