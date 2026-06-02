# Rastreador de eventos

* Author: Joseph Lee, Thiago Seus

Este extra produz informação sobre objectos pelos quais foram disparados eventos. As propriedades registadas no modo de registo de depuração incluem tipo de objecto, nome, função, evento, módulo de aplicação, e informação específica da API de acessibilidade, tal como accName para objecto IAccessible e Automation Id para objectos UIA.

Notas:

* Este extra foi concebido para programadores e utilizadores avançados que necessitem de acompanhar eventos provenientes de aplicações e vários controlos.
* Para utilizar o extra, o NVDA deve estar em modo de depuração (configurado a partir de definições gerais/nível de registo, ou reiniciar com o registo de depuração activado).
* Pode acontecer que extras carregados antes do Event Tracker não passem o evento para outros extras, incluindo o Event Tracker. Se isto acontecer, o Event Tracker não será capaz de registar eventos.
* Os eventos são tratados a partir de plugins globais, módulos de aplicação, interceptores de árvores, e objectos do NVDA, por esta ordem.

## Eventos e suas informações

Os seguintes eventos são rastreados e registados:

* Manipulação do foco: ganhar foco, perder foco, foco introduzido, primeiro plano
* Alterações: nome, valor, estado, descrição, região de procedência
* Other events: alert
* UIA events: controller for, drag drop and drop target effects, element selected, item status, layout invalidated, notification, system alert, text change, tooltip open, window open

Para cada evento, serão registadas as seguintes informações:

* Nome do evento
* Objecto
* Nome do objecto
* Papel do objecto
* Valor do objecto ou estado dependendo dos eventos
* Módulo de aplicação
* Para objectos acessíveis ao IA: nome de acesso, identificação de descendente
* For UIA objects: Automation Id, class name, notification properties if recording notification event information, child count for layout invalidated event, properties for item status, drag drop, and drop target effect if defined

You can also assign a gesture to view the events on a list (NVDA menu/Preferences/Input gestures, Event Tracker category). The list saves up to 100 latest events processed.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
