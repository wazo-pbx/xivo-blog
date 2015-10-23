Title: Launch and relaunch docker containers manually with ease
Date: 2015-02-26 09:35
Author: jhlavacek
Category: Xuc
Slug: launch-and-relaunch-docker-containers-manually-with-ease
Status: published

First you create a file, let's say
`/etc/YOUR_APPLICATION/docker-run.conf`, with one parameter by line. it
can look like this:

~~~
# cat /etc/YOUR_APPLICATION/docker-run.conf
-t
-d
--restart=always
--name=YOUR_CONTAINER_NAME
-p 9000:9000
-v /etc/YOUR_APPLICATION/conf:/conf/
YOUR/REPOSITORY
~~~


Notice the `--restart=always` - it's an interesting option that
automatically restarts the container when it stops.

You can then start your container by running the following command:

~~~
# docker run $(cat /etc/YOUR_APPLICATION/docker-run.conf)
~~~


Now let's imagine that you have updated your image and you would like to
deploy and restart it using the same parameters. You can do that with
the following script. It ensures a minimum downtime and can also be used
to start your container the first time.

~~~
#!/bin/sh

docker pull YOUR/REPOSITORY:latest;
docker stop YOUR_CONTAINER_NAME;
docker rm YOUR_CONTAINER_NAME;
docker run $(cat /etc/docker/YOUR_APPLICATION/docker-run.conf)
~~~


You can check our XuC repository for a real world use case [1](1 "1")

**Ressources:**

-   [1](1 "1") XuC docker repository:
    [https://registry.hub.docker.com/u/x...](https://registry.hub.docker.com/u/xivo/xuc/ "https://registry.hub.docker.com/u/xivo/xuc/").

</p>

