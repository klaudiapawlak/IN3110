import os
import re
from bs4 import BeautifulSoup
import requests as req
from requesting_urls import get_html
from collect_dates import find_dates


def extract_events(url):
    """Extract date, venue and siscipline for competitions.
    args:
        url (str) -- The url to extract events from.
    returns:
        table_info (list of lists) -- A nested list where the rows represent each
                                      race date, and the columns are
                                      [date, venue, discipline].
    """

    disciplines = {
        "DH": "Downhill",
        "SL": "Slalom",
        "GS": "Giant Slalom",
        "SG": "Super Giant Slalom",
        "AC": "Alpine Combined",
        "PG": "Parallel Giant Slalom"
    }

    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    calendar_header = soup.find(id="Calendar")
    calendar_table = calendar_header.find_all_next("table")[0]
    rows = calendar_table.find_all("tr")

    # Checking that we have the right indices.
    assert calendar_table.find_all("th")[0].get_text(strip=True) == "#"
    assert calendar_table.find_all("th")[1].get_text(strip=True) == "Event"
    assert calendar_table.find_all("th")[3].get_text(strip=True) == "Venue"
    assert calendar_table.find_all("th")[4].get_text(strip=True) == "Type"

    found_event = found_venue = found_discipline = None
    events = []

    full_row_length = 9
    # Some rows have fewer because the "venue" spans multiple rows
    # short_row_length means a repeated venue, which should be re-used from the
    # previous iteration.
    short_row_length = full_row_length - 1

    for row in rows:
        cells = row.find_all("td")

        # some rows have one number of columns, if it's a different number
        # (usually 0 or 1), ignore it.
        if len(cells) not in {full_row_length, short_row_length}:
            if len(cells) == 5:
                # Cancelled events, need to keep the venue information.
                found_venue = cells[2].text.strip()
            continue

        event = cells[1]
        # An event seems to always be a 1-3digit number, so we can check that we
        # have an event with a simple regex
        if re.match(r"\d{1,3}", event.text.strip()):
            found_event = event.text.strip()

            # Need to get the date
            date = re.findall(r"\d{1,2} .*", cells[2].text.strip())[0]
            date = find_dates(date)[0]
        else:
            found_event = None

        if len(cells) == full_row_length:
            event_cell = cells[1]
            venue_cell = cells[3]
            found_venue = venue_cell.text.strip()
            discipline_index = 4

        else:
            # repeated venue, discipline is in a different column
            discipline_index = 3

        discipline = cells[discipline_index]

        discipline_regex = r"(DH|SL|GS|SG|AC|PG)"
        discipline_match = re.search(discipline_regex, discipline.text.strip())
        if discipline_match:
            found_discipline = disciplines[discipline_match[0]]
        else:
            found_discipline = None

        if found_venue and found_event and found_discipline:
            events.append((date, found_venue, found_discipline))
    return events


def create_betting_slip(events, save_as):
    """Saves a markdown format betting slip to the location
    ´./datetime_filter/<save_as>.md´.
    args:
        events (list)    -- takes a list of 3-tuples containing date, venue and
                            type for each event.
        save_as (string) -- filename to save the markdown betting slip as.
    """
    # ensure directory exists
    os.makedirs("datetime_filter", exist_ok=True)

    with open(f"./datetime_filter/{save_as}.md", "w") as out_file:
        out_file.write(f"# BETTING SLIP ({save_as})\n\nName:\n\n")
        out_file.write("Date | Venue | Discipline | Who wins?\n")
        out_file.write(" --- | --- | --- | --- \n")
        for e in events:
            date, venue, discipline = e
            out_file.write(f"{date} | {venue} | {discipline}\n")


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup"
    events = extract_events(url)
    create_betting_slip(events, "betting_slip_empty")
