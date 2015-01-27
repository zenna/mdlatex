#!/usr/bin/python

import os.path

import subprocess
try:
  config_file = open("config", 'r')
except:
  raise IOError("No config file found")

config = [l.strip() for l in config_file.readlines()]
if len(config) < 2: raise Error("config file must have at least two entries: name and an md")

paper = config[0]
md_string = ["md/%s.md" % s for s in config[1:]]
md_string = " ".join(md_string)

print("Converting Markdown to Latex")
tex_out = "pandoctex/%spandoc.tex" % paper

bashCommand = "pandoc --template super.template %s -s -o %s" % (md_string, tex_out)
print(bashCommand)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

print("Compiling with Latex")
bashCommand = "pdflatex -output-directory=pandoctex %s" % tex_out
print(bashCommand)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

# Do the conference specific shit
template_fname = "%s.template" % paper
print("Looking for template %s" % template_fname)
if os.path.isfile(template_fname):
  print("Compiling Conference Specific")
  tex_out = "%stex/%s.tex" % (paper,paper)
  bashCommand = "pandoc --template %s.template %s -s -o %s" % (paper, md_string, tex_out)
  print(bashCommand)
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
  
  print("Compiling with Latex")
  bashCommand = "pdflatex -output-directory=%stex %s" % (paper,tex_out)
  print(bashCommand)
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output = process.communicate()[0]
else:
  print("Couldn't find %s - skipping" % template_fname)

config_file.close()