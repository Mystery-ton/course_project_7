from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
# from kivymd.uix.picker import MDDatePicker
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton
from kivy.config import Config
from kivy.factory import Factory
#from kivymd.uix.picker import MDDatePicker
from kivy.uix.popup import Popup

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "700")

Window.clearcolor = (.80, .242, .126, 1)


class App(MDApp):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.controller.set_view(self)
        self.number_record_per_page = 5
        self.number_record = 0
        self.number_page = 1
        self.current_page = 1
        self.current_id = 0
        # self.search = Search()
        # self.search.setController(controller)
        self.buffer = None

    def exit(self):
        self.stop()

    def build(self):
        root = Builder.load_file('product.kv')
        return root

    def count_number_page(self):
        self.number_page = self.number_record // self.number_record_per_page
        if self.number_record % self.number_record_per_page > 0:
            self.number_page += 1

    def to_first_page(self, current_page):
        self.current_page = 1
        current_page.text = str(self.current_page)
        self.show_data()

    def to_last_page(self, current_page):
        dctnry = self.model.get_data()
        self.current_page = len(dctnry) // self.number_record_per_page + 1
        current_page.text = str(self.current_page)
        self.show_data()

    def to_x_page(self, current_page, sign):
        dctnry = self.model.get_data()
        if sign == '+':
            if (len(dctnry) // self.number_record_per_page) >= self.current_page:
                self.current_page += 1
                current_page.text = str(self.current_page)
        elif sign == '-':
            if self.current_page - 1 > 0:
                self.current_page -= 1
                current_page.text = str(self.current_page)
        self.show_data()

    def connect_table_sotrudnik(self):
        x = self.root.ids.sotrudnik_screen.ids.gl_2
        y = self.root.ids.sotrudnik_screen.ids.gl_3
        dctnry = self.controller.get_sotrudnik()
        self.clear_label()
        n = (self.current_page - 1) * self.number_record_per_page

        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))

            else:
                x.add_widget(
                    Label(text=str(dctnry[j + n][0]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 600 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 600 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][2], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 600 / self.number_record_per_page)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][3]), on_press=self.open_edit_product_popup, icon="auto-fix",
                                 icon_color=(.14, .26, 1, 1), halign='center',
                                 valign='center', size_hint=(1.5, 1.3)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][3]), on_press=self.controller.del_sotrudnik, icon="delete",
                                 icon_color=(.14, .26, .41, 1), halign='center', valign='center',
                                 size_hint=(1.5, 1.3)))

        self.root.ids.sotrudnik_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.sotrudnik_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def open_edit_product_popup(self, event):
        self.current_id = int(event.id)
        Factory.EditClientPopup().open(event.id)

    def clear_label(self):
        x = self.root.ids.sotrudnik_screen.ids.gl_2
        y = self.root.ids.sotrudnik_screen.ids.gl_3
        y.clear_widgets()
        x.clear_widgets()

    def to_x_record(self, num):
        self.clear_label()
        self.number_record_per_page = num
        self.count_number_page()
        self.connect_table_sotrudnik()

    def open_edit_recipe_popup(self, event):
        self.current_id = int(event.id)
        Factory.EditRecipePopup().open(event.id)

    def connect_table_recipe(self):
        x = self.root.ids.recipe_screen.ids.gl_recipe1
        y = self.root.ids.recipe_screen.ids.gl_recipe2
        dctnry = self.controller.get_recipe()
        self.clear_label_r()
        n = (self.current_page - 1) * self.number_record_per_page

        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))

            else:
                x.add_widget(
                    Label(text=str(dctnry[j + n][0]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][2], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][3], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][4]), on_press=self.open_edit_recipe_popup, icon="auto-fix",
                                 icon_color=(.14, .26, 1, 1), halign='center',
                                 valign='center', size_hint=(1.5, 2)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][4]), on_press=self.controller.del_recipe, icon="delete",
                                 icon_color=(.14, .26, .41, 1), halign='center', valign='center',
                                 size_hint=(1.5, 2)))

        self.root.ids.recipe_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.recipe_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def clear_label_r(self):
        x = self.root.ids.recipe_screen.ids.gl_recipe1
        y = self.root.ids.recipe_screen.ids.gl_recipe2
        y.clear_widgets()
        x.clear_widgets()

    def to_x_record_r(self, num):
        self.clear_label_r()
        self.number_record_per_page = num
        self.count_number_page()
        self.connect_table_recipe()

    def open_edit_provider_popup(self, event):
        self.current_id = int(event.id)
        Factory.EditProviderPopup().open(event.id)

    def connect_table_provider(self):
        x = self.root.ids.provider_screen.ids.gl_provider1
        y = self.root.ids.provider_screen.ids.gl_provider2
        dctnry = self.controller.get_provider()
        self.clear_label_p()
        n = (self.current_page - 1) * self.number_record_per_page
        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
                    y.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))

            else:
                x.add_widget(
                    Label(text=str(dctnry[j + n][0]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][2], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=str(dctnry[j + n][3]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][4]), on_press=self.open_edit_provider_popup, icon="auto-fix",
                                 icon_color=(.14, .26, 1, 1), halign='center',
                                 valign='center', size_hint=(1.5, 2)))
                y.add_widget(
                    MDIconButton(id=str(dctnry[j + n][4]), on_press=self.controller.del_provider, icon="delete",
                                 icon_color=(.14, .26, .41, 1), halign='center', valign='center',
                                 size_hint=(1.5, 2)))

        self.root.ids.provider_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.provider_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def clear_label_p(self):
        x = self.root.ids.provider_screen.ids.gl_provider1
        y = self.root.ids.provider_screen.ids.gl_provider2
        y.clear_widgets()
        x.clear_widgets()

    def to_x_record_p(self, num):
        self.clear_label_p()
        self.number_record_per_page = num
        self.count_number_page()
        self.connect_table_provider()

    def input_data_price(self):
        Factory.ChoosePricePopup().open()

    def connect_table_price(self, c_ed_price1, c_ed_price2, c_ed_price3):
        x = self.root.ids.price_screen.ids.gl_price1
        dctnry = self.controller.get_price(c_ed_price1, c_ed_price2, c_ed_price3)
        self.clear_label_pr()
        n = (self.current_page - 1) * self.number_record_per_page
        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            else:
                x.add_widget(
                    Label(text=str(dctnry[j + n][0]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=str(dctnry[j + n][2]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][3], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=str(dctnry[j + n][4]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
        self.root.ids.price_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.price_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def clear_label_pr(self):
        x = self.root.ids.price_screen.ids.gl_price1
        x.clear_widgets()

    def to_x_record_pr(self, num):
        self.clear_label_pr()
        self.number_record_per_page = num
        self.count_number_page()
        self.connect_table_price()

    def connect_table_calories(self):
        x = self.root.ids.calories_screen.ids.gl_cal1
        dctnry = self.controller.get_calories()
        self.clear_label_cal()
        n = (self.current_page - 1) * self.number_record_per_page
        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            else:
                x.add_widget(
                    Label(text=dctnry[j + n][0], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=str(dctnry[j + n][1]), color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
        self.root.ids.price_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.price_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def clear_label_cal(self):
        x = self.root.ids.calories_screen.ids.gl_cal1
        x.clear_widgets()

    def connect_table_prodrec(self):
        x = self.root.ids.prod_rec_screen.ids.gl_procrec1
        dctnry = self.controller.get_prod_rec()
        self.clear_label_rec()
        n = (self.current_page - 1) * self.number_record_per_page
        for j in range(self.number_record_per_page):
            if len(dctnry) <= j:
                for k in range(4):
                    x.add_widget(Label(text='', color=(0, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            elif n + j >= len(dctnry):
                for k in range(4):
                    x.add_widget(Label(text='', color=(1, .26, .41, 1), halign='center', valign='center',
                                       text_size=(150, 700 / self.number_record_per_page)))
            else:
                x.add_widget(
                    Label(text=dctnry[j + n][0], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
                x.add_widget(
                    Label(text=dctnry[j + n][1], color=(0, .26, .41, 1), halign='center', valign='center',
                          text_size=(150, 700 / self.number_record_per_page)))
        self.root.ids.prod_rec_screen.ids.number_record.text = "Кол-во записей: " + str(len(dctnry))
        self.number_record = len(dctnry)
        self.root.ids.price_screen.ids.last_page.text = str(
            len(dctnry) // self.number_record_per_page + 1)

    def clear_label_rec(self):
        x = self.root.ids.prod_rec_screen.ids.gl_procrec1
        x.clear_widgets()


    class Sotrudnik(Screen):
        pass

    class Recipe(Screen):
        pass

    class Provider(Screen):
        pass

    class Price(Screen):
        pass

    class Calories(Screen):
        pass

    class Prod_Rec(Screen):
        pass

    class MenuScreen(Screen):
        pass

    class WindowManager(ScreenManager):
        pass