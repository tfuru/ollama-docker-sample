#!/bin/sh -e

/etc/init.d/dbus start
/etc/init.d/avahi-daemon start

tail -f /dev/null
