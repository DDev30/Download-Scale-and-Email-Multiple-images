import os

os.system("python Download.py \"motorbike\" 20 \"output1\" ")
os.system("python convertToGreyscale.py \"output1\" \"output2\" ")
os.system("python scale.py \"output2\" \"output3\" 50")
os.system("python zip.py \"output3\" \"Finalzip.zip\" ")
os.system("python sendToEmail.py \"Finalzip.zip\" \"email@email.com\"")
