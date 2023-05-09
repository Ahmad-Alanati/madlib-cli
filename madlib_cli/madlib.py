import re

def welcome_message():
    welcomeing='''welcome to madlib game:

rules:
you will be giving a type of word and you have to enter the same type.
ex:Adjective->Dazzling
after you enter all the data needed we will print you a paragraph with your input.
'''
    print(welcomeing)

def game_commands():
    commands = '''//////////////////////////////////////////////////////////////////////////////////
to play the game press enter.
to quit write quit.
//////////////////////////////////////////////////////////////////////////////////'''
    print(commands)

def end_game():
    print("thank you for playing madlib")

def user_input(txt_tuple):
    user_list = [input("enter an {} : ".format(element)) for element in txt_tuple]
    return user_list

def read_template(path):
    try:
        with open(path,'r') as file:
            return file.read()
    except KeyError as err:
        return err

def parse_template(txt):
    txt_list =re.findall(r"\{\w+[ (\d\-\d|\w'\w*)]*\}",txt)
    print(txt_list)
    txt_tuples = tuple([x[1:len(x)-1] for x in txt_list])
    new_txt = txt
    for element in txt_tuples:
        new_txt = new_txt.replace(element,"")
    return new_txt,txt_tuples

def merge(txt,user_tuples):
    return txt.format(*user_tuples)

def main():
    welcome_message()
    file_data = read_template("assets/dark_and_stormy_night_template.txt")
    new_txt_str, txt_tuple = parse_template(file_data)
    game_commands()
    while input(">") != "quit":
        user_data = user_input(txt_tuple)
        new_sentence = merge(new_txt_str,user_data)
        print('''
your new sentences:
{}
'''.format(new_sentence))
        game_commands()
    end_game()

if __name__ == "__main__":
    main()