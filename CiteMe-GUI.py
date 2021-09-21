# Created by the Four Corners team for Hack the North 2021. This is the GUI for the CiteMe programme.
# Integration with the main algorithm is still needed

#CiteMe GUI was created by Johann Maldonado

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

window = tk.Tk()
window.title("Welcome to CiteMe")

# def erase_entries:


def generate_references(intext, references):
    intext_citation = intext
    references_citation = references
    intext_scroll.insert(tk.END, intext_citation)
    references_scroll.insert(tk.END, references_citation)


def button_clicked():
    bookname = book_name.get()
    return bookname



book_frame = ttk.LabelFrame(window, text="Publication Information")
book_frame.grid(column=0, row=0, padx=10, pady=10)

book_name = tk.StringVar()
book_title_entry = ttk.Entry(book_frame, width=50, textvariable=book_name)
book_title_entry.insert(0, "Book Title")
book_title_entry.grid(column=0, row=0)

edition_name = tk.StringVar()
edition_title_entry = ttk.Entry(book_frame, width=20, textvariable=edition_name)
edition_title_entry.insert(0, "Edition")
edition_title_entry.grid(column=1, row=0)

publisher_name = tk.StringVar()
publisher_title_entry = ttk.Entry(book_frame, width=50, textvariable=publisher_name)
publisher_title_entry.insert(0, "Publisher")
publisher_title_entry.grid(column=0, row=1, sticky=tk.W)

year = tk.StringVar()
year_entry = ttk.Entry(book_frame, width=20, textvariable=year)
year_entry.insert(0, "Year")
year_entry.grid(column=1, row=1, sticky=tk.W)

optional_frame = ttk.LabelFrame(window, text="Optional")
optional_frame.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

doi = tk.StringVar()
doi_entry = tk.Entry(optional_frame, width=50, textvariable=doi)
doi_entry.insert(0, "DOI")
doi_entry.grid(column=0, row=0, sticky=tk.W)

description = tk.StringVar()
description_entry = tk.Entry(optional_frame, width=50, textvariable=description)
description_entry.insert(0, "Description")
description_entry.grid(column=0, row=1, sticky=tk.W)


author_frame = ttk.LabelFrame(window, text="Author")
author_frame.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

forename = tk.StringVar()
forename_entry = tk.Entry(author_frame, width=50, textvariable=forename)
forename_entry.insert(0, "First Name")
forename_entry.grid(column=0, row=0, sticky=tk.W)

middle_name = tk.StringVar()
middle_name_entry = tk.Entry(author_frame, width=20, textvariable=middle_name)
middle_name_entry.insert(0, "Middle Name")
middle_name_entry.grid(column=1, row=0, sticky=tk.W)

surname = tk.StringVar()
surname_entry = tk.Entry(author_frame, width=50, textvariable=surname)
surname_entry.insert(0, "Last Name")
surname_entry.grid(column=0, row=1, sticky=tk.W)


intext_frame = ttk.LabelFrame(window, text="In-text citation")
intext_frame.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky=tk.W)

scrollW = 50
scrollH = 1

intext_scroll = scrolledtext.ScrolledText(intext_frame, width=scrollW, height=scrollH, wrap=tk.WORD)
intext_scroll.grid(column=0, row=0, columnspan=2)

references_frame = ttk.LabelFrame(window, text="Reference")
references_frame.grid(column=0, row=4, columnspan=2, padx=10, pady=10, sticky=tk.W)

scrollW = 50
scrollH = 1

references_scroll = scrolledtext.ScrolledText(references_frame, width=scrollW, height=scrollH, wrap=tk.WORD)
references_scroll.grid(column=0, row=0, columnspan=2)

button_frame = ttk.LabelFrame(window, text="")
button_frame.grid(column=0, row=5, columnspan=2, padx=10, pady=20, sticky=tk.W)

generate_button = ttk.Button(button_frame, text="Generate Citation", command=button_clicked)
generate_button.grid(row=5, column=0, sticky=tk.E)

window.mainloop()
