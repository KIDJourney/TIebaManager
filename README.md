# TiebaManager

Auto management tool for Baidu tieba.

There are still many unexpected situations unhandled, just a simple and crude demo to do basic jobs.

## Requirements

* Python 3
* Requests module
* beautifulsoup4 module
* python redis module
* redis

Tested only in *linux*.

## Install

After you satisfy the requirements.
Make sure your Redis has the default configuration.

### Step 0

Clone the Repo.
```
$ git clone https://github.com/KIDJourney/TiebaManager
```

### Step 1

Edit ```config.example.ini``` to add your cookie and managed bars. Then
```
$ mv config.example.ini config.ini
```

### Step 2

```
$ python3 main.py 
```
You can use ```Tmux``` or something similar to run it in backgroud.

## Judge Method

You can implement your own judge methods in ```judgemethods.py```.

There are two kinds of methods you can write yourself.

### Post judge method

The method is implemented as a function. Accept a ```Post``` object as an argument.

Make sure you register your method with the ```post_method``` decorator.

### Reply judge method

The method is implemented as a function. Accept a ```Reply``` object as an argument.

Make sure you register your method with the ```reply_method``` decorator.

## Warning

The project is still in develop, some of the codes may be refactored frequently.

## License

[Apache 2.0](http://choosealicense.com/licenses/apache-2.0/)
