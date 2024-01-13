import math
weiter = "y"
while weiter == "y" or weiter == "Y":
    Lagerkräfte_berechnen = str(input("Sollen die Lagerkraft berchnet werden? (y or n): "))
    if Lagerkräfte_berechnen == "y" or Lagerkräfte_berechnen == "Y":
        Motorleistung = float(input("Motorleistung in kw: "))
        Drehzahlmotor = float(input("Drehzahlmotor in rpm: "))
        #x = float(input(x: ))
        drehmoment_motor = (Motorleistung*9550)/Drehzahlmotor
        print("Drehmoment Motor: " + str(drehmoment_motor))
        #if vorübersetzung == "y" or vorübersetzung == "Y" :


        Efficentsgrad_der_Übersetzung =float(input("Efficentsgrad der Übersetzung in % OHNE % Zeichen: "))
        übersetzungsverhätnis = float(input("Übersetzungs Verhäniss: "))
        drehzahl_getriebe = Drehzahlmotor / übersetzungsverhätnis 
        drehmoment_getriebe = drehmoment_motor * übersetzungsverhätnis
        drehzahl_getriebe_eff = Efficentsgrad_der_Übersetzung/100 * drehzahl_getriebe
        drehmoment_getriebe_eff = Efficentsgrad_der_Übersetzung/100 * drehmoment_getriebe
        print("drehzahl_getriebe: " + str(drehzahl_getriebe_eff))
        print("drehmoment_getriebe: "+ str(drehmoment_getriebe_eff))


        model_zahnrad = float(input("Mudul des Zahnrattes an der zu messen Welle in mm: "))
        zähnezahl_Zahnrad = float(input("Zähnezahl des Zahnrattes an der zu messen Welle: "))
        Teilkreisdruchmesser = model_zahnrad * zähnezahl_Zahnrad
        print("Teilkreisdruchmesser: "+str(Teilkreisdruchmesser))

        #if vorübersetzung == "y" or vorübersetzung == "Y" :
        #   Tangenzialkraft = drehmoment_getriebe_eff / Teilkreisdruchmesser/1000
        #    print("Tangenzialkraft: " + str(Tangenzialkraft))
        #else:

        Tangenzialkraft = drehmoment_getriebe / (Teilkreisdruchmesser/2000)
        print("Tangenzialkraft: " + str(Tangenzialkraft))
        Zahnradwinkel = float(input("Verzahnungswinkel in Grad OHNE Gradzeichen: "))

        #if vorübersetzung == "y" or vorübersetzung == "Y" :
        #    Radialkraft = Tangenzialkraft * math.tan(Zahnradwinkel)
        #    print("Tangenzialkraft: " + str(Radialkraft))
        #else:

        Radialkraft = Tangenzialkraft * math.tan(Zahnradwinkel*(3.14159265359/180))
        print("Tangenzialkraft: " + str(Radialkraft))
        Tangenzialkraft_rimenscheibe = (drehmoment_getriebe_eff *2000 * float(input("Berchnungs korektur für Fw Faktor: ")))/ (float(input("Durchmesser der Rimenscheibe in mm: ")))
        print("Fw: " +str(Tangenzialkraft_rimenscheibe))


        Fw_vorzeichen_draufsicht = float(input("Fw Vorzeichen Richtung Draufsicht als Faktor schreiben (-1 or +1): "))
        Fzt_vorzeichen_draufsicht = float(input("Tangenzialkraft Richtung Draufsicht als Faktor schreiben (-1 or +1): "))
        Fr_vorzeichen_draufsicht = float(input("Radialkraft Richtung Draufsicht als Faktor schreiben (-1 or +1): "))
        Fa_vorzeichen_draufsicht = float(input("Lagerkraft a Richtung Draufsicht als Faktor schreiben (-1 or +1): "))
        Fb_vorzeichen_draufsicht = float(input("Lagerkraft b Riechtung Draufsicht als Faktor schreiben (-1 or +1): "))
        Länge_fa_zu_Fw = float(input("Länge zwischen Fa und Fw und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_Fzt = float(input("Länge zwischen Fa und Fzt und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_Fr = float(input("Länge zwischen Fa und Fr und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_fb = float(input("Länge zwischen Fa und Fb und das Vorzeichen ist die Drehrichtung um Fa: "))


        fa1 = Länge_fa_zu_fb*((Fr_vorzeichen_draufsicht * Radialkraft) + (Fw_vorzeichen_draufsicht * Tangenzialkraft_rimenscheibe)+ (Fzt_vorzeichen_draufsicht * Tangenzialkraft))
        fa2 = Länge_fa_zu_Fr*Fr_vorzeichen_draufsicht*Radialkraft-Länge_fa_zu_Fzt*Fzt_vorzeichen_draufsicht*Tangenzialkraft-Länge_fa_zu_Fw*Fw_vorzeichen_draufsicht*Tangenzialkraft_rimenscheibe
        Fay = (-fa1+fa2)/Länge_fa_zu_fb
        Fby = -1*(Länge_fa_zu_Fr*Radialkraft+Länge_fa_zu_Fzt*Tangenzialkraft+Länge_fa_zu_Fw*Tangenzialkraft_rimenscheibe)/Länge_fa_zu_fb

        print("Lagerkraft für die Draufsicht für Fa"+str(Fay))
        print("Lagerkraft für die Draufsicht für Fb"+str(Fby))

        Fw_vorzeichen_Seitenansicht = float(input("Fw Vorzeichen Richtung Seitenansicht als Faktor schreiben (-1 or +1): "))
        Fzt_vorzeichen_Seitenansicht = float(input("Tangenzialkraft Richtung Seitenansicht als Faktor schreiben (-1 or +1): "))
        Fr_vorzeichen_Seitenansicht = float(input("Radialkraft Richtung Seitenansicht als Faktor schreiben (-1 or +1): "))
        Fa_vorzeichen_Seitenansicht = float(input("Lagerkraft a Richtung Seitenansicht als Faktor schreiben (-1 or +1): "))
        Fb_vorzeichen_Seitenansicht = float(input("Lagerkraft b Riechtung Seitenansicht als Faktor schreiben (-1 or +1): "))
        Länge_fa_zu_Fw = float(input("Länge zwischen Fa und Fw und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_Fzt = float(input("Länge zwischen Fa und Fzt und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_Fr = float(input("Länge zwischen Fa und Fr und das Vorzeichen ist die Drehrichtung um Fa: "))
        Länge_fa_zu_fb = float(input("Länge zwischen Fa und Fb und das Vorzeichen ist die Drehrichtung um Fa: "))


        fa1 = Länge_fa_zu_fb*((Fr_vorzeichen_Seitenansicht * Radialkraft) + (Fw_vorzeichen_Seitenansicht * Tangenzialkraft_rimenscheibe)+ (Fzt_vorzeichen_Seitenansicht * Tangenzialkraft))
        fa2 = Länge_fa_zu_Fr*Fr_vorzeichen_Seitenansicht*Radialkraft-Länge_fa_zu_Fzt*Fzt_vorzeichen_Seitenansicht*Tangenzialkraft-Länge_fa_zu_Fw*Fw_vorzeichen_Seitenansicht*Tangenzialkraft_rimenscheibe
        Fax = (-fa1+fa2)/Länge_fa_zu_fb
        Fbx = -1*(Länge_fa_zu_Fr*Radialkraft+Länge_fa_zu_Fzt*Tangenzialkraft+Länge_fa_zu_Fw*Tangenzialkraft_rimenscheibe)/Länge_fa_zu_fb

        print("Lagerkraft für die Seitenansicht für Fa"+str(Fax))
        print("Lagerkraft für die Seitenansicht für Fb"+str(Fbx))

    Eigenwerte = "y"

    Lebensdauer = str(input("Sollen Lagerlebensdauer A berechnet werden (y or n): "))
    if Lebensdauer == "y" or Lebensdauer == "Y":
        c0 = float(input("Eingabe von C0 für Lager A in kn: "))
        c =  float(input("Eingabe von C für Lager A in kn: "))
        Eigenwerte = str(input("Sollen Solleneigne Werte benutzt werden (y or n): "))
        if Eigenwerte == "y" or Eigenwerte == "Y":
            Eigen_Radialkräfte = float(input("Wert für Radialkäfte in Lager A in kn: "))
            Eigen_Axialkräfte = float(input("Wert für Axialkäfte in Lager A in kn: "))
            if Eigen_Axialkräfte == 0:
                X = 1
                Y = 0
                print ("Der X Wert ist 1! ")
                print ("Der Y Wert ist 1! ")
                Last_im_Lager =  Eigen_Radialkräfte * X + Eigen_Axialkräfte * Y
                drehzahl_getriebe_eff = float(input("Drehzahl des Lagers :"))
            else:
                e_vergleich = Eigen_Radialkräfte/Eigen_Axialkräfte 
                print("e Vergleichswert: " + str(e_vergleich))
                X = float(input("Wert für X: "))
                Y = float(input("Wert für Y: ")) 
                Last_im_Lager =  Eigen_Radialkräfte * X + Eigen_Axialkräfte * Y
                drehzahl_getriebe_eff = float(input("Drehzahl des Lagers :"))
        else:
            Restirende_lagerkräfte_fa = (Fax**2 + Fay**2)**0.5
            Restirende_lagerkräfte_fb_in_kn = Restirende_lagerkräfte_fa /1000
            Eigen_Axialkräfte = float(input("Wert für Axialkäfte in kn: "))
            e_vergleich = Restirende_lagerkräfte_fb_in_kn/Eigen_Axialkräfte 
            print("e Vergleichswert" + str(e_vergleich))
            print("Radialkräfte Fa in kn: "+ str(Restirende_lagerkräfte_fb_in_kn))
            e = Restirende_lagerkräfte_fb_in_kn/c0
            print("Der Wert e "+str(e))
            X = float(input("Wert für X: "))
            Y = float(input("Wert für Y: "))  
            Last_im_Lager = Restirende_lagerkräfte_fb_in_kn * X + Eigen_Axialkräfte * Y
        
        Lebensdauer_in_h = ((c/Last_im_Lager)*10**6)/(60*drehzahl_getriebe_eff)
        print("Lebensdauer von Lager A in Stunden: "+str(Lebensdauer_in_h))

    Lebensdauer = str(input("Sollen Lagerlebensdauer B berechnet werden (y or n): "))
    if Lebensdauer == "y" or Lebensdauer == "Y":
        c0 = float(input("Eingabe von C0 für Lager B in kn: "))
        c =  float(input("Eingabe von C für Lager B in kn: "))
        Eigenwerte = str(input("Sollen Solleneigne werte benutzt werden (y or n): "))
        if Eigenwerte == "y" or Eigenwerte == "Y":
            Eigen_Radialkräfte = float(input("Wert für Radialkäfte Lager B in kn: "))
            Eigen_Axialkräfte = float(input("Wert für Axialkäfte in Lager B in kn: "))
            if Eigen_Axialkräfte == 0:
                X = 1
                Y = 0
                print ("Der X Wert ist 1! ")
                print ("Der Y Wert ist 1! ")
                Last_im_Lager =  Eigen_Radialkräfte * X + Eigen_Axialkräfte * Y
                drehzahl_getriebe_eff = float(input("Drehzahl des Lagers :"))
            else:
                e_vergleich = Eigen_Radialkräfte/Eigen_Axialkräfte 
                print("e Vergleichswert: " + str(e_vergleich))
                X = float(input("Wert für X: "))
                Y = float(input("Wert für Y: ")) 
                Last_im_Lager =  Eigen_Radialkräfte * X + Eigen_Axialkräfte * Y
                drehzahl_getriebe_eff = float(input("Drehzahl des Lagers :"))
        else:
            Restirende_lagerkräfte_fb = (Fbx**2 + Fby**2)**0.5
            Restirende_lagerkräfte_fb_in_kn = Restirende_lagerkräfte_fb /1000
            Eigen_Axialkräfte = float(input("Wert für Axialkäfte in kn: "))
            e_vergleich = Restirende_lagerkräfte_fb_in_kn/Eigen_Axialkräfte 
            print("e Vergleichswert" + str(e_vergleich))
            print("Radialkräfte Fb in kn: "+ str(Restirende_lagerkräfte_fb_in_kn))
            e = Restirende_lagerkräfte_fb_in_kn/c0
            print("Der Wert e "+str(e))
            X = float(input("Wert für X: "))
            Y = float(input("Wert für Y: "))  
            Last_im_Lager = Restirende_lagerkräfte_fb_in_kn * X + Eigen_Axialkräfte * Y
        
        Lebensdauer_in_h = ((c/Last_im_Lager)*10**6)/(60*drehzahl_getriebe_eff)
        print("Lebensdauer von Lager A in Stunden: "+str(Lebensdauer_in_h))    


    weiter = str(input("Soll etwas noch mal oder neu berechent werden? (y or n): "))


print("Ende")