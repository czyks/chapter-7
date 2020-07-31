import os

def run(**args):
	
	print "[*] w module dirliste."
	files = os.listdir(".")

	return str(files)

