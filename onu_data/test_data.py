import pandas


from_str_to_int = lambda str_datum: int(str_datum.replace(' ', ''))
# from_str_to_float = lambda str_datum: float(str_datum)


def test_crpd_2018():
    print('# CRPD 2018')
    crpd_2018 = 'crpd_2018_special_education_centres.csv'
    data_crpd_2018 = pandas.read_csv(crpd_2018, sep=',', decimal=".")

    nb_persons = data_crpd_2018['persons number enrolled in special education centres']

    # Official total number of children with disabilities enrolled: 16 496
    nb_enrolled_children__reference = 16496
    nb_enrolled_children__calculated = sum(
        map(
            from_str_to_int,
            nb_persons
            ))
    diff_reference_calculated = nb_enrolled_children__reference - nb_enrolled_children__calculated
    print('enrolled children number, reference-calculated difference: ', diff_reference_calculated)

    disabilities_percentage = data_crpd_2018['percentage enrolled in special education centres']
    disabilities_percentage__calculated = sum(disabilities_percentage)
    print('enrolled children percentage, reference-calculated difference: ', 100.0-disabilities_percentage__calculated)


def test_crpd_2010_taux_handicap():
    print('# CRPD 2010 - taux handicap')
    crpd_2010_taux_handicap = 'crpd_2010_taux_handicap.csv'


def test_crpd_2010_types_handicap():
    print('# CRPD 2010 - types handicap')
    crpd_2010_types_handicap = 'crpd_2010_types_handicap.csv'
    data_crpd_2010_types_handicap = pandas.read_csv(crpd_2010_types_handicap, sep=';', decimal=',')

    nb_personnes = data_crpd_2010_types_handicap['nombre de personnes handicapées']  # par type de handicap
    nb_personnes__reference = 151423  # total dans tableau
    nb_personnes__calcule = sum(
        map(
            from_str_to_int,
            nb_personnes
            ))
    print('nombre de personnes handicapées, différence reférence-calculé: ', nb_personnes__reference - nb_personnes__calcule)

    pourcentage_personnes = data_crpd_2010_types_handicap['pourcentage']  # par type de handicap
    pourcentage_personnes__calcule = sum(pourcentage_personnes)
    print('pourcentage personnes handicapées, différence reférence-calculé: ', 100.0 - pourcentage_personnes__calcule)


def test_crpd_2010_causes_handicap():
    print('# CRPD 2010 - causes handicap')
    crpd_2010_causes_handicap = 'crpd_2010_causes_handicap.csv'
    data_crpd_2010_causes_handicap = pandas.read_csv(crpd_2010_causes_handicap, sep=';', decimal=',')

    nb_personnes = data_crpd_2010_causes_handicap['nombre de personnes handicapées']
    nb_personnes__reference = 151423  # total dans tableau (identique types handicap)
    nb_personnes__calcule = sum(
        map(
            from_str_to_int,
            nb_personnes
            ))
    print('nombre de personnes handicapées, différence reférence-calculé: ', nb_personnes__reference - nb_personnes__calcule)

    pourcentage_personnes = data_crpd_2010_causes_handicap['pourcentage']  # par cause de handicap
    pourcentage_personnes__calcule = sum(pourcentage_personnes)
    print('pourcentage personnes handicapées, différence reférence-calculé: ', 100.0 - pourcentage_personnes__calcule)


def test_crpd_2010_repartition_sexes():
    print('# CRPD 2010 - répartition du handicap par sexe')
    crpd_2010_repartion_sexes_handicap = 'crpd_2010_repartion_sexes_handicap.csv'
    data_crpd_2010_repartion_sexes_handicap = pandas.read_csv(crpd_2010_repartion_sexes_handicap, sep=';', decimal=',')

    nb_personnes = data_crpd_2010_repartion_sexes_handicap['nombre de personnes handicapées']
    nb_personnes__reference = 151423  # total dans tableau
    nb_personnes__calcule = sum(
        map(
            from_str_to_int,
            nb_personnes
            ))
    print('nombre de personnes handicapées, différence reférence-calculé: ', nb_personnes__reference - nb_personnes__calcule)


if __name__ == "__main__":
    # test_crpd_2010_taux_handicap()
    test_crpd_2010_types_handicap()
    test_crpd_2010_causes_handicap()
    test_crpd_2010_repartition_sexes()
    test_crpd_2018()
