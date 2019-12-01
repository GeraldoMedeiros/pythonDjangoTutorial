# pythonDjangoTutorial

Tutorial baseado em https://docs.djangoproject.com/pt-br/2.2/intro/tutorial01/

Imagem retirada de https://github.com/mezzoblue/csszengarden.com


## T03 - Tarefa 03 - Estudo sobre o Framework Django

1. Seguir o tutorial de Django da Parte 01 até a Parte 07.
https://docs.djangoproject.com/pt-br/2.2/intro/tutorial01/

2. Enviar o link do repositório no github com o código gerado a partir do tutorial.

3. Deve ter commits para as várias partes do tutorial.

4. Explique um pouco sobre o Framework Django e o padrão arquitetural MTV.
    O **Frameword Django**, assim como vários outros, ajuda aos desenvolvedores na criação de aplicações. No caso do Django, ele está voltado para o desenvolvimento de aplicações web utilisando a liguagem _Python_. Com a utilização do Django, muitas das tarefas básicas feitas por um desenvolvedor web são automatizadas, isso por o Django trazer uma grande maioria delas implementadas na sua estrutura interna, como por exemplo, a conexão com banco de dados. Assim como o Django-Python, uma grande parte das liguagens de programação têm seus vários frameworks com funções parecidas e alguns diferenciais também. Um dos pricipais objetivos dos frameworks é agilizar e automatizar tarefas, comumente necessárias aos desenvolvedores, com componentes já prontos para usar.
    O Django implementa um padrão de projeto denominado **MTV** (Model, Template, View) que estabelece uma estrutura básica de trabalho a ser seguida pelo desenvolvedores, não sendo obrigatório, mas faz parte das boas práticas de escrita de código e estruturação de aplicações.
    Para o padrão MTV, o **model** suporta as interações entre a aplicação e a camada de persistência de dados, dessa forma o Django tem um estrutura ORM (Object-relational Mapping) que dá suporte à diversos bancos de dados relacionais na parte de baixo, deixando uma API padrão na parte de cima utilizada pelo Django e mais facilmente compreendida pelo desenvolvedor que não tenha muita habilidade com bancos de dados;
    O **tempalte** é parte mais externa do padrão MTV, ela deve ser responsável pela interação com o usuário, coletando os dados digitados por eles nas páginas e exibindo os dados proveniente da aplicação. É importante ressaltar que esse padrão arquitetural não permite processamento de dados na template, sendo uma mau prática de programação a realização dos mesmo. A única resposabilidade do tempalte é exibir dados processados pelas views e coletar dados para a view processar.
    A **view** é a estrela da aplicação, é nela que devem ser impletadas todas as lógicas de negócios e regras de acesso ao sistema. Também devem ser feitos os tratamentos dos dados coletados a partir do template e preparação dos dados para o model. As várias classes e métodos padrões nos websites serão implementados ou invocados aqui. Em geral, cada view tem um template associado, isso promove uma facilidade interessante na manutenção da sua aplicação.
