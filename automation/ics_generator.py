# src - https://www.kanzaki.com/docs/ical/

from datetime import datetime
import sys
import hashlib

calendar = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//tvrtleb0y//tvrtl3b0y_@ut0mat1on'
]

md5_str = sys.argv[1]

start_time = datetime.strptime('2019-01-1', '%Y-%m-%d')
event = [
    'BEGIN:VEVENT',
    'UID:' + str(int(hashlib.md5((md5_str + str(start_time)).encode('utf-8')).hexdigest(), 16))[0:16],
    'CATEGORIES:MEETING',
    'STATUS:TENTATIVE',
    'TZID:US/California',
    'DTSTAMP:' + '{0:%Y}{0:%m}{0:%d}T000000'.format(start_time),
    'DTSTART:' + '{0:%Y}{0:%m}{0:%d}T100000'.format(start_time),
    'DTEND:' + '{0:%Y}{0:%m}{0:%d}T110000'.format(start_time),
    'RRULE:FREQ=MONTHLY;UNTIL=20191201T230000',
    'SUMMARY:Facebook Profile Pic',
    'BEGIN:VALARM',
    'ACTION:DISPLAY',
    'DESCRIPTION:REMINDER',
    'TRIGGER:-PT30M',
    'END:VALARM',
    'DESCRIPTION:Change profile pic today',
    'CLASS:PRIVATE',
    'END:VEVENT'
]
calendar.append('\n'.join(event))

calendar.append('END:VCALENDAR')
with open('events.ics', 'w') as f:
    f.write('\n'.join(calendar))
