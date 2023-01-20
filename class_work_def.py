def greeting(client_name : str):
    print(f"Hi, {client_name} = )")


def get_client_name():
    client_name = input("Please enter your name: ")
    return client_name

def farewell(client_name : str = ''):
    print(f"Goodbye {client_name} =(")



client_name = get_client_name()
greeting(client_name=client_name)
farewell(client_name=client_name)





def get_dates():
    name = input("Enter your name: ")
    surname = input("Enter your last_name: ")
    age = input("Enter your age: ")
    education = input("Enter your education: ")
    addres = input("Enter your addres")
    # Fix age
    if age >= 18:
        result = True
    else:
        result = False
        return result

def print_result(result: bool):
    if result:
        print("Adult")
    else:
        print("Where are you your parents")






