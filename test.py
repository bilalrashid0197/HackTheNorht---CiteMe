import numpy as np
from author_names import *
from citations import *

print("          Testing book citations", "\n", "#########################################")
print("All info present:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing Author middle name:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", ln1="Maldonado"), "\n")

print("Missing Author last name:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro"), "\n")

print("Missing book title:")
print(citing_books(publisher="Four Corners", publishing_year="2021", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing publisher:")
print(citing_books(book_title="HacktheNorth 2021", publishing_year="2021", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing publishing year:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing DOI:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing alternate description:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing alternate description:")
print(citing_books(publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Tests for multiple authors:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Madison", mn1="Eleanor", ln1="Chapel",
                   fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                   fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"), "\n")

print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Madison", mn1="Eleanor", ln1="Chapel",
                   fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                   fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin",
                   fn5="Hack", mn5="The", ln5="North", fn6="Madison", mn6="Eleanor", ln6="Chapel",
                   fn7="Johann", mn7="Alejandro", ln7="Maldonado",
                   fn8="Bilal", ln8="Rashid", ln9="Oh", fn9="Sumin",
                   fn10="Hack", mn10="The", ln10="North", fn11="Madison", mn11="Eleanor", ln11="Chapel",
                   fn12="Johann", mn12="Alejandro", ln12="Maldonado",
                   fn13="Bilal", ln13="Rashid", ln14="Oh", fn14="Sumin",
                   fn15="Hack", mn15="The", ln15="North", fn16="Madison", mn16="Eleanor", ln16="Chapel",
                   fn17="Johann", mn17="Alejandro", ln17="Maldonado",
                   fn18="Bilal", ln18="Rashid", ln19="Oh", fn19="Sumin",
                   fn20="Hack", mn20="The", ln20="North", ln21="Last", mn21="Middle", fn21="First"), "\n")

### Tests for web page citation ###
print("        Testing web page citations", "\n", "#########################################")
print("All info present:")
print(citing_webpage(publishing_year="2021", publishing_month="September", publishing_day="18",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"))

print("Missing date components:")
print("    - Month: ")
print(citing_webpage(publishing_year="2021", publishing_day="18",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")
print("    - Day: ")
print(citing_webpage(publishing_year="2021", publishing_month="September",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("    - Year: ")
print(citing_webpage(publishing_month="September", publishing_day="18",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("Missing title:")
print(citing_webpage(publishing_year="2021", publishing_month="September", publishing_day="18",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021",
                     alternate_description="An alternate description for the source", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("Missing webpage name:")
print(citing_webpage(publishing_year="2021", publishing_month="September", publishing_day="18",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     url="https://github.com/Mach-2/HtN2021",
                     alternate_description="An alternate description for the source", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("Missing url:")
print(citing_webpage(publishing_year="2021", publishing_month="September", publishing_day="18",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     webpage_name="Four Corners", fn1="Madison", mn1="Eleanor", ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("Author and Webpage name the same:")
print(citing_webpage(publishing_year="2021", publishing_month="September", publishing_day="18",
                     title_of_webpage="How to Win a Hackathon! (or at least have fun)",
                     webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021", ln1="Four Corners"), "\n")

print("Missing date and title:")
print(citing_webpage(webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021",
                     alternate_description="An alternate description for the source", fn1="Madison", mn1="Eleanor",
                     ln1="Chapel",
                     fn2="Johann", mn2="Alejandro", ln2="Maldonado", fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),
      "\n")

print("Missing author, date, and title:")
print(citing_webpage(webpage_name="Four Corners", url="https://github.com/Mach-2/HtN2021",
                     alternate_description="An alternate description for the source"), "\n")

### Tests for journal article citation ###
print("        Testing journal citations", "\n", "#########################################\n")
print("All info present:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"), "\n")

print("Missing year:")
print(citing_journal(article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"), "\n")

print("Missing title:")
print(citing_journal(publishing_year="2021",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"), "\n")

print("Missing journal:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing page start:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing page end:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing volume:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing issue:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing alt description:")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing DOI: ")
print(citing_journal(publishing_year="2021", article_title="How to Win at Hackathons",
                     journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")

print("Missing year and title:")
print(citing_journal(journal_name="Hack the North Methods and Reviews", page_start="100", page_end="150", volume="6",
                     issue="12", alt_description="An alternate description", DOI="https://github.com/Mach-2/HtN2021/",
                     fn1="Madison", mn1="Eleanor", ln1="Chapel", fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                     fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"),"\n")