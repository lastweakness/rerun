#!/usr/bin/env python
#
# Rerun is a Gtk+3 application launcher, command runner, root runner and
# graphics switcher (run application with PRIME turned on). BUT thats all
# it does. No added features, not many bug fixes or anything else.
# No bloat whatsoever, no feature creep.
# Licensing and other notes at the end.
from __future__ import print_function
BUILDERTEXT = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0

The MIT License (MIT)
This file is part of Rerun

Copyright (c) 2017 Mufeed Ali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Mufeed Ali

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
                  <object class="GtkRadioButton" id="prdefault">
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
                  <object class="GtkRadioButton" id="pron">
                    <property name="label" translatable="yes">Enabled</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">prdefault</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="proff">
                    <property name="label" translatable="yes">Disabled</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">prdefault</property>
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
              <object class="GtkImage" id="primewhat">
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
              <object class="GtkImage" id="rootsafe">
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
              <object class="GtkLabel" id="rootlab">
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
                  <object class="GtkRadioButton" id="pkexecopt">
                    <property name="label" translatable="yes">pkexec</property>
                    <property name="visible">True</property>
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
                  <object class="GtkRadioButton" id="sudopt">
                    <property name="label" translatable="yes">sudo</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="tooltip_markup" translatable="yes">Running GUI apps with sudo is &lt;b&gt;not&lt;/b&gt; recommended.</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">pkexecopt</property>
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
              <object class="GtkEntry" id="rootpass">
                <property name="can_focus">True</property>
                <property name="tooltip_markup" translatable="yes">This is &lt;b&gt;NOT&lt;/b&gt; root password. Just the User password.</property>
                <property name="visibility">False</property>
                <property name="activates_default">True</property>
                <property name="placeholder_text" translatable="yes">User Password</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkSwitch" id="rootrun">
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
          <object class="GtkBox" id="xfix">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkButton" id="xfixbutton">
                <property name="label" translatable="yes">Fix 'Run As Root' on Wayland</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="relief">half</property>
                <signal name="clicked" handler="xfixpress" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkImage" id="xfixinfo">
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
          <object class="GtkBox" id="hovers">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="hexpand">True</property>
            <property name="spacing">8</property>
            <child>
              <object class="GtkLabel" id="safety">
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
              <object class="GtkLabel" id="about">
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
              <object class="GtkEntry" id="command">
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

    def gload():
        global builder
        builder = Gtk.Builder()
        builder.add_from_string(BUILDERTEXT)
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


class main():

    def run(self, cmd, sin=None, rpass=None, prime=0):
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

    def threadrun(self, cmd, sin=None, rpass=None, prime=0):
        if prime == 0:
            threading.Thread(target=self.run,
                             args=(cmd, sin, rpass)).start()
        else:
            threading.Thread(target=self.run,
                             args=(cmd, sin, rpass),
                             kwargs={'prime': prime, }).start()

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
            self.threadrun(command.get_text())
        elif pron.get_active():
            self.threadrun(command.get_text(), prime=2)
        elif proff.get_active():
            self.threadrun(command.get_text(), prime=1)

    def sudorun(self):
        if prdefault.get_active():
            if rootpass.get_sensitive():
                self.threadrun('sudo -S "' + command.get_text().strip() +
                               '"', subprocess.PIPE, rootpass.get_text())
            else:
                self.threadrun('pkexec "' + command.get_text().strip() + '"')
        elif pron.get_active():
            self.primeroot(rootpass, command, 1)
        elif proff.get_active():
            self.primeroot(rootpass, command, 0)

    def primeroot(self, rootpass, command, primeval):
        if rootpass.get_sensitive():
            self.threadrun('sudo -S "' + command.get_text().strip() +
                           '"', subprocess.PIPE, rootpass.get_text(),
                           prime=primeval + 1)
        else:
            self.threadrun('pkexec "' + command.get_text().strip() + '"',
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
            subprocess.Popen(["xhost", "si:localuser:root"],
                             stdout=open(os.devnull, 'w'))
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