from html.parser import HTMLParser
from errbot import BotPlugin, botcmd, arg_botcmd

from bs4 import BeautifulSoup
import requests


class KQParser(HTMLParser):
    found = False
    result = None

    def handle_starttag(self, tag, attrs):
        if tag == "div" and dict(attrs).get("id") == "rs_0_0":
            self.found = True

    def handle_data(self, data):
        if self.found:
            self.result = data
            self.found = False


class Pymi(BotPlugin):
    """
    for PyMiers
    """

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd("name", type=str)
    @arg_botcmd("--favorite-number", type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return "Hello {name}".format(name=args.name)
        else:
            return "Hello {name}, your favorite number is {number}".format(
                name=args.name,
                number=args.favorite_number,
            )

    @botcmd()
    def ketqua2(self, message, args):
        """
        Giải đặc biệt xổ số ngày hôm nay.
        """
        r = requests.get("http://ketqua.net", timeout=5)
        p = KQParser()
        p.feed(r.text)

        return "Giải đặc biệt: {}".format(p.result)

    @botcmd()
    def ketqua(self, message, args):
        """
        Giải đặc biệt xổ số ngày hôm nay.
        """
        resp = requests.get("http://ketqua.net", timeout=5)
        tree = BeautifulSoup(resp.text)
        node = tree.find(attrs={"id": "rs_0_0"})
        return "Giải đặc biệt: {}".format(node.text)

    @botcmd()
    def next(self, message, args):
        """
        When is next course?
        """
        resp = requests.get("https://pymi.vn/")
        tree = BeautifulSoup(resp.text)
        i_tags = [
            node.text
            for node in tree.find("div", attrs={"role": "alert"}).find_all(
                "li"
            )
        ]
        for msg in i_tags:
            yield msg
