# Rerun
Rerun is a tool to run shell commands and GUI applications by just typing the command. It comes with a few unique features too:

 1. Support for Switchable Graphics using PRIME.
 2. Run applications as Root, including Graphical Applications.
 3. Tooltip-based help and built-in documentation, all in a single window.
 4. No useless bloat or 'features'. Just whats sometimes necessary.
 5. Easily customizable and fast. Made using Python and Glade.
 6. Free, Open Source and forever-supported.
 7. Modern with support for Wayland (including running apps as root under Wayland)
 8. Comes with tips and a fix for possible issue faced.
 9. Uses multi-threading to prevent conflicts and also to prevent freezes.
 10. Simple code with less than 200 lines. (master branch)

Rerun's master branch is perfectly stable with no reasons to not use it.

## API
Rerun comes with a minimal API that provides threaded running as `threadrun` and normal running as `run`. Syntax is the same for both:
```python
import rerun

rerun.run("CommanToRun", InputFileOrPipe, "RootPassword", int(PRIMEstatus))
rerun.threadrun("CommanToRun", InputPipe, "RootPassword", int(PRIMEstatus))
```
`threadrun` is actually a layer over `run` that puts it through the python `threading` module.  
The API will be expanded in the near future to support all features of Rerun directly.

## TO-DO

 - [ ] Better error-handling.
 - [ ] Expand API
 - [ ] Improve Documentation
 - [x] Define an API
 - [x] Follow Semantic Versioning
 - [x] Keep a Changelog

## Explanations and Reasoning

#### Is this an alternative to Alt-F2?
Yes and No. If you mean simply running commands, then Yes. If you mean, Desktop-specific features (like 'r' & 'lg' in GNOME), No.  
Also, Rerun has no auto-complete feature as with KDE's Alt-F2 interface.

#### Auto-completion. Any Plans?
Maybe in the future. But for now, focus is on stabilizing and standardizing the code. I will never implement a full-fledged search interface or anything like that. Maybe something that simply browses /bin and /usr/bin.

#### Do standards matter to you?
Yes. Absolutely. The python code is almost PEP8-compliant (tiny sacrifice made for speed, one rule broken) and non-complex according to McCabe. The XML is valid as expected from Glade.

#### Then, isn't shell=True unsafe?
No, not in this case. In this case, the command run is from the user anyway and the user could do the same thing from his terminal. The security issue of the application would then be the actual use of the application itself. This should in no way hinder the user's actions.

#### Is Rerun an application launcher?
Not quite. Sure, you could use it to run apps. But Rerun simply runs commands, has no auto-complete, no ability to run applications by their true names, etc.
