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

    def template(self, path, params=None):
        with open(path) as fp:
            self.body = fp.read()
            self.body.format(**params)


    def send(self, from_address, to_address, subject, body=None, html=True):
        message = Message(
            From=from_address,
            To=to_address,
            charset=self.charset
        )

        if body:
            self.body = body

        message.Subject = "%sAn HTML Email" % self.subject_prefix
        message.Html = self.body
        message.Body = self.body

        sender = Mailer(self.host)
        sender.send(message)
