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


@error_messages
def exist_message():
    return 'THIS ITEM ALREADY EXIST'


@error_messages
def not_exist_message():
    return 'THIS ITEM DOES NOT EXIST'

def show_help():
    print('=' * 50)
    print('enter "PRODUCTS" to show the available items in store with their prices')# noqa E501
    print('enter "HELP" to show you users guide')
    print('enter "SHOW" to show items in your list')
    print('enter "SEARCH" to search for a item in your shopping list')
    print('enter "DELETE" to remove a item from your list')
    print('enter "DONE" to stop adding items to your list')
    print('***you can use your discount code after you are done with your shopping***') # noqa E501
    print('what you need to get from store? add it to your list')
    print('=' * 50)

def user_bar_help():
    print('='*50)
    print("to see or edit your account's info enter 1: ")
    print("to get discount code add 2: ")
    print("to get into our online store enter 3: ")
    print("to quit the app enter 4: ")
    print('='*50)

def edit_info_help():
    print('='*50)
    print('to edit your username enter 1: ')
    print('to edit your password enter 2: ')
    print('to edit your address enter 3: ')
    print('to edit your phone number enter 4: ')
    print('to keep on with previous info or exit editing enter 5: ')
    print('='*50)

DISCOUNT_CODES = ["CHRISTMAS", 'MYBIRTHDAY', 'GOLDMEMBER', 'nodiscount' ]
enter_username="please enter your username: "
enter_password="please enter your password: "
enter_pass_confirm="please enter your password again to confirm: "
enter_full_name="please enter your full name: "
enter_phone="please enter your phone number: "
enter_address="please enter your address: "
enter_n_username="please enter your new username: "
enter_n_password="please enter your new password: "
enter_n_pass_confirm="please enter your new password again to confirm: "
enter_n_full_name="please enter your new full name: "
enter_n_phone="please enter your new phone number: "
enter_n_address="please enter your new address: "
confirm_failed="***the pass you add for confirmation did not matched***"
invalid_command="*****invalid command*****"
chose_command="please chose what you want to do: "
product_category="our products come in three categories, VEGETABLES, FRUITS, SUPERMARKET\nwhich category's products do you want to see?: "
item_search="what do you want to search through your list?: "
item_delete="what do you want to delete from your list?: "
add_item="please add the item you need: "