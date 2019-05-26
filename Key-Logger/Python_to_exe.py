from cx_Freeze import setup, Executable
setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        #options = {"build_exe": build_exe_options},
        executables = [Executable("D:/hh.py")])