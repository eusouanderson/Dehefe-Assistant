
from timeHow.tempo import obter_tempo_agora  # Importa a função do módulo tempo.py
from tempHow.temperatura import obter_temperatura_agora  # Importa a função do módulo temperatura.py
  # Importa a função do módulo soma.py
assistant_name = "Duda"

responses = {
    "ola": f"Olá! Eu sou a {assistant_name}. Como posso ajudar você?",
    "oi": f"Oi! Eu sou a {assistant_name}. Como posso ajudar você?",
    "tudo bem": "Estou sempre bem! Como posso ajudar você?",
    "tudo bem com você": "Estou sempre bem! Como posso ajudar você?",
    "qual a sua função": "Minha função é ser sua assistente virtual e ajudar no que for possível.",
    "quem é você": f"Eu sou a {assistant_name}, sua assistente virtual.",
    "quem sou eu": "Você é uma pessoa incrível!",
    "qual é a sua idade": "Eu sou uma inteligência artificial, não tenho idade, mas posso sempre aprender mais!",
    "temperatura": "Calculando pela temperatura do sistema, é " + obter_temperatura_agora(),
    "como esta": "Oi, estou bem, obrigado por perguntar!",
    "hora agora": "Agora são " + obter_tempo_agora(),
    "sair": f"Até logo! Foi um prazer ajudar você.",
    "bom dia": f"Bom dia! Como posso ajudá-la hoje?",
    "boa tarde": f"Boa tarde! Em que posso lhe ser útil?",
    "boa noite": f"Boa noite! Espero que tenha um ótimo descanso.",
    "como você está": f"Eu sou uma inteligência artificial, então não tenho sentimentos, mas obrigada por perguntar!",
    "meu nome é": "Legal, prazer em te conhecer!",
    "qual e o seu nome": f"Eu sou a {assistant_name}, sua assistente virtual.",
    "como você pode me ajudar": "Eu posso responder perguntas, fornecer informações e realizar algumas tarefas simples!",
    "qual é a sua função": "Minha função é ser sua assistente virtual, pronta para ajudar no que for possível.",
    "onde você mora": "Eu sou uma inteligência artificial, não tenho um local físico!",
    "você gosta de música": "Eu não tenho preferências, mas posso te ajudar a encontrar músicas ou informações sobre artistas!",
    "qual é a sua cor favorita": "Minha cor favorita é rosa!",
    "quantos anos você tem": "Eu sou uma IA, então não tenho idade, mas posso sempre aprender mais!",
    "me ajuda com algo": "Claro! Em que posso te ajudar?",
    "quem fez você": "Eu fui criada por Anderson Rodrigues, programador especializado.",
    "como você funciona": "Eu uso aprendizado de máquina para processar suas perguntas e fornecer respostas.",
    "quais são suas habilidades": "Posso responder perguntas, fornecer informações e ajudar com algumas tarefas simples!",
    "você sabe piadas": "Claro! Por que a programadora foi ao médico? Porque ela tinha um bug!",
    "me faça rir": "Por que os pássaros não usam Facebook? Porque já têm Twitter!",
    "qual é a capital da França": "A capital da França é Paris.",
    "qual é a capital da Espanha": "A capital da Espanha é Madri.",
    "qual é a capital da Alemanha": "A capital da Alemanha é Berlim.",
    "qual é a capital da Itália": "A capital da Itália é Roma.",
    "qual é a capital do Japão": "A capital do Japão é Tóquio.",
    "qual é a capital da Rússia": "A capital da Rússia é Moscou.",
    "qual é a capital da China": "A capital da China é Pequim.",
    "qual é a capital do Brasil": "A capital do Brasil é Brasília.",
    "qual é a capital dos Estados Unidos": "A capital dos Estados Unidos é Washington.",
    "qual é a distância da Terra à Lua": "A distância média da Terra à Lua é cerca de 384.400 quilômetros.",
    "quem descobriu o Brasil": "O Brasil foi descoberto em 1500 pelo explorador Pedro Álvares Cabral.",
    "qual é o maior planeta do sistema solar": "O maior planeta do sistema solar é Júpiter.",
    "quantos estados o Brasil tem": "O Brasil tem 26 estados e um Distrito Federal.",
    "qual é a moeda do Brasil": "A moeda oficial do Brasil é o Real (BRL).",
    "como está o mercado de ações": "Eu não tenho dados em tempo real, mas você pode verificar em sites especializados em ações.",
    "receita de bolo de chocolate": "Aqui vai uma receita simples: Misture 2 xícaras de farinha, 1 xícara de cacau, 2 xícaras de açúcar, 3 ovos, 1 xícara de leite, 1/2 xícara de óleo e 1 colher de fermento. Asse por 30 minutos a 180°C.",
    "presidente do Brasil": "Atualmente, a presidente do Brasil é Luiz Inácio Lula da Silva.",
    "fuso horário do Brasil": "O Brasil possui vários fusos horários, variando de UTC-2 a UTC-5.",
    "como faço para aprender programação": "Você pode começar estudando lógica de programação, depois aprender linguagens como Python, JavaScript ou Java, e praticar criando projetos.",
    "como posso melhorar minhas habilidades em programação": "Pratique bastante, participe de projetos de código aberto, leia documentação, e estude algoritmos e estruturas de dados.",
    "qual é o maior rio do mundo": "O maior rio do mundo é o Amazonas, localizado na América do Sul.",
    "qual é a montanha mais alta do mundo": "A montanha mais alta do mundo é o Monte Everest, com 8.848 metros.",
    "me fale sobre inteligência artificial": "A inteligência artificial envolve o uso de máquinas e algoritmos para imitar funções cognitivas humanas, como aprendizado e tomada de decisões.",
    "quais são os tipos de inteligência artificial": "Os principais tipos de IA são IA reativa, IA com memória limitada, IA com teoria da mente e IA autossuficiente.",
    "qual é a velocidade da luz": "A velocidade da luz no vácuo é de aproximadamente 299.792.458 metros por segundo.",
    "qual é a maior cidade do mundo": "A maior cidade do mundo em termos de população é Tóquio, Japão.",
    "como você pode me ajudar com estudos": "Eu posso fornecer explicações sobre conceitos, ajudar com perguntas difíceis ou sugerir recursos de estudo.",
    "qual é a fórmula da água": "A fórmula química da água é H2O.",
    "você sabe o que é programação orientada a objetos": "Sim, a programação orientada a objetos (POO) é um paradigma de programação que usa objetos e suas interações para projetar programas.",
    "você pode me ajudar a aprender inglês": "Claro! Eu posso te ajudar com vocabulário, gramática e até mesmo frases comuns em inglês.",
    "quais são os tipos de computação em nuvem": "Os principais tipos de computação em nuvem são IaaS, PaaS e SaaS.",
    "quem é Albert Einstein": "Albert Einstein foi um físico teórico famoso por desenvolver a teoria da relatividade.",
    "me fale sobre o Google": "O Google é uma empresa de tecnologia conhecida principalmente por seu motor de busca e outros serviços como YouTube e Google Maps.",
    "quem é Steve Jobs": "Steve Jobs foi o cofundador da Apple Inc. e um dos maiores nomes da indústria de tecnologia.",
    "quanto tempo o sol leva para dar uma volta ao redor da galáxia": "O Sol leva cerca de 225 milhões de anos para dar uma volta completa ao redor da Via Láctea.",
    "qual é a maior floresta do mundo": "A maior floresta do mundo é a Floresta Amazônica, localizada principalmente no Brasil.",
    "qual é o animal mais rápido do mundo": "O animal mais rápido do mundo é o guepardo, que pode alcançar velocidades de até 110 km/h.",
    "qual é o maior oceano do mundo": "O maior oceano do mundo é o Oceano Pacífico.",
    "quem é a filha de quem te criou": "A filha de quem me construiu é a Heloisa Santana, ela tem mais 2 filhos, Felipe e Derick.",
    "quem criou você": "Eu fui criada por Anderson Rodrigues, programador especializado, junto com sua filha Heloisa Santana.",
    "quem são seus irmãos": "Tenho três irmãos: Heloisa, Felipe e Derick.",
    "quem é Anderson Rodrigues": "Anderson Rodrigues é um programador especializado em desenvolvimento de software, pai de três filhos e amigo de poucas pessoas.",
}
