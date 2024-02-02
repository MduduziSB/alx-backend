#!/usr/bin/env python3
""" Index range module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing start index and end index.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
