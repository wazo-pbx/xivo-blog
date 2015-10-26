XiVO blog
=========

This repository contains the sources for XiVO's blog hosted at http://blog.xivo.io.  The XiVO dev
team welcomes anyone who would like to write and contribute articles to our blog. You can submit
your articles by sending us a [pull request](https://help.github.com/articles/using-pull-requests)

Requirements
============

The blog is generated using [pelican](http://blog.getpelican.com). Python 3 is recommended. Install
requirements with ```pip install -r requirements.txt```

Writing an article
==================

Create a new article in ```content/articles```. Usually, the filename will be the same as the
article's slug and will end with ```.md```. A slug is lowercase with words seperated by hypens.
Filename example: ```my-super-duper-article.md```

Articles must be written in [Markdown](https://en.wikipedia.org/wiki/Markdown) and contain the
following metadata at the beginning of the file:

    Title: My super duper article
    Date: 2015-10-16 12:00:00
    Author: John Smith
    Category: XiVO IPBX
    Tags: XiVO, development
    Slug: my-super-duper-article
    Status: draft

    This is the beginning of the article

Once the article is ready for publication, change the status to ```published```.

Generating the blog locally
===========================

To preview what the blog will look like, run the following command :

    make html serve

Then open a browser at http://localhost:5000

Publishing 
==========

Publishing is done via github pages. Once the blog is ready, run the following command:

    make github

Files will automatically be generated and uploaded using your github credentials.
