import csv

brasileirao2023 = []
for i in range(1, 221):
    brasileirao2023.append([{"numero": 1, "jogador": "Matheus Cavichioli", "posicao": "Goleiro", "time": "America Mineiro"},
    {"numero": 2, "jogador": "Arthur", "posicao": "Lateral-Esquerdo", "time": "America Mineiro"},
    {"numero": 3, "jogador": "Eder", "posicao": "Zagueiro", "time": "America Mineiro"},
    {"numero": 4, "jogador": "Maidana", "posicao": "Zagueiro", "time": "America Mineiro"},
    {"numero": 5, "jogador": "Marlon", "posicao": "Lateral-Direito", "time": "America Mineiro"},
    {"numero": 6, "jogador": "Alê", "posicao": "Volante", "time": "America Mineiro"},
    {"numero": 7, "jogador": "Matheusinho", "posicao": "Meio-Campista", "time": "America Mineiro"},
    {"numero": 8, "jogador": "Juninho", "posicao": "Meio-Campista", "time": "America Mineiro"},
    {"numero": 9, "jogador": "Benitez", "posicao": "Meio-Campista", "time": "America Mineiro"},
    {"numero": 10, "jogador": "Everaldo", "posicao": "Meio-Campista", "time": "America Mineiro"},
    {"numero": 11, "jogador": "Aloisio", "posicao": "Atacante", "time": "America Mineiro"},
    {"numero": 12, "jogador": "Bento", "posicao": "Goleiro", "time": "Athetico Paranaense"},
    {"numero": 13, "jogador": "Khellven", "posicao": "Lateral-Direito", "time": "Athetico Paranaense"},
    {"numero": 14, "jogador": "José Ivaldo", "posicao": "Zagueiro", "time": "Athetico Paranaense"},
    {"numero": 15, "jogador": "Thiago Heleno", "posicao": "Zagueiro", "time": "Athetico Paranaense"},
    {"numero": 16, "jogador": "Pedrinho", "posicao": "Lateral-Esquerdo", "time": "Athetico Paranaense"},
    {"numero": 17, "jogador": "Erick", "posicao": "Volante", "time": "Athetico Paranaense"},
    {"numero": 18, "jogador": "Terans", "posicao": "Meio-Campista", "time": "Athetico Paranaense"},
    {"numero": 19, "jogador": "Hugo Moura", "posicao": "Meio-Campista", "time": "Athetico Paranaense"},
    {"numero": 20, "jogador": "Alex Santana", "posicao": "Meio-Campista", "time": "Athetico Paranaense"},
    {"numero": 21, "jogador": "Romulo", "posicao": "Meio-Campista", "time": "Athetico Paranaense"},
    {"numero": 22, "jogador": "Vitor Roque", "posicao": "Atacante", "time": "Athetico Paranaense"},
    
    {"numero": 23, "jogador": "Everson", "posicao": "Goleiro", "time": "Atletico Mineiro"},
    {"numero": 24, "jogador": "Saraiva", "posicao": "Lateral-Direito", "time": "Atletico Mineiro"},
    {"numero": 25, "jogador": "Mauricio Lemos", "posicao": "Zagueiro", "time": "Atletico Mineiro"},
    {"numero": 26, "jogador": "Jemerson", "posicao": "Zagueiro", "time": "Atletico Mineiro"},
    {"numero": 27, "jogador": "Rubens", "posicao": "Lateral-Esquerdo", "time": "Atletico Mineiro"},
    {"numero": 28, "jogador": "Zaracho", "posicao": "Meio-Campista", "time": "Atletico Mineiro"},
    {"numero": 29, "jogador": "Edenílson", "posicao": "Meio-Campista", "time": "Atletico Mineiro"},
    {"numero": 30, "jogador": "Hyoran", "posicao": "Meio-Campista", "time": "Atletico Mineiro"},
    {"numero": 31, "jogador": "Otávio", "posicao": "Meio-Campista", "time": "Atletico Mineiro"},
    {"numero": 32, "jogador": "Paulinho", "posicao": "Atacante", "time": "Atletico Mineiro"},
    {"numero": 33, "jogador": "Hulk", "posicao": "Atacante", "time": "Atletico Mineiro"},

    {"numero": 34, "jogador": "Bento", "posicao": "Goleiro", "time": "BAHIA"},
    {"numero": 35, "jogador": "Khellven", "posicao": "Lateral-Direito", "time": "BAHIA"},
    {"numero": 36, "jogador": "José Ivaldo", "posicao": "Zagueiro", "time": "BAHIA"},
    {"numero": 37, "jogador": "Thiago Heleno", "posicao": "Zagueiro", "time": "BAHIA"},
    {"numero": 38, "jogador": "Pedrinho", "posicao": "Zagueiro", "time": "BAHIA"},
    {"numero": 39, "jogador": "Erick", "posicao": "Lateral-Esquerdo", "time": "BAHIA"},
    {"numero": 40, "jogador": "Terans", "posicao": "Volante", "time": "BAHIA"},
    {"numero": 41, "jogador": "Hugo Moura", "posicao": "Volante", "time": "BAHIA"},
    {"numero": 42, "jogador": "Alex Santana", "posicao": "Meio-Campista", "time": "BAHIA"},
    {"numero": 43, "jogador": "Romulo", "posicao": "Meio-Campista", "time": "BAHIA"},
    {"numero": 44, "jogador": "Vitor Roque", "posicao": "Atacante", "time": "BAHIA"},

    {"numero": 45, "jogador": "Lucas Perri", "posicao": "Goleiro", "time": "Botafogo"},
    {"numero": 46, "jogador": "Rafael", "posicao": "Lateral-Direito", "time": "Botafogo"},
    {"numero": 47, "jogador": "Adryelson", "posicao": "Zagueiro", "time": "Botafogo"},
    {"numero": 48, "jogador": "Victor Cuesta", "posicao": "Zagueiro", "time": "Botafogo"},
    {"numero": 49, "jogador": "Marçal", "posicao": "Lateral-Esquerdo", "time": "Botafogo"},
    {"numero": 50, "jogador": "Tchê Tchê", "posicao": "Volante", "time": "Botafogo"},
    {"numero": 51, "jogador": "Danilo Barbosa", "posicao": "Volante", "time": "Botafogo"},
    {"numero": 52, "jogador": "Eduardo", "posicao": "Meio-Campista", "time": "Botafogo"},
    {"numero": 53, "jogador": "Júnior Santos", "posicao": "Atacante", "time": "Botafogo"},
    {"numero": 54, "jogador": "Tiquinho Soares", "posicao": "Atacante", "time": "Botafogo"},
    {"numero": 55, "jogador": "Victor Sá", "posicao": "Atacante", "time": "Botafogo"},

    {"numero": 56, "jogador": "Lucão", "posicao": "Goleiro", "time": "Red Bull Bragantino"},
    {"numero": 57, "jogador": "Aderlan", "posicao": "Lateral-Direito", "time": "Red Bull Bragantino"},
    {"numero": 58, "jogador": "Eduardo Santos", "posicao": "Zagueiro", "time": "Red Bull Bragantino"},
    {"numero": 59, "jogador": "Natan", "posicao": "Zagueiro", "time": "Red Bull Bragantino"},
    {"numero": 60, "jogador": "Juninho Capixaba", "posicao": "Lateral-Esquerdo", "time": "Red Bull Bragantino"},
    {"numero": 61, "jogador": "Matheus Fernandes", "posicao": "Volante", "time": "Red Bull Bragantino"},
    {"numero": 62, "jogador": "Eric Ramires", "posicao": "Volante", "time": "Red Bull Bragantino"},
    {"numero": 63, "jogador": "Bruninho", "posicao": "Meio-Campista", "time": "Red Bull Bragantino"},
    {"numero": 64, "jogador": "Helinho", "posicao": "Atacante", "time": "Red Bull Bragantino"},
    {"numero": 65, "jogador": "Eduardo Sacha", "posicao": "Atacante", "time": "Red Bull Bragantino"},
    {"numero": 66, "jogador": "Sorriso", "posicao": "Atacante", "time": "Red Bull Bragantino"},

    {"numero": 67, "jogador": "Cássio", "posicao": "Goleiro", "time": "CORINTHIANS"},
    {"numero": 68, "jogador": "Du Queiroz", "posicao": "Lateral-Direito", "time": "CORINTHIANS"},
    {"numero": 69, "jogador": "Gil", "posicao": "Zagueiro", "time": "CORINTHIANS"},
    {"numero": 70, "jogador": "Murilo", "posicao": "Zagueiro", "time": "CORINTHIANS"},
    {"numero": 71, "jogador": "Matheus Bidu", "posicao": "Lateral-Esquerdo", "time": "CORINTHIANS"},
    {"numero": 72, "jogador": "Fausto Vera", "Volante": "Goleiro", "time": "CORINTHIANS"},
    {"numero": 73, "jogador": "Roni", "posicao": "Volante", "time": "CORINTHIANS"},
    {"numero": 74, "jogador": "Adson", "posicao": "Meio-Campista", "time": "CORINTHIANS"},
    {"numero": 75, "jogador": "Angel Romero", "posicao": "Meio-Campista", "time": "CORINTHIANS"},
    {"numero": 76, "jogador": "Yuri Alberto", "posicao": "Atacante", "time": "CORINTHIANS"},
    {"numero": 77, "jogador": "Róger Guedes", "posicao": "Atacante", "time": "CORINTHIANS"},

    {"numero": 78, "jogador": "Gabriel", "posicao": "Goleiro", "time": "Coritiba"},
    {"numero": 79, "jogador": "Kuscevic", "posicao": "Zagueiro", "time": "Coritiba"},
    {"numero": 80, "jogador": "Bruno Viana", "posicao": "Zagueiro", "time": "Coritiba"},
    {"numero": 81, "jogador": "Victor Luis", "posicao": "Zagueiro", "time": "Coritiba"},
    {"numero": 82, "jogador": "Natanael", "posicao": "Meio-Campista", "time": "Coritiba"},
    {"numero": 83, "jogador": "Jamerson", "posicao": "Meio-Campista", "time": "Coritiba"},
    {"numero": 84, "jogador": "Willian Farias", "posicao": "Meio-Campista", "time": "Coritiba"},
    {"numero": 85, "jogador": "Bruno Gomes", "posicao": "Meio-Campista", "time": "Coritiba"},
    {"numero": 86, "jogador": "Alef Manga", "posicao": "Atacante", "time": "Coritiba"},
    {"numero": 87, "jogador": "Rodrigo Pinho", "posicao": "Atacante", "time": "Coritiba"},
    {"numero": 88, "jogador": "Kaio César", "posicao": "Atacante", "time": "Coritiba"},

    {"numero": 89, "jogador": "Rafael Cabral", "posicao": "Goleiro", "time": "Cruzeiro"},
    {"numero": 90, "jogador": "William", "posicao": "Lateral-Direito", "time": "Cruzeiro"},
    {"numero": 91, "jogador": "Neris", "posicao": "Zagueiro", "time": "Cruzeiro"},
    {"numero": 92, "jogador": "Luciano Castán", "posicao": "Zagueiro", "time": "Cruzeiro"},
    {"numero": 93, "jogador": "Marlon", "posicao": "Lateral-Esquerdo", "time": "tCruzeiro"},
    {"numero": 94, "jogador": "Richard Coelho", "posicao": "Volante", "time": "Cruzeiro"},
    {"numero": 95, "jogador": "Ramiro", "posicao": "Volante", "time": "Cruzeiro"},
    {"numero": 96, "jogador": "Nikão", "posicao": "Meio-Campista", "time": "Cruzeiro"},
    {"numero": 97, "jogador": "Mateus Vital", "posicao": "Meio-Campista", "time": "Cruzeiro"},
    {"numero": 98, "jogador": "Bruno Rodrigues", "posicao": "Atacante", "time": "Cruzeiro"},
    {"numero": 99, "jogador": "Gilberto", "posicao": "Atacante", "time": "Cruzeiro"},

    {"numero": 100, "jogador": "Walter", "posicao": "Goleiro", "time": "Cuiaba"},
    {"numero": 101, "jogador": "Matheusinho", "posicao": "Lateral-Direito", "time": "Cuiaba"},
    {"numero": 102, "jogador": "Marllon", "posicao": "Zagueiro", "time": "Cuiaba"},
    {"numero": 103, "jogador": "Alan Empereur", "posicao": "Zagueiro", "time": "Cuiaba"},
    {"numero": 104, "jogador": "PK", "posicao": "Lateral-Esquerdo", "time": "Cuiaba"},
    {"numero": 105, "jogador": "Filipe Augusto", "posicao": "Volante", "time": "Cuiaba"},
    {"numero": 106, "jogador": "Raniele", "posicao": "Volante", "time": "Cuiaba"},
    {"numero": 107, "jogador": "Ceppelini", "posicao": "Meio-Campista", "time": "Cuiaba"},
    {"numero": 108, "jogador": "Jonathan Cafu", "posicao": "Atacante", "time": "Cuiaba"},
    {"numero": 109, "jogador": "Deyverson", "posicao": "Atacante", "time": "Cuiaba"},
    {"numero": 110, "jogador": "Emerson Ramon", "posicao": "Atacante", "time": "Cuiaba"},

    {"numero": 111, "jogador": "Santos", "posicao": "Goleiro", "time": "Flamengo"},
    {"numero": 112, "jogador": "Fabrício Bruno", "posicao": "Zagueiro", "time": "Flamengo"},
    {"numero": 113, "jogador": "David Luiz", "posicao": "Zagueiro", "time": "Flamengo"},
    {"numero": 114, "jogador": "Léo Pereira", "posicao": "Zagueiro", "time": "Flamengo"},
    {"numero": 115, "jogador": "Wesley", "posicao": "Lateral-Direito", "time": "Flamengo"},
    {"numero": 116, "jogador": "Thiago Maia", "posicao": "Volante", "time": "Flamengo"},
    {"numero": 117, "jogador": "Vidal", "posicao": "Volante", "time": "Flamengo"},
    {"numero": 118, "jogador": "Ayrton Lucas", "posicao": "Lateral-Esquerdo", "time": "Flamengo"},
    {"numero": 119, "jogador": "Everton Ribeiro", "posicao": "Meio-Campista", "time": "Flamengo"},
    {"numero": 120, "jogador": "Gabriel", "posicao": "Atacante", "time": "Flamengo"},
    {"numero": 121, "jogador": "Pedro", "posicao": "Atacante", "time": "Flamengo"},

    {"numero": 122, "jogador": "Fábio", "posicao": "Goleiro", "time": "Fluminense"},
    {"numero": 123, "jogador": "Guga", "posicao": "Lateral-Direito", "time": "Fluminense"},
    {"numero": 124, "jogador": "Nino", "posicao": "Zagueiro", "time": "Fluminense"},
    {"numero": 125, "jogador": "Manoel", "posicao": "Zagueiro", "time": "Fluminense"},
    {"numero": 126, "jogador": "Alexsander", "posicao": "Lateral-Esquerdo", "time": "Fluminense"},
    {"numero": 127, "jogador": "André", "posicao": "Volante", "time": "Fluminense"},
    {"numero": 128, "jogador": "Lima", "posicao": "Volante", "time": "Fluminense"},
    {"numero": 129, "jogador": "Gabriel Pirani", "posicao": "Meio-Campista", "time": "Fluminense"},
    {"numero": 130, "jogador": "John Kennedy", "posicao": "Atacante", "time": "Fluminense"},
    {"numero": 131, "jogador": "Alan", "posicao": "Atacante", "time": "Fluminense"},
    {"numero": 132, "jogador": "Lelê", "posicao": "Atacante", "time": "Fluminense"},

    {"numero": 133, "jogador": "Fernando Miguel", "posicao": "Goleiro", "time": "Fortaleza"},
    {"numero": 134, "jogador": "Tinga", "posicao": "Lateral-Direito", "time": "Fortaleza"},
    {"numero": 135, "jogador": "Brítez", "posicao": "Zagueiro", "time": "Fortaleza"},
    {"numero": 136, "jogador": "Titi", "posicao": "Zagueiro", "time": "Fortaleza"},
    {"numero": 137, "jogador": "Bruno Pacheco", "posicao": "Lateral-Esquerdo", "time": "Fortaleza"},
    {"numero": 138, "jogador": "Caio Alexandre", "posicao": "Volante", "time": "Fortaleza"},
    {"numero": 139, "jogador": "Hércules", "posicao": "Volante", "time": "Fortaleza"},
    {"numero": 140, "jogador": "Pochettino", "posicao": "Meio-Campista", "time": "Fortaleza"},
    {"numero": 141, "jogador": "Calebe", "posicao": "Atacante", "time": "Fortaleza"},
    {"numero": 142, "jogador": "Thiago Galhardo", "posicao": "Atacante", "time": "Fortaleza"},
    {"numero": 143, "jogador": "Romarinho", "posicao": "Atacante", "time": "Fortaleza"},

    {"numero": 144, "jogador": "Tadeu", "posicao": "Goleiro", "time": "Goias"},
    {"numero": 145, "jogador": "Maguinho", "posicao": "Lateral-Direito", "time": "Goias"},
    {"numero": 146, "jogador": "Lucas Halter", "posicao": "Zagueiro", "time": "Goias"},
    {"numero": 147, "jogador": "Bruno Melo", "posicao": "Zagueiro", "time": "Goias"},
    {"numero": 168, "jogador": "Sander", "posicao": "Lateral-Esquerdo", "time": "Goias"},
    {"numero": 149, "jogador": "Zé Ricardo", "posicao": "Volante", "time": "Goias"},
    {"numero": 150, "jogador": "Morelli", "posicao": "Volante", "time": "Goias"},
    {"numero": 151, "jogador": "Diego", "posicao": "Meio-Campista", "time": "Goias"},
    {"numero": 152, "jogador": "Julián Palacios", "posicao": "Meio-Campista", "time": "Goias"},
    {"numero": 153, "jogador": "Vinicius", "posicao": "Meio-Campista", "time": "Goias"},
    {"numero": 154, "jogador": "Matheus Peixoto", "posicao": "Atacante", "time": "Goias"},
    {"numero": 155, "jogador": "Gabriel Grando", "posicao": "Goleiro", "time": "Grêmio"},
    {"numero": 156, "jogador": "João Pedro ", "posicao": "Lateral-Direito", "time": "Grêmio"},
    {"numero": 157, "jogador": "Bruno Alves", "posicao": "Zagueiro", "time": "Grêmio"},
    {"numero": 158, "jogador": "Kannemann", "posicao": "Zagueiro", "time": "Grêmio"},
    {"numero": 159, "jogador": "Reinaldo", "posicao": "Lateral-Esquerdo", "time": "Grêmio"},
    {"numero": 160, "jogador": "Felipe Carballo", "posicao": "Volante", "time": "Grêmio"},
    {"numero": 161, "jogador": "Pepe", "posicao": "Volante", "time": "Grêmio"},
    {"numero": 162, "jogador": "Franco Cristaldo", "posicao": "Meio-Campista", "time": "Grêmio"},
    {"numero": 163, "jogador": "Bitelo", "posicao": "Meio-Campista", "time": "Grêmio"},
    {"numero": 164, "jogador": "Vina", "posicao": "Atacante", "time": "Grêmio"},
    {"numero": 165, "jogador": "Luis Suarez", "posicao": "Atacante", "time": "Grêmio"},

    {"numero": 166, "jogador": "John Victor", "posicao": "Goleiro", "time": "internacional"},
    {"numero": 167, "jogador": "Bustos", "posicao": "Lateral-Direito", "time": "internacional"},
    {"numero": 168, "jogador": "Vitão", "posicao": "Zagueiro", "time": "internacional"},
    {"numero": 169, "jogador": "Mercado", "posicao": "Zagueiro", "time": "internacional"},
    {"numero": 170, "jogador": "Renê", "posicao": "Lateral-Esquerdo", "time": "internacional"},
    {"numero": 171, "jogador": "Carlos de Pena", "posicao": "Volante", "time": "internacional"},
    {"numero": 172, "jogador": "Matheus Dias", "posicao": "Volante", "time": "internacional"},
    {"numero": 173, "jogador": "Johnny", "posicao": "Volante", "time": "internacional"},
    {"numero": 174, "jogador": "Mauricio", "posicao": "Atacante", "time": "internacional"},
    {"numero": 175, "jogador": "Pedro Henrique", "posicao": "Atacante", "time": "internacional"},
    {"numero": 176, "jogador": "Luiz Adriano", "posicao": "Atacante", "time": "internacional"},

    {"numero": 177, "jogador": "Weverton", "posicao": "Goleiro", "time": "Palmeiras"},
    {"numero": 178, "jogador": "Mayke", "posicao": "Lateral-Direito", "time": "Palmeiras"},
    {"numero": 179, "jogador": "Gustavo Gómez", "posicao": "Zagueiro", "time": "Palmeiras"},
    {"numero": 180, "jogador": "Murilo", "posicao": "Zagueiro", "time": "Palmeiras"},
    {"numero": 181, "jogador": "Piquerez", "posicao": "Lateral-Esquerdo", "time": "Palmeiras"},
    {"numero": 182, "jogador": "Zé Rafael", "posicao": "Volante", "time": "Palmeiras"},
    {"numero": 183, "jogador": "Gabriel Menino", "posicao": "Volante", "time": "Palmeiras"},
    {"numero": 184, "jogador": "Raphael Veiga", "posicao": "Meio-Campista", "time": "Palmeiras"},
    {"numero": 185, "jogador": "Artur", "posicao": "Atacante", "time": "Palmeiras"},
    {"numero": 186, "jogador": "Rony", "posicao": "Atacante", "time": "Palmeiras"},
    {"numero": 187, "jogador": "Dudu", "posicao": "Atacante", "time": "Palmeiras"},

    {"numero": 188, "jogador": "João Paulo", "posicao": "Goleiro", "time": "Santos"},
    {"numero": 189, "jogador": "Nathan", "posicao": "Lateral-Direito", "time": "Santos"},
    {"numero": 190, "jogador": "Messias", "posicao": "Zagueiro", "time": "Santos"},
    {"numero": 191, "jogador": "Eduardo Bauermann", "posicao": "Zagueiro", "time": "Santos"},
    {"numero": 192, "jogador": "Lucas Pires", "posicao": "Lateral-Esquerdo", "time": "Santos"},
    {"numero": 193, "jogador": "Rodrigo Fernández", "posicao": "Volante", "time": "Santos"},
    {"numero": 194, "jogador": "Dodi", "posicao": "Volante", "time": "Santos"},
    {"numero": 195, "jogador": "Lucas Lima", "posicao": "Meio-Campista", "time": "Santos"},
    {"numero": 196, "jogador": "Mendoza", "posicao": "Atacante", "time": "Santose"},
    {"numero": 197, "jogador": "Marcos Leonardo", "Atacante": "Goleiro", "time": "Santos"},
    {"numero": 198, "jogador": "Soteldo", "posicao": "Atacante", "time": "Santos"},

    {"numero": 199, "jogador": "Rafael", "posicao": "Goleiro", "time": "São Paulo"},
    {"numero": 200, "jogador": "Raí Ramos", "posicao": "Lateral-Direito", "time": "São Paulo"},
    {"numero": 201, "jogador": "Diego Costa", "posicao": "Zagueiro", "time": "São Paulo"},
    {"numero": 202, "jogador": "Lucas Beraldo", "posicao": "Zagueiro", "time": "São Paulo"},
    {"numero": 203, "jogador": "Caio Paulista", "posicao": "Lateral-Esquerdo", "time": "São Paulo"},
    {"numero": 204, "jogador": "Luan", "posicao": "Volante", "time": "São Paulo"},
    {"numero": 205, "jogador": "Pablo Maia", "posicao": "Volante", "time": "São Paulo"},
    {"numero": 206, "jogador": "Alisson", "posicao": "Meio-Campista", "time": "São Paulo"},
    {"numero": 207, "jogador": "Rodrigo Nestor", "posicao": "Meio-Campista", "time": "São Pauloe"},
    {"numero": 208, "jogador": "Wellington Rato", "posicao": "Meio-Campista", "time": "São Paulo"},
    {"numero": 209, "jogador": "Luciano", "posicao": "Atacante", "time": "São Paulo"},

    {"numero": 210, "jogador": "Léo Jardim", "posicao": "Goleiro", "time": "Vasco"},
    {"numero": 211, "jogador": "Puma Rodríguez", "posicao": "Lateral-Direito", "time": "Vasco"},
    {"numero": 212, "jogador": "Robson Bambu", "posicao": "Zagueiro", "time": "Vasco"},
    {"numero": 213, "jogador": "Léo", "posicao": "Zagueiro", "time": "Vasco"},
    {"numero": 214, "jogador": "Lucas Piton", "posicao": "Lateral-Esquerdo", "time": "Vasco"},
    {"numero": 215, "jogador": "Andrey Santos", "Volante": "Goleiro", "time": "Vasco"},
    {"numero": 216, "jogador": "Jair", "posicao": "Volante", "time": "Vasco"},
    {"numero": 217, "jogador": "Marlon Gomes", "posicao": "Volante", "time": "Vasco"},
    {"numero": 218, "jogador": "Gabriel Pec", "posicao": "Meio-Campista", "time": "Vasco"},
    {"numero": 219, "jogador": "Alex Teixeira", "posicao": "Meio-Campista", "time": "Vasco"},
    {"numero": 220, "jogador": "Pedro Raul", "posicao": "Atacante", "time": "Vasco"},])

with open('brasileirao2023.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Número", "Nome", "Descrição", "Disponibilidade"])
    for figurinha in brasileirao2023:
        writer.writerow(figurinha)


