#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests


def get_page(url: str) -> str:
    """ obtains HTML content of a particular URL
    Return:
        The HTML content
    """
    return requests.get(url).text
