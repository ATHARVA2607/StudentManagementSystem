class ReadUtils:
    def ReadUserInputStr(self, userMsg, errmsg):
        self.stringData = input(userMsg)
        self.stringData = self.stringData.strip()
        if self.stringData=='':
            print(errmsg)
            self.ReadUserInputStr(userMsg, errmsg)
        return self.stringData

    def ReadUserInputInt(self, userMsg, errmsg):
        try:
            self.integerData=int(input(userMsg))
        except Exception as e:
            print("{}  : \n {}".format(errmsg,e))
            self.ReadUserInputInt(userMsg,errmsg)
        return self.integerData

