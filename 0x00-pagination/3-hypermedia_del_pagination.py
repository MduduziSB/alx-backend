#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia information for the specified start index.

        Args:
        - index (int, optional): The start index of the current page. Def None.
        - page_size (int, optional): The number of items per page. Default 10.

        Returns:
        - dict: Dictionary containing hypermedia information.
        """
        assert type(index) == int and index >= 0
        assert type(page_size) == int and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        start_index = index
        next_index = min(start_index + page_size, total_rows)

        page_data = dataset[start_index:next_index]

        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data
        }
