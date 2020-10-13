# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ---
# >> **UŽDUOTIS**
# >>
# >> 1. Sukurkite masyvą `a_np` (10,) formos susidedantį iš skaičių sekos nuo 3
# iki 4 paskirstytų vienodais žingsniais
# >> 2. Sukurkite masyvą `b_np` (2,10) formos su skaičių seka nuo 1 iki 20
# >> 3. Padalinkite `b_np` į du 1 dimensijos masyvus (1,10)
# >>











# ---
# >> **UŽDUOTIS**
# >>
# >> Praplėskite funkciją kad būtų galima keisti amplitudę ir fazę
# >>
# ---

def gen_wave(Hz=10, sample_rate=1000, length_sec=1):
    t = np.linspace(0, length_sec, length_sec * sample_rate, endpoint=False)
    x = np.sin(Hz * 2 * np.pi * t)
    return(t, x)


sample_rate = 1000
length_sec = 1
plt.plot(*gen_wave());







# ---
# >> **UŽDUOTIS**
# >>
# >> Naudojant NumPy sukurkite signalus
# >>
# ---

# ![a1](../images/a1.png)







# ![a2](../images/a2.png)







# ![a3](../images/a3.png)







# ![a4](../images/a4.png)







# ![a5](../images/a5.png)







# ![a6](../images/a6.png)







# ![a7](../images/a7.png)







# ![a8](../images/a8.png)



















#  ##  Atsakymai

a_np = np.linspace(3, 4, 10)

b_np = np.linspace(1, 20, 20).reshape(2, 10)

c1, c2 = np.split(b_np, [1])


def gen_wave_amp(Hz, sample_rate, length_sec, phase, amplitude):
    t = np.linspace(0, length_sec, int(
        length_sec * sample_rate), endpoint=False)
    x = amplitude * np.sin(Hz * 2 * np.pi * t + phase)
    return(t, x)


time = np.linspace(0, 1, 1000)
plt.plot(time);

# Log

plt.plot(time, np.log(time));

# Root

plt.plot(time, np.sqrt(time));

# Kvadratas

plt.plot(np.concatenate((np.zeros(1000), np.ones(1000), np.zeros(1000))));


# Sumine banga

t,wave_10 = gen_wave(10, sample_rate, length_sec)
t,wave_1 = gen_wave(1, sample_rate, length_sec)
t,wave_40 = gen_wave(40, sample_rate, length_sec)
wave_sum = wave_10+wave_1+wave_40
plt.plot(t, wave_sum)
plt.title('suma skirtingų bangų')
plt.ylabel('Amplitudė')
plt.xlabel('Laikas , s');


# Spikes

s1 = 1
s2 = 5
s3 = 10
spike = [sample_rate * 0.1, sample_rate * 0.3, sample_rate * 0.7]
t = np.arange(sample_rate)
spike_train = (
    np.exp(-(((t - spike[0]) / (s1)) ** 2))
    + np.exp(-(((t - spike[1]) / (s2)) ** 2))  # width of the Gaussian
    + np.exp(-(((t - spike[2]) / (s3)) ** 2))
)
t = np.linspace(0, 1, sample_rate)
plt.plot(t, spike_train)
plt.title("Spikes")
plt.xlabel("Laikas, s")
plt.ylabel("Amplitudė");

# Stačiakampiai

w1 = 1
w2 = 5
w3 = 50
spikai = [sample_rate * 0.1, sample_rate * 0.3, sample_rate * 0.7]
time = np.arange(sample_rate)
steps = (
    ((time > spikai[0] - w1) & (time < spikai[0] + w1))
    # Logical indexing to define places
    + ((time > spikai[1] - w2) & (time < spikai[1] + w2))
    + ((time > spikai[2] - w3) & (time < spikai[2] + w3))
)
t = np.linspace(0, 1, sample_rate)
plt.plot(t, steps)
plt.title("Stačiakampiai")
plt.xlabel("Laikas, s")
plt.ylabel("Amplitudė");

# Triukšmas

noise = np.random.randn(sample_rate)
t = np.linspace(0, len(noise), sample_rate)

plt.plot(t, noise)
plt.title("Triukšmas")
plt.xlabel("Laikas, s")
plt.ylabel("Amplitudė");


