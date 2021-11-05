class Carscanner2XMLConverter:
    def __init__(self, input_string):
        self.str = input_string
        self.blocks = []
        self.result_str = ''

    def convert(self):
        k=0
        for i in range(int(len(self.str)/2)):
            try:
                block = f"0x{self.str[k]}{self.str[k+1]}"
                k += 2
                self.blocks.append(block)
            except IndexError as e:
                print(f"{e} at {k}")
        return tuple(self.blocks)

    def combine_output(self):
        for item in self.blocks:
            self.result_str+=f'{item},'
        self.result_str = self.result_str.rstrip(",",)
        return self.result_str

    def compare_lenght(self):
        input_str_len = len(self.str)
        blocks_item_count = len(self.blocks)
        if input_str_len/2 == blocks_item_count:
            return True
        else:
            return False

    def get_result(self):
        self.convert()
        self.combine_output()
        if self.compare_lenght():
            return self.result_str
        else:
            return -1
