import datetime
import psycopg2


class Controller:
    def __init__(self):
        super().__init__()
        self.connection = psycopg2.connect(user="postgres",
                                           password="FYNJY11",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="pract")

    def set_view(self, view):
        self.view = view

    def get_sotrudnik(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from СОТРУДНИКИ")
        sotrudnik_data = cursor.fetchall()
        cursor.close()
        return sotrudnik_data

    def del_sotrudnik(self, event):
        print('wow')
        cursor = self.connection.cursor()
        cursor.execute("delete from СОТРУДНИКИ where id = /*'%d'" % int(event.id))
        self.view.connect_table_sotrudnik()
        self.connection.commit()
        cursor.close()

    def add_sotrudnik(self, input_comp, input_name, input_tamozhna, status):
        if input_comp.text == '':
            status.text = 'Поле "Компьютер" не заполнено'
        elif input_name.text == "":
            status.text = 'Поле "Сотрудник" не заполнено'
        elif input_tamozhna.text == '':
            status.text = 'Поле "Таможня" не заполнено'
        else:
            status.text = 'Добавление выполнено'
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO СОТРУДНИКИ (ЛичныйНомер, Фамилия, Таможня) VALUES ('{}','{}', '{}')".format(
                    input_comp.text, input_name.text, input_tamozhna.text))
            self.view.connect_table_sotrudnik()
            self.connection.commit()
            cursor.close()

    def edit(self, input_comp, input_name, input_tamozhna, status, id):
        cursor = self.connection.cursor()
        if input_comp.text != '':
            cursor.execute(
                "UPDATE СОТРУДНИКИ SET ЛичныйНомер = '{}' WHERE id = '{}'".format(input_comp.text, id))
            self.view.show_data_product()
            self.connection.commit()
        if input_name.text != '':
            cursor.execute(
                "UPDATE СОТРУДНИКИ SET Фамилия = '{}' WHERE id = '{}'".format(input_name.text, id))
            self.view.show_data_product()
            self.connection.commit()
        if input_tamozhna.text != '':
            cursor.execute(
                "UPDATE СОТРУДНИКИ SET Таможня = '{}' WHERE id = '{}'".format(input_tamozhna.text, id))
            self.view.show_data_sotrudnik()
            self.connection.commit()
        status.text = 'Редактирование выполнено'
        cursor.close()

    def get_recipe(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from recipes")
        recipe_data = cursor.fetchall()
        cursor.close()
        return recipe_data

    def del_recipe(self, event):
        print('wow')
        cursor = self.connection.cursor()
        cursor.execute("delete from recipes where id = '%d'" % int(event.id))
        self.view.connect_table_recipe()
        self.connection.commit()
        cursor.close()

    def add_recipe(self, input_number, input_name, input_layout, input_author, status):
        if input_number.text == '':
            status.text = 'Поле "Номер" не заполнено'
        elif input_name.text == "":
            status.text = 'Поле "Название" не заполнено'
        elif input_layout.text == '':
            status.text = 'Поле "Раскладка" не заполнено'
        elif input_author.text == '':
            status.text = 'Поле "Автор" не заполнено'
        else:
            status.text = 'Добавление выполнено'
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO recipes (number_r, layout, name_r, author) VALUES ('{}','{}','{}','{}')".format(
                    input_number.text, input_layout.text, input_name.text, input_author.text))
            self.view.connect_table_recipe()
            self.connection.commit()
            cursor.close()

    def edit_recipe(self, input_number, input_name, input_layout, input_author, status, id):
        cursor = self.connection.cursor()
        if input_number.text != '':
            cursor.execute(
                "UPDATE recipes SET number_r = '{}' WHERE id = '{}'".format(input_number.text, id))
            self.view.connect_table_recipe()
            self.connection.commit()
        if input_layout.text != '':
            cursor.execute(
                "UPDATE recipes SET layout = '{}' WHERE id = '{}'".format(input_layout.text, id))
            self.view.connect_table_recipe()
            self.connection.commit()
        if input_name.text != '':
            cursor.execute(
                "UPDATE recipes SET name_r = '{}' WHERE id = '{}'".format(input_name.text, id))
            self.view.connect_table_recipe()
            self.connection.commit()
        if input_author.text != '':
            cursor.execute(
                "UPDATE recipes SET author = '{}' WHERE id = '{}'".format(input_author.text, id))
            self.view.connect_table_recipe()
            self.connection.commit()
        status.text = 'Редактирование выполнено'
        cursor.close()

    def get_provider(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from providers")
        provider_data = cursor.fetchall()
        cursor.close()
        return provider_data

    def del_provider(self, event):
        print('wow')
        cursor = self.connection.cursor()
        cursor.execute("delete from providers where id = '%d'" % int(event.id))
        self.view.connect_table_provider()
        self.connection.commit()
        cursor.close()

    def add_provider(self, input_code, input_name, input_adress, input_number, status):
        if input_code.text == '':
            status.text = 'Поле "Код" не заполнено'
        elif input_name.text == "":
            status.text = 'Поле "Название" не заполнено'
        elif input_adress.text == '':
            status.text = 'Поле "Адрес" не заполнено'
        elif input_number.text == '':
            status.text = 'Поле "Телефон" не заполнено'
        else:
            status.text = 'Добавление выполнено'
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO providers (code_p, name_p, adress, phone) VALUES ('{}','{}','{}','{}')".format(
                    input_code.text, input_name.text, input_adress.text, input_number.text))
            self.view.connect_table_provider()
            self.connection.commit()
            cursor.close()

    def edit_provider(self, input_code, input_name, input_adress, input_number, status, id):
        cursor = self.connection.cursor()
        if input_code.text != '':
            cursor.execute(
                "UPDATE providers SET code_p = '{}' WHERE id = '{}'".format(input_code.text, id))
            self.view.connect_table_provider()
            self.connection.commit()
        if input_name.text != '':
            cursor.execute(
                "UPDATE providers SET name_p = '{}' WHERE id = '{}'".format(input_name.text, id))
            self.view.connect_table_provider()
            self.connection.commit()
        if input_name.text != '':
            cursor.execute(
                "UPDATE providers SET adress = '{}' WHERE id = '{}'".format(input_adress.text, id))
            self.view.connect_table_provider()
            self.connection.commit()
        if input_number.text != '':
            cursor.execute(
                "UPDATE providers SET phone = '{}' WHERE id = '{}'".format(int(input_number.text), id))
            self.view.connect_table_provider()
            self.connection.commit()
        status.text = 'Редактирование выполнено'
        cursor.close()

    def get_price(self, provider, date1, date2):
        cursor = self.connection.cursor()
        cursor.execute(
            """SELECT date_, adress, phone, ingredient, price from deliveri_note
            INNER JOIN providers ON providers.name_p = deliveri_note.name_p
            WHERE providers.name_p = '{}' AND date_ BETWEEN '{}' AND '{}'""".format(provider.text, date1.text, date2.text))
        price_data = cursor.fetchall()
        cursor.close()
        return price_data

    def get_calories(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM calorific_value ORDER BY calorific_value"
        )
        price_data = cursor.fetchall()
        cursor.close()
        return price_data

    def get_prod_rec(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT DISTINCT name_p, recipe FROM products"
        )
        price_data = cursor.fetchall()
        cursor.close()
        return price_data