Title: Sprint Review 16.09
Date: 2016-07-13
Author: sduthil
Category: XiVO IPBX
Tags: XiVO, development
Slug: sprint-review-1609
Status: published

Hello XiVO community! Here comes the release of XiVO 16.09!

New features in this sprint
---------------------------

**Web interface**: We've reduced the edition time of a user in the web interface: this operation was especially long when a user had many function keys.

**Entities**: A new API has been added to manage entities on a XiVO. Entities allow administrators to isolate multiple companies or departments on the same XiVO server, so that they may share resources like the machine itself, or phone connections with operators.

**User call flow**: New APIs have also been added so that users may control their current call flow, like hanging up or transferring to a third party. The XiVO Client uses those APIs under the hood, and benefits from a couple of bugfixes brought by those APIs.

**Installation**: Older versions of XiVO may be installed via the installation script (only the older ISO images were available until now). This is especially useful for restoring old backups, or migrating XiVO across machines. Thank you to Grégory Esnaud from the XiVO community for contributing!


Technical features
------------------

**SCCP phones:** the new firmwares 9.4 are available.

---

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.xivo.io/en/latest/upgrade/upgrade.html#upgrade-notes)
* [XiVO 16.09 Roadmap](http://projects.xivo.io/versions/245)
