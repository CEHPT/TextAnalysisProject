from TextAnalysisProject import textanalysis
class TextAnalysisMenu:
    """Text analysis menu class."""

    def start(self):
        test = textanalysis.textanalysisclass()    # Create object.

        while True:
            print ("Text Analysis")
            print()
            print ("1. Predefined text")
            print ("2. Keyboard input")
            print ("3. File input")
            print ("4. Exit")
            print()
            opt = int(input("Enter your choice: (1-4) "))

            if opt == 1:
                test. SetDefaultText()
            elif opt == 2:
                test.SetUserInput()
            elif opt == 3:
                test.SetFileText()
            elif opt == 4:
                break
            else:
                print ("Invalid input. Try again.\n\n")
                continue

            test.TextAnalysis()
            test.ShowResults()

        del test


