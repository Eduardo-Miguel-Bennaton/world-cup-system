import tkinter as tk
import tkinter.ttk as tkk

Root = tk.Tk()
Root.title("World-Cup-System")

#CREATING DEFAULT-ATTRIBUTES TO OUR STANDARDS
class Default_Attributes():
    def __init__(self,Color_1 = "#D1D1D1",Color_2 = "#FFFFFF",Color_3 = "#5C5C5C",Color_4 = "#FF0000",Color_5 = "#000000",Color_6 = "#f0f0f0",Size_1 = 12,Size_2 = 15,Size_3 = 30,Size_4 = 10,Size_5 = 8,Font_1 = "Segoe UI Semibold",Font_2 = "Segoe UI Light",Font_3 = "Segoe UI Light Italic",Font_4 = "Calibri",Font_5 = "Cascadia Code SemiBold"):
        #SETTINGS COLORS
        self.Color_1 = Color_1
        self.Color_2 = Color_2
        self.Color_3 = Color_3
        self.Color_4 = Color_4
        self.Color_5 = Color_5
        self.Color_6 = Color_6
        #SETTINGS SIZES
        self.Size_1 = Size_1
        self.Size_2 = Size_2
        self.Size_3 = Size_3
        self.Size_4 = Size_4
        self.Size_5 = Size_5
        #SETTINGS FONTS
        self.Font_1 = Font_1
        self.Font_2 = Font_2
        self.Font_3 = Font_3
        self.Font_4 = Font_4
        self.Font_5 = Font_5
Default = Default_Attributes() #Settings the default size paramenter 
#CREATING CLASSES
    #Creating the team standard information
class Team:
    def __init__(self,name,Pts=0,W=0,L=0,D=0,GD=0,GA=0,GF=0,MP=0):
        self.name = name
        self.Pts = Pts
        self.W = W
        self.L = L
        self.D = D
        self.games = W + L + D
        self.GD = GD
        self.GA = GA
        self.GF = GF
        self.MP = MP
    def __repr__(self):
        return f"{self.name},{self.Pts}".format(self=self)
    #Creating the metrics for the general usage
class Metrics:
    def __init__(self,Universal_Counter=0,Max_Teams = 32):
        self.Uninversal_Counter = Universal_Counter
        self.Max_Teams = Max_Teams
Default_Metrics = Metrics()
    #Creating the main stage subdivisions
class Stages:
    def __init__(self,Group_Stage=[],Knockout_Stage=[]):
        self.Group_Stage = Group_Stage
        self.Knockout_Stage = Knockout_Stage
        self.Group_Stage_St = "Group Stage"
        self.Knockout_Stage_St = "Knockout Stage"
    #Settings defaults for general usage
Default_Stages = Stages()
    #Creating the group correspondance
class Groups:
    def __init__(self,Group_A="Group A",Group_B="Group B",Group_C="Group C",Group_D="Group D",Group_E="Group E",Group_F="Group F",Group_G="Group G",Group_H="Group H"):
        self.Group_A = Group_A
        self.Group_B = Group_B
        self.Group_C = Group_C
        self.Group_D = Group_D
        self.Group_E = Group_E
        self.Group_F = Group_F
        self.Group_G = Group_G
        self.Group_H = Group_H
        self.Array_Conjunction = [self.Group_A,self.Group_B,self.Group_C,self.Group_D,self.Group_E,self.Group_F,self.Group_G,self.Group_H]
    #Settings defaults for general usage
Default_Groups = Groups()
     #Creating the classifications correspondance
class Classifications:
    def __init__(self,Round_Of_16="Round of 16",Quarter_finals="Quarter finals",Semi_finals="Semi finals",Final="Finals"):
        self.Round_Of_16 = Round_Of_16
        self.Quarter_finals = Quarter_finals
        self.Semi_finals = Semi_finals
        self.Final = Final
        self.Array_Conjunction = [self.Round_Of_16,self.Quarter_finals,self.Semi_finals,self.Final]
    #Settings defaults for general usage
Default_Classifications = Classifications()
    #Creating Slots for further-visualization
class Slots():
    def __init__(self,Name_Of_Slots,Number_Of_Slot):
        self.Name_Of_Slots = Name_Of_Slots
        self.Number_Of_Slots = Number_Of_Slot

#CREATING SPECIFICS(FUNCTION-WISE)
    #Creating a warning-configuration function ----------- FORMAT(Warning_Name,Text_Wanted,ColS=None,Col=None,Row=None,RowS=None)
def Warning_Configuration(Warning_Name,Text_Wanted,ColS=None,Col=None,Row=None,RowS=None):
    Warning_Name.config(text=Text_Wanted,foreground=Default.Color_4)
    Warning_Name.grid(columnspan=ColS,rowspan=RowS,column=Col,row=Row)
    #Creating a warning-configuration function ----------- FORMAT(Attribute_Name,Text_Wanted,Color_Wanted)
def Specified_Configuration(Attribute_Name,Text_Wanted,Color_Wanted):
    Attribute_Name.configure(text=Text_Wanted,foreground=Color_Wanted)  
    #Creating a button-creation function ----------- FORMAT(Name_Of_Father,Text,Font,Width,Command,Background_Color,Letter_Color,ColS=None,Col=None,Row=None,RowS=None)
def Create_Button(Name_Of_Father,Text,Font,Width,Command,Background_Color,Letter_Color,ColS=None,Col=None,Row=None,RowS=None):
    New_Button = tk.Button(Name_Of_Father,text=Text,font=Font,width=Width,command=Command,background=Background_Color,fg=Letter_Color)
    New_Button.grid(columnspan=ColS,rowspan=RowS,column=Col,row=Row)
    return New_Button
    #Creating a label-creation function ----------- FORMAT(Name_Of_Father,Text,Font,ColS=None,Col=None,Row=None,RowS=None,Background_Color=None)
def Create_Label(Name_Of_Father,Text,Font,ColS=None,Col=None,Row=None,RowS=None,Background_Color=None,Width=None,Height=None):
    New_Label = tk.Label(Name_Of_Father,text=Text,font=Font,background=Background_Color,width=Width,height=Height)
    New_Label.grid(columnspan=ColS,rowspan=RowS,column=Col,row=Row)
    return New_Label
    #Creating an entry-creation function ----------- FORMAT(Name_Of_Father,Font,ColS=None,Col=None,Row=None,RowS=None,Width=None)
def Create_Entry(Name_Of_Father,Font,ColS=None,Col=None,Row=None,RowS=None,Width=None,Height=None):
    New_Entry = tk.Entry(Name_Of_Father,font=Font,width=Width)
    New_Entry.grid(columnspan=ColS,column=Col,row=Row,rowspan=RowS)
    return New_Entry
    #Creating a canvas-creation functions ----------- FORMAT(Name_Of_Father,Width=None,Height=None,ColS=None,RowS=None,Row=None,Col=None)
