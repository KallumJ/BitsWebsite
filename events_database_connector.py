from config import eventsDbUsername, eventsDBURL, eventsDbPassword
import mysql.connector
from datetime import datetime
import pytz


class Event(object):
    def __init__(self, name, time, date):
        self.name = name
        self.time = time
        self.date = date


class Database(object):
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=eventsDBURL,
            user=eventsDbUsername,
            password=eventsDbPassword,
            database="events"
        )

    def get_agenda(self):
        # Select correct database, and retrieve all the events
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM event")
        events_sql_result = cursor.fetchall()

        # Create list of events
        events = []
        for event in events_sql_result:
            event_name = str(event[1])
            event_time = str(event[2])
            event_date = str(event[3])

            # Check event is upcoming, and not already happened
            event_time_arr = event_time.split(":")
            event_date_arr = event_date.split("-")

            date = datetime(
                year=int(event_date_arr[0]),
                month=int(event_date_arr[1]),
                day=int(event_date_arr[2]),
                hour=int(event_time_arr[0]),
                minute=int(event_time_arr[1]),
                second=int(event_time_arr[2]),
            )

            timezone = pytz.timezone("UTC")
            date = timezone.localize(date)

            if date.date() > datetime.today().date():
                events.append(Event(name=event_name, time=event_time, date=event_date))

        return events
