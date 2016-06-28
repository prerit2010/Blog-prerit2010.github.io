---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Weekly update'
date:   2016-06-28 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

Added [Travis-CI](https://travis-ci.org/) integration in the API. Now at each commit I make on github, Travis will test the API by running the `test.py` file, and will inform if the build fails.

In the API, when a user sends the data with same `unique_user_id`, i.e another attempt, API was not updating the `UserSystemInfo` on this request, assuming the system's information will remain same even in the second request. But this isn't true for `email_id` and `workshop_id`. A user may enter the email id in the second attempt, while may have denied in the previous one. And also, they may have entered a wrong email id in the previous attempt, so they might want to update them in the next. So everytime a user makes a request, system's information is also updated.

But this may create a problem. If second time user doesn't enter the email and workshop id, the API will rewrite the email and workshop field to `None`. So API should update only when the received email or workshop id is **not** `None`. Added the unit test for the same.

Tested the scripts at various platform of linux and windows as well. But I had no access to OS X. So [Piotr Banaszkiewicz](https://github.com/pbanaszkiewicz) asked [Greg Wilson](https://github.com/gvwilson) to test the scripts on his OS X machine and share the feedback with us. The scripts ran without any issues on OS X as well.

I have increased the rate limit to 500 per hour per IP for the time. As when I was testing the API on my computer, the test script made more than 10 calls to API on single execution, and thus very soon all the tests started failing, as the limit had reached.

Now, I think it's time to get going with the frontend, and visualize the data with charts and statistics. There are several options like [Plotly.js](https://plot.ly/javascript/), [C3.js](http://c3js.org/), [MetricGRaphics.js](http://metricsgraphicsjs.org/) etc. I'll select the most approriate library after having all the use cases with me. MetricGraphics is a well maintained JS library by Mozilla. But it seems like more for timeline purpose. So I may have to rely either on Plotly or C3. They kinda do justice to my requirements. Anyway, I'll come to that later.