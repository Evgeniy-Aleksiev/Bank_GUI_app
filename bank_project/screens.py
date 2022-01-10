import tkinter as tk

from authentication import *
from interest_calculator import *


def clear_window(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def get_username():
    with open(os.path.join('db', 'sessions.txt'), 'r') as file:
        user_line = json.load(file)
        return user_line['username']


def get_user_info(username):
    with open(os.path.join('db', 'bank_db.txt'), 'r') as file:
        for user_line in file:
            user = json.loads(user_line)
            if user.get('username') == username:
                result = f"Consumer credit: {user['credits']['consumer credit']} |" \
                          f" Housing loan: {user['credits']['housing loan']} |" \
                          f" Saving account: {user['credits']['saving account']}"
                return result


def render_main_enter_screen(window):
    clear_window(window)

    tk.Button(window,
              text='Login',
              fg="white",
              bg="blue",
              padx=45,
              font=('Helvetica', 10, 'bold'),
              command=lambda: render_login_screen(window)).grid(row=2, column=1)

    tk.Button(window,
              text='Forgot password?',
              fg='blue',
              bg='white',
              padx=8,
              font=('Helvetica', 10, 'bold'),
              command=lambda: render_password_change(window)).grid(row=3, column=1)

    tk.Button(window,
              text='Create new account',
              fg="white",
              bg="green",
              font=('Helvetica', 10, 'bold'),
              command=lambda: render_register_screen(window)).grid(row=4, column=1)


def render_register_screen(window):
    clear_window(window)

    tk.Label(window, text='Enter username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Enter password: ').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Label(window, text='Enter first name: ').grid(row=2, column=0)
    first_name = tk.Entry(window)
    first_name.grid(row=2, column=1)

    tk.Label(window, text='Enter last name: ').grid(row=3, column=0)
    last_name = tk.Entry(window)
    last_name.grid(row=3, column=1)

    def on_register():
        result = register(username.get(), password.get(), first_name.get(), last_name.get())
        if result is True:
            render_login_screen(window)
        else:
            tk.Label(window, text=result, fg='red').grid(row=4, column=1)

    tk.Button(window,
              text='Register',
              fg='white',
              bg='green',
              font=('Helvetica', 10, 'bold'),
              command=lambda: on_register()).grid(row=5, column=1)


def render_login_screen(window):
    clear_window(window)

    tk.Label(window, text='Username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Password: ').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    def log():
        result = login(username.get(), password.get())
        if result:
            main_page_screen(window)
        else:
            tk.Label(window,
                     text="The username and/or password you specified are not correct.",
                     fg='red').grid(row=2, column=1)

    tk.Button(window,
              text='Enter',
              fg='white',
              bg='blue',
              font=('Helvetica', 10, 'bold'),
              command=lambda: log()).grid(row=3, column=1)


def render_password_change(window):
    clear_window(window)

    tk.Label(window, text='Username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    def check_if_username_is_correct():
        result = forgotten_password(username.get())

        if result:
            change_password(window, username.get())
        else:
            tk.Label(window,
                     text='Invalid username.',
                     fg='red').grid(row=2, column=1)

    tk.Button(window,
              text='Enter',
              fg='white',
              bg='blue',
              font=('Helvetica', 10, 'bold'),
              command=lambda: check_if_username_is_correct()).grid(row=3, column=1)


def change_password(window, username):
    clear_window(window)

    tk.Label(window, text='Enter password: ').grid(row=1, column=0)
    password1 = tk.Entry(window, show='*')
    password1.grid(row=1, column=1)

    tk.Button(window,
              text='Enter',
              fg='white',
              bg='blue',
              padx=8,
              font=('Helvetica', 10, 'bold'),
              command=lambda: changing_password(username, password1.get())).grid(row=4, column=1)

    tk.Button(window,
              text='Login',
              fg='white',
              bg='green',
              padx=7,
              font=('Helvetica', 10, 'bold'),
              command=lambda: render_login_screen(window)).grid(row=5, column=1)


def main_page_screen(window):
    clear_window(window)

    tk.Label(window, text='Value: BGN\nAmount: up to 75 000\nTerm: up to 120 m\nInterest rate: 6.95%',
             fg='white',
             bg='blue',
             font=('Helvetica', 10, 'bold')).grid(row=0, column=0)

    tk.Label(window, text='Value: BGN\nAmount: up to 500 000\nTerm: up to 420 m\nInterest rate: 2.67%',
             fg='white',
             bg='red',
             font=('Helvetica', 10, 'bold')).grid(row=0, column=1)

    tk.Label(window, text='Value: BGN\nMinimum amount: 20\nAnnual interest rate: 0.15%\nAnnual interest: -',
             fg='white',
             bg='green',
             font=('Helvetica', 10, 'bold')).grid(row=0, column=2)

    tk.Label(window, text=f'Hi,\n@{get_username()}',
             fg='black',
             font=('Helvetica', 10, 'bold')).grid(row=0, column=4)

    tk.Button(window,
              text='Consumer credit',
              fg='white',
              bg='blue',
              font=('Helvetica', 10, 'bold'),
              command=lambda: consumer_page_screen(window)).grid(row=1, column=0)

    tk.Button(window,
              text='Housing loan',
              fg='white',
              bg='red',
              font=('Helvetica', 10, 'bold'),
              command=lambda: housing_loan_page(window)).grid(row=1, column=1)

    tk.Button(window,
              text='Saving account',
              fg='white',
              bg='green',
              font=('Helvetica', 10, 'bold'),
              command=lambda: saving_account_page(window)).grid(row=1, column=2)

    tk.Button(window,
              text='Cards',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: cards_page(window)).grid(row=1, column=3)

    tk.Button(window,
              text='Sign out',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: render_main_enter_screen(window)).grid(row=1, column=4)


def consumer_page_screen(window):
    clear_window(window)
    user = get_username()

    tk.Label(window, text='amount: ', font=('Helvetica', 10, 'bold')).grid(row=1, column=0)
    tk.Label(window, text='period: ', font=('Helvetica', 10, 'bold')).grid(row=2, column=0)

    amount = tk.Entry(window)
    amount.grid(row=1, column=1)
    period = tk.Entry(window)
    period.grid(row=2, column=1)

    def interest_calculator():
        consumer_credit = ConsumerCredit(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.interest(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    def get_credit():
        consumer_credit = ConsumerCredit(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.get_credit(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    tk.Button(window,
              text='Calculate: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=interest_calculator).grid(row=3, column=0)

    tk.Button(window,
              text='Get credit: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=get_credit).grid(row=4, column=0)

    tk.Button(window,
              text='Back',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: main_page_screen(window)).grid(row=5, column=0)


def housing_loan_page(window):
    clear_window(window)
    user = get_username()

    tk.Label(window, text='amount: ', font=('Helvetica', 10, 'bold')).grid(row=1, column=0)
    tk.Label(window, text='period: ', font=('Helvetica', 10, 'bold')).grid(row=2, column=0)

    amount = tk.Entry(window)
    amount.grid(row=1, column=1)
    period = tk.Entry(window)
    period.grid(row=2, column=1)

    def interest_calculator():
        consumer_credit = HousingLoanPage(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.interest(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    def get_credit():
        consumer_credit = HousingLoanPage(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.get_credit(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    tk.Button(window,
              text='Calculate: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=interest_calculator).grid(row=3, column=0)

    tk.Button(window,
              text='Get credit: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=get_credit).grid(row=4, column=0)

    tk.Button(window,
              text='Back',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: main_page_screen(window)).grid(row=5, column=0)


def saving_account_page(window):
    clear_window(window)
    user = get_username()

    tk.Label(window, text='amount: ', font=('Helvetica', 10, 'bold')).grid(row=1, column=0)
    tk.Label(window, text='period: ', font=('Helvetica', 10, 'bold')).grid(row=2, column=0)

    amount = tk.Entry(window)
    amount.grid(row=1, column=1)
    period = tk.Entry(window)
    period.grid(row=2, column=1)

    def interest_calculator():
        consumer_credit = SavingAccountPage(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.interest(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    def get_credit():
        consumer_credit = SavingAccountPage(user, int(amount.get()), int(period.get()))
        tk.Label(window, text=consumer_credit.get_credit(), font=('Helvetica', 10, 'bold')).grid(row=3, column=1)

    tk.Button(window,
              text='Calculate: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=interest_calculator).grid(row=3, column=0)

    tk.Button(window,
              text='Get credit: ',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=get_credit).grid(row=4, column=0)

    tk.Button(window,
              text='Back',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: main_page_screen(window)).grid(row=5, column=0)


def cards_page(window):
    clear_window(window)
    user_info = get_user_info(get_username())

    tk.Label(window, text="Value: BGN", font=('Helvetica', 10, 'bold')).grid(row=0, column=0)
    tk.Label(window, text=user_info, font=('Helvetica', 10, 'bold')).grid(row=0, column=1)

    tk.Button(window,
              text='Back',
              fg='black',
              bg='white',
              font=('Helvetica', 10, 'bold'),
              command=lambda: main_page_screen(window)).grid(row=5, column=0)