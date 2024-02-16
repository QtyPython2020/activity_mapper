# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""

# Standard library
import functools
import os
import typing
# Third party
import pandas as pd
import polyline
# import shapely
# Local imports
import backend.utils as bu
# import backend.resources as br

AUTH_LINK = "https://www.strava.com/oauth/token"
STRAVA_CLIENT_ID = os.environ.get("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.environ.get("STRAVA_CLIENT_SECRET")

def get_access_token(authorization_code: str) -> tuple[str]:
    """


    Parameters
    ----------
    authorization_code : str
        DESCRIPTION.

    Returns
    -------
    athlete_name : str
        DESCRIPTION.
    access_token : str
        DESCRIPTION.
    refresh_token : str
        DESCRIPTION.
    created_at : str
        DESCRIPTION.
    """
    res = bu.post_request(AUTH_LINK,
                          data={"client_id": STRAVA_CLIENT_ID,
                                "client_secret": STRAVA_CLIENT_SECRET,
                                "code": authorization_code,
                                "grant_type": "authorization_code"})
    athlete_name = " ".join((res.get("athlete", {}).get("firstname", ""),
                             res.get("athlete", {}).get("lastname", "")
                             )
                            )
    refresh_token = res.get("refresh_token")
    access_token = res.get("access_token")
    created_at = res.get("athlete", {}).get("created_at", "Not found")
    return athlete_name, access_token, refresh_token, created_at


def request_data_from_api(access_token: str) -> list[dict]:
    """
    Send get requests in a loop to retreive all the activities. Loop will stop
    if the result is empty implying that all activities have been retrieved.

    Parameters
    ----------
    access_token : str
        DESCRIPTION.

    Returns
    -------
    list[dict]
        DESCRIPTION.

    """
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {"Authorization": f"Bearer {access_token}"}
    request_page_num = 1
    all_activities = []

    while True:
        param = {"per_page": 200,
                 "page": request_page_num}
        response = bu.get_request(url=activities_url,
                                  headers=header,
                                  params=param)
        # if an invalid response is received
        # return the message and stop looping
        if isinstance(response, dict):
            all_activities.append(response)
            break
        # otherwise add the response to the list
        all_activities.extend(response)
        # if the page is empty or less than 200 records stop the loop
        if len(response) < 200 or response == []:
            break
        # increment to get the next page
        request_page_num += 1
    return all_activities


def get_lat_long(value: list[float]) -> list[typing.Union[None, float]]:
    """


    Parameters
    ----------
    value : list[float]
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if value == []:
        return [None, None]
    return value


# @functools.cache
def locate_country(coords, dataframe=None):
    # point = shapely.geometry.Point(coords)
    # mask = gdf.geometry.apply(lambda c:c.contains(point))
    # try:
    #     country = gdf.loc[mask, "ADMIN"].values[0]
    # except:
    #     country = "Undefined"
    # return country
    return "Belgium"


def parse(activities: list[dict]) -> pd.DataFrame:
    """


    Parameters
    ----------
    activities : list[dict]
        DESCRIPTION.

    Returns
    -------
    dataframe : TYPE
        DESCRIPTION.

    """
    if activities == [{}]:
        return pd.DataFrame()
    parsed_activities = []
    for activity in activities:
        timestamp = pd.to_datetime(activity.get("start_date_local"),
                                   # format="%Y%m%dT%H:%MZ"
                                   )
        # TODO: change view on strava to id
        elements = {"view on Strava":
                    f"https://www.strava.com/activities/{activity.get('id')}",
                    "name": activity.get("name"),
                    "timestamp": timestamp,
                    "year": timestamp.year,
                    "week": timestamp.week,
                    "calender-week": f"{timestamp.year}-{timestamp.week}",
                    "date": timestamp.date(),
                    "weekday": timestamp.weekday(),
                    "time": timestamp.time(),
                    "hour": timestamp.hour,
                    "minutes": timestamp.minute,
                    "moving_time": activity.get("moving_time"),
                    "type": activity.get("type"),
                    "sport_type": activity.get("sport_type"),
                    "polyline": activity.get("map", {}
                                             ).get("summary_polyline")
                    }
        elements.update(dict(zip(["lat", "lon"],
                                 get_lat_long(activity.get("start_latlng",
                                                           [])))))
        if elements.get("polyline"):
            elements.update({"coords": polyline.decode(elements.get("polyline"
                                                                    ),
                                                       5),
                             "country": locate_country(tuple(map(lambda x:round(x,3),
                                                              [row.lon, row.lat])
                                                 ))
                             }
                            )
        parsed_activities.append(elements)
    dataframe = pd.DataFrame(parsed_activities)
    dataframe["app"] = "Strava"
    return dataframe


if __name__ == "__main__":
    pass
