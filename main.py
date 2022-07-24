from add_user import *
from add_buku import *
from search_buku import *
from issue_book import *
from return_book import *

UserLibrary()
if __name__ == "__main__":
    while (True):
        welcomeLMS = '''.........LIBRARY MANAGEMENT.........
        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman
        4. Tampilkan Daftar Buku
        5. Tampilkan Daftar User
        6. Tampilkan Daftar Peminjaman
        7. Cari Buku
        8. Pengembaliam
        9. Exit
        '''
        print(welcomeLMS)
        a = int(input("\nEnter a choice: "))
        if a == 1:
            UserLibrary().add_user()
        elif a == 2:
            BookLibrary().add_book()
        elif a == 3:
            IssueBook().issue_book()
        elif a == 4:
            BookLibrary().view_book()
        elif a == 5:
            UserLibrary().view_user()
        elif a == 6:
            IssueBook().view_issue()
        elif a == 7:
            BookSearch().search_book()
        elif a == 8:
            ReturnBook().return_book()
        elif a == 9:
            print(".................\nHave a great day\n.................")
            exit()