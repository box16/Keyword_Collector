import MeCab
import re

class KeyWordCollector():

    def __init__(self):
        self.mecab_dictionary = MeCab.Tagger('-d /usr/lib/arm-linux-gnueabihf/mecab/dic/mecab-ipadic-neologd')

    def noun_collector(self,text):
        self.mecab_dictionary.parse("")
        text = self.text_cleaner(text)

        node = self.mecab_dictionary.parseToNode(text)
        
        result_nouns = []
        while node:
            if self.is_legal(node):
                legal_noun = self.make_link_scrapbox(node.surface)
                result_nouns.append(legal_noun)
            node = node.next

        result_nouns = list(set(result_nouns))#被りの削除
        result_text = ""

        for noun in result_nouns:
            result_text += noun
        return result_text
    
    def is_legal(self,node):
        is_noun = (node.feature.split(",")[0] == "名詞")
        is_pronoun = (node.feature.split(",")[1] == "代名詞")
        is_legal_word_length = (len(node.surface) >= 3)
        
        return is_noun and is_legal_word_length and not is_pronoun
    
    def make_link_scrapbox(self,text):
        text = re.sub('[\s]','_',text)
        text = "#" + text + " "
        return text

    def text_cleaner(self,text):
        text = re.sub(r'[!-~]', "", text)
        text = re.sub(r'[︰-＠]', "", text)
        text=re.sub('\n', " ", text)
        return text