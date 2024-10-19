import re


def find_urls(html_string, base_url=None, output=None):
    """Finds all unique urls which are anchored with <a> in a given html_string
    If output is specified, the response text and url get printed to a txt file
    with the name given in output
    args:
        html_string (str) -- The html where we want to find urls
        base_url (dict)   -- The base_url which the function will default to
                             if the file contains relative paths
        output (str)      -- Will write the urls to this file
    returns:
        url_list(lst) -- A list containing all the unique urls in the given
                         html
    """

    # Matches everything that starts with `<a` and ends with `>`
    url_pat = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)

    # Matches everything that starts with `href=` and ends with `"`
    href_pat = re.compile(r'href="([^"]+)"')

    url_list = []
    for url_tag in url_pat.findall(html_string):
        for href in href_pat.findall(url_tag):
            # expression will remove everything after and including `#`
            expression = r"^(?!#)[^#]+"
            url = re.findall(expression, href)
            if url != []:
                url = url[0]
                if re.match(r"http.*", url) is None:
                    if re.match(r"//.*", url):
                        # Missing https/http.
                        if base_url is None:
                            # No base string to use, therefore use https
                            protocol = "https:"
                        else:
                            if re.match(r"https:.*", base_url):
                                protocol = "https:"
                            elif re.match(r"http:.*", base_url):
                                protocol = "http:"
                        url = protocol + url

                    elif re.match(r"/.*", url):
                        # Relative path
                        url = base_url + url

                if url not in url_list and url:
                    url_list.append(url)

    if output:
        f = open(output, "w")
        for url in url_list:
            f.write(url + "\n")
        f.close()

    return url_list


def find_articles(html_string, output=None):
    """Finds all wikipedia pages in a given html
    If output is specified, the articles urls get printed to a txt file with
    the name given in output
    args:
        html_string (str) -- The html where we want to find articles
        output (str)      -- Will write the article urls to this file
    returns:
        url_list(lst) -- A list containing all the unique urls in the given
                         html
    """

    url_list = find_urls(html_string, base_url="https://en.wikipedia.org")

    article_url_list = []
    c = 0
    for url in url_list:
        # Only urls which contains `wikipedia.org` AND no `:` after `.org`
        if re.findall(r"(?<=wikipedia\.org)(?!.*[:]+)", url) != []:
            article_url_list.append(url)

    if output:
        f = open(output, "w")
        for url in article_url_list:
            f.write(url + "\n")
        f.close()

    return article_url_list


if __name__ == '__main__':
    from requesting_urls import get_html

    # -------------- Nobel Price --------------
    url1 = "https://en.wikipedia.org/wiki/Nobel_Prize"
    html1 = get_html(url1)
    find_urls(html1, base_url="https://en.wikipedia.org",
              output="filter_urls/Find_url_Nobel_Price.txt")

    find_articles(html1, output="filter_urls/Find_articles_Nobel_Price.txt")
    # -----------------------------------------

    # -------------- Bundesliga --------------
    url2 = "https://en.wikipedia.org/wiki/Bundesliga"
    html2 = get_html(url2)
    find_urls(html2, base_url="https://en.wikipedia.org",
              output="filter_urls/Find_url_Bundesliga.txt")

    find_articles(html2, output="filter_urls/Find_articles_Bundesliga.txt")
    # -----------------------------------------

    # -------------- ski_cup --------------
    url3 = "https://en.wikipedia.org/wiki/2019%E2%80%9320_\
            FIS_Alpine_Ski_World_Cup"
    html3 = get_html(url3)
    find_urls(html3, base_url="https://en.wikipedia.org",
              output="filter_urls/Find_url_ski_cup.txt")
    find_articles(html2, output="filter_urls/Find_articles_ski_cup.txt")
    # -----------------------------------------
