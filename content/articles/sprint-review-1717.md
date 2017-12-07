Title: Sprint Review 17.17
Date: 2017-12-11
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1717
Status: published

## New features in this sprint

**REST API**: REST APIs have been added for SIP trunks, timezones, prompt languages, call permissions voicemail and IAX configuration.

**Network**: NAT configuration has been simplified, when the Wazo server is hosted in a datacenter.

**API interconnection**: Wazo is now able to use OAuth2 authentication client mechanisms to interact with external API systems. The first example we are working on is to interconnect Wazo with Zoho, other such API include Google, Office 365, etc.


## Ongoing features

**User and Tenant Management**: We are currently reworking the user and entities (a.k.a tenant) configuration. This should make installations with multiple entities feel more natural in future versions.

**REST API**: We are working towards replacing the old orange admin web interface with the more modern and easier to maintain blue web interface (wazo-admin-ui on `/admin`). Since wazo-admin-ui is only using REST API under the hood, we need REST API to cover all cases of administration of Wazo. Hence we are completing the set of REST API offered by Wazo. You can find the complete API documentation on [http://api.wazo.community](http://api.wazo.community).

---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) are available in the documentation.
The instructions for [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) as also available in the documentation. Be sure to read the [breaking changes](http://documentation.wazo.community/en/wazo-17.17/upgrade/upgrade_notes.html).

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/wazo-17.17/upgrade/upgrade_notes.html)
* [Wazo 17.17 Roadmap](https://projects.wazo.community/versions/270)
