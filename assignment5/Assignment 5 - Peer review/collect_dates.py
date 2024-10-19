import re


def find_dates(html_string, output=None):
    """Finds all the dates in a html string
    The ed list is in the following format:
    - 1998/10/02
    - 1998/11/04
    - 1999/01/13
    The following formats are considered when searching:
    DMY: 13 Oct(ober) 2020
    MDY: Oct(ober) 13, 2020
    YMD: 2020 Oct(ober) 13
    ISO: 2020-10-13
    args:
        html_string (str) -- The html where we want to find dates
        output (str)      -- Will write the dates to this file
    returns:
        results (lists) -- A list with all the dates found in Y/M/D format
    """
    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"

    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM](?:ay)\b"
    jun = r"\b[jJ]un(?:e)?\b"

    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]ug(?:ust)?\b"
    sep = r"\b[sS]ep(?:tember)?\b"

    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"

    months = rf"(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|\
                 {oct}|{nov}|{dec})"

    # ------------------------------
    def month_to_number(month):
        """Converts the given month to the month number and removes the
        incorrect dates.
        args:
            month (str) -- The given month to be converted
        returns:
            month_nr (str) -- The month number, will always have 2 digits.
        """
        month = month[:3].lower()
        months_to_nr = {"jan": "01", "feb": "02", "mar": "03", "apr": "04",
                        "may": "05", "jun": "06", "jul": "07", "aug": "08",
                        "sep": "09", "oct": "10", "nov": "11", "dec": "12"}

        return months_to_nr[month]

    # 00, and 32++ are excluded
    day = r"\b[1-9]\b|[0][1-9]\b|\b[1-2]\d{1}\b|\b[3][01]\b"
    year = r"\b[12]\d{3}\b"
    iso_month_format = r"\b(?:0\d|1[0-2])\b"

    dmy = rf"({day})\s({months})\s({year})"
    mdy = rf"({months})\s({day})\s({year})"
    ymd = rf"({year})\s({months})\s({day})"
    iso = rf"({year})-({iso_month_format})-({day})"

    dates = {"dmy": re.findall(rf"{dmy}", html_string)}
    dates["mdy"] = re.findall(rf"{mdy}", html_string)
    dates["ymd"] = re.findall(rf"{ymd}", html_string)
    dates["iso"] = re.findall(rf"{iso}", html_string)

    results = []
    for format in dates:
        for date in dates[format]:
            if format == "dmy":
                day, month, year = date
                month = month_to_number(month)
            elif format == "mdy":
                month, day, year = date
                month = month_to_number(month)
            elif format == "ymd":
                year, month, day = date
                month = month_to_number(month)
            else:
                year, month, day = date
            converted_date = year + "/" + month + "/" + day
            results.append(converted_date)

    if output:
        f = open(output, "w")
        for date in results:
            f.write(date + "\n")
        f.close()

    return results


if __name__ == '__main__':
    from requesting_urls import get_html

    url1 = "https://en.wikipedia.org/wiki/J._K._Rowling"
    html1 = get_html(url1)
    find_dates(html1, output="find_dates/collect_date_J._K._Rowling.txt")

    url2 = "https://en.wikipedia.org/wiki/Richard_Feynman"
    html2 = get_html(url2)
    find_dates(html2, output="find_dates/collect_date_Richard_Feynman.txt")

    url3 = "https://en.wikipedia.org/wiki/Hans_Rosling"
    html3 = get_html(url3)
    find_dates(html3, output="find_dates/collect_date_Hans_Rosling.txt")
