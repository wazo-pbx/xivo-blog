Title: Sprint Review 18.02
Date: 2018-02-12
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1802
Status: published

## New features in this sprint

**REST API**: We added new REST APIs to manage call filters (i.e. boss-secretary filters). Those APIs will allow us to manage call filters from the new admin-ui web interface.

**CDR**: The CDR REST API has been improved: for a given call, we have the two following information: 1. what extension has been dialed and 2. what extension or user has answered the call.

**Admin-UI web interface**: A lot of management plugins have been improved. Also, plugins for managing sound files, SIP trunks, IAX trunks and SIP, SCCP and custom lines have been added.


## Ongoing features

**User and Tenant Management**: We are currently reworking the user and entities (a.k.a tenant) configuration. This should make installations with multiple entities feel more natural in future versions.

**REST API**: We are working towards replacing the old orange admin web interface with the more modern and easier to maintain blue web interface (wazo-admin-ui on `/admin`). Since wazo-admin-ui is only using REST API under the hood, we need REST API to cover all cases of administration of Wazo. Hence we are completing the set of REST API offered by Wazo. You can find the complete API documentation on [http://api.wazo.community](http://api.wazo.community).

---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) are available in the documentation.
The instructions for [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) as also available in the documentation. Be sure to read the [breaking changes](http://documentation.wazo.community/en/wazo-18.02/upgrade/upgrade_notes.html).

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/stable/upgrade/upgrade_notes.html)
* [Wazo 18.02 Roadmap](https://projects.wazo.community/versions/264)
