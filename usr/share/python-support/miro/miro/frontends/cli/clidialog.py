# Miro - an RSS based video player application
# Copyright (C) 2005-2008 Participatory Culture Foundation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#
# In addition, as a special exception, the copyright holders give
# permission to link the code of portions of this program with the OpenSSL
# library.
#
# You must obey the GNU General Public License in all respects for all of
# the code used other than OpenSSL. If you modify file(s) with this
# exception, you may extend this exception to your version of the file(s),
# but you are not obligated to do so. If you do not wish to do so, delete
# this exception statement from your version. If you delete this exception
# statement from all source files in the program, then also delete it here.

import cmd

from miro import app
from miro.frontends.cli.util import print_box, print_text

class DialogAsker(cmd.Cmd):
    def __init__(self, dialog):
        self.dialog = dialog
        self.quit_flag = False
        self.prompt = "Choose one: "
        cmd.Cmd.__init__(self)

    def completenames(self, text, line, begidx, endidx):
        options = [b.text.lower() for b in self.dialog.buttons]
        options.append('quit')
        text = text.lower()
        return [option for option in options if option.startswith(text)]

    def default(self, line):
        line = line.strip().lower()
        for button in self.dialog.buttons:
            if button.text.lower().startswith(line):
                self.dialog.runCallback(button)
                self.quit_flag = True
                return
        cmd.Cmd.default(self, line)

    def do_quit(self, line):
        app.cli_interpreter.quit_flag = self.quit_flag = True

    def postcmd(self, stop, line):
        return self.quit_flag

def handle_dialog(dialog):
    print_box("Question: %s" % dialog.title)
    print_text(dialog.description)
    print '   '.join(['[%s]' % button.text for button in dialog.buttons])

    command = DialogAsker(dialog)
    command.cmdloop()
