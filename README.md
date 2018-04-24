# meeting-scribe
A web service that performs ML text analysis on meeting transcripts

# Host it locally

Set up a virtual environment to host the application:

```
$ mkdir meeting-scribe
$ cd meeting-scribe
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```

Now, start the application.

```
$ python main.py
```

Or just host it on an Azure web application instance. :)

# How to use it

There is only one HTTP endpoint, at the root path. Submit a meeting transcript using a POST request to `/`. The request body should be in JSON, with the following structure:

```
{
  'transcript': '<your transcript here>'
}
```

The body of the return will be a JSON object with your summary and keywords in the following structure:

```
{
  'summary': <summary>,
  'keywords': <keywords>
}
```

# Test it

You can test it with a curl request. This request will send the contents of the file `transcript.txt`:

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"transcript":"`cat transcript.txt`"}' http://localhost:5000/
```
