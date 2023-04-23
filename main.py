import interface,func


def main_prog():
    flag = True
    while flag:
        a = interface.hello()
        if a == '1':
            func.add_contact(interface.get_contact())
        elif a == '2':  
            func.search_contact()
        elif a == '3':
            func.print_all()
        else:
            flag = False       

main_prog()    