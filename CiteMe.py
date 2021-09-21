"""This is a command-line version of the CiteMe program, developed by the Four Corners team for Hack the North 2021.
This program requests user-input and generates an APA-7 formatted citation. Currently, it works for book, Ebook,
and web resources, with additional functionality planned for future implementations! """

from citations import *
from author_names import *

ref_list = ""
citations = True

### Introduce the CiteMe program
print("Welcome to CiteMe! Please follow the prompts to generate your APA7-compliant citations and reference list.")

while citations:
    # Determine the type of resource:
    reference = None
    while reference not in ("1", "2", "3"):
        reference = input("Please specify the type of source you are referencing. Options are:\n    1. Book\n    2. Website\n    3. Journal Article\n "
                      "Please enter a number to select your option\n")
        if not reference:
            print("Whoops, please try again!")


    # Get inputs for a book

    if reference == "1":
        # Initialize variables to remove values from previous citations
        authDict = {}
        title = False
        pub = False
        pub_year = False
        doi = False
        # Take author names and append to dictionary?
        auth_in = True
        authNum = 0
        # Get author names
        while auth_in is True:
            authNum += 1
            name = input("Please provide the author name. If the author is unknown, press enter to skip:\n")
            fn = "fn" + str(authNum)
            mn = "mn" + str(authNum)
            ln = "ln" + str(authNum)
            split = name.split()
            if len(split) == 0:
                print("Authors unknown, understood!")
                auth_in = False;
                break
            elif len(split) == 1:
                authDict[ln] = split[0]
            elif len(split) == 2:
                authDict[fn] = split[0]
                authDict[ln] = split[1]
            elif len(split) == 3:
                authDict[fn] = split[0]
                authDict[mn] = split[1]
                authDict[ln] = split[2]
            elif len(split) > 3:
                print(
                    "Sorry, we're still working out some bugs and can only accept names in the form 'Firstname Middlename Lastname' for now! Please enter this name again")
                continue
            # More authors?
            more = None
            while more not in ('y', 'n'):
                more = input("Are there more authors? y/n\n")
                if not more:
                    print("Whoops, please try again!\n")
            if more == 'n':
                auth_in = False

        # Capitalize author names
        authDict = dict((k, v.capitalize()) for k,v in authDict.items())

        # Get the rest of the info
        # Title and alternate description
        title = input("Please provide the book title. If the title is unknown, press enter to skip:\n")
        alt = False
        if not title:
            alt = input("In liu of a title, please provide a description of your resource:\n")
        # Publisher
        pub = input("Please provide the publisher name. This information is required to generate a citation!\n")
        # Publishing year
        pub_year = input(
            "Please provide the year of publication. If the publication date is unknown, press enter to skip:\n")
        # DOI
        doi = input("Please provide the DOI if your resource is available online. If the DOI is unknown or unavailable, "
                    "press enter to skip: \n")

        # Add the reference to the list
        ref_list += citing_books(book_title=title, publisher=pub, publishing_year=pub_year, DOI=doi,
                                 alternate_description=alt, **authDict) + "\n"
        print("Citation added!")
        # Check for more citations
        more = None
        while more not in ('y', 'n'):
            more = input("Would you like to add another reference? y/n\n")
            if not more:
                print("Sorry, please enter your selection again: \n")
        if more == 'n':
            citations = False
        ### End of Book Citation

    # Get inputs for a web citation
    elif reference == "2":
        authDict = {}
        title = False
        pub_year = False
        pub_month = False
        pub_day = False
        siteName = False
        url = False
        alt = False
        # Take author names and append to dictionary?
        authType = input("Is your web page written by one or more authors, or by an organization?\n    1. One or more "
                         "authors\n    2. An organization "
                         "Please enter a number to select your option\n")
        if authType == "2":  # This makes no actual difference to the inputs, but it's maybe nice for the user. And I
            # guess I only need to account for ln1
            name = input("Please provide the name of the organization that wrote this web page. If the organization is "
                         "unknown, press enter to skip\n")
            authDict = {"ln1": name}
        elif authType == "1":  # Work written by one or more authors
            auth_in = True
            authNum = 0
            while auth_in is True:
                authNum += 1
                name = input("Please provide the author name. If the author is unknown, press enter to skip:\n")
                fn = "fn" + str(authNum)
                mn = "mn" + str(authNum)
                ln = "ln" + str(authNum)
                split = name.split()
                if len(split) == 0:
                    print("Authors unknown, understood!")
                    auth_in = False
                    break
                elif len(split) == 1:
                    authDict[ln] = split[0]
                elif len(split) == 2:
                    authDict[fn] = split[0]
                    authDict[ln] = split[1]
                elif len(split) == 3:
                    authDict[fn] = split[0]
                    authDict[mn] = split[1]
                    authDict[ln] = split[2]
                elif len(split) > 3:
                    print(
                        "Sorry, we're still working out some bugs and can only accept names in the form 'Firstname "
                        "Middlename Lastname' for now!")
                # More authors?
                more = None
                while more not in ('y', 'n'):
                    more = input("Are there more authors? y/n\n")
                    if not more:
                        print("Sorry, please enter your selection again: \n")
                if more == 'n':
                    auth_in = False

        # Capitalize author names
        authDict = dict((k, v.capitalize()) for k,v in authDict.items())

        # Get the rest of the citation material
        # Get the rest of the info
        # Title and alternate description
        title = input("Please provide the title of your web article. If the title is unknown, press enter to skip:\n")
        if not title:
            alt = input("In liu of a title, please provide a description of your resource:\n")
        # Publisher
        siteName = input("Please provide the website name. This information is required to generate a citation!\n")
        # Publishing year
        pub_year = input(
            "Please provide the year of publication. If the publication year is unknown, press enter to skip:\n")
        if pub_year:  # If year exists, try to get more date info
            pub_month = input(
                "Please provide the month of publication, written out (i.e., 'February' instead of 'Feb' or '02'). If the month is unknown, press enter to skip:\n").capitalize()
            if pub_month:
                pub_day = input("Please provide the day of publication. If the day is unknown, press enter to skip:\n")

        # DOI
        url = input(
            "Please provide the website URL. This information is required to generate a citation!\n")

        # Add the reference to the list
        ref_list += citing_webpage(publishing_year=pub_year, publishing_day=pub_day, publishing_month=pub_month,
                                   title_of_webpage=title, webpage_name=siteName, url=url, alt=alt, **authDict)
        print("Citation added!")
        # Find out if more references are required
        more = input("Would you like to add another reference? y/n\n")
        if more == 'y':
            continue
        elif more == "n" or more == "no":
            citations = False
            break
        ### End of Web Citation


    # Get inputs for a Journal

    if reference == "3":
        # Initialize variables to remove values from previous citations
        authDict = {}
        pub_year = False
        title = False
        journal = False
        page_start = False
        page_end = False
        vol = False
        iss = False
        doi = False

        # Take author names and append to dictionary?
        auth_in = True
        authNum = 0
        # Get author names
        while auth_in is True:
            authNum += 1
            name = input("Please provide the author name. If the author is unknown, press enter to skip:\n")
            fn = "fn" + str(authNum)
            mn = "mn" + str(authNum)
            ln = "ln" + str(authNum)
            split = name.split()
            if len(split) == 0:
                print("Authors unknown, understood!")
                auth_in = False;
                break
            elif len(split) == 1:
                authDict[ln] = split[0]
            elif len(split) == 2:
                authDict[fn] = split[0]
                authDict[ln] = split[1]
            elif len(split) == 3:
                authDict[fn] = split[0]
                authDict[mn] = split[1]
                authDict[ln] = split[2]
            elif len(split) > 3:
                print(
                    "Sorry, we're still working out some bugs and can only accept names in the form 'Firstname Middlename Lastname' for now! Please enter this name again")
                continue
            # More authors?
            more = None
            while more not in ('y', 'n'):
                more = input("Are there more authors? y/n\n")
                if not more:
                    print("Whoops, please try again!\n")
            if more == 'n':
                auth_in = False

        # Capitalize author names
        authDict = dict((k, v.capitalize()) for k,v in authDict.items())

        # Get the rest of the info
        # Title and alternate description
        title = input("Please provide the title of the journal article. If the title is unknown, press enter to skip:\n")
        alt = False
        if not title:
            alt = input("In liu of a title, please provide a description of your resource:\n")
        # Journal
        journal = input("Please provide the journal name. This information is required to generate a citation!\n")
        # Volume
        vol = input("Please enter the volume number of the journal your article was published in: \n")
        # Issue
        iss = input("Please enter the issue number of the journal your article was published in: \n")
        # Page range
        page_start = input("Please provide the page range. If you don't know the page range, press enter to skip. Otherwise, please enter the page your article starts on:\n")
        if not page_start:
            print("Understood! Skipping page range entry.")
        else:
            page_end = input("And now, please provide the page your article ends on: \n")
        # Publishing year
        pub_year = input(
            "Please provide the year of publication. If the publication date is unknown, press enter to skip:\n")
        # DOI
        doi = input("Please provide the DOI if your resource is available online. If the DOI is unknown or unavailable, "
                    "press enter to skip: \n")

        # Add the reference to the list
        ref_list += citing_journal(publishing_year=pub_year,article_title=title,journal_name=journal,page_start=page_start, page_end=page_end,volume=vol,issue=iss,alt_description=alt,DOI=doi,**authDict) + "\n"
        print("Citation added!")
        # Check for more citations
        more = None
        while more not in ('y', 'n'):
            more = input("Would you like to add another reference? y/n\n")
            if not more:
                print("Sorry, please enter your selection again: \n")
        if more == 'n':
            citations = False
        ### End of Journal Citation



# Print the entire reference list!
print(ref_list)
