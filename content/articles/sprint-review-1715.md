Title: Sprint Review 17.15
Date: 2017-10-09
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1715
Status: published

Hello Wazo community! Here comes the release of Wazo 17.15!

[We are looking for beta testers for the Wazo Zapier plugin](https://projects.wazo.community/boards/1/topics/11514).

## Security update

**Chat**: In Wazo 17.14 the chat history of a user could be seen by another authenticated malicious user.


## New features in this sprint

**API**: We have added a new API to be able to switch a call between devices while keeping the conversion going. For example, If Alice is on the phone with Bob from her office. Alice can switch the call from her desk phone to her mobile phone without disrupting the call so that she can leave her office without ending the conversation.


## Ongoing features

**User and Tenant management**: We are currently reworking the user and tenant configuration. This should make installations with multiple entities feel more natural in future versions.

**Performance**: We are making changes to the way xivo-ctid-ng handle messages from Asterisk to be able to handle more simultaneous calls.


## New upstream versions

**Asterisk**: Wazo now includes Asterisk 15.0.0 [See the Asterisk 15 releace announcement](http://www.digium.com/blog/2017/10/03/open-source-asterisk-15-released/)


---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) or [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) are available in the documentation.

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/wazo-17.15/upgrade/upgrade.html#upgrade-notes)
* [Wazo 17.15 Roadmap](https://projects.wazo.community/versions/268)
