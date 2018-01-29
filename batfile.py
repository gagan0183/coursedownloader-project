cont = "y"
while(cont == "y"):
	coursename = str(raw_input("Please enter a course name : "))
	url = str(raw_input("Please enter url : "))
	totalfile = int(raw_input("Please enter total number of file : "))
	f = open("p.bat", "a+")
	f.write('script.py {} "{}" {}\n'.format(coursename, url, totalfile));
	f.close()
	cont = str(raw_input("Do you want to continue (y/n) ? "))