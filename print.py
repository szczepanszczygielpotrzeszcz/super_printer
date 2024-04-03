class Printer:
	def __init__(self):
		print("Init the printer.")
		print()

		self.data = 0

	def print(self, data):
		print(data)

	def print_nl(self, data):
		print(data)
		print()

	def print_tuple(self, tpl, nl=False):
		print(f"The tuple: {tpl}")
		if nl: print()

	def print_list(self, ls, nl=False):
		print(f"The list: {ls}")
		if nl: print()
	
	def print_dict(self, dict, nl=False):
		print(f"The dict: {dict}")
		if nl: print()

def code1():
	pr = Printer()

	pr.print("abc")
	pr.print(123)
	pr.print_nl("abc with nl")
	print()

	pr.print_tuple((3, 4, 5))
	pr.print_list([1, 10, 100])
	pr.print_dict({ "abc" : 100, "def" : 400 })
	print()



if __name__ == "__main__":
	print("Printer tests.")
	print()

	code1()
