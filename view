
from tkinter import *
from tkinter import messagebox
import controller
import numpy as np



MAX_NUMBER_OF_CONFIGS = 10
MAX_NUMBER_OF_ELEMENTS = 5


class View():
        
    list_of_entries_forces = list()
    list_of_sum_forces = list()
    

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.current_config = IntVar()
        self.current_TWS = DoubleVar()
        self.current_TWA = DoubleVar()
        self.current_BS  = DoubleVar()
        self.current_Heel = DoubleVar()
        self.current_Leeway = DoubleVar()
        self.maVarQuiChange = DoubleVar()
        self.element_load_entry_widget = [None] * MAX_NUMBER_OF_ELEMENTS
        self.create_vpp_base()
        

    def create_vpp_base(self):
        self.create_top_bar()
        self.create_left_elements_loader()
        self.create_right_results_matrix()
        self.create_bottom_results_sum()
        self.create_bottom_run()


    def create_top_bar(self):
        topbar_frame = Frame(self.parent, height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=2, padx=5, pady=5)

        Label(topbar_frame, text='   TWS :').grid(row=0, column=0)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_CONFIGS - 1, width=5,
                textvariable=self.current_TWS, command=self.on_VAR_changed).grid(row=0, column=1)

        Label(topbar_frame, text='   TWA :').grid(row=1, column=0)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_CONFIGS - 1, width=5,
                textvariable=self.current_TWA, command=self.on_VAR_changed).grid(row=1, column=1)

        Label(topbar_frame, text='   BS :').grid(row=0, column=5)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_CONFIGS - 1, width=5,
                textvariable=self.current_BS, command=self.on_VAR_changed).grid(row=0, column=6)

        Label(topbar_frame, text='   Heel :').grid(row=1, column=5)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_CONFIGS - 1, width=5,
                textvariable=self.current_Heel, command=self.on_VAR_changed).grid(row=1, column=6)

        Label(topbar_frame, text='   Leeway :').grid(row=0, column=7)
        Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_CONFIGS - 1, width=5,
                textvariable=self.current_Leeway, command=self.on_VAR_changed).grid(row=0, column=8)



    
    def create_left_elements_loader(self):

        left_frame = Frame(self.parent)
        left_frame.grid(row=10, column=0, columnspan=6, sticky=W + E + N + S)

        Label(left_frame, text='Eléments').grid(row=0, column=0)
        Label(left_frame, text='Stab carene').grid(row=1, column=0, padx=10, pady=3)
        Label(left_frame, text='Dyn carene').grid(row=2, column=0, padx=10, pady=3)
        Label(left_frame, text='Voile').grid(row=3, column=0, padx=10, pady=3)
        Label(left_frame, text='Dérive').grid(row=4, column=0, padx=10, pady=3)
        Label(left_frame, text='Safran').grid(row=5, column=0, padx=10, pady=3)


        """
        open_file_icon = PhotoImage(file='images/openfile.gif')
        for i in range(MAX_NUMBER_OF_ELEMENTS):
            open_file_button = Button(left_frame, image=open_file_icon,
                                      command=self.on_open_file_button_clicked(i))
            open_file_button.image = open_file_icon
            open_file_button.grid(row=i+1, column=0,  padx=0, pady=0)
            self.element_load_entry_widget[i] = Entry(left_frame)
            self.element_load_entry_widget[i].grid(row=i+1, column=4, padx=7, pady=4)
        """
   

    def create_right_results_matrix(self):

        right_frame = Frame(self.parent)
        right_frame.grid(row=10, column=7, columnspan=6, sticky=W + E + N + S)

        Label(right_frame, text='FX').grid(row=0, column=0)
        Label(right_frame, text='FY').grid(row=0, column=1)
        Label(right_frame, text='FZ').grid(row=0, column=2)
        Label(right_frame, text='MX').grid(row=0, column=3)
        Label(right_frame, text='MY').grid(row=0, column=4)
        Label(right_frame, text='MZ').grid(row=0, column=5)

        for i in range(MAX_NUMBER_OF_ELEMENTS):
            for j in range(6):
                temp_entry = Entry(right_frame, width=10)
                temp_entry.grid(row=1+i, column=j, padx=10, pady=4)
                self.list_of_entries_forces.append(temp_entry)

        """
        Entry(right_frame, width=10).grid(row=2, column=0, padx=10, pady=4)
        Entry(right_frame, width=10).grid(row=2, column=1, padx=10, pady=4)
        Entry(right_frame, width=10).grid(row=2, column=2, padx=10, pady=4)
        Entry(right_frame, width=10).grid(row=2, column=3, padx=10, pady=4)
        Entry(right_frame, width=10).grid(row=2, column=4, padx=10, pady=4)
        self.entry = Entry(right_frame, width=10)
        self.entry.grid(row=2, column=5, padx=10, pady=4)
        """
                


    def create_bottom_results_sum(self):

        results_frame = Frame(self.parent)
        results_frame.grid(columnspan=12, sticky=W + E + N + S)

        Label(results_frame, text='Somme').grid(row=0, column=0)


        for i in range(6):
            temp_entry = Entry(results_frame, width=10)
            temp_entry.grid(row=0, column=i+1, padx=10, pady=4)
            self.list_of_sum_forces.append(temp_entry)




    def create_bottom_run(self):

        bottom_run_frame = Frame(self.parent)
        bottom_run_frame.grid(columnspan=12, sticky=W + E + N + S)

        run_button = Button(bottom_run_frame, text='RUN',
                            command=self.on_run_button_clicked)
        run_button.grid(row=0, column=0,  padx=10, pady=4)



    def on_run_button_clicked(self):
        #a = self.controller.model[0].force_fx
        #messagebox.showinfo('MsgBox', a)
        self.update_variables()
        self.update_forces_matrix()
        self.update_sum_forces(MAX_NUMBER_OF_ELEMENTS)


    def on_VAR_changed(self):
        pass


    def update_variables(self):
        self.controller.model.cw_tws = self.current_TWS.get()
        self.controller.model.cw_twa = self.current_TWA.get()
        self.controller.model.cn_bs = self.current_BS.get()
        self.controller.model.cn_leeway = 0.
        self.controller.model.cn_heel = 0.
        


    def update_forces_matrix(self):

        for i in range(MAX_NUMBER_OF_ELEMENTS):
            self.controller.model[i].update_forces(self.controller.model.cw_tws,
                                                   self.controller.model.cw_twa,
                                                   self.controller.model.cn_bs,
                                                   self.controller.model.cn_heel,
                                                   self.controller.model.cn_leeway)

        for i in range(MAX_NUMBER_OF_ELEMENTS): #i=[0,1]
            for j in range(6): #j=[0,1,2,3,4,5]
                self.list_of_entries_forces[6*i+j].delete(0,END)
                self.list_of_entries_forces[6*i+j].insert(0,self.controller.model[i].vec6_torseur_ab[j])
                
    # pour label(i) de (0) à (nbelts*6 -1)
    # mettre à jour les valeurs des labels
    # avec force(j) de l'elt(i)
    # Idée : les elements ont un champ de type array qui contient les efforts dans repere ab
        pass



    def update_sum_forces(self, nb_elements):

        self.controller.model.update_sum_of_forces(nb_elements)

        for i in range(6):
            self.list_of_sum_forces[i].delete(0,END)
            self.list_of_sum_forces[i].insert(0,self.controller.model.sum_of_forces[i])


def main(controller):
    root = Tk()
    root.title(">>> VyPyPy <<<")
    View(root, controller)
    root.mainloop()


def init_new_vpp():
    initial_data = controller.Controller()
    main(initial_data)



if __name__ == "__main__":
    init_new_vpp()


