_TEXTNOW_URL = 'https://www.textnow.com'
_PERMISSION_COOKIE = { 'name': 'PermissionPriming', 'value': '-1', 'url': _TEXTNOW_URL }

class TextNowBot:
  def __init__(self, page, cookies=None, username=None, password=None):
    self.page = page

    if cookies:
      page.context.addCookies(cookies)
      page.goto(f'{_TEXTNOW_URL}/login', waitUntil='networkidle')
    elif username and password:
      page.context.clearCookies()
      page.goto(f'{_TEXTNOW_URL}/login')
      page.type('#txt-username', username)
      page.type('#txt-password', password)
      page.click('#btn-login')
      page.waitForNavigation()
      page.context.addCookies([_PERMISSION_COOKIE])
    else:
      raise Exception('missing authentication info')

    if not '/messaging' in page.url:
      raise Exception('unauthenticated user')

  def get_cookies(self):
    return self.page.context.cookies(_TEXTNOW_URL)

  def send_message(self, recipient, message):
    self.page.goto(f'{_TEXTNOW_URL}/messaging')
    self.page.click('#newText')
    self.page.type('.newConversationTextField', recipient)
    self.page.press('.newConversationTextField', 'Enter')
    self.page.type('#text-input', message)
    self.page.press('#text-input', 'Enter')
    self.page.waitForTimeout(500)
