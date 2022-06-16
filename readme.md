# Codept v7
## The Leader of Cam E-Governance
Codept 7 is a all in one cam-based E-governance for any institute.
### Technologies used:
- Python 3.7+
- Django 3.2+
- Mysql, Posgresql.
- Google Cloud for backup of data
## Features

- Managing the officials, employees and other catagories of users
- QR code for every official whereas other users can scan the qr for quick access of the info.
- Work on various pages to maintain the portfolio.
- Project management, Timetable, Time accessible and many major features for smoother workspace management.
- Mark The serialiesd events, manage them and generate the reports.


## Installation

Codept 7  requires [Python](https://www.python.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
python --version
pip freeze
pip install -r requirements.txt
```

For production environments...

```sh
pip install -r prod-requirements.txt
```



## Development

Want to contribute? Great!

Codept v7 uses Python + Django for fast developing.
Make a change in your file and instantaneously see your updates!

```sh
python manage.py -runserver 127.0.0.1:8000
```

> Note: ip can be set to `0.0.0.0' for local address access to the web-server.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT
