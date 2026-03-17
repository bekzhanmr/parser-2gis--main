import os
import sys

if getattr(sys, "frozen", False):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))

    tcl_candidates = [
        os.path.join(base_path, "_tcl_data"),
        os.path.join(base_path, "tcl8.6"),
        os.path.join(base_path, "lib", "tcl8.6"),
    ]

    tk_candidates = [
        os.path.join(base_path, "_tk_data"),
        os.path.join(base_path, "tk8.6"),
        os.path.join(base_path, "lib", "tk8.6"),
    ]

    for path in tcl_candidates:
        if os.path.isdir(path):
            os.environ["TCL_LIBRARY"] = path
            break

    for path in tk_candidates:
        if os.path.isdir(path):
            os.environ["TK_LIBRARY"] = path
            break