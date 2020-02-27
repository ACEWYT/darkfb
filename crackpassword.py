#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import hashlib
print("\n md5 password cracker \n")
while __name__ == "__main__":
 hashu = input("what is the md5 hash: ")
  
 fileo=("password",
          "123456", 
          "billybob", 
          "password123",
          "Password",
          "BillyBob",
          "FluffyUnicorn")
 
 counter = 1
 for passes in fileo:
  md5has = hashlib.md5(passes.encode('utf-8').strip()) .hexdigest()
  print('trying pw %d: %s'%(counter, passes))
  counter += 1
  if hashu == md5has:
   print("\n password found: %s \n"%(passes))
   break
 else:
  print("404 hash not found")
      
