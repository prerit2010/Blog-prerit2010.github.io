---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Front end weekly update 2.0'
date:   2016-07-20 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

* The endpoint `/view/detail/` initially returned only json. I have created the front-end for the same. Several details like operating system used, linux distribution, platform etc were to be shown. I chose to show charts only for operating systems and python version used, and rest all shall be shown in a **tabular** form.

* Also, for all the charts, I have also added an option to view the data in the tabular form. When the button is clicked, the tables expand and the data can be viewed in tabular form as well.

* As there are a lot failed packages, the list is huge, and thus the graph doesn't show all the values, but it selects some of those to be viewed. In order to see the hidden values, one can zoom in the graph and take a closer look at it.

* [Raniere](https://github.com/rgaiacs) suggested to limit this graph upto top 10 failed packages, and expand the view to all the packages on user's request. This seems quite legitimate, and I will work upon it.

* The `linux_distribution_name` and `version` are properties valid only for linux. On Mac and Windows, these values are returned as empty strings. And thus, in the chart of linux distribution name and version, data count was also being displayed for the empty strings. This was a quick fix issue.

* Raniere suggested to have both the dropdowns (filter by workshop and filter by package name) at one place (at the top). This also didn't require to have that checkbox for showing data for all workshops. Neat :-)

* Meanwhile, there was also a requirement for creating a **sample database** to test the interface. So I created a command in `manage.py` to import the database. I did this using `SQL` file. The `sample.sql` file contains the SQL insert queries, and these are used to insert the data in the database after the database is created. In case the user wants to overwrite the data, and refresh it with previous sample data, `--overwrite` option can be used with the command `import_db`.

* One important feature to be implemented is the integration of **attempts** with failed packages. Currently data is returned for all the attempts. [Piotr](https://github.com/pbanaszkiewicz) suggested to have a **toggle button** to switch all attempts on and off. If all attempts button is switched on, data is shown for all the attempts of all users. While if it is in off state, only the latest attempt is considered.