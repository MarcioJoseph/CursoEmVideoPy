medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print(' A medida de {}m corresponde a \n{:.0f}cm e \n{:.0f}mm \n{:.0f}dm \n{:.1f}dam \n{:.2f}hm \n{:.3f}km '.format(medida, cm, mm, dm, dam, hm, km))

