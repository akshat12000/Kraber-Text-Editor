# Use shift + alt + down arrow key in windows to copy the line below it
# Hold alt and with mouse to use it as multiple cursor  
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter.constants import NONE, TRUE
from typing import Counter

main_window=tk.Tk()
main_window.geometry('1200x800') # this will set the default size of apllication window
main_window.title('Kraber Text Editor')
main_window.wm_iconbitmap('myicon.ico') # this is to give icon to your application

# importing icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
bold_icon=tk.PhotoImage(file='icons2/bold.png')
italic_icon=tk.PhotoImage(file='icons2/italic.png')
underline_icon=tk.PhotoImage(file='icons2/underline.png')
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')

#------------------Start of MainMenu--------------------#

main_menu=tk.Menu(main_window)

### File 
file=tk.Menu(main_menu,tearoff=0)

### Edit
edit=tk.Menu(main_menu,tearoff=0)

### View
view=tk.Menu(main_menu,tearoff=0)

### Color Theme
color_theme=tk.Menu(main_menu,tearoff=0)
theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_icon,dark_icon,red_icon,night_blue_icon,monokai_icon)
color_dict={
    'Light(Default)':('#000000','#ffffff'), # (fg color,bg color)
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#ffd700','#1a1a2e'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Night Blue':('#ededed','#6b9dc2'),
    'Monokai':('#474747','#d3b774')
}

# Cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)

#------------------END of MainMenu----------------------#

#------------------Start of ToolBar---------------------#

tool_bar=ttk.Label(main_window)
tool_bar.pack(side=tk.TOP,fill=tk.X) # this will place it on top and fill it completely horizontally!!
print(tk.font.families()) # this will print all the available fonts in the computer!!
print(type(tk.font.families())) # this will print 'tuple'

### Font Box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,textvariable=font_family,width=35,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

### Size Box
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,textvariable=size_var,width=5,state='readonly')
size_box['value']=tuple(range(1,101))
size_box.current(11)
size_box.grid(row=0,column=1,padx=5)

### Bold Button
Bold_btn=ttk.Button(tool_bar,image=bold_icon,compound=tk.CENTER)
Bold_btn.grid(row=0,column=3,padx=5)

### Italic Button
Italic_btn=ttk.Button(tool_bar,image=italic_icon,compound=tk.CENTER)
Italic_btn.grid(row=0,column=4,padx=5)

### Underline Button
Underline_btn=ttk.Button(tool_bar,image=underline_icon,compound=tk.CENTER)
Underline_btn.grid(row=0,column=5,padx=5)

## Font Color Button
Font_Color_btn=ttk.Button(tool_bar,image=font_color_icon,compound=tk.CENTER)
Font_Color_btn.grid(row=0,column=6,padx=5)

## Align Left Button
Align_Left_btn=ttk.Button(tool_bar,image=align_left_icon,compound=tk.CENTER)
Align_Left_btn.grid(row=0,column=7,padx=5)

## Align Center Button
Align_Center_btn=ttk.Button(tool_bar,image=align_center_icon,compound=tk.CENTER)
Align_Center_btn.grid(row=0,column=8,padx=5)

## Align Right Button
Align_Right_btn=ttk.Button(tool_bar,image=align_right_icon,compound=tk.CENTER)
Align_Right_btn.grid(row=0,column=9,padx=5)

#------------------END of ToolBar-----------------------#

#------------------Start of TextEditor------------------#

text_editor=tk.Text(main_window)
text_editor.config(wrap='word',relief=tk.FLAT) # whenever you are at last line of the editor then the whole word your are writing moves in newline

## Scroll Bar
scroll_bar=ttk.Scrollbar(main_window,orient='vertical')
text_editor.focus_set() # this is to place cursor at fix point by default
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview) # this is to link the text_editor and scroll bar
text_editor.config(yscrollcommand=scroll_bar.set) # this is to tell that scroll bar will be vertical

## Font Family and Font Size functionality
def_font='Arial'
def_size=12

def font_changer(main_window): # we have pass an argument due to 'bind' function!!
    global def_font ,def_size
    def_font= font_family.get()
    text_editor.configure(font=(def_font,def_size))

def size_changer(event=None):  # It is not neccessary to write main_window as argument
    global def_font ,def_size
    def_size=size_var.get()
    text_editor.configure(font=(def_font,def_size))

font_box.bind('<<ComboboxSelected>>',font_changer) # this is to apply the fonts changed by the user on the text!!
size_box.bind('<<ComboboxSelected>>',size_changer) # this is to apply the changed size given by the user on the text!!

## Button Functionality
print(tk.font.Font(font=text_editor['font']).actual()) # this will give the default text property of text_editor in dictionary format

# Bold Button Functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']!='bold':
        text_editor.configure(font=(def_font,def_size,'bold'))
    else:
        text_editor.configure(font=(def_font,def_size,'normal'))
Bold_btn.config(command=change_bold)

# Italic Button Functionality
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']!='italic':
        text_editor.configure(font=(def_font,def_size,'italic'))
    else:
        text_editor.configure(font=(def_font,def_size,'normal'))
Italic_btn.config(command=change_italic)

# Underline Button Functionality
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(def_font,def_size,'underline'))
    else:
        text_editor.configure(font=(def_font,def_size,'normal'))
Underline_btn.config(command=change_underline)

## Font color functionality
def color_changer():
    color_var=tk.colorchooser.askcolor() # this will create a window for user where he/she can pick the color
    print(color_var) # this will print a tuple which contains--> ((R,G,B),hexadecimal_code)
    text_editor.configure(fg=color_var[1]) # since the hexadecimal value of color is present at index '1'
Font_Color_btn.config(command=color_changer)

