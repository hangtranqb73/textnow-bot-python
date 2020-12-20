class TextNowBot:
  def __init__(self, page, cookies=None):
    self.page = page
    self.is_logged_in = False

    if cookies:
      self.page.context.addCookies(cookies)
      self.page.goto('https://www.textnow.com/login', waitUntil='networkidle')

      if '/messaging' in self.page.url:
        self.is_logged_in = True

  def log_in(self, username, password):
    self.page.context.clearCookies()
    self.page.goto('https://www.textnow.com/login')
    self.page.type('#txt-username', username)
    self.page.type('#txt-password', password)
    self.page.click('#btn-login')
    self.page.waitForNavigation()
    self.is_logged_in = True
    return self.page.context.cookies('https://www.textnow.com')

  def send_message(self, recipient, message):
    if not self.is_logged_in:
      raise Exception('user is not logged in')

    self.page.goto('https://www.textnow.com/messaging')
    self.page.click('#newText')
    self.page.type('.newConversationTextField', recipient)
    self.page.press('.newConversationTextField', 'Enter')
    self.page.type('#text-input', message)
    self.page.press('#text-input', 'Enter')
    self.page.waitForTimeout(500)
