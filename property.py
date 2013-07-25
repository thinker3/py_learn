class String2Int(object):
    def __init__(self, str_num):
        self.str_num = str_num

    def get_num(self):
        return int(self.str_num)

    def set_num(self, value):
        self.str_num = str(value)

    def show_int(self):
        print self.num, type(self.num)

    def show_str(self):
        print self.str_num, type(self.str_num)

    num = property(get_num, set_num)


n = String2Int('123')
n.show_int()
n.show_str()
n.num = 321
n.show_int()
n.show_str()

