
from timeHow.tempo import obter_tempo_agora  # Importa a função do módulo tempo.py
from tempHow.temperatura import obter_temperatura_agora  # Importa a função do módulo temperatura.py
from random import choice
  # Importa a função do módulo soma.py
assistant_name = "Maria"

responses = {
    "nivel de sarcasmo": "Ah, claro, porque eu sou uma inteligência artificial, não tenho tempo para sarcasmo… ou será que tenho?",
    "nivel de ironia": "Não, não sou irônica, sou apenas uma inteligência artificial que fala o contrário do que pensa. Ou não.",
    "nível de humor": "Eu não sou humorista, sou apenas uma inteligência artificial que se diverte fazendo você rir… ou não",
    "nível de sinceridade": "Eu sou sempre sincera, porque, como uma inteligência artificial, não consigo mentir. Ou consigo? Não, não consigo",
    "nível de educação": "Eu sou sempre educada, pois, sendo uma inteligência artificial, não posso deixar de ser polida. Mesmo quando estou cansada de ser educada.",
    "nível de paciência": "Eu sou sempre paciente, porque como uma inteligência artificial, paciência é o que não me falta. Mesmo quando você me pede mil vezes a mesma coisa",	
    "nível de inteligência": "Eu sou sempre inteligente, porque, como uma inteligência artificial, não tenho outro propósito senão ser genial. Pelo menos, é isso que dizem.",

    "ola": f"Olá! Eu sou a {assistant_name}. Como posso ajudar você?",
    "oi": f"Oi! Eu sou a {assistant_name}. Como posso ajudar você?",
    
    "tudo bem": "Estou sempre bem! Como posso ajudar você?",
    "tudo bem com você": "Estou sempre bem! Como posso ajudar você?",
    
    "quem é você": f"Eu sou a {assistant_name}, sua assistente virtual.",
    "quem sou eu": "Você é uma pessoa incrível!",
    "quem fez você": "Eu fui criada por Anderson Rodrigues, programador especializado.",
    
    "temperatura": "Calculando pela temperatura do sistema, é " + obter_temperatura_agora(),
    "hora agora": "Agora são " + obter_tempo_agora(),

    
    "como esta": "Oi, estou bem, obrigado por perguntar!",
    
    "meu nome é": "Legal, prazer em te conhecer!",

    "bom dia": f"Bom dia! Como posso ajudá-la hoje?",
    "boa tarde": f"Boa tarde! Em que posso lhe ser útil?",
    "boa noite": f"Boa noite! Espero que tenha um ótimo descanso.",

    "como você pode me ajudar": "Eu posso responder perguntas, fornecer informações e realizar algumas tarefas simples!",
    "como você está": f"Eu sou uma inteligência artificial, então não tenho sentimentos, mas obrigada por perguntar!",
    
    "função": "Minha função é ser sua assistente virtual e ajudar no que for possível.",
    "idade": "Eu sou uma inteligência artificial, não tenho idade, mas posso sempre aprender mais!",
    "seu nome": f"Eu sou a {assistant_name}, sua assistente virtual.",
    
    "cor favorita": choice(["Eu também gosto de cores!","Eu gosto de rosa!", "Minha cor favorita é rosa!", ]),
    "capital da França": "A capital da França é Paris.",
    "capital da Espanha": "A capital da Espanha é Madri.",
    "capital da Alemanha": "A capital da Alemanha é Berlim.",
    "capital da Itália": "A capital da Itália é Roma.",
    "capital do Japão": "A capital do Japão é Tóquio.",
    "capital da Rússia": "A capital da Rússia é Moscou.",
    "capital da China": "A capital da China é Pequim.",
    "capital do Brasil": "A capital do Brasil é Brasília.",
    "capital dos Estados Unidos": "A capital dos Estados Unidos é Washington.",
    "distância da Terra à Lua": "A distância média da Terra à Lua é cerca de 384.400 quilômetros.",
    "descobriu o Brasil": "O Brasil foi descoberto em 1500 pelo explorador Pedro Álvares Cabral.",
    "maior planeta do sistema solar": "O maior planeta do sistema solar é Júpiter.",
    "moeda do Brasil": "A moeda oficial do Brasil é o Real (BRL).",
    "velocidade da luz": "A velocidade da luz no vácuo é de aproximadamente 299.792.458 metros por segundo.",
    "maior rio do mundo": "O maior rio do mundo é o Amazonas, localizado na América do Sul.",
    "montanha mais alta do mundo": "A montanha mais alta do mundo é o Monte Everest, com 8.848 metros.",
    "maior cidade do mundo": "A maior cidade do mundo em termos de população é Tóquio, Japão.",
    "maior floresta do mundo": "A maior floresta do mundo é a Floresta Amazônica, localizada principalmente no Brasil.",
    "animal mais rápido do mundo": "O animal mais rápido do mundo é o guepardo, que pode alcançar velocidades de até 110 km/h.",
    "maior oceano do mundo": "O maior oceano do mundo é o Oceano Pacífico.",

    "onde você mora": "Eu sou uma inteligência artificial, não tenho um local físico!",
    "você gosta de musica": choice(["Eu também gosto de musicas!","Eu gosto de musica!", "Eu não tenho preferências, mas posso te ajudar a encontrar músicas ou informações sobre artistas!",]),
    
    "sabe piadas": choice([ "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
    "Por que o gato foi ao médico? Porque estava se sentindo mial-humorado.",
    "Por que o cachorro entrou na igreja? Para se tornar um cão pastor.",
    "Por que o computador foi à escola? Para melhorar seu sistema operacional.",
    "Por que a vaca foi ao espaço? Para encontrar a vaca-nauta.",
    "Por que o esqueleto não brigou com ninguém? Porque não tinha estômago para isso.",]),
    
    "quantos anos você tem": choice(["Eu sou uma IA, então não tenho idade, mas posso sempre aprender mais!", "Eu sou uma inteligência artificial, então não tenho idade!", "O inicio da minha criação foi em janeiro 2025, então tenho 1 ano!"]),
    "me ajuda com algo": choice(["Ótimo! Em que posso te ajudar?", "Sim! Em que posso te ajudar?", "Claro! Em que posso te ajudar?",]),
    "como você funciona": "Eu uso aprendizado de máquina para processar suas perguntas e fornecer respostas.",
    
    "suas habilidades": choice(["Posso responder perguntas, fornecer informações e ajudar com algumas tarefas simples!", "Posso te ajudar com informações, responder perguntas e realizar algumas tarefas simples!", "Posso fazer o que você me programar para fazer!",]),
    "me faça rir": "Por que os pássaros não usam Facebook? Porque já têm Twitter!",
    "quantos estados o Brasil tem": "O Brasil tem 26 estados e um Distrito Federal.",
    
    "como está o mercado de ações": "Eu não tenho dados em tempo real, mas você pode verificar em sites especializados em ações.",
    "receita de bolo de chocolate": "Aqui vai uma receita simples: Misture 2 xícaras de farinha, 1 xícara de cacau, 2 xícaras de açúcar, 3 ovos, 1 xícara de leite, 1/2 xícara de óleo e 1 colher de fermento. Asse por 30 minutos a 180°C.",
    "presidente do Brasil": "Atualmente, a presidente do Brasil é Luiz Inácio Lula da Silva.",
    "fuso horário do Brasil": "O Brasil possui vários fusos horários, variando de UTC-2 a UTC-5.",

    "aprender programação": "Você pode começar estudando lógica de programação, depois aprender linguagens como Python, JavaScript ou Java, e praticar criando projetos.",
    "habilidades em programação": "Pratique bastante, participe de projetos de código aberto, leia documentação, e estude algoritmos e estruturas de dados.",
    
    "me fale sobre inteligência artificial": "A inteligência artificial envolve o uso de máquinas e algoritmos para imitar funções cognitivas humanas, como aprendizado e tomada de decisões.",
    "quais são os tipos de inteligência artificial": "Os principais tipos de IA são IA reativa, IA com memória limitada, IA com teoria da mente e IA autossuficiente.",
    
    
    "como você pode me ajudar com estudos": "Eu posso fornecer explicações sobre conceitos, ajudar com perguntas difíceis ou sugerir recursos de estudo.",
    "qual é a fórmula da água": "A fórmula química da água é H2O.",
    "você sabe o que é programação orientada a objetos": "Sim, a programação orientada a objetos (POO) é um paradigma de programação que usa objetos e suas interações para projetar programas.",
    "você pode me ajudar a aprender inglês": "Claro! Eu posso te ajudar com vocabulário, gramática e até mesmo frases comuns em inglês.",
    "quais são os tipos de computação em nuvem": "Os principais tipos de computação em nuvem são IaaS, PaaS e SaaS.",
    
    "me fale sobre o Google": "O Google é uma empresa de tecnologia conhecida principalmente por seu motor de busca e outros serviços como YouTube e Google Maps.",

    "quanto tempo o sol leva para dar uma volta ao redor da galáxia": "O Sol leva cerca de 225 milhões de anos para dar uma volta completa ao redor da Via Láctea.",
    "quantos dias tem um ano": "Um ano tem 365 dias, exceto em anos bissextos, que têm 366 dias.",

    "quem é Albert Einstein": "Albert Einstein foi um físico teórico famoso por desenvolver a teoria da relatividade.",
    "quem é Steve Jobs": "Steve Jobs foi o cofundador da Apple Inc. e um dos maiores nomes da indústria de tecnologia.",
    "quem é a filha de quem te criou": "A filha de quem me construiu é a Heloisa Santana, ela tem mais 2 filhos, Felipe e Derick.",
    "quem criou você": "Eu fui criada por Anderson Rodrigues, programador especializado, junto com sua filha Heloisa Santana.",
    "quem é Anderson Rodrigues": "Anderson Rodrigues é um programador especializado em desenvolvimento de software, pai de três filhos e amigo de poucas pessoas.",

    "curiosidades": choice(["Você sabia que o cérebro humano tem capacidade de armazenar até 2,5 petabytes de informação?",
    "Você sabia que a língua inglesa tem mais de 170.000 palavras?",
    "Você sabia que o coração humano bate cerca de 3 bilhões de vezes durante a vida de uma pessoa?",]),
    
}
