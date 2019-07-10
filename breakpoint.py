# -*- coding: utf-8 -*-

def breakpoint(bpname, args):
    print('>enter breakpoint ' + str(bpname))
    while True:
        try:
            input_exp = input('>>')
            if input_exp == 'break':
                print('>exit breakpoint ' + str(bpname))
                break
            eval_res = eval(input_exp)
            print(eval_res)
        except Exception as Arg:
            #print('not exp')
            try:
                exec(input_exp)
                
            except Exception as Arg_:
                print('>eval: ' + str(Arg) + '')
                print('>exec: ' + str(Arg_) + '')
            #print(str(Argment))
            
        
        
if __name__ == '__main__':
    a=1
    b='abc'
    breakpoint('1')
    c=8
    breakpoint('2')