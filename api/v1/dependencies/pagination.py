"""
MIT License

Copyright (c) 2024 Christopher Atkinson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from fastapi import Depends
from pydantic import BaseModel
from typing import Annotated


class PaginationModel(BaseModel):
    """
    Model representing pagination parameters.

    Attributes:
        limit (int): The maximum number of items to retrieve per page.
        offset (int): The number of items to skip from the beginning.
    """
    limit: int
    offset: int


async def pagination_params(limit: int = 100, offset: int = 0) -> PaginationModel:
    """
    Asynchronous function to create a PaginationModel with provided parameters.

    Args:
        limit (int, optional): The maximum number of items to retrieve per page. Defaults to 100.
        offset (int, optional): The number of items to skip from the beginning. Defaults to 0.

    Returns:
        PaginationModel: An instance of PaginationModel containing the pagination parameters.
    """
    return PaginationModel(limit=limit, skip=offset)


Pagination = Annotated[PaginationModel, Depends(pagination_params)]
