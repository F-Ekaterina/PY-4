Домашняя работа 1.1
print ('"бюджет поездки"')
euro= 56.23#rub
print ('курс евро:',euro, 'руб')
day_cost=90#euro
print ('стоимость дня проживания в евро', day_cost)
day_cost_rub=day_cost*euro
print ('стоимость дня проживания в рублях', day_cost_rub)

stay_1=10
stay_2=20
stay_3=30

flight_R_E=100#euro
flight_E_E=50#euro
flights_number_R_E=2
flights_number_E_E=2

trip_cost=(stay_1+stay_2+stay_3)*day_cost
trip=trip_cost+(flights_number_R_E*flight_R_E+flights_number_E_E*flight_E_E)
print ('стоимость поездки', trip)


salary_my=30000#rub
salary_husband=40000#rub
salary_euro=(salary_my+salary_husband)/euro
print ('семейный бюджет в евро', salary_euro)

part_for_trip=salary_euro*0.3
term_sevings=12#month
budget_of_trip=part_for_trip*term_sevings
print ('бюджет поездки', budget_of_trip)


if trip>budget_of_trip:
  deficit=trip-budget_of_trip
  print ('нам не хватает:', deficit)
else:
  proficit=budget_of_trip-trip
  print ('Ура, мы едем!', proficit)
  