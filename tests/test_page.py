from page import Widget


def test_input_nums(page):

    # ввод от 1 до 100 и проверка результата
    widget = Widget(page)
    widget.open_page()
    widget.input_min_nums('1')
    widget.input_max_nums('100')
    widget.click_generate()
    widget.check_result('100')

    # ввод от 1 до 1 и проверка результата
    widget.clear_field()
    widget.input_min_nums('1')
    widget.input_max_nums('1')
    widget.click_generate()
    widget.check_result('2')

    # ввод от 23 до 13 и проверка результата
    widget.clear_field()
    widget.input_min_nums('23')
    widget.input_max_nums('13')
    widget.click_generate()
    widget.check_result('24')

