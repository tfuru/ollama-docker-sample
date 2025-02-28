FROM ubuntu:18.04

RUN apt-get update && apt-get install avahi-utils iputils-ping net-tools -y

ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf

ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]