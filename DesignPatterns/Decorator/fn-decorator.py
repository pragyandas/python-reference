def addKetchup(fn):
	def wrapper():
		#Wrap the function to add before and after scripts
		#to the function execution
		print("Added Ketchup")
		fn()
		print("Burger Ready")

	return wrapper

#Decorating function
@addKetchup
def prepare_burger():
	print('Prepare Patty')

prepare_burger()

