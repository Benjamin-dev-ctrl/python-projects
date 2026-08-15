books={'lord of the rings':4,'fairy tales':3,'history book':5,'science book':3}
for i in books:
    print(i)
while True:
 b_r=input('Do you want to borrow a book or return a book? b/r ')
 if b_r == 'b':
     book_b=input('what book do you want to borrow? ')
     if book_b not in books:
        print('book not availeble')
     elif books[book_b]==0:
         print('cant borrow book')
     else:
        print('you succesfully borrowed a book')
        books[book_b]=books[book_b]-1
 elif b_r=='r':
    book_r=input('what book do you want to return? ')
    if book_r in books:
     books[book_r]=books[book_r]+1
     print('succesfully returned a book')
    else:
       print('book not availeble')
 else:
    break

