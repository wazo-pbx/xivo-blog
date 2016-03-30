Title: Sprint Review 16.04
Date: 2016-04-04
Author: gsanderson
Category: XiVO IPBX
Tags: XiVO, development
Slug: sprint-review-1603
Status: published

Greetings fellow XiVO fans, it is my pleasure to announce the release of XiVO 16.04.

New features in this sprint
---------------------------

**Fax**: The Fax system in XiVO has been improved. Fax files can be converted to PDF on reception. Files can also be
deposited on a FTP server. Futher details on how to configure these features can be found in the documentation

**Forwards**: All call forwards configured on a phone will activate their BLFs when enabled. A BLF (Busy Lamp Field)
is a small light found next to the function key on a phone. The light helps indicate to the user if any call forwards
are currently active.

**Xivo Client**: The XiVO Client has received small mouse improvements: A double-click on the call button in the people
xlet will call the user's main phone number, where as a right click will copy the number to the clipboard.

**REST API**: New APIs for managing forwards and services has been integrated to the user resource. All call forwards
can now be fully controlled through the REST API. A new API for managing call permissions has also been added. Call
permissions enables administrators to control which phone numbers are allowed to be called by users. These new APIs
represent an additional step towards our long-term goal of offering a PBX system that is more flexible, customizable and
useful for third party developers.

**REST API**: New APIs for managing forwards and services has been integrated to the user resource. All call forwards
can now be fully controlled through the REST API. This new API represents an additional step towards our long-term goal
of offering a PBX system that is more flexible, customizable and useful for third party developers.


Technical Features
------------------

**SCCP**: SCCP phones can be configured to use the g722 codec.

**Digium**: The firmware for digium cards has been updated to the latest version which supports TE133 and TE435
cards.

**Yealink**: The firmware for V80 has been updated to the latest version. Support for the following Yealink phones has
also been added : T40P, T27P, T29P, T49G. 


Ongoing features
----------------

**REST API**: We are working on new APIs for managing call transfers. This will offer third
parties more flexibility when developing applications that manage a user's services.

**Web applications**: Work on tools for connecting web applications to XiVO is ongoing. A good example of a Web application is a switchboard application, where the operator may answer, hold and transfer calls from his browser, effectively controlling his physical phone. This may also be coupled with a WebRTC softphone, in order to have a full Web switchboard environment.

---

*My fellow xivoists, as the **Lord of XiVO** allow me to bid you a happy and invigorating farewell. I wish you shall
remain in high spirits until our next fateful encounter, 3 weeks from now. May the freedom of XiVO bless your
communications across the vast VoIP expanse.*

Sources:

* [XiVO 16.04 Upgrade notes](http://documentation.xivo.io/en/stable/upgrade/upgrade.html#id2)
* [XiVO 16.04 Roadmap](http://projects.xivo.io/versions/240)
* [REST API Changelog](http://documentation.xivo.io/en/stable/api_sdk/rest_api/confd/changelog.html)
