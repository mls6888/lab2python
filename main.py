#Liam Sullivan mls6888@psu.edu
# Collaborator: Andrew Ou ajo5499@psu.edu
# Collaborator: Marvin Jakobs mjk5388@psu.edu
# Collaborator: Fletcher Henneman fdh5031@psu.edu 
# Collaborator: Brian Chetle bjc5969@psu.edu
# Section: 11r
# Breakout : 11
def getLetterGrade(grade):
  if grade >= 93.0: 
    return "A";
  elif grade >= 90.0: 
    return "A-" 
  elif grade >= 87.0: 
    return "B+"
  elif grade >= 83.0: 
    return "B" 
  elif grade >= 80.0: 
    return "B-"
  elif grade >= 77.0:
    return "C+" 
  elif grade >= 70.0: 
    return "C"  
  elif grade >= 60.0: 
    return "D"  
  else:  
    return "F"
   



def run():

  grade = float(input("Enter your CMPSC 131 grade: ")) 
  print(f"Your letter grade for CMPSC is {getLetterGrade(grade)}.")
    
if __name__ == "__main__":
   run()
