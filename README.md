# TiebaManager
Auto moderation tool for baidu tieba .

There are still many unhandled exceptions, this is just a simple and crude demo.

## Requirements
* Python3
* Requests module
* beautifulsoup4 module
* python redis module
* redis

Tested on Linux only.

## Install

First, install the required packages. Then, make sure your redis server is using default configuration.

### Step 0
Clone the Repo .
```
$ git clone https://github.com/KIDJourney/TiebaManager
```
### Step 1
```
$ mv config.example.ini config.ini
```

Then, edit ```config.example.ini``` to with your cookie and the tieba to manage.

### Step 2
```
$ python3 main.py 
```
You can use ```tmux``` or something similar to run it in the backgroud .

## Moderation Method

You can implement your own moderation method in ```judgemethods.py``` .

There are two kinds of methods available

### Post moderation method

The method is implemented as a function, accepting a ```Post``` object as argument .

Make sure to register your method with the ```post_method``` decorator.

### Reply moderation method

The method is implemented as a function, accepting a ```Reply``` object as argument .

Make sure ou register your method with the ```reply_method``` decorator.

## Warning

The Project is still in development, some of code may be refactored frequently.

## Licenses
[Apache licenses](http://choosealicense.com/licenses/apache-2.0/)