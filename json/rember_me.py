import json
def main():
	file_name = 'username.json'
	try:
		with open(file_name) as f_obj:
			username =  json.load(f_obj)
	except FileNotFoundError as e:
		username = input("please you name")
		with open(file_name,'w') as f_obj:
			json.dump(username,f_obj)
			print("we will remberyour name")
	# else:
	finally:
		print("welcome you back " + username)

if __name__ == '__main__':
	main()