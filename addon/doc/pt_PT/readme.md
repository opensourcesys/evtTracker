# Rastreador de eventos #

* Author: Joseph Lee, Thiago Seus

Este extra produz informação sobre objectos pelos quais foram disparados
eventos. As propriedades registadas no modo de registo de depuração incluem
tipo de objecto, nome, função, evento, módulo de aplicação, e informação
específica da API de acessibilidade, tal como accName para objecto
IAccessible e Automation Id para objectos UIA.

Notas:

* Este extra foi concebido para programadores e utilizadores avançados que
  necessitem de acompanhar eventos provenientes de aplicações e vários
  controlos.
* Para utilizar o extra, o NVDA deve estar em modo de depuração (configurado
  a partir de definições gerais/nível de registo, ou reiniciar com o registo
  de depuração activado).
* Pode acontecer que extras carregados antes do Event Tracker não passem o
  evento para outros extras, incluindo o Event Tracker. Se isto acontecer, o
  Event Tracker não será capaz de registar eventos.
* Os eventos são tratados a partir de plugins globais, módulos de aplicação,
  interceptores de árvores, e objectos do NVDA, por esta ordem.

## Eventos e suas informações

Os seguintes eventos são rastreados e registados:

* Manipulação do foco: ganhar foco, perder foco, foco introduzido, primeiro
  plano
* Alterações: nome, valor, estado, descrição, região de procedência
* Other events: alert
* UIA events: controller for, drag drop and drop target effects, element
  selected, item status, layout invalidated, notification, system alert,
  text change, tooltip open, window open

Para cada evento, serão registadas as seguintes informações:

* Nome do evento
* Objecto
* Nome do objecto
* Papel do objecto
* Valor do objecto ou estado dependendo dos eventos
* Módulo de aplicação
* Para objectos acessíveis ao IA: nome de acesso, identificação de
  descendente
* For UIA objects: Automation Id, class name, notification properties if
  recording notification event information, child count for layout
  invalidated event, properties for item status, drag drop, and drop target
  effect if defined

You can also assign a gesture to view the events on a list (NVDA
menu/Preferences/Input gestures, Event Tracker category). The list saves up
to 100 latest events processed.

If you find this add-on useful, please [review it][1] in the NVDA Add-on
Store.

## Version 25.1.0

* NVDA 2025.1 compatibility.
* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Made the add-on code more robust with help from Pyright (a Python static
  type checker).
* NVDA will record actual control role name instead of integers when
  reporting events.

## Version 24.1.0

* NVDA 2024.1 compatibility.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* Alert event (mostly for IAccessible objects) will be tracked.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.12

* Added events list dialog (command unassigned) to list up to 100 recent
  events recorded by the add-on (Thiago Seus).
* Additional event information such as UIA notification properties are
  recorded at the same time as events.

## Version 22.10

* NVDA 2022.2 or later is required due to security.
* The following UIA property changes are tracked: drag drop effect, drop
  target effect.
* UIA item status property text is logged.
* NVDA will no longer play error tones or appear to do nothing if an object
  does not define a window class name.

## Version 22.06

* NVDA 2021.3 or later is required due to security.

## Versão 21.10

* É necessário o NVDA 2021.2 ou posterior devido a alterações do NVDA que
  afectam este extra.
* O evento invalidado pela UIA será rastreado.
* O papel do objecto e a informação sobre os estados assemelhar-se-ão a
  informações de desenvolvimento encontradas em versões mais recentes da
  NVDA.

## Versão 21.07

* Lançamento inicial.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
