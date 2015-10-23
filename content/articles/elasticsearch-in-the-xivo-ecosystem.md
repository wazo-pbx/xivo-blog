Title: ElasticSearch in the XiVO ecosystem
Date: 2015-02-19 15:35
Author: vdagrain
Category: Software
Slug: elasticsearch-in-the-xivo-ecosystem
Status: published

**What is ElasticSearch**

-   ElasticSearch is a real-time search and analytics engine with a
    RESTful API. It's a part of the ELK Stack, which is composed of a
    search engine (ElasticSearch), a logging tool (Logstash) and a
    visualization tool (Kibana). ElasticSearch is a distributed system,
    schema-less and provides a powerful query DSL.

![elasticsearch.png](/public/elasticsearch.png "elasticsearch.png")

**Our use cases**

-   We are using ElasticSearch and Kibana together with XiVO in call
    centers as a real-time information board, usually on a call
    center dashboard. It can be also used by supervisors for fast and
    easy analysis of trends and statistics history.

![Kibana call
center](/public/xuc/KibanaCC.png "Kibana call center, fév. 2015")

-   We are also integrating ElasticSeach and Kibana for use by our
    support team. They will use it for analyzing the recurrence of
    issues, common problems and other trends.

**Data structure**

-   ElasticSearch is schema free. Data must be organized differently
    than in a traditional relational database. The basic ElasticSearch
    data unit is a document with multiple fields.
-   The organization of our data is heavily influenced by the way the
    Kibana engine works. Kibana provides a time oriented graphical or
    textual representation of search results. Kibana dashboards are
    composed of widgets, each one showing a selection of a search
    request configured for the dashboard.
-   Data stored in ElasticSearch are usually structured as
    timestamped events. A parent-child relation between documents
    enables drill-down analysis. For example: A parent document can
    store data on a call and its child documents can will represent
    events associated with the call.

**Technical background**When we started with Elastic, the river-jdbc
[2](2 "2") plugin was not production ready. Therefore we developed a
small utility we called qlogtransfer. It is a basic synchronisation tool
written in Scala. It uses the jdbc Java driver to retrieve the data from
XiVO's postgresql database and inserts it into ElasticSearch using the
elastic4s scala client. The only data transformation done is through a
SQL request with JOIN clauses. The river-jdbc plugin seems to be stable
nowadays, so we are integrating it with our support team's use case.  
We are also using another plugin: Head. It provides an easy but powerful
web interface to ElasticSearch with data browsing features. Plugin
installation is really very easy, the Head plugin installation can be
accomplished with one command:

~~~
sudo elasticsearch/bin/plugin -install mobz/elasticsearch-head
~~~


However, ElasticSearch doesn't include any access right management, a
commercial extension called Shield must be used for this purpose.

**Kibana features**Kibana is a powerful web based visualization tool.
Multiple dashboards can be configured, each dashboard contains widgets
organized in rows as can be seen on the picture of our use case.
Dashboards are saved in ElasticSearch, inside a specific index. They can
be exported and you can also use advanced features like templated or
scripted dashboards. Kibana runs completely inside the web browser and
gets data from ElasticSearch through its REST API. Therefore, it's quite
CPU intensive, can consume a lot of bandwidth and needs to be able to
communicate directly with the ElasticSearch server. It seems to be a
good idea to protect the server behind a proxy, eventually with some
form of authorization if you don't have the Shield plugin (which is our
case).

**Conclusion**ElasticSearch is a powerful tool. Combined with Kibana you
can create nice monitoring interface. You can use nice features like the
time to live parameter for each document inserted, automatic data
distribution between nodes and a powerful search API. However, it's a
pity that the Shield plugin isn't open sourced.

**Ressources:**

-   [1](1 "1") ElasticSearch: <http://www.elasticsearch.org>
-   [2](2 "2") River-jdbc:
    <https://github.com/jprante/elasticsearch-river-jdbc>
-   Community: <http://www.elasticsearch.com/community/>

</p>

