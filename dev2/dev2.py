import gdb
import sys

class FindPointers(gdb.Command):
	def __init__ (self):
		gdb.Command.__init__ (self, "fpointers", gdb.COMMAND_NONE)

	def invoke (self, arg, from_tty):
		argv = gdb.string_to_argv(arg)
		address = int(argv[0], 16)	
		size = int(argv[1])
		for i in range(size):
			try:
				res = gdb.execute("x/gx %s" % hex(address+i), to_string=True)
				res = res.replace(":", "").replace("\n", "")
				res = res.split("\t")
				source = int(res[0], 16)
				content = int(res[1], 16)
				if(content >= address and content <= address+size):
					print("Pointer at", hex(source), "-->", hex(content))
			except:
				None

FindPointers()
