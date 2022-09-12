class TextConverter():

    def opened(self,url):
        return open(url,'r')

    def text_splitter(self,url):
        input_content = self.opened(url)
        return input_content.read().split()

    def text_processor(self,url,start_with_letter):
        words_count = 0
        text = self.text_splitter(url)
        for i in text:
            if i.lower().startswith(start_with_letter):
                words_count += 1

        print(words_count)
















