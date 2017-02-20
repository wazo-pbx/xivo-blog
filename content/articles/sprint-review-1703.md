Title: Sprint Review 17.03
Date: 2017-02-20
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1703
Status: published

Hello Wazo community! Here comes the release of Wazo 17.03!

New features in this sprint
---------------------------

**Music on hold API**: There are new REST API for managing music on hold classes and audio files related to music on hold. Music on hold control what callers hear when they arrive in a queue or user group, while agents or users are ringing. One music on hold class may contain multiple sound files that will be played one after the other.


Ongoing features
----------------

**Switchboard API**: We are changing the internals of the Switchboard feature so that we can control more precisely how calls are answered, transferred, etc. We are also adding a REST API over the switchboard feature, to allow different interfaces for the switchboard, be it web or desktop client.

**API policies permissions**: The current model of permissions for authentication tokens is a bit too rigid to give users only the permissions they need. We are making the system more flexible in order to have more fine-grained control over what user is allowed to do, such as entering/leaving only certain groups, answering calls from certain switchboards, etc.

**New web interface**: The first lines of code of a new web interface have been written. This web interface will only use the REST API we've been developing in the past few years, with no brittle complicated internal logic like the current web interface has: all the logic is handled by the REST APIs. This web interface will not replace the current web interface before it has all the same features, so it will take time to become the default interface. However, both web interfaces will coexist during the maturation of the new one. We'll keep you posted when the new web interface becomes usable.

---

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/wazo-17.03/upgrade/upgrade.html#upgrade-notes)
* [xivo-confd REST API Changelog](http://documentation.wazo.community/en/wazo-17.03/api_sdk/rest_api/confd/changelog.html)
* [Wazo 17.03 Roadmap](https://projects.wazo.community/versions/255)
