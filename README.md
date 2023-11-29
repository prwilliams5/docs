# Monitoring Overview

This repo contains documentation for setting up a robust and scalable Zabbix/Grafana
monitoring environment. This stack utlilzes polling and SNMP Traps, as well as Shell,
Perl, and Python scripting to provide live status updates across multiple sites.

The Grafana & Zabbix stack is a monitoring solution used in many applications.
There are two main methods to grab metrics from hosts, polling with agents and SNMP Traps.

SNMP Traps are configured in Zabbix and will be used along with polling metrics. Traps
enable us to see any significant events occuring in the hardware stack as it happens. Using
them in tandem with polling gives extensive monitoring coverage for important items such as
physical network links and BGP sessions.

---

![Grafana Dashboard](./images/grafana-dash.png)

## Grafana Dashboards

- Network
- Power
- vCenter
- Morpheus
- Zabbix localhost

## Zabbix

- Zabbix-Main-01

- Zabbix-Proxy-SLC-01

- Zabbix-Proxy-CHI-01