def Create_Canvas(Name_Of_Father,Width=None,Height=None,ColS=None,RowS=None,Row=None,Col=None):
    New_Canvas = tk.Canvas(Name_Of_Father,width=Width,heigh=Height)
    New_Canvas.grid(columnspan=ColS,rowspan=RowS,column=Col,row=Row)
    #Creating a multi-removal function [Essentially a Mass-Removal function] ----------- FORMAT([Array])
def Massive_Remover(Array):
    for i in Array:
        i.destroy()
    #Creating a size restricting function
def Size_Overall_Restriction(Name_Of_Root,Width=0,Height=0):
    Name_Of_Root.maxsize(Width,Height)
    Name_Of_Root.minsize(Width,Height)
    #Firing Defaults
Size_Overall_Restriction(Root,600,300)

    #Creating an array generator that makes sub-divisions to our will
def Array_Generator(Ancestor_Arrays,Father_Arrays,Children_Arrays,Additional_Commentry=None):
    if Additional_Commentry == "Degradable_Style":
        Used_Metrics = Default_Metrics.Uninversal_Counter
        Group_Standards = Default_Groups.Array_Conjunction
        Temporary_Array = []
        Father_Arrays = Father_Arrays*2
        for i in range(Ancestor_Arrays):
            Temporary_Array.append([([None]*Children_Arrays)]*(int(Father_Arrays/2)))
            Father_Arrays = int(Father_Arrays/2)
            Used_Metrics += 1
        return Temporary_Array
    if Ancestor_Arrays == None:
        Modified_Body = [([[None]]*Children_Arrays)]*Father_Arrays
        return Modified_Body
    else:
        Modified_Body = [[([""]*Children_Arrays)]*Father_Arrays]*Ancestor_Arrays
        return Modified_Body

#CREATING THE MAIN "STAGES" OF OUR APPLICATION
Raw_Group_Stage = Default_Stages.Group_Stage
Raw_Knockout_Stage = Default_Stages.Knockout_Stage
Group_Stage = Array_Generator(None,8,4,None)
Knockout_Stage = Array_Generator(4,8,2,"Degradable_Style")

#CREATING PRE_DESIGNED CLASSES
def Basic_Component_Creation(Multiple_Usage=False):
    global Canvas
    global registration_tittle
    global log_in
    global warning
    global submit_entry
    global click_button
    if Multiple_Usage == False:
        Canvas = Create_Canvas(Root,600,300,20,20)
        submit_entry = Create_Entry(Root,(Default.Font_1,Default.Size_1),20,0,7)
        click_button = Create_Button(Root,"Continue",(Default.Font_4,Default.Size_1),9,(lambda:button_clicked(submit_entry,Logging_In,click_button)),Default.Color_1,Default.Color_3,20,0,8)
    registration_tittle = Create_Label(Root,"REGISTRATION",(Default.Font_5,Default.Size_3),20,0,0)
    log_in = Create_Label(Root,"Please provide us your first name",(Default.Font_2,Default.Size_2),20,0,6)
    warning = Create_Label(Root,"",(Default.Font_1,Default.Size_1,),20,0,9)
Basic_Component_Creation()

#CREATING FUNCTIONS
def Organizer(Array,Specifics):
    if Specifics == "Group Stage":
        Used_Metric = Default_Metrics.Uninversal_Counter
        Group_Standards = Default_Groups.Array_Conjunction
        Default_Array = [[],Specifics]
        for i in Array:
            New_Array = [i,Group_Standards[Used_Metric]]
            Default_Array[0].append(New_Array)
            Used_Metric += 1
        return Default_Array
    elif Specifics == "Knockout Stage":
        Used_Metric = Default_Metrics.Uninversal_Counter
        KO_standards = Default_Classifications.Array_Conjunction
        Default_Array = [[],Specifics]
        for i in Array:
            New_Array = [i,KO_standards[Used_Metric]]
            Default_Array[0].append(New_Array)
            Used_Metric += 1
        return Default_Array

#------------------------------------------------------------------------------------#Adnan retrieve data from here for group stage points
Organized_Group = Organizer(Group_Stage,"Group Stage")
Organized_Knock_Out_Group = Organizer(Knockout_Stage,"Knockout Stage")
Able_To_Operate = True

def Create_Visualizer(Father_Of_Boxes,Wanted_Groups,Internal_Slots,Width):
    for i in range(Wanted_Groups):
            Group_Name = Create_Label(Father_Of_Boxes,Default_Groups.Group_A,None,None,None,i,None,None)
            Group_Name = Create_Label(Father_Of_Boxes,Default_Groups.Group_A,None,None,None,i,None,None)
            for j in range(Internal_Slots):                
                Slot = Create_Entry(Group_Name,(Default.Font_1,Default.Size_5),None,None,0,j+1,Width)

#For the Quarter
GENERAL_1_VALUE = None
GENERAL_2_VALUE = None
GENERAL_3_VALUE = None
GENERAL_4_VALUE = None
GENERAL_5_VALUE = None
GENERAL_6_VALUE = None
GENERAL_7_VALUE = None
GENERAL_8_VALUE = None

#For Semi
Participant_1 = None
Participant_2 = None
Participant_3 = None
Participant_4 = None

Last_Participant_1 = None
Last_Participant_2 = None

