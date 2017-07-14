# Udacity - Intro to Relational Databases
This repo contains exercise solutions for *Intro to Relational Databases* course from Udacity. It also contains the **Logs Analysis** project for FSND inside the `project/` directory. Here are the instructions to get the project up and running on your machine.

## System requirements:
* Python2.7
* Vagrant
* VirtualBox

## Prerequisites:
1. Execute the following commands in your terminal:
```bash
git clone https://github.com/air-walk/udacity-intro-to-relational-databases.git
cd udacity-intro-to-relational-databases/project/vagrant
vagrant up
vagrant ssh
```
You should now be logged into the VM managed by Vagrant.

## Steps:
1. Execute the following commands inside the VM managed by Vagrant:
```bash
cd /vagrant
psql -d news -f newsdata.sql
python logs_analysis.py
```
