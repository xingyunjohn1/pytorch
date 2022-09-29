# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class Tool(object):
    """The analysis tool that was run."""

    driver: Any = dataclasses.field(metadata={"schema_property_name": "driver"})
    extensions: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "extensions"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )


# flake8: noqa
