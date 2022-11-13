
class name_formatting():
    
    
    def package_name(self, *args):
        tmp = ''
        for _ in args:
            tmp += _[0:3].lower()
            
        print(f'your package name: {tmp}')
        return tmp
        
        
    def module_name(self, *args):
        tmp = ''
        data_element = len(args)
        i = 1
        for _ in args:
            if (i == data_element):
                tmp += _.lower()
            else:
                tmp += _.lower()
                tmp += '_'
            i += 1
        
        print(f'your module name: {tmp}')
        return tmp
        

    def class_name(self, *args):
        tmp = ''
        data_element = len(args)
        i = 1
        for _ in args:
            if (i == 1):
                tmp += _.capitalize()
            elif(i == data_element):
                tmp += _.lower()
            else:
                tmp += _.lower()
                tmp += '_'
            i += 1
        
        print(f'your class name: {tmp}')
        return tmp


    def method_name(self, *args):
        tmp = ''
        data_element = len(args)
        i = 1
        for _ in args:
            if(i == data_element):
                tmp += _.lower()
            else:
                tmp += _.lower()
                tmp += '_'
            i += 1
        
        print(f'your method name: {tmp}')
        return tmp

        
    def function_name(self, *args):
        tmp = ''
        data_element = len(args)
        i = 1
        for _ in args:
            if(i == data_element):
                tmp += _.lower()
            else:
                tmp += _.lower()
                tmp += '_'
            i += 1
        
        print(f'your function name: {tmp}')
        return tmp
        
        
    def variable_name(self, *args):
        tmp = ''
        data_element = len(args)
        i = 1
        for _ in args:
            if(i == data_element):
                tmp += _.lower()
            else:
                tmp += _.lower()
                tmp += '_'
            i += 1
        
        print(f'your variable name: {tmp}')
        return tmp
        
        
    def constant_name(self, *args):
        tmp = ''
        for _ in args:
            tmp += _.upper()
            
        print(f'your constant name: {tmp}')
        return tmp
        
        
if __name__ == '__main__':
    tmp = name_formatting()
    tmp.package_name('dAta', 'iNclude')
    tmp.module_name('dAta', 'iNclude')
    tmp.class_name('dAta', 'iNclude')
    tmp.method_name('dAta', 'iNclude')
    tmp.function_name('dAta', 'iNclude')
    tmp.variable_name('dAta', 'iNclude')
    tmp.constant_name('dAta', 'iNclude')
    
    tmp.method_name('sony', 'accumulation')
    tmp.method_name('Risona', 'Fluctuation')