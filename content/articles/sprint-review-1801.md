Title: Sprint Review 18.01
Date: 2018-01-22
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1801
Status: published

## New features in this sprint

**REST API**: REST APIs have been added for:
  * SCCP general configuration
  * IAX trunks configuration
  * ConfBridge configuration
  * Special extensions configuration, e.g. setting DND extension to `*55` instead of `*25`, etc.
  * Sound files
  * Trunk registrations


## Technical features

**System**: the underlying Debian GNU/Linux system is upgraded to Debian 9 Stretch. The upgrade procesure is a bit different than usual and will take longer than previous upgrades. See the [specific release notes](http://documentation.wazo.community/en/latest/upgrade/18.01/stretch.html) for more details.

**Asterisk**: Asterisk is upgraded to the latest version [15.2.0](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-15.2.0).


## Contributions

**Yealink**: The provisioning plugin for Yealink now includes the v82 firmware. Thanks to DamienB505 for the patches!


## Ongoing features

**User and Tenant Management**: We are currently reworking the user and entities (a.k.a tenant) configuration. This should make installations with multiple entities feel more natural in future versions.

**REST API**: We are working towards replacing the old orange admin web interface with the more modern and easier to maintain blue web interface (wazo-admin-ui on `/admin`). Since wazo-admin-ui is only using REST API under the hood, we need REST API to cover all cases of administration of Wazo. Hence we are completing the set of REST API offered by Wazo. You can find the complete API documentation on [http://api.wazo.community](http://api.wazo.community).

---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) are available in the documentation.
The instructions for [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) as also available in the documentation. Be sure to read the [breaking changes](http://documentation.wazo.community/en/wazo-18.01/upgrade/upgrade_notes.html).

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/stable/upgrade/upgrade_notes.html)
* [Wazo 18.01 Roadmap](https://projects.wazo.community/versions/271)
