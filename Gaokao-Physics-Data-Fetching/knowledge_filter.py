import re

def knowledge_filter(all_text):
    filter_=['\u4e00-\u9fa5','，','。','：','“','”','（','）','[A-Z]','[a-z]']
    char_set=re.sub("[^"+"|".join(filter_)+"]","",all_text)
    return char_set

if __name__=='__main__':
    all_text='是，ΑB'
    print(knowledge_filter(all_text))