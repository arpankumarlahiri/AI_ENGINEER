"""Routes that convert a document source into Markdown."""

from docling.document_converter import DocumentConverter
from fastapi import APIRouter, status

from ..schemas import schema_uploader

router = APIRouter(
    prefix="/uploader",
    tags=["Uploader"],
)

# Reused across requests; constructing a converter loads models and is expensive.
_converter = DocumentConverter()


@router.post(
    "/",
    response_model=schema_uploader.uploader_out,
    status_code=status.HTTP_200_OK,
    summary="Convert a document to Markdown",
)
def uploader(content: schema_uploader.uploader_in) -> schema_uploader.uploader_out:
    """Convert a document at the given path or URL into Markdown.

    Args:
        content: Request body whose ``url`` is a file path or document URL.

    Returns:
        The converted document as a raw Markdown string.
    """
    document = _converter.convert(content.url).document
    markdown = document.export_to_markdown()
    return schema_uploader.uploader_out(raw_str=markdown)
