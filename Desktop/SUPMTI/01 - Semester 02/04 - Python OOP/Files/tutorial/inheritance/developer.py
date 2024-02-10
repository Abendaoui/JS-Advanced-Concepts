from employee import Employee


class Developer(Employee):
    def __init__(self,id,first,last,age,salary,languages=None):
        super().__init__(id,first,last,age,salary)
        if languages is None:
            self.languages = []
        else:
            self.languages = languages

    def get_languages(self):
        if self.languages is None or len(self.languages) == 0:
            print('Developer {} Has No Languages'.format(self.full_name()))
        else:
            for lang in self.languages:
                print('Language : {}'.format(lang))
                
                
    def add_language(self, new_lang):
        if new_lang in self.languages:
            print('This {} language already exists'.format(new_lang))
        else:
            self.languages.append(new_lang)
            print('Deleted Successfully')
            
    def delete_language(self, lang):
        if lang not in self.languages:
            print('This Language {} does not exist'.format(lang))
        else:
            self.languages.remove(lang)
            print('Deleted Successfully')            



# print(isinstance(dev_01, Developer))
# print(issubclass(Developer,Employee))
