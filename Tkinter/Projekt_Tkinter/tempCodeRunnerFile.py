def setVerschaltung(self, Vv):
    #     #Hier sucht das Programm die verfügbaren Optionen für die Variable Vv in Abhängigkeit vom Motor_Name
    #     print("\n")
    #     vv_keys = ["Seriel", "2TM", "3TM", "4TM", "5TM", "6TM", "8TM", "10TM", "12TM"]
    #     vv_values = Daten[Motor_Name][vv_keys]
    #     vv_values = vv_values[vv_values!=''].astype(int)
    #     Vv = ""
    #     while True:
    #         try:
    #             print("Die für diesen Motor verfügbaren Teilmotoren sind:\n", vv_values )
    #             print("\n")
    #             Vv = int(input("Wählen Sie den Teilmotor: "))
    #             print("\n")
            
    #             if Vv not in vv_values.values:
    #                 print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
    #             else:
    #                 break
    #         except:
    #             print("Das war falsch!!")