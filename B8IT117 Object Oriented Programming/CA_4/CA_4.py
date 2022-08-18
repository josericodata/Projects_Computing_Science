#CA 1
#Student Name: Jose Maria Rico Leal - 10539218
#Module Name: B8IT117 Object Oriented Programming
#Presentation Date: Tuesday 26th of October

#Importing the two classes we have created
import patient
import procedure

#Method to create the fill up the objects.
def createobjects():
    patient0 = patient.Patient('Jose Maria','Rico','Leal','Apt. 9 Adelaide Road Earl Court','Dublin','Ireland','D02 PV02','+353894520767','Ana Larino Pinazas','+34602219653')
                               
                            
    procedure1 = procedure.Procedure('Physical exam','15/09/2021','Dr. Jones','300€')
                                     
    procedure2 = procedure.Procedure('X-Ray', '15/09/2021','Dr. Ryan','600€')
                                     
    procedure3 = procedure.Procedure('Blood test', '15/09/2021','Dr. Smith', '100€')
                                     
    return(patient0,procedure1,procedure2,procedure3)

#Calling the main function
def main():
     pat,proc1,proc2,proc3 = createobjects()
     print(pat)
     print()
     print(proc1)
     print()
     print(proc2)
     print()
     print(proc3)

main()