documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
      
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def people_get():
  user_input = input( 'введите номер документа' )
  for document in documents:
    if "number" in document.keys() and user_input in document.values():
      print( document["name"] )
    else:
      None
  print('_________________________________' , '\n')    

def get_documents():
  for document in documents:
    print (*document.values())
  print('_________________________________' , '\n')
  
def shelf_get():
  user_input=input('введите номер документа')
  for key, val in directories.items():
    if user_input in val:
      print(key)
    else:
      None
  print('_________________________________' , '\n')    
      
  
def add_get():
  user_input_type = input('введите тип документа')
  user_input_number = input('введите номер документа')
  user_input_name = input('введите "имя, фамилия"')
  new_document = {"type": user_input_type , "number": user_input_number , "name":user_input_name}
  documents.append(new_document)
  print(documents)
  user_input_directory = input('введите номер полки, на которую убрать:')
  if user_input_directory in directories.keys():
    directories[user_input_directory].append(user_input_number)
    print (directories)
  print('_________________________________' , '\n')  
 
def main():
  while True:
    user_input=input('''Введите команду, которую хотите выполнить:
  p- поиск человека по номеру документа
  l- вывод на экран всех имеющихся документов
  s- поиск "полки"по номеру документа
  a- добавление нового документа
  Если желаете закончить работу работу с программой, введите q ''')
    if user_input=='q':
      break
    elif user_input=='p':
      people_get()
    elif user_input=='l':
      get_documents()
    elif user_input=='s':
      shelf_get()
    elif user_input=='a':
        add_get()
    

main()
  
