import subprocess 
import sys

b = ("""

  o__ __o        o           o__ __o        o__ __o          o__ __o     o__ __o                o           o__ __o     o         o/ 
 <|     v\      <|>         /v     v\      /v     v\        /v     v\   <|     v\              <|>         /v     v\   <|>       /v  
 / \     <\     / \        />       <\    />       <\      />       <\  / \     <\             / \        />       <\  / >      />   
 \o/     o/   o/   \o     _\o____        _\o____         o/             \o/     o/           o/   \o    o/             \o__ __o/     
  |__  _<|/  <|__ __|>         \_\__o__       \_\__o__  <|               |__  _<|           <|__ __|>  <|               |__ __|      
  |          /       \               \              \    \\              |       \          /       \   \\              |      \     
 <o>       o/         \o   \         /    \         /      \         /  <o>       \o      o/         \o   \         /  <o>      \o   
  |       /v           v\   o       o      o       o        o       o    |         v\    /v           v\   o       o    |        v\  
 / \     />             <\  <\__ __/>      <\__ __/>        <\__ __/>   / \         <\  />             <\  <\__ __/>   / \        <\ 
""")
print(b)
a = input("Write the string of which you want to generate more password like that:  ")
passwordlist = [a, "1234567890" , "123" , "2021", "!2021", "hello", "admin","1","2","3","4","5","6","7","8","9","10", "messi", "1010","80","@","#","2005","!","@","*","fig","hero","mr","mrs","Mr","Mrs","jio","crack","-"]


for x in passwordlist:
 text1 =  print(x + a)


for x in passwordlist:
      text2 =    print(a + x)


f = open("passcracker.txt", "w")
f.write(hi,bye)
f.close()
