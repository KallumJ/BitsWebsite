from config import eventsLocalDbName, eventsLocalDbURL, eventsLocalDbUsername, eventsLocalDbPassword, \
    eventsDevDbPassword, eventsDevDbUsername, eventsDevDbName, eventsDevDbURL
from database import Database
from remote_server_utils import check_on_hogwarts


class Event(object):
    def __init__(self, name, time, date):
        self.name = name
        self.time = time
        self.date = date


class EventsDatabase(object):
    def __init__(self):
        try:
            if check_on_hogwarts():
                self.database = Database(eventsLocalDbURL, eventsLocalDbUsername, eventsLocalDbPassword, eventsLocalDbName)
            else:
                self.database = Database(eventsDevDbURL, eventsDevDbUsername, eventsDevDbPassword, eventsDevDbName)
        except Exception as err:
            print("There was an error connecting to the events database" + str(err))
            self.database = None

    def get_agenda(self):
        if self.database:
            events_sql_result = self.database.execute_query("SELECT * FROM event WHERE event_Date >= CURRENT_DATE()")

            # Create list of events
            events = []
            for event in events_sql_result:
                event_name = str(event[1])
                event_time = str(event[2])
                event_date = str(event[3])

                # Check event is upcoming, and not already happened
                events.append(Event(name=event_name, time=event_time, date=event_date))

            return events
        else:
            return None
