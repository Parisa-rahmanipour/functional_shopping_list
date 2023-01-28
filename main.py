import os
import json
import random
import logging
import logging.config
from helper import msg
from datetime import datetime
from helper.msg import DISCOUNT_CODES
from typing import (List,
                    Tuple,
                    Dict)


logging.config.fileConfig(fname='log/handler.toml', disable_existing_loggers=False) # noqa E501
logger = logging.getLogger("log/authLogger")


shopping_list: List['str'] = list()
date = datetime.now()


def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")


def write_users_info(info_file: __file__, username: str, name: str, password: str, address: str, phone: str): # noqa E501
    """
    this func get users info as arg and write the infos
    as nested dict in json file
    Parameters
    ----------
    info_file:__file__ :
        json file contain users info
    username: str :
        username
    name: str :
        full name
    password: str :
        user's pass
    address: str :
        user's address
    phone: str :
        user's phone number
    Returns
    -------
    """
    with open(info_file, 'r') as users_info:
        data = json.load(users_info)
        info_dict = {
            'username': f'{username}',
            'full_name': f'{name}',
            'password': f'{password}',
            'address': f'{address}',
            'phone_number': f'{phone}'}
        data[f'{username}'] = info_dict
        info = json.dumps(data,  indent=4)
        with open(info_file, 'w') as new_user_info:
            new_user_info.write(info)


def check_user_password(info_file: __file__, username: str, password: str) -> bool: # noqa E501
    """
    this func check's user's username and password by reading it from json file
    Parameters
    ----------
    info_file:__file__ :
        json file containing user's info
    username: str :
        username
    password: str :
        password
    Returns
    -------
    return's true or false to show if user could log in or not
    """
    logged_in = False
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        try:
            assert username in info_dict.keys()

        except AssertionError:
            print('this username does not exist')
            logger.error('user tried entering invalid username')
        else:
            if password != info_dict[username]["password"]:
                print('wrong password!')
                logger.error(f'{username} entered wrong password')
            else:
                logged_in = True
    return logged_in


def read_users_info(info_file: __file__, username: str):
    """
    this func reads user's info and show them
    Parameters
    ----------
    info_file:__file__ :
        json file containing user's info
    username: str :
        username
    Returns
    -------
    """
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        if username in info_dict.keys():
            print(f'username: {info_dict[username]["username"]}')
            print(f'full name: {info_dict[username]["full_name"]}')
            print(f'address: {info_dict[username]["address"]}')
            print(f'phone number: {info_dict[username]["phone_number"]}')


def get_users_info(info_file: __file__, username: str) -> Tuple:
    """
    this func reads user's info and return them in tuple
    Parameters
    ----------
    info_file:__file__ :
        json file containing user's info
    username:str :
        username
    Returns
    -------
    user's info: username, name, phone, address and pass
    """
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        if username in info_dict.keys():
            full_name = info_dict[username]["full_name"]
            address = info_dict[username]["address"]
            phone_number = info_dict[username]["phone_number"]
            password = info_dict[username]["password"]
    return username, password, full_name, address, phone_number


def edit_user_info(info_file: __file__, username: str, name: str, password: str, address: str, phone: str): # noqa E501
    """
    this func read's user's info, delete the dicts
    and replace new dict by new info
    Parameters
    ----------
    info_file:__file__ :
        json file containing user's info
    username: str :
        username
    name: str :
        user's full name
    password:str :
        user's pass
    address:str :
        user's address
    phone:str :
        user's phone number
    Returns
    -------
    """
    with open(info_file, 'r+') as users_info:
        data = json.load(users_info)
        del data[username]
        info_dict = {
            'username': f'{username}',
            'full_name': f'{name}',
            'password': f'{password}',
            'address': f'{address}',
            'phone_number': f'{phone}'}
        data[f'{username}'] = info_dict
        info = json.dumps(data,  indent=4)
        with open(info_file, 'w') as new_user_info:
            new_user_info.write(info)


def error_messages(func):
    """its a decorator which add stars to message
    to bold messages
    Parameters
    ----------
    func :
        func which returns messages
    Returns
    -------
    add_star func which add starts up and down line of func message
    """
    def add_star():
        """ """
        print('*' * 50)
        print(f'***{func()}****')
        print('*' * 50)
    return add_star


def add_items(shopping_list: List['str'], item: str) -> List:
    """this function add new items to our list
    Parameters
    ----------
    shopping_list : List['str'] :
        shopping list
    item : str :
        new item we want to add to shopping list
    Returns
    -------
    shopping lia with new items
    """
    shopping_list.append(item)


