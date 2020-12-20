import json
import os
import playwright

_COOKIES_FILE = 'cookies.json'
_USERNAME = ''
_PASSWORD = ''
_RECIPIENT = ''
_MESSAGE = ''

from textnow_bot import TextNowBot

with playwright.sync_playwright() as api:
  browser = api.firefox.launch()
  page = browser.newPage()

  try:
    if os.path.isfile(_COOKIES_FILE):
      print('Logging in with existing cookies...')

      with open(_COOKIES_FILE, 'r') as file:
        cookies = json.load(file)
        bot = TextNowBot(page, cookies)
    else:
      print('Logging in with account credentials...')

      bot = TextNowBot(page)
      cookies = bot.log_in(_USERNAME, _PASSWORD)

    print('Successfully logged into TextNow!')

    print('Sending message...')
    bot.send_message(_RECIPIENT, _MESSAGE)
    print('Successfully sent message!')

    browser.close()
  except:
    if page:
      page.screenshot(path='./error-screenshot.png')

    if browser:
      browser.close()

    raise

  print(f'Updating {_COOKIES_FILE}...')
  with open(_COOKIES_FILE, 'w') as file:
    json.dump(cookies, file)
  print(f'Successfully updated {_COOKIES_FILE}!')
