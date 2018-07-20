from crawler.mail import MailService
from gui.main import main_page

service = MailService('chrome')

main_page(service)
