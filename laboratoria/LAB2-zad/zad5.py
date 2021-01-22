print("proszę dmuchać w ustnik, zostanie zbadana zawartość\n"
      "alkoholu w wydychanym przez Pana powietrzu")
a=float(input("\n*dmuchanie przez pijanego*\n"))
if a>0.25:
    print("jest pan naje**")
elif a>0 and a<0.25:
    print("jest pan wstawiony, ale dopuszczalnie")
else:
    print("jest pan trzeźwy")
