import requests as req


def get_html(url, params=None, output=None):
    """ Function to get the html from a website
    If output is specified, the response text and url get printed to a txt file
    with the name given in output
    args:
        url (str)     -- A url to the website
        params (dict) -- A dictionary containing the url parameters
        output (str)  -- Will write the content of the website to this file
    returns:
        html_str (str) -- the html of the website
    """

    page = req.get(url, params=params)
    assert page.status_code
    html_str = page.text

    if output:
        with open(output, "w", encoding="utf8") as f:
            f.write(page.url + "\n")
            f.write(html_str)
            f.close()

    return html_str


if __name__ == '__main__':
    url1 = "https://en.wikipedia.org/wiki/Studio_Ghibli"
    html1 = get_html(url1, output="requesting_urls/Studio_Ghibli.txt")

    url2 = "https://en.wikipedia.org/wiki/Star_Wars"
    html2 = get_html(url2, output="requesting_urls/Star_Wars.txt")

    url3 = "https://en.wikipedia.org/w/index.php"
    param3 = {"title": "Main_Page", "action": "info"}
    html3 = get_html(url3, param3, "requesting_urls/Main_Page.txt")
