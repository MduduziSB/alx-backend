#!/usr/bin/env python3
""" get_hyper Module """
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page size.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing start index and end index.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the specified page of the dataset.

        Args:
        - page (int, optional): The page number (1-indexed). Default 1.
        - page_size (int, optional): The number of items per page. Default 10.

        Returns:
        - list: The list of rows for the specified page.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        page_data = self.dataset()

        if start_index <= len(page_data):
            return page_data[start_index:end_index]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get hypermedia information for the specified page.

        Args:
        - page (int, optional): The page number (1-indexed). Default 1.
        - page_size (int, optional): The number of items per page. Default 10.

        Returns:
        - dict: Dictionary containing hypermedia information.
        """

        page_data = self.get_page(page, page_size)

        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': int(total_pages)
        }