## Align Button Functionalities
# Align Left 
def align_left():
    text_var=text_editor.get(1.0,'end') # this will take all the text from line one to the end !!
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_var,'left')
Align_Left_btn.config(command=align_left)

# Align Center
def align_center():
    text_var=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_var,'center')
Align_Center_btn.config(command=align_center)

# Align Right
def align_right():
    text_var=text_editor.get(1.0,'end') 
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_var,'right')
Align_Right_btn.config(command=align_right)

text_editor.configure(font=('Arial',12))

#------------------END of TextEditor--------------------#

#------------------Start of StatusBar-------------------#

status_bar=ttk.Label(main_window,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

## character and word counter which will diplay on the status bar
text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        word=len(text_editor.get(1.0,'end-1c').split(" ")) # "end-1c" will eliminate the count of '\n' 
        char=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Character: {char}    Words: {word}')
    text_editor.edit_modified(False) # this is done to display the changes in words and character whenever user types something
# if this statement is not included then it will only update the word and characters once and will show only '1'(char) and '1'(word)

text_editor.bind('<<Modified>>',changed)

#------------------END of StatusBar---------------------#

#------------------Start of MainMenu Functionality------#

### Global variable for the file path
url=''

## New functionality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

## Open Functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('Text File','*.txt'),('All Files','*.*')))
    # this will open the window where user will select his/her file by default it will open the cwd and will give option to open text file
    # as separate entity and all other files as another separate entity
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    else:
        messagebox.showinfo('Success!','File opened successfully')
    main_window.title(os.path.basename(url)) # this will change the name of window as the opened file name

## Save functionality
def save_file(event=None):
    global url
    try:
        if url: # if file already exists!!
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else: # if file doesnot exists!!
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))    
            content2=str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except Exception:
        return

## Save As functionality
def save_as_file():
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))    
        content=str(text_editor.get(1.0,tk.END))
        url.write(content)
        url.close()
    except Exception:
        return

## Exit functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning!','Do you want to save the changes in your file?')
            if mbox is True:
                if url:
                    content=str(text_editor.get(1.0,tk.END))
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                    main_window.destroy() # this will exit the window
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_window.destroy()
            elif mbox is False:
                main_window.destroy()
            # we have written conditions like this so that when user presses the cancel button then the window should not get exited
        else:
            main_window.destroy() 
    except Exception:
        return
### File commands
# New 
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file) # if we do not use this 'compound=tk.LEFT' then icon and Label will overlap each other!!
# By the use of 'accelarator="Ctrl+N"' we can provide the text after the label
# Open
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
# Save
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
# Save As
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)
# Exit
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

## Find Functionality
def find_and_replace(event=None):
    find=tk.Toplevel()
    find.geometry('450x250+500+200') # the plus sign indicates we want to shift the window  
    find.title('Find And Replace')
    find.wm_iconbitmap('find.ico')
    find.resizable(0,0) # this restricts the user to resize the window
    
    # LabelFrame
    lab=ttk.Labelframe(find,text='Enter the Entries')
    lab.pack(pady=20)
    
    # Labels
    labf=ttk.Label(lab,text='Find: ')
    labf.grid(row=0,column=0,padx=5,pady=5)
    
    labr=ttk.Label(lab,text='Replace: ')
    labr.grid(row=3,column=0,padx=5,pady=5)

    # Entry boxes
    fi_var=tk.StringVar()
    fi_entry=ttk.Entry(lab,width=25,textvariable=fi_var)
    fi_entry.grid(row=1,column=0,padx=5,pady=5)

    re_var=tk.StringVar()
    re_entry=ttk.Entry(lab,width=25,textvariable=re_var)
    re_entry.grid(row=4,column=0,padx=5,pady=5)

    # Find Button
    def find_func():
        word=str(fi_var.get())
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True: # seaching for all matching string
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END) # seaching for matching string
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c' 
                text_editor.tag_add('match',start_pos,end_pos) # adding the tag
                matches+=1 # match count
                start_pos=end_pos # updating the search range
                text_editor.tag_config('match',foreground='red',background='yellow') # setting the display for matched items 
    
    fi_btn=ttk.Button(lab,text='Find',compound=tk.CENTER,command=find_func)
    fi_btn.grid(row=2,column=0,padx=10,pady=5)

    # Replace Button
    def replace_func():
        word=str(fi_var.get())
        replace_text=str(re_var.get())
        content=text_editor.get('1.0',tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete('1.0',tk.END)
        text_editor.insert('1.0',new_content)

    re_btn=ttk.Button(lab,text='Replace',compound=tk.CENTER,command=replace_func)
    re_btn.grid(row=5,column=0,padx=10,pady=5)

    find.mainloop()
### Edit commands
# Cut
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda :text_editor.event_generate("<Control x>"))
# Copy
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda :text_editor.event_generate("<Control c>"))
# Paste
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda :text_editor.event_generate("<Control v>"))
# Clear All
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda : text_editor.delete(1.0,tk.END))
# Find
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_and_replace)

### View commands
show_toolbar=tk.BooleanVar()
show_statusbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget() # it will remove the tool bar!!
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget() # it will remove the status bar!!
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

# Tool Bar
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
# Status Bar
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

### Color theme commands
def change_theme():
    color=str(theme_choice.get())
    color_tuple=color_dict.get(color)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(fg=fg_color,bg=bg_color)

counter=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[counter],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    counter+=1

#------------------END of MainMenu Functionality--------#

main_window.config(menu=main_menu)

### Adding shortcut keys
main_window.bind('<Control-n>',new_file)
main_window.bind('<Control-o>',open_file)
main_window.bind('<Control-s>',save_file)
main_window.bind('<Control-Alt-s>',save_as_file)
main_window.bind('<Control-q>',exit_func)
main_window.bind('<Control-f>',find_and_replace)

main_window.mainloop()