def Semi_Final_Check(Team_Array):
    global Participant_1,Participant_2,Participant_3,Participant_4,Last_Participant_1,Last_Participant_2
    KO_S = Knockout_Stage.copy()

    def Finding_Finalist(Group,Group_Indicator):
        if Group[0] != None:
            if Group[1] != None:
                if Group[0].Pts > Group[1].Pts:
                    if Group_Indicator == 1:
                        Last_Participant_1 = Group[0]
                        Organized_Knock_Out_Group[0][3][0][0] = [Last_Participant_1,Last_Participant_2]
                    elif Group_Indicator == 2:
                        Last_Participant_2 = Group[0]
                        Organized_Knock_Out_Group[0][3][0][0] = [Last_Participant_1,Last_Participant_2]
                if Group[1].Pts > Group[0].Pts:
                    if Group_Indicator == 1:
                        Last_Participant_1 = Group[0]
                        Organized_Knock_Out_Group[0][3][0][0] = [Last_Participant_1,Last_Participant_2]
                    elif Group_Indicator == 2:
                        Last_Participant_2 = Group[0]
                        Organized_Knock_Out_Group[0][3][0][0] = [Last_Participant_1,Last_Participant_2]
                if Group[1].Pts == Group[0].Pts:
                    Organized_Knock_Out_Group[0][3][0][0] = [None,None]

    if Team_Array[0][0] != None:
        if Team_Array[0][1] != None:
            if Team_Array[0][0].Pts > Team_Array[0][1].Pts:
                Participant_1 = Team_Array[0][0]
                Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
            if Team_Array[0][0].Pts < Team_Array[0][1].Pts:
                Participant_1 = Team_Array[0][1]
                Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
            if Team_Array[0][0].Pts == Team_Array[0][1].Pts:
                Organized_Knock_Out_Group[0][2][0][0] = [None,None]
        else:
            Participant_1 = Team_Array[0][0]
            Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
            Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
    if Team_Array[1][0] != None:
        if Team_Array[1][1] != None:
            if Team_Array[1][0].Pts > Team_Array[1][1].Pts:
                Participant_2 = Team_Array[1][0]
                Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
            if Team_Array[1][0].Pts < Team_Array[1][1].Pts:
                Participant_2 = Team_Array[1][1]
                Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
            if Team_Array[1][0].Pts == Team_Array[1][1].Pts:
                Organized_Knock_Out_Group[0][2][0][0] = [None,None]
        else:
            Participant_2 = Team_Array[1][0]
            Organized_Knock_Out_Group[0][2][0][0] = [Participant_1,Participant_2]
            Finding_Finalist(Organized_Knock_Out_Group[0][2][0][0],1)
    if Team_Array[2][0] != None:
        if Team_Array[2][1] != None:
            if Team_Array[2][0].Pts > Team_Array[2][1].Pts:
                Participant_3 = Team_Array[2][0]
                Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)
            if Team_Array[2][0].Pts < Team_Array[2][1].Pts:
                Participant_3 = Team_Array[2][1]
                Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)
            if Team_Array[2][0].Pts == Team_Array[2][1].Pts:
                Organized_Knock_Out_Group[0][2][0][1] = [None,None]
        else:
            Participant_3 = Team_Array[2][0]
            Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
            Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)
    if Team_Array[3][0] != None:
        if Team_Array[3][1] != None:
            if Team_Array[3][0].Pts > Team_Array[3][1].Pts:
                Participant_4 = Team_Array[3][0]
                Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)
            if Team_Array[3][0].Pts < Team_Array[3][1].Pts:
                Participant_4 = Team_Array[2][1]
                Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
                Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)
            if Team_Array[3][0].Pts == Team_Array[3][1].Pts:
                Organized_Knock_Out_Group[0][2][0][1] = [None,None]
        else:
            Participant_4 = Team_Array[3][0]
            Organized_Knock_Out_Group[0][2][0][1] = [Participant_3,Participant_4]
            Finding_Finalist(Organized_Knock_Out_Group[0][2][0][1],2)

#Settings a default value for each of the globals [in case one is fired before the other one]
def Move_Teams_Forward(Current_Group):
        #Creating general values to facilitate communication between functions
        global GENERAL_1_VALUE
        global GENERAL_2_VALUE 
        global GENERAL_3_VALUE 
        global GENERAL_4_VALUE 
        global GENERAL_5_VALUE 
        global GENERAL_6_VALUE 
        global GENERAL_7_VALUE 
        global GENERAL_8_VALUE
        #BEGINNING STAGE TO MOVE_TEAMS_FORWARD
        #BETWEEN FIRST AND SECOND            
        if Current_Group == 0:
            Examinating_Slot = Knockout_Stage[0][0]
            if Knockout_Stage[0][0][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_1_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_1_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_2_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][0] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
        elif Current_Group == 1:
            Examinating_Slot = Knockout_Stage[0][1]
            if Knockout_Stage[0][1][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_2_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_2_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_1_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][0] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][0] = [GENERAL_1_VALUE,GENERAL_2_VALUE]
                    return
        #BETWEEN THIRD AND FOURTH
        if Current_Group == 2:
            Examinating_Slot = Knockout_Stage[0][2]
            if Knockout_Stage[0][2][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_3_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_3_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_4_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][1] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
        elif Current_Group == 3:
            Examinating_Slot = Knockout_Stage[0][3]
            if Knockout_Stage[0][3][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_4_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_4_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_3_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][1] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][1] = [GENERAL_3_VALUE,GENERAL_4_VALUE]
                    return
        #BETWEEN FIFTH AND SIXTH
        if Current_Group == 4:
            Examinating_Slot = Knockout_Stage[0][4]
            if Knockout_Stage[0][4][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_5_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_5_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_6_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][2] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
        if Current_Group == 5:
            Examinating_Slot = Knockout_Stage[0][5]
            if Knockout_Stage[0][5][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_6_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_5_VALUE =Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_5_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][2] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][2] = [GENERAL_5_VALUE,GENERAL_6_VALUE]
                    return
        #BETWEEN SEVENTH AND EIGHT
        if Current_Group == 6:
            Examinating_Slot = Knockout_Stage[0][6]
            if Knockout_Stage[0][6][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_7_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_7_VALUE,GENERAL_8_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_7_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_7_VALUE,GENERAL_8_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_6_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][3] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_6_VALUE,GENERAL_7_VALUE]
                    return
        elif Current_Group == 7:
            Examinating_Slot = Knockout_Stage[0][7]
            if Knockout_Stage[0][7][1] != None:
                if Examinating_Slot[0].Pts > Examinating_Slot[1].Pts:
                    GENERAL_8_VALUE = Examinating_Slot[0]
                    Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_7_VALUE,GENERAL_8_VALUE]
                    return
                if Examinating_Slot[0].Pts < Examinating_Slot[1].Pts:
                    GENERAL_8_VALUE = Examinating_Slot[1]
                    Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_7_VALUE,GENERAL_8_VALUE]
                    return
                if Examinating_Slot[0].Pts == Examinating_Slot[1].Pts:
                    if GENERAL_7_VALUE == None:
                        Organized_Knock_Out_Group[0][1][0][3] = [None,None]
                    else:
                        Organized_Knock_Out_Group[0][1][0][3] = [GENERAL_6_VALUE,GENERAL_7_VALUE]
                    return

