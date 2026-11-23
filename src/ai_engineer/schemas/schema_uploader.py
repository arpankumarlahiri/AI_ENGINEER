from pathlib import Path

from docling.datamodel.base_models import DocumentStream, HttpSource
from pydantic import BaseModel


class uploader_in(BaseModel):
    url: Path | str | DocumentStream | HttpSource


class uploader_out(BaseModel):
    raw_str: str
