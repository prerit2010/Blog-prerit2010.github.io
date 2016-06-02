---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Schema update'
date:   2016-06-02 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

The concern regarding the updation of data, if the user run the scripts several times has been resolved . Initially I had thoughts of using _workshop_id_ and _email_id_ to identify the user. But as it turned out, we had to capture the data even if a user doesn't provide their _email_id_ and _workshop_id_. So as proposed by [Piotr Banaszkiewicz](https://github.com/pbanaszkiewicz), we can use a hash which will be returned by API to the user. This hash can then be saved on the disk.

We have to keep a track of the user's progress during installation of packages. So everytime a user runs the script, all the data is logged in the tables. But this would require an attempt number to be associated with each request, so that, each attempt can be distinguished from the other. I have added a table **Attempts**, the primary key of which will be used as foreign key in both tables, and would allow us to distinguish between attempts.

**Therefore, on each request a user makes, following things are done:**

* Script checks whether it already has a unique key in the file 'key.txt'. If yes, it checks whether the date of the key and current date are same. As this key might have been generated for some other workshop held on some other day.
* If both checks are passed, then it sends this unique key along with the data. Else, unique key is set to None.
* Server checks whether it already has a 'user' record for this unique id. If yes, same user id is used for insertion of data in the tables.
* Attempts table contains a primary key `id` which is also the foreign key in 'successfull_installs' and 'failed_installs' tables. Using this key, attempts/progress of the user can be tracked down.

A unique id is associated with each user and their several attempts. This helps in recognizing the existing user, and thus associating the same user id with _failed_ and _succesfull installs_. I chose to use UUID over hash, as it is much easier to handle. Refer this [link](http://stackoverflow.com/questions/703035/when-are-you-truly-forced-to-use-uuid-as-part-of-the-design/786541#786541). And it also turns out to be better than hashing technique like SHA1 in some aspects. Refer this [link](https://www.percona.com/blog/2007/03/13/to-uuid-or-not-to-uuid/) 
<font color="Green"><b>Summing up, following things have been done till date :</b></font><br />
<i class="fa fa-check" aria-hidden="true"></i>   Develop models of database using SQLAlchemy. <br />
<i class="fa fa-check" aria-hidden="true"></i>   Migration of database using Flask-Migrate. <br />
<i class="fa fa-check" aria-hidden="true"></i>   API endpoint "/installation_data/". <br />
<i class="fa fa-check" aria-hidden="true"></i>   Database connection with API. <br />
<i class="fa fa-check" aria-hidden="true"></i>   Modification of installation script to send data to server (POST request). <br />
<i class="fa fa-check" aria-hidden="true"></i>   Saving key to local disk for unique identification. <br />

<font color="Red"><b>TODO :</b></font><br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Sending the error description and causes along with failure and success list. <br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Collecting User's system information for sending to server.<br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Writing Unit tests.<br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Analysis of results.<br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Writing the front end to visualize the data.<br />
<i class="fa fa-tasks" aria-hidden="true"></i>   Testing and Bug fixes. <br/>
<i class="fa fa-tasks" aria-hidden="true"></i>   Testing the scripts on several operating systems. <br/>

**Project Code:**

* API Repository : [Result-aggregation-server](https://github.com/prerit2010/Result-aggregation-server)
* Scripts Repository : [swc-setup-installation-test](https://github.com/prerit2010/swc-setup-installation-test)