def group_progression(specified_stage,group):
        max_ga = Default_Metrics.Uninversal_Counter-1
        #Creating arrays that determine irregularities
        Whole_Comparison_Value = []
        First_Comparison_Stage = []
        Highest_GD = []
        def Goal_Difference_Comparision(Array):
            for i in Array:
                Highest_GD.append(i[0].GD)
            Highest_GD.sort()
            if len(Highest_GD) > 1:
                if Highest_GD[int(len(Highest_GD)-1)] == 0 and Highest_GD[int(len(Highest_GD)-2)] == 0:
                    print("Undetermined, please change the values accordingly [No teams will be changed and previous will remain]")
                else:
                    if Highest_GD[int(len(Highest_GD)-1)] > Highest_GD[int(len(Highest_GD)-2)]:
                        Knockout_Stage[0][group].pop()
                        Max_Value = max(First_Comparison_Stage)
                        First_Comparison_Stage.pop()
                        Index_Max = Un_Sorted_Stage.index(Max_Value)
                        Un_Sorted_Stage.pop(Index_Max)
                        Copy_Of_Array[0][group] += [Whole_Comparison_Value[Index_Max][0]]
                        Whole_Comparison_Value.pop(Index_Max)
                        Move_Teams_Forward(group)
                    if Highest_GD[int(len(Highest_GD)-1)] == Highest_GD[int(len(Highest_GD)-2)]:
                        print("We got equal numbers again")
        for i in specified_stage[0][group][0]:
            if i[0] != None:
                First_Comparison_Stage.append(i[0].Pts)
                Whole_Comparison_Value.append(i)
        Un_Sorted_Stage = First_Comparison_Stage.copy()
        First_Comparison_Stage.sort()
        if len(First_Comparison_Stage) > 1:
            if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] == 0:
                print("All are Zero, therefore teams have not been set accordingly")
                return
            if len(First_Comparison_Stage) == 4:
                if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] > 0 and First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] > 0:
                    if First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-4)]:
                        print(f"All numbers are equal to {First_Comparison_Stage[3]}; AKA the highest number")
                        Goal_Difference_Comparision(Whole_Comparison_Value)
                    else:
                        Whole_Comparison_Value.pop(0)
                        Goal_Difference_Comparision(Whole_Comparison_Value)
                    return
                if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] > 0:
                    if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] > First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] > First_Comparison_Stage[int(len(First_Comparison_Stage)-3)]:
                        Array = Organized_Knock_Out_Group[0][0]
                        Copy_Of_Array = Array[:]
                        Copy_Of_Array[0][group] = []
                        for i in range(2):
                            Max_Value = max(First_Comparison_Stage)
                            First_Comparison_Stage.pop()
                            Index_Max = Un_Sorted_Stage.index(Max_Value)
                            Un_Sorted_Stage.pop(Index_Max)
                            Copy_Of_Array[0][group] += [Whole_Comparison_Value[Index_Max][0]]
                            Whole_Comparison_Value.pop(Index_Max)
                        Move_Teams_Forward(group)
                    elif First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] > First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-3)]:
                        Max_Value = max(First_Comparison_Stage)
                        Array = Organized_Knock_Out_Group[0][0]
                        Copy_Of_Array = Array[:]
                        Copy_Of_Array[0][group] = [Whole_Comparison_Value[Un_Sorted_Stage.index(Max_Value)][0],None]
                        Whole_Comparison_Value.pop(0)
                        #Function that distinguishes which of the following has the max value in terms of the biggest second highest values
                        Current_Max = 0
                        for i in Whole_Comparison_Value:
                            if i[0].Pts >= Current_Max:
                                Current_Max = i[0].Pts
                            else:
                                Whole_Comparison_Value.remove(i)
                        Goal_Difference_Comparision(Whole_Comparison_Value)
                    if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] > First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] == 0 and First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-4)]:
                        Array = Organized_Knock_Out_Group[0][0]
                        Copy_Of_Array = Array[:]
                        Copy_Of_Array[0][group] = []
                        for i in range(2):
                            Max_Value = max(First_Comparison_Stage)
                            First_Comparison_Stage.pop()
                            Index_Max = Un_Sorted_Stage.index(Max_Value)
                            Un_Sorted_Stage.pop(Index_Max)
                            Copy_Of_Array[0][group] += [Whole_Comparison_Value[Index_Max][0]]
                            Whole_Comparison_Value.pop(Index_Max)
                        Goal_Difference_Comparision(Whole_Comparison_Value)
                        Move_Teams_Forward(group)
                    return
            if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and len(First_Comparison_Stage)== 2:
                if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] != 0 and len(First_Comparison_Stage) == 2:
                    Array = Organized_Knock_Out_Group[0][0]
                    Copy_Of_Array = Array[:]
                    Copy_Of_Array[0][group] = [Whole_Comparison_Value[1][0],Whole_Comparison_Value[0][0]]
                elif First_Comparison_Stage[int(len(First_Comparison_Stage)-1)]:
                    Whole_Comparison_Value.pop(0)
                    Whole_Comparison_Value.pop()
                    Goal_Difference_Comparision(Whole_Comparison_Value)
                if len(First_Comparison_Stage) > 2:
                    if First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-3)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] != 0:
                        Whole_Comparison_Value.pop()
                        Goal_Difference_Comparision(Whole_Comparison_Value)
            else:
                if len(First_Comparison_Stage) == 3:
                    if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] != First_Comparison_Stage[int(len(First_Comparison_Stage)-2)]:
                        if First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-3)]:
                            Max_Value = max(First_Comparison_Stage)
                            Array = Organized_Knock_Out_Group[0][0]
                            Copy_Of_Array = Array[:]
                            Copy_Of_Array[0][group] = [Whole_Comparison_Value[Un_Sorted_Stage.index(Max_Value)][0],None]
                            Whole_Comparison_Value.pop()
                            Goal_Difference_Comparision(Whole_Comparison_Value)
                        else:
                            Array = Organized_Knock_Out_Group[0][0]
                            Copy_Of_Array = Array[:]
                            Copy_Of_Array[0][group] = [Whole_Comparison_Value[2][0],Whole_Comparison_Value[1][0]]
                            Move_Teams_Forward(group)
                    else:
                        if First_Comparison_Stage[int(len(First_Comparison_Stage)-1)] == First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] and First_Comparison_Stage[int(len(First_Comparison_Stage)-2)] > First_Comparison_Stage[int(len(First_Comparison_Stage)-3)]:
                            Array = Organized_Knock_Out_Group[0][0]
                            Copy_Of_Array = Array[:]
                            Copy_Of_Array[0][group] = []
                            for i in range(2):
                                Max_Value = max(First_Comparison_Stage)
                                First_Comparison_Stage.pop()
                                Index_Max = Un_Sorted_Stage.index(Max_Value)
                                Un_Sorted_Stage.pop(Index_Max)
                                Copy_Of_Array[0][group] += [Whole_Comparison_Value[Index_Max][0]]
                                Whole_Comparison_Value.pop(Index_Max)
                        else:
                            Array = Organized_Knock_Out_Group[0][0]
                            Copy_Of_Array = Array[:]
                            Copy_Of_Array[0][group] = [None,None]
                            Goal_Difference_Comparision(Whole_Comparison_Value)
                else:
                    Array = Organized_Knock_Out_Group[0][0]
                    Copy_Of_Array = Array[:]
                    Copy_Of_Array[0][group] = [Whole_Comparison_Value[1][0],Whole_Comparison_Value[0][0]]
        else:
            if First_Comparison_Stage[0] != 0:
                Array = Organized_Knock_Out_Group[0][0]
                Copy_Of_Array = Array[:]
                Copy_Of_Array[0][group] = [Whole_Comparison_Value[0][0],None]
            else:
                print("Starting stage, uncapable of calculating between other teams: lack of teams")
        Move_Teams_Forward(group)
        Semi_Final_Check(Organized_Knock_Out_Group[0][1][0])