def get_categories(info_file: __file__, category: str):
    """
    this func reads json file containing products info
    and check product's category
    which are dict's key
    Parameters
    ----------
    info_file:__file__ :
        json file containing product's info
    category:str :
        key of nested dict in json file
    Returns
    -------
    """
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        if category in info_dict.keys():
            for key, value in info_dict[category].items():
                print('{}  :  {}$'.format(key, value))


def check_available_products(info_file: __file__) -> List:
    """
    this func check if a product is available in our store
    by checking key inner nested dict written in json file
    Parameters
    ----------
    info_file:__file__ :
        json file containing products info
    Returns
    -------
    """
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        products = list()
        for key, value in info_dict['VEGETABLES'].items():
            products.append(key)
        for key, value in info_dict['FRUITS'].items():
            products.append(key)
        for key, value in info_dict['SUPERMARKET'].items():
            products.append(key)
    return products


def get_products_dict(info_file: __file__) -> Dict:
    """
    this func unpack all dicts about products info from json file into one
    Parameters
    ----------
    info_file:__file__ :
        json file containing products info
    Returns
    -------
    """
    with open(info_file, 'r+') as file:
        info_dict = json.load(file)
        products_info = {**info_dict['VEGETABLES'], **info_dict['FRUITS'], **info_dict['SUPERMARKET']} # noqa E501
    return products_info


def delete_item(shopping_list: List['str'], item: str) -> str:
    """this func let user to delete an item which exist in our list or
    return not exist message if the item does not exist in our list
    Parameters
    ----------
    shopping_list : List['str'] :
        shopping list
    item : str :
        the item we want to delete from our shopping list
    Returns
    -------
    """
    if item in shopping_list:
        shopping_list.remove(item)
        print('{} have been removed from your list'.format(item))
    else:
        print('{} does not exist in your list'.format(item))


def shopping_list_search(shopping_list: List['str'], item: str) -> str:
    """this function let users to search if a item exist in our list or not

    Parameters
    ----------
    shopping_list :
        shopping list
    item :
        item we want to search for in shopping list
    Returns
    -------
    """
    if item in shopping_list:
        msg.exist_message()
    else:
        msg.not_exist_message()


def show_list(shopping_list: List['str'], item: str) -> str:
    """this func shows the list and the items in it
    Parameters
    ----------
    shopping_list :
        shopping list
    item :
        items inside the shopping list
    Returns
    -------
    """
    print('this is your shopping list:')
    for item in shopping_list:
        print("{}".format(item))


def get_discount_code(discount_codes: List) -> str:
    """this func randomly choose a discount code
    from available codes(different codes, have different weights)
    """
    code: List = random.choices(discount_codes, weights=[1, 2, 3, 4])
    if code[0] == 'CHRISTMAS':
        print(f'you can get 50% off by entering code {code[0]}')
    elif code[0] == 'MYBIRTHDAY':
        print(f'you can get 30% off by entering code {code[0]}')
    elif code[0] == 'GOLDMEMBER':
        print(f'you can get 10% off by entering code {code[0]}')
    else:
        print("your bad! you didn't get any discount code this time")


clear_screen()
while True:
    registration_mode = input('have you registered in our site?:[YES/NO] ').upper() # noqa E501
    clear_screen()
    match registration_mode:
        case "NO":
            print('please fill in your information to create an account')
            username = input(msg.enter_username)
            full_name = input(msg.enter_full_name)
            address = input(msg.enter_address)
            while True:
                password = input(msg.enter_password)
                password_confirm = input(msg.enter_pass_confirm)
                if password == password_confirm:
                    break
                else:
                    print(msg.confirm_failed)
                    continue
            phone_number = input(msg.enter_phone)
            write_users_info('user_info.json', username, full_name, password, address, phone_number) # noqa E501
            logger.info(f'{username} registered')
            break
        case "YES":
            username = input(msg.enter_username)
            password = input(msg.enter_password)
            logged_in = check_user_password('user_info.json', username, password) # noqa E501
            if logged_in is True:
                logger.info(f'{username} logged in')
                break
        case _:
            print(msg.invalid_command)
            continue

