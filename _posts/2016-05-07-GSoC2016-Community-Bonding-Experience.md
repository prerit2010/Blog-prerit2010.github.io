---
layout: post
cover: 'assets/images/gsoc2016-banner.png'
title: 'GSoC2016 - Community Bonding Experience'
date:   2016-05-07 10:18:00
tags: GSoC2016
subclass: 'post tag-GSoC2016'
categories: 'prerit2010'
logo: 'assets/images/ghost.png'
navigation: True
---

The **Community Bonding period** of [Google Summer of Code 2016](https://summerofcode.withgoogle.com/) started from _April 23, 2016_ and will last till _May 22, 2016_.

During this period students are expected to learn about their community, get to know the code base, setup the environment etc. My project focuses around creating an API to store the results of [installation test scripts](https://github.com/wking/swc-setup-installation-test). For more about it, take a look at [Project Description](https://github.com/numfocus/gsoc/blob/master/2016/ideas-list-swc.md#write-a-result-aggregation-server-for-the-installation-test-scripts). I had been in conversation with my mentors through emails, a couple of follow up tasks were decided to be done during this period:

* Install some **Virtual Machines** on the system, as the code shall be tested on several operating systems.
* Get to know the working of **Installation test scripts**. 

#### Virtual Machines Installation

I didn't have any significant experience in playing around with Virtual Machines. I needed to install [Windows Virtual machines](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/linux/) as well. They required a lot of space, so the first requirement was external Hard Drive. So I bought a 2TB WD My Passport Ultra to do the work. Initially I was having a hard time searching around the ways to install VMs on External Hard Drive. After Googling around a bit, I found about [Portable Virtual Box](http://www.vbox.me/), allows you to create portable operating systems and run them on any PC. But apparently that's available only for Windows. But, I won't require that, as selecting the destination folder as External Hard drive would do the trick for me.

So long story short, I have installed [Virtual box for Ubuntu 15.10](https://www.virtualbox.org/wiki/Linux_Downloads). Selected the destination folder for the VMs as the external Hard Drive. And installed the following VMs:	

* [Fedora Workstation 23](https://getfedora.org/en/workstation/download/)
* [Debian 8.4](https://www.debian.org/distrib/) 
* [Windows 7 32-bit](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/linux/)
* [Windows 8.1 32-bit](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/linux/)
* [Windows 10 64-bit](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/linux/)

So, I'll be testing the code on the above platforms including **Ubuntu**, which is my host operating system. Testing is to be done for the installation scripts, as students who attend the workshops use different platforms to run these scripts.
I've also created **snapshots** of the Virtual Machines, as Windows VMs provided by Microsoft
will expire after 90 days. Initially I was worried about the performance of Virtual Machines on Virtualbox, but they seem to be working **Nicely** as of now. :)

#### Installation Test Scripts

[Installation test scripts](https://github.com/wking/swc-setup-installation-test) are to be updated to add the feature of sending the data to the server, that I'll be creating during the coding period. I went through the scripts, and I must say, its written quite comprehensively. Also, the best part being, it may not be required to play with a lot of code in there, as the information that I need from the script, which is mainly **successfully installed packages** list and **failed installed packages** list is directly available in the form of `python lists`. Here is a little code snippet of that :

```python
def check(checks=None):
    successes = []
    failures = []
    if not checks:
        checks = CHECKS
    for check in checks:
        try:
            checker = CHECKER[check]
        except KeyError as e:
            raise InvalidCheck(check)# from e
        _sys.stdout.write('check {0}...\t'.format(checker.full_name()))
        try:
            version = checker.check()
        except DependencyError as e:
            failures.append(e)
            _sys.stdout.write('fail\n')
        else:
            _sys.stdout.write('pass\n')
            successes.append((checker, version))
    if successes:
        print('\nSuccesses:\n')
        for checker,version in successes:
            print('{0} {1}'.format(
                    checker.full_name(),
                    version or 'unknown'))
    if failures:
        print('\nFailures:')
        printed = []
        for failure in failures:
            if failure not in printed:
                print()
                print(failure)
                printed.append(failure)
        return False
    return True
```

I've my end semester exams coming up from 9 May, 2016, so will be occupied with that mostly from now on. Will post further updates soon! :)