# Pichu bot sample

A sample plugin for [Errbot](https://github.com/errbotio/errbot).

## Usage
Follow setup guide of [Errbot](https://github.com/errbotio/errbot)

Set the backend to Slack and path to plugins/ folder in `config.py`, e.g:

```py
BACKEND = 'Slack'
BOT_DATA_DIR = '/var/lib/pichubot'
BOT_EXTRA_PLUGIN_DIR = './plugins'
BOT_IDENTITY = {
    'token': "YOUR_SLACK_TOKEN"
}
BOT_ADMINS = ('YOUR_SLACK_HANDLE')
```
then run `errbot -c config.py`
