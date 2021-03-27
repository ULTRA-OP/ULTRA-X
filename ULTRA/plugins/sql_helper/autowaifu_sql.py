try:
    from ULTRA.plugins.sql_helper import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import BigInteger, Column, Numeric, String, UnicodeText


class Joinwafu(BASE):
    __tablename__ = "wafuautoproceta"
    chat_id = Column(String(14), primary_key=True)
    previous_wafu = Column(BigInteger)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def init(self, chat_id, previous_wafu, reply, f_mesg_id):
        self.chat_id = str(chat_id)
        self.previous_wafu = previous_wafu
        self.reply = reply
        self.f_mesg_id = f_mesg_id


Joinwafu.table.create(checkfirst=True)

def get_wafu(chat_id):
    try:
        return SESSION.query(Joinwafu).get(str(chat_id))
    finally:
        SESSION.close()
def getwafu(chat_id):
    try:
        return SESSION.query(Joinwafu).get(str(chat_id))
    finally:
        SESSION.close()

def get_current_wafu_settings(chat_id):
    try:
        return (
            SESSION.query(Joinwafu).filter(Joinwafu.chat_id == str(chat_id)).one()
        )
    except BaseException:
        return None
    finally:
        SESSION.close()
def getcurrent_wafu_settings(chat_id):
    try:
        return (
            SESSION.query(Joinwafu).filter(Joinwafu.chat_id == str(chat_id)).one()
        )
    except BaseException:
        return None
    finally:
        SESSION.close()
def add_wafu_setting(chat_id, previous_wafu, reply, f_mesg_id):
    to_check = getwafu(chat_id)
    if not to_check:
        adder = Joinwafu(chat_id, previous_wafu, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Joinwafu).get(str(chat_id))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Joinwafu(chat_id, previous_wafu, reply, f_mesg_id)
    SESSION.commit()
    return False

def addwafu_setting(chat_id, previous_wafu, reply, f_mesg_id):
    to_check = getwafu(chat_id)
    if not to_check:
        adder = Joinwafu(chat_id, previous_wafu, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Joinwafu).get(str(chat_id))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Joinwafu(chat_id, previous_wafu, reply, f_mesg_id)
    SESSION.commit()
    return False

def rm_wafu_setting(chat_id):
    try:
        rem = SESSION.query(Joinwafu).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False

def rmwafu_setting(chat_id):
    try:
        rem = SESSION.query(Joinwafu).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False

def update_previous_wafu(chat_id, previous_wafu):
    row = SESSION.query(Joinwafu).get(str(chat_id))
    row.previous_wafu = previous_wafu
    SESSION.commit()
def updateprevious_wafu(chat_id, previous_wafu):
    row = SESSION.query(Joinwafu).get(str(chat_id))
    row.previous_wafu = previous_wafu
    SESSION.commit()
