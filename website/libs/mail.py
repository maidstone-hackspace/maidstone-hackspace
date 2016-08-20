from mailer import Mailer
from mailer import Message
from config.logger import log

class sendmail:
    config = 'localhost'
    charset = 'utf-8'
    subject_prefix = ''

    @classmethod
    def set_server(cls, config, charset='utf-8'):
        cls.config = config

    def __call__(self, **args):
        return self

    def template(self, path, params=None):
        with open(path) as fp:
            self.body = fp.read()
            self.body.format(**params)

    def send(self, from_address, to_address, subject, body=None, html=True):
        try:
            message = Message(
                From=from_address,
                To=to_address,
                charset=self.charset
            )

            if body is None:
                body = ''
            self.body = body

            message.Subject = "%s - %s" % (self.subject_prefix, subject)
            message.Html = self.body
            message.Body = self.body
        except Exception as e:
            log.exception('[scaffold_mailer] - Failed to create message object for mailer')
            return False

        try:
            sender = Mailer(
                host=self.config.get('host'),
                port=self.config.get('port'),
                use_tls=self.config.get('use_tls', False),
                use_ssl=True,
                usr=self.config.get('username'),
                pwd=self.config.get('password'))
            sender.send(message)
        except Exception as e:
            log.exception('[scaffold_mailer] - Failed to connect to smtp sever and send message with subject: %s' % message.Subject)
            return False
        return True
