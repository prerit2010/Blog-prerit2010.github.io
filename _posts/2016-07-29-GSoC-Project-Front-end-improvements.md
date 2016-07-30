---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Front end improvements'
date:   2016-07-29 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

As only 2-3 weeks are left in the GSoC period, most of the major work has been done. Though some improvements are required, but these improvements will never come to end, as a software has always some room for improvements.

* One of the major things left to be implemented was the integration of attempts with the results. Initially data was being shown for all attempts of each user. Now I have added a toggle button to switch between latest attempt and all attempts. By default it remains in off state, i.e. latest attempt state.

![image1](http://imgur.com/aMU95Zr.png)  ![image2](http://imgur.com/sOK7Fff.png)

* As the failed packages list is huge, and we need to visualize it in a graph, plotly selects some of the values to be displayed by default, and rest of those can be seen by zooming in the graph by drawing a box on it. But we are not be concerned to look at all the data in one go. So it's better to have an option to show only top 10-12 results of failed packages. So I added a toggle button to switch between top 12 and all results. By default it shows only top 12.

![image3](http://imgur.com/RHOKVsb.png)

* Raniere suggested to have another plot for showing the list of failed packages grouped by only names, not version. It just required to query the database and grouping the packages by their names only.

![image4](http://imgur.com/E7ydu8s.png)

* There was an issue with the packages having version in the format like : **2.7.10 (default, Oct 14 2015, 16:09:02) [GCC 5.2.1 20151010]**. On clicking on these packages through the dropdown, they did not show any details on the `/view/detail/` page. The issue was because of the presence of '\n' between **2.7.10 (default, Oct 14 2015, 16:09:02)**  and  **[GCC 5.2.1 20151010]**. When they were selected from the dropdown, '\n' was converted to '\r\n'. And thus it did not match with any entry in the database. So I removed the '\n' from the package versions when they are received in the request from installation test scripts.

* Earlier, **all attempts** and **latest attempt** was integrated only on the `/view/` page. But this was not consistent with the `/view/details/` page. So I added the parameter of all_attempts while requesting the details for that package. Now the details shown for the package are also attempts based.