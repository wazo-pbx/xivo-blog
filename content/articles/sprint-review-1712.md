Title: Sprint Review 17.12
Date: 2017-08-28
Author: The Wazo Authors
Category: Wazo IPBX
Tags: wazo, development
Slug: sprint-review-1712
Status: published

Hello Wazo community! Here comes the release of Wazo 17.12!

## New features in this sprint

**REST API**: A new REST API has been added to fetch a user's chat history.

**Plugins**: The administration interface now shows if a plugin has a new version available and allows the administrator to upgrade plugins to a more recent version.


## Technical features

**Web Hooks**: Options have been added to make web hook configuration more usable. These options include, the content type, trusted certificates and templates for the body and URL.

**Plugins**: wazo-plugind memory usage has been improved.

**Chat**: The chat history is now stored in the database and included in backups.


## Ongoing features

**Plugin management**: Work will now be done to add a front end to our plugin market, allowing users to browse, add and modify plugins.

**Webhooks**: We are adding a new way of interconnecting Wazo with other software: webhooks. Outgoing webhooks allow Wazo to notify other applications about events that happen on the telephony server, e.g. when a call arrives, when it is answered, hung up, when a new contact is added, etc. Incoming webhooks also allow Wazo to be notified of events happening on other applications, e.g. a new customer was added in your CRM, a new employee was added in your directory, etc. Unfortunately, there is no magic and the application in question must be able to send or receive webhooks so that Wazo can talk with it. See also this [blog post (sorry, it's in French)](http://blog.wazo.community/wazo-webhook.html#wazo-webhook) about Wazo and webhooks.


---

The instructions for [installing Wazo](http://documentation.wazo.community/en/stable/installation/installsystem.html) or [upgrading Wazo](http://documentation.wazo.community/en/stable/upgrade/upgrade.html) are available in the documentation.

For more details about the aforementioned topics, please see the roadmap linked below.

See you at the next sprint review!

Sources:

* [Upgrade notes](http://documentation.wazo.community/en/wazo-17.12/upgrade/upgrade.html#upgrade-notes)
* [Wazo 17.12 Roadmap](https://projects.wazo.community/versions/264)
