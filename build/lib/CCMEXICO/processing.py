import scrapy
import logging
from datetime import datetime
import pandas as pd
from typing import List
import requests
from lxml import html


class ProcessingSearches:
    def __init__(self, parameters):
        self.parameters = parameters
        self.get_urls = []
        self.logger = logging.getLogger("CCMEXICOSpider")
        self.total_pages = 0
        self.crawl()
        self.category()
        self.blog()

    def crawl(self, searchlist=None):
        # If searchlist is None, set it to an empty list
        searchlist = self.parameters.searchlist
        if searchlist is None:
            return
        new_list = []
        for searchlist in self.parameters.searchlist:
            # Check if there is more than one word
            if len(searchlist.split()) > 1:
                # Replace spaces with a hyphen
                searchlist = searchlist.replace(" ", "+")
            url = f"https://ccmexico.com.mx/?s={searchlist}"
            response = requests.get(url)
            tree = html.fromstring(response.content)

            # Check if the sector page contains the desired xpath
            if tree.xpath(
                '//nav[contains(@class, "navigation pagination")]// /ul[contains(@class, "page-numbers")]/li[position() = last()-1]/a/text()'
            ):
                # Get the item of the list of Selector objects representing the pagination elements
                selector = tree.xpath(
                    '//nav[contains(@class, "navigation pagination")]//div[contains(@class, "nav-links")]/ul[contains(@class, "page-numbers")]/li[position() = last()-1]/a/text()'
                )

                # Extract the string value from the first Selector object in the list
                total_pages = int(selector[0])
                print("Total number of pages:", total_pages)

                for depth in range(1, total_pages + 1):
                    new_list.append(
                        f"https://ccmexico.com.mx/page/{depth}/?s={searchlist}"
                    )

                self.get_urls = new_list
                self.searchlist = ""

            else:
                self.logger.info(
                    f"Error: The keyword {searchlist} does not contain the desired XPath."
                )
                self.get_urls.append(url)

    def category(self):
        new_list = []
        list_available_categories = (
            "comercio internacional",
            "juridico",
            "prensa",
            "noticias canaco",
            "cefen canaco",
            "enlace",
            "foros",
            "turismo",
        )

        if self.parameters.category is not None:
            for c in self.parameters.category:
                if c in list_available_categories:
                    c = c.replace(" ", "-")
                    c.lower()
                    url = f"https://ccmexico.com.mx/category/{c}/"

                    response = requests.get(url)
                    tree = html.fromstring(response.content)

                    # Check if the sector page contains the desired xpath
                    if tree.xpath(
                        '//nav[contains(@class, "navigation pagination")]//div[contains(@class, "nav-links")]/ul[contains(@class, "page-numbers")]/li[position() = last()-1]/a/text()'
                    ):
                        # Get the item of the list of Selector objects representing the pagination elements
                        selector = tree.xpath(
                            '//nav[contains(@class, "navigation pagination")]//div[contains(@class, "nav-links")]/ul[contains(@class, "page-numbers")]/li[position() = last()-1]/a/text()'
                        )
                        # Extract the string value from the first Selector object in the list
                        total_pages = int(selector[0])
                        print("Total number of pages:", total_pages)

                        for depth in range(1, int(total_pages) + 1):
                            new_list.append(
                                f"https://ccmexico.com.mx/category/{c}/page/{depth}"
                            )

                        self.get_urls = new_list
                        self.searchlist = ""
                    else:
                        self.logger.info(
                            f"Error: Section {c} does not contain the desired XPath."
                        )
                        self.get_urls.append(url)
                else:
                    self.logger.info(f"Error: Section {c} does not exist.")

    def blog(self):
        new_list = []
        list_available_categories = (
            "home newsletter",
            "capacitacion",
            "noticias",
            "emprendimiento",
            "donde",
        )

        if self.parameters.blog is not None:
            for b in self.parameters.blog:
                if b in list_available_categories:
                    b = b.replace(" ", "-")
                    b.lower()
                    url = f"https://ccmexico.com.mx/blog/category/{b}/"
                    response = requests.get(url)
                    tree = html.fromstring(response.content)

                    # Check if the sector page contains the desired xpath
                    if tree.xpath(
                        '//div[contains(@class, "pagination")]/ul[contains(@class, "axil-post-pagination")]/li[position() = last()-1]/a/text()'
                    ):
                        # Get the item of the list of Selector objects representing the pagination elements
                        selector = tree.xpath(
                            '//div[contains(@class, "pagination")]/ul[contains(@class, "axil-post-pagination")]/li[position() = last()-1]/a/text()'
                        )
                        # Extract the string value from the first Selector object in the list
                        total_pages = int(selector[0])
                        print("Total number of pages:", total_pages)

                        for depth in range(1, int(total_pages) + 1):
                            new_list.append(
                                f"https://ccmexico.com.mx/blog/category/{b}/page/{depth}"
                            )

                        self.get_urls = new_list
                        self.searchlist = ""
                    else:
                        self.logger.info(
                            f"Error: Blog section {b} does not contain the desired XPath."
                        )
                        self.get_urls.append(url)
                else:
                    self.logger.info(f"Error: Blog section {b} does not exist.")
