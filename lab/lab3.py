# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ---
# # Lab 3
#
# 2020-09-29
#

#  ![datacamp](../images/datacamp.png)
#  
# Python fundamentals
#  - Introduction to python 1,2,3 up to numpy
#  - python data science toolbox part
#
# Python toolbox
#  - regular expressions


# >> **UŽDUOTIS**
# >>
# >> 1. Perskaityti dokumentacijas ir regex panaudojimą DNR sekose
# >>
# ---

# ---
# >> **UŽDUOTIS**
# >>
# >> 2. Pakeiskite programą kad kuriant Exp_....txt failus dar ir įrašytų informaciją
# >>
# ---

test_dir_pathlib.mkdir()
for subj in range(1, 11):
    for txt_file in range(1, 11):
        if txt_file < 6:
            measure = "power"
        else:
            measure = "phase"
        p = pathlib.Path.joinpath(
            pathlib.Path.home(),
            "Documents",
            "biod2020",
            "data",
            f"Exp_{txt_file}_{measure}_{subj}.txt",
        )
        p.touch()


# ---
# >> **3. UŽDUOTIS**
# >>
# >>  - Suraskite failus tik pirmo dalyvio (subj)
# >>  - Išfiltruokite tik galios matavimus
# >>
# ---








# ---
# >> **4. UŽDUOTIS**
# >>
# >> Pakeiskite programą kad galėtų rodyt tik direktorijas
# >>
# ---

def tree(directory):
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {path.name}")


tree(bioa_dir)

tree(bioa_dir, "onlydir")






# ---
# >> **5. UŽDUOTIS**
# >>
# >> Raskite tekste šiuos elementus
# >>
# ---

text = 'There’s also a syntax for referring to named groups as defined by the (?P<name>...) syntax. \g<name> will use the substring matched by the group named name, and \g<number> uses the corresponding group number. \g<2> is therefore equivalent to \2, but isn’t ambiguous in a replacement string such as \g<2>0. (\20 would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character "0".) The following substitutions are all equivalent, but use all three variations of the replacement string.'
text



# Visus skaičius
#
# Out[]: ['2', '2', '0', '20', '2', '0']




# Elementus esančius tarp ženklų <>
#
# Out[]: ['name', 'name', 'number', '2', '2']




# 3 raidžių žodžius
#
# Out[]: ['for', 'the', 'use', 'the', 'the', 'and', 'the', 'but', 'isn', 'not', 'the', 'The', 'are', 'all', 'but', 'use', 'all', 'the']




# ---
# >> **6. UŽDUOTIS**
# >>
# >> faile data/tekstas5.txt yra 100 žodžių
# >>
# >> Atidarykite failą ir raskite žodžius prasidedančius raide c ir pasibaigiančius  t arba n
# >>
# ---








# ---
# >> **7. UŽDUOTIS**
# >>
# >> Pakeiskite kintamąjį `text` kad jis taptų toks kaip Out
# >>
# >> Out []: "'1', '2', '3', '4'"
# >>
# ---
#


text = "1, 2, 3, 4"
text

re.sub(



# Out []:
#
# "'1', '2', '3', '4'"


# ---
# >> **8. UŽDUOTIS**
# >>
# >> Suraskite ir ištrinkite visus žodžius kur frazė su yra pakartota du arba tris kartus kad gauti Out[?]
# >>
# ---
# Out[?]:
#
# 'su su3 sususususu4 susususususu6'

text='su susu1 sususu2 su3 sususususu4 susu5 susususususu6'
text

patter=''
re.sub(pattern, '', text)






























# ## Atsakymai
#
# 2. pridėti  p.write_text(f'asdf')
#
# 3. list(Path(test_dir_pathlib).rglob(r'Exp_\d_\w+_1.txt'))
#
# 4.

def tree(directory, flag="all"):
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        if flag == "onlydir" and path.is_dir():
            depth=len(path.relative_to(directory).parts)
            spacer="    " * depth
            print(f"{spacer}+ {path.name}")
        elif flag == "all":
            depth=len(path.relative_to(directory).parts)
            spacer="    " * depth
            print(f"{spacer}+ {path.name}")


tree(bioa_dir, "onlydir")

# 5

re.findall(r"\d+", text)
re.findall(r'<(.*?)>', text)
re.findall(r'\b\w{3,3}\b', text)


# 6

def find_words(filename, pattern):
    result=[]
    with open(filename, "r") as txt:
        for line in txt:
            if re.search(pattern, line):
                result.append(line.strip())
    return result

pattern="^c.*(t|n)$"
filename="/home/aleks/Documents/biod2020/data/tekstas5.txt"

find_words(filename, pattern)

# 7

re.sub("\b?", "'", text)

# 8

text='su susu1 sususu2 su3 sususususu4 susu5 susususususu6'
text

pattern=r'\b(su){2,3}\d'
re.sub(pattern, '', text)
