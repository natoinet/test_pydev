The output with Pydev is:
```
pydev debugger: starting (pid: 13268)
utf-8
Traceback (most recent call last):
  File "/Applications/eclipse/plugins/org.python.pydev_3.9.2.201502050007/pysrc/pydevd.py", line 2235, in <module>
    globals = debugger.run(setup['file'], None, None)
  File "/Applications/eclipse/plugins/org.python.pydev_3.9.2.201502050007/pysrc/pydevd.py", line 1661, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/eclipse/plugins/org.python.pydev_3.9.2.201502050007/pysrc/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc) 
  File "/Users/antoinebrunel/src/test/python/test_pydev/test_pydev/test_pydev.py", line 18, in <module>
    for keyword in csvreader:
  File "/Users/antoinebrunel/.virtualenvs/test_pydev_venv/lib/python3.4/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 0: ordinal not in range(128)
```

The output while running it from the console is:
```
> . ~/test_pydev_venv/bin/activate
> python test_pydev.py
utf-8
é
```
