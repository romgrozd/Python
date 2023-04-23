def add_contact(contact):
    #contact = [input("Введите имя: ")+" ", input("Введите фамилию: ")+" ", input("Введите отечество: ")+ " ", input("Введите номер телефона: ")]
    data = open('file.txt', 'a')
    data.writelines(contact)
    data.write('\n')
    data.close()

def search_contact():
    contact_list = open('file.txt', 'r')
    search = input("Введите фамилию для поиска: ")
    for i in contact_list:
         if search in i:
             print(i)
    contact_list.close()

def print_all():
    contact_list = open('file.txt', 'r')
    num = 1
    for i in contact_list:
            print(f'{num}. {i}')
            num +=1
    contact_list.close()            

      
        