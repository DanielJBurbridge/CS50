import re

def main():

   date = user_input_phase()

def user_input_phase():
      date = input("Date: ").strip()
      american_dates = re.compile("^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$")
      month_words = re.compile("^[A-Z][a-z]+\s+[0-9]{1,2},\s+[0-9]{4}$")

      if bool(american_dates.search(date)):
         #print("This is an American Date")
         convert_american(date)
      elif bool(month_words.search(date)):
         #print("This date has a month spelled in it")
         convert_month(date)
      else:
         user_input_phase()

def convert_american(d):

   date = d.split("/")
   formated_date = [date[2], date[0].zfill(2), date[1].zfill(2)]

   if validator(formated_date):
      print_date(formated_date)
   else:
      user_input_phase()

def convert_month(d):
   date = d.split(" ")
   date[0] = lookup(date[0])
   date[1] = date[1][:-1]
   formated_date = [date[2], date[0].zfill(2), date[1].zfill(2)]

   if validator(formated_date):
      print_date(formated_date)
   else:
      user_input_phase()

def lookup(s):

   months = {
       "January" : "1",
       "February" : "2",
       "March" : "3",
       "April" : "4",
       "May" : "5",
       "June" : "6",
       "July" : "7",
       "August" : "8",
       "September" : "9",
       "October" : "10",
       "November" : "11",
       "December" : "12"
   }

   return months.get(s)

def validator(d):
   return not (int(d[1]) > 12 or int(d[2]) > 31)

def print_date(d):
   print("-".join(d))

if __name__ == "__main__":
   main()