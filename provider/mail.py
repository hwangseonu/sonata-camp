class Mail:
    def __init__(self, sender, title, content, files, url):
        self.sender = sender
        self.title = title
        self.content = content
        self.files = files
        self.url = url

    def __str__(self):
        return f'{self.sender} {self.title}'


class MailProvider:
    def __init__(self):
        pass

    def get_mails(self) -> [Mail]:
        pass

    def parse_mail(self, url) -> Mail:
        pass

    def download_files(self, mail: Mail):
        pass
