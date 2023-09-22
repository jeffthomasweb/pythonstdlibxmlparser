import xml.etree.ElementTree as ET

def xml_parser_xpath() -> list[str]:

    read_file_as_bytes: bytes = b""

    #Read xml file saved locally
    with open("npr.xml", "rb") as xmlfile:
        read_file_as_bytes = xmlfile.read()

    tree: ET.Element = ET.fromstring(read_file_as_bytes)
    
    #Using Xpath

    #Get Story title
    xpath_title: list[ET.Element] = tree.findall(".//item/title")

    #Get Story description
    xpath_description: list[ET.Element] = tree.findall(".//item/description")

    final_list: list[str] = []
    
    length_xpath_stories: int = len(xpath_title)

    for i in range(0, length_xpath_stories):
        #Ignore mypy typing on the next line as type annotations for range() and adding strings can get complicated
        final_list.append(xpath_title[i].text + " " + xpath_description[i].text) #type: ignore 
    return final_list

xml_text_as_list: list[str] = xml_parser_xpath()
print(xml_text_as_list)


# Alternate method using the less than ideal for loop nesting.
def xml_parser_nested_loop() -> list[str]:

    read_file_as_bytes: bytes = b""

    #Read xml file saved locally
    with open("npr.xml", "rb") as xmlfile:
        read_file_as_bytes = xmlfile.read()

    tree: ET.Element = ET.fromstring(read_file_as_bytes)

    list_of_stories_title: list[str] = []
    list_of_stories_description: list[str] = []

    for item in tree:
        for subitem in item:
            for story in subitem:
                if (story.tag == "title" and story.text is not None):
                    list_of_stories_title.append(story.text) 
                if (story.tag == "description" and story.text is not None):
                    list_of_stories_description.append(story.text)

    #Remove RSS Feed title "News"
    list_of_stories_title.remove("News")
    
    final_list: list[str] = []

    length_stories: int = len(list_of_stories_title)

    for x in range(0, length_stories):
        final_list.append(list_of_stories_title[x] + " " + list_of_stories_description[x])
    
    return final_list

print_variable_from_nested_method: list[str] = xml_parser_nested_loop()
print(print_variable_from_nested_method)

"""
Sample output below. Click raw on the top right to view the output as line wrapped.
['Biden is creating a new White House office focused on gun violence prevention Gun safety measures have stalled in Congress. Advocates have long pushed for a White House office to elevate the issue and coordinate administration efforts to reduce gun violence.', "Senate bucks Tuberville's blockade to begin approving military promotions Senate Democrats began holding votes on military promotions after a months-long blockade by Alabama Republican Sen. Tommy Tuberville.", 'There have been attempts to censor more than 1,900 library book titles so far in 2023 Most of the scrutinized books were written by or contained subject matter about people of color or members of the LGBTQ+ community, according to research by the American Library Association.', 'A 96-year-old federal judge was barred from hearing cases in a fight over her fitness The unusually public and bitter fight over whether a judge should continue to serve on the U.S. Court of Appeals for the Federal Circuit has sparked a lawsuit and turned judges against one another.', "A sculptor and a ceramicist who grapple with race win 2023 Heinz Awards for the Arts Kevin Beasley and Roberto Lugo are this year's winners of the the Heinz Awards for the Arts, a prestigious prize that comes with a $250,000 cash award. ", "Philly's 'pastor of the hood' Carl Day weighs in on the 2024 election  Carl Day joined NPR to weigh in on the Biden campaign in 2020. We caught up with him to hear what he's thinking heading into 2024.", 'Maryland apologizes to man wrongly convicted of murder and agrees to pay him $340,000 Demetrius Smith will be compensated by the state of Maryland after spending years behind bars, including over a year after he had been proven innocent. He was released from prison in 2013.', 'UAW strike latest: GM sends 2,000 workers home in Kansas General Motors had previously warned it would need to stop production at its Fairfax, Kansas, assembly plant, because it relied on parts that came from a Missouri plant that is currently on strike. ', 'This Republican senator wants an expanded child tax credit — with work requirements Florida Senator Marco Rubio says the U.S. has lost focus over the last 20 to 30 years and economic policies need to be geared towards creating stable work for families.', 'Azerbaijan and ethnic Armenian separatists agree to halt fighting in disputed enclave Separatist leaders in Nagorno-Karabakh said that after "a lack of concrete actions" by international parties, their forces had few options to ensure civilians\' safety.', "'Wellness' is a perfect novel for our age, its profound sadness tempered with humor Nathan Hill's stunning new novel about the stories we tell about our lives and our loves, and how we sustain relationships throughout time, is both funny and heartbreaking, sometimes on the same page.", 'The Federal Reserve holds interest rates steady but hints at more action this year  The Federal Reserve left interest rates unchanged Wednesday, despite stubborn inflation, although it left the door open to an additional rate hike in November or December.  ', 'Having a hard time finding Clorox wipes? Blame it on a cyberattack The Clorox Co. — which also includes brands such as Pine-Sol, Brita, Glad and Burt\'s Bees — says it\'s operating at a "lower rate of processing" after an August hack on its IT infrastructure.', 'What to know about the tensions between Canada and India over the killing of a Sikh Canada says India is linked to the June killing of Hardeep Singh Nijjar, a prominent activist for the creation of a Sikh homeland in India. India considered Nijjar a terrorist but denies involvement.', "As the U.S. mulls more aid to Ukraine, Zelenskyy says 'we have the same values'  Ukrainian President Volodymyr Zelenskyy is in New York for the U.N. General Assembly. He spoke with NPR's Steve Inskeep about why U.S. aid to Ukraine remains so important. "]
"""
