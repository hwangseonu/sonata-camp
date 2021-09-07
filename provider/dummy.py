from .mail import MailProvider, Mail


# 테스트용 더미 데이터 provider입니다.
class DummyMailProvider(MailProvider):
    def get_mails(self) -> [Mail]:
        return [self.get_mail("")] * 20

    def get_mail(self, url):
        return Mail(
            sender="hwangseonu12@naver.com",
            title="12345 황선우",
            content="더미 데이터입니다.",
            files=[],
            url=url,
        )

    def download_files(self, mail: Mail):
        pass
