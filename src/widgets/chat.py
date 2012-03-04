#!/usr/bin/env python
# -*- coding: utf-8 -*-

#QT
from PyQt4.QtGui import QWidget, QPixmap, QListWidgetItem

#Python builtin
from time import strftime, localtime

#Local
from ui.chatmessage import Ui_ChatMessage

__all__ = ['ChatMessageWidget',]


class ChatMessageListItem(QListWidgetItem):
    def __init__(self, nick='', body='', timestamp=None, avatar=None, media=None):
        super(ChatMessageListItem, self).__init__(type=1001)

        print dir(self)

class ChatMessageWidget(QWidget, Ui_ChatMessage):
    def __init__(self, nick='', body='', timestamp=None, avatar=None, media=None):
        super(ChatMessageWidget, self).__init__()
        self.setupUi(self)

        if nick:
            self.action_lbl.setText('%s says:' % nick)
        else:
            self.action_lbl.clear()

        if body:
            self.body_lbl.setText(body)
        else:
            self.body_lbl.clear()

        if timestamp:
            self.timestamp_lbl.setText(strftime('%H:%M:%S',localtime(timestamp)))
        else:
            self.timestamp_lbl.setText(strftime('%H:%M:%S'))

        if avatar:
            self.avatar_lbl.setPixmap(QPixmap(avatar))

        if media:
            self.media_lbl.setText("This message has media, but the coder is lazy.")
        else:
            self.media_lbl.hide()

