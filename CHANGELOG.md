# Changelog
`IMP` = Important Note or Announcement related to the release  
`FIX` = Bug-fix  
`NEW` = New feature
`CNG` = Changes  
`MOD` = Changes to the module or API
`SPD` = Changes effecting Performance

## Current versions following Semantic Versioning
### 4.0.0 - 2017-06-29
- `IMP` The module (or API) has changed a lot and has been expanded. The module
has been split-off into `rerun_core.py` which rerun also imports.
- `NEW` Added a Safe Mode where the shell is not invoked. This allows the user
to not have to worry about possible security issues with the shell.
- `NEW` Ability to parse command-line input. For now, just `-s` or `--safe`.
- `NEW` Added 'Return' key as hotkey so that it works anywhere on the UI.
- `CNG` SFRun structure changed, but still single-file.
- `CNG` A lot of functions' and objects' names have changed for the sake of
Human readability.
- `CNG` Way better in-code documentation with `docstrings` and more.
- `MOD` Functions have been renamed, refer to README.
- `MOD` New functions have been added, refer to README.

### 3.0.0 - 2017-06-09
- `IMP` New module (or API), Follows Semantic Versioning, adds a changelog
- `FIX` Fixes signal sent during crash due to not finding GTK+ bindings
- `NEW` An module (or API) and the ability to import Rerun without rendering the
 UI
- `CNG` The application structure has been reworked again.

## Before Semantic Versioning
### 2.0.1 - 2017-06-04
- `FIX` Fixes wrong license info in the UI
- `CNG` The entire application structure has been reworked for better
performance and simpicity
- `SPD` Speed of running commands and responsiveness have increased

### 2.0.0 - 2017-05-03
- `FIX` Fixes a UI glitch in Adapta GTK theme
- `NEW` Switched License to the permissive MIT License
- `NEW` Support for running programs as root through `pkexec` has been added
- `CNG` Greatly Improved UI
- `SPD` Faster Launch and better structure

### 1.1.1 - 2017-04-17
- `CNG` Updated SFRun

### 1.1.0 - 2017-04-17
- `CNG` Improved UI Layout

### 1.0.1 - 2017-04-09
- `NEW` Added SFRun - A single-file version of Rerun
- `SPD` Optimizations

### 1.0.0 - 2017-04-08
- `NEW` Initial release licensed under GPLv3
