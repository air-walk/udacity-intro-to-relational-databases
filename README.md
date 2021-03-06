# Udacity - Intro to Relational Databases
This repo contains solved exercises for Udacity's [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) course. It also contains the **Logs Analysis** project for Full Stack Nanodegree inside the `project/` directory. Here are the instructions to get the project up and running on your machine.

## System requirements:
* Python2.7
* Vagrant
* VirtualBox

## Prerequisites:
1. Execute the following commands in your terminal:
```bash
git clone https://github.com/air-walk/udacity-intro-to-relational-databases.git
cd udacity-intro-to-relational-databases/project/vagrant
curl https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip -o newsdata.zip
unzip newsdata.zip
rm newsdata.zip
vagrant up
vagrant ssh
```
You should now be logged into the VM managed by Vagrant.

## Steps:
1. Execute the following commands inside the VM managed by Vagrant:
```bash
cd /vagrant
psql -d news -f newsdata.sql
psql -d news -f create_views.sql
python logs_analysis.py
```
***Note*** that `create_views.sql` has these view creation DDL statements:
```sql
create view aggregated_error_logs AS (select time::date as date, count(*) as count
from log
where status != '200 OK'
group by time::date);

create view aggregated_all_logs AS (select time::date as date, count(*) as count
from log
group by time::date);
```
## Output:
Outptut generated has been placed in `output.txt`
