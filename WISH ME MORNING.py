import time
min = int(time.strftime("%M"))

hr=int(time.strftime("%H"))

shift=time.strftime("%p")

hr1=int(time.strftime("%I"))

print("\n""HELLO SIR,")
if hr>=12 and hr<17 :
    print("GOOD AFTERNOON SIR")


elif hr<12 and hr>6:
    print("GOOD MORNING SIR")


elif hr>17 and hr<20:
    print("GOOD EVENING SIR")

else :
    print("GOOD NIGHT SIR") 

print("It is",hr1,":",min,shift)
print("\n")





# %H	Hour (00-23)	
# %I	Hour (01-12)	
# %p	AM or PM	PM
# %M	Minute (00-59)	
# %S	Second (00-59)	
# %f	Microsecond (000000-999999)
# %x	Locale's appropriate date representation



# %Y	Year with century	
# %y	Year without century	
# %m	Month as a zero-padded decimal (01-12)	
# %B	Full month name	
# %b	Abbreviated month name	
# %d	Day of the month as zero-padded 
# %j	Day of the year as zero-padded
# %a	Abbreviated weekday name	
# %A	Full weekday name	
# %w	Weekday as decimal 
# %U	Week number of the year (Sunday-start) 
# %W	Week number of the year (Monday-start)
