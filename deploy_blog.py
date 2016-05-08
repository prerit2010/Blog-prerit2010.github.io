import os, shutil, sys
from distutils.dir_util import copy_tree

destination = '/home/prerit2010/projects/prerit2010.github.io'
source = '/home/prerit2010/projects/Blog-prerit2010.github.io/_site'
ignore = ['README.md','.git', '.gitignore']

for the_file in os.listdir(destination):
    if the_file not in ignore:
	    file_path = os.path.join(destination, the_file)
	    try:
	        if os.path.isfile(file_path):
	            os.unlink(file_path)
	        elif os.path.isdir(file_path): shutil.rmtree(file_path)
	    except Exception as e:
	        print(e)
	    
print "\nFiles Deleted from prerit2010.github.io repository!\n"

copy_tree(source, destination)
print "files copied from _site to prerit2010.github.io"

try:
	commit_message = sys.argv[1]
except:
	print "No commit message written"
else:
	import git
	repo = git.Repo(destination)
	print repo.git.add(u=True)
	print repo.git.commit( m=commit_message)
	print "Pushing......"
	print repo.git.push()
	print "\nPushed to prerit2010.github.io\n"


