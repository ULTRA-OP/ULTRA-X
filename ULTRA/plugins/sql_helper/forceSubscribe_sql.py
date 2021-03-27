#    Copyright (C) 2020-2021 by @LEGENDX22, @PROBOYX
#    This program is a part of LEGEND BOT project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from sqlalchemy import Column, Numeric, String

from userbot.plugins.sql_helper import BASE, SESSION


class forceSubscribe(BASE):
    __tablename__ = "forceSubscribe"
    chat_id = Column(Numeric, primary_key=True)
    channel = Column(String)

    def __init__(self, chat_id, channel):
        self.chat_id = chat_id
        self.channel = channel


forceSubscribe.__table__.create(checkfirst=True)


def fs_settings(chat_id):
    try:
        return (
            SESSION.query(forceSubscribe)
            .filter(forceSubscribe.chat_id == chat_id)
            .one()
        )
    except:
        return None
    finally:
        SESSION.close()


def add_channel(chat_id, channel):
    adder = SESSION.query(forceSubscribe).get(chat_id)
    if adder:
        adder.channel = channel
    else:
        adder = forceSubscribe(chat_id, channel)
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(forceSubscribe).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
