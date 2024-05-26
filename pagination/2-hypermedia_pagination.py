#!/usr/bin/env python3
'''
hypermedia pagination
'''
import csv
import math
from typing import Dict, List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        retrieves page list of records
        args page int, page_size int
        returns list of elements in page
        '''
        assert(type(page_size) == int and type(page) == int)
        assert(page > 0 and page_size > 0)
        beginning, end = index_range(page, page_size)
        return self.dataset()[beginning:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        get_hyper
        args pag int, page_size int
        returns dict of pagintatin elements
        '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        new_dictionary = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return new_dictionary
