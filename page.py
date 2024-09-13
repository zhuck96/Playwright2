class Widget():

    def __init__(self, page):  # конструктор класса с параметром page который ожидает функцию page из conftest.py
        self.page = page

    def open_page(self):
        self.page.goto("https://www.random.org/widgets/integers/iframe")

    def input_min_nums(self,num):

        self.page.get_by_label('Min').click()
        self.page.get_by_label('Min').fill(num)

    def input_max_nums(self,num):
        self.page.get_by_label('Max').click()
        self.page.get_by_label('Max').fill(num)

    def click_generate(self):
        self.page.get_by_role('button', name='Generate').click()

    def clear_field(self):
        self.page.get_by_label('Min').click()
        self.page.get_by_label('Min').press('Control+A')
        self.page.get_by_label('Min').press('Backspace')
        self.page.get_by_label('Max').click()
        self.page.get_by_label('Max').press('Control+A')
        self.page.get_by_label('Max').press('Backspace')


    def check_result(self,max):
        x = self.page.locator("xpath=/html/body/div/span[5]/center/span[1]").text_content()
        x = int(x)

        i = 0
        nums_1 = []
        max = int(max)
        while i <= max:
            nums_1.append(i)
            i += 1

        if x in nums_1:
            print(f"Выведенное число {x} входит в диапазон")
        else:
            print(f"Число {x} не входит в диапазон")
