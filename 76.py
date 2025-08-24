Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.name
'posix'
>>> os.mkdir(nanna)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.mkdir(nanna)
NameError: name 'nanna' is not defined
>>> os.mkdir("nanna")
>>> os.getcwd()
'/Users/harshavardhankonanki/Documents'
>>> os.chdir("Documents")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.chdir("Documents")
FileNotFoundError: [Errno 2] No such file or directory: 'Documents'
>>> os.chdir("/Users/harshavardhankonanki/Documents")
>>> os.getcwd()
'/Users/harshavardhankonanki/Documents'
>>> os.chdir("/Users/harshavardhankonanki")

>>> os.getcwd()
'/Users/harshavardhankonanki'
>>> os.listdir()
['.eclipse', '.config', 'Music', '.rest-client', 'seriesN.java', '.zshrc.omz-uninstalled-2022-12-30_19-19-12', '.zcompdump-HarshaVardhan’s MacBook Air-5.8.1', '.DS_Store', 'eclipse', '.CFUserTextEncoding', '.jssc', '.zshrc', '.psql_history', '.mongodb', 'Pictures', '.zprofile', 'node_modules', 'code', '<!DOCTYPE html>.html', '.zsh_history', '.p2', 'Desktop', 'Library', 'eclipse-workspace', '.lesshst', 'TAB', '.oracle_jre_usage', 'committers-2021-12', '.bash_sessions', 'Public', '.idlerc', 'OneDrive - K L University', '.ssh', 'Movies', 'Applications', '.Trash', '.npm', 'Documents', '.anydesk', 'wrute and read student details ', '.vscode', '.oh-my-zsh', 'Downloads', '.cache', '.bash_history', '.zsh_sessions']
