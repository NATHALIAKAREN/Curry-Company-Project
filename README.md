# Problema de Negócio 📊

A Cury Company é uma empresa de tecnologia que desenvolveu um aplicativo inovador, conectando restaurantes, entregadores e clientes.

Através deste aplicativo, os clientes podem fazer pedidos de refeições em restaurantes cadastrados e receber suas refeições no conforto de suas casas por meio de entregadores também registrados no aplicativo da Cury Company.

A empresa opera em uma interface de negócios envolvendo restaurantes, entregadores e clientes, gerando um grande volume de dados relacionados a entregas, tipos de pedidos, condições climáticas, e avaliações dos entregadores. Apesar do crescimento constante das entregas, o CEO enfrenta o desafio de não ter uma visão completa dos principais Indicadores-chave de Desempenho (KPIs) necessários para tomar decisões estratégicas.

Você foi contratado como um Cientista de Dados para criar soluções de análise de dados para a entrega, mas antes de treinar algoritmos avançados, a empresa precisa consolidar os principais KPIs estratégicos em uma única ferramenta, permitindo que o CEO consulte esses indicadores e tome decisões simples, porém impactantes.

A Cury Company opera sob o modelo de negócio chamado Marketplace, atuando como intermediário entre três principais grupos de clientes: restaurantes, entregadores e consumidores. Para acompanhar o crescimento desses segmentos de negócios, o CEO deseja monitorar as seguintes métricas de crescimento:

## Do lado da empresa 🏢:

1. Quantidade de pedidos por dia.
2. Quantidade de pedidos por semana.
3. Distribuição dos pedidos por tipo de tráfego.
4. Comparação do volume de pedidos por cidade e tipo de tráfego.
5. A quantidade de pedidos por entregador por semana.
6. Localização central de cada cidade por tipo de tráfego.
   
## Do lado do entregador 🚚:

1. Faixa etária mais jovem e mais velha dos entregadores 👴🏼.
2. Condições de veículos, desde os piores 🚗 até os melhores 🏎️.
3. Avaliação média de cada entregador ⭐.
4. Avaliação média e desvio padrão por tipo de tráfego.
5. Avaliação média e desvio padrão por condições climáticas ☀️.
6. Os 10 entregadores mais rápidos em cada cidade 🏁.
7. Os 10 entregadores mais lentos em cada cidade 🐌.
   
## Do lado dos restaurantes 🍔:

1. Quantidade de entregadores únicos.
2. Distância média entre os restaurantes e os locais de entrega 📍.
3. Tempo médio de entrega por cidade ⏱️.
4. Tempo médio e desvio padrão de entrega por cidade e tipo de pedido.
5. Tempo médio e desvio padrão de entrega por cidade e tipo de tráfego.
6. Tempo médio de entrega durante festivais 🎉.

O objetivo deste projeto é fornecer um conjunto de gráficos e tabelas que apresentem essas métricas de forma eficaz para o CEO.

# 2. Premissas Assumidas para a Análise 🗓️

1. A análise foi realizada com dados coletados entre 11/02/2022 e 06/04/2022 📅.
2. O modelo de negócios considerado é o Marketplace 💼.
3. As três principais perspectivas de negócios são: Visão de transações de pedidos, visão de restaurantes e visão de entregadores 👀.

# 3. Estratégia da Solução 🚀

Desenvolvemos um painel estratégico que aborda as três principais perspectivas do modelo de negócios da empresa:

1. Visão do crescimento da empresa
   a. Pedidos por dia
   b. Porcentagem de pedidos por condições de trânsito 🚦
   c. Quantidade de pedidos por tipo e por cidade.
   d. Pedidos por semana
   e. Quantidade de pedidos por tipo de entrega
   f. Quantidade de pedidos por condições de trânsito e tipo de cidade.

2. Visão do crescimento dos restaurantes
   a. Quantidade de pedidos únicos.
   b. Distância média percorrida.
   c. Tempo médio de entrega durante festival e dias normais.
   d. Desvio padrão do tempo de entrega durante festivais e dias normais.
   e. Tempo de entrega médio por cidade.
   f. Distribuição do tempo médio de entrega por cidade.
   g. Tempo médio de entrega por tipo de pedido.

3. Visão do crescimento dos entregadores
   a. Idade do entregador mais velho e mais novo 👴🏼.
   b. Avaliação do melhor e do pior veículo 🚗.
   c. Avaliação média por entregador ⭐.
   d. Avaliação média por condições de trânsito.
   e. Avaliação média por condições climáticas.
   f. Tempo médido do entregador mais rápido 🏁.
   g. Tempo médio do entregador mais rápido por cidade.

# 4. Principais Insights de Dados 📈

1. A quantidade de pedidos apresenta sazonalidade diária, com uma variação de aproximadamente 10% entre dias consecutivos 📉.
2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito 🚗.
3. As maiores variações no tempo de entrega acontecem durante o clima ensolarado ☀️.
   
# 5. O produto final do projeto 🖥️

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: [Painel da Cury Company](https://curry-company-project-nathaliakaren.streamlit.app/) 💻.

# 6. Conclusão 📝

O objetivo deste projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão da Empresa, podemos concluir que o número de pedidos cresceu entre a semana 06 e a semana 13 do ano de 2022.

# 7. Próximo passos

1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócio
