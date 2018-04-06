import array
# This is a simple calculator which only does addition.
def run():
	
	
	collection = []
	# To ask the size of the collection
	arraySize = input("How many numbers you would like to have? ")

	# Create the array 

	i = 0
	# for loop right here 
	for i in range(0, arraySize):

		# User start input the numbers 
		collection.append(input("Please input the numbers here: "))
		i += 1

	print(collection)
	print("Goodbye")

def main():
	run()

	
if __name__ == "__main__": main()
