import datetime
from enum import Enum

account = [['Credit', 'Debit', 'Balance']]


def get_current_date():
    # getting the current date and time
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%m/%d/%Y")


def transaction():
    now = datetime.datetime.now()
    dayMonthYear = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if creditQ == 'y':
            validInput = True
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, credit, 0, round(credit + float(lastRow[3]), 2)]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account) - 1][3])
            else:
                newRow = [dayMonthYear, credit, 0, credit]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account) - 1][3])
        elif creditQ == 'n':
            validInput = True

        else:
            print('Please enter a valid input.')

    validInput = False
    while validInput == False:
        debitQ = input('Do you want to debit your account in this transaction? Y/N').lower()
        if debitQ == 'y':
            validInput = True
            debit = float(input('How much do you want to debit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, 0, debit, round(float(lastRow[3]) - debit, 2)]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account) - 1][3])
            else:
                newRow = [dayMonthYear, 0, debit, -debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account) - 1][3])
        elif debitQ == 'n':
            validInput = True
        else:
            print('Please enter a valid input.')


def transaction2():
    current_datetime = datetime.now()
    transaction_types = ["C", "D", "Q"]
    transaction_type = None
    while transaction_type not in transaction_types:
        input_type = input("Enter C=Credit, D=Debit, Q=quit :")
        if len(input_type) > 0:
            transaction_type = input_type.upper()[0]
        else:
            transaction_type = None
    print(f"transaction type = {transaction_type}")
    if transaction_type == 'Q':
        return

    amount = 0.0
    while amount == 0:
        input_type = input("Enter an amount  :")
        try:
            amount = float(input_type)
        except:
            amount = 0.0
    print(f"amount = {amount}")

    cr_amount = amount if transaction_type == 'C' else 0.0
    db_amount = amount if transaction_type == 'D' else 0.0
    row = [current_datetime.strftime("%m/%d/%Y"), cr_amount, db_amount, 0.0]
    print(row)


def insert_row(credit, debit, balance):
    now = datetime.datetime.now()
    dayMonthYear = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
    newRow = [dayMonthYear, credit, debit, balance]
    account.append(newRow)


if __name__ == '__main__':

    insert_row(450.0, 0, 450.0)
    insert_row(0, 30.0, 420.0)
    insert_row(1000.0, 0, 1420.0)
    insert_row(4400.0, 0, 5820.0)
    insert_row(0, 776.0, 5044.0)
    insert_row(2333.33, 0, 7377.33)
    insert_row(2000.0, 0, 9377.33)
    insert_row(0, 1444.33, 7933.0)
    for i in account:
        print(i)

    while True:
        transaction()
