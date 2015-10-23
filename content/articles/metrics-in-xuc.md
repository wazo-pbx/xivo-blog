Title: Metrics in XUC
Date: 2014-11-11 17:45
Author: jhlavacek
Category: Xuc
Slug: metrics-in-xuc
Status: published

We use Metrics in two contexts: contact centre statistics management and
xuc health supervision. We created two independent registries to
separate statistics data and technical data.

Metrics integrates the ability to report periodically data to the
logfile, or on demand via http.

### JSON representation via HTTP

#### JVM statistics

~~~
#curl -XGET 'http://127.0.0.1:9000/stats/admin/metrics?name=tech'@@
{
  "version" : "3.0.0",
  "gauges" : {
    "blocked.count" : {
      "value" : 0
    },
    "count" : {
      "value" : 56
    },
    "daemon.count" : {
      "value" : 17
    },
    "deadlock.count" : {
      "value" : 0
    },
    "deadlocks" : {
      "value" : [ ]
    },
    "heap.committed" : {
      "value" : 1020264448
    },
    "heap.init" : {
      "value" : 1073741824
    },
    "heap.max" : {
      "value" : 1020264448
    },
    "heap.usage" : {
      "value" : 0.4769269545301259
    },
    "heap.used" : {
      "value" : 486591616
    },
    ...
~~~


#### Call-centre statistics

~~~
#curl -XGET 'http://127.0.0.1:9000/stats/admin/metrics?name=Stats'
{
  "version" : "3.0.0",
  "gauges" : {
    "3000-TotalNumberCallsAbandonned-gauge" : {
      "value" : 2.0
    },
    "3000-TotalNumberCallsAbandonnedAfter15-gauge" : {
      "value" : 5.0
    },
    "3000-TotalNumberCallsAnswered-gauge" : {
      "value" : 0.0
    },
    "3000-TotalNumberCallsAnsweredBefore15-gauge" : {
      "value" : 0.0
    },
    "3000-TotalNumberCallsClosed-gauge" : {
      "value" : 1.0
    },
    "3000-TotalNumberCallsEntered-gauge" : {
      "value" : 1.0
    }
  },
  "counters" : { },
  "histograms" : {
    "3000-PercentageAbandonnedAfter15-window" : {
      "count" : 1,
      "max" : 1,
      "mean" : 1.0,
      "min" : 1,
      "p50" : 1.0,
      "p75" : 1.0,
      "p95" : 1.0,
      "p98" : 1.0,
      "p99" : 1.0,
      "p999" : 1.0,
      "stddev" : 0.0
    },
    ...
~~~


### Statistics in log file

~~~
2014-11-12 11:49:30,764 - [info] application - type=GAUGE, name=3000-PercentageAbandonnedAfter15-gauge, value=0.0
2014-11-12 11:49:30,765 - [info] application - type=GAUGE, name=3000-PercentageAnsweredBefore15-gauge, value=0.0
2014-11-12 11:49:30,765 - [info] application - type=GAUGE, name=3000-TotalNumberCallsAbandonned-gauge, value=1.0
2014-11-12 11:49:30,765 - [info] application - type=GAUGE, name=3000-TotalNumberCallsAbandonnedAfter15-gauge, value=0.0
2014-11-12 11:49:30,765 - [info] application - type=GAUGE, name=3000-TotalNumberCallsAnswered-gauge, value=0.0
2014-11-12 11:49:30,766 - [info] application - type=GAUGE, name=3000-TotalNumberCallsAnsweredBefore15-gauge, value=0.0
2014-11-12 11:49:30,766 - [info] application - type=GAUGE, name=3000-TotalNumberCallsClosed-gauge, value=1.0
2014-11-12 11:49:30,766 - [info] application - type=GAUGE, name=3000-TotalNumberCallsEntered-gauge, value=1.0
~~~


### Links

-   [XUC sources](https://gitlab.com/groups/xuc "XUC sources")
-   [XUC
    documentation](http://xuc.readthedocs.org/en/latest/ "XUC documentation")
-   [Metrics](https://dropwizard.github.io/metrics/3.1.0/ "Metrics")

</p>

