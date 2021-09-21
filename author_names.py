"""
A helper function designed to enable our program to accept a variable number of author names. Names must be identified with the following abbreviations: fn (first name), mn (middle name), ln (last name). 
Names are passed to the function in order from first author to last author, in the following form:
author_names(fn1 = '', mn1 = '', ln1 = '', fn2 = '', ln2 = '') 
Middle and / or first names can be omitted. Last names cannot be omitted. If no names are passed to the argument, the value False will be returned.
"""

def author_names(**names):
    # Set up variables
    authors_list = ''
    num_authors = 0

    # How many authors in citation?
    for key in names:
        if 'ln' in key:
            num_authors += 1

    # One author
    if num_authors == 1:
        ln = "ln1"
        mn = "mn1"
        fn = "fn1"
        if ln in names:
            if fn in names:
                finitial = names[fn][0:1]
                name = names[ln] + ", " + finitial + "."
                if mn in names:
                    minitial = names[mn][0:1]
                    name = names[ln] + ", " + finitial + ". " + minitial + "."
            else:
                name = names[ln]
            authors_list += name
        else:  # There are no names passed as arguments
            return False

    # 2 to twenty authors
    elif 1 < num_authors < 21:
        for auth_index in range(1, num_authors + 1):
            ln = "ln" + str(auth_index)
            mn = "mn" + str(auth_index)
            fn = "fn" + str(auth_index)
            if ln in names:
                if fn in names:
                    finitial = names[fn][0:1]
                    name = names[ln] + ", " + finitial + "."
                    if mn in names:
                        minitial = names[mn][0:1]
                        name = names[ln] + ", " + finitial + ". " + minitial + "."
                else:
                    name = names[ln] + "."
                # If this is the last author, add &
                if auth_index == num_authors:
                    authors_list += "& " + name
                else:
                    authors_list += name + ", "
            else:
                break
        # More than twenty authors
    elif num_authors > 20:
        # Add first 19 names
        for auth_index in range(1, 20):
            ln = "ln" + str(auth_index)
            mn = "mn" + str(auth_index)
            fn = "fn" + str(auth_index)
            if ln in names:
                if fn in names:
                    finitial = names[fn][0:1]
                    name = names[ln] + ", " + finitial + "."
                    if mn in names:
                        minitial = names[mn][0:1]
                        name = names[ln] + ", " + finitial + ". " + minitial + "."
                else:
                    name = names[ln] + "."
                # Add the name to the list
                authors_list += name + ", "
        # Add ellipses
        authors_list += ". . . "
        # Add last author
        ln = "ln" + str(num_authors)
        mn = "mn" + str(num_authors)
        fn = "fn" + str(num_authors)
        if ln in names:
            if fn in names:
                finitial = names[fn][0:1]
                name = names[ln] + ", " + finitial + "."
                if mn in names:
                    minitial = names[mn][0:1]
                    name = names[ln] + ", " + finitial + ". " + minitial + "."
            else:
                name = names[ln]
            # Add the name to the list
            authors_list += name
    else:  # There were no authors names entered
        return False
    return authors_list
