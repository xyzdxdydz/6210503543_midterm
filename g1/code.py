class AIChatBot():
    
    def showSubjectName(self):
        print("AI for robot system")

    def showStudentYear(self, std_id):
        year = std_id[0:2]
        return 66 - int(year) 
    
    def calculator(self, ops, x, y):
        x = float(x)
        y = float(y)
        return x + y if ops == "+" else x - y
    
    def main(self):
        while True:
            cmd = input()
            if cmd == "subject":
                self.showSubjectName()
                
            elif cmd == "year":
                year_std = self.showStudentYear(input())
                print(year_std)
                
            elif cmd == "calc":
                ops = input()
                x = input()
                y = input()
                
                res = self.calculator(ops, x, y)
                print(res) 
                
obj = AIChatBot()
obj.main()