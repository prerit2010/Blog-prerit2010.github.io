---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'Beginning the GSoC Project'
date:   2016-05-26 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

After 2 long exhausting weeks of exams, I am finally done with my graduation :). And now I have buckled up to code the summer away with Software Carpentry (NumFocus).

As I had figured out earlier, the installation data about the packages, like name and version is easily available in the [installation test scripts](https://github.com/wking/swc-setup-installation-test) in the form of a list. But this case is only for successful installs. For failures I don't have a direct list, rather I have a list of messages that are displayed by the script to the users for each failure, which have been designed something like this:

```python
def __str__(self):
        url = self.get_url()
        lines = [
            'check for {0} failed:'.format(self.checker.full_name()),
            '  ' + self.message,
            '  For instructions on installing an up-to-date version, see',
            '  ' + url,
            ]
        if self.causes:
            lines.append('  causes:')
            for cause in self.causes:
                lines.extend('  ' + line for line in str(cause).splitlines())
        return '\n'.join(lines)
```

So, I'll have to format the data and make it appropriate to be sent to server.

As per the discussion with my mentor **@pbanaszkiewicz**, I will get back to installation scripts a litter later. Firstly I'll be creating the server and API, it will help me in understanding the format and requirement of data which is to be prepared later during modification of installation test scripts.

So, I have begun working on the server side, the code of which resides in the github repository [Result-aggregation-server](https://github.com/prerit2010/Result-aggregation-server). API is to be built using python's micro web framwork flask. Following are the basic requirements of this API:

* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [SQLite](https://www.sqlite.org/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

I have created an endpoint **installation_data** which sends the user's system information, the installed packages by the user, and failed packages. The installation script should make a POST request with headers : **"Content-Type : application/json"** to this end point. Currently there are 3 tables in the database namely **user_system_info**, **successful_installs**, and **failed_installs**. Both successful_installs and failed installs contain a foreign key which references the id of user table. The schema is as follows:
![image](http://i.imgur.com/vTTrkDP.png)

I have created the [models](https://github.com/prerit2010/Result-aggregation-server/blob/master/app/models.py) and also the relationship between the tables (one to many). Each time there is any change in the schema I run the migration script `manage.py` which migrates and then upgrades the schema. This script uses [Flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) which is built on top of [alembic](http://alembic.readthedocs.io/en/latest/). Data that is to be sent by installation test scripts will be a dictionary with 3 keys: _user_system_info_ , _succesful_installs_, and _failed_installs_. Here, _user_system_info_ will be a dictionary, _successful_installs_, a list of dictionaries, and _failed_installs_, a list of dictionaries too. I have written the [endpoint](https://github.com/prerit2010/Result-aggregation-server/blob/master/app/views.py) and tested it using curl. Everything seems to be working correctly. Although, there are some constrains to be applied during the insertion of data. One user may run the script many times, in that case data should be updated instead of insertion. I'm planning to use the combination of _email_id_ and _workshop_id_ as the unique key to identify a user and update their data. Also, the response the API gives can be improved, as it may contain some useful information for the user. Will post further updates soon. Cheers! :)