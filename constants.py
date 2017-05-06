# URL for the current season
url = "http://www.myteamsports.net/prd/league/myleague.asp?orgid=5&orgsportid=32&leagueID=770&seasonID=8749"

current_teams = ["Estonian Thunderfrogs", "Tricycle #PHREAKZ"]
old_team_names = ["Tay Klompson and the Laun Shivingstons"]

email = "{0} vs. {1}\nGame Time: {2}\nLocation: {3}"

locations_mapping = {
    "M'HAHA Acad HS (MA) North Campus, Court WEST": "Minnehaha Academy North Campus (high school), West court",
    "placeholder": "Minnehaha Academy North Campus (high school), East court",
    "placeholder2": "Probably the YMCA?"
}
# Generic season url, looks like.
base_season_url = "http://www.myteamsports.net/prd/league/myleague.asp?orgid=5&orgsportid=32&leagueID=770&seasonID={0}"
current_season_index = 8692

# A basic google calendar event
event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2017-05-28T09:00:00-07:00',
    # 'timeZone': 'America/Los_Angeles',
    'timeZone': 'US/Central'
  },
  'end': {
    'dateTime': '2017-05-28T17:00:00-07:00',
    # 'timeZone': 'America/Los_Angeles',
    'timeZone': 'US/Central'
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

# Old urls, just in case they get lost
very_old_season = "http://www.myteamsports.net/prd/league/myleague.asp?orgid=5&orgsportid=32&leagueID=770&seasonID=8639"
old_season = "http://www.myteamsports.net/prd/league/myleague.asp?orgid=5&orgsportid=32&leagueID=770&seasonID=8692"