---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - API Deployment and Testing'
date:   2016-06-23 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

One of the most tedious task in any python web application project is the **Deployment** (at least for those who haven't tasted it yet). I have done this many times, but it still annoys me ;-). May be that’s why companies have a separate Devops team who look into all of these deployment issues. Well, whether it feels good or not, I have deployed my flask API on the [nginx]() server which runs on Ubuntu 16.04. The usual steps : Creating **uwsgi configuration file**, **nginx configuration file** etc. Earlier I used to create an _upstart script_ to automatically run uwsgi on reboot of system, but as it turned out, since Ubuntu 15.04, systemd services have been made as default. So basically now I created a _systemd_ service unit file, and started it using `sudo systemctl start Result-aggregation-server`.

Major portion of the code like inserting the data in the tables has been done. Now it needed some testing. I had added the feature of unique key in the installation test scripts, i.e whenever a request is sent to server, a unique is sent along with the data to identify the user. But as it got struck in my mind, if by any chance the user accidentally changes the unique key manually in `key.txt`, then their will be inconsistent data in the table. So I inserted a check upon the validity of the key as well, as whether a record exists with this unique Key or not.

**Unit Tests:** Also wrote a few unit test to test some important use cases. For example:

* If the `successful_installs` list is empty
* If the `failed_installs` list is empty
* Deleting a user should also delete its corresponding success and fail data.

I also tested the scripts on windows platform and other linux distribution, there were some errors like version couldn't be found, etc. Well, now they seem to be working well.

During the course of testing the scripts and API, I came across with 2 issues :

* If we ask the users to input the email id and workshop id, and in case they do not want to provide their email id, they might terminate the script completely. This would prevent any data to be pushed to server. So maybe we should totally remove the idea of any such user input. But, having said that, workshop id can be a really useful data.

Above issue has been resolved by simply asking from the user whether they want to share their email id and workshop id.

* As the scripts are totally open source, and thus our API endpoint, we should have some kind of secret key required to push the data to server, as otherwise any random person (with dirty intention) can harm our server severely.

Above issue is resolved by throttling. Using redis, requests are limited to 100 per IP per hour.

Further steps may include the development of the front end with charts and statistics to extract some useful information out of the data received from installation scripts.