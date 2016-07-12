---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Front end weekly update'
date:   2016-07-12 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

Front end work is on its way. I have created 3 endpoints as of now.

* `/view/` : This shows the charts for all the workshops without any filtering. Currently I have added just 2 charts :
	* One for different OS users across all the workshops
	* Other for most failed packages across all the workshops.

There is one problem with the second one, as the number of failed packages can be too much, all of them are not showing up, we may have to zoom in the chart to view all of them, and there is difficulty in reading the names :

![image](http://i.imgur.com/95F6CCh.png)

One solution is to keep the bar chart horizontal. But as the version names in some cases are too long, a lot of margin is needed in the left side of the graph. So maybe we can cut short the version names in case they are long.

* `/view/<workshop_id>/` : This show the results only for a particular workshop. I have also provided a dropdown of a list of workshops, selecting one of which leads to this endpoint with charts only for this workshop.

* `/view/detail/` : I have also provided a dropdown list of failed packages, selecting one of which hits this endpoint and shows the environment details, like what operating system or environment was used during testing of that failed package. Currently only json is returned.

In all of the above endpoints, there is an option to export the data into json. For example : `/view/?export=json`

* While we are on the page of a particular workshop, when we select one of the failed packages from the dropdown list, it shows the details of that workshop only. I have also added a checkbox by which we can get details about all the workshops if we want. This checkbox appears only when we are at `/view/<workshop_id>`, and not on `/view/`.

![image](http://imgur.com/JWyfPeg.png) 

On hitting submit button leads to `/view/detail/?...` and displays the details about systems used during testing of that package.