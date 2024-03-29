# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

All the variables used throughout the app.
"""
#  Standard library
import os
# Third party
import plotly.express as px

# STRAVA CREDENTIALS
STRAVA_CLIENT_ID = os.environ.get("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.environ.get("STRAVA_CLIENT_SECRET")

# TEXT
CAPTION: str = \
    """
This page was created by UnicornOnAzur and the code can be found on
https://github.com/UnicornOnAzur/activity_mapper .
"""
EXPLANATION: str =\
    """
To use this dashboard click on "Connect with Strava". This will redirect you to
the Strava page. Then select to view public and/or private activities, and
click "Authorize". This provides the dashboard with your data for the duration
of your use.
"""
ERROR_MESSAGE1: str =\
    """
The scope provided is not sufficient. Please allow to view activities.
"""
ERROR_MESSAGE2: str =\
    """
An error occurred while retrieving the data. Please try to authorize again.
"""
HELP_TEXT: str = """See this activity on the Strava website"""
TITLE: str = "Activity Mapper"
DT_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ"

# COLUMNS FOR DATAFRAMA
DISPLAY_COLS: list[str] = ["name",
                           "id",  # input for the 'view on Strava' column
                           "date",
                           "sport_type",
                           "country"
                           ]
STRAVA_COLS: list[str] = ["name",
                          "id",  # used in days figure
                          "date",  # used in days figure
                          "sport_type",  # used for types figure
                          "country",  # used for locations figure
                          "app",  # used in days figure
                          "weekday",  # used in days figure
                          "time",
                          "hour",
                          "minutes",
                          "lat",
                          "lon",
                          "calender-week",
                          "year",
                          "week",
                          "timestamp",
                          "coords"
                          ]

# DICT WITH CONFIGURATION FOR PLOTLY CHARTS
CONFIG: dict = {"displaylogo": False,  # remove the plotly logo
                "displayModeBar": False  # modebar never visible
                }
CONFIG2: dict = {"displaylogo": False,  # remove the plotly logo
                 "modeBarButtonsToRemove":  # remove buttons from modebar
                 ["pan2d",  # pan button
                  "toImage",  # download button
                  ]
                 }

# FILE PATHS
PATH_CODES: str = "files/country_codes.txt"
PATH_CONNECT: str = "logos/btn_strava_connectwith_orange@2x.png"
PATH_LOGO: str = "logos/api_logo_pwrdBy_strava_horiz_light.png"
PATH_GEOJSON: str = "files/countries.geojson"
PATH_MAPPER: str = "files/strava_categories.txt"

# COLORS AND THEMES
COLOR_MAP: dict = {"Strava": "#FC4C02"}  # the color of the Strava app
DISCRETE_COLOR: list[str] = px.colors.sequential.Oranges
DISCRETE_COLOR_R: list[str] = px.colors.sequential.Oranges_r
TEMPLATE: str = "plotly_dark"

# SIZES FOR PLOTS
LEFT_RIGHT_MARGIN: int = 20
TOP_BOTTOM_MARGIN: int = 25
TOP_ROW_HEIGHT: int = 200
BOTTOM_ROW_HEIGHT: int = 600

# URLS
ACTIVITIES_LINK: str = "https://www.strava.com/api/v3/athlete/activities"
ACTIVITIES_URL: str = "https://www.strava.com/activities/"
ATHLETE_URL: str = "https://www.strava.com/api/v3/athlete"
APP_URL: str = "https://strava-activity-mapper.streamlit.app/"
AUTH_LINK: str = "https://www.strava.com/oauth/authorize"
NOMINATIM_LINK: str = "https://nominatim.openstreetmap.org/reverse"
authorization_link = f"""
{AUTH_LINK}?client_id={STRAVA_CLIENT_ID}&redirect_uri={APP_URL}&response_type=code&approval_prompt=force&scope=activity:read,activity:read_all
"""
TOKEN_LINK: str = "https://www.strava.com/oauth/token"

if __name__ == "__main__":
    pass
