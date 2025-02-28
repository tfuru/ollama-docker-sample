#!/bin/bash

/etc/init.d/dbus start
/etc/init.d/avahi-daemon start

hostname 

tail -f /dev/null
