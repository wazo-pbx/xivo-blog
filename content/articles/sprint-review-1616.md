Title: Sprint Review 16.16
Date: 2016-12-12
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1616
Status: published

Hello Wazo community! Here comes the first release of Wazo, Wazo 16.16!

We will describe the changes made since XiVO 16.13, which is the release of XiVO where Wazo starts from. This sprint review is a bit longer than the others, since it includes the equivalent of 3 versions, 16.13 having been released more than 2 months ago. Future releases will come out every 3 weeks, except for quality assurance no-gos.

New features in this sprint
---------------------------

**Migration from XiVO infrastructure**: Since the domain xivo.io went down, we spent some time rebuilding everything that was needed to make Wazo work correctly from a XiVO installation. You can find the instruction to migrate from XiVO [on the documentation](http://documentation.wazo.community/en/latest/upgrade/16.16/xivo_to_wazo.html). Note that you don't have to upgrade your XiVO to use the new infrastructure. See the documentation for more details.

**Codecs**: The Opus codec is now available in Wazo. The Opus codec is a [very efficient codec](http://opus-codec.org/comparison/) that has been around for a while, but is a potential subject for patent-infringement lawsuits. The Asterisk editor Digium came out with [a solution](http://blogs.digium.com/2016/09/30/opus-in-asterisk/) that we deem satisfying, given the great advantages of the Opus codec.

**REST API**: A new REST API has been added to manage SIP trunks and outgoing calls. Trunks and outgoing calls were the last missing APIs to be able to control inbound and outbound call routing without the need of the web interface.

**REST API**: Groups may now be managed via REST API. A very popular usage for groups is to ring the multiple phones of the same user with the same phone number. Note that the REST API allows you to assign multiple lines to a single user, giving you the same behavior as the aforementioned group configuration, but without some drawbacks of the groups. So this REST API is mainly intended for groups ringing multiple users.

**REST API**: We have added another REST API to manage conference rooms. The conference rooms from the REST API are quite different from the conference rooms we were used to from the web interface: they use a different backend (Confbridge instead of Meetme) and have the additional feature of conference administration: by entering the administrator PIN, a conference member may mute or reject other members.

**Directories**: Until now, XiVO allowed only one phonebook, that was shared across all entities, meaning all users of different entities would see the same contacts that are stored in the phonebook. This was clearly not a good idea, since the purpose of entities is to isolate users from each other while staying on the same server. You may now configure multiple phonebooks on the same Wazo. Phonebooks may be shared across entities or isolated, at your convenience.

Technical features
------------------

**Asterisk**: Asterisk has been upgraded from [13.11.2 to 14.2.1](http://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-14-current), including security fixes.


Ongoing features
----------------

**Switchboard**: We are changing the internals of the Switchboard feature so that we can control more precisely how calls are answered, transferred, etc.

---

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/latest/upgrade/upgrade.html#upgrade-notes)
* [xivo-confd REST API Changelog](http://documentation.wazo.community/en/latest/api_sdk/rest_api/confd/changelog.html)
* [Wazo 16.16 Roadmap](http://projects.wazo.community/versions/252)
