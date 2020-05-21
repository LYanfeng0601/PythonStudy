import json

def write_into_json():
	numbers = [1,2,3,4,5,6]
	filename = 'number_josn'
	with open(filename,'w') as f_obj:
		json.dump(numbers,f_obj)
def output_from_json():
	filename = 'number_josn'
	with open(filename) as f_obj:
		number_out = json.load(f_obj)
	print(number_out)
	print(type(number_out))


if __name__ == '__main__':
	write_into_json()
	output_from_json()