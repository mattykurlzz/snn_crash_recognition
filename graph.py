import matplotlib.pyplot as plt

electricity_charge = 0.8
income = 15 * 0.3 - electricity_charge
daily_additions = 5
asic_cost = 2190

years = 4

disp_asics = 2
savings = 0

asics_vec = []
savings_vec = []
earnings_vec = []
days_vec = range(0, years * 365)

for day in days_vec:
    savings += income * disp_asics + daily_additions
    if savings >= asic_cost:
        disp_asics += 1
        savings -= asic_cost

    asics_vec += [disp_asics]
    savings_vec += [savings]
    earnings_vec += [income * disp_asics]

fig, ax = plt.subplots()
ax.plot(days_vec, earnings_vec)

# ax2 = ax.twinx()
# ax2.plot(days_vec, savings_vec, color="y")

asics_vec = []
savings_vec = []
earnings_vec = []
savings = 0
disp_asics = 2

for day in days_vec:
    savings += income * disp_asics
    if savings >= asic_cost:
        disp_asics += 1
        savings -= asic_cost

    asics_vec += [disp_asics]
    savings_vec += [savings]
    earnings_vec += [income * disp_asics]


ax.plot(days_vec, earnings_vec)

asics_vec = []
savings_vec = []
earnings_vec = []
days_vec = range(0, years * 365)
daily_additions = 10
savings = 0
disp_asics = 2
for day in days_vec:
    savings += income * disp_asics + daily_additions
    if savings >= asic_cost:
        disp_asics += 1
        savings -= asic_cost

    asics_vec += [disp_asics]
    savings_vec += [savings]
    earnings_vec += [income * disp_asics]
ax.plot(days_vec, earnings_vec)


# ax2 = ax.twinx()
# ax2.plot(days_vec, savings_vec, color="y")

plt.show()
