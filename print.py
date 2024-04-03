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


if __name__ == "__main__":
	print("Printer tests.")
	print()

	pr = Printer()

	pr.print("abc")
	pr.print(123)
	pr.print_nl("abc with nl")
