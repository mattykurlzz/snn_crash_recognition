import matplotlib.pyplot as plt


class miner:
    def __init__(self, power_watt, income_per_month_dol, cost, coin):
        self.power_watt = power_watt
        self.raw_income_per_day = income_per_month_dol / 30
        self.cost = cost
        self.coin = coin

    def get_daily_income(self, electricity_bill_per_kw, day):
        return (
            self.raw_income_per_day
            - self.power_watt / 1000 * 24 * electricity_bill_per_kw
        )


def get_mining_prognosis(
    dollar_cost=90,
    electricity_charge_rub_per_kwatt=4.5,
    hotel_electricity_charge_rub_per_kwatt=8,
    monthly_additions_rub=15000,
    years=4,
    savings=0,
    disp_miners=[],
    planned_miners=[miner(630, 6 * 30, 2190, "ltc")],
    pool_comission=0.03,
    hotel_comission=0.07,
):
    electricity_charge_dol_per_kwatt = electricity_charge_rub_per_kwatt / dollar_cost
    daily_additions = monthly_additions_rub / 30 / dollar_cost

    miners_vec = []  # счетчик имеющихся асиков без учета доходности
    earnings_vec = []  # счетчик текущей скорости накоплений за день
    days_vec = range(0, years * 365)

    electricity = electricity_charge_dol_per_kwatt

    for day in days_vec:
        cur_income = daily_additions
        for miner in disp_miners:
            cur_income += (
                miner.get_daily_income(
                    electricity,
                    day,
                )
                * (1 - pool_comission)
                * (1 - (hotel_comission if len(disp_miners) >= 5 else 0))
            )
        savings += cur_income
        if savings >= planned_miners[0].cost:
            disp_miners += [planned_miners[0]]
            savings -= planned_miners[0].cost
            del planned_miners[0]

        miners_vec += [len(disp_miners)]
        earnings_vec += [cur_income]

        if len(disp_miners) >= 5:
            electricity = hotel_electricity_charge_rub_per_kwatt / dollar_cost
    return miners_vec, earnings_vec, days_vec


dollar_cost = 90

d1_home = miner(630, 3 * 30, 1300, "ltc")
ez100c = miner(760, 134, 2949, "btn")
ae_box = miner(360, 504, 3499, "aleo")
s21_xp = miner(5676, 900, 15555, "btc")
s21_hydro_plus = miner(4785, 500, 5000, "btc")

disp_miners = [d1_home, d1_home]
planned_miners = [
    [d1_home for _ in range(9999)],
    [ez100c, ae_box, ae_box] + [s21_xp for _ in range(999)],
    [ae_box, ae_box] + [s21_xp for _ in range(999)],
    [d1_home for _ in range(2)] + [s21_hydro_plus for _ in range(909)],
]
titles = [
    "Покупка DG1home или других недорогих эффективных майнеров",
    "ez100c, 2x AE box, s21 xp",
    "2x AE box, s21 xp",
    "20x DG1Home, s21 xp",
]

fig, ax = plt.subplots(2, 2)

for planned_miners, axis, title in zip(planned_miners, ax.flatten(), titles):
    miners_vec, earnings_vec, days_vec = get_mining_prognosis(
        disp_miners=[d1_home, d1_home],
        planned_miners=planned_miners,
        dollar_cost=90,
        years=4,
        hotel_comission=0.1,
        hotel_electricity_charge_rub_per_kwatt=5.4,
    )
    axis.plot(days_vec, earnings_vec, color="r")
    ax2 = axis.twinx()
    ax2.plot(days_vec, miners_vec, color="blue")

    axis.set_ylabel("ежедневный заработок, $", color="r")
    axis.tick_params(axis="y", labelcolor="r")
    axis.set_xlabel("Срок, дней")
    ax2.set_ylabel("Текущее количество майнеров", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    axis.set_title(title)

plt.show()
