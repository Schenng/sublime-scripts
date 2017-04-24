import sublime
import sublime_plugin
import os
import subprocess

class devupCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    path = "/Users/simoncheng/src/github.com/Shopify/shopify/"
    os.chdir(path)

    command_cd = 'tell app "Terminal" to do script "cd %s" in window 1' % path
    command_test = 'tell app "Terminal" to do script "dev up" in window 1'
    #self.view.insert(edit, 0, command)

    subprocess.call(['osascript', '-e', command_cd])
    subprocess.call(['osascript', '-e', command_test])

class devdownCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    path = "/Users/simoncheng/src/github.com/Shopify/shopify/"
    os.chdir(path)

    command_cd = 'tell app "Terminal" to do script "cd %s" in window 1' % path
    command_test = 'tell app "Terminal" to do script "dev down" in window 1'
    #self.view.insert(edit, 0, command)

    subprocess.call(['osascript', '-e', command_cd])
    subprocess.call(['osascript', '-e', command_test])

class devsCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    path = "/Users/simoncheng/src/github.com/Shopify/shopify/"
    os.chdir(path)

    command_cd = 'tell app "Terminal" to do script "cd %s" in window 1' % path
    command_test = 'tell app "Terminal" to do script "dev s" in window 1'
    #self.view.insert(edit, 0, command)

    subprocess.call(['osascript', '-e', command_cd])
    subprocess.call(['osascript', '-e', command_test])

class devtestCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    file_path = self.view.file_name()

    path = "/Users/simoncheng/src/github.com/Shopify/shopify/"
    os.chdir(path)

    command_cd = 'tell app "Terminal" to do script "cd %s" in window 1' % path
    command_test = 'tell app "Terminal" to do script "dev test %s" in window 1' % file_path
    #self.view.insert(edit, 0, command)

    subprocess.call(['osascript', '-e', command_cd])
    subprocess.call(['osascript', '-e', command_test])

