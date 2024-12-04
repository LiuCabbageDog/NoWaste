'''
This is the main file of all the Application.

1. Use this file to manage the CRUD of inventory.
2. Use Matplotlib to create chart and diagram, reflecting the fluctuation of inventory.
3. Use tkinter to show front UI.
4. Use csv file "database" to store data.
5. Update item is actually delete and add a new one.
'''

import csv # library for managing csv file
from datetime import date # library for inducting 'date' data type.

def main():
        add_item()
        add_item()

        ShowAsString()

        delete_id = input('please input id of the item you want to delete: ')
        delete_item(delete_id)

        ShowAsString()



'''
# 提示用户输入日期
user_input = input("请输入一个日期(格式:YYYY-MM-DD):")

try:
    # 解析用户输入的日期字符串为 datetime.date 对象
    date_object = datetime.strptime(user_input, "%Y-%m-%d").date()
    print(f"您输入的日期是：{date_object}")
except ValueError:
    # 捕获输入格式错误
    print("输入的日期格式不正确，请使用 YYYY-MM-DD 格式。")
'''


# Add new items into inventroy.
'''
status = ['Normal','Expiring soon', 'Expired', 'Used']
'''
def add_item():
        new_item = []
        # input fields of a new item into a list.
        user_input = input("Please input item name, item id, category, quantity, unit of quantity, purchase date,"
                        "shelf life, expired date, status, total price, where you buy.\nEvery data is separated by comma.\n")
        new_item = user_input.split(',')

        # input error handling.
        while(len(new_item) != 11): # Use a constant here, can be optimized in the future.
                print("Input wrong number of fields!\n")
                user_input = input("Please input item name, item id, category, quantity, unit of quantity, purchase date,"
                           "shelf life, expired date, status, total price, where you buy.\nEvery data is separated by comma.\n")
                new_item = user_input.split(',')

        # put the new item list into databse.
        fields = [new_item]
        with open('database.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(fields)

        '''
        Input data separately as below:

        Name = input("Please input item name")
        new_item.append(Name)

        Category = input("Please input item category")
        new_item.append(Category)

        Quantity = input("Please input item quantity")
        new_item.append(Quantity)

        Quantity_Unit = input("Please input unit of quantity")
        new_item.append(Quantity_Unit)

        Date_Purchase = input("Please input item purchase date")
        new_item.append(Date_Purchase)

        Shelf_Life = input("Please input item shelf life")
        new_item.append(Shelf_Life)

        # In future iteration, Expired Date can be calcualted based on its shelf life.
        Date_Expired = input("Please input item expired date")
        new_item.append(Date_Expired)

        # In future iteration, status can be estimated based on expired date.
        Status = input("Please input item status")
        new_item.append(Status)

        Total_Price = input("Please input item total price")
        new_item.append(Total_Price)

        Store = input("Please input where you buy this item")
        new_item.append(Store)
        '''

# delete specified row with id.
def delete_item(id):
        # Write a new table except which we want to delete. Here is an empty list waits for qualified data.
        new_table = []
        fieldnames = None

        # Search specified rows, construct new table without them.
        with open('database.csv', 'r') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames # To get fieldnames. Without this line, field name will lose.
                for row in reader:
                        if (row['ID'] != id):
                                new_table.append(row)

        # Overwrite original file.
        with open('database.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_table)

# print current form as dictionary
def ShowAsDict():
        with open('database.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                        print(row)

# print current form as string
def ShowAsString():
        with open('database.csv', 'r') as file:
                reader = csv.reader(file);
                for row in reader:
                                print(row)



main()