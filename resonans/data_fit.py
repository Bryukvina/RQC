#function, that takes parametrs and delta_frequensy list and return list of transmitted wave power points

def theor(x, do, dc, g):
    y = []
    for i in range(len(x)):
        y.append(abs((complex(do, -x[i]) ** 2 - dc ** 2 + g ** 2)/(complex(do + dc, -x[i]) ** 2 + g ** 2)) ** 2)
    y = np.array(y)
    return y

#data from file with processing

s = file.readline()
while s != "":
    t, c1, c2, c3 = map(float, s.split(", "))
    print(t)
    times.append(t)
    channel1.append(c1)
    channel2.append(c2)
    channel3.append(c3)
    s = file.readline()
times = np.array(times)
channel3 = np.array(channel3)

#transfering time list to frequency list, using interferometer's data
count = 0
for i in range(1, len(channel2) - 1):
    if channel2[i - 1] < channel2[i] and channel2[i + 1] < channel2[i]:
        count += 1
#constant dw = ....

dt = (max(times) - min(times)) / count
freq = dw / dt

#draw grafix with fitting data. parameters were had already piked up

plt.figure(figsize=(6, 3))
plt.plot(freq, theor(freq, 1 / 30000000000, 5/ 30000000000, 5/ 30000000000))
plt.plot(freq + 0.0000000002, (channel3 - min(channel3)) /(8.4099E-01 - min(channel3)))
plt.show()

#parameters
do = 3.3333333333333335e-11
dc = 1.6666666666666666e-10
g = 1.6666666666666666e-10
