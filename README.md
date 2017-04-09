# Rerun
Rerun is a tool to run shell commands and GUI applications by just typing the command. It comes with a few unique features too:

 1. Support for Switchable Graphics using PRIME.
 2. Run applications as Root, including Graphical Applications.
 3. Tooltip-based help and built-in documentation, all in a single window.
 4. No useless bloat or 'features'. Just whats sometimes necessary.
 5. Easily customizable and fast. Made using Python and Glade.
 6. Free, Open Source and forever-supported.
 7. Modern with support for Wayland (including running apps as root under wayland)
 8. Comes with tips and a fix for possible issue faced.
 9. Uses multithreading to prevent conflicts and also to prevent freezes.

## Explanations and Reasoning

#### Why sudo and not pkexec?
Well, for one, pkexec does not support Wayland while trying to run graphical applications.  
For another, pkexec requires every application to have a seperate policy file. Some applications that require root are yet to support this.  
However, I do plan on supporting pkexec in the next release. But it won't be the default and sudo will stay default until pkexec gets proper Wayland support. It will instead be added as a togglable option just like with Switchable Graphics.

#### Is this an alternative to Alt-F2?
Yes and No. If you mean simply running commands, then Yes. If you mean, Desktop-specific features (like 'r' & 'lg' in GNOME), No.  
Also, Rerun has no auto-complete feature as with KDE's Alt-F2 interface.

#### Auto-completion. Any Plans?
Maybe in the future. But for now, focus is on stabilizing and standardizing the code. I will never implement a full-fledged search interface or anything like that. Maybe something that simply browses /bin and /usr/bin.

#### Do standards matter to you?
Yes. Absolutely. The python code is PEP8-compliant and non-complex according to McCabe. The XML is valid as expected from Glade.

#### Then, isn't shell=True unsafe?
No, not in this case. In this case, the command run is from the user anyway and the user could do the same thing from his terminal.

#### Is Rerun an application launcher?
Not quite. Sure, you could use it to run apps. But Rerun simply runs commands, has no auto-complete, no ability to run applications by their true names, etc.