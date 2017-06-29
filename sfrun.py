#!/usr/bin/env python
#
# Rerun is a Gtk+3 application launcher, command runner, root runner and
# graphics switcher (run application with PRIME turned on). BUT thats all
# it does. No added features, not many bug fixes or anything else.
# No bloat whatsoever, no feature creep.
# Licensing and other notes at the end.
from __future__ import print_function
import argparse
import os
import subprocess  # for processes.
import threading
import shlex
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--safe", action="store_true",
                    help="Turn on safe mode. This turns off the usage of " +
                         "shell in Rerun. This has an added security bonus " +
                         "but restricts usage of Rerun because of the lack " +
                         "of operators like '&&' or '||'.")
parsed = parser.parse_args()


def Run(Command, stdin=None, RootPassword=None, PRIME=0):
    envi = os.environ.copy()
    if PRIME == 1:
        envi["DRI_PRIME"] = "0"
    elif PRIME == 2:
        envi["DRI_PRIME"] = "1"
    if parsed.safe:
        Command = shlex.split(Command)
        ShInvoke = False
        print("Safe Mode is on.")
    else:
        ShInvoke = True
    with open(os.devnull, 'w') as NULLMAKER:
        p = subprocess.Popen(Command, stdin=stdin, shell=ShInvoke,
                             stdout=NULLMAKER, stderr=NULLMAKER,
                             env=envi)
    if stdin is not None:
        p.stdin.write(RootPassword.encode() + b'\n')
        p.stdin.close()


def ThreadRun(Command, stdin=None, RootPassword=None, PRIME=0):
    if PRIME == 0:
        threading.Thread(target=Run,
                         args=(Command, stdin,
                               RootPassword)).start()
    elif PRIME == 1 or PRIME == 2:
        threading.Thread(target=Run,
                         args=(Command, stdin, RootPassword),
                         kwargs={'PRIME': PRIME, }).start()


def sudoThreadRun(Command, RootPassword=None, PRIME=0):
    ThreadRun('sudo -S ' + Command, subprocess.PIPE, RootPassword,
              PRIME)


def pkexecThreadRun(Command, PRIME=0):
    ThreadRun('pkexec ' + Command, PRIME=PRIME)

BUILDERTEXT = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0
-->
<interface>
  <requires lib="gtk+" version="3.16"/>
  <!-- interface-license-type mit -->
  <!-- interface-name Rerun -->
  <!-- interface-description A tool to run GUI applications or simple commands with additional options and better support. -->
  <!-- interface-copyright 2017 Mufeed Ali -->
  <!-- interface-authors Mufeed Ali -->
  <object class="GtkWindow" id="rerun">
    <property name="can_focus">False</property>
    <property name="window_position">center</property>
    <property name="default_width">250</property>
    <property name="default_height">85</property>
    <signal name="destroy" handler="on_window_destroy" swapped="no"/>
    <child>
      <object class="GtkBox" id="activatables">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="margin_left">4</property>
        <property name="margin_right">4</property>
        <property name="margin_top">4</property>
        <property name="margin_bottom">4</property>
        <property name="orientation">vertical</property>
        <property name="spacing">4</property>
        <child>
          <object class="GtkBox" id="primebox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkLabel" id="primelabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">PRIME:</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox" id="primeradios">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkRadioButton" id="prime_default">
                    <property name="label" translatable="yes">Default</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="prime_on">
                    <property name="label" translatable="yes">Enabled</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">prime_default</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="prime_off">
                    <property name="label" translatable="yes">Disabled</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">prime_default</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkImage" id="prime_infimg">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="tooltip_markup" translatable="yes">&lt;b&gt;This is ONLY for switchable graphics devices&lt;/b&gt;
This has NO effect, negative or positive, on single graphics devices.
This sets the state of use of Discrete cards on switchable graphics devices. It is the same as using (or not using) the DRI_PRIME environment variable.
&lt;b&gt;NOTE&lt;/b&gt;: If you use PRIME while running applications as root, it is suggested to use sudo as pkexec remains untested.</property>
                <property name="margin_top">2</property>
                <property name="margin_bottom">2</property>
                <property name="icon_name">help-info-symbolic</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack_type">end</property>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="rootbox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkImage" id="root_infimg">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="tooltip_markup" translatable="yes">Running graphical applications as root is not recommended.
The recommended way to run anything as root is &lt;b&gt;pkexec&lt;/b&gt; and it works very well with X11 and as of recently, Wayland too. Therefore, pkexec is the current default method for running applications as root.
In Rerun, &lt;b&gt;sudo&lt;/b&gt; is a second option to pkexec as pkexec may not work with everything you wish to use. But sudo is &lt;b&gt;not&lt;/b&gt; recommended and the better option is always &lt;b&gt;pkexec&lt;/b&gt;.</property>
                <property name="icon_name">help-info-symbolic</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack_type">end</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="root_label">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Run As Root</property>
                <property name="use_markup">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox" id="rootopt">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkRadioButton" id="root_pkexec">
                    <property name="label" translatable="yes">pkexec</property>
                    <property name="visible">True</property>
                    <property name="sensitive">False</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="tooltip_markup" translatable="yes">pkexec is the new &lt;b&gt;standard&lt;/b&gt; way of executing applications as root. This is recommended way to go.</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <signal name="clicked" handler="pktoggle" swapped="no"/>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="root_sudo">
                    <property name="label" translatable="yes">sudo</property>
                    <property name="visible">True</property>
                    <property name="sensitive">False</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="tooltip_markup" translatable="yes">Running GUI apps with sudo is &lt;b&gt;not&lt;/b&gt; recommended.</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">root_pkexec</property>
                    <signal name="clicked" handler="sutoggle" swapped="no"/>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkEntry" id="root_entry">
                <property name="visible">True</property>
                <property name="sensitive">False</property>
                <property name="can_focus">True</property>
                <property name="tooltip_markup" translatable="yes">This is &lt;b&gt;NOT&lt;/b&gt; root password. Just the User password.</property>
                <property name="visibility">False</property>
                <property name="activates_default">True</property>
                <property name="placeholder_text" translatable="yes">User Password</property>
                <property name="input_purpose">password</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkSwitch" id="root_switch">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="margin_top">2</property>
                <property name="margin_bottom">2</property>
                <signal name="state-set" handler="switched" swapped="no"/>
                <accelerator key="r" signal="activate" modifiers="GDK_CONTROL_MASK"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack_type">end</property>
                <property name="position">3</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="box_xfix">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkButton" id="xfix">
                <property name="label" translatable="yes">Fix 'Run As Root' on Wayland</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="relief">half</property>
                <signal name="clicked" handler="XFix" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkImage" id="xfix_infimg">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="tooltip_markup" translatable="yes">&lt;b&gt;This is usually only needed on Wayland&lt;/b&gt;
