import sys
clients = ['pablo', 'ricardo']


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)               
    elif client_name in clients:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        list_clients()    
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
        list_clients()
    else:
        print('Client is not in clients list')


def search_client(client_name):
    
    for client in clients:
        if client != client_name:
            continue
        elif client == client_name:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead clients list')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')  

        if client_name == 'exit':
            client_name = None
            break 

    if not client_name: 
        sys.exit()
                
    return client_name


if __name__ == "__main__":

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ') 
        update_client(client_name, updated_client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in client\'s list')
        else:
            print(f'The client {client_name} was not found')
    else:
        print('Invalid command')