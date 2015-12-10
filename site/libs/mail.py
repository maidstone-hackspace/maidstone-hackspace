from mailer import Mailer
from mailer import Message


class sendmail:
    host = 'localhost'
    charset = 'utf-8'
    subject_prefix = ''

    @classmethod
    def set_server(cls, host='localhost', charset='utf-8'):
        cls.host = host

    def __call__(self, **args):
        return self

    def send(self, from_address, to_address, subject, body='', html=True):
        message = Message(From="me@example.com",
                          To=to_address,
                          charset=self.charset)
        message.Subject = "%sAn HTML Email" % self.subject_prefix
        message.Html = body
        message.Body = body

        sender = Mailer(self.host)
        sender.send(message)
