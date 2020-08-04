# ----------------
#  This is a test file for checking all 
# the functions in all the moduiles under sirex

# ----------------


import sirex.file  as sf 
import sirex.numeric as nm
import sirex.string as st
import sirex.utils as ut


def main():
    # Utils package 
    #--------------------
    result1 = ut.file_to_str('fix.txt')
    print("Result_1 = {}".format(result1))


    # Numeric package 
    #--------------------
    
    result2 = nm.count_numbers("hello123")
    print("Result_2 = {}".format(result2))

    result2b = nm.count_numbers("hello123 342",blocks= True)
    print("Result_2b = {}".format(result2b))

    result2c = nm.biggest_number("hello123 34")
    print("Result_2c = {}".format(result2c))

    result2d = nm.smallest_number("hello123 34")
    print("Result_2c = {}".format(result2d))

    result2e = nm.replace_numbers("he23llo 123","*")
    print("Result_2e = {}".format(result2e))

    result2f = nm.is_number("23")
    print("Result_2f = {}".format(result2f))
   
    result2g = nm.remove_numbers("23 is my age")
    print("Result_2g = {}".format(result2g))
   
    result2h = nm.endswith_number("23 is my age")
    print("Result_2h = {}".format(result2h))

    result2i = nm.beginswith_number("23 is my age")
    print("Result_2i = {}".format(result2i))


    # String package 
    #--------------------

    result3a = st.count_occurance("this" , "this is This",True)
    print("result3a = {}".format(result3a))

    result3b = st.count_occurance("this" , "this is This")
    print("result3b = {}".format(result3b))

    # File package 
    #--------------------
    result5 = sf.word_count('fix.txt')  
    print("Result_5 = {}".format(result5))


if __name__ == '__main__':
    main()

