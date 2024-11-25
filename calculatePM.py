import sys

exp_const = {"A": 2.94, "B": 0.91}
levels = {"very low": 0, "low": 1, "nominal": 2, "high": 3, 
          "very high": 4, "extra high": 5}

sf = {"PREC": [6.2, 4.96, 3.72, 2.48, 1.24, 0],
      "FLEX": [5.07, 4.05, 3.04, 2.03, 1.01, 0],
      "RESL": [7.07, 5.65, 4.24, 2.83, 1.41, 0],
      "TEAM": [5.48, 4.38, 3.29, 2.19, 1.1, 0],
      "PMAT": [7.8, 6.24, 4.68, 3.12, 1.56, 0]}

em = {"RELY": [0.82, 0.92, 1, 1.1, 1.26, None],
      "DATA": [None, 0.9, 1, 1.14, 1.28, None],
      "CPLX": [0.73, 0.87, 1, 1.17, 1.34, 1.74],
      "RUSE": [None, 0.95, 1, 1.07, 1.15, 1.24],
      "DOCU": [0.81, 0.91, 1, 1.11, 1.23, None],
      "TIME": [None, None, 1, 1.11, 1.29, 1.63],
      "STOR": [None, None, 1, 1.05, 1.17, 1.46],
      "PVOL": [None, 0.87, 1, 1.15, 1.3, None],
      "ACAP": [1.42, 1.19, 1, 0.85, 0.71, None],
      "PCAP": [1.34, 1.15, 1, 0.88, 0.76, None],
      "PCON": [1.29, 1.12, 1, 0.9, 0.81, None],
      "APEX": [1.22, 1.1, 1, 0.88, 0.81, None],
      "PLEX": [1.19, 1.09, 1, 0.91, 0.85, None],
      "LTEX": [1.2, 1.09, 1, 0.91, 0.85, None],
      "TCOL": [1.17, 1.09, 1, 0.9, 0.78, None],
      "SITE": [1.22, 1.09, 1, 0.93, 0.86, 0.8],
      "SCED": [1.43, 1.14, 1, 1, 1, None]}

lang_sloc_by_ufp = {"Access": 38, "Ada 83": 71, "Ada 95": 49, "AI Shell": 49, 
        "APL": 32, "Assembly-Basic": 320, "Assembly-Macro": 213, "Basic-ANSI": 64,
        "Basic-Complied": 91, "Basic-Visual": 32, "C": 128, "C++": 55, "Cobol": 91,
        "Database - default": 40, "Fifth Generation Lang.": 4, "First Generation Lang.": 320,
        "Forth": 64, "Fortran 77": 107, "Fortran 95": 71, "Fourth Generation Lang.": 20, 
        "High Level Lang.": 64, "HTML 3.0": 15, "Java": 53, "Jovial": 107,
        "Lisp": 64, "Machine Code": 640, "Modula 2": 80, "Pascal": 91, "Perl": 27,
        "PowerBuilder": 16, "Prolog": 64, "Query - default": 13, "Report Generator": 80,
        "Second Generation Lang": 107, "Simulation - default": 46, "Spreadsheet": 6,
        "Third Generation Lang.": 80, "Unix Shell Script": 107, "Visual Basic 5.0": 29, "Visual C++": 34}

revl_input = input("Enter revl: ")
try:
    revl = float(revl_input)
    if revl < 0 or revl > 100:
        raise ValueError()
except ValueError:
    print("Invalid input!!")
    sys.exit(-1)

language = input("Enter language: ")
if (sloc_by_ufp := lang_sloc_by_ufp.get(language)) == None:
    print("This system does not support this language!!")
    sys.exit(-1)

ufp_input = input("Enter ufp: ")
try:
    ufp = int(ufp_input)
except ValueError:
    print("Invalid input!!")
    sys.exit(-1)

size = (1 + revl / 100) * (ufp * sloc_by_ufp / 1000)

sum_sf = 0
mul_em = 1
print("input level by each sf and em")
print(f"{", ".join([f"{name} = {levels[name]}" for name in levels])}")
for sf_type in sf:
    sf_level = input(f"{sf_type}: ")
    try:
        if not sf_level:
            sum_sf += sf[sf_type][2]
        else:
            if (level := int(sf_level)) > 5:
                raise ValueError()
            if sf[sf_type][level]:
                sum_sf += sf[sf_type][level]
            else:
                raise ValueError
    except ValueError:
        print("Invalid input!!")
        sys.exit(-1)

for em_type in em:
    em_level = input(f"{em_type}: ")
    try:
        if not em_level:
            mul_em *= em[em_type][2]
        else:
            if (level := int(em_level)) > 5:
                raise ValueError()
            if em[em_type][level]:
                mul_em *= em[em_type][level]
            else:
                raise ValueError
    except ValueError:
        print("Invalid input!!")
        sys.exit(-1)

effort = exp_const["B"] + 0.01 * sum_sf

pm = exp_const["A"] * pow(size, effort) * mul_em

print("")
print(f"Size = {size}")
print(f"Sum of SF = {sum_sf}")
print(f"Mul of EM = {mul_em}")
print(f"E = {effort}")
print(f"PM = {pm}")