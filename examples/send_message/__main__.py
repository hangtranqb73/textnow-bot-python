import json
import textnow_bot
import pathlib
import playwright
import sys

_COOKIES_FILE_PATH = pathlib.Path('cookies.json')
_SCREENSHOT_PATH = pathlib.Path('playwright_screenshot.png')

with playwright.sync_playwright() as api:
  recipient = sys.argv[1]
  message = sys.argv[2]
  browser = None
  page = None

  try:
    browser = api.chromium.launch()
    page = browser.newPage()
    bot = None

    if len(sys.argv) == 5:
      print('Logging in with account info...')
      username = sys.argv[3]
      password = sys.argv[4]
      bot = textnow_bot.TextNowBot(page, username=username, password=password)
    elif len(sys.argv) == 3:
      print('Logging in with existing cookies...')
      cookies = json.loads(_COOKIES_FILE_PATH.read_text())
      bot = textnow_bot.TextNowBot(page, cookies)
    else:
      print(f'usage: {sys.argv[0]} <recipient> <message> [<username> <password>]')
      raise Exception('missing parameters')

    print('Sending message...')
    bot.send_message(recipient, message)

    print(f'Updating {_COOKIES_FILE_PATH}...')
    cookies = bot.get_cookies()
    _COOKIES_FILE_PATH.write_text(json.dumps(cookies))

    browser.close()
    print('Successfully sent message on TextNow!')
  except:
    if page:
      page.screenshot(path=_SCREENSHOT_PATH)

    if browser:
      browser.close()

    raise
