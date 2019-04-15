#XA = 65474
#YA = 48
#XB = 843578
#YB = 3857
#XC = 8476
#YC = 84859
#XD = 983
#YD = 83939


def przeciecie(XA, YA, XB, YB, XC, YC, XD, YD):
    
    if (XB-XA)*(YD-YC)-(YB-YA)*(XD-XC) == 0:
        roz = "proste sa rownolegle"
        XP = None
        YP = None
    else:
        
        t1 = ((XC-XA)*(YD-YC)-(YC-YA)*(XD-XC))/((XB-XA)*(YD-YC)-(YB-YA)*(XD-XC))
        t2 =((XC-XA)*(YB-YA)-(YC-YA)*(XB-XA))/((XB-XA)*(YD-YC)-(YB-YA)*(XD-XC))
        
        if 0<=t1 and t1<=1:
            
            if 0<=t2 and t2<=1 :
                 roz = "punkt lezy na przecieciu odcinkow"
            else:
                 roz = "punkt lezy na odcinku AB"
        else: 
            
            if 0<=t2 and t2<=1:
                roz = " punkt lezy na odcinku CD"
            
            else:
                 roz = "punkt nie lezy na zadnym odcinku"
                
            
        XP = XA + t1*(XB-XA)
        YP = YA + t1*(YB-YA)
        XP = round(XP, 3)
        YP = round(YP, 3)
        
        with open('punktprze.txt', 'w') as file:
            file.write('{:^10s} {:^10s}\n'.format('XP', 'YP'))
            file.write('{:<10.3f} {:<10.3f}'.format(XP, YP))
            
    return(roz, XP, YP, t1, t2)

    

    