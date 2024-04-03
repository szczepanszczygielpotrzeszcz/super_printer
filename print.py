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


if __name__ == "__main__":
	print("Printer tests.")
	print()

	pr = Printer()

	pr.print("abc")
	pr.print(123)
	pr.print_nl("abc with nl")
	print()

	pr.print_tuple((3, 4, 5))
	pr.print_list([1, 10, 100])
	print()
