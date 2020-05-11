import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }
]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)               
    elif client in clients:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client_name, updated_client):
    global clients

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            clients[idx] = updated_client
            list_clients()    


def delete_client(client_name): #Returns found to validate in main execution if the clients exists in list
    global clients
    found = None

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            clients.pop(idx)
            list_clients() 
            found = True
        else:
            found = False

    return found            


def search_client(client_name):
    global clients
    found = None

    for client in clients:
        if client['name'] != client_name:
            found = False
            continue
        elif client['name'] == client_name:
            found = True
            break

    if found:
        print('The client is in client\'s list')
    else:
        print(f'The client {client_name} was not found')

    return found


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead clients list')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_from_user():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),         
            }

    return client
    

def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')
    
    return field


# def _get_client_name():
#     client_name = None

#     while not client_name:
#         client_name = input('What is the client name? ')  

#         if client_name == 'exit':
#             client_name = None
#             break 

#     if not client_name: 
#         sys.exit()
                
#     return client_name


if __name__ == "__main__":

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_field('name')
        validate = search_client(client_name)  #Using search method to validate if client exists in lists

        if validate:   
            print(f'\nIntroduce the new values for the client you want to update:')
            updated_client = _get_client_from_user()
            update_client(client_name, updated_client)
    elif command == 'D':
        client_name = _get_client_field('name')
        validate = delete_client(client_name) #This method deletes the client if exists in list, if not returns False to validate

        if validate == False: 
            print(f'Client {client_name} is not in clients list')
    elif command == 'S':
        client_name = _get_client_field('name')
        search_client(client_name)      
        
    else:
        print('Invalid command')