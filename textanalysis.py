class textanalysisclass:

    def __init__(self):

        self.text=""
        self.result={}

        # Set Text automatically
    def SetDefaultText(self):
        self.text = """Lorem Ipsum is simply dummy text of the printing and 
                    typesetting industry. Lorem Ipsum has been the industry's 
                    standard dummy text ever since the 1500s, when an unknown 
                       printer took a galley of type and scrambled it to make a 
                    type specimen book. It has survived not only five centuries, 
                    but also the leap into electronic typesetting, 
                    remaining essentially unchanged. It was popularised in the 1960s 
                    with the release of Letraset sheets containing Lorem Ipsum 
                    passages, and more recently with desktop publishing software 
                    like Aldus PageMaker including versions of Lorem Ipsum."""

    # Set text from user input.
    def SetUserInput(self):
        inText = ""
        print("Enter text below (null Enter to finish input) : \n")

        while True:
            tmpText = input()
            if len(tmpText) == 0:
                break

            inText += tmpText

        self.text = inText

        # set text by File name.
    def SetFileText(self):
        fileName =input("Enter file name: ")
        with open(fileName, "r") as f:
            self.text = f.read()


    def DisplayText(self):
        print(self.text)

    def TextAnalysis(self):
        self.result.clear()

        temptext=self.text.lower()

        for c in temptext:
            if c.isalpha():
                if c in  self.result:
                    self.result[c]+=1
                else:
                    self.result[c]=1
        print(self.result)


    def ShowResults(self):

        for k,v in self.result.items():
            print("%s  %3d "%(k,v),"*"*v)
