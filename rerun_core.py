#!/usr/bin/env python
#
# Rerun is a Gtk+3 application launcher, command runner, root runner and
# graphics switcher (run application with PRIME turned on). BUT thats all
# it does. No added features, not many bug fixes or anything else.
# No bloat whatsoever, no feature creep.
# Licensing and other notes at the end.
import os
import subprocess  # for processes.
import threading
import shlex


def Run(Command, stdin=None, RootPassword=None, PRIME=0):
    """Run a command. This does not use threading and may hang up the
     main thread and thus, the application"""
    envi = os.environ.copy()
    if PRIME == 1:
        envi["DRI_PRIME"] = "0"
    elif PRIME == 2:
        envi["DRI_PRIME"] = "1"
    with open(os.devnull, 'w') as NULLMAKER:
        p = subprocess.Popen(Command, stdin=stdin, shell=True,
                             stdout=NULLMAKER, stderr=NULLMAKER,
                             env=envi)
    if stdin is not None:
        p.stdin.write(RootPassword.encode() + b'\n')
        p.stdin.close()


def safeRun(Command, stdin=None, RootPassword=None, PRIME=0):
    """A safer variant of Run() that is invulnerable to shell injection"""
    envi = os.environ.copy()
    if PRIME == 1:
        envi["DRI_PRIME"] = "0"
    elif PRIME == 2:
        envi["DRI_PRIME"] = "1"
    with open(os.devnull, 'w') as NULLMAKER:
        p = subprocess.Popen(shlex.split(Command), stdin=stdin,
                             stdout=NULLMAKER, stderr=NULLMAKER,
                             env=envi)
    if stdin is not None:
        p.stdin.write(RootPassword.encode() + b'\n')
        p.stdin.close()


def ThreadRun(Command, stdin=None, RootPassword=None, PRIME=0):
    """Run a command without locking up the main thread by using 
    multithreading"""
    if PRIME == 0:
        threading.Thread(target=Run,
                         args=(Command, stdin,
                               RootPassword)).start()
    elif PRIME == 1 or PRIME == 2:
        threading.Thread(target=Run,
                         args=(Command, stdin, RootPassword),
                         kwargs={'PRIME': PRIME, }).start()


def safeThreadRun(Command, stdin=None, RootPassword=None, PRIME=0):
    """A safer variant of ThreadRun() that is invulnerable to shell 
    injection"""
    if PRIME == 0:
        threading.Thread(target=safeRun,
                         args=(Command, stdin,
                               RootPassword)).start()
    elif PRIME == 1 or PRIME == 2:
        threading.Thread(target=safeRun,
                         args=(Command, stdin, RootPassword),
                         kwargs={'PRIME': PRIME, }).start()


def sudoThreadRun(Command, RootPassword=None, PRIME=0):
    """A variant of ThreadRun() that runs the application as root
     using sudo."""
    ThreadRun('sudo -S ' + Command, subprocess.PIPE, RootPassword,
              PRIME)


def sudoSafeThreadRun(Command, RootPassword=None, PRIME=0):
    """A safer variant of sudoThreadRun() that is invulnerable to 
    shell injection."""
    safeThreadRun('sudo -S ' + Command, subprocess.PIPE, RootPassword,
                  PRIME)


def sudoRun(Command, RootPassword=None, PRIME=0):
    """A variant of Run() that runs the application as root using sudo."""
    Run('sudo -S ' + Command, subprocess.PIPE,
        RootPassword, PRIME)


def sudoSafeRun(Command, RootPassword=None, PRIME=0):
    """A safer variant of sudoRun() that is invulnerable to shell issues."""
    safeRun('sudo -S ' + Command, subprocess.PIPE,
            RootPassword, PRIME)


def pkexecThreadRun(Command, PRIME=0):
    """A variant of ThreadRun() that runs the application as root
     using pkexec."""
    ThreadRun('pkexec ' + Command, PRIME=PRIME)


def pkexecSafeThreadRun(Command, PRIME=0):
    """A safer variant of pkexecThreadRun() that is invulnerable to
     shell injection."""
    safeThreadRun('pkexec ' + Command, PRIME=PRIME)


def pkexecRun(Command, PRIME=0):
    """A variant of Run() that runs the application as root using pkexec."""
    Run('pkexec ' + Command, PRIME=PRIME)


def pkexecSafeRun(Command, PRIME=0):
    """A safer variant of pkexecRun() that is invulnerable to shell issues."""
    safeRun('pkexec ' + Command, PRIME=PRIME)


def XHostFix():
    """Fixes possible launch issues on Wayland"""
    with open(os.devnull, 'w') as NULLMAKER:
        subprocess.Popen(["xhost", "si:localuser:root"],
                         stdout=NULLMAKER)

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
