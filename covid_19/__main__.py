from pathlib import Path
import json

import plotly.graph_objects as go


uk_deaths_json = Path(__file__).parent / 'data/uk_deaths.json'
with open(uk_deaths_json, 'rt') as open_file:
    uk_deaths = json.load(open_file)

data = []

for entry in uk_deaths['data']:
    data.append({'date': entry['date'], 'deaths':entry['newDeaths28DaysByDeathDate']})


fig = go.Figure([go.Scatter(x=[x['date'] for x in data], y=[y['deaths'] for y in data])])

fig.update_layout(title='UK Daily Deaths from Covid 19', yaxis_title='New Deaths')

"""
Lockdown dates taken from https://www.instituteforgovernment.org.uk/sites/default/files/chart-images/timeline-lockdown-updated.png
which can be see at data/timeline-lockdown-updated.png

Lockdown 3 end date selected as when non-essential retail reopened.

2020-03-23 lockdown 1 start
2020-06-23 lockdown 1 end

2020-10-31 lockdown 2 start
2020-12-15 lockdown 2 end

2021-01-06 lockdown 3 start
2021-04-12 lockdown 3 end

"""
fig.add_vrect(x0="2020-03-23", x1="2020-06-23",
              annotation_text="lockdown 1", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)

fig.add_vrect(x0="2020-10-31", x1="2020-12-15",
              annotation_text="lockdown 2", annotation_position="top left",
              fillcolor="orange", opacity=0.25, line_width=0)

fig.add_vrect(x0="2021-01-06", x1="2021-04-12",
              annotation_text="lockdown 3", annotation_position="top left",
              fillcolor="yellow", opacity=0.25, line_width=0)

fig.show()


