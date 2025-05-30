#try:
#    file = open("a_file.txt")
#    a_dictionary = {"k": "v"}
#    print(a_dictionary["k"])
#except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("a\n")
#except KeyError as error_message:
#    print(f"There is no {error_message} key")
#else:
#    content = file.read()
#   print(content)
#finally:
#   file.close()
#    print("File was closed.")


height = float(input(f"What is your height: "))
weight = int(input(f"What is your weight: "))

bmi = weight / height ** 2
print(bmi)