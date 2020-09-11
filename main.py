#Liam Sullivan mls6888@psu.edu
# Section: 11r
# Breakout : 11
def getGradePoint(grade):
  if grade == "A": 
    return 4.0
  elif grade == "A-": 
    return 3.67 
  elif grade == "B+": 
    return 3.33
  elif grade == "B": 
    return 3.0 
  elif grade == "B-": 
    return 2.67
  elif grade == "C+":
    return 2.33 
  elif grade == "C": 
    return 2.0  
  elif grade == "D": 
    return 1.0  
  else:  
    return 0.0
   



def run():
  gradepoint1 = getGradePoint(input("Enter your course 1 letter grade: ")) 
  credit1 = input("Enter your course 1 credit: ")
  credit1 = int(credit1)
  print(f"Grade point for course 1 is:",gradepoint1)
  gradepoint2 = getGradePoint(input("Enter your course 2 letter grade: "))
  credit2 = input("Enter your course 2 credit: ")
  credit2 = int(credit2)
  print(f"Grade point for course 2 is:",gradepoint2)
  gradepoint3 = getGradePoint(input("Enter your course 3 letter grade: ")) 
  credit3 = input("Enter your course 3 credit: ")
  credit3 = int(credit3)
  print(f"Grade point for course 2 is:",gradepoint2)
  GPA = (gradepoint1*credit1+gradepoint2*credit2+gradepoint3*credit3)/(credit1+credit2+credit3)
  print("Your GPA is:",GPA)

  
  
  

    
if __name__ == "__main__":
   run()
