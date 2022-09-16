import codecs
import email
from email.header import make_header
import imaplib
from nntplib import decode_header
import re
import string
# from .colors import colors
class RamblerEmail():
    """+==============================+"""
    """| Rambler.ru Google Activator  |"""
    """+==============================+"""
    this_last_email = (False, None)
    username:string = None
    password: string = None
    def __init__(self, username:string, password: string) -> None:
        self.username = username
        self.password = password
    def get_code(self, debug_level: int = 0):  # @params username: example@rambler.ru, password:xxxxxxx 
            try:
                M = imaplib.IMAP4_SSL(port=993, host="imap.rambler.ru")
                M.login(self.username, self.password)
                if debug_level and debug_level > 0:
                    M.debug = debug_level
                M.select('INBOX',False)
                typ1, ids1 = M.uid('search',None,'ALL') # (\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*)
                typ, ids = M.uid('search',None,'Seen') # (\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*)
                seen =  ids[0].decode().split()
                ALL =  ids1[0].decode().split()
                self.this_last_email = (False, None)
                for id in ALL:
                    try: 
                        if id not in seen:
                            typ, messageRaw = M.uid('fetch',id,'(RFC822)')
                            if typ == "OK":
                                message = email.message_from_bytes(messageRaw[0][1])
                                if message["From"] == "Google <noreply@google.com>":
                                    email_from = str(make_header(decode_header(message['From']))).encode('utf-8')
                                    email_from = codecs.decode(email_from)
                                    subject = str(email.header.make_header(email.header.decode_header(message['Subject']))).encode('utf-8')
                                    subject = codecs.decode(subject)
                                    b = message 
                                    body = ""

                                    if b.is_multipart():
                                        for part in b.walk():
                                            ctype = part.get_content_type()
                                            cdispo = str(part.get('Content-Disposition'))
                                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                                body = part.get_payload(decode=True)  # decode
                                                # print("type: \n", type(body))
                                                body = codecs.decode(body)
                                                body = re.search(r'[0-9]{6}',body)[0]
                                                break
                                    else:
                                        body = b.get_payload(decode=True)
                            M.store(id, '-FLAGS', '/Seen')
                            self.this_last_email = (True, body)
                    except Exception as ex_:
                        self.this_last_email = (False, ex_)
                return self.this_last_email
            except Exception as ex:
                self.this_last_email = (False, ex)
                return self.this_last_email