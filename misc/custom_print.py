class CustomPrint(object):
    the_whole_string = ''

    def reset(self):
        self.the_whole_string = ''

    def print(self, a_str):
        self.the_whole_string += a_str + '<br>\n'

    def dump(self):
        print("THE CONTENT IS: {}".format(self.the_whole_string))
        the_dump = self.the_whole_string
        self.reset()
        return the_dump


custom_print = CustomPrint()
