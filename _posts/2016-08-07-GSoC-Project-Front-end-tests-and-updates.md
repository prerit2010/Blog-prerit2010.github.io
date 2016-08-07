---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Front end tests and updates'
date:   2016-08-07 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

As the end of Google Summer of code is quite near (2 weeks more), I proceeded towards more improvements in code writing and also testing. I covered the following things this week :

* Added all the data retrieved from the database and from application into JSON. Earlier some of the parameters like `all_attempts`, `all_workshops` etc were not included in the raw JSON and were directly rendered in the html template. But now a single variable `response` contains all the data. And by providing `export=json` as the url parameter, one can retrieve all the data in JSON.

* I had not written any test cases for `/view/detail/` while writing the code. So I added several unit test cases for this endpoint. Some of these were :
	* Details of package for all attempts and all workshops.
	* Details of package for latest attempt and all workshops.
	* Details of package for all attempts and one workshops.
	* Details of package for latest attempt and one workshops.
	* Count of Workshops in the list on the `/view/` page.

...and several more.

* I was not following any coding standard till now. But now I have brought the code under PEP8 standards, and now it looks much better and cleaner.

* I also got an idea of a plot for `/view/detail/` page. For each failed package there would be a time series plot, which would describe how much this package has been failing over the period of time.

![image](http://imgur.com/ZZ7yH3e.png)

* The above plot would be valid only for **all workshops** option. As for a single workshop, a failed package would be associated with a single date only. So I disabled this plot when details of failed package are queried only for a particular workshop.

* AS suggested by [Raniere](https://github.com/rgaiacs), I have sent an email on the mailing list of software carpentry, and have asked for the feedback of instructors and other people in the community, so that I can work on the suggested changes in the coming 2 weeks.