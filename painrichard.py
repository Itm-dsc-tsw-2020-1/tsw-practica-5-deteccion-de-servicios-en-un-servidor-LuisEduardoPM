import os
import mysql.connector as mysql
def getn():
    f = open("archivo.txt", "r")
    b = open("things.txt", "w")
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='hackiar' )
    operacion = conexion.cursor()
    while(True):

        linea = f.readline()
        if not linea.find('Nmap scan report for '):
            c = 21
            ip = ""
            while (c<len(linea)):

                ip=ip+linea [c]
                c=c+1
            print ("IP = "+ip)
            linea = f.readline()
            linea = f.readline()
            linea = f.readline()
            linea = f.readline()

            while (len(linea)>1):
                c=0
                c1=1
                port=""
                state=""
                service=""
                
                #print (len(linea))
                while (c1==1 and linea[c]!=' '):
                    port+=linea[c]
                    c+=1
                print(port)
                c1+=1
                while (linea[c]==' '):
                    c+=1
                while (c1==2 and linea[c]!=' '):
                    state+=linea[c]
                    c+=1
                print(state)
                c1+=1
                while (linea[c]==' '):
                    c+=1
                while (c1==3 and c<len(linea)):
                    service+=linea[c]
                    c+=1
                print(service)
                c1+=1
                #print (linea)

                
                operacion.execute( "INSERT INTO nmap (ip, puerto, servicio, estado) VALUES (\""+ip+"\", \""+port+"\",\""+state+"\",\""+service+"\")" )
                
                linea = f.readline()
                pass

        if not linea:
            break
    conexion.commit()
    f.close()
    b.close()





def insertar():
    f = open ("things.txt","r")
    while(True):
        c=0
        c1=1
        port=""
        state=""
        service=""
        linea = f.readline()
        if(len(linea)==0):
            linea = f.readline()
        else:
            while (c1==1 and linea[c]!=' '):
                port+=linea[c]
                c+=1
            print(port)
            c1+=1
            while (linea[c]==' '):
                c+=1
            while (c1==2 and linea[c]!=' '):
                state+=linea[c]
                c+=1
            print(state)
            c1+=1
            while (linea[c]==' '):
                c+=1
            while (c1==3 and c<len(linea)):
                service+=linea[c]
                c+=1
            print(service)
            c1+=1
        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='hackiar' )
        operacion = conexion.cursor()
        ip="200.33.171.125"
        operacion.execute( "INSERT INTO nmap (ip, puerto, servicio, estado) VALUES (\""+ip+"\", \""+port+"\",\""+state+"\",\""+service+"\")" )
        conexion.commit()
        if not linea:
            break





red = "200.33.171.0/24"
os.system("nmap -oN archivo.txt "+ red)


#os.system("nmap -oN "+archivo.txt+' '+ip)




getn()
#insertar()

## nmap -oN archivo.txt 200.33.171.125
## nmap -oN archivo.txt 200.33.171.0/24