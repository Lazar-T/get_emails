get_emails
=========

### About
Scraper built with [Scrapy](http://scrapy.org/) framework. Scrapes email addresses from list of site url/s. Designed to crawl whole domain.

### Installing


###### Linux

```
pip install scrapy
```

###### Mac

http://doc.scrapy.org/en/latest/intro/install.html#mac-os-x


###### Windows

http://doc.scrapy.org/en/latest/intro/install.html#windows

### Running

To run this scraper you will need to create a csv file called `emails.csv` and save it into root directory. File should be populated with url/s in this layout:

![ss](http://i.imgur.com/ZbnTfTC.png)

Finally run scraper with command:

```
scrapy crawl emails
```