def Print_Structure():   
    print() #This is written as to avoid collision between previous structures of the World-cup
    print(Organized_Group[1])
    for i in range(int(len(Organized_Group)/2)):
        for j in Organized_Group[0]:
            print(j)
    print()
    print(Organized_Knock_Out_Group[1]) 
    for i in Organized_Knock_Out_Group[0]:
        print(i)

def Return_To_Main(Additional_Information,Settings,Array,Additional_Operation=None,Attributes=None):
    Basic_Component_Creation(True)
    Logging_In(Additional_Information,Settings)
    if Additional_Operation != None:
        Additional_Operation(Attributes[0],Attributes[1])
    Massive_Remover(Array)
    
def Text_To_Class(Text,Class_Wanted):
    New_Class = Class_Wanted(Text)
    return New_Class

def Adding_Team(text,Bridged_Value):
    global Full_Capacity,Is_Same_Text
    Is_Same_Text = False
    Full_Capacity = False
    Slots_Free = False
    Group_Standards = Default_Groups.Array_Conjunction

    Current_Group_Selected = Bridged_Value[0].get()
    global Number_Provided
    Number_Provided = 0
    if Current_Group_Selected == "Group A":
        Number_Provided = 0
    if Current_Group_Selected == "Group B":
        Number_Provided = 1
    if Current_Group_Selected == "Group C":
        Number_Provided = 2
    if Current_Group_Selected == "Group D":
        Number_Provided = 3
    if Current_Group_Selected == "Group E":
        Number_Provided = 4
    if Current_Group_Selected == "Group F":
        Number_Provided = 5
    if Current_Group_Selected == "Group G":
        Number_Provided = 6
    if Current_Group_Selected == "Group H":
        Number_Provided = 7

    #Making a function that verifies if we have enough space to insert the team
    def Slot_Verification(i,Stage_Wanted):
        global Full_Capacity,Is_Same_Text

        if i == Stage_Wanted:
            Is_Same_Text = False
            for j in range(8):
                global Current_Slot
                Current_Slot = Organized_Group[0][j]
                if Current_Slot[1] == Current_Value:
                    for g in range(8):
                        #Setting global and univeral accesible variables
                        global First_Value
                        global Previous_Team_Value_1
                        global Previous_Team_Value_2 
                        global Previous_Team_Value_3
                        if g == 4:
                            Full_Capacity = True
                            return False
                        if Current_Slot[0][g][0] == None:
                            First_Value = Current_Slot[0][0][0]
                            Current_Slot[0] = [[Text_To_Class(text,Team)],[None],[None],[None]]
                            global Selected_Number_Slot
                            Selected_Number_Slot = g
                            if g == 1:
                                if First_Value.name != text:
                                    Current_Slot[0] = [Previous_Team_Value_1,[Text_To_Class(text,Team)],[None],[None]]
                                elif Current_Slot[0][0][0].name == text:
                                    Is_Same_Text = True
                                    return False
                            if g == 2:
                                if text != Previous_Team_Value_1[0].name and text != Previous_Team_Value_2[0].name:
                                    Current_Slot[0] = [Previous_Team_Value_1,Previous_Team_Value_2,[Text_To_Class(text,Team)],[None]]
                                else:
                                    Current_Slot[0] = [Previous_Team_Value_1,Previous_Team_Value_2,[None],[None]]
                                    Is_Same_Text = True
                                    return False
                            if g == 3:
                                if text != Previous_Team_Value_1[0].name and text != Previous_Team_Value_2[0].name and text != Previous_Team_Value_3[0].name:
                                    Current_Slot[0] = [Previous_Team_Value_1,Previous_Team_Value_2,Previous_Team_Value_3,[Text_To_Class(text,Team)]]
                                else:
                                    Current_Slot[0] = [Previous_Team_Value_1,Previous_Team_Value_2,Previous_Team_Value_3,[None]]
                                    Is_Same_Text = True
                                    return False
                            return True
                        else:
                            Previous_Team_Value_1 = Current_Slot[0][0]
                            if g == 1:
                                Previous_Team_Value_2 = Current_Slot[0][1]
                            if g == 2:
                                Previous_Team_Value_3 = Current_Slot[0][2]

    if type(Bridged_Value) == list:
        for i in Bridged_Value:
            if type(i) == tk.Label:
                if Slots_Free == True:
                    global Message
                    Message = i
                    Specified_Configuration(Message,"Please insert the corresponding team's Group-Stage points:",Default.Color_5)
                    click_button = Create_Button(Root,"Finish Layout",(Default.Font_4,Default.Size_1),12,(lambda:Uploading_New_Team(click_button,General_Option_Menu,Current_Stats,i)),Default.Color_1,Default.Color_3,20,2,4)
                    #Creation of a list and the correspondance of points
                    Selection_list = [i for i in range(0,10)]
                    global Var
                    Var = tk.StringVar(Root)
                    General_Option_Menu = tk.OptionMenu(Root,Var,*Selection_list)
                    Var.set(Selection_list[0])
                    General_Option_Menu.grid(columnspan=10,column=3,row=1,rowspan=12)
            elif type(i) == tk.StringVar:
                global Current_Value
                Current_Value = i.get()
                for i in Group_Standards:
                    if Current_Value == i:
                        Able_To_Insert = Slot_Verification(Current_Value,i)
                        if Able_To_Insert == True:
                            Current_Stats = Create_Label(Root,(f"Current team: {text}"+f"\nCurrent group: {Current_Value}"),(Default.Font_1,Default.Size_4),20,0,2)
                            Slots_Free = True

def Uploading_New_Team(Connection_Button,Connective_Extra_1,Connective_Extra_2,Settings_to_configure):
    Represented_Figure = Current_Slot[0][Selected_Number_Slot][0]
    Represented_Figure.Pts = int(Var.get()) 
    #The function checks the teams and based on the new information it fetches, it passes the new teams in the corresponding group to the new group        
    group_progression(Organized_Group,Number_Provided)
    Return_To_Main(Username,True,[Connection_Button,Connective_Extra_1,Connective_Extra_2,Message,return_button])

