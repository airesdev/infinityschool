# Ex. 01
	SELECT count(*) FROM ator;
		# 200

# Ex. 02
	SELECT * FROM ator WHERE ator_id = 31;
		# Sissy Sobieki

# Ex. 03
	SELECT * FROM pais WHERE pais LIKE 'B%';
		# 15

# Ex. 04
	SELECT * FROM pais WHERE pais LIKE 'A%';
		/*
Afghanistan
Algeria
American Samoa
Angola
Anguilla
Argentina
Armenia
Australia
Austria
Azerbaijan
*/

# Ex. 05
	SELECT count(*) FROM pais WHERE pais LIKE 'A%'; 
		# 10

# Ex. 06
	SELECT * FROM pais WHERE pais LIKE 'P%';
		/*
		Pakistan
		Paraguay
		Peru
		Philippines
		Poland
		Puerto Rico
        */

# Ex. 07
	SELECT count(*) FROM pais WHERE pais LIKE 'P%'; 
		# 6
# Ex. 08
	SELECT * FROM pais WHERE pais LIKE 'O%';
		/*
        Oman
        */

# Ex. 09
	SELECT count(*) FROM pais WHERE pais LIKE 'O%';
		# 1

# Ex. 08
	SELECT * FROM pais WHERE pais LIKE '%NA%';
		/*
        Argentina
		Canada
		China
		French Guiana
		Nauru
		Saint Vincent and the Grenadines
		Vietnam
        */

# Ex. 09
	SELECT count(*) FROM pais WHERE pais LIKE '%NA%';
		# 7