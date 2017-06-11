# Rerun
Rerun is a tool to run shell commands and GUI applications by just typing the command. It comes with a few unique features too:

 1. Support for Switchable Graphics using PRIME.
 2. Run applications as Root, including Graphical Applications.
 3. Tooltip-based help and built-in documentation, all in a single window.
 4. No useless bloat or 'features'. Just what is sometimes necessary.
 5. Easily customizable and fast. Made using Python and Glade.
 6. Free, Open Source and forever-supported.
 7. Modern with support for Wayland (including running apps as root under
     Wayland)
 8. Comes with tips and a fix for possible issue faced.
 9. Uses multi-threading to prevent conflicts and also to prevent freezes.
 10. Simple API that makes it easy to do just what is needed.
 11. Human-readable code that is easy to modify.

Rerun's master branch is perfectly stable with no reasons to not use it.

## Python Module or API
Rerun comes with a minimal python module called `rerun_core.py` that provides
threaded running as `ThreadRun` and normal running as `Run`.  There are also
their root variants and an additional `XHostFix` for fixing an issue on Wayland.
 Syntax is very similar for all except `XHostFix` which requires no arguments.

Most of the module is simply layering one function over the other.

## Usage of the Python module
```python
import rerun_core

# Regular ones first
rerun_core.Run(
        "CommanToRun",
        InputFileOrPipe,
        "RootPassword",
        int(PRIMEstatus)
        )
rerun_core.ThreadRun("CommanToRun", InputFileOrPipe, "RootPassword",
                     int(PRIMEstatus))

rerun_core.sudoRun(
        "CommanToRun",
        "RootPassword",
        int(PRIMEstatus)
        )
rerun_core.sudoThreadRun("CommanToRun", "RootPassword", int(PRIMEstatus))

rerun_core.pkexecRun(
        "CommanToRun",
        int(PRIMEstatus)
        )
rerun_core.pkexecThreadRun("CommanToRun", int(PRIMEstatus))

# Safer alternatives with other caveats
# They have the same syntax as their regular counter-parts:
rerun_core.safeRun("CommanToRun", InputFileOrPipe, "RootPassword",
                   int(PRIMEstatus))
rerun_core.safeThreadRun("CommanToRun", InputFileOrPipe, "RootPassword",
                         int(PRIMEstatus))
rerun_core.sudoSafeRun("CommanToRun", "RootPassword", int(PRIMEstatus))
rerun_core.sudoSafeThreadRun("CommanToRun", "RootPassword", int(PRIMEstatus))
rerun_core.pkexecSafeRun("CommanToRun", int(PRIMEstatus))
rerun_core.pkexecSafeThreadRun("CommanToRun", int(PRIMEstatus))

# Functions that are dissimilar to others and take no arguments
rerun_core.XHostFix()
```

## TO-DO

 - [ ] Better error-handling. `Ongoing`
 - [ ] Improve Documentation `Ongoing`
 - [x] Expand the module or API
 - [x] Define a module or an API
 - [x] Follow Semantic Versioning
 - [x] Keep a Changelog

## Explanations and Reasoning

#### Is this an alternative to Alt-F2?
Yes and No. If you mean simply running commands, then Yes. If you mean, Desktop-specific features (like 'r' & 'lg' in GNOME), No.  
Also, Rerun has no auto-complete feature as with KDE's Alt-F2 interface.

#### Auto-completion. Any Plans?
Maybe in the future. But for now, focus is on stabilizing and standardizing the code. I will never implement a full-fledged search interface or anything like that. Maybe something that simply browses /bin and /usr/bin.

#### Do standards matter to you?
Yes. Absolutely. The python code is PEP8-compliant and non-complex according to McCabe. The XML is valid as expected from Glade.

#### Then, isn't shell=True unsafe?
No, not in this case. In this case, the command run is from the user anyway and the user could do the same thing from his terminal. The security issue of the application would then be the actual use of the application itself. This should in no way hinder the user's actions.

#### Is Rerun an application launcher?
Not quite. Sure, you could use it to run apps. But Rerun simply runs commands, has no auto-complete, no ability to run applications by their true names, etc.
