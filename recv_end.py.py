import socket,time
target_ip="127.0.0.1"
target_port=2222
a=4
#decryption
def decrypt(text,a): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((((ord(char) - a)-65) % 26) + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((((ord(char) - a) - 97) % 26) + 97) 
  
    return result 
#now we are creating UDP socket -- this remains same for sen/rev
#    using ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#this is for receiver
s.bind((target_ip,target_port))


while True:
    
    client=s.recvfrom(100)
    newmsg=(client[0].decode('ascii'))
    result=decrypt(newmsg,a)
    
    print(result)
    #print("now replying :- ",client[1][0])
    #s.sendto("hii guys thanks ",client[1])