def button_clicked(Entry,Function_To_Fire,Self,Type_Two_Function_Fire=None,Element_Removal=None,Bridged_Value=None,Specifics=None):
    text = Entry.get()
    Has_Numbers = False
    Has_Spaces = False
    Returned_Empty = False
    Restrictions = False
    global Exceptions
    Exceptions = ["Saudi Arabia","Costa Rica","South Korea","North Korea","Ivory Coast","Bosnia and Herzegovina","Faroe Islands","Northern Ireland","North Macedonia","New Zealand","Trinidad y Tobago","Serbia and Montenegro"]
    Exception_Noted = False

    for i in text:
        for j in range(0,10):
            if i == str(j):
                if Specifics == None:
                    Warning_Configuration(warning,"Your name cannot include any numbers!")
                    Has_Numbers = True
                else:
                    Warning_Configuration(warning,"Your team cannot include any numbers!")
                    Has_Numbers = True
                return
        if i == " " and Specifics == None:
            Warning_Configuration(warning,"Your name cannot not include any spaces!")
            Has_Spaces = True
        if i == " " and Specifics != None:
            Counter = Default_Metrics.Uninversal_Counter
            for j in Exceptions:
                Counter += 1
                if text == j:
                    Exception_Noted = True
                    break
                if Counter == len(Exceptions):
                    Warning_Configuration(warning,"Your team cannot not include any spaces!")
                    Has_Spaces = True
            
            
    if text == "" and Specifics == None:
        Returned_Empty = True
        Warning_Configuration(warning,"You cannot leave the input empty! Please write your first name!")
    elif text == "" and Specifics != None:
        Returned_Empty = True
        Warning_Configuration(warning,"You cannot leave the input empty! Please write your team's name!")

    if Has_Numbers == False and Has_Spaces == False and Returned_Empty == False:
        if text.isalpha() or Exception_Noted == True:
            if Bridged_Value != None:
                Function_To_Fire(text,Bridged_Value)
                if Full_Capacity == False and Is_Same_Text == False:
                    return_button.destroy()
                if Is_Same_Text == True or Full_Capacity == True:
                    Restrictions = True
            else:
                Function_To_Fire(text)
            Warning_Configuration(warning,"")
            if Type_Two_Function_Fire != None:
                Type_Two_Function_Fire()
                if Element_Removal:
                    Massive_Remover([Element_Removal])
            elif Element_Removal != None:
                if Restrictions == False:
                    Massive_Remover([Element_Removal])
                else:
                    if Full_Capacity == True:
                        Warning_Configuration(warning,"Error! The current group is full! Edit the corresponding group")
                    if Is_Same_Text == True:
                        Warning_Configuration(warning,"Team already exists! Please choose another name!")
            if Restrictions == False:
                Massive_Remover((Entry,Self))
        else:
            Warning_Configuration(warning,"Your name cannot not include any special characters!")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------# UNDER-DEVELOPMENT