clear_screen()
while True:
    msg.user_bar_help()
    user_command = input(msg.chose_command)
    match user_command:
        case "1":
            read_users_info("user_info.json", username)
            to_edit_info = input('if you want to edit info press 1: ')
            if to_edit_info == '1':
                while True:
                    clear_screen()
                    msg.edit_info_help()
                    info_edit_type = input(msg.chose_command)
                    match info_edit_type:
                        case "1":
                            new_username = input(msg.enter_n_username)
                            username, password, full_name, address, phone_number = get_users_info('user_info.json', username) # noqa E501
                            username = new_username
                        case "2":
                            while True:
                                new_password = input(msg.enter_n_password)
                                new_password_confirm = input(msg.enter_n_pass_confirm) # noqa E501
                                if new_password == new_password_confirm:
                                    username, password, full_name, address, phone_number = get_users_info('user_info.json', username) # noqa E501
                                    password = new_password
                                    break
                                else:
                                    continue
                        case "3":
                            new_address = input(msg.enter_n_address)
                            username, password, full_name, address, phone_number = get_users_info('user_info.json', username) # noqa E501
                            address = new_address
                        case "4":
                            new_phone_number = input(msg.enter_n_phone)
                            username, password, full_name, address, phone_number = get_users_info('user_info.json', username) # noqa E501
                            phone_number = new_phone_number
                        case "5":
                            break
                        case _:
                            clear_screen()
                            print(msg.invalid_command)
                            msg.edit_info_help()
                    edit_user_info("user_info.json", username, full_name, password, address, phone_number) # noqa E501
            else:
                continue
        case "2":
            get_discount_code(DISCOUNT_CODES)
        case "3":
            break
        case "4":
            os._exit()
        case _:
            clear_screen()
            print(msg.invalid_command)
            msg.user_bar_help()
            continue

clear_screen()
msg.show_help()
while True:
    new_item = input(msg.add_item).upper().strip()
    clear_screen()
    if new_item in shopping_list:
        print(msg.exist_message())
    else:
        match new_item:
            case "SEARCH":
                to_search_item = input(msg.item_search).upper()
                shopping_list_search(shopping_list, to_search_item)
            case "DELETE":
                to_delete_item = input(msg.item_delete).upper()
                delete_item(shopping_list, to_delete_item)
            case "SHOW":
                show_list(shopping_list, new_item)
            case "DONE":
                break
            case "HELP":
                msg.show_help()
            case "PRODUCTS":
                category = input(msg.product_category).upper()
                get_categories('shopping_list_data.json', category)
            case _:
                available_products = check_available_products('shopping_list_data.json') # noqa E501
                if new_item in available_products:
                    add_items(shopping_list, new_item)
                else:
                    print(msg.not_exist_message())

costs = list()
for length in range(len(shopping_list)):
    quantity = int(input(f'how many boxes of {shopping_list[length]} you want?: ')) # noqa E501
    clear_screen()
    available_products_dict = get_products_dict('shopping_list_data.json')
    value_of_item = int(available_products_dict[shopping_list[length]])
    item_cost = (quantity)*(value_of_item)
    costs.append(item_cost)


for item_cost in costs:
    total: int = sum(costs)

discount_code:str = input("enter your discount code or if you don't have any code press enter: ").upper() # noqa E501
clear_screen()
# use these discount code for different percentage of discount
# christmas: 50% off
# mybirthday 30% off
# goldmember 10% off
if discount_code in DISCOUNT_CODES:
    match discount_code:
        case "CHRISTMAS":
            discounted_total_price = (total*50)/100
        case "MYBIRTHDAY":
            discounted_total_price = (total*70)/100
        case "GOLDMEMBER":
            discounted_total_price = (total*90)/100
else:
    discounted_total_price = "***THERE IS NO DISCOUNT FOR THIS SHOPPING***"

clear_screen()
while True:
    print('\nwill you pick up your shopping or do you need delivery?')
    delivery: str = input('enter 1 for pick up and enter 2 for delivery: \n')
    clear_screen()
    delivery_codes: list = ['1', '2']
    if delivery not in delivery_codes:
        print(msg.invalid_command)
        continue
    else:
        break

clear_screen()
print('*****we wish you are satisfied with your shopping*****')
print('=' * 50)
print('\tItem Name\tItem Price')

for k in range(len(shopping_list)):
    item_name = shopping_list[k]
    item_price = available_products_dict.get(shopping_list[k])
    print('\t{}\t\t${}'.format(item_name.title(), item_price))

print('=' * 50)
print('\t\t\tTotal')
print('\t\t\t${}'.format(total))
print('=' * 50)
print('\t\t\ttotal cost after discount')
print('\t\t\t${}'.format(discounted_total_price))

print('=' * 50)
print(f'you are done with your shopping at{date} and ')
if delivery == '1':
    print('you can pick up your shopping in 10 minutes')
if delivery == '2':
    print('we will deliver this shopping for following info')
    read_users_info('user_info.json', username)
