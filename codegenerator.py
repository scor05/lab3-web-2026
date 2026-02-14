""" 
Just made this file to automatically create all the index.html files in codes/
"""

with open("indexCodes.html", "r", encoding="utf-8") as file1, open("indexCodesFinal.html", "r", encoding="utf-8") as file2: 
    linesNormal = file1.read().splitlines()
    linesEnd = file2.read().splitlines()
    
    code_int = 0
    # indexes 16, and 36 for normal
    # indexes 16, 32 for final
    #"                    Currently entered the code: <strong></strong> into the safe. <br><br>"
    #"                    You tried the code: <strong></strong> with the safe. <br><br>"
    #"                        <li><a href='../../'>The Beginning</a></li>"
    
    for i in range(39):
        if ((code_int + 1) % 10 < 4):
            code_int += 1
            
        elif ((code_int + 1) % 100 < 34):
            code_int += 8 # +10 -2
            
        elif ((code_int + 100) % 1000 < 334):
            code_int += 78 # +100 -22

        digit3 = int(code_int % 1000 // 100)
        digit2 = int(code_int % 100 // 10)
        digit1 = int(code_int % 10)
        
        newLines = []
        back = "../"
        home_path = 0
        if (digit3 != 0):
            home_path += 1
        if (digit2 != 0):
            home_path += 1
        
        
        if (digit3 != 0):
            newLines = linesEnd.copy()
            newLines[16] = f"                    You tried the code: <strong>{digit3}{digit2}{digit1}</strong> with the safe. <br><br>"
            newLines[32] = f"                        <li><a href='../../{back*home_path}'>The Beginning</a></li>"
            if (digit3 != 0):
                newLines.insert(33, f"                        <li><a href='../../{digit2}'>{digit2}</a></li>")
            if (digit2 != 0):
                newLines.insert(33, f"                        <li><a href='../../{back}{digit3}'>{digit3}</a></li>")
        else:
            newLines = linesNormal.copy()
            newLines[16] = f"                    Currently entered the code: <strong>{digit3 if (digit3 != 0) else ''}{digit2 if (digit2 != 0) else ''}{digit1}</strong> into the safe. <br><br>"
            newLines[36] = f"                        <li><a href='../../{back*home_path}'>The Beginning</a></li>"
            if (digit2 != 0):
                newLines.insert(37, f"                        <li><a href='../../{digit2}'>{digit2}</a></li>")
                
        newOut = ""
        for l in newLines:
            newOut += (l + "\n")
            
        if (digit2 == 0 and digit3 == 0):
            with open(f"codes/{digit1}/index.html", "w", encoding="utf-8") as f:
                f.write(newOut)
                f.close()
        elif (digit2 != 0 and digit3 == 0):
            with open(f"codes/{digit2}/{digit1}/index.html", "w", encoding="utf-8") as f:
                f.write(newOut)
                f.close()
        else:
            with open(f"codes/{digit3}/{digit2}/{digit1}/index.html", "w", encoding="utf-8") as f:
                f.write(newOut)
                f.close()