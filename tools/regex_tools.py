import re

class RegexTools:
    # phoneregex = re.compile(r'''
    # (\d{3}|\(\d{3}\))?              # area code
    # (\s|-|\.)?                       # separator
    # (\d{3})                          # first 3 digits
    # (\s|-|\.)                        # separator
    # (\d{4})                          # last 4 digits
    # (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    # ''', re.VERBOSE)

    '''
    1. 获取字符串里电话号码（）
    '''
    def get_phone_number(self, str=None):
        # regex = re.compile("\^[1][3,4,5,7,8][0-9]{9}$")
        regex = re.compile("\+?\d[\(-]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}")
        numbers = re.findall(regex, str)
        result = ''.join(numbers)
        return result


regex_tool = RegexTools()
if __name__ == '__main__':

    # regex_tool = RegexTools()
    # str = 'w22352352352523 ww 13817556839';
    # print(regex_tool.get_phone_number(str))
    # s
    str ='77438016868304121'
    print(len(str))
