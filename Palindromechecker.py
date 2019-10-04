"""
Rasmus Hén
Windows 10
"""

#Import Tkinter
import tkinter
import tkinter.messagebox

#Creates the main window, text label and an input box
main_window = tkinter.Tk()
label_message = "Välkommen till Palindromkollen!"
main_label = tkinter.Label(main_window, text = label_message, font = 30, \
                           height = 5, width = 41, bg = "#0AABBA")
user_input = tkinter.Entry(main_window, width = 73)

#Calls the different functions to create the window
def main():
    create_main_window()
    create_main_frame()
    
    tkinter.mainloop()

#Main window
def create_main_window():
    main_window.geometry("450x330+100+100")
    main_window.title("INP - Palindromdetektor")

#Calls the widgets that are to be displayed in the main window
def create_main_frame():
    main_label.grid(row = 0, rowspan = 1, column = 0, columnspan = 3)
    create_input_box()
    create_buttons()

#Defines where the input box is on the main window and imports text into it
def create_input_box():
    user_input.insert(0, "Skriv in den text du vill kontrollera här...")
    user_input.grid(row = 1, rowspan = 1, column = 0, columnspan = 3, pady = 10, padx = (3,0), sticky = "w")

#Creates buttons that each calls a different function. Defines where those buttons are to be diplayed on the main window
def create_buttons():
    evaluate_button = tkinter.Button(main_window, text = "Evaluera texten", command = action_evaluate, bg = "#05676E", width = 20, pady = 3)
    instruction_button = tkinter.Button(main_window, text = "Instruktioner", command = action_instruction, bg = "#05676E", width = 20, pady = 3)
    save_button = tkinter.Button(main_window, text = "Spara Palindrom", command = action_save, bg = "#05676E", width = 20, pady = 3)
    exit_button = tkinter.Button(main_window, text = "Avsluta", command = action_exit, bg = "#05676E", width = 20, pady = 3)
    
    evaluate_button.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, pady = 5, padx = 10, sticky = "e")
    instruction_button.grid(row = 3, rowspan = 1, column = 0, columnspan = 1, pady = 5, padx = 10, sticky = "w")
    save_button.grid(row = 4, rowspan = 1, column = 0, columnspan = 1, pady = 5, padx = 10, sticky = "w")
    exit_button.grid(row = 5, rowspan = 1, column = 0, columnspan = 1, pady = 5, padx = 10, sticky = "w")

#Evaluates if the user's input is a palindrome
def action_evaluate():
    giltiga_tecken = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n",\
                  "o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö",\
                  "1","2","3","4","5","6","7","8","9")
    palindrome = user_input.get()
    palindrome = palindrome.lower()
    
    #Removes all unwanted characters
    cor_palindrome = []
    for i in palindrome:
        if i in giltiga_tecken:
            cor_palindrome += i
            
    #Makes a new list of cor_palindrome but backwards
    rev_palindrome = []
    count = len(cor_palindrome) - 1
    while count >= 0:
        rev_palindrome.append(cor_palindrome[count])
        count -= 1

    #Compares the user's input (minus unwanted characters) with the user's input (minus unwanted characters) backwards
    if cor_palindrome == rev_palindrome:
        label_message = "Ja, det är en palindrom."
        main_label.config(bg = "#AEE239", text = label_message)
        return cor_palindrome
    else:
        label_message = "Nej, det är inte en palindrom."
        main_label.config(bg = "#C21A01", text = label_message)
        
#Creates a messagebox with instructions
def action_instruction():
    tkinter.messagebox.showinfo("Instruktioner", "Välkommen till Palindromkollen!\nSkriv in det ord du tror är en palindrom i textrutan och tryck på Evaluera för att se om det är rätt\n" \
                                "Om du hittar en palindrom du gillar kan du spara den genom att trycka på Spara Palindrom\nLycka till!")

#Calls the function action_evaluate to evaluate if the output is valid and if so save it in a .txt-file
def action_save():
    try:
        save_text = action_evaluate()
        if save_text == None:
            tkinter.messagebox.showinfo("Felmeddelande", "Du kan bara spara palindrom")
        else:
            save_text = ''.join(save_text)
            save_file = open("Palindromlista.txt", "a")
            save_file.write(save_text + "\n")
            save_file.close()
            tkinter.messagebox.showinfo("Sparat", save_text + " är sparat i Palindromlista.txt")
    except IOError:
        tkinter.messagebox.showinfo("Felmeddelande", "Det går inte att hitta filen")
    
#Creates a messagebox with a yes/no-function, if yes: kill program   
def action_exit():
    if tkinter.messagebox.askyesno("Avsluta palindromdetektor", "Vill du verkligen avsluta?"):
        main_window.destroy()
    
#Calls the main function and starts the program  
main()
