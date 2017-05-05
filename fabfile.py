
from fabric.api import local

def test1():

	local("cd /home/praveen/python/fabricscripts/fabric-test1 && touch file1 file2 file3")

	local("cd /home/praveen/python/fabricscripts/fabric-test1 && git add . && git commit -m test")

	local("cd /home/praveen/python/fabricscripts/fabric-test1 && git push origin master")
