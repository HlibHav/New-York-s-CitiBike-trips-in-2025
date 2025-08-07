Bike Sharing Expansion Dashboard Plan
This document outlines the proposed elements and analysis questions for a bike-sharing dashboard. The overall objective is to recommend locations for new stations and to provide insights into how weather and user behaviour influence bike shortages and demand across the city.
1. Research Questions and Data Requirements
• What are the most popular stations in the city?
  - Data needed: counts of trips by start station and end station.
  - Visualization: A horizontal bar chart showing the top 10–20 stations with the highest number of departures or arrivals. Bar charts are appropriate for comparing values across categories because they make differences between subgroups easy to see.
• Which months have the most trips, and is there a relationship with weather?
  - Data needed: trip counts aggregated by month, daily weather variables (average temperature, precipitation). The NOAA Global Historical Climatology Network reports average temperature (TAVG) values in tenths of a degree Celsius; to convert to degrees Celsius we divide by 10.
  - Visualization: A line chart plotting monthly trip counts over time and overlaying a second line for the average temperature. Line charts are well suited for showing trends over time and comparing multiple series.
  - Additional question: Do extreme weather days (e.g., heavy rain or heat waves) correspond with lower ridership?  This can be explored with scatter plots of daily ridership versus daily average temperature or precipitation.
• What are the most popular trip routes between stations?
  - Data needed: origin–destination pairs from trip data.
  - Visualization: A map with curved or straight lines connecting stations for the top routes. Pin maps and region maps are common ways to summarise geospatial data. Pin maps place markers on each location, but too many points can clutter the map; therefore, the top N routes should be highlighted with arrows or flow lines.  The thickness or colour of the lines can indicate trip volume.
• Are existing stations evenly distributed across the city?
  - Data needed: geographical coordinates of stations and a map of the city’s neighbourhoods.
  - Visualization: A point map or heat map overlaying station locations on a city map. Region maps group data by neighbourhood to reveal patterns. If the project includes recommended new locations, these can be marked on the same map to show gaps in service.
• How does ridership vary by time of day and by day of the week?
  - Data needed: timestamps of trip start and end times.
  - Visualization: A heatmap where the x‑axis represents the hour of day and the y‑axis represents the day of the week, with colour intensity showing the number of trips. Heatmaps are useful for showing relationships between two categorical variables.
• Are there differences in usage patterns between members and casual riders?
  - Data needed: rider type information (e.g., member vs. single ride vs. day pass). Divvy’s trip data includes rider types along with trip start and end times.
  - Visualization: Multiple bar charts or small multiples comparing trip counts, average trip duration, and seasonal patterns for each rider type.
2. Additional Considerations
• Weather data acquisition: Daily average temperatures will be obtained from NOAA’s Global Historical Climatology Network via their API using the station closest to the city (e.g., New York’s LaGuardia Airport or Chicago’s O’Hare Airport). The API returns temperatures in tenths of a degree Celsius, so values need to be divided by 10 before joining with the trip data.
• Demand versus supply: Where the number of trips departing from a station consistently exceeds the number arriving, the dashboard should flag potential shortages. This can be visualised with a bar or scatter plot comparing departures and arrivals for each station, with the difference represented as an additional metric.
• Planned expansions and city context: According to a 2023 announcement by the Chicago Department of Transportation, Divvy planned to install up to 250 additional traditional stations and nearly 3,000 new classic bikes over the 2023–2024 seasons. The system already operates more than 800 stations and 15,000 bikes and scooters. Expanding service is expensive, so identifying high-demand areas will help optimise where new stations should be placed.
3. Conclusion
This plan sets out the core elements and visualisations required for a strategic bike‑sharing dashboard. By analysing popular stations, seasonal trends, route patterns, station distribution, temporal usage patterns, and rider type differences, stakeholders will gain a comprehensive understanding of demand. Combining trip data with weather information and geographic context will support data‑driven recommendations for station expansion and operational improvements.
