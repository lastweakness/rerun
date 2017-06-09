#!/usr/bin/env python
#
# Rerun is a Gtk+3 application launcher, command runner, root runner and
# graphics switcher (run application with PRIME turned on). BUT thats all
# it does. No added features, not many bug fixes or anything else.
# No bloat whatsoever, no feature creep.
# Licensing and other notes at the end.
from __future__ import print_function
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

    def gload():
        global builder
        GLADEFILE = os.path.dirname(os.path.realpath(__file__)) + "/rerun.ui"
        builder = Gtk.Builder()
        builder.add_from_file(GLADEFILE)
        window = builder.get_object('rerun')  # main window
        window.show_all()

    gload()
    command = builder.get_object('command')
    pron = builder.get_object('pron')
    proff = builder.get_object('proff')
    prdefault = builder.get_object('prdefault')
    rootpass = builder.get_object('rootpass')
    pkexecopt = builder.get_object('pkexecopt')
    sudopt = builder.get_object('sudopt')
    rootpass.set_sensitive(False)
    pkexecopt.set_sensitive(False)
    sudopt.set_sensitive(False)
import subprocess  # for processes.
import threading


def run(cmd, sin=None, rpass=None, prime=0):
    denvi = os.environ.copy()
    if prime == 1:
        denvi["DRI_PRIME"] = "0"
    elif prime == 2:
        denvi["DRI_PRIME"] = "1"
    with open(os.devnull, 'w') as NULLMAKER:
        p = subprocess.Popen(cmd, stdin=sin, shell=True, stdout=NULLMAKER,
                             stderr=NULLMAKER, env=denvi)
    if sin is not None:
        p.stdin.write(rpass.encode() + b'\n')
        p.stdin.close()


def threadrun(cmd, sin=None, rpass=None, prime=0):
    if prime == 0:
        threading.Thread(target=run,
                         args=(cmd, sin, rpass)).start()
    else:
        threading.Thread(target=run,
                         args=(cmd, sin, rpass),
                         kwargs={'prime': prime, }).start()


class main():

    def on_window_destroy(self, rerun):
        Gtk.main_quit()

    def pktoggle(self, pkexecopt):
        rootpass.set_sensitive(False)

    def sutoggle(self, sudopt):
        rootpass.set_sensitive(True)

    def switched(self, rootrun, crap=None):
        rootrun = builder.get_object('rootrun')
        if rootrun.get_active():
            pkexecopt.set_sensitive(True)
            sudopt.set_sensitive(True)
        else:
            pkexecopt.set_sensitive(False)
            sudopt.set_sensitive(False)

    def regrun(self):
        if prdefault.get_active():
            threadrun(command.get_text())
        elif pron.get_active():
            threadrun(command.get_text(), prime=2)
        elif proff.get_active():
            threadrun(command.get_text(), prime=1)

    def sudorun(self):
        if prdefault.get_active():
            if rootpass.get_sensitive():
                threadrun('sudo -S "' + command.get_text().strip() + '"',
                          subprocess.PIPE, rootpass.get_text())
            else:
                threadrun('pkexec "' + command.get_text().strip() + '"')
        elif pron.get_active():
            self.primeroot(rootpass, command, 1)
        elif proff.get_active():
            self.primeroot(rootpass, command, 0)

    def primeroot(self, rootpass, command, primeval):
        if rootpass.get_sensitive():
            threadrun('sudo -S "' + command.get_text().strip() + '"',
                      subprocess.PIPE, rootpass.get_text(),
                      prime=primeval + 1)
        else:
            threadrun('pkexec "' + command.get_text().strip() + '"',
                      prime=primeval + 1)

    def on_run_clicked(self, run):
        rootrun = builder.get_object('rootrun')
        try:
            if not command.get_text().strip() == '':
                if not rootrun.get_active():
                    self.regrun()
                else:
                    self.sudorun()
        except Exception as exe:
            print('Failed to run command!')
            print(exe)

    def xfixpress(self, xfixbutton):
        try:
            with open(os.devnull, 'w') as NULLMAKER:
                subprocess.Popen(["xhost", "si:localuser:root"],
                                 stdout=NULLMAKER)
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
