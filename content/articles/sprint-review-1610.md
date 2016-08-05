Title: Sprint Review 16.10
Date: 2016-08-08
Author: sduthil
Category: XiVO IPBX
Tags: XiVO, development
Slug: sprint-review-1610
Status: published

Hello XiVO community! Here comes the release of XiVO 16.10!

New features in this sprint
---------------------------

**XiVO Client**: There are currently three ways of starting a transfer in XiVO: from the key on your phone, by dialing *1 or *2 during the call, or from the XiVO Client. In the latter case, there was no way to complete or cancel the transfer from the XiVO Client since the xlet Contacts was replaced with the xlet People. You could complete the transfer by hanging up your phone, but cancelling a transfer was simply not possible at all, since dialing *0 during the call has no effect for transfers started from the XiVO Client. This problem is now fixed by the addition to the xlet Identity of two new buttons: complete and cancel a transfer.

![The new buttons of the xlet Identity](/public/16.10/identity-transfer.png)

Technical features
------------------

**Asterisk**: Asterisk has been upgraded to [13.10.0](http://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-13.10.0)


Community contributions
-----------------------

**XiVO Client**: Thanks to Marilyn "Kaalyn" Pauvert for making the xlet Identity [more friendly (fr)](http://projects.xivo.io/issues/6206) to long user names.


Ongoing features
----------------

**Multiple phones**: We are working on supporting multiple phones for the same user. The REST API is working, and we still need to integrate it in the web interface, but it's almost there! This is a feature we've been waiting for a long time, and it's the result of a long set of modifications we started a few years ago, so we're really glad we can finally make this step forward.


---

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.xivo.io/en/latest/upgrade/upgrade.html#upgrade-notes)
* [xivo-confd REST API Changelog](http://documentation.xivo.io/en/latest/api_sdk/rest_api/confd/changelog.html)
* [XiVO 16.10 Roadmap](http://projects.xivo.io/versions/246)
