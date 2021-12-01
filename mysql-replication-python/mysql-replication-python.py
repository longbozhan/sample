#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
import sys

mysql_settings = {'host': 'xx', 'port': 3306,
                  'user': 'xx', 'passwd': 'xx'}
def main():
    stream = BinLogStreamReader(
        connection_settings=mysql_settings,
        server_id=1,
        blocking=True,
        only_schemas=["ads_admin"],
        only_tables=["config_center"],
        only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent])

    for binlogevent in stream:
        for row in binlogevent.rows:
            event = {"schema": binlogevent.schema, "table": binlogevent.table, "log_pos": binlogevent.packet.log_pos}
            if isinstance(binlogevent, DeleteRowsEvent):
                event["action"] = "delete"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            elif isinstance(binlogevent, UpdateRowsEvent):
                event["action"] = "update"
                event["before_values"] = dict(row["before_values"].items())
                event["after_values"] = dict(row["after_values"].items())
                event = dict(event.items())
            elif isinstance(binlogevent, WriteRowsEvent):
                event["action"] = "insert"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            print(event)
            sys.stdout.flush()


if __name__ == "__main__":
    main()
