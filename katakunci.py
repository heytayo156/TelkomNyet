import os, sys

print ("")
print ("\033[1;33mHarap Masukan Username dan Password Authornya [!]")

print ("\033[1;33mAtau HandPhone Anda Datanya Hilang ")
print ("_________________________________________________")
print ("")
print ("\033[1;36mBisa Juga Hubungi Forum Kami ")

print ("\033[1;36m> Whatsapp : 081326848668")

print ("\033[1;36m> Facebook : Jafar Sans")

print ("\033[1;91m")
username = '434'

password = 'EDITOR'



def restart():

        ngulang = sys.executable

        os.execl(ngulang, ngulang, *sys.argv)



def main():

        uname = raw_input("username : ")
        if uname == username:

                pwd = raw_input("password : ")



                if pwd == password:

                        print ""

                        print ""

                        print "\033[1;32mYeee Bisa Masuuk....",

                        sys.exit()



                else:

                        print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"

                        print "Silahkan segera Log-in Kembali..\n"

                        restart()



        else:

                print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

                print "Silahkan segera Log-in kembali...!!\n"

                restart()



try:

        main()

except KeyboardInterrupt:

        os.system('clear')

        restart()