def Edit_Button_Function(list_of_elements,edit_text):
    global Expansion_Is_Open,New_Tab
    Expansion_Is_Open = False

    if Able_To_Operate == True:
        Massive_Remover(list_of_elements)
        Specified_Configuration(edit_text,"Please insert the corresponding values accordingly:",Default.Color_5)
        Canvas = Create_Canvas(Root,600,300,20,20)
        Current_Name = Create_Label(Canvas,"Current Team's Name:",(Default.Font_1,Default.Size_4),12,1,8)
        Old_Team_Name = Create_Entry(Canvas,(Default.Font_3,Default.Size_4),20,4,8)
        New_Name = Create_Label(Canvas,"New Name:",(Default.Font_1,Default.Size_4),12,2,9)
        New_Team_Name = Create_Entry(Canvas,(Default.Font_3,Default.Size_4),20,4,9)
        Points_Label = Create_Label(Canvas,"Points:",(Default.Font_1,Default.Size_4),13,2,10)
        Save_And_Continue = Create_Button(Canvas,"Save and continue",(Default.Font_4,Default.Size_1),None,(lambda:Verification()),Default.Color_1,Default.Color_3,20,14,17)

        array_for_removal = [Current_Name,Old_Team_Name,New_Name,New_Team_Name,Points_Label,Save_And_Continue,edit_text]
        return_button = Create_Button(Root,"Return to Main-Menu",(Default.Font_4,Default.Size_1),None,(lambda:Return_To_Main(Username,True,array_for_removal,Warning_Configuration,(warning,""))),Default.Color_1,Default.Color_3,7,0,17)
        warning.grid(row=15)

        def Verification():
            Stage_Type = Var4.get()
            Specification_In_Stage = Var3.get()
            Specified_Group = Var2.get()

            def Group_Stage_Function(i,HT,Specifics=None):
                Dependable = None
                if Specifics == None:
                    Dependable = i[0]
      
                if type(Dependable) == Team:
                    Old_Team_Current =  Old_Team_Name.get()
                    New_Team_Points = int(Var1.get())
                    if Expansion_Is_Open == True:
                        New_Team_MP = New_Var_1.get()
                        New_Team_W = New_Var_2.get()
                        New_Team_D = New_Var_3.get()
                        New_Team_L = New_Var_4.get()
                        New_Team_GF = New_Var_5.get()
                        New_Team_GA = New_Var_6.get()
                        New_Team_GD = New_Var_7.get()

                    New_Team_Current = New_Team_Name.get()
                    if Old_Team_Current == Dependable.name:
                        #Creating a function that automatically does the expected results without the neccessity of re-writting each function
                        def Normal_Proceedure():
                            Dependable.Pts = New_Team_Points
                            
                            if Expansion_Is_Open == True:
                                Dependable.MP = int(New_Team_MP)
                                Dependable.W = int(New_Team_W)
                                Dependable.D = int(New_Team_D)
                                Dependable.L = int(New_Team_L)
                                Dependable.GF = int(New_Team_GF)
                                Dependable.GA = int(New_Team_GA)
                                Dependable.GD = int(New_Team_GD)
                                New_Var_1.set(0)
                                New_Var_2.set(0)
                                New_Var_3.set(0)
                                New_Var_4.set(0)
                                New_Var_5.set(0)
                                New_Var_6.set(0)
                                New_Var_7.set(0)

                            print("Attributes were updated successfully")
                            Warning_Configuration(warning,"")
                            New_Team_Name.delete(0,'end')
                            Old_Team_Name.delete(0,'end')
                            Var1.set(0)
                        #-------------------------------------------- Where the value/s update
                            for w in HT:
                                if type(w[0]) == Team: 
                                    if New_Team_Current == w[0].name:
                                        return

                        if New_Team_Current != "" and New_Team_Current.isalpha():
                            Normal_Proceedure()
                            Dependable.name = New_Team_Current
                            return True
                        if New_Team_Current == "":
                            Normal_Proceedure()
                            Dependable.name = Old_Team_Current
                            return True
                        elif New_Team_Current.isalpha():
                            Normal_Proceedure()
                            return True
                        for f in New_Team_Current:
                            if f == " ":
                                for j in Exceptions:
                                    if New_Team_Current == j:
                                        Dependable.name = New_Team_Current
                                        Normal_Proceedure()
                                        return True

            if Stage_Type == "Group Stage":
                if Specification_In_Stage == "Group A":
                    Whole_Table = Organized_Group[0][0][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,0)
                            return
                if Specification_In_Stage == "Group B":
                    Whole_Table = Organized_Group[0][1][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,1)
                            return
                if Specification_In_Stage == "Group C":
                    Whole_Table = Organized_Group[0][2][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,2)
                            return
                if Specification_In_Stage == "Group D":
                    Whole_Table = Organized_Group[0][3][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,3)
                            return
                if Specification_In_Stage == "Group E":
                    Whole_Table = Organized_Group[0][4][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,4)
                            return
                if Specification_In_Stage == "Group F":
                    Whole_Table = Organized_Group[0][5][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,5)
                            return
                if Specification_In_Stage == "Group G":
                    Whole_Table = Organized_Group[0][6][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,6)
                            return
                if Specification_In_Stage == "Group H":
                    Whole_Table = Organized_Group[0][7][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table)
                        if Successfully_Updated == True:
                            group_progression(Organized_Group,7)
                            return
                Warning_Configuration(warning,"Error: please check if all the information is provided accordingly")
            else:
                if Specified_Group == "Round of 16":
                    Whole_Table = Organized_Knock_Out_Group[0][0][0][0]
                    for i in Whole_Table:
                        Successfully_Updated = Group_Stage_Function(i,Whole_Table,"On")
                        if Successfully_Updated == True:
                            return
                if Specified_Group == "Quarter finals":
                    for i in Organized_Knock_Out_Group[0][1][0][0]:
                        None
                if Specified_Group == "Semi finals":
                    for i in Organized_Knock_Out_Group[0][2][0][0]:
                        None
                if Specified_Group == "Finals":
                    for i in Organized_Knock_Out_Group[0][3][0][0]:
                        None
                Warning_Configuration(warning,"Error: please check if all the information is provided accordingly")

        #POINT VAR - Number-based selection list
        Selection_list_1 = [i for i in range(0,10)]
        Var1 = tk.StringVar(Root)
        General_Option_Menu_1 = tk.OptionMenu(Root,Var1,*Selection_list_1)
        Var1.set(Selection_list_1[0])
        General_Option_Menu_1.grid(columnspan=11,column=5,row=6,rowspan=11)
  
        def Create_Expansion_Tab():
            global New_Var_1,New_Var_2,New_Var_3,New_Var_4,New_Var_5,New_Var_6,New_Var_7,Expansion_Is_Open,New_Tab
            if Expansion_Is_Open == False:
                Expansion_Is_Open = True
                
                New_Tab = tk.Tk()
                New_Tab.title("Expansion customization")
                Size_Overall_Restriction(New_Tab,502,70)
                #Creating new labels for the new expansion table
                Space_1 = tk.Label(New_Tab,text=" "+" ").grid(row=0,column=0)
                Label_2 = tk.Label(New_Tab,text="      "+"MP"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=1)
                Label_3 = tk.Label(New_Tab,text="      "+"W"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=2)
                Label_4 = tk.Label(New_Tab,text="      "+"D"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=3)
                Label_5 = tk.Label(New_Tab,text="      "+"L"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=4)
                Label_6 = tk.Label(New_Tab,text="      "+"GF"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=5)
                Label_7 = tk.Label(New_Tab,text="      "+"GA"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=6)
                Label_8 = tk.Label(New_Tab,text="      "+"GD"+"      ",font=(Default.Font_1,Default.Size_4)).grid(row=0,column=7)

                #Creating a function that allows us to make StringVars with ease
                def Create_New_OptionMenu(Father,StringVar,ContentsOfList,R,C):
                    
                    General_Option_Menu_1 = tk.OptionMenu(Father,StringVar,*ContentsOfList).grid(row=R,column=C)
                    StringVar.set(ContentsOfList[10])

                #We are going to use this list to create ALL option menus
                General_List = [i for i in range(-10,10)]

                #Creating the actual Option-Menus
                    #CREATING THE VARS
                New_Var_1 = tk.StringVar(New_Tab)
                New_Var_2 = tk.StringVar(New_Tab)
                New_Var_3 = tk.StringVar(New_Tab)
                New_Var_4 = tk.StringVar(New_Tab)
                New_Var_5 = tk.StringVar(New_Tab)
                New_Var_6 = tk.StringVar(New_Tab)
                New_Var_7 = tk.StringVar(New_Tab)

                    #CREATING THE OPTION-MENU
                Create_New_OptionMenu(New_Tab,New_Var_1,General_List,1,1)
                Create_New_OptionMenu(New_Tab,New_Var_2,General_List,1,2)
                Create_New_OptionMenu(New_Tab,New_Var_3,General_List,1,3)
                Create_New_OptionMenu(New_Tab,New_Var_4,General_List,1,4)
                Create_New_OptionMenu(New_Tab,New_Var_5,General_List,1,5)
                Create_New_OptionMenu(New_Tab,New_Var_6,General_List,1,6)
                Create_New_OptionMenu(New_Tab,New_Var_7,General_List,1,7)

                array_for_removal.append(New_Tab)
                #Creating the function that will close after the user closes the tab
                def Close_Expansion_Tab():
                    global Expansion_Is_Open
                    Warning_Configuration(warning,"")
                    Index_For_NewTab = array_for_removal.index(New_Tab)
                    array_for_removal.pop(Index_For_NewTab)
                    Expansion_Is_Open = False
                    New_Tab.destroy()
                #Creating a function that if the main tab is closed, the tab, both of the tabs will be closed one after the other
                def Close_With_Expansion_Open():
                    if Expansion_Is_Open == True:
                        Close_Expansion_Tab()
                    Root.destroy
                    Root.quit()
                    
                New_Tab.protocol("WM_DELETE_WINDOW",Close_Expansion_Tab)
                Root.protocol('WM_DELETE_WINDOW',Close_With_Expansion_Open)
            else:
                Warning_Configuration(warning,"You already have an expansion menu open!")
        Expand = Create_Button(Root,"Expand Menu",(Default.Font_4,Default.Size_1),None,(lambda:Create_Expansion_Tab()),Default.Color_6,Default.Color_3,10,10,10)
        array_for_removal.append(Expand)

        #POINT VAR2 - Classification-based selection list
        Selection_list_2 = [Default_Classifications.Round_Of_16,Default_Classifications.Quarter_finals,Default_Classifications.Semi_finals,Default_Classifications.Final]
        Var2 = tk.StringVar(Root)

        #POINT VAR3 - Group-based selection list (Re-configure to actual group analysis [as in, actually check instead of having just pre-set information])
        Selection_list_3 = []
            #Function that allows us to get the respective information from within the group itself    
        def Checking_Team_Integrity(Attribute,List_Wanted,Specifics=None):
            Counter = Default_Metrics.Uninversal_Counter
            for i in Attribute[0]:
                Current_Value = Attribute[0][Counter][1]
                List_Wanted.append(Current_Value)
                Counter += 1
            if Specifics == "Only-Stages":
                for i in Attribute[0]:
                    Current_Value = Attribute[0][Counter][1]
                    List_Wanted.append(Current_Value)
                    Counter += 1

        Checking_Team_Integrity(Organized_Group,Selection_list_3)
        Var3 = tk.StringVar(Root)
        General_Option_Menu_3 = tk.OptionMenu(Root,Var3,*Selection_list_3)
        Var3.set(Selection_list_3[0])
        General_Option_Menu_3.grid(columnspan=11,column=0,row=0,rowspan=10)

        #POINT VAR4
        Selection_list_4 = [Default_Stages.Group_Stage_St,Default_Stages.Knockout_Stage_St]
        Var4 = tk.StringVar(Root)
        General_Option_Menu_4 = tk.OptionMenu(Root,Var4,*Selection_list_4)
        Var4.set(Selection_list_4[0])
        General_Option_Menu_4.grid(columnspan=19,column=0,row=0,rowspan=10)

        global Starter_Value
        global Currently_Group_Stage
        global Old_Value

        Starter_Value = Selection_list_4[0]
        #We are now adding the elements to the array that we couldn't add before in the "array of removal", due to us being unable to call something didn't yet exist
        wanted_elements_to_array = [return_button,General_Option_Menu_1,General_Option_Menu_3,General_Option_Menu_4]
        for i in wanted_elements_to_array:
            array_for_removal.append(i)

        #Update function: Automatically updates the variables inside the selected lists with accordance to the leading box (which are Group-Staging and Knockout-Staging)
        def Update_Function(New_Value=None):
            global Selection_list_3 

            def Get_My_Members():
                if New_Value == "Round of 16":
                    return len(Organized_Knock_Out_Group[0][0][0])
                if New_Value == "Quarter finals":
                    return len(Organized_Knock_Out_Group[0][1][0])
                if New_Value == "Semi finals":
                    return len(Organized_Knock_Out_Group[0][2][0])
                if New_Value == "Finals":
                    return len(Organized_Knock_Out_Group[0][3][0])

            New_Selection_List = []

            My_Member_Count = Get_My_Members()      
            for i in range(1,My_Member_Count+1):
                New_Selection_List.append(i)

            General_Option_Menu_3.destroy()
            Test_Option_Menu = tk.OptionMenu(Root,Var3,*New_Selection_List)
            Test_Option_Menu.grid(columnspan=11,column=0,row=0,rowspan=10)
            Var3.set(New_Selection_List[0])
            array_for_removal.append(Test_Option_Menu)

        Old_Value = Var2.get()
        def Hello(*args):
            global Old_Value
            New_Value = Var2.get()
            if Old_Value != New_Value:
                Update_Function(New_Value) 
            if New_Value == "Round of 16" and Old_Value == New_Value:
                Update_Function(New_Value)
            Old_Value = New_Value

        def Switching_Button(*arg):
            global Starter_Value
            global General_Option_Menu_N
            Current_State = Var4.get()
            if Current_State == "Group Stage" and Starter_Value != Current_State:
                General_Option_Menu_N.destroy()

                New_Selection_List = []
                Checking_Team_Integrity(Organized_Group,New_Selection_List)
                Test_Option_Menu = tk.OptionMenu(Root,Var3,*New_Selection_List)
                Test_Option_Menu.grid(columnspan=11,column=0,row=0,rowspan=10)
                Var3.set(New_Selection_List[0])
                array_for_removal.append(Test_Option_Menu)

            if Current_State == "Knockout Stage" and Starter_Value != Current_State:
                
                New_Selection_List_2 = []
                Checking_Team_Integrity(Organized_Knock_Out_Group,New_Selection_List_2)
                General_Option_Menu_N = tk.OptionMenu(Root,Var2,*Selection_list_2)
                Var2.set(Selection_list_2[0])
                General_Option_Menu_N.grid(columnspan=12,column=8,row=0,rowspan=10)
                array_for_removal.append(General_Option_Menu_N)

            Starter_Value = Current_State

        Var2.trace('w',Hello)
        Var4.trace('w',Switching_Button)
    else:
        Warning_Configuration(warning,"You are not allowed to edit while operating side-functions")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------# UNDER-DEVELOPMENT
