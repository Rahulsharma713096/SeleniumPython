from OOPDemo import Addition


class childClassName(Addition):
    num2 = 20

    def getCompleteAddition(self):
        return self.num2 + self.first + self.second + Addition.answer
