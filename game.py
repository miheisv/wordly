class Game:
    def __init__(self, chat_id, stage, word):
        self.chat_id = chat_id
        self.stage = stage
        self.word = word

    def get_answer(self, text):
        text = text.lower()
        answer = ''
        mask = list(self.word)
        if len(self.word) != len(text):
            return self.answer
        for i in range(len(text)):
            if text[i] == self.word[i]:
                letter = text[i].upper()
                answer += f'__{letter}__'
                mask.remove(text[i])
                print(answer)
            elif text[i] in mask:
                letter = text[i].upper()
                answer += letter
                mask.remove(text[i])
            else:
                letter = text[i].lower()
                answer += letter
        return answer
