import fastf1
from fastf1.livetiming.data import LiveTimingData

livedata = LiveTimingData('saved_data.txt')
session = fastf1.get_testing_session(2025, 1, 1)
session.load(livedata=livedata)