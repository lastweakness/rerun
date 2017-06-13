#!/usr/bin/env python
#
# Rerun is a Gtk+3 application launcher, command runner, root runner and
# graphics switcher (run application with PRIME turned on). BUT thats all
# it does. No added features, not many bug fixes or anything else.
# No bloat whatsoever, no feature creep.
# Licensing and other notes at the end.
from __future__ import print_function
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--safe", action="store_true",
                    help="Turn on safe mode. This turns off the usage of " +
                         "shell in Rerun. This has an added security bonus " +
                         "but restricts usage of Rerun because of the lack " +
                         "of operators like '&&' or '||'.")
parsed = parser.parse_args()
if parsed.safe:
    from rerun_core import (safeThreadRun as ThreadRun,
                            pkexecSafeThreadRun as pkexecThreadRun,
                            sudoSafeThreadRun as sudoThreadRun)
    print("Safe Mode is On.")
else:
    from rerun_core import ThreadRun, pkexecThreadRun, sudoThreadRun

if __name__ == "__main__":
    import sys
    import os
    try:
        import gi
        gi.require_version('Gtk', '3.0')  # inform the PC that we need GTK+ 3.
        import gi.repository.Gtk as Gtk  # this is the GNOME depends
    except ImportError as imper:
        print("Importing GObject failed!")
        print("Install GObject bindings.")
        print(imper)
        sys.exit(1)

    def Load_GUI():
        global builder
        GLADEFILE = os.path.dirname(os.path.realpath(__file__)) + "/rerun.ui"
        builder = Gtk.Builder()
        builder.add_from_file(GLADEFILE)
        window = builder.get_object('rerun')  # main window
        window.show_all()

    Load_GUI()
    command_entry = builder.get_object('command_entry')
    prime_on = builder.get_object('prime_on')
    prime_off = builder.get_object('prime_off')
    prime_default = builder.get_object('prime_default')
    root_entry = builder.get_object('root_entry')


class main():

    def on_window_destroy(self, rerun):
        Gtk.main_quit()

    def pktoggle(self, root_pkexec):
        root_entry.set_sensitive(False)

    def sutoggle(self, root_sudo):
        root_entry.set_sensitive(True)

    def switched(self, root_switch, crap=None):
        root_switch = builder.get_object('root_switch')
        root_pkexec = builder.get_object('root_pkexec')
        root_sudo = builder.get_object('root_sudo')
        if root_switch.get_active():
            root_pkexec.set_sensitive(True)
            root_sudo.set_sensitive(True)
        else:
            root_pkexec.set_sensitive(False)
            root_sudo.set_sensitive(False)

    def NormalRun(self, Command):
        if prime_default.get_active():
            ThreadRun(Command)
        elif prime_on.get_active():
            ThreadRun(Command, PRIME=2)
        elif prime_off.get_active():
            ThreadRun(Command, PRIME=1)

    def RunAsRoot(self, Command):
        if prime_default.get_active():
            if root_entry.get_sensitive():
                sudoThreadRun(Command, root_entry.get_text())
            else:
                pkexecThreadRun(Command)
        elif prime_on.get_active():
            self.PRIMERootRun(Command, 2)
        elif prime_off.get_active():
            self.PRIMERootRun(Command, 1)

    def PRIMERootRun(self, Command, PRIME):
        if root_entry.get_sensitive():
            sudoThreadRun(Command, root_entry.get_text(), PRIME)
        else:
            pkexecThreadRun(Command, PRIME)

    def on_run_clicked(self, run):
        root_switch = builder.get_object('root_switch')
        try:
            Command = command_entry.get_text().strip()
            if not Command == '':
                if not root_switch.get_active():
                    self.NormalRun(Command)
                else:
                    self.RunAsRoot(Command)
        except Exception as exe:
            print('Failed to run command!')
            print(exe)

    def XFix(self, xfix=None):
        try:
            XHostFix()
        except Exception as exe:
            print("Running the command failed. Something wrong with")
            print("your PC? This shouldn't be happening. Error:")
            print(exe)


if __name__ == "__main__":
    builder.connect_signals(main())
    Gtk.main()

# LICENSING:
#
# The MIT License (MIT)
#
# Copyright (c) 2017 Mufeed Ali
# This file is part of Rerun
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Mufeed Ali