def Logging_In(text,first=True):
    global Username
    Username = text
    #CONFIGURATION AND REMOVAL
    if first == True:
        log_in.destroy()
    registration_tittle.config(text="Welcome" + " " + text + "!")
    #NEW CREATION OF VALUES
    global Can_Generate_Preset
    Can_Generate_Preset = True
    proceedure_inquiry = Create_Label(Root,"What would you like to do today?",(Default.Font_2,Default.Size_2),20,0,3)
    greetings_message = Create_Label(Root,"I am ECHO, your personal assistant,",(Default.Font_1,Default.Size_4),20,0,2)
    disclaimer_message = Create_Label(Root,"Disclaimer: the following application is still under development. Please be patient!",(Default.Font_2,Default.Size_4),20,0,19)
    #NEW SUB-DIVISION CREATION
    Sub_Box = Create_Label(Root,None,None,20,0,3,10,Default.Color_3)
    Add_Button = Create_Button(Sub_Box,"Add Team/Scores",(Default.Font_1,Default.Size_4),None,(lambda:add_button_clicked()),Default.Color_1,Default.Color_3,None,1,1)
    Edit_Button = Create_Button(Sub_Box,"Edit Teams/Scores",(Default.Font_1,Default.Size_4),None,(lambda:Edit_Button_Function([registration_tittle,greetings_message,disclaimer_message,Sub_Box],proceedure_inquiry)),Default.Color_1,Default.Color_3,None,2,1)    
    View_Button = Create_Button(Sub_Box,"Structure Pre-view",(Default.Font_1,Default.Size_4),None,(lambda:Print_Structure()),Default.Color_1,Default.Color_3,None,4,1)    
    #FIRING CORRESPONDING FUNCTIONS
    def add_button_clicked():
        if Able_To_Operate == True:
            Massive_Remover([registration_tittle,greetings_message,disclaimer_message,Sub_Box])
            Specified_Configuration(proceedure_inquiry,"Please specify the team's destination and name",Default.Color_5)

            Selection_list = ["Group A","Group B","Group C","Group D","Group E","Group F","Group G","Group H"]
            Var = tk.StringVar(Root)
            General_Option_Menu = tk.OptionMenu(Root,Var,*Selection_list)

            Var.set(Selection_list[0])
            General_Option_Menu.grid(columnspan=10,column=1,row=0,rowspan=12)
            submit_entry = Create_Entry(Root,(Default.Font_1,Default.Size_1),20,2,7)
            click_button = Create_Button(Root,"Continue",(Default.Font_4,Default.Size_1),9,(lambda:button_clicked(submit_entry,Adding_Team,click_button,None,General_Option_Menu,[Var,proceedure_inquiry],"Team Creation")),Default.Color_1,Default.Color_3,20,2,8)
            global return_button
            return_button = Create_Button(Root,"Return to Main-Menu",(Default.Font_4,Default.Size_1),None,(lambda:Return_To_Main(text,True,[return_button,submit_entry,click_button,General_Option_Menu,warning,proceedure_inquiry])),Default.Color_1,Default.Color_3,7,0,17)
        else:
            Warning_Configuration(warning,"You are not allowed to add while operating side-functions")
Root.mainloop()