import pandas as pd
import matplotlib.pyplot as plt 

def add_transaction (date, amount,category,description):
  try:
    data = pd.read_csv('data.csv')
  except FileNotFoundError:
    data = pd.DataFrame(colums=['date', 'amount', 'category', 'description']) 

  new_transaction = pd.DataFrame({
      'Date': [date], 
      'Amount': [amount],
      'Category': [category], 
      'Description': [description]
  })

  data = pd.concat([data, new_transaction], ignore_index=True)  
  data.to_csv('data.csv',index=Falsese)

def view_transaction ():
  try:
    data = pd.read_csv('data.csv')
    print(data)
  except FileNotFoundError:
    print('No transaction Found')

def gen_summary():
  try:
    data=pd.read_csv('data.csv')
  except FileNotFoundError:
    print ('No transaction Found')
    return 
  summary = data.groupby('category')['amount'].sum()
  print (summary)

  summary.plot(kind='bar')
  plt.title('Spending by category')
  plt.xlabel('category')
  plt.ylabel('Total amount')
  plt.show()

def main():
  while True:
    print('\nPersonal finance tracker')
    print('1. Add transaction')
    print('2. View transaction')
    print('3. Generate summary')
    print('4. Exit')

    choice = input('Enter your choice (1-4) :')
    if choice=='1':
      date= input('Enter date (YYYY-MM-DD) : ')
      amount= float(input('Enter the amount : '))
      category= input ('Enter category : ')
      description=input ("Enter description : ")
      add_transaction(date,amount, category, description)
      print ('Transaction added')

    elif choice=='2':
      view_transaction() 
    elif choice=='3':
      gen_summary()
    elif choice=='4':
      print('Exiting the program')
      break 

    else:
      print('Invalid choice please choose between (1-4) ')


if __name__ =="__main__":
  main()

      
   
