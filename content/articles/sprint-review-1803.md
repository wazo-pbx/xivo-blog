Title: Sprint Review 18.03
Date: 2018-03-05
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1803
Status: published

## New features in this sprint

**Admin-UI web interface**: A lot of management plugins have been improved. Also, plugins for managing general settings (SIP, voicemails, conference rooms), schedules, devices, boss-secretary filters, call permissions, CDR export, extension features (like DND, call forwards, call recording, etc.) have been added.

**Admin-UI web interface**: The login page has been redesigned.


## Contributions

**Aastra/Mitel firmwares**: We thank Alexis de Lattre and José Herbrecht for submitting updates to the provisioning plugins for Aastra/Mitel phones.


## Technical features

**Asterisk**: Asterisk was updated from 15.2.0 to [15.2.2](https://downloads.asterisk.org/pub/telephony/asterisk/ChangeLog-15.2.2), fixing 6 security issues.


## Ongoing features

**User and Tenant Management**: We are currently reworking the user and entities (a.k.a tenant) configuration. This should make installations with multiple entities feel more natural in future versions.

**REST API**: We are working towards replacing the old orange admin web interface with the more modern and easier to maintain blue web interface (wazo-admin-ui on `/admin`). Since wazo-admin-ui is only using REST API under the hood, we need REST API to cover all cases of administration of Wazo. Hence we are completing the set of REST API offered by Wazo. You can find the complete API documentation on [http://api.wazo.community](http://api.wazo.community).

**Authentication**: We are changing the authentication mechanism of users and administrators to use a more secure storage. Most of the login experience will be the same, with a few limitations, like not being able to see passwords in clear text.

---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) are available in the documentation.
The instructions for [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) as also available in the documentation. Be sure to read the [breaking changes](http://documentation.wazo.community/en/wazo-18.03/upgrade/upgrade_notes.html).

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/stable/upgrade/upgrade_notes.html)
* [Wazo 18.03 Roadmap](https://projects.wazo.community/versions/272)
