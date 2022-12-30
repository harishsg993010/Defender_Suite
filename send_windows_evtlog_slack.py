import json
import logging
import os
import pywintypes
import win32evtlog
import win32evtlogutil
import requests

# Set the name of the event log to monitor
event_log = "Application"

# Set the name of the Slack channel to send the events to
channel = "#event-logs"

# Set the URL of the Slack webhook to use for posting messages
webhook_url = "https://hooks.slack.com/services/XXX/XXX/XXX"

# Set the format for the event log message
log_format = "{EventType:<8} {SourceName:<12} {Message}"

def send_to_slack(text):
    """Send a message to the Slack channel using the webhook URL."""
    payload = {"text": text, "channel": channel}
    requests.post(webhook_url, json=payload)

while True:
    # Open the event log
    log = win32evtlog.OpenEventLog(None, event_log)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(log)
    last_record = win32evtlog.GetOldestEventLogRecord(log) + total
    events = 1
    while events:
        events = win32evtlog.ReadEventLog(log, flags, last_record)
        for event in events:
            # Format the event log message
            message = win32evtlogutil.SafeFormatMessage(event, event_log)
            event_type = win32evtlog.EventCategory(event).strip()
            source_name = event.SourceName.strip()
            log_message = log_format.format(EventType=event_type, SourceName=source_name, Message=message)
            # Send the event log message to Slack
            send_to_slack(log_message)
    # Close the event log
    win32evtlog.CloseEventLog(log)
    # Sleep for a short period of time before scanning again
    time.sleep(10)