On Wayland, GUI applications may not run as root due to xhost access control. This can be worked around every boot by clicking this button. Better yet, you can make this command run on every boot (this feature will be built-in in an upcoming release).
This fix (or workaround) tells xhost to allow root to run graphical applications. It is the same as running "xhost si:localuser:root" on every boot.</property>
                <property name="margin_left">8</property>
                <property name="margin_top">4</property>
                <property name="margin_bottom">4</property>
                <property name="icon_name">help-info-symbolic</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack_type">end</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="box_hover">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="hexpand">True</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkLabel" id="safety_info">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="tooltip_markup" translatable="yes">&lt;b&gt;Warnings&lt;/b&gt;
Rerun might be simple, as is the commandline. But just as in the commandline, you have to try and be safe.
 1. Do NOT randomly copy and paste commands from the internet.
 2. Review every command carefully may it be a root command or otherwise (eg: systemctl)
 3. Do not do random typing.
 4. Rerun is basically a shell interface. &lt;span size="x-small"&gt;[shell=True if you know python]&lt;/span&gt; This also means that you can run non-graphical commands like 'rm'. So, be careful and &lt;b&gt;DON'T&lt;/b&gt; run " rm * " or anything of the sort.
&lt;b&gt;Tips&lt;/b&gt;
 1. As said before, Rerun is a GUI for shell. So, it also has a default working directory, which is wherever it is run from. You could even use cd to go into other working directories. It also supports multiple commands in one string, for example, "sleep 3h; systemctl shutdown". That would work and so would "cd ~ ; ./myscript.sh" given that they're all real paths accessible from shell.
 2. The command seen earlier, "sleep 3h ; systemctl shutdown", is a nice way to schedule a shutdown using Rerun. In this case, it shuts down after 3 hours.</property>
                <property name="label" translatable="yes">&lt;b&gt;Safety Warnings and Tips&lt;/b&gt; &lt;span size="x-small"&gt;[hover over to read]&lt;/span&gt;</property>
                <property name="use_markup">True</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkSeparator" id="hsep">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="about_info">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="tooltip_markup" translatable="yes">&lt;span size="large"&gt;About Rerun&lt;/span&gt;
Rerun is a tool to run shell commands or applications directly while ignoring output and disallowing input. This allows quickly running applications like gedit or nautilus.
Rerun has a few tricks up its sleeve: Support for switchable graphics, Run As Root and a tiny fix. It is also very highly optimized for speed. Anything the shell can do, Rerun can do too but just safer and with no output.
Everything was made from ground-up to be customizable and easy to use and fast. So, enjoy!

Author: Mufeed Ali &lt;span size="x-small"&gt;[nightglare or mufeed20 or mufeed2000][mufeed.ali53@gmail.com]&lt;/span&gt;
License: MIT Permissive License</property>
                <property name="label" translatable="yes">&lt;b&gt;About Rerun&lt;/b&gt; &lt;span size="x-small"&gt;[hover to read]&lt;/span&gt;</property>
                <property name="use_markup">True</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">3</property>
          </packing>
        </child>
      </object>
    </child>
    <child type="titlebar">
      <object class="GtkHeaderBar" id="runhead">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="show_close_button">True</property>
        <property name="decoration_layout">minimize:close</property>
        <child type="title">
          <object class="GtkBox" id="mainbox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_left">8</property>
            <property name="margin_right">8</property>
            <property name="hexpand">True</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkEntry" id="command_entry">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="has_focus">True</property>
                <property name="is_focus">True</property>
                <property name="hexpand">True</property>
                <property name="activates_default">True</property>
                <property name="placeholder_text" translatable="yes">Type your command here...</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkSeparator" id="sep2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="run">
                <property name="label" translatable="yes">Run</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="can_default">True</property>
                <property name="has_default">True</property>
                <property name="receives_default">True</property>
                <property name="relief">none</property>
                <signal name="clicked" handler="on_run_clicked" swapped="no"/>
                <accelerator key="Return" signal="clicked"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkSeparator" id="sep1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="maintitle">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">&lt;span size="large"&gt;Rerun&lt;/span&gt;
&lt;span size="x-small"&gt;Simple. Thats all.&lt;/span&gt;</property>
                <property name="use_markup">True</property>
                <property name="justify">right</property>
                <property name="track_visited_links">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">4</property>
              </packing>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>"""

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
