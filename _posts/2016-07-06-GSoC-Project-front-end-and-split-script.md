---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC 2016 Project - Front end and split script'
date:   2016-07-05 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

I have decided to use [plotly.js](https://plot.ly/javascript/) primarily for plotting the graphs, but as it hardly matters, I can use other libraries as well as per the requirements. To start with, I added a graph for number of users using different operating systems, and most failed installs packages till date.

* Here we have 2 cases to follow in case of failed installs packages.
	* User may have run the script many times, and so all the attempts are saved. So one case is to show the graph on the basis of all the data (including all attempts of a user).
	* Other case is to have the graph show only the latest attempt. So, we would like to have a toggle button to switch on "Only latest attempt", or switch it off to show all the data.

* The graphs should also be filtered on the basis of workshop. We can have a dropdown containing a list of all the workshops, and selecting one of which will lead to filtering the data for that workshop ONLY.

* [Raniere](https://github.com/rgaiacs) pointed out to have raw json as well in place for the information that we are going to display. For example : [http://installation.software-carpentry.org/view/?export=json](). So we can have the json formatted data for all the information that we tend to receive, and just use this json to display charts in the HTML pages as well.

* Project was initially built on python 2.7 (I don't know why didn't I use python3 from the beginning :p), but now I have migrated it to python 3.5. It didn't require a lot of tasks, just some fixes in importing the files.

* In the installation test scripts, 2 more command line options have been added :
	* `-H` to specify the HOST name to which the data should be submitted. for example : `python swc-main.py -H 127.0.0.1:5000`.
	* `-n` to turn off sending data to server. e.g : `python swc-main.py -n`

* Changed the name of "key.txt" file to '.swc_submission_id', as now it would remain hidden, and having **swc** in the file name tells that it belongs to software carpentry.

* [Piotr](https://github.com/pbanaszkiewicz) suggested to split the long script, and having something like :

```python
import requirements_check
import api as API

REQUIRED = [
    'python>=3.5',
    'numpy',
]

if __name__ == '__main__':
    errors, passed = requirements_check.check(REQUIRED)

    for error in errors:
        # communicate error to the user

        # gives user a pointer on what to do when something fails
        solution = requirements_check.solution(error)

        pass

    # check if user agrees to submit their data
    agreement = input('...')
    submition_id = API.submit(errors, passed)

    # add logic for working with the submition_id
    pass

    # logic for submitting workshop name and email
    pass
```

So that's what I have done. I have separated the code for **API**, **requirements_check** and running the script. Also there used to be 2 scripts, 1 for checking the python version, and the other for checking the other requirements. But now, I have merged the first script in the second. So previous structure was :

```
|__/swc-setup-installation-test
	|--swc-installation-test-1.py
	|--swc-installation-test-2.py
```
But now it is :

```
|__/swc-setup-installation-test
	|--api.py
	|--requirements_checks.py
	|--swc-main.py
```

`swc-main.py` is the only script that needs to be run. It imports **api** and **requirements_checks** for checking the installation dependencies and sending them to server.

It looks good as of now, a lot of documentation is required to be done though.