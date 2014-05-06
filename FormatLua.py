import os
import subprocess
import sublime
import sublime_plugin
import re
from os.path import basename
from os.path import join

class FormatLuaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        # if there are more than 1 region or region one and it's not empty
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    s = view.substr(region)
                s = self._run(s)
                view.replace(edit, region, s)
        else:   #format all text
            alltextreg = sublime.Region(0, view.size())
            s = view.substr(alltextreg)
            s = self._run(s)
            view.replace(edit, alltextreg, s)

    def _run(self, s):
        # settings = self.view.settings()
        # indent_char = " " if settings.get("translate_tabs_to_spaces") else "\t"
        # indent_char = " " #TODO indent by TAB (currently not supported in python-sqlparse)
        # indent_size = int(settings.get("tab_size")) if indent_char == " " else 1
        s = s.encode("utf-8")
        packages_path = join(sublime.packages_path(), "FormatLua")
        os.chdir(packages_path)
        tmp = 'tmp.lua'
        fileHandle = open(tmp, 'w')
        fileHandle.write(s)
        fileHandle.close()
        settings = sublime.load_settings('FormatLua.sublime-settings')
        lua_path = settings.get('lua_path')
        cmd = lua_path + ' formatter.lua --file ' + tmp
        # print cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sourcecode = p.stdout.read()
        os.remove(tmp)
        return sourcecode.decode('utf-8')

