#!/usr/bin/python3


flutes = float(input("nr of flutes: "))
rpm = float(input("spindle rpm: "))
print("""
                        3mm bit     4mm bit      6mm bit        8mm bit 
alu:                    0.08-0.13   0.081-0.133  0.102-0.155    0.139-0.187
acrilic:                            0.090-0.150  0.194-0.245    0.229-0.279
hardwood:               0.08-0.13   0.102-0.153  0.220-0.270    0.310-0.370
softplywood:            0.10-0.15   0.120-0.180  0.270-0.320    0.360-0.420
mdf:                    0.10-0.18   0.140-0.210  0.320-0.396    0.430-0.500
High Pressure Laminate:             0.102-0.163  0.219-0.294    0.311-0.381
Phenolic:               0.10-0.13   0.136-0.154  0.269-0.294    0.362-0.386
Hard Plastic:           0.05-0.10   0.067-0.121  0.148-0.221    0.181-0.240
Soft Plastic:           0.08-0.13   0.086-0.162  0.168-0.242    0.221-0.278
""")
chipload = float(input("chip load: "))

print("feedrate = flutes x chip load x rpm")

feedrate = round(flutes * chipload * rpm)

print(f"{feedrate} = {flutes} x {chipload} x {rpm}")
